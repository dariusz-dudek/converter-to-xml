from dataclasses import dataclass
from datetime import datetime


@dataclass
class Delivery:
    delivery_location_number: str = ''
    delivery_date: datetime = datetime.today()
    despatch_number: str = ''


@dataclass
class Order:
    buyer_order_number: str = ''
    supplier_order_number: str = ''
    buyer_order_date: datetime = datetime.today()


@dataclass
class Reference:
    invoice_reference_number: str = ''
    invoice_reference_date: datetime = datetime.today()


@ dataclass
class DeliveryTerms:
    delivery_terms_code: str = ''
    payment_method: str = ''


@dataclass
class Delivery:
    delivery_location_number: int = 0
    tax_id: str = ''
    delivery_date: datetime = datetime.today()
    despatch_number: str = ''
    despatch_date: datetime = datetime.today()
    despatch_advice_number: str = ''
    name: str = ''
    street_and_number: str = ''
    city_name: str = ''
    postal_code: str = ''
    country: str = ''
    delivery_terms: DeliveryTerms = DeliveryTerms()


@dataclass
class Returns:
    returns_notice_number: str = ''
    returns_notice_date: str = ''

@dataclass
class InvoiceHeader:
    invoice_number: str = ''
    invoice_date: datetime = datetime.today()
    sales_date: datetime = datetime.today()
    invoice_duplicate_date: datetime = datetime.today()
    invoice_currency: str = ''
    invoice_payment_due_date: datetime = datetime.today()
    invoice_payment_terms: int = 0
    invoice_payment_means: str = ''
    payment_information: str = ''
    deferred_payment: str = ''
    invoice_post_date: datetime = datetime.today()
    document_function_code: str = ''
    message_type: str = ''
    correction_reason: str = ''
    remakes: str = ''
    order: Order = Order()
    reference: Reference = Reference()
    delivery: Delivery = Delivery()
    returns: Returns = Returns()


@dataclass
class Buyer:
    iln: int = None
    tax_id: str = ''
    account_number: str = ''
    name: str = ''
    street_and_number: str = ''
    city_name: str = ''
    postal_code: str = ''
    country: str = ''


@dataclass
class Payer:
    iln: int = None
    tax_id: str = ''
    account_number: str = ''
    name: str = ''
    street_and_number: str = ''
    city_name: str = ''
    postal_code: str = ''
    country: str = ''


@dataclass
class Invoicee:
    iln: int = None
    tax_id: str = ''
    account_number: str = ''
    name: str = ''
    street_and_number: str = ''
    city_name: str = ''
    postal_code: str = ''
    country: str = ''


@dataclass
class ContactInformation:
    contact_id: str = ''
    contact_name: str = ''
    phone_number: str = ''
    fax: str = ''
    electronic_mail: str = ''
    x400: str = ''


@dataclass
class AccountingContactInformation:
    contact_id: str = ''
    contact_name: str = ''
    phone_number: str = ''
    fax: str = ''
    electronic_mail: str = ''
    x400: str = ''


@dataclass
class SalesAdministration:
    contact_id: str = ''
    contact_name: str = ''
    phone_number: str = ''
    fax: str = ''
    electronic_mail: str = ''
    x400: str = ''


@dataclass
class SalesRepresentative:
    contact_id: str = ''
    contact_name: str = ''
    phone_number: str = ''
    fax: str = ''
    electronic_mail: str = ''
    x400: str = ''


@dataclass
class Seller:
    iln: int = None
    tax_id: str = ''
    account_number: str = ''
    financial_institution_name: str = ''
    code_by_buyer: str = ''
    name: str = ''
    street_and_number: str = ''
    city_name: str = ''
    postal_code: str = ''
    country: str = ''
    utilization_register_number: str = ''
    court_and_capital_information: str = ''
    certificate_number: str = ''
    contact_information: ContactInformation = ContactInformation()
    accounting_contact_information: AccountingContactInformation = AccountingContactInformation()
    sales_administration: SalesAdministration = SalesAdministration()
    sales_representative: SalesRepresentative = SalesRepresentative()


@dataclass
class Payee:
    iln: int = None
    tax_id: str = ''
    account_number: str = ''
    name: str = ''
    street_and_number: str = ''
    city_name: str = ''
    postal_code: str = ''
    country: str = ''


@dataclass
class SellerHeadquarters:
    iln: int = None
    name: str = ''
    street_and_number: str = ''
    city_name: str = ''
    postal_code: str = ''
    country: str = ''


