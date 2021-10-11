import xml.etree.ElementTree as ET
from main_csv import read, xml_document
from datetime import date

read()

document_invoice = ET.Element('Document-Invoice')

invoice_header = ET.SubElement(document_invoice, 'Invoice-Header')
invoice_number = ET.SubElement(invoice_header, 'InvoiceNumber').text = xml_document.invoice_header.invoice_number
invoice_date = ET.SubElement(invoice_header, 'InvoiceDate').text = xml_document.invoice_header.invoice_date.isoformat()
sales_date = ET.SubElement(invoice_header, 'SalesDate').text = xml_document.invoice_header.sales_date.isoformat()
invoice_currency = ET.SubElement(invoice_header, 'InvoiceCurrency').text = 'PLN'
invoice_payment_due_date = ET.SubElement(
    invoice_header,
    'InvoicePaymentDueDate'
).text = xml_document.invoice_header.invoice_payment_due_date.isoformat()
invoice_payment_terms = ET.SubElement(invoice_header, 'InvoicePaymentTerms').text = \
    str((xml_document.invoice_header.invoice_payment_due_date - xml_document.invoice_header.sales_date).days)
document_function_code = ET.SubElement(invoice_header, 'DocumentFunctionCode').text = 'O'
order = ET.SubElement(invoice_header, 'Order')
buyer_order_number = ET.SubElement(order, 'BuyerOrderNumber')
buyer_order_date = ET.SubElement(order, 'BuyerOrderDate')
delivery = ET.SubElement(invoice_header, 'Delivery')
delivery_location_number = ET.SubElement(delivery, 'DeliveryLocationNumber')
delivery_date = ET.SubElement(delivery, 'DeliveryDate')
despatch_number = ET.SubElement(delivery, 'DespatchNumber')
despatch_advice_number = ET.SubElement(delivery, 'DespatchAdviceNumber')

invoice_parties = ET.SubElement(document_invoice, 'Invoice-Parties')

buyer = ET.SubElement(invoice_parties, 'Buyer')

iln_buyer = ET.SubElement(buyer, 'ILN')
tax_id_buyer = ET.SubElement(buyer, 'TaxID').text = xml_document.invoice_parties.buyer.tax_id
account_number_buyer = ET.SubElement(buyer, 'AccountNumber')
name_buyer = ET.SubElement(buyer, 'Name')
street_and_number_buyer = ET.SubElement(buyer, 'StreetAndNumber')
city_name_buyer = ET.SubElement(buyer, 'CityName')
postal_code_buyer = ET.SubElement(buyer, 'PostalCode')
country_buyer = ET.SubElement(buyer, 'Country')

payer = ET.SubElement(invoice_parties, 'Payer')

iln_payer = ET.SubElement(payer, 'ILN')
tax_id_payer = ET.SubElement(payer, 'TaxID').text = xml_document.invoice_parties.buyer.tax_id
account_number_payer = ET.SubElement(payer, 'AccountNumber')
name_payer = ET.SubElement(payer, 'Name')
street_and_number_payer = ET.SubElement(payer, 'StreetAndNumber')
city_name_payer = ET.SubElement(payer, 'CityName')
postal_code_payer = ET.SubElement(payer, 'PostalCode')
country_payer = ET.SubElement(payer, 'Country')

invoicee = ET.SubElement(invoice_parties, 'Invoicee')

iln_invoicee = ET.SubElement(invoicee, 'ILN')
tax_id_invoicee = ET.SubElement(invoicee, 'TaxID').text = xml_document.invoice_parties.buyer.tax_id
account_number_invoicee = ET.SubElement(invoicee, 'AccountNumber')
name_invoicee = ET.SubElement(invoicee, 'Name')
street_and_number_invoicee = ET.SubElement(invoicee, 'StreetAndNumber')
city_name_invoicee = ET.SubElement(invoicee, 'CityName')
postal_code_invoicee = ET.SubElement(invoicee, 'PostalCode')
country_invoicee = ET.SubElement(invoicee, 'Country')

