""" Database functions """

import sqlite3

# Establish database connection
test_db = False

DB_FILE = 'travel_risks.db'

if test_db is True:
    conn = sqlite3.connect(':memory:')

else:
    conn = sqlite3.connect(DB_FILE)

c = conn.cursor()


def create_table(name):

    with conn:

        c.execute("""
            CREATE TABLE {name} (
                name text,
                code text,
                link text,
                risk_level text,
                risk_regions text,
                date integer,
                source text
                )""".format(name=name))


def insert_record(table_name, record):
    """ Function to insert risk records into the database """

    keys = [
        'name',
        'code',
        'link',
        'risk_level',
        'risk_regions',
        'date',
        'source'
    ]

    valid_record = True

    for key in keys:

        if key not in record:

            valid_record = False

            print(record['name'] + ': Missing ' + key + ' in parsed function argument')

    if valid_record is True:

        with conn:

            c.execute("""
                INSERT INTO {table_name} VALUES
                (:name, :code, :link, :risk_level, :risk_regions, :date, :source)
                """.format(table_name=table_name), {
                    'name': record['name'],
                    'code': record['code'],
                    'link': record['link'],
                    'risk_level': record['risk_level'],
                    'risk_regions': record['risk_regions'],
                    'date': record['date'],
                    'source': record['source']
                })


def show_records(table_name):

    with conn:

        c.execute("""
            SELECT * FROM {name};
        """.format(name=table_name))

        print(c.fetchall())
