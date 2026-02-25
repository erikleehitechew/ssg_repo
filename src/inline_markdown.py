from enum import Enum
from htmlnode import LeafNode
from nodes_delimiter import split_nodes_delimiter
from extract_markdown import extract_markdown_links, extract_markdown_images
from textnode import TextNode, TextType, split_nodes_image, split_nodes_link
import re

'''
Form an initial node from incoming text and a TextType of "TEXT."
Turn this node into a list, and then use that for testing.
Split by BOLD on asterisks
Split by ITALIC on underscores
Split by CODE on tildes
Then split by images
Then split by linnks
'''

def text_to_textnodes(text):
    
    initial_node = TextNode(text, TextType.TEXT)
    test_nodes = [initial_node]

    test_nodes = split_nodes_delimiter(test_nodes, "**", TextType.BOLD)
    test_nodes = split_nodes_delimiter(test_nodes, "_", TextType.ITALIC)
    test_nodes = split_nodes_delimiter(test_nodes, "`", TextType.CODE)
    test_nodes = split_nodes_image(test_nodes)
    test_nodes = split_nodes_link(test_nodes)

    return test_nodes
