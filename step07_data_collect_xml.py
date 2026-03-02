import xml.etree.ElementTree as ET

# tell top 10 operations to be done on XML file using Python

# 1. Parsing an XML File
# 2. Accessing the Root Element
# 3. Finding Specific Elements
# 4. Searching with XPath
# 5. Reading and Modifying Text
# 6. Managing Attributes
# 7. Adding New Elements
# 8. Removing Elements
# 9. Validating Against a Schema (XSD)
# 10. Writing to a File



# 1. Parsing an XML File
# Loads 'data.xml' into an ElementTree object
try:
    tree = ET.parse('data.xml')
    root = tree.getroot()  # 2. Accessing the Root Element
except FileNotFoundError:
    # Creating a dummy root if file doesn't exist for demonstration
    root = ET.Element("catalog")
    tree = ET.ElementTree(root)

# 3. Finding & 5. Modifying Text
# Find the first element with the tag 'item' and change its text
item = root.find('item')
if item is not None:
    item.text = "Updated Item Name"

# 6. Managing Attributes
# Add or update an attribute on the root element
root.set('last_updated', '2030-01-01')

# 7. Adding New Elements
# Create a new 'product' sub-element under the root
new_product = ET.SubElement(root, 'product', id='101')
new_product.text = "New Python Guide"

# 8. Removing Elements
# Remove all elements with the tag 'old_data'
for old in root.findall('old_data'):
    root.remove(old)

# 10. Writing to a File
# Save changes back to the disk with an XML declaration
tree.write('output.xml', encoding='utf-8', xml_declaration=True)

print("XML operations complete. Check 'output.xml'.")
