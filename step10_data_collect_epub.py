from bs4 import BeautifulSoup
from ebooklib import epub, ITEM_DOCUMENT
import openai
from ebooklib import epub, ITEM_IMAGE

# tell top 6 operations to be done on epub file using Python

# 1. Extract Metadata
# 2. Read and Extract Text
# 3. Extract Images
# 4. Modify Metadata
# 5. Create New EPUBs
# 6. Convert Formats


path_book1 = "data\\epub\\book1.epub"
path_book2 = "data\\epub\\book2.epub"
path_book3 = "data\\epub\\book3.epub"
path_book4 = "data\\epub\\book4.epub"


# 1. Extract Metadata:
#           Retrieve core information like the book's title, author, language, and publication date.
book = epub.read_epub(path_book1)
title = book.get_metadata('DC', 'title')[0][0]
author = book.get_metadata('DC', 'creator')[0][0]
print(f"Title: {title}, Author: {author}")




# 2. Read and Extract Text:
#           Convert the internal (X)HTML documents into plain text.
#           This is useful for data analysis or creating text-to-speech applications.
book = epub.read_epub(path_book2)
for item in book.get_items_of_type(ITEM_DOCUMENT):
    soup = BeautifulSoup(item.get_content(), 'html.parser')
    text = soup.get_text()
    print(text[:100]) # Print first 100 characters




# 3. Extract Images:
#           Loop through all items in the book to find and save embedded images,
#           such as the cover or internal illustrations, to your local drive.
img_dump_path = "data\\epub\\img_dump\\"
book = epub.read_epub(path_book3)
for image in book.get_items_of_type(ITEM_IMAGE):
    with open(img_dump_path + os.path.basename(image.get_name()), 'wb') as f:
        f.write(image.get_content())




# 4. Modify Metadata:
#           Programmatically update a book's tags, series information, or author names without using a GUI like Calibre.
book = epub.read_epub(path_book3)
book.set_title('Updated Title')
book.add_author('New Author')
epub.write_epub(path_book3.replace(".epub", "_new.epub"), book)






# 5. Create New EPUBs:
#           Generate professional ebooks from scratch by bundling HTML, CSS, and images into a valid EPUB structure.
new_book = epub.EpubBook()
new_book.set_title('My New Book')
c1 = epub.EpubHtml(title='Introduction', file_name='intro.xhtml')
c1.content = '<h1>Welcome</h1><p>This is my first chapter.</p>'
new_book.add_item(c1)
new_book.spine = ['nav', c1]
epub.write_epub(path_book4, new_book)




# 6. Convert Formats:
#           Use Python scripts to automate the conversion of EPUB files to other formats like MOBI (using Calibre's CLI) or TXT.
full_text = []
book = epub.read_epub(path_book2)
for item in book.get_items_of_type(ITEM_DOCUMENT):
    soup = BeautifulSoup(item.get_content(), 'html.parser')
    full_text.append(soup.get_text())

with open(path_book2.replace(".epub", ".txt"), 'w', encoding='utf-8') as f:
    f.write('\n'.join(full_text))

