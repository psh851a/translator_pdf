import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            page_text = page.get_text("text")
            if page_text:
                text += page_text
        doc.close()
        if not text.strip():
            raise ValueError("PDF contains no extractable text")
        return text  # Return text as string
    except Exception as e:
        raise ValueError(f"PDF processing failed: {str(e)}")

def create_bilingual_pdf(english_text, chinese_text, output_path):
    doc = fitz.open()
    page = doc.new_page()
    
    # Set up page dimensions and margins
    page_width = page.rect.width
    margin = 50
    line_height = 14
    
    # Add English section
    eng_heade
import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            page_text = page.get_text("text")
            if page_text:
                text += page_text
        doc.close()
        if not text.strip():
            raise ValueError("PDF contains no extractable text")
        return text  # Return text as string
    except Exception as e:
        raise ValueError(f"PDF processing failed: {str(e)}")

def create_bilingual_pdf(english_text, chinese_text, output_path):
    doc = fitz.open()
    page = doc.new_page()
    
    # Page layout settings
    margin = 50
    line_height = 14
    para_spacing = 20
    current_y = margin
    page_width = page.rect.width - 2 * margin
    page_height = page.rect.height
    
    import warnings
    
    # Split texts into paragraphs
    english_paras = [p.strip() for p in english_text.split('\n\n') if p.strip()]
    chinese_paras = [p.strip() for p in chinese_text.split('\n\n') if p.strip()]
    
    # Handle paragraph count mismatch with warning
    para_count = min(len(english_paras), len(chinese_paras))
    if len(english_paras) != len(chinese_paras):
        warnings.warn(f"Paragraph count mismatch - English: {len(english_paras)}, Chinese: {len(chinese_paras)}. Processing first {para_count} pairs.")
    
    for eng_para, ch_para in zip(english_paras[:para_count], chinese_paras[:para_count]):
        # Check if we need a new page
        if current_y > page_height - 100:
            page = doc.new_page()
import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            page_text = page.get_text("text")
            if page_text:
                text += page_text
        doc.close()
        if not text.strip():
            raise ValueError("PDF contains no extractable text")
        return text  # Return text as string
    except Exception as e:
        raise ValueError(f"PDF processing failed: {str(e)}")

def create_bilingual_pdf(english_text, chinese_text, output_path):
    doc = fitz.open()
    page = doc.new_page()
    
    # Set up page dimensions and margins
    page_width = page.rect.width
    margin = 50
    line_height = 14
    
    # Add English section
    eng_heade
import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            page_text = page.get_text("text")
            if page_text:
                text += page_text
        doc.close()
        if not text.strip():
            raise ValueError("PDF contains no extractable text")
        return text  # Return text as string
    except Exception as e:
        raise ValueError(f"PDF processing failed: {str(e)}")

def create_bilingual_pdf(english_text, chinese_text, output_path):
    doc = fitz.open()
    page = doc.new_page()
    margin = 50
    line_height = 14
    para_spacing = 20
    current_y = margin
    page_width = page.rect.width - 2 * margin

    # Split texts into paragraphs
    english_paras = [p.strip() for p in english_text.split('\n\n') if p.strip()]
    chinese_paras = [p.strip() for p in chinese_text.split('\n\n') if p.strip()]
    
    if len(english_paras) != len(chinese_paras):
        raise ValueError("Mismatch in number of English/Chinese paragraphs")

    for idx, (eng_para, ch_para) in enumerate(zip(english_paras, chinese_paras)):
        # English paragraph
        eng_header = f"English Paragraph {idx+1}:"
        header_height = line_height * 2
        page.insert_text((margin, current_y), eng_header, 
                        fontname="helv", fontsize=12)
        
        eng_rect = fitz.Rect(margin, current_y + header_height, 
                           page_width, page.rect.height - margin)
        text_height = page.insert_textbox(eng_rect, eng_para, 
                                        fontname="helv", fontsize=10,
                                        align=fitz.TEXT_ALIGN_LEFT)
        current_y += header_height + text_height + para_spacing

        # Chinese paragraph
        ch_header = f"Chinese Paragraph {idx+1}:"
        page.insert_text((margin, current_y), ch_header, 
                        fontname="helv", fontsize=12)
        
        ch_rect = fitz.Rect(margin, current_y + header_height, 
                          page_width, page.rect.height - margin)
        text_height = page.insert_textbox(ch_rect, ch_para, 
                                        fontname="china-s", fontsize=10,
                                        align=fitz.TEXT_ALIGN_LEFT)
        current_y += header_height + text_height + para_spacing * 2

        # Add new page if needed
        if current_y > page.rect.height - 100:
            page = doc.new_page()
            current_y = margin

    doc.save(output_path)
    doc.close()
