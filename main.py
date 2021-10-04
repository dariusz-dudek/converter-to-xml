from dataclasses import dataclass
from datetime import datetime


@dataclass
class Order:
    buyer_order_number: str = None              # Numer zamówienia
    supplier_order_number: str = None           # Numer zamówienia według sprzedawcy
    buyer_order_date: datetime = None           # Data zamówienia


@dataclass
class Reference:
    invoice_reference_number: str = None        # Numer faktury korygowanej
    invoice_reference_date: datetime = None     # Data faktury korygowanej


@dataclass
class DeliveryTerms:
    # Kod warunków dostawy lub transportu (INCOTERMS):
    # „04E” – płatne przy odbiorze
    # „EXW” – ex works
    # „FOR” – przekazane przewoźnikowi w określonym miejscu
    # „CPT” – opłacone do miejsca dostawy
    delivery_terms_code: str = None
    # Sposób płatności kosztów transportu:
    # „DF” – określony przez kupującego i dostawcę
    # „PC” – opłacony z góry, obciążający klienta
    payment_method: str = None


@dataclass
class Delivery:
    delivery_location_number: int = None        # ILN lokalizacji dostawy (sklepu)
    tax_id: str = None                          # NIP lokalizacji dostawy (sklepu)
    delivery_date: datetime = None              # Data dostawy
    despatch_number: str = None                 # Numer dostawy
    despatch_date: datetime = None              # Data dokumentu dostawy
    despatch_advice_number: str = None          # Numer awiza wysyłki
    name: str = None                            # Nazwa Punktu Dostawy
    street_and_number: str = None               # Ulica i numer
    city_name: str = None                       # Miasto
    postal_code: str = None                     # Kod pocztowy
    country: str = None                         # Kraj (kodowane ISO 3166)
    delivery_terms: DeliveryTerms = DeliveryTerms()


@dataclass
class Returns:
    returns_notice_number: str = None           # Numer zawiadomienia o zwrotach
    returns_notice_date: str = None             # Data zawiadomienia o zwrotach


@dataclass
class InvoiceHeader:
    invoice_number: str = None                  # Numer faktury
    invoice_date: datetime = None               # Data faktury
    sales_date: datetime = None                 # Data dostawy towarów lub wykonania usługi
    invoice_duplicate_date: datetime = None     # Data duplikatu faktury
    invoice_currency: str = None                # Waluta faktury
    invoice_payment_due_date: datetime = None   # Data płatności
    invoice_payment_terms: int = None           # Termin płatności (w dniach)
    invoice_payment_means: str = None           # Sposób płatności: 10–gotówka 20–czek 42–przelew 97–kompensata
    payment_information: str = None             # Adnotacja o podzielonej płatności
    deferred_payment: str = None                # Tekstowy opis odroczonej płatności
    invoice_post_date: datetime = None          # Data wpłynięcia do systemu
    document_function_code: str = None          # Typ dokumentu: O–oryginał D–duplikat C–korekta R–duplikat korekty
    message_type: str = None                    # Typ dokumentu: INV–faktura SB–rachunek własny
    correction_reason: str = None               # Powód korekty
    remakes: str = None                         # Uwagi
    order: Order = Order()
    reference: Reference = Reference()
    delivery: Delivery = Delivery()
    returns: Returns = Returns()


@dataclass
class Buyer:
    iln: int = None                             # ILN Kupującego
    tax_id: str = None                          # NIP Kupującego
    account_number: str = None                  # Konto bankowe Kupującego
    name: str = None                            # Nazwa Kupującego
    street_and_number: str = None               # Ulica i numer
    city_name: str = None                       # Miasto
    postal_code: str = None                     # Kod pocztowy
    country: str = None                         # Kraj (kodowane ISO 3166)


@dataclass
class Payer:
    iln: int = None                             # ILN Płatnika
    tax_id: str = None                          # NIP Płatnika
    account_number: str = None                  # Konto bankowe Płatnika.
    name: str = None                            # Nazwa Płatnika
    street_and_number: str = None               # Ulica i numer
    city_name: str = None                       # Miasto
    postal_code: str = None                     # Kod pocztowy
    country: str = None                         # Kraj (kodowane ISO 3166)


