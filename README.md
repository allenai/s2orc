# Semantic Scholar GORC Corpus

**Latest release: 2019-09-28**

The Semantic Scholar Graph of References in Context (GORC) dataset is a literature graph of 81.0M academic publications and 380.5M citation edges. 
Full text and citation contexts are available for 8.1M papers. Abstracts are available for 73.4M papers.

The dataset is located in the S3 bucket `s3://ai2-s2-gorc-release/`. 

To gain access to this bucket, create an AWS account and fill out this access request [form](https://docs.google.com/forms/d/e/1FAIpQLSeNeo4UBeRoe1taaN3oJ1Fr1BZokVs3vVo18mvfc0Lhnw7n1g/viewform).

Use of this data is subject to the [Semantic Scholar Dataset License](http://api.semanticscholar.org/corpus/legal/).

The full corpus consists of 10000 zipped files, and is around 205GB.

The manifest file `s3://ai2-s2-gorc-release/20190928/manifest.json` lists all available files for download.

## Download instructions

First, please complete this [form](https://docs.google.com/forms/d/e/1FAIpQLSeNeo4UBeRoe1taaN3oJ1Fr1BZokVs3vVo18mvfc0Lhnw7n1g/viewform) to request access. We will email you to confirm access granted.

### Download GORC data using Python:

1. Setup an environment (below example uses Miniconda)
    * Download the Miniconda installer for your OS: [https://docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html)
    * Run `bash Miniconda-3.5.5-MacOSX-x86_64.sh` to install
    * Add conda path to $PATH variable
    * Create a conda environment: `conda create -n gorc -y python==3.7`
    * Activate environment: `conda activate gorc`

2. Install requirements:
    
    `pip install -r requirements.txt`
    
3. Run setup.py:
    
    `python setup.py develop`
    
4. Download GORC:
 
    `python ./examples/download_gorc.py`

### Download GORC using AWS CLI 

1. Create a folder for the data:

    `mkdir gorc/`
    
2. Download GORC:
    
    `aws s3 sync s3://ai2-s2-gorc-release/20190928/papers/ gorc/`
    
AWS CLI [documentation](https://aws.amazon.com/cli/)
