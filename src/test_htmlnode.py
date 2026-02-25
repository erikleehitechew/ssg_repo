import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType, text_node_to_html_node

class TestHTMLNode(unittest.TestCase):

    '''
    ####### v HTMLNode tests ######

    def test_eq(self):
        hnode1 = HTMLNode("a","",[],{
                "href": "https://www.google.com",
                "target": "_blank",
            })
        hnode2 = HTMLNode("a","",[],{
                "href": "https://www.google.com",
                "target": "_blank",
            })
        self.assertEqual(hnode1, hnode2)

    def test_neq(self):
        hnode1 = HTMLNode("a","",[],{
                "href": "https://www.google.com",
                "target": "_blank",
            })
        hnode2 = HTMLNode("a","",[],{
                "href": "https://www.bing.com",
                "target": "_blank",
            })

    def test_print(self):
        hnode1 = HTMLNode("a","",[],{
                "href": "https://www.google.com",
                "target": "_blank",
            })
        print(hnode1)

    def test_props(self):
        hnode1 = HTMLNode("a","",[],{
                "href": "https://www.google.com",
                "target": "_blank",
            })
        print(hnode1.props_to_html())

    ###### ^ HTMLNode tests ######
    '''

    '''
    ###### v LeafNode tests ######

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        #print("\n")
        #print(f"Node to HTML: {node.to_html()}")
        #print(f"Node as text: <p>Hello, world!</p>")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_tohtml_p(self):
        node_p = LeafNode("p", "This is a paragraph of text.").to_html()
        print("\n" + node_p)

    def test_tohtml_ahref(self):
        node_ahref = LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
        print("\n" + node_ahref)

    def test_tohtml_justtext(self):
        node_justtext = LeafNode(None, "Just text")
        print(node_justtext)

    def test_leaf_raw_text(self):
        node_justtext = LeafNode(None, "Just text")
        self.assertEqual(node_justtext.to_html(), "Just text")

    def test_leaf_to_html_a_multiple_props(self):
        node = LeafNode("a", "Click me!", {
            "href": "https://www.google.com",
            "target": "_blank",
        })
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\" target=\"_blank\">Click me!</a>")

    ###### ^ LeafNode tests ######
    '''

    '''
    ###### v ParentNode tests ######

    def test_parent_4children(self):
        node_p4 = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ]
        )

        print("\n" + node_p4.to_html())

    def test_parent_props(self):
        node_p1 = ParentNode(
                tag = "a",
                props = {"href": "https://www.google.com"},
                children = [LeafNode("i", "italic text")],
        )

        print("\n" + node_p1.to_html())

    def test_parent_notag(self):
        node_notag = ParentNode(
                tag = None,
                children = [LeafNode(None, "normal text")]
        )

        with self.assertRaises(ValueError):
            print("\n" + node_notag.to_html())

    def test_parent_nochildren(self):
        node_nochildren = ParentNode(
                tag = "a",
                children = None
        )
        
        with self.assertRaises(ValueError):
            print("\n" + node_nochildren.to_html())

    def test_parent_empty_children(self):
        node_emptychildren = ParentNode(
                tag = "a",
                children = []
        )

        with self.assertRaises(ValueError):
            print("\n" + node_emptychildren.to_html())
        

    ###### ^ ParentNode tests ######
    '''

    '''
    ###### v TextNode to HTMLNode tests ######

    
    def test_text(self):
        nodeTtH = TextNode("This is a text node", TextType.TEXT)
        print(f"\ntext: {nodeTtH.text}, \ntype: {nodeTtH.text_type}")
        html_node = text_node_to_html_node(nodeTtH)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        nodeBold = TextNode("This is a bold node", TextType.BOLD)
        print(f"\ntext: {nodeBold.text}, \ntype: {nodeBold.text_type}")
        html_node = text_node_to_html_node(nodeBold)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")

    def test_italic(self):
        nodeItalic = TextNode("This is an italic node", TextType.ITALIC)
        print(f"\ntext: {nodeItalic.text}, \ntype: {nodeItalic.text_type}")
        html_node = text_node_to_html_node(nodeItalic)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic node")

    def test_code(self):
        nodeCode = TextNode("This is a code node", TextType.CODE)
        print(f"\ntext: {nodeCode.text}, \ntype: {nodeCode.text_type}")
        html_node = text_node_to_html_node(nodeCode)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")

    def test_link(self):
        nodeLink = TextNode("This is a link node", TextType.LINK)
        print(f"\ntext: {nodeLink.text}, \ntype: {nodeLink.text_type}")
        html_node = text_node_to_html_node(nodeLink)
        print(html_node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
    
    def test_image(self):
        nodeImage = TextNode("This is an image node", TextType.IMAGE, "https://example.com/image.png")
        print(f"\ntext: {nodeImage.text}, \ntype: {nodeImage.text_type}")
        html_node = text_node_to_html_node(nodeImage)
        print(html_node)
        self.assertEqual(html_node.tag, "img")
        with self.assertRaises(AssertionError):
            self.assertEqual(html_node.value, "This is an image node")

    def test_boots(self):
        nodeBoots = TextNode("This is a Boots node", TextType.TEXT)
        nodeBoots.text_type = "boots"
        with self.assertRaises(Exception):
            text_node_to_html_node(nodeBoots)

    ###### ^ TextNode to HTMLNode tests ######
    '''

if __name__ == "__main__":
    unittest.main()
