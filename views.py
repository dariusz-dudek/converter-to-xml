from containers.xml_template_classes_full_classes import DocumentInvoice
from contractors.add_contractor import add_contractor_all
from pyexcel.exceptions import FileTypeNotSupported
from containers.calculate_sumary import Sumary
from converters.excel_mag_krak import MagKrak
from converters.sewera_csv import Sewera
from terminaltables import AsciiTable
from converters.raw_pol import Rawpol
from abc import ABC, abstractmethod
from draw import draw_xml


class AbstractView(ABC):
    def __init__(self):
        self.repositories = {}

    @abstractmethod
    def draw(self):
        pass

    def set_repository(self, name, repository):
        self.repositories[name] = repository


class AddFunction:
    @staticmethod
    def load_file(converter, xml_doc, name):
        found_file = False
        while not found_file:
            file_name = input('Podaj nazwę pliku wraz z rozszerzeniem lub napisz quit aby wyjść: ')
            if file_name == 'quit':
                found_file = True
                continue
            try:
                converter.read(file_name, xml_doc)
                add_contractor_all(xml_doc)
                Sumary.calculate_sumary(xml_doc)
                draw_xml(f'result/{name}.xml', xml_doc)
                found_file = True
            except FileNotFoundError:
                print(f'\nPliku {file_name} nie znaleziono.')
                print('Spróbuj jeszcze raz.\n')
            except FileTypeNotSupported:
                print(f'\nNieobsługiwany rodzaj pliku.')
                print('Spróbuj jeszcze raz.\n')
            except IndexError:
                print('\nWynik operacji poza skalą lub nieobsługiwany rodzaj pliku.')
                print('Spróbuj jeszcze raz.\n')


class SeweraImport(AbstractView):
    SHORTCUT = 'sewera'
    LABEL = 'Plik SEWERA csv'

    def draw(self):
        print(SeweraImport.LABEL)
        xml_document = DocumentInvoice()
        sewera = Sewera()
        AddFunction.load_file(sewera, xml_document, SeweraImport.SHORTCUT)


class RawpolImport(AbstractView):
    SHORTCUT = 'rawpol'
    LABEL = 'Plik RAW-POL csv'

    def draw(self):
        print(RawpolImport.LABEL)
        xml_document = DocumentInvoice()
        rawpol = Rawpol()
        AddFunction.load_file(rawpol, xml_document, RawpolImport.SHORTCUT)


class MagKrakImport(AbstractView):
    SHORTCUT = 'magkrak'
    LABEL = 'Plik Mag Krak xls'

    def draw(self):
        print(MagKrakImport.LABEL)
        xml_document = DocumentInvoice()
        mag_krak = MagKrak()
        AddFunction.load_file(mag_krak, xml_document, MagKrakImport.SHORTCUT)


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
