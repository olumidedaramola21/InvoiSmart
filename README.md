# InvoiSmart

A Flask-based automatic invoice generator leveraging WeasyPrint, featuring a customizable invoice template. This system dynamically generates invoices using Jinja, simplifying the process of crafting polished and professional invoices.

## Requirements:

Make sure you have the following dependencies installed:

- [Python](https://www.python.org/) (3.11.4)
- [Flask](https://palletsprojects.com/p/flask/) (3.0.0)
- [WeasyPrint](https://weasyprint.readthedocs.io/) (60.1)

## Usage

### Running the Application

To run the application, execute the following command in the terminal:


`python yourapp.py`

Please note that running the application on Chrome directly may not be effective. Clients are required to send data in the form of JSON using the header:

`if request.headers.get("Content-Type") == "application/json":`

This ensures that the server processes the incoming data correctly.

### Using Postman to send POST request

1. **Open Postman.**
2. Set the request type to `POST`.
3. Enter the URL: `http://localhost:5000/` (or the appropriate URL for your Flask application).
4. In the Headers section, add a new header:
   - Key: `Content-Type`
   - Value: `application/json`
5. In the Body section:
   - Select the "raw" option.
   - Choose `JSON (application/json)` as the type.
   - Enter your JSON data in the request body. For example:
     ```json
     {
       "duedate": "November 7, 2023",
       "other_key": "other_value",
       "another_key": "another_value",
       ...
     }
     ```
6. Click the "Send" button to make the POST request.

Ensure that your Flask application is running and listening on `http://localhost:5000/`. The data structure in the JSON body should match what Flask application expects.
