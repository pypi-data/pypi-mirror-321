import regex, re, os, shutil, argparse, requests
from subprocess import call
import xml.etree.ElementTree as etree
from string import punctuation
from tqdm import tqdm
from bs4 import BeautifulSoup
from torch.utils.data import random_split
from bioc import biocjson



def ncbi_to_brat(path_from, path_to):
    mkdir(path_to)
    for root, dirs, files in os.walk(path_from):
        for file in files:
            with open(root+"/"+file) as inp:
                new_root = file.replace(".txt", "")
                mkdir(path_to+"/"+new_root)
                for line in inp:
                    if prefix := regex.match(r"(\d+)\|(\w)\|(.+)", line):
                        doc_id = prefix.group(1)
                        annotations = []
                        if prefix.group(2) == "t" : text = prefix.group(3)
                        elif prefix.group(2) == "a" :
                            text += "\n" + prefix.group(3)
                            with open(f"{path_to}/{new_root}/{doc_id}.txt", "w") as txt: txt.write(text)
                        else: raise ValueError(f"Uknown prefix : {prefix.group(2)}")
                    elif line == "\n":
                        try: save_annotations(annotations=annotations, path=f"{path_to}/{new_root}/{doc_id}.ann")
                        except UnboundLocalError: pass
                    else:
                        doc_id, start, end, token, ne, mesh_id = line.strip().split("\t")
                        annotations.append({"NE":ne, "start":start, "end":end, "token":token, "nel":[{"DB":"MESH", "id":mesh_id}]})
            save_annotations(annotations=annotations, path=f"{path_to}/{new_root}/{doc_id}.ann")



def ieer_to_brat(path_from, path_to):
    """Transform your corpus from the ieer format to the Bacteria Biotope (BB) format."""
    root = path_from+"/tmp"
    os.mkdir(root)
    replacements = {"&AMP;": "and", "&UR;":"", "&LR;":""}
    for file in filter(lambda name:os.path.isfile(f"{path_from}/{name}") and name != "README", os.listdir(path_from)):
        with open(f"{path_from}/{file}") as inp, open(f"{root}/{file}", "w") as out:
            for line in inp:
                for k, v in replacements.items(): line = line.replace(k, v)
                out.write(regex.sub("<e_([a-z]+)>", "</b_\g<1>>", line))
    mkdir(path_to)
    for file in os.listdir(root):
        tree = etree.parse(root+"/"+file)
        docs = tree.getroot()
        len_opening_tag, len_ending_tag = len("<TEXT>"),-len("</TEXT>")
        for doc in docs:
            for element in doc:
                if element.tag == "DOCNO":
                    file_num = element.text
                elif element.tag == "BODY":
                    try: headline, body = element
                    except ValueError: headline, body = etree.fromstring("<empty> </empty>"), element[0]
                    text = headline.text + "".join(body.itertext())
                    body_str = etree.tostring(body)[len_opening_tag:len_ending_tag].decode()
                    body_str = regex.sub(r"<([A-Z]+)>([^<]+)</\1>", r"\2", body_str) #remove unnecessary tags
                    annotations_tags  = get_tags(body_str)
                    shift = len(headline.text)
                    annotations = []
                    for tag in annotations_tags:
                        start = tag["start"] + shift
                        end = start + len(tag["token"])
                        shift -= tag["end"] - tag["start"] - len(tag["token"])
                        annotations.append({"NE":tag["NE"], "start":start, "end":end, "token":tag["token"]})
            with open(f"{path_to}/{file_num.strip()}.txt", "w") as out: out.write(text)
            save_annotations(annotations, f"{path_to}/{file_num.strip()}.ann")
    shutil.rmtree(root)


