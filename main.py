import pdfplumber
import pandas as pd

cropped_pages = []

with pdfplumber.open("26_DTOC2.pdf") as pdf:
    for page in pdf.pages:
        if page == pdf.pages[0]:
            cropped_page = page.crop((42, 227, 442, 792))
        else:
            cropped_page = page.crop((42, 0, 442, 792))
        cropped_pages.append(cropped_page)


cropped_pages[0].to_image().show()