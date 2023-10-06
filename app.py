from weasyprint import HTML
from flask import Flask


html = HTML("invoice.html")
html.write_pdf("invoice.pdf")
