import sqlite3


class Db:
    def get_iln(self, nip: str):
        with sqlite3.connect('gln.db') as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT iln FROM main.company WHERE nip=(?)', (nip,))
            answer = cursor.fetchone()
            return answer[0] if answer is not None else ''
