<p align="center">
  <img src="https://raw.githubusercontent.com/allenai/s2orc/master/assets/logo.svg" alt="Logo of S2ORC, pronounced stork" width="20%">
</p>


# S2ORC: The Semantic Scholar Open Research Corpus

S2ORC is a general-purpose corpus for NLP and text mining research over scientific papers.

* **[Download instructions](#download-instructions)**.
* S2ORC was developed by [Kyle Lo](https://kyleclo.github.io/) and [Lucy Lu Wang](https://llwang.net/) at the [Allen Institute for AI](https://allenai.org/). It is now being maintained as a product offering by the API team at [Semantic Scholar](https://www.semanticscholar.org/product/api).
* S2ORC is released under the [ODC-By 1.0](https://opendatacommons.org/licenses/by/1-0/).  By using S2ORC, you agree to the terms in the license.
* Please cite [our ACL 2020 paper](https://www.aclweb.org/anthology/2020.acl-main.447) if you use S2ORC for your project.  See the [BibTeX](#citation). You can also watch [our 12 min ACL 2020 talk](https://slideslive.com/38929131/s2orc-the-semantic-scholar-open-research-corpus).



## News and Releases

⭐ **S2ORC now available through S2 API**

It's Jan 2023; happy new year! After years of managing S2ORC as a research project, it has now been adopted as a core dataset offering through the [Semantic Scholar Public API](https://www.semanticscholar.org/product/api). Please look for the instructions under "Bulk Dataset" for download! 

S2ORC is now available through the [Semantic Scholar Public API](https://www.semanticscholar.org/product/api) as a "Bulk Dataset". It is continuously being rebuilt so if you access it through there, you'll get access to **new** papers as well!

**Software Release: 2021-02-01**

- Released [s2orc-doc2json](https://github.com/allenai/s2orc-doc2json) to support parsing of PDF and LaTeX to JSON format.


**S2ORC Release: 2020-07-05**

- Released a new version of S2ORC containing papers up until 2020-04-14, bringing full text coverage from 8M to 12M.
- Lifted some paper filters to be more lenient toward papers that don't have sufficient amount of text.  This brought total paper count to 136M from 81M.   
- Updated the schema to keep paper metadata and parsed paper text separate.
- Fixed major bugs such as (i) missing section names, (ii) inline citation mention links that don't resolve to bibliographies, and (iii) unpredictable typing in certain metadata fields. 
- Omitted LaTeX parses from this release.  They will be added in a subsequent release.  Part of the dataset schema change is to accommodate incremental releases (e.g. LaTeX-only release without having to re-run PDF parsing). 

- Feb 2023 update: We are no longer supporting access to this version & recommend everyone use the latest way of accessing S2ORC through the Semantic Scholar Public API.  If you must use this version and need assistance, please contact Kyle and Lucy.


**Project Status: 2020-04-07**

- S2ORC has been accepted to ACL 2020!
- We've changed the name of the project to S2ORC.  We will update the [preprint](https://arxiv.org/abs/1911.02782) shortly with the new name.
- The [BibTeX citation](#citation) has also been changed to reflect this.
- Feb 2023 update: We are no longer supporting access to this version & recommend everyone use the latest way of accessing S2ORC through the Semantic Scholar Public API.  If you must use this version and need assistance, please contact Kyle and Lucy.


**S2ORC Release: 2019-09-28**

- Statistics: 81M+ paper nodes; 73M+ gold abstracts; 8M+ full text papers
- Due to release bugs (e.g. missing section names), we no longer recommend usage of this version.  If you must use this version and need assistance, please contact Kyle and Lucy.


## Download instructions

The original S2ORC dataset files were refactored into multiple datasets available through [the Semantic Scholar APIs](https://api.semanticscholar.org/) (See detailed documentation [here](https://api.semanticscholar.org/api-docs/datasets)). 

For questions, feature requests, bug reports, please search existing issues on [the s2-folks Github repo](https://github.com/allenai/s2-folks/issues?q=is%3Aissue) before creating [a new issue](https://github.com/allenai/s2-folks/issues/new). 


## Contact us

The best way to contact us is through email.  Don't hesitate to reach out about anything; we've helped a lot of people get started with the dataset, which can be a bit daunting given its size.

**Email:** Please include `{kylel, lucyw, rodneyk, wammar}@allenai.org` on all correspondence.

**Twitter** [@kylelostat](https://twitter.com/kylelostat), [@lucyluwang](https://twitter.com/lucyluwang)

**Give us Feedback:**  Totally optional, but we'd love to hear how you're using this dataset & any feedback for improving it.  Send us an email or leave a Github Issue. 

**Report issues:** 

S2ORC is now being maintained by the S2 API product team. For questions, feature requests, bug reports, please search existing issues on [the s2-folks Github repo](https://github.com/allenai/s2-folks/issues?q=is%3Aissue) before creating [a new issue](https://github.com/allenai/s2-folks/issues/new). 
 

## FAQ

#### What's the difference between [S2ORC](https://arxiv.org/abs/1911.02782) and [S2AG](https://dl.acm.org/doi/fullHtml/10.1145/3487553.3527147)?
At a high level:

- S2AG is everything that is covered in the literature graph, including Nodes (i.e. papers, authors) and Edges (i.e. citations, authorship). A `paper` in S2AG is represented by a bundle of Metadata, such as the Title, Authors, Year, Venue, Abstract, etc. You can download different releases of S2AG via the [the Semantic Scholar APIs](https://api.semanticscholar.org/) (See detailed documentation [here](https://api.semanticscholar.org/api-docs/datasets)).

- S2ORC is everything that is machine-readable **full text** of the paper, which we derive using models run on the paper's PDF. The original S2ORC dataset files are no longer available for download. They were refactored into multiple datasets available through [the Semantic Scholar APIs](https://api.semanticscholar.org/) (See detailed documentation [here](https://api.semanticscholar.org/api-docs/datasets)).  

If you're unsure what to use or cite, please email us and we'd be happy to discuss your project with you.

#### I have an old version of S2ORC. How is it different from the version of S2ORC from the S2 API?

- Original S2ORC was a research project w/ original code. The current S2ORC is a reimplementation of the ideas from the research project within the Semantic Scholar data pipeline. As such, there can be differences due to low level implementation details being different.

- Current S2ORC is maintained by a different team than the original researchers. 


- Original S2ORC was released under a non-commercial license. The current S2ORC is released under an ODC-By 1.0 license. We ask that users take care to double-check whether their intended usage of S2ORC and its underlying contents is permissible under this license.


## License

S2ORC is currently released through the [Semantic Scholar Public API](https://www.semanticscholar.org/product/api) under the [ODC-By 1.0](https://opendatacommons.org/licenses/by/1-0/). By using S2ORC, you are agreeing to its usage terms. 



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
