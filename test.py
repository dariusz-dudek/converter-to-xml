from dotenv import load_dotenv, find_dotenv, dotenv_values
from os import getenv

# config = dotenv_values(".env")
#
# print(config['API_REGONAPI'])

# API_REGONAPI = ''
# API_LOGIN = ''

load_dotenv()

# print(f'{getenv("API_REGONAPI")} -- {getenv("API_LOGIN")}')


class Foo:

    def print(self):
        # load_dotenv(find_dotenv())
        return f'{getenv("API_REGONAPI")} -- {getenv("API_LOGIN")}'


if __name__ == '__main__':

    foo = Foo()
    print(foo.print())
