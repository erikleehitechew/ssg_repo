from extract_title import extract_title
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType, text_node_to_html_node
from markdown_to_hnode import markdown_to_html_node

import os, shutil

def generate_page(from_path, template_path, dest_path):
    with open(from_path) as f:
        frompath_contents = f.read()

    with open(template_path) as t:
        templatepath_contents = t.read()

    pagetitle = extract_title(frompath_contents)
    mdfile = markdown_to_html_node(frompath_contents) # ParentNode 
    htmlstring = mdfile.to_html()

    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    #print(f"Page title: {pagetitle}")

    templatepath_contents = templatepath_contents.replace("{{ Title }}", pagetitle).replace("{{ Content }}", htmlstring)

    os.makedirs(os.path.dirname(dest_path), exist_ok = True)

    with open(dest_path, "w") as d:
        d.write(templatepath_contents)

def generate_pages_recursive(content_dir, template_path, dest_dir):
    for root, _, files in os.walk(content_dir):
        for file in files:
            if file != "index.md":
                continue # keep looking for directories
            md_path = os.path.join(root, file)

            rel_dir = os.path.relpath(root, content_dir) # e.g., blog/glorfindel
            out_dir = os.path.join(dest_dir, rel_dir)    # public/blog/glorfindel
            os.makedirs(out_dir, exist_ok = True)

            html_path = os.path.join(out_dir, "index.html")
            generate_page(md_path, template_path, html_path)