def biocreative_to_brat(path_from, path_to):

    mkdir(path_to)
    for root, dirs, files in os.walk(path_from):
        for file in files:
            new_root = path_to+"/"+regex.sub("\..+", "", file)
            mkdir(new_root)
            print(root, file)
            with open(root+"/"+file) as inp:
                data = biocjson.load(inp)
                for doc in data.documents:
                    text = ""
                    annotations = []
                    for passage in doc.passages:
                        for ann in filter(lambda a:a.text, passage.annotations):
                            entity_type = ann.infons["type"]
                            start = len(text)+ann.locations[0].offset-passage.offset
                            end = start + ann.locations[0].length
                            entity = ann.text
                            concepts = ann.infons.get("identifier", "")
                            annotations.append({"NE":entity_type, "start":start, "end":end, "token":entity, "nel":[]})
                            for concept in concepts.split(","):
                                try:
                                    db, concept_id = concept.split(":")
                                    annotations[-1]["nel"].append({"DB":db, "id":concept_id})
                                except ValueError as ve:
                                    assert str(ve) == "not enough values to unpack (expected 2, got 1)"
                                    continue
                        text += passage.text + "\n"
                    with open(f"{new_root}/{doc.id}.txt", "w") as out: out.write(text)
                    save_annotations(annotations, f"{new_root}/{doc.id}.ann")


def ontonotes_to_brat(path_from, path_to):
    iob_to_brat(path_from=path_from, path_to=path_to,
                 token_column=1,
                 ner_column=10,
                 columns_sep="\t",
                 doc_sep="\n",
                 phrase_sep="")


def multinerd_to_brat(path_from, path_to):
    iob_to_brat(path_from=path_from, path_to=path_to,
                 token_column=1,
                 ner_column=2,
                 columns_sep="\t",
                 doc_sep="\n",
                 phrase_sep="",
                 nel_db_and_columns={"BabelNet":3, "Wikidata":4, "Wikipedia":5})


def gmb_to_brat(path_from, path_to, token_column=0, ner_column=3, columns_sep="\t"):
    """Transform your corpus from the gmb format to the Bacteria Biotope (BB) format."""
    mkdir(path_to)
    for root, dirs, files in os.walk(path_from):
        for dir in dirs:
            new_file = regex.match("d[0-9]{4}", dir)
            if new_file:
                new_root = path_to+"/"+regex.search("p[0-9]{2}", root).group()
                new_file = new_file.group()
                mkdir(new_root)
                text = copy_text(path_from="/".join([root, dir, "en.raw"]), path_to=new_root + "/" + new_file + ".txt")
                annotations = [{"NE":"", "start":0, "token":"", "end":0}]
                with open("/".join([root, dir, "en.tags"])) as all_annotations:
                    for annotation in filter(lambda line:line!="\n", all_annotations):
                        tags = annotation.split(columns_sep)
                        token, entity = tags[token_column].replace("~", " "), tags[ner_column]
                        if entity != "O":
                            start = text.find(token, annotations[-1]["end"])
                            end = start+len(token)
                            annotations.append({"NE":entity, "start":start, "end":end, "token":token})
                del annotations[0]
                annotations = realign_annotations(annotations, text)
                save_annotations(annotations, new_root + "/" + new_file + ".ann")


def geovirus_to_brat(path_from, path_to):
    """Transform your corpus from the geovirus format to the Bacteria Biotope (BB) format."""
    reformat = {"location":"NE", "toponym":"NE", "start":"start", "end":"end", "phrase":"token", "name":"token"}
    mkdir(path_to)
    for file in filter(lambda x: os.path.isfile(path_from+"/"+x), os.listdir(path_from)):
        start_index = 1 if "GeoVirus" in file else 0
        new_root = path_to + "/" + file.replace(".xml", "")
        mkdir(new_root)
        tree = etree.parse(path_from+"/"+file)
        articles = tree.getroot()
        for i, article in enumerate(articles, 115):
            annotations = []
            for element in article:
                if element.tag == "text":
                    with open(f"{new_root}/{i}.txt", "w") as out:
                        out.writelines(element.text)
                elif element.tag in ["toponyms", "locations"]:
                    for entity in element:
                        annotation = {"NE":element.tag}
                        for info in entity:
                            if info.tag in reformat.keys():
                                annotation[reformat[info.tag]] = info.text
                            elif info.tag == "gaztag":
                                annotation["DB"] = "GeoNames"
                                annotation["id"] = info.attrib["geonameid"]
                            elif info.tag == "page" and info.text !="N/A":
                                annotation["DB"] = "GeoNames"
                                wikipage = BeautifulSoup(requests.get(info.text).content, "html.parser")
                                hrefs = wikipage.find_all("span", text="Wikidata item")
                                if len(hrefs) == 1:
                                    wikidata = BeautifulSoup(requests.get(hrefs[-1].parent["href"]).content, "html.parser")
                                    geoname_id = wikidata.find_all(href=lambda x: x and x.startswith("https://www.geonames.org/"))
                                    if len(geoname_id) == 1:
                                        annotation["id"] = geoname_id[0].text
                        if start_index :
                            for index in ["start", "end"]: annotation[index] = int(annotation[index]) - start_index
                        annotations.append(annotation)
            save_annotations(annotations=annotations, path=f"{new_root}/{i}.ann")


