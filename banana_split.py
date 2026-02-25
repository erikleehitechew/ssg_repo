from src.extract_markdown import extract_markdown_links, extract_markdown_images

current_text = "I like apples and I like bananas too but I like apples more than I like bananas today"
find_words = ["apples", "bananas"]

new_nodes = []
for word in find_words:
    sections = current_text.split(word, 1)
    # sections[0] is everything before the word
    # sections[1] is everything after
    print(f"Before: {sections[0]}")
    print(f"The word: {word}")
    current_text = sections[1] # We 'zoom in' on the rest of the string

# After the loop
print(f"Leftover: {current_text}")
