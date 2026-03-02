import os
from email import policy
from email.parser import BytesParser
import extract_msg




# Email processing : .eml, .msg file

# 1. Parse the .eml file
# 2. Extract Metadata (Headers)
# 3. Extract Email Body (Plain Text and HTML)
# 4. Extract and Save Attachments

# 1. Extract Metadata (Headers) from .msg file
# 2. Extract Email Body
# 3. Extract and Save Attachments








eml_file_path = "data\\emails\\demo_subject_1.eml"
output_attachments_dir = "data\\emails\\extracted_attachments"

if not os.path.exists(output_attachments_dir):
    os.makedirs(output_attachments_dir)

# 1. Parse the .eml file
with open(eml_file_path, 'rb') as fp:
    # Use policy.default for a high-level, easy-to-use API
    msg = BytesParser(policy=policy.default).parse(fp)

# 2. Extract Metadata (Headers)
print(f"Subject==>: {msg['subject']}")
print(f"From==>: {msg['from']}")
print(f"To==>: {msg['to']}")
print(f"Date==>: {msg['date']}")

# 3. Extract Email Body (Plain Text and HTML)
# get_body() automatically finds the best part based on preference
body_text = msg.get_body(preferencelist=('plain')).get_content()
print(f"\nBody Snippet==>:\n{body_text[:100]}...")

# 4. Extract and Save Attachments
for attachment in msg.iter_attachments():
    filename = attachment.get_filename()
    if filename:
        print(f"Saving attachment==>: {filename}")
        filepath = os.path.join(output_attachments_dir, filename)
        with open(filepath, 'wb') as f:
            f.write(attachment.get_payload(decode=True))







msg_file_path = "data\\emails\\demo_subject_1.msg"
attachment_dir = "data\\emails\\extracted_attachments"
if not os.path.exists(attachment_dir):
    os.makedirs(attachment_dir)

msg = extract_msg.openMsg(msg_file_path)

# 1. Extract Metadata (Headers) from .msg file
print(f"Subject===>: {msg.subject}")
print(f"From===>: {msg.sender}")
print(f"To===>: {msg.to}")
print(f"Date===>: {msg.date}")

# 2. Extract Email Body
# You can choose between plain text, HTML, or RTF
print(f"\nPlain Text Body Snippet:\n{msg.body}...")
# msg.htmlBody is also available for HTML content

# 3. Extract and Save Attachments
for attachment in msg.attachments:
    # Get the filename (handles cases where filename might be missing)
    filename = attachment.longFilename or attachment.shortFilename or "attachment.bin"
    print(f"Saving attachment===>: {filename}")

    # Save to disk
    save_path = os.path.join(attachment_dir, filename)
    with open(save_path, "wb") as f:
        f.write(attachment.data)

msg.close()


