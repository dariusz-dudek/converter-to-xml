from dataclasses import field
from typing import List


class Order:

    def __init__(self, **kwargs):
        self.kwargs = kwargs


class Reference:

    def __init__(self, **kwargs):
        self.kwargs = kwargs


class DeliveryTerms:

    def __init__(self, **kwargs):
        self.kwargs = kwargs


class Delivery:

    def __init__(self, delivery_terms: DeliveryTerms = DeliveryTerms(), **kwargs):
        self.delivery_terms: delivery_terms
        self.kwargs = kwargs


class Returns:

    def __init__(self, **kwargs):
        self.kwargs = kwargs


class InvoiceHeader:

    def __init__(
            self,
            order: Order = Order(),
            reference: Reference = Reference(),
            delivery: Delivery = Delivery(),
            returns: Returns = Returns(),
            ):
        self.returns = returns
        self.delivery = delivery
        self.reference = reference
        self.order = order


class Buyer:

    def __init__(self, **kwargs):
        self.kwargs = kwargs


class Payer:

    def __init__(self, **kwargs):
        self.kwargs = kwargs


class Invoicee:

    def __init__(self, **kwargs):
        self.kwargs = kwargs


class ContactInformation:

    def __init__(self, **kwargs):
        self.kwargs = kwargs


class AccountingContactInformation:

    def __init__(self, **kwargs):
        self.kwargs = kwargs


class SalesAdministration:

    def __init__(self, **kwargs):
        self.kwargs = kwargs


class SalesRepresentative:

    def __init__(self, **kwargs):
        self.kwargs = kwargs


class Seller:

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


class Payee:

    def __init__(self, **kwargs):
        self.kwargs = kwargs


class SellerHeadquarters:

    def __init__(self, **kwargs):
        self.kwargs = kwargs


class OrderedBy:

    def __init__(self, **kwargs):
        self.kwargs = kwargs


class Sender:

    def __init__(self, **kwargs):
        self.kwargs = kwargs


class Receiver:

    def __init__(self, **kwargs):
        self.kwargs = kwargs


class InvoiceParties:
    def __init__(
            self,
            buyer: Buyer = Buyer(),
            payer: Payer = Payer(),
            invoicee: Invoicee = Invoicee(),
            seller: Seller = Seller(),
            payee: Payee = Payee(),
            seller_headquarters: SellerHeadquarters = SellerHeadquarters(),
            sender: Sender = Sender(),
            ordered_by: OrderedBy = OrderedBy(),
            receiver: Receiver = Receiver()
    ):
        self.receiver = receiver
        self.ordered_by = ordered_by
        self.sender = sender
        self.seller_headquarters = seller_headquarters
        self.payee = payee
        self.seller = seller
        self.invoicee = invoicee
        self.payer = payer
        self.buyer = buyer


class TaxReference:

    def __init__(self, **kwargs):
        self.kwargs = kwargs


class LineItem:

    def __init__(
            self,
            tax_reference: TaxReference = TaxReference(),
            **kwargs
    ):
        self.tax_reference = tax_reference
        self.kwargs = kwargs


class LineOrder:

    def __init__(self, **kwargs):
        self.kwargs = kwargs


class LineReference:

    def __init__(self, **kwargs):
        self.kwargs = kwargs


class DeliveryTerms:

    def __init__(self, **kwargs):
        self.kwargs = kwargs


class LineDelivery:

    def __init__(
            self,
            delivery_terms: DeliveryTerms = DeliveryTerms(),
            **kwargs
    ):
        self.delivery_terms = delivery_terms
        self.kwargs = kwargs


class LineReturns:

    def __init__(self, **kwargs):
        self.kwargs = kwargs


class Allowance:

    def __init__(self, **kwargs):
        self.kwargs = kwargs


class LineAllowances:

    def __init__(self, allowance: Allowance = Allowance()):
        self.allowance = allowance


class Charge:

    def __init__(self, **kwargs):
        self.kwargs = kwargs


class LineCharges:
    def __init__(self, charge: Charge = Charge()):
        self.charge = charge


class LineMeasurements:

    def __init__(self, **kwargs):
        self.kwargs = kwargs


class Line:
    def __init__(
            self,
            line_item: LineItem = LineItem(),
            line_order: LineOrder = LineOrder(),
            line_reference: LineReference = LineReference(),
            line_delivery: LineDelivery = LineDelivery(),
            line_returns: LineReturns = LineReturns(),
            line_allowances: LineAllowances = LineAllowances(),
            line_charges: LineCharges = LineCharges(),
            line_measurements: LineMeasurements = LineMeasurements(),
    ):
        self.line_measurements = line_measurements
        self.line_charges = line_charges
        self.line_allowances = line_allowances
        self.line_returns = line_returns
        self.line_delivery = line_delivery
        self.line_reference = line_reference
        self.line_order = line_order
        self.line_item = line_item


class InvoiceLines:
    def __init__(self, line=None):
        if line is None:
            line = [Line]
        self.line = line

    # def add(self, item):
    #     return self.line.append(item)


class TaxSummaryLine:

    def __init__(self, **kwargs):
        self.kwargs = kwargs


class TaxSummary:
    def __init__(self, tax_summary_line: TaxSummaryLine = field(default_factory=[TaxSummaryLine])):
        self.tax_summary_line = [tax_summary_line]


class DepositSummary:

    def __init__(self, **kwargs):
        self.kwargs = kwargs


class Charge:

    def __init__(self, **kwargs):
        self.kwargs = kwargs


class ChargeSummary:

    def __init__(self, charge: Charge = Charge()):
        self.charge = charge


class InvoiceSummary:

    def __init__(
            self,
            tax_summary=None,
            deposit_summary: DepositSummary = DepositSummary(),
            charge_summary: ChargeSummary = ChargeSummary(),
            total_lines: int = 0,
            total_net_amount: float = 0,
            total_taxable_basis: float = 0,
            total_tax_amount: float = 0,
            total_gross_amount: float = 0,
            gross_amount_in_words: str = '',
            **kwargs
    ):
        self.total_lines = total_lines
        self.total_net_amount = total_net_amount
        self.total_taxable_basis = total_taxable_basis
        self.total_tax_amount = total_tax_amount
        self.total_gross_amount = total_gross_amount
        self.gross_amount_in_words = gross_amount_in_words
        if tax_summary is None:
            tax_summary = [TaxSummary]
        self.charge_summary = charge_summary
        self.deposit_summary = deposit_summary
        self.tax_summary = tax_summary
        self.kwargs = kwargs

    def add_tax(self, item):
        return self.tax_summary.append(item)


class DocumentInvoice:
    def __init__(
            self,
            invoice_header: InvoiceHeader = InvoiceHeader(),
            invoice_parties: InvoiceParties = InvoiceParties(),
            invoice_lines: InvoiceLines = InvoiceLines(),
            invoice_summary: InvoiceSummary = InvoiceSummary()):
        self.invoice_summary = invoice_summary
        self.invoice_lines = invoice_lines
        self.invoice_parties = invoice_parties
        self.invoice_header = invoice_header

    # def __init__(self, invoice_header: InvoiceHeader = InvoiceHeader(),
    #          invoice_parties: InvoiceParties = InvoiceParties(),
    #          invoice_lines: InvoiceLines = field(default_factory=[InvoiceLines()]),
    #          invoice_summary: InvoiceSummary = InvoiceSummary()):
    # self.invoice_header = invoice_header
    # self.invoice_parties = invoice_parties
    # self.invoice_lines = [invoice_lines]
    # self.invoice_summary = invoice_summary
