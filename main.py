import os
import PyPDF2
import subprocess


def merge_pdfs_in_directory(directory_path, output_path):
    # Create a PDF writer object
    pdf_writer = PyPDF2.PdfWriter()

    # Loop through all files in the directory
    for filename in os.listdir(directory_path):
        # Check if the file is a PDF
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(directory_path, filename)

            # Open the PDF file
            with open(pdf_path, 'rb') as pdf_file:
                pdf_reader = PyPDF2.PdfReader(pdf_file)

                # Add all pages from the PDF to the writer
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    pdf_writer.add_page(page)

    # Write the merged PDF to the output file
    with open(output_path, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)

    print(f"All PDFs in '{directory_path}' have been merged successfully into '{output_path}'.")

def compress_pdf_ghostscript(input_pdf, output_pdf, quality="screen"):
    """Quality options: screen, ebook, printer, prepress
    # For web viewing or smallest file size → /screen
    # For reading on devices (Kindle, tablets) → /ebook
    # For normal printing (home/office) → /printer
    # For high-end publishing (magazines, press) → /prepress
    """
    gs_command = [
        "gswin64", "-sDEVICE=pdfwrite", "-dCompatibilityLevel=1.4",
        f"-dPDFSETTINGS=/{quality}", "-dNOPAUSE", "-dBATCH",
        f"-sOutputFile={output_pdf}", input_pdf
    ]

    subprocess.run(gs_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    print(f"Original Size: {os.path.getsize(input_pdf) / 1024:.2f} KB")
    print(f"Compressed Size: {os.path.getsize(output_pdf) / 1024:.2f} KB")




# Example usage
directory_path = r"D:\Bewerbungen\ThomasFejes\temp"  # Change this to your PDF directory
output_path_4_merged_pdfs = directory_path + r'\merged_output.pdf'  # Path for the merged PDF
merge_pdfs_in_directory(directory_path, output_path_4_merged_pdfs)
pdf_file_path = r"D:\Bewerbungen\ThomasFejes_Profil.pdf"
pdf_file_compressed_path = r"D:\Bewerbungen\ThomasFejes_Profil_compressed.pdf"
# compress_pdf_ghostscript(pdf_file_path, pdf_file_compressed_path, quality="ebook")

