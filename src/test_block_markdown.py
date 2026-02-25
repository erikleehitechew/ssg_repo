import unittest

from block_markdown import markdown_to_blocks
from blocktype import BlockType, block_to_block_type

class TestBlockMarkdown(unittest.TestCase):
    '''
    def test_markdown_to_blocks_bold(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_italic(self):
        md = """
This is _italic_ paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is _italic_ paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_big_block(self):
        md = """
This is a paragraph.



This is another paragraph.
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is a paragraph.",
                "This is another paragraph."
            ],
        )
    '''

class TestBlockType(unittest.TestCase): 
    '''
    def test_block_to_block_type(self):
        text_block = "Boots Boots Boots Boots"

        self.assertEqual(
            block_to_block_type(text_block),
            BlockType.PARAGRAPH
        )

    def test_heading1(self):
        test_heading = "# Heading"

        self.assertEqual(
            block_to_block_type(test_heading),
            BlockType.HEADING
        )

    def test_heading2(self):
        test_heading = "## Heading"

        self.assertEqual(
            block_to_block_type(test_heading),
            BlockType.HEADING
        )

    def test_heading3(self):
        test_heading = "### Heading"

        self.assertEqual(
            block_to_block_type(test_heading),
            BlockType.HEADING
        )

    def test_heading4(self):
        test_heading = "#### Heading"

        self.assertEqual(
            block_to_block_type(test_heading),
            BlockType.HEADING
        )

    def test_heading5(self):
        test_heading = "##### Heading"

        self.assertEqual(
            block_to_block_type(test_heading),
            BlockType.HEADING
        )

    def test_heading6(self):
        test_heading = "###### Heading"

        self.assertEqual(
            block_to_block_type(test_heading),
            BlockType.HEADING
        )

    def test_heading_toomanyhashes(self):
        test_heading = "####### Heading"

        self.assertEqual(
            block_to_block_type(test_heading),
            BlockType.PARAGRAPH
        )

    def test_heading_nospaces(self):
        test_heading = "######Heading"

        self.assertEqual(
            block_to_block_type(test_heading),
            BlockType.PARAGRAPH
        )

    def test_multiline_code_block(self):
        test_mc = """```
        There once was an ursine named Boots
        Who liked calculating square roots
        But then they got big
        And blew up his rig
        All that strained effort gave him the scoots
        ```"""

        self.assertEqual(
            block_to_block_type(test_mc),
            BlockType.CODE
        )

    def test_unordered_list(self):
        test_ul = """- Parsley
- Sage
- Rosemary
- Thyme""" # not being able to do """\n threw me off despite looking nicer

        self.assertEqual(
            block_to_block_type(test_ul),
            BlockType.UNORDERED_LIST
        )

    def test_ordered_list(self):
        test_ol = """1. The Fool
2. The Magician
3. The High Priestess
4. The Empress
5. The Emperor
6. The Hierophant
7. The Lovers
8. The Chariot
9. Strength
10. The Hermit
11. The Wheel of Fortune
12. Justice
13. The Hanged Man
14. Death
15. Temperance
16. The Devil
17. The Tower
18. The Star
19. The Moon
20. The Sun
21. Judgement
22. The World"""

        self.assertEqual(
            block_to_block_type(test_ol),
            BlockType.ORDERED_LIST
        )

    def test_wrong_order(self):
        test_wo = """2. The Fools
3. The Wise
4. The Judges"""

        self.assertEqual(
            block_to_block_type(test_wo),
            BlockType.PARAGRAPH
        )

    def test_list_no_space(self):
        test_lns = """1.The Fools
2.The Wise
3.The Judges"""

        self.assertEqual(
            block_to_block_type(test_lns),
            BlockType.PARAGRAPH
        )
    '''
