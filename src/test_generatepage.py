import unittest

from extract_title import extract_title
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType, text_node_to_html_node
from markdown_to_hnode import markdown_to_html_node

from generate_page import generate_page

import os, shutil

class test_generatepage(unittest.TestCase):
    def test_tolkien(self):
        from_path = "content/index.md" # markdown file, hence ".md" extension
        template_path = "template.html"
        dest_path = "public/index.html"

        with open(from_path) as f:
            file_contents = f.read()

        with open(template_path) as t:
            template_contents = t.read()
        
        generate_page(from_path, template_path, dest_path)
