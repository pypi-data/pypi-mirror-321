from setuptools import setup, find_packages

def readme():
  with open('README.md', 'r') as f:
    return f.read()

setup(
  name='ner-reformat',
  version='1.0.0',
  author='MB',
  author_email='mariya.borovikova@universite-paris-saclay.fr',
  description='A Python package for converting various Named Entity Recognition (NER) formats to BRAT and BIO formats.',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/project178/ner_reformat',
  packages=find_packages(),
  install_requires=['regex',
        'requests',
        'beautifulsoup4',
        'tqdm',
        'torch',
        'bioc',
        'joblib',],
  classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
  keywords='NLP Named Entity Recognition annotation NER BRAT BIO',
  python_requires='>=3.7'
)