from containers.xml_template_classes_full_classes import Line, LineItem, TaxSummaryLine
from pyexcel import get_sheet
from datetime import timedelta
from db import Db

SELLER_NIP = '6780034235'
BUYER_NIP = '6280012377'


class MagKrak:
    def read(self, filename, xml_document):

        sheet = get_sheet(file_name=filename, encoding='utf-8')
        db = Db()

        xml_document.invoice_parties.seller.tax_id = SELLER_NIP
        xml_document.invoice_parties.seller.iln = db.get_iln(SELLER_NIP)
        xml_document.invoice_parties.payee.tax_id = SELLER_NIP
        xml_document.invoice_parties.payee.iln = db.get_iln(SELLER_NIP)
        xml_document.invoice_parties.seller_headquarters.tax_id = SELLER_NIP
        xml_document.invoice_parties.seller_headquarters.iln = db.get_iln(SELLER_NIP)
        xml_document.invoice_parties.buyer.tax_id = BUYER_NIP
        xml_document.invoice_parties.buyer.iln = db.get_iln(BUYER_NIP)
        xml_document.invoice_parties.payer.tax_id = BUYER_NIP
        xml_document.invoice_parties.payer.iln = db.get_iln(BUYER_NIP)
        xml_document.invoice_parties.invoicee.tax_id = BUYER_NIP
        xml_document.invoice_parties.invoicee.iln = db.get_iln(BUYER_NIP)
        xml_document.invoice_header.invoice_date = sheet['X2']
        xml_document.invoice_header.sales_date = sheet['X2']
        xml_document.invoice_header.invoice_payment_due_date = sheet['X2'] + timedelta(days=90)

        omitted = 0
        omitted_list = []

        for row_number, row in enumerate(sheet):
            if row_number == 0:
                continue
            if row[21] == ' ':
                omitted += 1
                omitted_list.append(row[0])
                continue
            xml_document.invoice_lines.append(Line(LineItem(
                    line_number=row[0],
                    supplier_item_code=MagKrak.encode(row[3]),
                    item_description=MagKrak.encode(row[1]),
                    item_type='CU',
                    invoice_quantity=float(row[4]),
                    invoice_unit_net_price=float(row[6]),
                    net_amount=float(row[12]),
                    tax_amount=float(row[14]),
                    unit_of_measure=row[5],
                    tax_rate=float(row[13]),
                    ean=row[21],
                    tax_category_code='S'
            )))

        xml_document.invoice_header.invoice_number = 'wpisa?? nr FA'
        if not omitted == 0:
            xml_document.invoice_header.invoice_number = f'Omini??to {omitted} wierszy FA: {omitted_list}'

    @staticmethod
    def encode(text: str) -> str:
        char_to_polish = {
            '??': '??',
            '??': '??',
            '??': '??',
            '000002': '??',
            '??': '??',
            '??': '??',
            '??': '??',
            '??': '??',
            '000005': '??',
            '000006': '??',
            '??': '??',
            '000007': '??',
            '??': '??',
            '??': '??',
            '??': '??',
            '000008': '??',
            '000009': '??',
            '0000010': '??',
            '??': 'fi'
        }

        text_converted = ''
        for char in text:
            if char in char_to_polish:
                text_converted += char_to_polish[char]
                continue
            text_converted += char
        return text_converted
