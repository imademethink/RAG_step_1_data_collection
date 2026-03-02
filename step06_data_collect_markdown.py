import markdown
import frontmatter
import os, re, requests


# tell top 10 operations to be done on .md (mark down) file using Python

# 1. Read and Write Markdown Files
# 2. Convert Markdown to HTML
# 3. Convert HTML back to Markdown
# 4. Manage Front Matter (Metadata)
# 5. Extract Specific Elements
# 6. Find and Replace with Regex
# 7. Generate a Table of Contents (TOC)
# 8. Automate Indexing
# 9. Syntax Highlighting for Code Blocks
# 10. Validate Links and Images



# 1. Read and Write Markdown Files
# Write a new Markdown file
with open('example.md', 'w', encoding='utf-8') as f:
    f.write("# Hello World\nThis is a sample markdown file.")
# Read the content
with open('example.md', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)



# 2. Convert Markdown to HTML
with open('example.md', 'r') as f:
    text = f.read()
html = markdown.markdown(text)
with open('example.html', 'w') as f:
    f.write(html)

# 3. Convert HTML back to Markdown
from markdownify import markdownify as md
html = "<h1>Title</h1><p>This is <b>bold</b> text.</p>"
markdown_text = md(html, heading_style="ATX")
print(markdown_text) # Output: # Title\n\nThis is **bold** text.


# 4. Manage Front Matter (Metadata)
# Load file with YAML metadata
post = frontmatter.load('example.md')
print(post['title']) # Access metadata like a dict
# Update metadata
post['date'] = '2030-03-30'
with open('example.md', 'wb') as f:
    f.write(frontmatter.dumps(post).encode('utf-8'))


# 5. Extract Specific Elements
# Simple Regex to extract all H2 headers
with open('example.md', 'r') as f:
    content = f.read()
    headers = re.findall(r'^## (.*)', content, re.MULTILINE)
    print(headers)

# 6. Find and Replace with Regex
with open('example.md', 'r') as f:
    content = f.read()
# Replace all old local image paths with a CDN URL
new_content = re.sub(r'!\[(.*?)\]\(images/(.*?)\)', r'![\1](https://cdn.com\2)', content)
with open('example.md', 'w') as f:
    f.write(new_content)


# 7. Generate a Table of Contents (TOC)
md_text = "[TOC]\n# Section 1\n## Sub 1\n# Section 2"
html = markdown.markdown(md_text, extensions=['toc'])
print(html) # Includes a nested <ul> list of headers


# 8. Automate Indexing
files = [f for f in os.listdir('.') if f.endswith('.md')]
with open('index.md', 'w') as index:
    index.write("# Site Index\n\n")
    for f in sorted(files):
        index.write(f"- [{f}]({f})\n")


# 9. Syntax Highlighting for Code Blocks
md_text = "```python\nprint('hello')\n```"
html = markdown.markdown(md_text, extensions=['codehilite'])
# Output contains <div> with syntax-specific classes


# 10. Validate Links and Images
with open('example.md', 'r') as f:
    links = re.findall(r'\[.*?\]\((http.*?)\)', f.read())
for link in links:
    status = requests.get(link).status_code
    print(f"{link}: {status}")
