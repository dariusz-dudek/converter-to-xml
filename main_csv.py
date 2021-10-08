from xml_template_classes_short_wdc import DocumentInvoice, LineItem, InvoiceLines, Line, TaxSummaryLine
from csv import reader
from datetime import date

with open('example.csv') as file:
    data = reader(file, delimiter=';')

    xml_document = DocumentInvoice()

    header = next(data)
    xml_document.invoice_parties.seller.tax_id = header[0]
    xml_document.invoice_header.invoice_number = f"<![CDATA[{header[1]}]]>"
    xml_document.invoice_parties.buyer.tax_id = header[2]
    xml_document.invoice_parties.payer.tax_id = header[2]
    xml_document.invoice_parties.invoicee = header[2]
    xml_document.invoice_header.invoice_date = date.fromisoformat(header[3])
    xml_document.invoice_header.sales_date = date.fromisoformat(header[3])
    xml_document.invoice_header.invoice_payment_due_date = date.fromisoformat(header[4])

    vat = []

    for number, row in enumerate(data):
        xml_document.add(InvoiceLines(Line(LineItem(
            line_number=number + 1,
            supplier_item_code=row[0],
            manufacturer_item_code=row[1],
            item_description=f'<![CDATA[{row[2]}]]',
            item_type='CU',
            invoice_quantity=row[3],
            invoice_unit_net_price=row[4],
            net_amount=round(float(row[5]) - float(row[6]), 2),
            tax_amount=row[6],
            unit_of_measure=row[8],
            tax_rate=row[9],
            ean=row[10],
            tax_category_code='S'
        ))))

        if f'vat{str(row[9]).split(".")[0]}' not in vat:
            globals()[f'vat{str(row[9]).split(".")[0]}'] = TaxSummaryLine(
                tax_rate=row[9],
                tax_category_code='S',
                taxable_basis=0,
                taxable_amount=0,
                tax_amount=0
            )
            xml_document.invoice_summary.add_tax(globals()[f'vat{str(row[9]).split(".")[0]}'])
            vat.append(f'vat{str(row[9]).split(".")[0]}')

        # xml_document.invoice_summary.total_lines += 1
        # xml_document.invoice_summary.total_net_amount += round(float(row[5]) - float(row[6]), 2)
        # xml_document.invoice_summary.total_taxable_basis += round(float(row[5]) - float(row[6]), 2)

        globals()[f'vat{str(row[9]).split(".")[0]}'].kwargs['taxable_basis'] += round(float(row[5]) - float(row[6]), 2)
        globals()[f'vat{str(row[9]).split(".")[0]}'].kwargs['taxable_amount'] += round(float(row[5]) - float(row[6]), 2)
        globals()[f'vat{str(row[9]).split(".")[0]}'].kwargs['tax_amount'] += float(row[6])

    # for row in xml_document.invoice_summary.tax_summary.tax_summary_line:
    #     print(row)

    for line in xml_document.invoice_lines:
        print(line)
    # print(xml_document.invoice_lines)