@dataclass
class Invoicee:
    iln: int = None                             # ILN Odbiorcy Faktury
    tax_id: str = None                          # NIP Odbiorcy Faktury
    account_number: str = None                  # Konto bankowe Odbiorcy Faktury.
    name: str = None                            # Nazwa Odbiorcy Faktury
    street_and_number: str = None               # Ulica i numer
    city_name: str = None                       # Miasto
    postal_code: str = None                     # Kod pocztowy
    country: str = None                         # Kraj (kodowane ISO 3166)


@dataclass
class ContactInformation:
    contact_id: str = None                      # Id kontaktu
    contact_name: str = None                    # Nazwa kontaktu
    phone_number: str = None                    # Numer kontaktowy
    fax: str = None                             # Fax
    electronic_mail: str = None                 # Adres e-mail
    x400: str = None                            # X400


@dataclass
class AccountingContactInformation:
    contact_id: str = None                      # Id kontaktu
    contact_name: str = None                    # Nazwa kontaktu
    phone_number: str = None                    # Numer kontaktowy
    fax: str = None                             # Fax
    electronic_mail: str = None                 # Adres e-mail
    x400: str = None                            # X400


@dataclass
class SalesAdministration:
    contact_id: str = None                      # Id kontaktu
    contact_name: str = None                    # Nazwa kontaktu
    phone_number: str = None                    # Numer kontaktowy
    fax: str = None                             # Fax
    electronic_mail: str = None                 # Adres e-mail
    x400: str = None                            # X400


@dataclass
class SalesRepresentative:
    contact_id: str = None                      # Id kontaktu
    contact_name: str = None                    # Nazwa kontaktu
    phone_number: str = None                    # Numer kontaktowy
    fax: str = None                             # Fax
    electronic_mail: str = None                 # Adres e-mail
    x400: str = None                            # X400


@dataclass
class Seller:
    iln: int = None                             # ILN Sprzedawcy
    tax_id: str = None                          # NIP Sprzedawcy
    account_number: str = None                  # Konto bankowe Sprzedawcy
    financial_institution_name: str = None      # Nazwa instytucji finansowej
    code_by_buyer: str = None                   # Kod dostawcy wg Kupującego
    name: str = None                            # Nazwa Sprzedawcy
    street_and_number: str = None               # Ulica i numer
    city_name: str = None                       # Miasto
    postal_code: str = None                     # Kod pocztowy
    country: str = None                         # Kraj (kodowane ISO 3166)
    utilization_register_number: str = None     # Numer rejestrowy (utylizacyjny)
    court_and_capital_information: str = None   # Oznaczenie sądu rejestrowego i numeru rejestru
    certificate_number: str = None              # Numer certyfikatu
    contact_information: ContactInformation = ContactInformation()
    accounting_contact_information: AccountingContactInformation = AccountingContactInformation()
    sales_administration: SalesAdministration = SalesAdministration()
    sales_representative: SalesRepresentative = SalesRepresentative()


@dataclass
class Payee:
    iln: int = None                             # ILN Odbiorcy Płatności
    tax_id: str = None                          # NIP Odbiorcy Płatności
    account_number: str = None                  # Konto Odbiorcy Płatności
    name: str = None                            # Nazwa Odbiorcy Płatności
    street_and_number: str = None               # Ulica i numer
    city_name: str = None                       # Miasto
    postal_code: str = None                     # Kod pocztowy
    country: str = None                         # Kraj (kodowane ISO 3166)


@dataclass
class SellerHeadquarters:
    iln: int = None                             # ILN Siedziby Sprzedawcy
    name: str = None                            # Nazwa Siedziby Sprzedawcy
    street_and_number: str = None               # Ulica i numer
    city_name: str = None                       # Miasto
    postal_code: str = None                     # Kod pocztowy
    country: str = None                         # Kraj (kodowane ISO 3166)


@dataclass
class OrderedBy:
    iln: int = None                             # ILN Zamawiającego
    tax_id: str = None                          # NIP Zamawiającego
    account_number: str = None                  # Konto bankowe Zamawiającego
    name: str = None                            # Nazwa Zamawiającego
    street_and_number: str = None               # Ulica i numer
    city_name: str = None                       # Miasto
    postal_code: str = None                     # Kod pocztowy
    country: str = None                         # Kraj (kodowane ISO 3166)


