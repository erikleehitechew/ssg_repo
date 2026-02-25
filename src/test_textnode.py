import unittest

from htmlnode import HTMLNode
from nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType, split_nodes_link, split_nodes_image, text_to_textnodes

class TestTextNode(unittest.TestCase):

    '''
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url_none(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertIsNone(node.url)

    def test_diffTextType(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_diffURL(self):
        node = TextNode("This is a text node", TextType.BOLD, url = "www.google.com")
        node2 = TextNode("This is a text node", TextType.BOLD, url = "www.bing.com")
        self.assertNotEqual(node, node2)
    '''

    '''
    ###### v split images and links tests ######
    def test_split_images(self):
        node = TextNode(
                "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT,
            )
        print("\n")
        new_nodes = split_nodes_image([node])

        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
                "This is text with a [link](https://www.serebii.net) and another [link](https://www.google.com)", TextType.TEXT,
            )
        print("\n")
        new_nodes = split_nodes_link([node])

        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.serebii.net"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://www.google.com"
                ),
            ],
            new_nodes,
        )

    def test_no_links(self):
        node = TextNode(
                "This is text without a link.", TextType.TEXT,
            )
        print("\n")
        new_nodes = split_nodes_link([node])

        self.assertListEqual(
            [
                TextNode("This is text without a link.", TextType.TEXT, None
                ),
            ],
            new_nodes,
        )

    def test_no_images(self):
        node = TextNode(
                "This is text without an image.", TextType.TEXT,
            )
        print("\n")
        new_nodes = split_nodes_image([node])

        self.assertListEqual(
            [
                TextNode("This is text without an image.", TextType.TEXT, None
                ),
            ],
            new_nodes,
        )
    ###### ^ split images and links tests ######
    '''

    '''
    ###### v text to textnodes tests ######

    def test_text_to_textnodes(text):
        test_string = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

        initial_node = TextNode(test_string, TextType.TEXT)
        test_nodes = [initial_node]

        test_nodes = split_nodes_delimiter(test_nodes, "**", TextType.BOLD)
        test_nodes = split_nodes_delimiter(test_nodes, "_", TextType.ITALIC)
        test_nodes = split_nodes_delimiter(test_nodes, "`", TextType.CODE)
        test_nodes = split_nodes_link(test_nodes)
        test_nodes = split_nodes_image(test_nodes)

        print(test_nodes)

    ###### ^ text to textnodes tests ######
    '''

if __name__ == "__main__":
    unittest.main()
