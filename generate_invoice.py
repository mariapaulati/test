from fpdf import FPDF

def generate_invoice(data):
    # Initialize PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)

    # Header
    pdf.image("logo.png", x=10, y=8, w=50)  # Replace "logo.png" with your logo file
    pdf.set_xy(70, 10)
    pdf.cell(100, 10, 'Mozio Inc', ln=True)
    pdf.set_font('Arial', '', 12)
    pdf.set_xy(70, 18)
    pdf.cell(100, 10, 'Tehama Street 44, San Francisco, CA, 94105', ln=True)
    pdf.set_xy(70, 26)
    pdf.cell(100, 10, 'Phone: +1 415 992 8057', ln=True)
    pdf.set_xy(70, 34)
    pdf.cell(100, 10, 'Website: www.mozio.com', ln=True)

    # Invoice Title
    pdf.set_font('Arial', 'B', 16)
    pdf.set_xy(10, 50)
    pdf.cell(0, 10, 'INVOICE', ln=True, align='C')

    # Invoice Details
    pdf.set_xy(10, 60)
    pdf.set_font('Arial', '', 12)
    pdf.cell(100, 10, f"Invoice #: {data['invoice_number']}", ln=False)
    pdf.cell(0, 10, f"Date: {data['date']}", ln=True, align='R')

    # Bill To
    pdf.set_xy(10, 75)
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'BILL TO:', ln=True)
    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 10, data['passenger_name'], ln=True)
    pdf.cell(0, 10, data['company'], ln=True)
    pdf.cell(0, 10, data['address'], ln=True)

    # Ride Details
    pdf.set_xy(10, 110)
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Item', border=1, ln=False, align='L')
    pdf.cell(0, 10, 'Amount', border=1, ln=True, align='R')
    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 10, f"Booking ID: {data['booking_id']}", border=1, ln=False, align='L')
    pdf.cell(0, 10, data['amount'], border=1, ln=True, align='R')
    pdf.cell(0, 10, f"From: {data['from_location']}", border=1, ln=False)
    pdf.cell(0, 10, f"", border=1, ln=True)
    pdf.cell(0, 10, f"To: {data['to_location']}", border=1, ln=False)
    pdf.cell(0, 10, f"", border=1, ln=True)

    # Output
    pdf.output('invoice.pdf')
    print("Invoice saved as 'invoice.pdf'.")

# Input Data
ride_details = {
    "invoice_number": "1430-6174",
    "date": "1/28/2025",
    "passenger_name": "Sierra Huerta",
    "company": "Cruise Planners TA",
    "address": "Dionysos Sea Side Resort, Mylopotas, Greece",
    "booking_id": "2167487",
    "pickup": "May 15, 2025 9:49 AM",
    "from_location": "Dionysos Sea Side Resort, Mylopotas, Greece",
    "to_location": "Olia Hotel Mykonos, Mykonos, Greece",
    "vehicle": "Private Van",
    "service_type": "Point To Point",
    "amount": "117.95 EUR"
}

# Generate Invoice
generate_invoice(ride_details)
