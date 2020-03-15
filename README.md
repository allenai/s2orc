# Semantic Scholar GORC Corpus

**Latest release: 2019-09-28**

The Semantic Scholar Graph of References in Context (GORC) dataset is a citation graph of 81.1M academic publications and 380.5M citation edges.
Abstracts are available for 73.4M papers.  Full text and citation contexts are available for 8.1M papers.  Citation contexts are linked to their corresponding paper in the graph.

See [our arXiv preprint](https://arxiv.org/abs/1911.02782) for details.

## Contact / Feedback

We'd love to hear how you're using this dataset and any feedback you might have: [Please fill out this Google Form](https://forms.gle/vB4T481sd65rfnir8).  This is completely optional, but we'd really appreciate it since this information will inform how we'll maintain the project going forward.  Thanks!

If you'd prefer to email, contact us at:  `{kylel, lucyw}@allenai.org`


## Download instructions

You will need an AWS account to access the S3 bucket `s3://ai2-s2-gorc-release/`.

The full corpus consists of 10000 zipped files, and is around 205GB. The manifest file `s3://ai2-s2-gorc-release/20190928/manifest.json` lists all available files for download.

Use of this data is subject to the [Semantic Scholar Dataset License](http://api.semanticscholar.org/corpus/legal/).

We also provide metadata files for each of the 10000 zipped batches at `s3://ai2-s2-gorc-release/20190928/metadata/`.  These metadata files include inbound/outbound citations, field of study information, and associated identifiers.  A sample of this metadata is provided in `data/metadata_sample.tsv`.

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

### Download GORC using AWS CLI ([documentation](https://aws.amazon.com/cli/))

1. Create a folder for the data:

    `mkdir gorc/`
    
2. Download GORC:
    
    `aws s3 sync s3://ai2-s2-gorc-release/20190928/papers/ gorc/`




## Example data

A sample of GORC data is provided in `data/example_papers.jsonl`. 

The JSON schema for each paper is given below:

```json
{
  "paper_id": "paper_id",
  "metadata": {
    "title": "title_string",
    "authors": [
      {
        "first": "first_name",
        "middle": ["middle_name"],
        "last": "last_name",
        "suffix": "suffix_name"
      }
    ],
    "abstract": "abtract_string",
    "year": "year_string",
    "arxiv_id": "arxiv_id_string",
    "acl_id": "acl_id_string",
    "pmc_id": "pmc_id_string",
    "pubmed_id": "pubmed_id_string",
    "doi": "doi_string",
    "venue": "venue_string",
    "journal": "journal_string"
  },
  "s2_pdf_hash": "s2_pdf_hash",
  "grobid_parse": {
    "abstract": [
      {
        "text": "abstract_string",
        "cite_spans": [],
        "ref_spans": [],
        "eq_spans": null,
        "section": "Abstract"
      }
    ],
    "body_text": [
      {
        "text": "paragraph_string",
        "cite_spans": [
          {
            "start": 15,
            "end": 18,
            "text": "cite_span_text",
            "latex": null,
            "ref_id": "bibkey (index for bib_entries)"
          }
        ],
        "ref_spans": [
          {
            "start": 0,
            "end": 8,
            "text": "ref_span_text",
            "latex": null,
            "ref_id": "refkey (index for ref_entries)"
          }
        ],
        "eq_spans": [],
        "section": null
      }
    ],
    "ref_entries": {
      "refkey": {
        "text": "ref_string",
        "latex": null,
        "type": "ref_type (figure, table, equation, etc)"
      }
    },
    "bib_entries": {
      "bibkey": {
        "ref_id": "string",
        "title": "title_string",
        "authors": [
          {
            "first": "first_name",
            "middle": [],
            "last": "last_name",
            "suffix": "suffix_name"
          }
        ],
        "year": 2019,
        "venue": "venue_string",
        "volume": "volume_string",
        "issn": "issue_number_string",
        "pages": "pages_string",
        "other_ids": {
          "doi": ["doi_string"]
        },
        "links": "linked_paper_id"
      }
    }
  },
  "latex_parse": null
}
```

## Citation

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
