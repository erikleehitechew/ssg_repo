from enum import Enum
from extract_markdown import extract_markdown_links, extract_markdown_images
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(text):
    
    if text.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ",)):
        return BlockType.HEADING
    elif text.strip().startswith("```") and text.strip().endswith("```"):
        return BlockType.CODE
    elif text.startswith(">"):
        for line in text.split("\n"):
            if line.startswith(">") == False:
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    elif text.startswith("- "):
        for line in text.split("\n"):
            if line.startswith("- ") == False:
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    elif text.startswith("1. "):
        ordered_list_lines = text.split("\n")
        for ol_index, line in enumerate(ordered_list_lines):
            if line.startswith(f"{ol_index + 1}. ") == False:
                return BlockType.PARAGRAPH
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
