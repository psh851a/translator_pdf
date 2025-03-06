import tkinter as tk
from tkinter import filedialog, messagebox
from tkinterdnd2 import DND_FILES, TkinterDnD
from pdf_processor import extract_text_from_pdf, create_bilingual_pdf
from translator import translate_to_chinese
import os

class TranslatePDFApp:
    def __init__(self, root):
        self.root = root
        self.root.title("English to Chinese PDF Translator")
        self.root.geometry("400x300")
        self.label = tk.Label(root, text="Drag or Upload PDF here", font=("Arial", 14))
        self.label.pack(pady=20)
        self.upload_btn = tk.Button(root, text="Upload PDF", command=self.upload_file)
        self.upload_btn.pack(pady=10)
        self.translate_btn = tk.Button(root, text="Translate", command=self.translate_pdf, state="disabled")
        self.translate_btn.pack(pady=10)
        self.file_path = None
        self.root.drop_target_register(DND_FILES)
        self.root.dnd_bind('<<Drop>>', self.drop_file)

    def upload_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if self.file_path:
            self.label.config(text=f"File: {os.path.basename(self.file_path)}")
            self.translate_btn.config(state="normal")

    def drop_file(self, event):
        self.file_path = event.data
        if self.file_path.endswith(".pdf"):
            self.label.config(text=f"File: {os.path.basename(self.file_path)}")
            self.translate_btn.config(state="normal")

    def translate_pdf(self):
        if not self.file_path:
            messagebox.showerror("Error", "No PDF selected!")
            return

        try:
            english_text = extract_text_from_pdf(self.file_path)
            if not english_text:
                messagebox.showerror("Error", "Failed to extract text from PDF")
                return
            chinese_text = translate_to_chinese(english_text)
            output_path = f"output/translated_{os.path.basename(self.file_path)}"
            os.makedirs("output", exist_ok=True)
            create_bilingual_pdf(english_text, chinese_text, output_path)
            messagebox.showinfo("Success", f"Bilingual PDF saved as {output_path}")
        except ValueError as ve:
            messagebox.showerror("Translation Error", str(ve))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to process PDF: {str(e)}")

if __name__ == "__main__":
    root = TkinterDnD.Tk()
    app = TranslatePDFApp(root)
    root.mainloop()
