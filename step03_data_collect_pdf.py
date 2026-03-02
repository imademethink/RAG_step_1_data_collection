from io import BytesIO
from PIL import Image
from pypdf import PdfReader, PdfWriter, Transformation
import pdfplumber
import pandas as pd
from playwright.sync_api import sync_playwright

# tell top 10 operations to be done on a pdf file using Python

# 1. reader object, rotate page
# 2. merge pdf
# 3. split pdf
# 4. watermarking
# 5. extract table from pdf
# 6. html to pdf
# 7. compress pdf
    # extract image from pdf and save separately, then apply easyocr (OCR)
    # Generate Dynamic Reports from Scratch using ReportLab package
    # Transform PDFs into Images (and Vice Versa)
# 8. encrypt and decrypt pdf
# 9. extract images from within pdf
# 10. Chunking data and extracting it with metadata
# 11. to arrange llama index






base_pdf_path = "data\\pdf\\"
pdf_path = "data\\pdf\\lenscart.pdf"
pdf_path2 = "data\\pdf\\zomato.pdf"
pdf_table1 = "data\\pdf\\table1.pdf"
watermark_img_path = "data\\pdf\\watermark.png"
html_to_pdf_path = "data\\pdf\\html_to_pdf.pdf"
pdf_path_new = pdf_path.replace(".pdf", "_new.pdf")
pdf_path_merged = pdf_path.replace(".pdf", "_merged.pdf")
pdf_path_split = pdf_path2.replace(".pdf", "_split.pdf")
pdf_path_watermark = pdf_path2.replace(".pdf", "_watermark.pdf")


# reader object
pdf_rdr = PdfReader(pdf_path)

# total pages
print(len(pdf_rdr.pages))

# print all page content
full_text = ""
for one_page in pdf_rdr.pages:
    full_text += one_page.extract_text()
print(full_text)

# rotate page + save in a new file
rotation_angle = 90 # Must be an increment of 90 deg.
pdf_wtr = PdfWriter()
page0 = pdf_rdr.pages[0]
page0.rotate(angle=rotation_angle)
pdf_wtr.add_page(page0)
with open(pdf_path_new, 'wb') as newFile:
    pdf_wtr.write(newFile)

# merge pdf
pdf_wtr.append(pdf_path)
with open(pdf_path_merged, 'wb') as newFile:
    pdf_wtr.write(newFile)

# split pdf
pdf_rdr2 = PdfReader(pdf_path2)
pdf_wtr2 = PdfWriter()
pdf_wtr2.add_page(pdf_rdr2.pages[1])
pdf_wtr2.add_page(pdf_rdr2.pages[2])
with open(pdf_path_split, 'wb') as newFile:
    pdf_wtr2.write(newFile)

# watermarking
img = Image.open(watermark_img_path)
img_as_pdf = BytesIO()
img.save(img_as_pdf, "PDF")
img_as_pdf.seek(0)
pdf_rdr3 = PdfReader(pdf_path2)
pdf_wtr3 = PdfWriter()
stamp_page = PdfReader(img_as_pdf).pages[0]
for one_page in pdf_rdr3.pages:
    one_page.merge_transformed_page(page2=stamp_page, ctm=Transformation(), over=False)
    pdf_wtr3.add_page(one_page)
with open(pdf_path_watermark, "wb") as fp:
    pdf_wtr3.write(fp)




# extract table from pdf
table_settings = {
    "vertical_strategy": "text",
    "horizontal_strategy": "text"
}
pdf_rdr4 = pdfplumber.open(pdf_table1)
table0=pdf_rdr4.pages[0].extract_table(table_settings)
print(pd.DataFrame(table0[1::],columns=table0[0]))
# future scope pdf-table to csv or excel






# html to pdf
url1 = "https://www.nzpostbusinessiq.co.nz/latest-ecommerce-insights"
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto(url1)
    page.pdf(path=html_to_pdf_path, format="A4", print_background=True)
    browser.close()




# compress pdf
# extract image from pdf and save separately, then apply easyocr (OCR)
# Generate Dynamic Reports from Scratch using ReportLab package
# Transform PDFs into Images (and Vice Versa)





# encrypt and decrypt pdf
def encrypt_pdf(input_pdf, output_pdf, password):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    # Add all pages from the original PDF to the writer
    for page in reader.pages:
        writer.add_page(page)

    # Encrypt with the specified password
    # Recommended algorithm: "AES-256-R5" for strong security
    writer.encrypt(user_password=password, algorithm="AES-256-R5")

    with open(output_pdf, "wb") as f:
        writer.write(f)
    print(f"File encrypted and saved as {output_pdf}")

def decrypt_pdf(input_pdf, output_pdf, password):
    reader = PdfReader(input_pdf)

    # Check if the file is actually encrypted
    if reader.is_encrypted:
        # Returns 1 (User password) or 2 (Owner password) if successful
        status = reader.decrypt(password)
        if status == 0:
            print("Incorrect password.")
            return

    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)

    with open(output_pdf, "wb") as f:
        writer.write(f)
    print(f"File decrypted and saved as {output_pdf}")


pdf_path_encrypted = pdf_path2.replace(".pdf","_encrypted.pdf")
pdf_path_decrypted = pdf_path_encrypted.replace("_encrypted.pdf","_decrypted.pdf")
pdf_password = "password123"
encrypt_pdf(input_pdf=pdf_path2, output_pdf=pdf_path_encrypted, password=pdf_password)
decrypt_pdf(input_pdf=pdf_path_encrypted, output_pdf=pdf_path_decrypted, password=pdf_password)





import pymupdf4llm

# Standard text and tables are detected, brought in the right reading sequence and
# then together converted to GitHub-compatible Markdown text.
md_text = pymupdf4llm.to_markdown(doc=pdf_path2)
print(md_text)


# extract images from within pdf
pymupdf4llm.to_markdown(doc=pdf_path, page_chunks=True, write_images=True,
                        image_path=base_pdf_path + "extracted_images", image_format="png", dpi=300)


# Chunking data and extracting it with metadata
md_text_chunks = pymupdf4llm.to_markdown(doc=pdf_path, pages=[0,1], page_chunks=True)
for one_itr in md_text_chunks:
    print(one_itr["text"])
    print("\n\n\n====================\n\n\n")


# to arrange llama index
import pymupdf4llm
llama_reader = pymupdf4llm.LlamaMarkdownReader()
llama_docs = llama_reader.load_data(pdf_path)
print(f"Number of LlamaIndex documents: {len(llama_docs)}")
print(f"Content of first document: {llama_docs[0].text[:500]}")

