# Semantic Scholar GORC Corpus

**Latest release: 2019-09-28**

The Semantic Scholar Graph of References in Context (GORC) dataset is a literature graph of 81.0M academic publications and 380.5M citation edges. 
Full text and citation contexts are available for 8.1M papers. Abstracts are available for 73.4M papers.

See [our arXiv preprint](https://arxiv.org/abs/1911.02782) for details.

## Download instructions

First, please complete this [form](https://docs.google.com/forms/d/e/1FAIpQLSeNeo4UBeRoe1taaN3oJ1Fr1BZokVs3vVo18mvfc0Lhnw7n1g/viewform) to request access to the S3 bucket.  We will email you to confirm access granted.

You'll need an AWS account to access the S3 bucket `s3://ai2-s2-gorc-release/`.  The full corpus consists of 10000 zipped files, and is around 205GB.  The manifest file `s3://ai2-s2-gorc-release/20190928/manifest.json` lists all available files for download.


Use of this data is subject to the [Semantic Scholar Dataset License](http://api.semanticscholar.org/corpus/legal/).


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

### Citation

If using this dataset, please cite our arXiv preprint:

```
@misc{lo2019gorc,
    title={GORC: A large contextual citation graph of academic papers},
    author={Kyle Lo and Lucy Lu Wang and Mark Neumann and Rodney Kinney and Dan S. Weld},
    year={2019},
    eprint={1911.02782},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```
