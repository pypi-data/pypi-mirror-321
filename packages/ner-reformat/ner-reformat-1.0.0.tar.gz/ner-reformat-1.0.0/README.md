# NER Reformat

NER Reformat is a Python package that transforms Named Entity Recognition (NER) annotations into the BRAT and BIO formats. It also supports Named Entity Linking annotations transformation to BRAT format for some corpora. You can see the list of formats at section [Supported formats](#supported-formats)


## Installation

You can install NER Formatter using pip:
```
pip3 install ner-reformat
```

## Usage

Here's a basic example of how to use NER Formatter:
```
from ner-reformat import ncbi_to_brat

path_to = "your path/NCBI diseases"
path_from = "your path/NCBI diseases"
ncbi_to_brat(path_from=path_from, path_to=path_to)
```

## Supported Corpora

- IOB formatted, including:
   - CoNLL
   - OntoNotes
   - MultiNERD
   - WikiNeural
   - WNUT
   - MIT Movies
   - MIT Restaurants
- BRAT formatted, including:
  - CADEC
- NCBI
- IEER
- BioCreative
- Groningen Meaning Bank
- GeoVirus
- MalwareTextDB

### Annotation Schemes of BRAT and IOB

[BRAT](https://brat.nlplab.org/) (Brat Rapid Annotation Tool) format is a standoff annotation format used for text annotation tasks. In BRAT format, each entity is represented on a separate line with annotations including an ID, entity type, start and end offsets, and the annotated text. Example:
```
example.txt

The following month, he signed a contract to play for the Newark Bears in the International League.
```
```
example.ann

T1    ORG 58 70    Newark Bears
T2    ORG 78 98    International League
```

IOB (Beginning, Inside, Outside) format, also known as BIO, is a tagging scheme used for token-level annotation in NLP tasks like Named Entity Recognition. The `B-` prefix indicates the beginning of an entity, `I-` prefix indicates a token inside an entity, and `O` tag represents tokens outside any entity.

```
0    The    O
1    following    O
2    month    O
3    ,    O
4    he    O
5    signed    O
6    a    O
7    contract    O
8    to    O
9    play    O
10    for    O
11    the    O
12    Newark    B-ORG
13    Bears    I-ORG
14    in    O
15    the    O
16    International    B-ORG
17    League    I-ORG
18    .    O
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