seller = ET.SubElement(invoice_parties, 'Seller')

iln_seller = ET.SubElement(seller, 'ILN')
tax_id_seller = ET.SubElement(seller, 'TaxID').text = xml_document.invoice_parties.seller.tax_id
account_number_seller = ET.SubElement(seller, 'AccountNumber')
code_by_buyer_seller = ET.SubElement(seller, 'CodeByBuyer')
name_seller = ET.SubElement(seller, 'Name')
street_and_number_seller = ET.SubElement(seller, 'StreetAndNumber')
city_name_seller = ET.SubElement(seller, 'CityName')
postal_code_seller = ET.SubElement(seller, 'PostalCode')
country_seller = ET.SubElement(seller, 'Country')
utilization_register_number_seller = ET.SubElement(seller, 'UtilizationRegisterNumber')
court_and_capital_information_seller = ET.SubElement(seller, 'CourtAndCapitalInformation')

payee = ET.SubElement(invoice_parties, 'Payee')

iln_payee = ET.SubElement(payee, 'ILN')
tax_id_payee = ET.SubElement(payee, 'TaxID').text = xml_document.invoice_parties.seller.tax_id
account_number_payee = ET.SubElement(payee, 'AccountNumber')
name_payee = ET.SubElement(payee, 'Name')
street_and_number_payee = ET.SubElement(payee, 'StreetAndNumber')
city_name_payee= ET.SubElement(payee, 'CityName')
postal_code_payee = ET.SubElement(payee, 'PostalCode')
country_payee = ET.SubElement(payee, 'Country')

seller_headquarters = ET.SubElement(invoice_parties, 'SellerHeadquarters')

iln_seller_headquarters = ET.SubElement(seller_headquarters, 'ILN')
tax_id_seller_headquarters = ET.SubElement(seller_headquarters, 'TaxID').text = \
    xml_document.invoice_parties.seller.tax_id
account_number_seller_headquarters = ET.SubElement(seller_headquarters, 'AccountNumber')
name_seller_headquarters = ET.SubElement(seller_headquarters, 'Name')
street_and_number_seller_headquarters = ET.SubElement(seller_headquarters, 'StreetAndNumber')
city_name_seller_headquarters = ET.SubElement(seller_headquarters, 'CityName')
postal_code_seller_headquarters = ET.SubElement(seller_headquarters, 'PostalCode')
country_seller_headquarters = ET.SubElement(seller_headquarters, 'Country')

invoice_lines = ET.SubElement(document_invoice, 'Invoice-Lines')


