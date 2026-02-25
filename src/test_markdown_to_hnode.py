import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType, text_node_to_html_node
from markdown_to_hnode import markdown_to_html_node

class TestMarkdownToNode(unittest.TestCase):
    '''
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
        "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
        "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_orderedlist(self):
        md = """
1. Parsley
2. Sage
3. Rosemary
4. Thyme
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
        "<div><ol><li>Parsley</li><li>Sage</li><li>Rosemary</li><li>Thyme</li></ol></div>",
        )

    def test_unorderedlist(self):
        md = """
Boots
Bear
Down
Under
Tree
Fiddy
Frisky
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
        "<div><p>Boots Bear Down Under Tree Fiddy Frisky</p></div>",
        )

    def test_quoteblock(self):
        md = """
> chan
> text
> looks
> like
> this
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
        "<div><blockquote>chan text looks like this</blockquote></div>",
        )

    def test_heading1(self):
        md = """
# Heading text
"""
        node = markdown_to_html_node(md)
        print(f"\nNode tag: {node.children[0].tag}")
        print(f"\nNode value: {node.children[0].children[0].value}")
        html = node.to_html()
        self.assertEqual(
            html,
        "<div><h1>Heading text</h1></div>",
        )

    def test_heading6(self):
        md = """
###### Heading text
"""
        node = markdown_to_html_node(md)
        print(f"\nNode tag: {node.children[0].tag}")
        print(f"\nNode value: {node.children[0].children[0].value}")
        html = node.to_html()
        self.assertEqual(
            html,
        "<div><h6>Heading text</h6></div>",
        )
        '''

if __name__ == "__main__":
    unittest.main()
