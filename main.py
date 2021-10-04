from dataclasses import dataclass
from datetime import datetime


@dataclass
class Delivery:
    delivery_location_number: str = None
    delivery_date: datetime = None
    despatch_number: str = None


@dataclass
class Order:
    buyer_order_number: str = None
    supplier_order_number: str = None
    buyer_order_date: datetime = None


@dataclass
class Reference:
    invoice_reference_number: str = None
    invoice_reference_date: datetime = None


@dataclass
class DeliveryTerms:
    delivery_terms_code: str = None
    payment_method: str = None


@dataclass
class Delivery:
    delivery_location_number: int = 0
    tax_id: str = None
    delivery_date: datetime = None
    despatch_number: str = None
    despatch_date: datetime = None
    despatch_advice_number: str = None
    name: str = None
    street_and_number: str = None
    city_name: str = None
    postal_code: str = None
    country: str = None
    delivery_terms: DeliveryTerms = DeliveryTerms()


@dataclass
class Returns:
    returns_notice_number: str = None
    returns_notice_date: str = None


@dataclass
class InvoiceHeader:
    invoice_number: str = None
    invoice_date: datetime = None
    sales_date: datetime = None
    invoice_duplicate_date: datetime = None
    invoice_currency: str = None
    invoice_payment_due_date: datetime = None
    invoice_payment_terms: int = 0
    invoice_payment_means: str = None
    payment_information: str = None
    deferred_payment: str = None
    invoice_post_date: datetime = None
    document_function_code: str = None
    message_type: str = None
    correction_reason: str = None
    remakes: str = None
    order: Order = Order()
    reference: Reference = Reference()
    delivery: Delivery = Delivery()
    returns: Returns = Returns()


@dataclass
class Buyer:
    iln: int = None
    tax_id: str = None
    account_number: str = None
    name: str = None
    street_and_number: str = None
    city_name: str = None
    postal_code: str = None
    country: str = None


@dataclass
class Payer:
    iln: int = None
    tax_id: str = None
    account_number: str = None
    name: str = None
    street_and_number: str = None
    city_name: str = None
    postal_code: str = None
    country: str = None


@dataclass
class Invoicee:
    iln: int = None
    tax_id: str = None
    account_number: str = None
    name: str = None
    street_and_number: str = None
    city_name: str = None
    postal_code: str = None
    country: str = None


@dataclass
class ContactInformation:
    contact_id: str = None
    contact_name: str = None
    phone_number: str = None
    fax: str = None
    electronic_mail: str = None
    x400: str = None


@dataclass
class AccountingContactInformation:
    contact_id: str = None
    contact_name: str = None
    phone_number: str = None
    fax: str = None
    electronic_mail: str = None
    x400: str = None


@dataclass
class SalesAdministration:
    contact_id: str = None
    contact_name: str = None
    phone_number: str = None
    fax: str = None
    electronic_mail: str = None
    x400: str = None


@dataclass
class SalesRepresentative:
    contact_id: str = None
    contact_name: str = None
    phone_number: str = None
    fax: str = None
    electronic_mail: str = None
    x400: str = None


@dataclass
class Seller:
    iln: int = None
    tax_id: str = None
    account_number: str = None
    financial_institution_name: str = None
    code_by_buyer: str = None
    name: str = None
    street_and_number: str = None
    city_name: str = None
    postal_code: str = None
    country: str = None
    utilization_register_number: str = None
    court_and_capital_information: str = None
    certificate_number: str = None
    contact_information: ContactInformation = ContactInformation()
    accounting_contact_information: AccountingContactInformation = AccountingContactInformation()
    sales_administration: SalesAdministration = SalesAdministration()
    sales_representative: SalesRepresentative = SalesRepresentative()


@dataclass
class Payee:
    iln: int = None
    tax_id: str = None
    account_number: str = None
    name: str = None
    street_and_number: str = None
    city_name: str = None
    postal_code: str = None
    country: str = None


@dataclass
class SellerHeadquarters:
    iln: int = None
    name: str = None
    street_and_number: str = None
    city_name: str = None
    postal_code: str = None
    country: str = None


@dataclass
class OrderedBy:
    iln: int = None
    tax_id: str = None
    account_number: str = None
    name: str = None
    street_and_number: str = None
    city_name: str = None
    postal_code: str = None
    country: str = None


@dataclass
class Sender:
    iln: int = None
    tax_id: str = None
    name: str = None
    street_and_number: str = None
    city_name: str = None
    postal_code: str = None
    country: str = None


@dataclass
class Receiver:
    iln: int = None
    tax_id: str = None
    name: str = None
    street_and_number: str = None
    city_name: str = None
    postal_code: str = None
    country: str = None


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
    line_number: int = None
    order_line_number: int = None
    ean: str = None
    buyer_item_code: str = None
    supplier_item_code: str = None
    manufacturer_item_code: str = None
    serial_number: str = None
    customs_code: str = None
    item_description: str = None
    item_type: str = None
    country_of_origin: str = None
    grade: str = None
    variety: str = None
    payment_information: str = None
    product_type: str = None
    product_size: str = None
    product_color: str = None
    special_conditions: str = None
    invoice_quantity: float = None
    unit_of_measure: str = None
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
