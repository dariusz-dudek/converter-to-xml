from dataclasses import dataclass, field
import xml.etree.ElementTree as ET
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
    reference_type: str = None                  # Kod typu referencji: „SWW” lub „PKWiU”
    reference_number: str = None                # Kod SWW lub PKWiU


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
    # Identyfikator opakowania zwrotnego:
    # "CU" – jednostka handlowa
    # "RC" – opakowanie zwrotne
    # "IN" – jednostka fakturowana
    item_type: str = None
    country_of_origin: str = None               # Kraj pochodzenia
    grade: str = None                           # Klasa produktu
    variety: str = None                         # Odmiana
    payment_information: str = None             # Informacje o płatności: “Mechanizm podzielonej płatności”
    # Typ produktu, dodatkowe informacje dotyczące
    # produktów z grupy warzywa i owoce. Zgodnie z rozporządzeniem Komisji EU nr 543/2011
    # należy w niektórych przypadkach przekazywać również informacje o np. klasie, typie
    # handlowym, odmianie itp
    product_type: str = None
    product_size: str = None                    # Rozmiar produktu
    product_color: str = None                   # Kolor produktu
    special_conditions: str = None              # Specjalne warunki
    invoice_quantity: float = None              # Zafakturowana ilość
    unit_of_measure: str = None                 # Jednostka miary
    invoice_unit_packsize: float = None         # Liczba sztuk detalicznych w jednostce zbiorczej
    pack_item_unit_of_measure: str = None       # Jednostka miary sztuki detalicznej w jednostce zbiorczej
    free_goods_quantity: float = None           # Ilość towaru darmowego
    delivered_quantity: float = None            # Dostarczona ilość
    invoice_unit_net_price: float = None        # Cena netto
    invoice_unit_gross_price: float = None      # Cena brutto
    invoice_unit_retail_price: float = None     # Cena detaliczna
    invoice_unit_price_without_charges: float = None    # Cena informacyjna przed uwzględnieniem opłaty cukrowej
    tax_rate: float = None                      # Stawka VAT
    # Kod stawki:
    # "E" (exempt) - zwolniony
    # "S" (standard) - inna, wyrażona liczba ("standardowa")
    # "NA" (not applicable) – nie podlega "AE" (reverse charge)- odwrotne obciążenie
    tax_category_code: str = None
    tax_reference: TaxReference = TaxReference()
    tax_amount: float = None                    # Wartość VAT pozycji
    net_amount: float = None                    # Wartość netto pozycji
    deposit_amount: float = None                # Kwota kaucji za towary kaucjonowane
    previous_invoice_quantity: float = None     # Zafakturowana ilość przed korektą
    previous_delivered_quantity: float = None   # Dostarczona ilość przed korektą
    previous_invoice_unit_net_price: float = None   # Cena netto przed korektą
    previous_tax_rate: float = None             # Stawka VAT przed korektą
    # Kod stawki:
    # "E" (exempt) - zwolniony
    # "S" (standard) - inna, wyrażona liczba ("standardowa")
    # "NA" (not applicable) – nie podlega "AE" (reverse charge)- odwrotne obciążenie
    previous_tax_category_code: str = None
    previous_tax_amount: float = None           # Wartość VAT pozycji przed korektą
    previous_net_amount: float = None           # Wartość netto pozycji przed korektą
    previous_deposit_amount: float = None       # Kwota kaucji za towary kaucjonowane przed korektą
    correction_invoice_quantity: float = None   # Zafakturowana ilość.Różnica pomiędzy wartością prawidłową a korygowaną
    correction_delivered_quantity: float = None  # Dostarczona ilość. Różnica pomiędzy wartością prawidłową a korygowaną
    correction_invoice_unit_net_price: float = None  # Cena netto. Różnica pomiędzy wartością prawidłową, a korygowaną
    correction_tax_amount: float = None         # Wartość VAT pozycji.Różnica pomiędzy wartością prawidłową a korygowaną
    correction_net_amount: float = None         # Wartość netto - różnica pomiędzy wartością prawidłową, a korygowaną
    correction_gross_amount: float = None       # Wartość brutto - różnica pomiędzy wartością prawidłową, a korygowaną
    # Kwota kaucji za towary kaucjonowane – różnica pomiędzy wartością prawidłową, a korygowaną
    correction_deposit_amount: float = None
    expiration_date: datetime = None            # Data ważności
    production_date: datetime = None            # Data produkcji
    best_before_date: datetime = None           # Data przydatności do spożycia
    sales_date: datetime = None                 # Data dostawy towarów lub wykonania usługi
    certificate_number: str = None              # Numer certyfikatu
    correction_reason: str = None               # Powód korekty
    utilization_fee: str = None                 # Kwota kosztu gospodarowania odpadami (opłata utylizacyjna)