def malwaretextdb_to_brat(path_from, path_to):
    mkdir(path_to)
    copy_text_files(path_from=path_from, path_to=path_to)
    fix_unicode_shift_alignment(path_to)
    fix_pdf_names(path_to)
    copy_nel_annotations(path_from=path_from,
                         path_to=path_to,
                         NEL_id="A",
                         NEL_source="MAEC",
                         NEL_format=({"name":"id_NEL", "prefix":"", "suffix":""},
                                     {"name":"", "prefix":"", "suffix":""},
                                     {"name":"id_NER", "prefix":"", "suffix":""},
                                     {"name":"id_in_source", "prefix":"", "suffix":""}))


def cadec_to_brat(path_from, path_to):
    mkdir(path_to)
    copy_text_files(path_from=path_from+"/text", path_to=path_to)
    paths_nel = [path_from+"/"+directory for directory in filter(lambda x: os.path.isdir(path_from+"/"+x) and x not in [".DS_Store", "original", "text"], os.listdir(path_from))]
    join_annotation_files(path_ner=path_from+"/original", paths_nel=paths_nel, path_to=path_to)


def wikineural_to_brat(path_from, path_to):
    iob_to_brat(path_from=path_from, path_to=path_to, token_column=1, ner_column=2, columns_sep="\t", doc_sep="\n", phrase_sep="")


def conll_to_brat(path_from, path_to):
    iob_to_brat(path_from=path_from, path_to=path_to,
                 token_column=0,
                 ner_column=-1,
                 columns_sep=" ",
                 doc_sep="-DOCSTART- -X- -X- O\n",
                 phrase_sep="\n")


def wnut_to_brat(path_from, path_to):
    iob_to_brat(path_from=path_from, path_to=path_to,
                 token_column=0,
                 ner_column=-1,
                 columns_sep="\t",
                 doc_sep="\n",
                 phrase_sep="")


def mit_to_brat(path_from, path_to):
    iob_to_brat(path_from=path_from, path_to=path_to,
                 token_column=1,
                 ner_column=-0,
                 columns_sep="\t",
                 doc_sep="\n",
                 phrase_sep="")


