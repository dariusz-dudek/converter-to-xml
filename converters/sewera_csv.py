from containers.xml_template_classes_full_classes import LineItem, Line, TaxSummaryLine
from csv import reader
from datetime import date
from db import Db


class Sewera:
    def read(self, filename, xml_document):
        with open(filename) as file:
            db = Db()
            data = reader(file, delimiter=';')

            header = next(data)

            xml_document.invoice_parties.seller.tax_id = header[0][-10:]
            xml_document.invoice_parties.seller.iln = db.get_iln(header[0][-10:])
            xml_document.invoice_parties.payee.tax_id = header[0][-10:]
            xml_document.invoice_parties.payee.iln = db.get_iln(header[0][-10:])
            xml_document.invoice_parties.seller_headquarters.tax_id = header[0][-10:]
            xml_document.invoice_parties.seller_headquarters.iln = db.get_iln(header[0][-10:])
            xml_document.invoice_header.invoice_number = header[1]
            xml_document.invoice_parties.buyer.tax_id = header[2]
            xml_document.invoice_parties.buyer.iln = db.get_iln(header[2])
            xml_document.invoice_parties.payer.tax_id = header[2]
            xml_document.invoice_parties.payer.iln = db.get_iln(header[2])
            xml_document.invoice_parties.invoicee.tax_id = header[2]
            xml_document.invoice_parties.invoicee.iln = db.get_iln(header[2])
            xml_document.invoice_header.invoice_date = date.fromisoformat(header[3])
            xml_document.invoice_header.sales_date = date.fromisoformat(header[3])
            xml_document.invoice_header.invoice_payment_due_date = date.fromisoformat(header[4])

            for number, row in enumerate(data):
                xml_document.invoice_lines.append(Line(LineItem(
                        line_number=number + 1,
                        supplier_item_code=row[0],
                        manufacturer_item_code=row[1],
                        item_description=row[2],
                        item_type='CU',
                        invoice_quantity=float(row[3]),
                        invoice_unit_net_price=float(row[4]),
                        net_amount=round(float(row[5]) - float(row[6]), 2),
                        tax_amount=float(row[6]),
                        unit_of_measure=row[8],
                        tax_rate=float(row[9]),
                        ean=row[10],
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