@dataclass
class OrderedBy:
    iln: int = None
    tax_id: str = ''
    account_number: str = ''
    name: str = ''
    street_and_number: str = ''
    city_name: str = ''
    postal_code: str = ''
    country: str = ''


@dataclass
class Sender:
    iln: int = None
    tax_id: str = ''
    name: str = ''
    street_and_number: str = ''
    city_name: str = ''
    postal_code: str = ''
    country: str = ''


@dataclass
class Receiver:
    iln: int = None
    tax_id: str = ''
    name: str = ''
    street_and_number: str = ''
    city_name: str = ''
    postal_code: str = ''
    country: str = ''


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
    reference_type: str = ''
    reference_number: str = ''


@dataclass
class LineItem:
    line_number: int = None
    order_line_number: int = None
    ean: str = ''
    buyer_item_code: str = ''
    supplier_item_code: str = ''
    manufacturer_item_code: str = ''
    serial_number: str = ''
    customs_code: str = ''
    item_description: str = ''
    item_type: str = ''
    country_of_origin: str = ''
    grade: str = ''
    variety: str = ''
    payment_information: str = ''
    product_type: str = ''
    product_size: str = ''
    product_color: str = ''
    special_conditions: str = ''
    invoice_quantity: float = None
    unit_of_measure: str = ''
    invoice_unit_packsize: float = None
    pack_item_unit_of_measure: str = ''
    free_goods_quantity: float = None
    delivered_quantity: float = None
    invoice_unit_net_price: float = None
    invoice_unit_gross_price: float = None
    invoice_unit_retail_price: float = None
    invoice_unit_price_without_charges: float = None
    tax_rate: float = None
    tax_category_code: str = ''
    tax_reference: TaxReference = TaxReference()
    tax_amount: float = None
    net_amount: float = None
    deposit_amount: float = None
    previous_invoice_quantity: float = None
    previous_delivered_quantity: float = None
    previous_invoice_unit_net_price: float = None
    previous_tax_rate: float = None
    previous_tax_category_code: str = ''
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
    expiration_date: datetime = datetime.today()
    production_date: datetime = datetime.today()
    best_before_date: datetime = datetime.today()
    sales_date: datetime = datetime.today()
    certificate_number: str = ''
    correction_reason: str = ''
    utilization_fee: str = ''


@dataclass
class LineOrder:
    buyer_order_number: str = ''
    supplier_order_number: str = ''
    buyer_order_date: datetime = datetime.today()


@dataclass
class LineReference:
    invoice_reference_number: str = ''
    invoice_reference_date: datetime = datetime.today()


@dataclass
class DeliveryTerms:
    delivery_terms_code: str = ''
    payment_method: str = ''


@dataclass
class LineDelivery:
    delivery_location_number: str = ''
    tax_id: str = ''
    delivery_date: datetime = datetime.today()
    despatch_number: str = ''
    despatch_date: datetime = datetime.today()
    despatch_advice_number: str = ''
    ship_from_location_number: str = ''
    name: str = ''
    street_and_number: str = ''
    city_name: str = ''
    postal_code: str = ''
    country: str = ''
    delivery_terms: DeliveryTerms = DeliveryTerms()


@dataclass
class LineReturns:
    returns_notice_number: str = ''
    returns_notice_date: datetime = datetime.today()


@dataclass
class Allowance:
    percentage: str = ''
    allowance_amount: float = None
    original_amount: float = None


@dataclass
class LineAllowances:
    allowance: Allowance = Allowance()


@dataclass
class Charge:
    percentage: str = ''
    charge_amount: float = None
    original_amount: float = None
    special_service: str = ''
    special_service_description: str = ''


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
    tax_category_code: str = ''
    tax_amount: float = None
    taxable_basis: float = None
    taxable_amount: float = None
    gross_amount: float = None
    previous_tax_rate: float = None
    previous_tax_category_code: str = ''
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
    charge_number: str = ''
    charge_amount: float = None
    special_service: str = ''
    special_service_description: str = ''


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
    gross_amount_in_words: str = ''
    tax_summary: TaxSummary = TaxSummary()
    deposit_summary: DepositSummary = DepositSummary()
    charge_summary: ChargeSummary = ChargeSummary()


@dataclass
class DocumentInvoice:
    invoice_header: InvoiceHeader = InvoiceHeader()
    invoice_parties: InvoiceParties = InvoiceParties()
    invoice_lines: InvoiceLines = InvoiceLines()
    invoice_summary: InvoiceSummary = InvoiceSummary()