@dataclass
class LineOrder:
    buyer_order_number: str = None              # Numer zamówienia
    supplier_order_number: str = None           # Numer zamówienia według sprzedawcy
    buyer_order_date: datetime = None           # Data zamówienia


@dataclass
class LineReference:
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
class LineDelivery:
    delivery_location_number: str = None        # ILN lokalizacji dostawy (sklepu)
    tax_id: str = None                          # NIP lokalizacji dostawy (sklepu)
    delivery_date: datetime = None              # Data dostawy
    despatch_number: str = None                 # Numer dostawy
    despatch_date: datetime = None              # Data dokumentu dostawy
    despatch_advice_number: str = None          # Numer awiza wysyłki
    ship_from_location_number: str = None       # ILN Punktu wysyłki
    name: str = None                            # Nazwa Punktu Dostawy
    street_and_number: str = None               # Ulica i numer
    city_name: str = None                       # Miasto
    postal_code: str = None                     # Kod pocztowy
    country: str = None                         # Kraj (kodowane ISO 3166)
    delivery_terms: DeliveryTerms = DeliveryTerms()


@dataclass
class LineReturns:
    returns_notice_number: str = None           # Numer zawiadomienia o zwrotach
    returns_notice_date: datetime = None        # Data zawiadomienia o zwrotach


@dataclass
class Allowance:
    percentage: str = None                      # Oprocentowanie obniżki
    allowance_amount: float = None              # Wartość obniżki
    original_amount: float = None               # Wartość sprzed obniżki


@dataclass
class LineAllowances:
    allowance: Allowance = Allowance()


@dataclass
class Charge:
    percentage: str = None                      # Procent obciążenia
    charge_amount: float = None                 # Wartość obciążenia
    original_amount: float = None               # Wartość sprzed obciążenia
    special_service: str = None                 # Kod identyfikujący usługę specjalną, np. TX = opłata cukrowa
    special_service_description: str = None     # Opis usługi specjalnej


@dataclass
class LineCharges:
    charge: Charge = Charge()


@dataclass
class LineMeasurements:
    net_weight: float = None                    # Waga netto


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
    tax_rate: float = None                      # Stawka VAT
    # Kod stawki:
    # "E" (exempt) - zwolniony
    # "S" (standard) - inna, wyrażona liczba ("standardowa")
    # "NA" (not applicable) – nie podlega "AE" (reverse charge) - odwrotne obciążenie
    tax_category_code: str = None
    tax_amount: float = 0                    # Suma VAT dla danej stawki
    taxable_basis: float = 0                 # Kwota podlegająca opodatkowaniu objęta daną stawką
    taxable_amount: float = 0                # Kwota netto objęta daną stawką
    gross_amount: float = 0                  # Kwota brutto objęta daną stawką
    previous_tax_rate: float = None             # Stawka VAT przed korektą
    # Kod stawki:
    # "E" (exempt) - zwolniony
    # "S" (standard) - inna, wyrażona liczba ("standardowa")
    # "NA" (not applicable) – nie podlega "AE" (reverse charge) - odwrotne obciążenie
    previous_tax_category_code: str = None
    previous_tax_amount: float = None            # Suma VAT dla danej stawki przed korektą
    previous_taxable_amount: float = None        # Kwota netto objęta daną stawką przed korektą
    # Suma VAT dla danej stawki – różnica pomiędzy wartością prawidłową, a korygowaną
    correction_tax_amount: float = None
    # Kwota netto objęta daną stawką – różnica pomiędzy wartością prawidłową, a korygowaną
    correction_taxable_amount: float = None
    # Kwota brutto objęta daną stawką – różnica pomiędzy wartością prawidłową, a korygowaną
    correction_gross_amount: float = None


