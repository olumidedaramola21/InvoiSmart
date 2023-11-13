from weasyprint import HTML
from flask import Flask, render_template, request, send_file
import os
from datetime import datetime


app = Flask(__name__)


@app.route("/")
def create_pdf():
    if request.headers.get("Content-Type") == "application/json":
        posted_data = request.get_json() or {}
        today = datetime.today().strftime("%B %#d, %Y")
        default_data = {
            "duedate": "November 7, 2023",
            "from_addr": {
                "company_name": "Python Tip.",
                "addr1": "12345 Sunny Road",
                "addr2": "Sunnyville, CA 12345",
            },
            "invoice_number": 123,
            "items": [
                {"title": "website design", "charge": 300.00},
                {"title": "Hosting (3 months)", "charge": 75.00},
                {"title": "Domain name (1 year)", "charge": 10.00},
            ],
            "to_addr": {
                "company_name": "Acme Corp.",
                "person_name": "John Dilly",
                "person_email": "john@example.com",
            },
        }
        duedate = posted_data.get("duedate", default_data["duedate"])
        from_addr = posted_data.get("from_addr", default_data["from_addr"])
        to_addr = posted_data.get("to_addr", default_data["to_addr"])
        items = posted_data.get("items", default_data["items"])
        invoice_number = posted_data.get(
            "invoice_number", default_data["invoice_number"]
        )

        total = sum([i["charge"] for i in items])
        rendered = render_template(
            "invoice.html",
            date=today,
            from_addr=from_addr,
            to_addr=to_addr,
            items=items,
            total=total,
            invoice_number=invoice_number,
            duedate=duedate,
        )
        HTML(string=rendered).write_pdf("./static/invoice.pdf")
        # Process the data as required

    else:
        return (
            "Invalid Content-Type. Please use application/json",
            400,
        )  # HTTP 400 Bad Request


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
