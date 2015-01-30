"""
Utility script to generate all the empty solution files to problems on
leetcodeOJ
"""

import requests
from lxml.html.clean import Cleaner
import lxml.html


def get_doc_root(url):
    html = requests.get(url).content
    cleaner = Cleaner(page_structure=False)
    cleaned_html = cleaner.clean_html(html)
    root = lxml.html.fromstring(cleaned_html)
    return root

def write_to_solution_file(num, title):
    problem_url = "https://oj.leetcode.com/problems/" + title.lower().replace(" ", "-")
    problem_root = get_doc_root(problem_url)
    problem_desc = problem_root.xpath('//div[@class="question-content"]//text()')
    #problem_desc = [item.replace("\r", "") if item != "Show Tags" else "Tags:" for item in problem_desc if item.strip()]
    problem_desc = [item.replace('\r', '') if item != "Show Tags" else "Tags:" for item in problem_desc]

    if not problem_desc:
        print "no desc"
        return

    print problem_desc
    with open(num + "-" + title.replace(" ", "-")+".md", 'w') as f:
        f.write('##' + title + '\n')
        f.write('Source: ' + problem_url + "  \n")
        f.write('###Description\n')
        try:
            index = problem_desc.index("Tags:")
            f.write("  \n".join(problem_desc[:index]).encode('utf-8').rstrip() + "  \n###Tags\n" + ", ".join([item for item in problem_desc[index+1:] if item.strip()]) + "  \n")
        except:
            f.write("  \n".join(problem_desc[:index]).encode('utf-8').rstrip() + "  \n")

        f.write('###Solutions')

def getAllproblems(url):
    problem_set_root = get_doc_root(url)
    for tbl in problem_set_root.xpath('//table[@id="problemList"]'):
        for tr in tbl.xpath('.//tr'):
            problems = tr.xpath('.//td//text()')
            if problems:
                problem_num, problem_title, accept_rate,  level = problems[3], problems[5], problems[-2], problems[-1]
                write_to_solution_file(problem_num, problem_title)

def test():
    write_to_solution_file("1", "Two Sum")

if __name__ == "__main__":
    leetcode_problem_url = "https://oj.leetcode.com/problemset/algorithms/"
    getAllproblems(leetcode_problem_url)
