from fpdf import FPDF

def generate_report(data):

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial",size=12)

    for key,value in data.items():

        pdf.cell(200,10,f"{key}: {value}",ln=True)

    pdf.output("reports/security_report.pdf")