from xml_template_classes import DocumentInvoice, LineItem, InvoiceLines, Line
from csv import reader
from datetime import datetime, date

with open('example.csv') as file:
    data = reader(file, delimiter=';')

    xml_document = DocumentInvoice()

    header = next(data)
    xml_document.invoice_parties.seller = header[0]
    xml_document.invoice_header.invoice_number = f"<![CDATA[{header[1]}]]>"
    xml_document.invoice_parties.buyer = header[2]
    xml_document.invoice_parties.payer = header[2]
    xml_document.invoice_parties.invoicee = header[2]
    xml_document.invoice_header.invoice_date = date.fromisoformat(header[3])
    xml_document.invoice_header.sales_date = date.fromisoformat(header[3])
    xml_document.invoice_header.invoice_payment_due_date = date.fromisoformat(header[4])

    for number, row in enumerate(data):
        xml_document.invoice_lines.append(InvoiceLines(Line(LineItem(
            supplier_item_code=row[0],
            manufacturer_item_code=row[1],
            item_description=row[2],
            invoice_quantity=row[3],
            invoice_unit_net_price=row[4],
            net_amount=row[5] - row[6],
            tax_amount=row[6],
            unit_of_measure=row[8],
            tax_rate=row[9],
            ean=row[10]
        ))))

    print(xml_document.invoice_lines)