@dataclass
class Sender:
    iln: int = None                             # GLN Wysyłającego
    tax_id: str = None                          # NIP Wysyłającego
    name: str = None                            # Nazwa Wysyłającego
    street_and_number: str = None               # Ulica i numer
    city_name: str = None                       # Miasto
    postal_code: str = None                     # Kod pocztowy
    country: str = None                         # Kraj (kodowane ISO 3166)


@dataclass
class Receiver:
    iln: int = None                             # GLN Odbierającego
    tax_id: str = None                          # NIP Odbierającego
    name: str = None                            # Nazwa Odbierającego
    street_and_number: str = None               # Ulica i numer
    city_name: str = None                       # Miasto
    postal_code: str = None                     # Kod pocztowy
    country: str = None                         # Kraj (kodowane ISO 3166)


@dataclass
class InvoiceParties:
    buyer: Buyer = Buyer()
    payer: Payer = Payer()
    invoicee: Invoicee = Invoicee()
    seller: Seller = Seller()
    payee: Payee = Payee()
    seller_headquarters: SellerHeadquarters = SellerHeadquarters()
    ordered_by: OrderedBy = OrderedBy()
    sender: Sender = Sender()
    receiver: Receiver = Receiver()


@dataclass
class TaxReference:
    reference_type: str = None
    reference_number: str = None


@dataclass
class LineItem:
    line_number: int = None                     # Numer linii
    order_line_number: int = None               # Numer linii z zamówienia
    ean: str = None                             # EAN produktu
    buyer_item_code: str = None                 # Kod produktu wg nabywcy
    supplier_item_code: str = None              # Kod produktu wg dostawcy
    manufacturer_item_code: str = None          # Kod produktu wg producenta
    serial_number: str = None                   # Numer serii
    customs_code: str = None                    # Kod celny towaru
    item_description: str = None                # Nazwa produktu
    item_type: str = None                       # Identyfikator opakowania zwrotnego:
    # "CU" – jednostka handlowa
    # "RC" – opakowanie zwrotne
    # "IN" – jednostka fakturowana
    country_of_origin: str = None               # Kraj pochodzenia
    grade: str = None                           # Klasa produktu
    variety: str = None                         # Odmiana
    payment_information: str = None             # Informacje o płatności: “Mechanizm podzielonej płatności”
    product_type: str = None                    # Typ produktu, dodatkowe informacje dotyczące
    # produktów z grupy warzywa i owoce. Zgodnie z rozporządzeniem Komisji EU nr 543/2011
    # należy w niektórych przypadkach przekazywać również informacje o np. klasie, typie
    # handlowym, odmianie itp
    product_size: str = None                    # Rozmiar produktu
    product_color: str = None                   # Kolor produktu
    special_conditions: str = None              # Specjalne warunki
    invoice_quantity: float = None              # Zafakturowana ilość
    unit_of_measure: str = None                 # Jednostka miary
    invoice_unit_packsize: float = None
    pack_item_unit_of_measure: str = None
    free_goods_quantity: float = None
    delivered_quantity: float = None
    invoice_unit_net_price: float = None
    invoice_unit_gross_price: float = None
    invoice_unit_retail_price: float = None
    invoice_unit_price_without_charges: float = None
    tax_rate: float = None
    tax_category_code: str = None
    tax_reference: TaxReference = TaxReference()
    tax_amount: float = None
    net_amount: float = None
    deposit_amount: float = None
    previous_invoice_quantity: float = None
    previous_delivered_quantity: float = None
    previous_invoice_unit_net_price: float = None
    previous_tax_rate: float = None
    previous_tax_category_code: str = None
    previous_tax_amount: float = None
    previous_net_amount: float = None
    previous_deposit_amount: float = None
    correction_invoice_quantity: float = None
    correction_delivered_quantity: float = None
    correction_invoice_unit_net_price: float = None
    correction_tax_amount: float = None
    correction_net_amount: float = None
    correction_gross_amount: float = None
    correction_deposit_amount: float = None
    expiration_date: datetime = None
    production_date: datetime = None
    best_before_date: datetime = None
    sales_date: datetime = None
    certificate_number: str = None
    correction_reason: str = None
    utilization_fee: str = None


