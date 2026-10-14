#!/usr/bin/env python3

import os
from pypdf import PdfWriter

# Configuration
output_path = ""  # Enter the absolute path to your folder here, e.g., "C:/Users/YourUsername/Documents/PDFs"
output_filename = "merged_files.pdf"
files_to_merge = ["example1.pdf", "example2.pdf", "example3.pdf"]  # Replace with your actual PDF filenames


def merge_pdfs(pdf_list, folder_path):
    if not folder_path:
        print("❌ Error: Please provide a valid absolute path in 'output_path' before running.")
        return

    # Initialize the modern PdfWriter object
    writer = PdfWriter()
    
    # Loop through the list of PDF files and append them
    for pdf in pdf_list:
        # Build the complete path to find each certificate inside the folder
        full_pdf_path = os.path.join(folder_path, pdf)
        print(f"Appending: {full_pdf_path}")
        writer.append(full_pdf_path)
        
    # Combine the folder path and final output file name safely
    full_destination = os.path.join(folder_path, output_filename)
        
    # Open and write the data using a safe file variable 'f'
    with open(full_destination, "wb") as f:
        writer.write(f)
        
    writer.close()
    print(f"\n🎉 Successfully merged into: {full_destination}")


if __name__ == "__main__":
    # Run the function
    merge_pdfs(files_to_merge, output_path)
