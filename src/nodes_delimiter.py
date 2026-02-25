from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextType, TextNode, text_node_to_html_node

def split_nodes_delimiter(old_nodes, delimiter, text_type):
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
