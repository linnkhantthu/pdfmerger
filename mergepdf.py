from PyPDF2 import PdfMerger
import os
import re
import sys

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))


print("Current Directory: ")

# List all PDF files in the directory that start with a number
files = [f for f in os.listdir(current_dir) if f.endswith(
    '.pdf') and re.match(r'^\d', f)]

# Function to extract the number from the file name for sorting

print("Found PDF files: ", files)


def extract_number(file_name):
    match = re.match(r'(\d+)', file_name)
    return int(match.group(1)) if match else float('inf')


# Sort the PDF files using the extracted number
sorted_files = sorted(files, key=extract_number)

print("Sorted PDF files: ", sorted_files)

# Create a PdfMerger object
merger = PdfMerger()

# Loop through all PDFs and append them
for file in sorted_files:
    merger.append(file)

# Write the merged PDF to a new file
merger.write("mergedFile.pdf")
print("Merged PDF files successfully.")
merger.close()
print("Finished")
