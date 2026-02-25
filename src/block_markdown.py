def markdown_to_blocks(markdown): # representing a full document
    blocks = markdown.split("\n\n")
    #print(heading_test)

    blocks_to_return = []
    for i in range(len(blocks)):
        blocks[i] = blocks[i].strip()
        if blocks[i] == "":
            blocks[i] = None
        else:
            blocks_to_return.append(blocks[i])
        #print(f"Block {i + 1}:\n{blocks[i]}")
    return(blocks_to_return)

'''
heading_test = """
# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item
    """

markdown_to_blocks(heading_test)
'''