def iob_to_brat(path_from, path_to, token_column, ner_column, columns_sep, doc_sep, phrase_sep, nel_db_and_columns=None):
    """
    Transform your corpus from the CONLL or similar format to the Bacteria Biotope (BB) format.
    The corpus should consist of text files where each line is the annotation.
    :param path_from : str
        path to initial annotations
    :param path_to : str
        path to save final annotations
    :param token_column : int
        index of a column with a token
    :param ner_column : int
        index of a column with a NER annotation
    :param nel_db_and_columns : dict -> str:int
        database/ontology/etc. names and indeces of columns with NEL annotations (if any)
    :param columns_sep : str
        columns separator symbol
    :param doc_sep : str
        documents separator symbol
    :param phrase_sep : str
        phrase separator symbol
    Example:
        CRICKET NNP I-NP O
        - : O O
        LEICESTERSHIRE NNP I-NP I-ORG
        TAKE NNP I-NP O
        OVER IN I-PP O
        ...
    """
    mkdir(path_to)
    for root, dirs, files in os.walk(path_from):
        for file in files:
            new_root = path_to+"/"+regex.sub("\..+", "", file)
            mkdir(new_root)
            with open(root+"/"+file) as inp:
                count = 0
                text = [""]
                annotations = []
                for line in tqdm(inp):
                    if line == doc_sep:
                        with open(f"{new_root}/{count}.txt", "w") as out:
                            out.writelines(text)
                        annotations = realign_annotations(annotations, "".join(text))
                        save_annotations(annotations, f"{new_root}/{count}.ann")
                        count += 1
                        text = [""]
                        annotations = []
                    elif line == phrase_sep:
                        if end_of_the_paragraph(text[-1]):
                            text.append(line)
                    else:
                        info = line.strip().split(columns_sep)
                        token, entity = info[token_column], info[ner_column]
                        text.append(" "*need_space_before(text[-1], token))
                        text.append(token)
                        if entity not in "O_":
                            start = len("".join(text[:-1]))
                            end = start+len(token)
                            annotations.append({"NE": entity[2:], "start":start, "end":end, "token":token})
                            if nel_db_and_columns and entity.startswith("B"):
                                nel = []
                                for db, i in nel_db_and_columns.items():
                                    try: nel.append({"DB":db, "id":info[i]})
                                    except IndexError: continue #Sometimes you have not alignments with all the indicated sources
                                annotations[-1].update({"nel":nel})
    clean(path_to)


def join_ner_nel(ner, nel):
    final_annotations = []
    for incompleted_annotation in ner:
        for i, addition in enumerate(filter(bool, nel)):
            if incompleted_annotation["start"] == addition["start"] and incompleted_annotation["token"].startswith(addition["token"]):
                final_annotations.append(incompleted_annotation|{"DB":addition["DB"], "id":addition["id"]})
                nel[i] = None
    return final_annotations


def brat_to_iob(path_from, path_to, rename_entities_types=dict(), token_column=0, ner_column=1, columns_sep=" ", phrase_sep="\n", nel_annotation_start="#", annotations_extention=".ann", text_extention=".txt", split_data={
    'train':0.8, 'validation':0.1, 'test':0.1}):

    def next_(iterator):
        try: return next(iterator)
        except StopIteration: pass

    for root, dirs, files in os.walk(path_from):
        if not(dirs): dirs = ["dataset"]
        result = {dir:{"input":[], "labels":[]} for dir in dirs}
        for file in files:
            if file.endswith(text_extention):
                with open(root+"/"+file) as doc: lines = doc.readlines()
                text = "".join(lines)
                spaces = [re.finditer("\s+", line) for line in lines]
                inputs = [re.split(r'([!"$%\')+,-./:;<=>?\]}~]*)[\s]+(["\'(\[{]*)', i) for i in lines]
                inputs = [[token for token in line if token] for line in inputs]
                gold = [["O"] * len(line) for line in inputs]
                end_of_token_indeces = []
                l = 0
                for line, space_indeces in zip(inputs, spaces):
                    nearest_space = next(space_indeces)
                    shift = l
                    if nearest_space.start() == 0:
                        l += nearest_space.end()
                        nearest_space = next_(space_indeces) or nearest_space
                    end_of_token_indeces.append([])
                    for token in line:
                        l+=len(token)
                        end_of_token_indeces[-1].append(l)
                        while nearest_space.start() + shift == l:
                            l += nearest_space.end() - nearest_space.start()
                            nearest_space = next_(space_indeces) or nearest_space
                for i, end in enumerate(reversed(end_of_token_indeces)):
                    if end:
                        last_non_empty = -(i+1)
                        break
                assert end_of_token_indeces[last_non_empty][-1] == len(text.rstrip())
                with open(root+"/"+file.replace(text_extention, annotations_extention)) as annotations:
                    for annotation in annotations:
                        if not(annotation.startswith(nel_annotation_start)):
                            _, info, token = annotation.strip().split("\t")
                            entity = info[:info.index(" ")]
                            rename_entities_types[entity] = rename_entities_types.get(entity, entity.upper())
                            relevant_indeces = info[info.index(" ")+1:] #we have a NE before the first whitespace
                            for token_piece in relevant_indeces.split(";"):
                                start, end = token_piece.split()
                                found, finished = False, False
                                for i, line in enumerate(end_of_token_indeces):
                                    if not finished:
                                        for j, index in enumerate(line):
                                            if not(found):
                                                if index > int(start):
                                                    gold[i][j] = "B-"+rename_entities_types[entity]
                                                    found = True
                                            elif not(finished):
                                                if index <= int(end):
                                                    gold[i][j] = "I-"+rename_entities_types[entity]
                                                else:
                                                    finished = True
                                                    break
                for dir in dirs:
                    if dir in root or dirs == ["dataset"]:
                        result[dir]["input"] += [inputs]
                        result[dir]["labels"] += [gold]
        mkdir(path_to)
        import joblib
        if split_data:
            dataset = [(i, l) for sample in result.values() for i, l in zip(*sample.values())]
            dataset_size = len(dataset)
            sizes = {name:int(dataset_size*proportion) for name, proportion in split_data.items()}
            sizes["test"] = sizes.get("test", 0) + dataset_size - sum(sizes.values())
            splits = random_split(dataset, [v for k, v in sorted(sizes.items())])
            result = {name:dict(zip(["input", "labels"], zip(*list(split)))) for name, split in zip(sorted(sizes), splits)}
        for file, annotations in result.items():
            with open(path_to+"/"+file+".txt", "w") as outp:
                for text_of_tokens, text_of_entities in zip(annotations["input"], annotations["labels"]):
                    for tokens, entities in zip(text_of_tokens, text_of_entities):
                        for token, entity in zip(tokens, entities):
                            ordered = ["", ""]
                            token = token.replace("\n", "")
                            if token:
                                ordered[token_column] = token
                                ordered[ner_column] = entity
                                outp.write(columns_sep.join(ordered)+"\n")
                        outp.write(phrase_sep)


