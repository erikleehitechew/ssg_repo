import os, sys, shutil
from textnode import TextType, TextNode

from gencontent import generate_page, generate_pages_recursive

# print("hello world")

def copy_files_recursive(current_path, destination):

    basepath = "/"

    sys.argv[0] = basepath


    if not os.path.exists(destination):
        os.mkdir(destination)
    

    items = os.listdir(current_path)

    for item in items:
        from_path = os.path.join(current_path, item)
        to_path = os.path.join(destination, item)

        # Create the full path to this item

        if os.path.isdir(from_path):
            # If it's a folder, we need to "walk" inside it
            copy_files_recursive(from_path, to_path)
        else:
            # If it's a file, we just copy it
            # print(f"From path: {from_path}")
            shutil.copy(from_path, to_path)

def main():
    #testnode = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    #print(testnode)
    if os.path.exists("./public"):
        shutil.rmtree("./public") # remove current public folder

    copy_files_recursive("./static", "./public")
    
    from_path = sys.argv[1]
    template_path = sys.argv[2]
    dest_dir = sys.argv[3]

    if os.path.isdir(from_path):
        generate_pages_recursive(from_path, template_path, dest_dir)
    else:
        generate_page(from_path, template_path, os.path.join(dest_dir, "index.html"))

main()