for line_of_invoice in xml_document.invoice_lines:

    line = ET.SubElement(invoice_lines, 'Line')

    line_item = ET.SubElement(line, 'Line-Item')

    line_number = ET.SubElement(line_item, 'LineNumber').text = \
        str(line_of_invoice.line_item.line_number)
    buyer_item_code = ET.SubElement(line_item, 'BuyerItemCode')

    supplier_item_code = ET.SubElement(line_item, 'SupplierItemCode').text = \
        str(line_of_invoice.line_item.supplier_item_code)

    item_description = ET.SubElement(line_item, 'ItemDescription').text = \
        str(line_of_invoice.line_item.item_description)

    item_type = ET.SubElement(line_item, 'ItemType').text = \
        str(line_of_invoice.line_item.item_type)

    invoice_quantity = ET.SubElement(line_item, 'InvoiceQuantity').text = \
        str(line_of_invoice.line_item.invoice_quantity)

    unit_of_measure = ET.SubElement(line_item, 'UnitOfMeasure').text = \
        str(line_of_invoice.line_item.unit_of_measure)

    invoice_unit_packsize = ET.SubElement(line_item, 'InvoiceUnitPacksize')

    pack_item_unit_of_measure = ET.SubElement(line_item, 'PackItemUnitOfMeasure')

    invoice_unit_net_price = ET.SubElement(line_item, 'InvoiceUnitNetPrice').text = \
        str(line_of_invoice.line_item.invoice_unit_net_price)

    tax_rate = ET.SubElement(line_item, 'TaxRate').text = \
        str(line_of_invoice.line_item.tax_rate)

    tax_category_code = ET.SubElement(line_item, 'TaxCategoryCode')
        # .text = 'S'

    tax_reference = ET.SubElement(line_item, 'TaxReference')

    reference_type = ET.SubElement(tax_reference, 'ReferenceType')

    reference_number = ET.SubElement(tax_reference, 'ReferenceNumber')

    tax_amount = ET.SubElement(line_item, 'TaxAmount').text = \
        str(line_of_invoice.line_item.tax_amount)

    net_amount = ET.SubElement(line_item, 'NetAmount').text = \
        str(line_of_invoice.line_item.net_amount)

    line_order = ET.SubElement(line, 'Line-Order')

    buyer_order_number = ET.SubElement(line_order, 'BuyerOrderNumber')

    buyer_order_date = ET.SubElement(line_order, 'BuyerOrderDate')

    line_delivery = ET.SubElement(line, 'Line-Delivery')

    delivery_location_number = ET.SubElement(line_delivery, 'DeliveryLocationNumber')

    delivery_date = ET.SubElement(line_delivery, 'DeliveryDate')

    despatch_number = ET.SubElement(line_delivery, 'DespatchNumber')

    despatch_advice_number = ET.SubElement(line_delivery, 'DespatchAdviceNumber')


invoice_summary = ET.SubElement(document_invoice, 'Invoice-Summary')

total_lines = ET.SubElement(invoice_summary, 'TotalLines').text = \
    str(len(xml_document.invoice_lines))

total_net_amount = ET.SubElement(invoice_summary, 'TotalNetAmount').text = \
    str(xml_document.invoice_summary.total_net_amount)

total_taxable_basis = ET.SubElement(invoice_summary, 'TotalTaxableBasis').text = \
    str(xml_document.invoice_summary.total_taxable_basis)

total_tax_amount = ET.SubElement(invoice_summary, 'TotalTaxAmount').text = \
    str(xml_document.invoice_summary.total_tax_amount)

total_gross_amount = ET.SubElement(invoice_summary, 'TotalGrossAmount').text = \
    str(xml_document.invoice_summary.total_gross_amount)

gross_amount_in_words = ET.SubElement(invoice_summary, 'GrossAmountInWords').text = \
    str(xml_document.invoice_summary.gross_amount_in_words)

tax_summary = ET.SubElement(invoice_summary, 'Tax-Summary')


for tax_sumary_row in xml_document.invoice_summary.tax_summary.tax_summary_line:
    tax_summary_line = ET.SubElement(tax_summary, 'Tax-Summary-Line')
    tax_rate_s = ET.SubElement(tax_summary_line, 'TaxRate').text = str(tax_sumary_row.tax_rate)
    tax_category_code_s = ET.SubElement(tax_summary_line, 'TaxCategoryCode').text = str(tax_sumary_row.tax_category_code)
    tax_amount_s = ET.SubElement(tax_summary_line, 'TaxAmount').text = str(tax_sumary_row.tax_amount)
    taxable_basis_s = ET.SubElement(tax_summary_line, 'TaxableBasis').text = str(tax_sumary_row.taxable_basis)
    taxable_amount_s = ET.SubElement(tax_summary_line, 'TaxableAmount').text = str(tax_sumary_row.taxable_amount)
    gross_amount_s = ET.SubElement(tax_summary_line, 'GrossAmount').text = str(tax_sumary_row.gross_amount)

tree = ET.ElementTree(document_invoice)

tree.write('sample.xml', encoding='UTF-8', short_empty_elements=False)
