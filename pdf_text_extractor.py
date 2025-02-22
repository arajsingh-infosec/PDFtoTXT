import os
import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2
import time
from tqdm import tqdm

def select_pdf_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select a PDF file", filetypes=[("PDF Files", "*.pdf")])
    return file_path

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        num_pages = len(reader.pages)
        for i in tqdm(range(num_pages), desc="Extracting PDF content", unit="page"):
            time.sleep(0.1)
            text += reader.pages[i].extract_text() + "\n"
    return text

def select_destination_folder():
    root = tk.Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory(title="Select Destination Folder")
    return folder_selected

def save_text_file(text, destination_folder, pdf_filename):
    txt_filename = os.path.splitext(pdf_filename)[0] + ".txt"
    txt_path = os.path.join(destination_folder, txt_filename)
    with open(txt_path, "w", encoding="utf-8") as txt_file:
        txt_file.write(text)
    messagebox.showinfo("Success", f"Text file saved at: {txt_path}")

def main():
    pdf_path = select_pdf_file()
    if not pdf_path:
        messagebox.showwarning("No File Selected", "Please select a PDF file.")
        return
    messagebox.showinfo("Processing", "Extracting text from PDF, please wait...")
    extracted_text = extract_text_from_pdf(pdf_path)
    destination_folder = select_destination_folder()
    if not destination_folder:
        messagebox.showwarning("No Destination Selected", "Please select a destination folder.")
        return
    save_text_file(extracted_text, destination_folder, os.path.basename(pdf_path))
    messagebox.showinfo("Done", "PDF text extraction and saving completed successfully!")

if __name__ == "__main__":
    main()