@dataclass
class LineOrder:
    buyer_order_number: str = None
    supplier_order_number: str = None
    buyer_order_date: datetime = None


@dataclass
class LineReference:
    invoice_reference_number: str = None
    invoice_reference_date: datetime = None


@dataclass
class DeliveryTerms:
    delivery_terms_code: str = None
    payment_method: str = None


@dataclass
class LineDelivery:
    delivery_location_number: str = None
    tax_id: str = None
    delivery_date: datetime = None
    despatch_number: str = None
    despatch_date: datetime = None
    despatch_advice_number: str = None
    ship_from_location_number: str = None
    name: str = None
    street_and_number: str = None
    city_name: str = None
    postal_code: str = None
    country: str = None
    delivery_terms: DeliveryTerms = DeliveryTerms()


@dataclass
class LineReturns:
    returns_notice_number: str = None
    returns_notice_date: datetime = None


@dataclass
class Allowance:
    percentage: str = None
    allowance_amount: float = None
    original_amount: float = None


@dataclass
class LineAllowances:
    allowance: Allowance = Allowance()


@dataclass
class Charge:
    percentage: str = None
    charge_amount: float = None
    original_amount: float = None
    special_service: str = None
    special_service_description: str = None


@dataclass
class LineCharges:
    charge: Charge = Charge()


@dataclass
class LineMeasurements:
    net_weight: float = None


@dataclass
class Line:
    line_item: LineItem = LineItem()
    line_order: LineOrder = LineOrder()
    line_reference: LineReference = LineReference()
    line_delivery: LineDelivery = LineDelivery()
    line_returns: LineReturns = LineReturns()
    line_allowances: LineAllowances = LineAllowances()
    line_charges: LineCharges = LineCharges()
    line_measurements: LineMeasurements = LineMeasurements()


@dataclass
class InvoiceLines:
    line: Line = Line()


@dataclass
class TaxSummaryLine:
    tax_rate: float = None
    tax_category_code: str = None
    tax_amount: float = None
    taxable_basis: float = None
    taxable_amount: float = None
    gross_amount: float = None
    previous_tax_rate: float = None
    previous_tax_category_code: str = None
    previous_tax_amount: float = None
    previous_taxable_amount: float = None
    correction_tax_amount: float = None
    correction_taxable_amount: float = None
    correction_gross_amount: float = None


@dataclass
class TaxSummary:
    tax_summary_line: TaxSummaryLine = TaxSummaryLine()


@dataclass
class DepositSummary:
    total_net_amount: float = None
    total_gross_amount: float = None
    previous_total_net_amount: float = None
    previous_total_gross_amount: float = None
    correction_total_net_amount: float = None
    correction_total_gross_amount: float = None


@dataclass
class Charge:
    charge_number: str = None
    charge_amount: float = None
    special_service: str = None
    special_service_description: str = None


@dataclass
class ChargeSummary:
    charge: Charge = Charge()


@dataclass
class InvoiceSummary:
    total_lines: int = None
    total_net_amount: float = None
    total_taxable_basis: float = None
    total_tax_amount: float = None
    total_gross_amount: float = None
    total_deposit_amount: float = None
    total_discount_amount: float = None
    total_net_amout_without_charges: float = None
    previous_total_net_amount: float = None
    previous_total_taxable_basis: float = None
    previous_total_tax_amount: float = None
    previous_total_gross_amount: float = None
    previous_total_deposit_amount: float = None
    correction_total_net_amount: float = None
    correction_total_taxable_basis: float = None
    correction_total_tax_amount: float = None
    correction_total_gross_amount: float = None
    correction_total_deposit_amount: float = None
    gross_amount_in_words: str = None
    tax_summary: TaxSummary = TaxSummary()
    deposit_summary: DepositSummary = DepositSummary()
    charge_summary: ChargeSummary = ChargeSummary()


@dataclass
class DocumentInvoice:
    invoice_header: InvoiceHeader = InvoiceHeader()
    invoice_parties: InvoiceParties = InvoiceParties()
    invoice_lines: InvoiceLines = InvoiceLines()
    invoice_summary: InvoiceSummary = InvoiceSummary()
