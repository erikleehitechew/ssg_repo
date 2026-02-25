import re, os, sys

def extract_markdown_images(text):
    regex_pattern = r"!\[(.*?)\]\((.*?)\)"
    regex_matches = re.findall(regex_pattern, text)
    return regex_matches

def extract_markdown_links(text):
    regex_pattern = r"(?<!\!)\[(.*?)\]\((.*?)\)"
    regex_matches = re.findall(regex_pattern, text)
    return regex_matches
