"""
Database loader and query functions
"""

import sqlite3

class Database():
    """
    This class is used as a handler to grab data out of the database
    """


    def __init__(self):

        self._conn = sqlite3.connect('travel_risks.db')
        self._c = self._conn.cursor()


    def _json_record(self, data, multiple):
        """
        Grab sql row and return it as a json object with columns as the keys.
        """

        if multiple is True:

            record = [dict((self._c.description[i][0], value) \
                for i, value in enumerate(row)) for row in data]

        else:

            record = dict((self._c.description[i][0], value) \
                for i, value in enumerate(data))

        return record


    def _get_results(self, multiple):
        """
        Fetch the results from the sql cursor and return a json result
        """

        if multiple is True:

            record = self._c.fetchall()

        else:

            record = self._c.fetchone()

        if record is not None:

            if len(record) > 0:

                result = self._json_record(record, multiple)

                return result

        return None


    def fetch(self, table, key, value):

        with self._conn:

            self._c.execute(
                "SELECT * FROM {table} WHERE {column} LIKE :value"
                .format(table=table, column=key),
                {
                    'value': value
                }
            )

            result = self._get_results(False)

            return result


    def fetchand(self, table, key1, value1, key2, value2):

        with self._conn:

            self._c.execute("""
                SELECT * FROM {table} WHERE
                {column1} LIKE :value1
                and
                {column2} IS :value2
                """.format(table=table, column1=key1, column2=key2),
                            {
                                "value1": value1,
                                "value2": value2
                            })

            result = self._get_results(False)

            return result


    def fetchall(self, table):

        with self._conn:

            self._c.execute("SELECT * FROM {table}".format(table=table))

            result = self._get_results(True)

            return result


    def fetchall_match_column(self, table, column, match):

        with self._conn:

            self._c.execute("""
                SELECT * FROM {table}
                WHERE {column} IS :match
                """.format(table=table, column=column), {'match': match})

            result = self._get_results(True)

            return result
