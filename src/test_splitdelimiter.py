import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType, text_node_to_html_node
from nodes_delimiter import split_nodes_delimiter

class TestSplitDelim(unittest.TestCase):

    '''
    def test_codeblock(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        print(split_nodes_delimiter([node], "`", TextType.CODE))

    def test_multicode(self):
        node = TextNode("This is `code block 1` and this is `code block 2`", TextType.TEXT)
        print(split_nodes_delimiter([node], "`", TextType.CODE))

    def test_emptyfirst(self):
        node = TextNode("`code block` word", TextType.TEXT)
        print(split_nodes_delimiter([node], "`", TextType.CODE))

    def test_emptylast(self):
        node = TextNode("word `code block`", TextType.TEXT)
        print(split_nodes_delimiter([node], "`", TextType.CODE))

    def test_nodelist(self):
        nodes = [
                TextNode("word `code block` test", TextType.TEXT),
                TextNode("word `code block` test", TextType.CODE),
            ]
        print(split_nodes_delimiter(nodes, "`", TextType.TEXT))

    def test_incomplete(self):
        node = TextNode("Text `code block", TextType.TEXT)

        with self.assertRaises(Exception):
            print(split_nodes_delimiter([node], "`", TextType.CODE))
    '''
    pass
