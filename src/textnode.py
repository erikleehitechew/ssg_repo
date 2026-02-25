from enum import Enum
from htmlnode import LeafNode
from extract_markdown import extract_markdown_links, extract_markdown_images
import re

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (self.text == other.text and self.text_type == other.text_type and self.url == other.url)

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def split_nodes_link(inputNodes):
    result_nodes = []
    for node in inputNodes:
        if node.text_type != TextType.TEXT:
            result_nodes.append(node)
            continue
        links = extract_markdown_links(node.text)
        remaining_text = node.text
        for link in links:
            image_alt = link[0]
            image_link = link[1]
            sections = remaining_text.split(f"[{image_alt}]({image_link})", 1)
            if sections[0] != "":
                result_nodes.append(TextNode(sections[0], TextType.TEXT))
            result_nodes.append(TextNode(image_alt, TextType.LINK, image_link))
            remaining_text = sections[1]
        if remaining_text != "":
            result_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return result_nodes

def split_nodes_image(inputNodes):
    result_nodes = []
    for node in inputNodes:
        if node.text_type != TextType.TEXT:
            result_nodes.append(node)
            continue
        images = extract_markdown_images(node.text)
        remaining_text = node.text
        for image in images:
            alt_text = image[0]
            image_url = image[1]
            sections = remaining_text.split(f"![{alt_text}]({image_url})", 1)
            if sections[0] != "":
                result_nodes.append(TextNode(sections[0], TextType.TEXT))
            result_nodes.append(TextNode(alt_text, TextType.IMAGE, image_url))
            remaining_text = sections[1]
        if remaining_text != "":
            result_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return result_nodes

    '''
    new_nodes = []
    for node in old_nodes: # Outer loop
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            node_split = node.text.split(delimiter)
            if len(node_split) % 2 != 1: # if text only splits on a delimiter once, where's the matching delimiter?
                raise Exception("matching closing delimiter not found")
            for i, node_to_text in enumerate(node_split):
                if i % 2 == 1:
                    node_text = TextNode(f"{node_to_text}", text_type)
                else:
                    node_text = TextNode(f"{node_to_text}", node.text_type)
                new_nodes.append(node_text)
    return new_nodes
    '''

def text_to_textnodes(text):
    # see version from inline_markdown
    return text

def text_node_to_html_node(text_node):
    if text_node.text_type not in TextType:
        raise ValueError("text node's type not valid")

    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, props = {"href": text_node.url}) #.text = anchor text
        case TextType.IMAGE:
            return LeafNode("img", value = "", props = {"src": text_node.url, "alt": text_node.text})
