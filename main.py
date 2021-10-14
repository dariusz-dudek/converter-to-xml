from raw_pol import read_from_csv
from draw import draw_xml
from containers.xml_template_classes_full_classes import DocumentInvoice
from add_contractor import add_contractor_all

if __name__ == '__main__':
    xml_document = DocumentInvoice()
    read_from_csv('FS15732712025441021E.csv', xml_document)
    add_contractor_all(xml_document)
    draw_xml('sample.xml', xml_document)
    print(xml_document.invoice_parties.invoicee.tax_id)
