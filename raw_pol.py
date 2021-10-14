from containers.xml_template_classes_full_classes import LineItem, Line, TaxSummaryLine
from csv import reader
from datetime import date, timedelta
from db import Db


def read_from_csv(filename, xml_document):
    with open(filename, encoding='Windows-1250') as file:
        db = Db()
        data = reader(file, delimiter=';')

        header = next(data)

        xml_document.invoice_parties.seller.tax_id = '8351001704'
        xml_document.invoice_parties.seller.iln = db.get_iln('8351001704')
        xml_document.invoice_parties.payee.tax_id = '8351001704'
        xml_document.invoice_parties.payee.iln = db.get_iln('8351001704')
        xml_document.invoice_parties.seller_headquarters.tax_id = '8351001704'
        xml_document.invoice_parties.seller_headquarters.iln = db.get_iln('8351001704')
        xml_document.invoice_header.invoice_number = f'FS{header[0]}12025441021E'
        xml_document.invoice_parties.buyer.tax_id = '6280012377'
        xml_document.invoice_parties.buyer.iln = db.get_iln('6280012377')
        xml_document.invoice_parties.payer.tax_id = '6280012377'
        xml_document.invoice_parties.payer.iln = db.get_iln('6280012377')
        xml_document.invoice_parties.invoicee.tax_id = '6280012377'
        xml_document.invoice_parties.invoicee.iln = db.get_iln('6280012377')
        xml_document.invoice_header.invoice_date = date.fromisoformat(header[1][:10])
        xml_document.invoice_header.sales_date = date.fromisoformat(header[1][:10])
        xml_document.invoice_header.invoice_payment_due_date = date.fromisoformat(header[1][:10]) + timedelta(days=10)

        for number, row in enumerate(data):
            xml_document.invoice_lines.append(Line(LineItem(
                    line_number=number + 1,
                    supplier_item_code=row[0],
                    item_description=row[0],
                    item_type='CU',
                    invoice_quantity=float(row[3].replace(',', '.')),
                    invoice_unit_net_price=float(row[4].replace(',', '.')),
                    net_amount=round(float(row[3].replace(',', '.')) * float(row[4].replace(',', '.')), 2),
                    tax_amount=round(float(row[3].replace(',', '.')) * float(row[4].replace(',', '.')) * float(row[6])/100, 2),
                    unit_of_measure=row[2],
                    tax_rate=float(row[6]),
                    ean=row[7],
                    tax_category_code='S'
            )))

        for row in xml_document.invoice_lines:
            if row.line_item.tax_rate not in \
                    [float(vat.tax_rate) for vat in xml_document.invoice_summary.tax_summary.tax_summary_line]:
                xml_document.invoice_summary.tax_summary.tax_summary_line.\
                    append(TaxSummaryLine(tax_rate=float(row.line_item.tax_rate), tax_category_code='S'))

            for vat_summary in xml_document.invoice_summary.tax_summary.tax_summary_line:
                if vat_summary.tax_rate == row.line_item.tax_rate:
                    vat_summary.taxable_basis += row.line_item.net_amount

        for tax_sumary_line in xml_document.invoice_summary.tax_summary.tax_summary_line:
            tax_sumary_line.taxable_amount = tax_sumary_line.taxable_basis
            tax_sumary_line.tax_amount = round(tax_sumary_line.taxable_basis * (tax_sumary_line.tax_rate / 100), 2)
            tax_sumary_line.gross_amount = round(tax_sumary_line.tax_amount + tax_sumary_line.taxable_basis, 2)
            xml_document.invoice_summary.total_taxable_basis += tax_sumary_line.taxable_basis
            xml_document.invoice_summary.total_net_amount += tax_sumary_line.taxable_amount
            xml_document.invoice_summary.total_tax_amount += tax_sumary_line.tax_amount

        xml_document.invoice_summary.total_gross_amount = \
            float(xml_document.invoice_summary.total_taxable_basis)\
            + float(xml_document.invoice_summary.total_tax_amount)
