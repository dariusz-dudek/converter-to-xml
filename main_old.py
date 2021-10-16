from converters.raw_pol import read_from_csv
from draw import draw_xml
from containers.xml_template_classes_full_classes import DocumentInvoice
from contractors.add_contractor import add_contractor_all

if __name__ == '__main__':
    xml_document = DocumentInvoice()
    read_from_csv('examples/FS15732712025441021E.csv', xml_document)
    add_contractor_all(xml_document)
    draw_xml('examples/sample.xml', xml_document)
    print(xml_document.invoice_parties.invoicee.tax_id)