def complete_unicode_half_symbols(string, new="??"):
    """
    This function replace them by the indicated 'new' character chain ('??' by default).
    """
    return string.replace("\U00100194", new)


def fix_unicode_shift_alignment(path, **args):
    """
    If you have a half of a unicode symbol in your text, it will cause an index shift as it is one symbol shorter.
    Replace these half-characters to avoid it.
    :param path : str
    path to problematic files
    :param **args
        new - character chain by which corrupted unicode symbols will be replaced.
    """
    for file in filter(lambda f:f.endswith(".txt"), os.listdir(path)):
        with open(path_to+"/"+file, "r+") as f:
            lines = [complete_unicode_half_symbols(line, **args) for line in f]
            f.seek(0)
            f.truncate()
            f.writelines(lines)


def fix_pdf_names(path):
    """Remove an excess pdf extention in text files in the indicated path. Ex. File.pdf.txt -> File.txt"""
    for root, dirs, files in os.walk(path):
        for file in filter(lambda f:f.endswith(".txt"), files):
            full_path = root+"/"+file
            os.rename(full_path, full_path.replace(".pdf", ""))


def realign_annotations(annotations, text):
    """
    Join multiple annotations of one entity into one annotation.
    :param annotations : list of dict
    Example of realignment:
          [...,
          {"type":"MISC", "start":84, "end":88, "entity":"West"},
          {"type":"MISC", "start":89, "end":95, "entity":"Indian"},
          ...]
                                     ↓
        [...,
        {"type":"MISC", "start":84, "end":95, "entity":"West Indian"},
        ...]
    """
    for i, annotation in enumerate(annotations):
        distance = annotation["start"] - annotations[i-1]["end"]
        if (distance == 0 or (distance == 1 and text[annotation["start"]-1])) and annotation["NE"] == annotations[i-1]["NE"]:
            annotations[i]["token"] = annotations[i-1]["token"]+" "*distance + annotation["token"]
            annotations[i]["start"] = annotations[i-1]["start"]
            if nel := annotations[i-1].get("nel"): annotations[i]["nel"] = nel
            annotations[i-1] = dict()
    return list(filter(lambda x: x, annotations))


