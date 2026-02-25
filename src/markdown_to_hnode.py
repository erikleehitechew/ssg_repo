from enum import Enum
from block_markdown import markdown_to_blocks
from blocktype import block_to_block_type, BlockType
from extract_markdown import extract_markdown_links, extract_markdown_images
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node
import re


def markdown_to_html_node(markdown):
    md_blocks = markdown_to_blocks(markdown) # blocks returned

    block_nodes = []

    for md_block in md_blocks:
        #md_block = md_block.replace("\n", " ").strip()
        md_blocktype = block_to_block_type(md_block) # returns BlockType from enum list
        #print("BLOCKTYPE:", md_blocktype)

        if md_blocktype == BlockType.CODE:
            '''
            while md_block.startswith("`"):
                md_block = md_block[1:]

            while md_block.endswith("`"):
                md_block = md_block[:-1]
            '''
            md_block = md_block[3:-3].lstrip("\n")

            c_textNode = TextNode(md_block, TextType.TEXT)
            c_HTMLNode = text_node_to_html_node(c_textNode)

            codeNode = ParentNode("code", [c_HTMLNode])
            preNode  = ParentNode("pre", [codeNode])
            block_nodes.append(preNode)
        elif md_blocktype == BlockType.PARAGRAPH:
            md_block = md_block.replace("\n", " ").strip()
            # 1. Get the list of inline children
            children = text_to_children(md_block)
            # 2. Wrap them in a paragraph ParentNode
            paragraph_node = ParentNode("p", children) # p = 'paragraph' tag
            # 3. Save it to your list of blocks
            block_nodes.append(paragraph_node)
        elif md_blocktype == BlockType.HEADING:
            # 1. Clean the block to get the level and the actual text
            hashcount = 0
            while md_block.startswith("#"):
                hashcount += 1
                md_block = md_block[1:]

            clean_mdblock = md_block.strip()

            # 2. Convert that text into inline HTMLNode children
            children = text_to_children(clean_mdblock)

            # 3. Create the ParentNode for this block
            heading_tag = f"h{hashcount}" #h1, h2, h3, h4, h5, or h6
            heading_node = ParentNode(heading_tag, children)

            # 4. Save this block node to your list
            block_nodes.append(heading_node)
        elif md_blocktype == BlockType.QUOTE:
            md_blocklines = md_block.split("\n")

            clean_lines = []
            for line in md_blocklines:
                clean_line = line.lstrip(">").strip() # removes left > and any whitespace
                clean_lines.append(clean_line)

            quote_text = " ".join(clean_lines)

            children = text_to_children(quote_text)
            bq_node = ParentNode("blockquote", children)
            block_nodes.append(bq_node)

        elif md_blocktype == BlockType.UNORDERED_LIST:
            mdblock_lines = md_block.split("\n")

            ul_nodes = []
            for line in mdblock_lines:
                clean_line = line[2:]
                children = text_to_children(clean_line)
                ul_node = ParentNode("li", children)
                ul_nodes.append(ul_node)

            ul_ParentNode = ParentNode("ul", ul_nodes)
            block_nodes.append(ul_ParentNode)
        elif md_blocktype == BlockType.ORDERED_LIST:
            mdblock_lines = md_block.split("\n")

            ol_nodes = []
            for line in mdblock_lines:
                parts = line.split(". ", 1)
                clean_text = parts[1]
                children = text_to_children(clean_text)
                ol_node = ParentNode("li", children)
                ol_nodes.append(ol_node)

            ol_ParentNode = ParentNode("ol", ol_nodes)
            block_nodes.append(ol_ParentNode)

    div_node = ParentNode("div", block_nodes)
    return div_node

# using text_to_textnodes version from inline_markdown.py
def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = [] # list
    for t_node in text_nodes:
        h_node = text_node_to_html_node(t_node) # converting TextNode -> HTMLNode
        children.append(h_node)
    return children # list of HTMLNodes
