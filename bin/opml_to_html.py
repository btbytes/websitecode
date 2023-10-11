#!/usr/bin/env python
"""
opml to html script.

started with ChatGPT. some cleanup afterwards

Pradeep Gowda
2023-10-11
"""

import xml.etree.ElementTree as ET
from datetime import datetime


def opml_to_html(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    categories = {}

    for outline in root.findall(".//outline"):
        if "xmlUrl" in outline.attrib:  # This is a blog
            category = outline.get("text")
            if category not in categories:
                categories[category] = []
            categories[category].append(outline)

    html = """<!doctype html>
<html>
<html lang="en" dir="ltr">
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="author" content="Pradeep Gowda">
<meta name="twitter:site" content="@btbytes">
<meta name="twitter:title" content="Test HTML">
<meta http-equiv="date" content="%s">
<meta http-equiv="last-modified" content="%s">
<meta name="keywords" content="opml,feeds">
<meta name="kind" content="page">
<link href=/css/site4.css rel=stylesheet>
<title>The blogs I read</title>
<body>
<article>
<header>
<h1>The blogs I read</title>
<address class="author">
By <a rel="author" class="url fn n" href="https://www.btbytes.com/">
Pradeep Gowda</a>
</address>
on <time pubdate datetime="%s" title="%s">%s</time>
</header>
<main>
<p>You can download the <code>.opml</code> file <a href="/feeds.opml">here</p>
 """ % (
        datetime.now().strftime("%Y-%m-%d"),
        datetime.now().strftime("%Y-%m-%d"),
        datetime.now().strftime("%Y-%m-%d"),
        datetime.now().strftime("%Y-%m-%d"),
        datetime.now().strftime("%B %d, %Y"),
    )

    for category, outlines in categories.items():
        # html += f"<h2>{category}</h2><ul>"
        for outline in outlines:
            title = outline.get("title", outline.get("text"))
            url = outline.get("xmlUrl")
            html += f"<li><a href='{url}'>{title}</a></li>"
        html += "</ul>"

    html += "</body></html>"

    return html


infile = "content/feeds.opml"
outfile = "content/feeds.html"
html_content = opml_to_html(infile)
with open(outfile, "w") as f:
    f.write(html_content)

print(f"Wrote {infile} to {outfile}")