def join_annotation_files(path_ner, paths_nel, path_to):
    """
    Join multiple annotations files in one.
    :param path_ner: str
        Path containing files with NER annotations.
    :param path_nel: iterable of str
        List of paths containing files with NEL annotations (each path with different annotation type) for the same files as with NER annotations.
    :param path_to: str
        Path to save aggregative annotation files.
    """
    mkdir(path_to)
    known_databases = {"meddra":"MedDRA", "sct":"SNOMED_CT"}
    for root, _, files in os.walk(path_ner):
        for file in files:
            with open(path_to+"/"+file, "w") as annotations:
                with open(root+"/"+file) as ner_annotations:
                    for annotation in filter(lambda line: not(line.startswith("#")), ner_annotations):
                        annotations.write(annotation)
                nel_annotations = []
                for path in paths_nel:
                    db = known_databases[path.split("/")[-1]]
                    with open(path+"/"+file) as some_nel_annotations:
                        for annotation in some_nel_annotations:
                            i, ref, *rest = annotation.split()
                            nel_annotations.append({"db":db, "NE id":i[1:], "reference":ref})
                            if rest[0] == "|":
                                additional_refs = filter(lambda x: x.startswith("or"), "".join(rest).split("|")) #multiple annotations in one line (TT6	102498003 | Agony | or 76948002|Severe pain| 260 265	agony)
                                for ref in additional_refs:
                                    nel_annotations.append({"db":db, "NE id":i[1:], "reference":ref[2:]})
                for i, annotation in enumerate(sorted(nel_annotations, key=lambda annotation:annotation["NE id"]), 1):
                    annotations.write(f"N{i}\t{annotation['db']} Annotation:{annotation['NE id']} Referent:{annotation['reference']}\n")


def save_annotations(annotations, path):
    """
    Save annotations in an indicated location.
    :param annotations : list of dict
    :param path: str
    Each dictionnary should contain folowwing keys: 'NE' - NE tag, 'start' - start index in the text, 'end' - end index in the text, 'token' - characters chain in the text.
    For NEL annotations it should also contain 'DB' - database/ontology/etc. with which we align and 'id' - id in this knowledge base.
    Annotation example - {"NE":"toponym", "start":1, "end":6, "token":"Syrian Arab Republic", "nel":[{"DB":"GeoNames", "id":"163843"}]}
    """
    with open(path, "w") as ann:
        nel = []
        for i, annotation in enumerate(sorted(annotations, key=lambda a:int(a["start"])), 1):
            ann.write(f"T{i}\t{annotation['NE']} {annotation['start']} {annotation['end']}\t{annotation['token']}\n")
            for norm in annotation.get("nel", []):
                nel.append(f"{norm.get('DB')} Annotation:T{i} Referent:{norm.get('id')}")
        for i, annotation in enumerate(filter(lambda annotation: not(annotation.endswith("Referent:None")), nel), 1):
            ann.write(f"N{i}	{annotation}\n")


def copy_nel_annotations(path_from, path_to, NER_id="T", NEL_id="N", NEL_source="", NEL_format=({"name":"id_NEL", "prefix":"", "suffix":""}, {"name":"source", "prefix":"", "suffix":""}, {"name":"id_NER", "prefix":"Annotation:", "suffix":""}, {"name":"id_in_source", "prefix":"Referent:", "suffix":""})):
    """
    copy annotations from similar format
    :param path_from : str
    path to files with annotations
    :param path_to : str
    path to copy annotations
    :param NER_id : str
    part of annotation id that indicates it is a NE type annotation
    :param NEL_id : str
    part of annotation id that indicates it is a NEL annotation
    :param NEL_source : str
    DB used for NEL
    :param NEL_format : tuple of dicts
    format of a NEL annotation.
    Each dict should describe each annotation element after splitting the annotation line by space symbols.
    Each such description is a dictionnary with the following components:
        an annotation 'name', 'prefix' and 'suffix' as keys
        and
        an element name (str), irrelevant prefix (str) ans suffix (str) as values.
        The element name should be a value from the following list :
        - id_NEL (annotation id),
        - source (relevant DB/ontology),
        - id_NER (id of a relevant entity type annotation),
        - id_in_source (relevant id in the DB/ontology).
    Note that the dicts should be in the same order than the elements after splitting.
    Ex:
    annotation -  'N1	OntoBiotope Annotation:T3 Referent:OBT:002762'
    NEL_format - ({"name":"id_NEL", "prefix":"", "suffix":""},
                  {"name":"source", "prefix":"", "suffix":""},
                  {"name":"id_NER", "prefix":"Annotation:", "suffix":""},
                  {"name":"id_in_source", "prefix":"Referent:", "suffix":""})
    """
    for root, dirs, files in os.walk(path_from):
        for file in filter(lambda f:f.endswith(".ann"), files):
            nel_ann = []
            with open(root+"/"+file) as inp, open(path_to+"/"+file, "w") as outp:
                for line in inp:
                    if line.startswith(NER_id): outp.write(line.replace(NER_id, "T", 1))
                    elif line.startswith(NEL_id):
                        annotation = {info["name"]:element[len(info["prefix"]):len(element)-len(info["suffix"])] for element, info in zip(line.strip().split(), NEL_format)}
                        nel_ann.append(annotation['id_NEL'].replace(NEL_id, 'N', 1)+"\t"+' '.join([annotation.get('source', NEL_source), 'Annotation:'+annotation['id_NER'].replace(NER_id, "T", 1), 'Referent:'+annotation['id_in_source']])+"\n")
                outp.writelines(sorted(nel_ann))


