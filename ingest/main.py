""" Main file to orchestrate the ingestion to a database """

import ingester

table_name = 'travel_risks'

ingester.create_table(table_name)

ingester.smartraveller.ingest(table_name)
