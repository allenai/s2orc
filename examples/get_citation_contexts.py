"""
This script retrieves citation contexts (+/- 10 word tokens) from example GORC data.
"""

import json
from typing import Dict, List


def get_citation_contexts(paper: Dict, toks_in_context=10) -> List[Dict]:
    """
    Retrieve citation contexts from GORC paper
    :param paper:
    :param toks_in_context:
    :return:
    """
    if not paper:
        return []

    if not paper['grobid_parse']:
        return []

    if not paper['grobid_parse']['body_text']:
        return []

    contexts = []

    for paragraph in paper['grobid_parse']['body_text']:
        for cite_span in paragraph['cite_spans']:
            # get cited paper id, skip if none
            cite_ref = cite_span['ref_id']
            cited_paper_id = None
            if cite_ref in paper['grobid_parse']['bib_entries']:
                cited_paper_id = paper['grobid_parse']['bib_entries'][cite_ref]['links']
            if not cited_paper_id:
                continue

            # get pre and post tokens
            pre_span_tokens = paragraph['text'][:cite_span['start']].split(' ')[-toks_in_context:]
            post_span_tokens = paragraph['text'][cite_span['end']:].split(' ')[:toks_in_context]
            pre_string = ' '.join(pre_span_tokens)
            post_string = ' '.join(post_span_tokens)
            full_context = pre_string + cite_span['text'] + post_string

            contexts.append({
                "paper_id": paper['paper_id'],
                "context_string": full_context,
                "cite_start": len(pre_string),
                "cite_end": len(pre_string) + len(cite_span['text']),
                "cite_str": cite_span['text'],
                "cited_paper_id": cited_paper_id
            })

    return contexts


EXAMPLE_DATA_FILE = 'data/example_papers.jsonl'


if __name__ == '__main__':
    all_contexts = []
    with open(EXAMPLE_DATA_FILE, 'r') as f:
        for line in f:
            gorc_obj = json.loads(line)
            all_contexts += get_citation_contexts(gorc_obj)

    print(f'{len(all_contexts)} citation contexts.')
    print('done.')