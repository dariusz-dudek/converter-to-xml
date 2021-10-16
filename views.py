from abc import ABC, abstractmethod
from terminaltables import AsciiTable
from converters.sewera_csv import Sewera
from converters.raw_pol import Rawpol
from converters.excel_mag_krak import MagKrak
from containers.xml_template_classes_full_classes import DocumentInvoice
from contractors.add_contractor import add_contractor_all
from draw import draw_xml


class AbstractView(ABC):
    def __init__(self):
        self.repositories = {}

    @abstractmethod
    def draw(self):
        pass

    def set_repository(self, name, repository):
        self.repositories[name] = repository


class SeweraImport(AbstractView):
    SHORTCUT = 'sewera'
    LABEL = 'Plik SEWERA csv'

    def draw(self):
        print(SeweraImport.LABEL)
        xml_document = DocumentInvoice()
        sewera = Sewera()
        file = input('Podaj nazwę pliku wraz z rozszerzeniem: ')
        sewera.read_from_csv(file, xml_document)
        add_contractor_all(xml_document)
        draw_xml('sewera.xml', xml_document)


class RawpolImport(AbstractView):
    SHORTCUT = 'rawpol'
    LABEL = 'Plik RAW-POL csv'

    def draw(self):
        print(RawpolImport.LABEL)
        xml_document = DocumentInvoice()
        rawpol = Rawpol()
        file = input('Podaj nazwę pliku wraz z rozszerzeniem: ')
        rawpol.read_from_csv(file, xml_document)
        add_contractor_all(xml_document)
        draw_xml('rawpol.xml', xml_document)


class MagKrakImport(AbstractView):
    SHORTCUT = 'magkrak'
    LABEL = 'Plik Mag Krak xls'

    def draw(self):
        print(MagKrakImport.LABEL)
        xml_document = DocumentInvoice()
        mag_krak = MagKrak()
        file = input('Podaj nazwę pliku wraz z rozszerzeniem: ')
        mag_krak.read_from_xls(file, xml_document)
        add_contractor_all(xml_document)
        draw_xml('magkrak.xml', xml_document)


class MainMenu(AbstractView):
    OPTIONS = {
        SeweraImport.SHORTCUT: SeweraImport(),
        RawpolImport.SHORTCUT: RawpolImport(),
        MagKrakImport.SHORTCUT: MagKrakImport()
    }

    def get_screen(self):
        option = None
        while option not in MainMenu.OPTIONS:
            option = input('Wybierz opcję: ')

        return MainMenu.OPTIONS[option]

    def draw(self):
        print('Powiedz co chcesz zrobić: ')
        rows = [['Komenda', 'Działanie']]
        for option, screen in MainMenu.OPTIONS.items():
            rows.append([option, screen.LABEL])

        table = AsciiTable(rows)

        print(table.table)
