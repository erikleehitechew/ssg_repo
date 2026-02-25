from htmlnode import HTMLNode
from markdown_to_hnode import markdown_to_html_node
import unittest

from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    '''
    def test_h1(self):
        md1 = """
    # Heading 1
    """

        h1_value = extract_title(md1)
        self.assertEqual(
            h1_value,"Heading 1")

    def test_h2(self):
        md2 = """
    ## Heading 2
    """
        
        with self.assertRaises(Exception) as h2err:
            extract_title(md2)
        self.assertEqual(str(h2err.exception), "Exception: No <h1> header found")
    '''
