from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='p',unit='mm',format='A4')
pdf.set_auto_page_break(auto=False, margin= 0)
df= pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family='Times', style='B', size=12)
    pdf.set_text_color(250,0,0)
    pdf.cell(w=0, h=12, txt=row['Topic'], align="L", ln=1)

    for i in range(20,298,10):
        pdf.line(10,i,206,i)

    pdf.ln(264)
    pdf.set_font(family='Times', style='I', size=8)
    pdf.set_text_color(250, 0, 250)
    pdf.cell(w=0, h=10, txt=row['Topic'], align="R", ln=1)

    for i in range(row["Pages"] - 1):
        pdf.add_page()
        for i in range(20, 298, 10):
            pdf.line(10, i, 206, i)
        pdf.ln(276)
        pdf.set_font(family='Times', style='I', size=8)
        pdf.set_text_color(250, 0, 250)
        pdf.cell(w=0, h=10, txt=row['Topic'], align="R", ln=1)





pdf.output("output.pdf")
