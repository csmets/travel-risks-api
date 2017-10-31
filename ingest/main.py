""" Main file to orchestrate the ingestion to a database """

import ingester

table_name = 'test_table'

ingester.create_table(table_name)

ingester.smartraveller.ingest(table_name)

ingester.show_records(table_name)