def copy_text_files(path_from, path_to):
    """Copy multiple text files from one directory to another."""
    for root, dirs, files in os.walk(path_from):
        for file in filter(lambda f:f.endswith(".txt"), files):
            shutil.copy(src=root+"/"+file, dst=path_to+"/"+file)


def get_tags(xml_string):
    """
    Get NER annotations from XML string.
    XML string example - <TEXT>He said he grew up in northeast <b_enamex type="LOCATION">China</b_enamex>.</TEXT>
    Annotation example - {"NE":"China", "start":32, "end":37, "token":"LOCATION"}
    """
    res = []
    tag = regex.finditer(r"(<([a-z_]+)[^>]*>([^<]*(?R)[^<]*|([^<]+))</\2>)", xml_string)
    for match in tag:
        entity = regex.sub("<.+?>", "", match.group(3))
        start = match.start() - len("".join(regex.findall("<.+?>", xml_string[:match.start()])))
        end = start+len(entity)
        res.append({"token":entity, "NE":etree.fromstring(match.group(0)).attrib["type"], "start":start, "end":end})
        shift = xml_string.index(match.group(3))
        shift = "_"*(shift - len("".join(regex.findall("<.+?>", xml_string[:shift]))))
        res += get_tags(shift+match.group(3)) or []
    return res


def copy_text(path_from, path_to):
    """Copy a text file from one directory to another with removing uncorrect \n symbols."""
    text = ""
    with open(path_from) as inp, open(path_to, "w") as outp:
        for line in filter(lambda line:line!="\n", inp):
            line = line.replace("\n", "")
            if need_space_after(line): line += " "
            text += line
            outp.write(line)
    return text


def verify(path, hard_fix=False, log_file=None):
    """Verify your indeces in annotation files are correct."""
    errors = 0
    cleaned_annotations = dict()
    if not(log_file): log_file = path[path.rfind("/")+1:]+"_errors.txt"
    with open(log_file, "w") as _: pass
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".txt"):
                with open(root+"/"+file) as lines: text = "".join(lines.readlines())
                ann_root = root+"/"+file.replace("txt", "a2")
                with open(ann_root) as ann: annotations = ann.readlines()
                for i, annotation in enumerate(annotations):
                    try:
                        _, info, token = annotation.strip().split("\t")
                        result = []
                        relevant_indeces = info[info.index(" ")+1:] #we have a NE before the first whitespace
                        for token_piece in relevant_indeces.split(";"):
                            start, end = token_piece.split()
                            result.append(text[int(start):int(end)])
                        result = " ".join(result)
                        assert result == token
                    except ValueError: continue #this occurs when we pass to the NEL annotations part of the file
                    except AssertionError:
                        errors += 1
                        with open(log_file, "a") as log:
                            log.write("\n".join([f"{root}/{file}", f"in text: {result}", f"in annotations: {token}", f"{start}, {end}", "_________________", ""]))
                        if hard_fix:
                            cleaned_annotations[ann_root] = cleaned_annotations.get(ann_root, annotations)
                            gold = result.replace("\n", " ")
                            cleaned_annotations[ann_root][i] = annotations[i][:-1-len(token)] + gold + "\n"
                            text = text[:int(start)]+gold+text[int(end):]
                            with open(root+"/"+file, "w") as fixed: fixed.write(text)
    if hard_fix:
        for path, annotations in cleaned_annotations.items():
            with open(path, "w") as file: file.writelines(annotations)
    return errors