class TaxSummary:
    def __init__(self, tax_summary_line: TaxSummaryLine = field(default_factory=[TaxSummaryLine()])):
        self.tax_summary_line = [tax_summary_line]


@dataclass
class DepositSummary:
    total_net_amount: float = None               # Suma netto po doliczeniu kwoty za opakowania kaucjonowane
    total_gross_amount: float = None             # Suma brutto po doliczeniu kwoty za opakowania kaucjonowane
    # Suma netto po doliczeniu kwoty za opakowania kaucjonowane przed korektą
    previous_total_net_amount: float = None
    # Suma brutto po doliczeniu kwoty za opakowania kaucjonowane przed korektą
    previous_total_gross_amount: float = None
    # Suma netto po doliczeniu kwoty za opakowania kaucjonowane – różnica pomiędzy wartością prawidłową, a korygowaną
    correction_total_net_amount: float = None
    # Suma brutto po doliczeniu kwoty za opakowania kaucjonowane – różnica pomiędzy wartością prawidłową, a korygowaną
    correction_total_gross_amount: float = None


@dataclass
class Charge:
    charge_number: str = None                    # Numer obciążenia
    charge_amount: float = None                  # Wartość obciążenia
    special_service: str = None                  # Kod identyfikujący usługę specjalną, np. TX = opłata cukrowa
    special_service_description: str = None      # Opis usługi specjalnej


@dataclass
class ChargeSummary:
    charge: Charge = Charge()


@dataclass
class InvoiceSummary:
    total_lines: int = 0                         # Ilość linii
    total_net_amount: float = 0                  # Suma netto
    total_taxable_basis: float = 0               # Suma podlegająca opodatkowaniu
    total_tax_amount: float = None               # Suma VAT
    total_gross_amount: float = None             # Suma brutto
    total_deposit_amount: float = None           # Suma kaucji za towary kaucjonowane
    total_discount_amount: float = None          # Wartość kwoty należnego upustu
    total_net_amout_without_charges: float = None       # Suma netto bez dodatkowej opłaty
    previous_total_net_amount: float = None      # Suma netto przed korektą
    previous_total_taxable_basis: float = None   # Suma podlegająca opodatkowaniu przed korektą
    previous_total_tax_amount: float = None      # Suma VAT przed korektą
    previous_total_gross_amount: float = None    # Suma brutto przed korektą
    previous_total_deposit_amount: float = None  # Suma kaucji za towary kaucjonowane przed korektą
    correction_total_net_amount: float = None    # Suma netto.Różnica pomiędzy wartością prawidłową, a korygowaną
    # Suma podlegająca opodatkowaniu – różnica pomiędzy wartością prawidłową, a korygowaną
    correction_total_taxable_basis: float = None
    correction_total_tax_amount: float = None    # Suma VAT – różnica pomiędzy wartością prawidłową, a korygowaną
    correction_total_gross_amount: float = None  # Suma brutto.Różnica pomiędzy wartością prawidłową a korygowaną
    # Suma kaucji za towary kaucjonowane – różnica pomiędzy wartością prawidłową, a korygowaną
    correction_total_deposit_amount: float = None
    gross_amount_in_words: str = None            # Suma brutto słownie
    tax_summary: TaxSummary = TaxSummary()
    deposit_summary: DepositSummary = DepositSummary()
    charge_summary: ChargeSummary = ChargeSummary()


class DocumentInvoice:
    invoice_header: InvoiceHeader = InvoiceHeader()
    invoice_parties: InvoiceParties = InvoiceParties()
    invoice_lines: list[InvoiceLines] = []
    invoice_summary: InvoiceSummary = InvoiceSummary()

    def add(self, item):
        return self.invoice_lines.append(item)

    # def __init__(self, invoice_header: InvoiceHeader = InvoiceHeader(),
    #          invoice_parties: InvoiceParties = InvoiceParties(),
    #          invoice_lines: InvoiceLines = field(default_factory=[InvoiceLines()]),
    #          invoice_summary: InvoiceSummary = InvoiceSummary()):
    # self.invoice_header = invoice_header
    # self.invoice_parties = invoice_parties
    # self.invoice_lines = [invoice_lines]
    # self.invoice_summary = invoice_summary
