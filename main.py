from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0) #for footers

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
#header
    pdf.set_font(family="Times", style="B", size=24) #header
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L")
    #use range steps
    for x in range(0,250,10):
        pdf.line(10, 21+x, 200, 21+x)

#footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0,h=10,txt=row["Topic"], align="R")



    for i in range(row["Pages"] - 1): #Add pages depending on topic size
        pdf.add_page()
        #footer
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

        for x in range(0, 250, 10):
            pdf.line(10, 21 + x, 200, 21 + x)

pdf.output("output.pdf")
