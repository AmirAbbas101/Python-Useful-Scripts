import fitz  # PyMuPDF
import os

def reduce_pdf_size(input_path, output_path):
    # Open the original PDF
    doc = fitz.open(input_path)

    # Create a new PDF for the compressed version
    new_doc = fitz.open()

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)

        # Extract the image of the page
        pix = page.get_pixmap()

        # Create a new page in the new document with the same dimensions
        new_page = new_doc.new_page(width=page.rect.width, height=page.rect.height)

        # Insert the image into the new page
        new_page.insert_image(new_page.rect, pixmap=pix)

    # Save the new document
    new_doc.save(output_path)
    new_doc.close()
    doc.close()

    print("PDF size reduced successfully!")

if __name__ == "__main__":
    input_path = "C:\\Users\\Amir_Abbas\\Desktop\\Learning\\pdf-compressor-master\\Resume.pdf"
    output_path = "C:\\Users\\Amir_Abbas\\Desktop\\Learning\\pdf-compressor-master\\Resume_compressed.pdf"

    reduce_pdf_size(input_path, output_path)