def mkdir(path):
    if not(os.path.isdir(path)): os.mkdir(path)


def clean(path):
    """Remove empty text files and corresponding annotation files."""
    for root, _, files in os.walk(path):
        for file in filter(lambda f: os.path.getsize(root+"/"+f) == 0 and f.endswith(".txt"), files):
            for irrelevant in [file, file.replace("txt", "ann")]:
                os.remove(root+"/"+irrelevant)


def end_of_the_paragraph(token):
    """Check whether the token is the last in the paragraph."""
    return token not in punctuation and True not in [s.isalpha() for s in token]


def need_space_before(token1, token2):
    """Check whether two tokens should contain space between them."""
    return token1 not in "([{" and token2 not in "….,?;://'!)]}" and (not "'" in token2 or token1 in "….,?;://'!)]}")


def need_space_after(line):
    exceptions = []
    word_punct = list("-$%'`/")
    return not(line.endswith(tuple(exceptions + word_punct)))


if __name__ == "__main__":

    
    parser = argparse.ArgumentParser(description="Convert your NER dataset to BRAT or BIO annotation format.")
    parser.add_argument("path_from", type=str, help="Path to the directory where the converted corpus will be saved.")
    parser.add_argument("path_to", type=str, help="Path to save the converted corpus.")
    parser.add_argument("--format", type=str, required=True, choices=convert.keys(), help="Target format for corpus transformation. Options: 'brat' or 'iob'. Note: Command line conversion is only supported between BRAT and IOB formats.")
    parser.add_argument("--token_column", type=int, required=False, default=0, help="Index of the column containing tokens in IOB format files (default: 0).")
    parser.add_argument("--ner_column", type=int, required=False, default=-1, help="Index of the column containing named entity tags in IOB format files (default: -1, i.e., last column).")
    parser.add_argument("--columns_sep", type=str, required=False, default=" ", help="Delimiter used between columns in IOB files (default: space).")
    parser.add_argument("--phrase_sep", type=str, required=False, default="\n", help="Delimiter used between sentences in the IOB files (default: newline).")
    parser.add_argument("--doc_sep", type=str, required=False, default="-DOCSTART- -X- -X- O\n", help="Delimiter used between documents in the IOB files (default: '-DOCSTART- -X- -X- O' followed by a newline).")
    parser.add_argument("--annotations_extention", type=str, required=False, default=".ann", help="File extension for BRAT annotation files (default: .ann).")
    parser.add_argument("--text_extention", type=str, required=False, default=".txt", help="File extension for BRAT text files (default: .txt).")
    parser.add_argument('--verify', type=str, required=False, default="", help='Perform consistency check on annotations. Returns the number of errors found. A log file will be created in the output directory.')
    args = parser.parse_args()
    if args.format == "brat":
        iob_to_brat(path_from=args.path_from, path_to=args.path_to, token_column=args.token_column, ner_column=args.ner_column, columns_sep=args.columns_sep, phrase_sep=args.phrase_sep, doc_sep=args.doc_sep)
    elif args.format == "iob":
        brat_to_iob(path_from=args.path_from, path_to=args.path_to, token_column=args.token_column, ner_column=args.ner_column, columns_sep=args.columns_sep, phrase_sep=args.phrase_sep, annotations_extention= args.annotations_extention, text_extention=args.text_extention)
    else:
        print("Format error. It is possible to convert only from BRAT to IOB and from IOB to BRAT in the command line. If you wish to transform another supported format, use the tool as a python module.")
    if args.verbose:
        print(verify(args.path_to))