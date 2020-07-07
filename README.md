# S2ORC: The Semantic Scholar Open Research Corpus

S2ORC is a general-purpose corpus for NLP and text mining research over scientific papers.  

* We've curated a unified resource that combines aspects of citation graphs (i.e. rich paper metadata, abstracts, citation edges) with a full text corpus that preserves important scientific paper structure (i.e. sections, inline citation mentions, references to tables and figures).
* Our corpus covers 136M+ paper nodes with 12.7M+ full text papers and connected by 467M+ citation edges by unifying data from many different sources covering many different academic disciplines and identifying open-access papers using services like [Unpaywall](https://unpaywall.org/). 

For more details, see [our ACL 2020 paper](https://www.aclweb.org/anthology/2020.acl-main.447) for more details.

For an **example** snippet of data, see the [`data/`](https://github.com/allenai/s2orc/tree/master/data) directory in this repo. 

S2ORC is released under the [Semantic Scholar Dataset License](http://api.semanticscholar.org/corpus/legal/).

* S2ORC is jointly maintained by [Kyle Lo](https://twitter.com/kylelostat) and [Lucy Lu Wang](https://llwang.net/) at the [Allen Institute for AI](https://allenai.org/).  
* Feel free to [email us](#contact) and subscribe to our [mailing list](#contact).  
* Please cite our paper if you use S2ORC for your project.  See the [BibTeX](#citation). 

## Latest

**Release: 2020-07-05**

- Released a new version of S2ORC containing papers up until 2020-04-14, bringing full text coverage from 8M to 12M.
- Lifted some paper filters to be more lenient toward papers that don't have sufficient amount of text.  This brought total paper count to 136M from 81M.   
- Updated the schema to keep paper metadata and parsed paper text separate.
- Fixed major bugs such as (i) missing section names, (ii) inline citation mention links that don't resolve to bibliographies, and (iii) unpredictable typing in certain metadata fields. 
- Omitted LaTeX parses from this release.  They will be added in a subsequent release.  Part of the dataset schema change is to accommodate incremental releases (e.g. LaTeX-only release without having to re-run PDF parsing). 


**Status: 2020-04-07**

- S2ORC has been accepted to ACL 2020!
- We've changed the name of the project to S2ORC.  We will update the [preprint](https://arxiv.org/abs/1911.02782) shortly with the new name.
- The [BibTeX citation](#citation) has also been changed to reflect this.


**Release: 2019-09-28**

- Statistics: 81M+ paper nodes; 73M+ gold abstracts; 8M+ full text papers
- Due to release bugs (e.g. missing section names), we no longer recommend usage of this version.  If you must use this version and need assistance, please contact Kyle and Lucy.

## Download instructions

Please request access to S2ORC through this short [Google Form](https://forms.gle/dSBnP1vEtxWpPcVW8) and we'll send you URLs to download the dataset.  It's just a few questions like your email, what version you'd like, and whether you'd like to receive email updates.

#### Valid release versions

* `20200705v1` (latest)
* `20190928`

#### Release directory structure

As of the latest release, the full corpus consists of `metadata/` and `pdf_parses/` splits, each containing 100 gzipped files.  The directory structure for each release is:

```python
yyyymmddvi/                 # version ID.  e.g. `20200705v1` means the first version
                            # released on 2020-07-05
|-- full/ 
   |-- metadata/            # 100 jsonl files; each file approx 529MB & 2.0GB unzipped
       |-- metadata_0.jsonl.gz
       |-- metadata_1.jsonl.gz
       ...
   |-- pdf_parses/          # 100 jsonl files; each file approx 1.6GB zipped & 6.5GB unzipped
       |-- pdf_parses_0.jsonl.gz
       |-- pdf_parses_1.jsonl.gz
       ...
|-- sample/
   |-- metadata/            # 1 jsonl file; first 1000 rows of full/metadata/metadata_0.jsonl
       |-- sample.jsonl
   |-- pdf_parses/          # 1 jsonl file; first 203 rows of full/pdf_parses/pdf_parses_0.jsonl
       |-- sample.jsonl
|-- RELEASE_NOTES           # a few notes about this particular release
|-- LICENSE                 # license for usage of S2ORC
```

#### Data size

**We strongly recommend** users to first download the `sample/` (5.9MB) which before committing to downloading the `full/` collection (52GB for `metadata/` and 160GB for `pdf_parses/`). 

Also make sure there is enough space on your machine.  When unzipped the dataset grows to 191GB for `metadata/` and 643GB for `pdf_parses/`.


#### gzip

Each JSONlines file in `full/` is zipped up.  To unzip all files in the directory: `cd <dirname>` and `gunzip *`.  


## `metadata` schema

We recommend everyone work with `metadata/` as the starting point.  This is a JSONlines file (one line per paper) with the following keys:

#### Identifier fields

* `paper_id`: a `str`-valued field that is a unique identifier for each S2ORC paper.

* `arxiv_id`: a `str`-valued field for papers on [arXiv.org](https://arxiv.org).

* `acl_id`: a `str`-valued field for papers on [the ACL Anthology](https://www.aclweb.org/anthology/).

* `pmc_id`: a `str`-valued field for papers on [PubMed Central](https://www.ncbi.nlm.nih.gov/pmc/articles).

* `pubmed_id`: a `str`-valued field for papers on [PubMed](https://pubmed.ncbi.nlm.nih.gov/), which includes MEDLINE.  Also known as `pmid` on PubMed.

* `mag_id`: a `str`-valued field for papers on [Microsoft Academic](https://academic.microsoft.com).

* `doi`: a `str`-valued field for the [DOI](http://doi.org/).  

Notably:

* Resolved citation links are represented by the cited paper's `paper_id`.

* The `paper_id` resolves to a Semantic Scholar paper page, which can be verified using the `s2_url` field.

* We don't always have a value for every identifier field.  When missing, they take `null` value.


#### Metadata fields

* `title`: a `str`-valued field for the paper title.  Every S2ORC paper *must* have one, though the source can be from publishers or parsed from PDFs.  We prioritize publisher-provided values over parsed values.

* `authors`: a `List[Dict]`-valued field for the paper authors.  Authors are listed in order.  Each dictionary has the keys `first`, `middle`, `last`, and `suffix` for the author name, which are all `str`-valued with exception of `middle`, which is a `List[str]`-valued field.  Every S2ORC paper *must* have at least one author.

* `venue` and `journal`: `str`-valued fields for the published venue/journal.  *Please note that there is not often agreement as to what constitutes a "venue" versus a "journal". Consolidating these fields is being considered for future releases.*   

* `year`: an `int`-valued field for the published year.  If a paper is preprinted in 2019 but published in 2020, we try to ensure the `venue/journal` and `year` fields agree & prefer non-preprint published info. *We know this decision prohibits certain types of analysis like comparing preprint & published versions of a paper.  We're looking into it for future releases.*  

* `abstract`: a `str`-valued field for the abstract.  These are provided directly from gold sources (not parsed from PDFs).  We preserve newline breaks in structured abstracts, which are common in medical papers, by denoting breaks with `':::'`.     

* `inbound_citations`: a `List[str]`-valued field containing `paper_id` of other S2ORC papers that cite the current paper.  *Currently derived from PDF-parsed bibliographies, but may have gold sources in the future.*

* `outbound_citations`: a `List[str]`-valued field containing `paper_id` of other S2ORC papers that the current paper cites.  Same note as above.   

* `has_inbound_citations`: a `bool`-valued field that is `true` if `inbound_citations` has at least one entry, and `false` otherwise.

* `has_outbound_citations` a `bool`-valued field that is `true` if `outbound_citations` has at least one entry, and `false` otherwise.

We don't always have a value for every metadata field.  When missing, `str` fields take `null` value, while `List` fields are empty lists.

#### PDF parse-related metadata fields

* `has_pdf_parse`:  a `bool`-valued field that is `true` if this paper has a corresponding entry in `pdf_parses/`, which means we had processed that paper's PDF(s) at some point.  The field is `false` otherwise.

* `has_pdf_parsed_abstract`: a `bool`-valued field that is `true` if the paper's PDF parse contains a parsed abstract, and `false` otherwise.   

* `has_pdf_parsed_body_text`: a `bool`-valued field that is `true` if the paper's PDF parse contains parsed body text, and `false` otherwise.

* `has_pdf_parsed_bib_entries`: a `bool`-valued field that is `true` if the paper's PDF parse contains parsed bibliography entries, and `false` otherwise.

* `has_pdf_parsed_ref_entries`: a `bool`-valued field that is `true` if the paper's PDF parse contains parsed reference entries (e.g. tables, figures), and `false` otherwise.

Please note:

* If `has_pdf_parse = false`, the other four fields will not be present in the JSON (trivially `false`).

* If `has_pdf_parse = true` but `has_pdf_parsed_abstract`, `has_pdf_parsed_body_text`, or `has_pdf_parsed_ref_entries` are `false`, this can be because:

    * Our PDF parser failed to extract that element
    * Our PDF parser succeeded but that paper simply did not have that element (e.g. papers without abstracts)
    * Our PDF parser succeeded but that element was removed because the paper is not identified as open-access.  



## `pdf_parses` schema

We view `pdf_parses/` as supplementary to the `metadata/` entries.  PDF parses are also represented as JSONlines file (one line per paper) with the following keys:

* `paper_id`: a `str`-valued field which is the same S2ORC paper ID in `metadata/`

* `_pdf_hash`: a `str`-valued field.  Internal usage only.  We use this for debugging.

* `abstract` and `body_text` are `List[Dict]`-valued fields representing parsed text from the PDF.  Each `Dict` corresponds to a paragraph.  `List` preserves their original ordering.

* `bib_entries` and `ref_entries` are `Dict`-valued fields representing extracted entities that can be referenced (inline) within the text.

#### example 1

One example paragraph in `abstract` or `body_text` might look like:

```python
{
    "section": "Introduction",
    "text": "Dogs are happier cats [13, 15]. See Figure 3 for a diagram.",
    "cite_spans": [
        {"start": 22, "end": 25, "text": "[13", "ref_id": "BIBREF11"},
        {"start": 27, "end": 30, "text": "15]", "ref_id": "BIBREF30"},
        ...
    ],
    "ref_spans": [
        {"start": 36, "end": 44, "text": "Figure 3", "ref_id": "FIGREF2"},
    ]
}
```

and example `bib_entries` and `ref_entries` might look like:

```python
{
    ...,
    "BIBREF11": {
        "title": "Do dogs dream of electric humans?",
        "authors": [
            {"first": "Lucy", "middle": ["Lu"], "last": "Wang", "suffix": ""}, 
            {"first": "Mark", "middle": [], "last": "Neumann", "suffix": "V"}
        ],
        "year": "", 
        "venue": "barXiv",
        "link": null
    },
    ...
}
```

```python
{
    "TABREF4": {
        "text": "Table 5. Clearly, we achieve SOTA here or something.",
        "type": "table"
    }
    ...,
    "FIGREF2": {
        "text": "Figure 3. This is the caption of a pretty figure.",
        "type": "figure"
    },
    ...
}
```

Notice: 

* Inline `spans` are represented by character start and end indices into the paragraph `text`
* `spans` resolve to `BIBREF`, `TABREF` or `FIGREF` entries.
* `BIBREF` are IDs of bibliographic elements of `bib_entries`.  Bib entries may be missing fields (e.g. `year`).  They can be linked to S2ORC papers, as specified by `link`, but we also preserve any unlinked entries by setting `link` to `null`.
* `FIGREF` and `TABREF` are IDs of figure and table elements of `ref_entries`.  Ref entries contain the caption text of the corresponding object, and also indicate the type of object.


#### example 2

You may see empty `pdf_parses/` JSONs that look like: 

```python
{
    "paper_id": "...", 
    "_pdf_hash": "...", 
    "abstract": [], 
    "body_text": [], 
    "bib_entries": {}, 
    "ref_entries": {}
}
```

We keep these around for our internal usage, but the way to interpret these is that there is no usable PDF parse here, despite the corresponding `metadata/` entry still displaying `has_pdf_parse = true`.

These exist when (i) `bib_entries` does not successfully parse *and* (ii) the paper is not open-access, so we had to remove `abstract`, `body_text`, and `ref_entries`.   


## Example Usage

To start with something simple, let's count (outbound) citation edges:

```python
import os
import json

num_edges = 0
METADATA_DIR = '/disk2/s2orc/20200414/release_metadata/'
for metadata_file in os.listdir(METADATA_DIR):
    with open(os.path.join(METADATA_DIR, metadata_file)) as f_meta:
        for line in f_meta:
            metadata_dict = json.loads(line)
            num_edges += len(metadata_dict['outbound_citations'])
print(num_edges)
> 467588220
```

The way we expect most people to use S2ORC full text is to loop through the `metadata/` entries, select papers of interest, and retrieve the corresponding `pdf_parses/` entries when desired.  For example:

```python
import json

BATCH_ID = 0

# create a lookup for the pdf parse based on paper ID
paper_id_to_pdf_parse = {}
with open(f'full/pdf_parses/pdf_parses_{BATCH_ID}.jsonl') as f_pdf:
    for line in f_pdf:
        pdf_parse_dict = json.loads(line)
        paper_id_to_pdf_parse[pdf_parse_dict['paper_id']] = pdf_parse_dict

# filter papers using metadata values
citation_contexts = []
with open(f'full/metadata/metadata_{BATCH_ID}.jsonl') as f_meta:
    for line in f_meta:
        metadata_dict = json.loads(line)
        paper_id = metadata_dict['paper_id']
        print(f"Currently viewing S2ORC paper: {paper_id}")
        
        # suppose we only care about ACL anthology papers
        if not metadata_dict['acl_id']:
            continue
    
        # and we want only papers with resolved outbound citations
        if not metadata_dict['has_outbound_citations']:
            continue
        
        # get citation context (paragraphs)!
        if paper_id in paper_id_to_pdf_parse:
            pdf_parse = paper_id_to_pdf_parse[paper_id]
            
            # bib entries for looking up citation links
            bib_entries = pdf_parse['bib_entries']
            
            # loop over paragraphs
            for paragraph in pdf_parse['abstract'] + pdf_parse['body_text']:
                
                # each paragraph can have multiple inline citations
                for cite_span in paragraph['cite_spans']:
                    
                    # each inline citation can be resolved to a bib entry
                    cited_bib_entry = bib_entries[cite_span['ref_id']]
                    
                    # that bib entry *may* be linked to a S2ORC paper
                    linked_paper_id = cited_bib_entry['link']
                    if linked_paper_id:
                        citation_contexts.append({
                            'citing_paper_id': paper_id,
                            'cited_paper_id': linked_paper_id,
                            'context': paragraph['text'],
                            'citation_mention_start': cite_span['start'],
                            'citation_mention_end': cite_span['end'],
                        })
```



## Contact / Feedback

The best way to contact us is through email.  Don't hesitate to reach out about anything; we've helped a lot of people get started with the dataset, which can be a bit daunting given its size.

**Email:** `{kylel, lucyw}@allenai.org`

**Twitter** [@kylelostat](https://twitter.com/kylelostat), [@lucyluwang](https://twitter.com/lucyluwang)

**IRC:** `#s2orc` at `irc.oftc.net`

**Give us Feedback:**  Totally optional, but we'd love to hear how you're using this dataset & any feedback for improving it.  Send us an email or use this [Google Form](https://forms.gle/vB4T481sd65rfnir8). 

**Mailing list:**  Join our [Google Groups](https://groups.google.com/g/s2orc?pli=1)!  We email updates & releases about S2ORC here.

**Report issues:** Use [GitHub Issues](https://github.com/allenai/s2orc/issues) to report bugs or issues!  We'll try to fix it for the next release.

 

## FAQ

TBD.


## Citation

If using this dataset, please cite:

```
@inproceedings{lo-wang-2020-s2orc,
    title={{S2ORC: The Semantic Scholar Open Research Corpus}},
    author={Kyle Lo and Lucy Lu Wang and Mark Neumann and Rodney Kinney and Daniel S. Weld},
    year={2020},
    booktitle={Proceedings of ACL},
    url={https://www.aclweb.org/anthology/2020.acl-main.447}
}
```
