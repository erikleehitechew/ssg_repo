import unittest

from htmlnode import HTMLNode
from nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType, split_nodes_link, split_nodes_image
from inline_markdown import text_to_textnodes

'''
###### v text to textnodes tests ######
class TestInlineMarkdown(unittest.TestCase):

    def test_text_to_textnodes(self):
        test_string = "This is **text** with an _italic_ word"

        nodes = text_to_textnodes(test_string)
        self.assertEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            nodes
        )
###### ^ text to textnodes tests ######

class TestInlineMarkdown_code(unittest.TestCase):

    def test_code_to_textnodes(self):
        test_string = "This is `code` with an _italic_ word"

        nodes = text_to_textnodes(test_string)
        self.assertEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            nodes
        )

class TestInlineMarkdown_image(unittest.TestCase):

    def test_image_to_textnodes(self):
        test_string = "This is `code` with an _italic_ word and an ![image](https://i.imgur.com/fJRm4Vk.jpeg)"

        nodes = text_to_textnodes(test_string)
        self.assertEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg")
            ],
            nodes
        )

class TestInlineMarkdown_link(unittest.TestCase):

    def test_link_to_textnodes(self):
        test_string = "This is `code` with an _italic_ word and a [link](https://www.google.com)"

        nodes = text_to_textnodes(test_string)
        self.assertEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.google.com")
            ],
            nodes
        )

class TestInlineMarkdown_both(unittest.TestCase):

    def test_link_to_textnodes(self):
        test_string = "This is `code` with an _italic_ word and both an ![image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://www.google.com)"

        nodes = text_to_textnodes(test_string)
        self.assertEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and both an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.google.com")
            ],
            nodes
        )
    '''

if __name__ == "__main__":
    unittest.main()
