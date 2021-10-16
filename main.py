from views import MainMenu
from converters.sewera_csv import Sewera
from converters.raw_pol import Rawpol
from converters.excel_mag_krak import MagKrak
# from dotenv import load_dotenv, find_dotenv


class Application:
    def main(self):
        # load_dotenv(find_dotenv())
        menu = MainMenu()
        menu.draw()

        sewera_repository = self.get_sewera_repository()
        rawpol_repository = self.get_rawpol_repoository()
        mag_krak_repository = self.get_mag_krak_repository()

        screen = menu.get_screen()
        screen.set_repository('sewera', sewera_repository)
        screen.set_repository('rawpol', rawpol_repository)
        screen.set_repository('magkrak', mag_krak_repository)

        screen.draw()

    def get_sewera_repository(self):
        return Sewera()

    def get_rawpol_repoository(self):
        return Rawpol()

    def get_mag_krak_repository(self):
        return MagKrak()


if __name__ == '__main__':
    app = Application()
    app.main()
