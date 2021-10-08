from dataclasses import dataclass, field
from typing import Mapping, Any


@dataclass
class Order:
    kwargs: Mapping[Any, Any]

    def __init__(self, **kwargs):
        self.kwargs = kwargs


@dataclass
class Reference:
    kwargs: Mapping[Any, Any]

    def __init__(self, **kwargs):
        self.kwargs = kwargs


@dataclass
class DeliveryTerms:
    kwargs: Mapping[Any, Any]

    def __init__(self, **kwargs):
        self.kwargs = kwargs


@dataclass
class Delivery:
    kwargs: Mapping[Any, Any]

    def __init__(self, delivery_terms: DeliveryTerms = DeliveryTerms(), **kwargs):
        self.delivery_terms: delivery_terms
        self.kwargs = kwargs


@dataclass
class Returns:
    kwargs: Mapping[Any, Any]

    def __init__(self, **kwargs):
        self.kwargs = kwargs


@dataclass
class InvoiceHeader:
    kwargs: Mapping[Any, Any]

    def __init__(
            self,
            order: Order = Order(),
            reference: Reference = Reference(),
            delivery: Delivery = Delivery(),
            returns: Returns = Returns(),
            **kwargs):
        self.returns = returns
        self.delivery = delivery
        self.reference = reference
        self.order = order
        self.kwargs = kwargs


@dataclass
class Buyer:
    kwargs: Mapping[Any, Any]

    def __init__(self, **kwargs):
        self.kwargs = kwargs


@dataclass
class Payer:
    kwargs: Mapping[Any, Any]

    def __init__(self, **kwargs):
        self.kwargs = kwargs


@dataclass
class Invoicee:
    kwargs: Mapping[Any, Any]

    def __init__(self, **kwargs):
        self.kwargs = kwargs


@dataclass
class ContactInformation:
    kwargs: Mapping[Any, Any]

    def __init__(self, **kwargs):
        self.kwargs = kwargs


@dataclass
class AccountingContactInformation:
    kwargs: Mapping[Any, Any]

    def __init__(self, **kwargs):
        self.kwargs = kwargs


@dataclass
class SalesAdministration:
    kwargs: Mapping[Any, Any]

    def __init__(self, **kwargs):
        self.kwargs = kwargs


@dataclass
class SalesRepresentative:
    kwargs: Mapping[Any, Any]

    def __init__(self, **kwargs):
        self.kwargs = kwargs


@dataclass
class Seller:
    kwargs: Mapping[Any, Any]

    def __init__(
            self,
            contact_information: ContactInformation = ContactInformation(),
            accounting_contact_information: AccountingContactInformation = AccountingContactInformation(),
            sales_administration: SalesAdministration = SalesAdministration(),
            sales_representative: SalesRepresentative = SalesRepresentative(),
            **kwargs
    ):
        self.sales_representative = sales_representative
        self.sales_administration = sales_administration
        self.accounting_contact_information = accounting_contact_information
        self.contact_information = contact_information
        self.kwargs = kwargs


@dataclass
class Payee:
    kwargs: Mapping[Any, Any]

    def __init__(self, **kwargs):
        self.kwargs = kwargs


@dataclass
class SellerHeadquarters:
    kwargs: Mapping[Any, Any]

    def __init__(self, **kwargs):
        self.kwargs = kwargs


@dataclass
class OrderedBy:
    kwargs: Mapping[Any, Any]

    def __init__(self, **kwargs):
        self.kwargs = kwargs


@dataclass
class Sender:
    kwargs: Mapping[Any, Any]

    def __init__(self, **kwargs):
        self.kwargs = kwargs


@dataclass
class Receiver:
    kwargs: Mapping[Any, Any]

    def __init__(self, **kwargs):
        self.kwargs = kwargs


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
    kwargs: Mapping[Any, Any]

    def __init__(self, **kwargs):
        self.kwargs = kwargs


@dataclass
class LineItem:
    kwargs: Mapping[Any, Any]

    def __init__(
            self,
            tax_reference: TaxReference = TaxReference(),
            **kwargs
    ):
        self.tax_reference = tax_reference
        self.kwargs = kwargs


@dataclass
class LineOrder:
    kwargs: Mapping[Any, Any]

    def __init__(self, **kwargs):
        self.kwargs = kwargs


@dataclass
class LineReference:
    kwargs: Mapping[Any, Any]

    def __init__(self, **kwargs):
        self.kwargs = kwargs


@dataclass
class DeliveryTerms:
    kwargs: Mapping[Any, Any]

    def __init__(self, **kwargs):
        self.kwargs = kwargs


@dataclass
class LineDelivery:
    kwargs: Mapping[Any, Any]

    def __init__(
            self,
            delivery_terms: DeliveryTerms = DeliveryTerms(),
            **kwargs
    ):
        self.delivery_terms = delivery_terms
        self.kwargs = kwargs


@dataclass
class LineReturns:
    kwargs: Mapping[Any, Any]

    def __init__(self, **kwargs):
        self.kwargs = kwargs


@dataclass
class Allowance:
    kwargs: Mapping[Any, Any]

    def __init__(self, **kwargs):
        self.kwargs = kwargs


@dataclass
class LineAllowances:
    allowance: Allowance = Allowance()


@dataclass
class Charge:
    kwargs: Mapping[Any, Any]

    def __init__(self, **kwargs):
        self.kwargs = kwargs


@dataclass
class LineCharges:
    charge: Charge = Charge()


@dataclass
class LineMeasurements:
    kwargs: Mapping[Any, Any]

    def __init__(self, **kwargs):
        self.kwargs = kwargs


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
    kwargs: Mapping[Any, Any]

    def __init__(self, **kwargs):
        self.kwargs = kwargs


class TaxSummary:
    def __init__(self, tax_summary_line: TaxSummaryLine = field(default_factory=[TaxSummaryLine()])):
        self.tax_summary_line = [tax_summary_line]


@dataclass
class DepositSummary:
    kwargs: Mapping[Any, Any]

    def __init__(self, **kwargs):
        self.kwargs = kwargs


@dataclass
class Charge:
    kwargs: Mapping[Any, Any]

    def __init__(self, **kwargs):
        self.kwargs = kwargs


@dataclass
class ChargeSummary:
    charge: Charge = Charge()


@dataclass
class InvoiceSummary:
    kwargs: Mapping[Any, Any]

    def __init__(
            self,
            tax_summary: TaxSummary = TaxSummary(),
            deposit_summary: DepositSummary = DepositSummary(),
            charge_summary: ChargeSummary = ChargeSummary(),
            **kwargs
    ):
        self.charge_summary = charge_summary
        self.deposit_summary = deposit_summary
        self.tax_summary = tax_summary
        self.kwargs = kwargs


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
