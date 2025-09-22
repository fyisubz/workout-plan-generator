from fpdf import FPDF
import io

def export_to_pdf(plan_text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for line in plan_text.split('\n'):
        pdf.multi_cell(0,8,line)
    pdf_output = io.BytesIO()
    pdf.output(pdf_output)
    pdf_output.seek(0)
    return pdf_output

