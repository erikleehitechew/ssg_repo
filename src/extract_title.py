from htmlnode import HTMLNode
from markdown_to_hnode import markdown_to_html_node

def extract_title(markdown):
    node = markdown_to_html_node(markdown)

    #print(f"Node children: {node.children}")
    for child in node.children:
        if child.tag == "h1":
            return child.children[0].value
    raise Exception("Exception: No <h1> header found")
