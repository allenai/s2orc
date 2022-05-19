<p align="center">
  <img src="https://raw.githubusercontent.com/allenai/s2orc/master/assets/logo.svg" alt="Logo of S2ORC, pronounced stork" width="20%">
</p>


# S2ORC: The Semantic Scholar Open Research Corpus

S2ORC is a general-purpose corpus for NLP and text mining research over scientific papers.  

* We've curated a unified resource that combines aspects of citation graphs (i.e. rich paper metadata, abstracts, citation edges) with a full text corpus that preserves important scientific paper structure (i.e. sections, inline citation mentions linked to bibliography entries, references to tables and figures).
* Our corpus covers 136M+ paper nodes with 12.7M+ full text papers and connected by 467M+ citation edges by unifying data from many different sources covering many different academic disciplines and identifying open-access papers using services like [Unpaywall](https://unpaywall.org/). 


**Quick Start**
* For an example snippet, see the [`data/`](https://github.com/allenai/s2orc/tree/master/data) directory in this repo. 
* For access to the full thing, **[click here for Download instructions](#download-instructions)**.

**Info**
* S2ORC is jointly maintained by [Kyle Lo](https://twitter.com/kylelostat) and [Lucy Lu Wang](https://llwang.net/) at the [Allen Institute for AI](https://allenai.org/).  Feel free to [contact us](#contact-us).
* S2ORC is released under [ODC-BY](https://opendatacommons.org/licenses/by/1.0/).  By using S2ORC, you agree to the terms in the license.
* For more details, see [our ACL 2020 paper](https://www.aclweb.org/anthology/2020.acl-main.447) or watch [our 12 min ACL 2020 talk](https://slideslive.com/38929131/s2orc-the-semantic-scholar-open-research-corpus).  
* Please cite our paper if you use S2ORC for your project.  See the [BibTeX](#citation). 


## News

* May 2022 - **S2ORC is now available through the Semantic Scholar API**!  We ask that users get access through [the new process](https://www.semanticscholar.org/product/api#Bulk). 
* Feb 2021 - Released [s2orc-doc2json](https://github.com/allenai/s2orc-doc2json) to support parsing of PDF and LaTeX to JSON format.
* Apr 2020 - Our work is accepted to [ACL 2020](https://aclanthology.org/2020.acl-main.447/)!  We've changed the name of the project to S2ORC.  



## Project status

Updates as of May 2022:

1. As stated above, S2ORC is now a fully-fledged Semantic Scholar dataset offering.   We will honor requests for old versions of S2ORC through 2022, but encourage users to try out the newest S2ORC release.  [See details about the newest release below](#s2orc-releases).  

2. We're currently investing in better NLP models for improving PDF processing quality.  Our latest model [VILA](https://github.com/allenai/VILA) has been accepted to TACL 2022, and we're currently working to backfill higher quality S2ORC documents.  Stay tuned! 

3. We have extracted images and would also like to release these with S2ORC, but licensing/copyright around images is a bit tricky (they're separately licensed from the papers themselves).


## S2ORC releases

**Release: 2022-05-18**

- S2ORC is now availble through the [Semantic Scholar API](https://www.semanticscholar.org/product/api#Bulk). Instead of filling out a Google Form for access, please fill out a [Form](https://www.semanticscholar.org/product/api#Partner-Form) for an API key. 
- Automatically kept up-to-date with Semantic Scholar's papers.
- Faster turnaround time for granting access, from 1 week to few days.
- Specific open-access licenses for every single paper.
- Different JSON format. Cleaner format for separating PDF `text` from `annotations`. 
     

**Release: 2020-07-05**

- Released a new version of S2ORC containing papers up until 2020-04-14, bringing full text coverage from 8M to 12M.
- Lifted some paper filters to be more lenient toward papers that don't have sufficient amount of text.  This brought total paper count to 136M from 81M.   
- Updated the schema to keep paper metadata and parsed paper text separate.
- Fixed major bugs such as (i) missing section names, (ii) inline citation mention links that don't resolve to bibliographies, and (iii) unpredictable typing in certain metadata fields. 
- Omitted LaTeX parses from this release.  They will be added in a subsequent release.  Part of the dataset schema change is to accommodate incremental releases (e.g. LaTeX-only release without having to re-run PDF parsing). 


**Release: 2019-09-28**

- Statistics: 81M+ paper nodes; 73M+ gold abstracts; 8M+ full text papers
- Due to release bugs (e.g. missing section names), we no longer recommend usage of this version.  If you must use this version and need assistance, please contact Kyle and Lucy.
- MAG fields of study:

| Field of study | All papers | Full text |
|----------------|------------|-----------|
| Medicine       | 12.8M      | 1.8M      |
| Biology        | 9.6M       | 1.6M      |
| Chemistry      | 8.7M       | 484k      |
| n/a            | 7.7M       | 583k      |
| Engineering    | 6.3M       | 228k      |
| Computer Science       | 6.0M       | 580k      |
| Physics        | 4.9M       | 838k      |
| Material Science        | 4.6M       | 213k      |
| Math           | 3.9M       | 669k      |
| Psychology     | 3.4M       | 316k      |
| Economics      | 2.3M       | 198k      |
| Political Science       | 1.8M       | 69k       |
| Business       | 1.8M       | 94k       |
| Geology        | 1.8M       | 115k      |
| Sociology      | 1.6M       | 93k       |
| Geography      | 1.4M       | 58k       |
| Environmental Science        | 766k       | 52k       |
| Art            | 700k       | 16k       |
| History        | 690k       | 22k       |
| Philosophy     | 384k       | 15k       |


## Download instructions

S2ORC is now available through the [Semantic Scholar API](https://www.semanticscholar.org/product/api#Bulk). Please fill out this [Form](https://www.semanticscholar.org/product/api#Partner-Form) for an API key.  The turnaround time should be a few days; if it takes longer, please contact us via email.

**Instructions TBD...**


## Contact us

The best way to contact us is through email.  Don't hesitate to reach out about anything; we've helped a lot of people get started with the dataset, which can be a bit daunting given its size.

**Email:** `{kylel, lucyw}@allenai.org`

**Twitter** [@kylelostat](https://twitter.com/kylelostat), [@lucyluwang](https://twitter.com/lucyluwang)

**Report issues:** Use [GitHub Issues](https://github.com/allenai/s2orc/issues) to report bugs or issues!  We'll try to fix it for the next release.

 

## FAQ

#### How is this related to the [Semantic Scholar Academic Graph (S2AG)](https://www.semanticscholar.org/product/api)?
S2ORC and S2AG were originally different, separate datasets; but the two have become more aligned over time.  

**Definitions & Scope**

S2AG is fundamentally a citation graph.  It consists of paper metadata (e.g. title, authors) and citations between them.  S2ORC originally was also a (smaller) citation graph containing similar (but slightly different) paper metadata + a corpus of the full text of these papers.  

But as of v2020-05-18, S2AG and S2ORC are completely aligned. For example, a paper in S2AG maps exactly to a paper in S2ORC, and vice versa.  As such, we now refer to the citation graph (papers, metadata, citation links) as the S2AG dataset, and the full text corpus as the S2ORC dataset.    


If you're unsure what to use, please email us and we'd be happy to discuss your project with you.

**Discrepancies between S2AG paper metadata and S2ORC full text**

S2ORC contains all the content processed from PDFs of papers, which naturally includes paper metadata such as Titles, Authors, Abstract, Bibliography entries, etc.  Of course, S2AG also provides this information.  Users may notice differences in these fields between S2ORC and S2AG.

This is because of paper deduplication. For example, when Semantic Scholar has copies of the same paper from both arXiv and PubMed, we ensure there is only a single representative paper in S2AG.  But what if the Title or Abstract is different between the arXiv and PubMed versions?  S2AG prioritizes metadata associated with the official version of record, while S2ORC prioritizes versions of the paper that have an associated open-access license.  Then in our example, S2ORC paper content (including PDF-processed Title or Abstract) might come the arXiv rather than the PubMed version.



## License

S2ORC is released under [ODC-BY](https://opendatacommons.org/licenses/by/1.0/).  By using S2ORC, you agree to the terms in the license.


## Citation

If using this dataset, please cite:

```
@inproceedings{lo-wang-2020-s2orc,
    title = "{S}2{ORC}: The Semantic Scholar Open Research Corpus",
    author = "Lo, Kyle  and Wang, Lucy Lu  and Neumann, Mark  and Kinney, Rodney  and Weld, Daniel",
    booktitle = "Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics",
    month = jul,
    year = "2020",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2020.acl-main.447",
    doi = "10.18653/v1/2020.acl-main.447",
    pages = "4969--4983"
}
```
