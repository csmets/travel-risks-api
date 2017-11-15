""" Script to injest all country risks from smart traveller """

import json
import requests
from lxml import html
from ingester import get_country_code
from ingester import insert_record

def ingest(table_name):
    """
        Large wrapping function to do the ingestion of country risk data from
        smart traveller.
    """

    smarttraveler_request = requests.get(
        'http://smartraveller.gov.au/countries/pages/list.aspx')

    raw_source = smarttraveler_request.text

    html_source = html.fromstring(raw_source)

    javascript = html_source.cssselect(
        '#rs_read_this > div.content__main > script')[0]

    countries = json.loads(javascript.text[60:-2])

    for country in countries:
        record = dict()

        record['name'] = country['Title']

        record['code'] = get_country_code(country['Title'])

        record['link'] = 'http://smartraveller.gov.au/' + country['FileRef'][1:]

        raw_date_string = country['ArticleStartDate']

        if raw_date_string is not None:
            record['date'] = int(raw_date_string[6:-5])

        else:
            record['date'] = None

        record['source'] = 'smartraveller'

        risks = json.loads(country['Smartraveller_x0020_Advice_x0020_Levels'])

        risk_areas = []

        if len(risks['items']) > 0:
            count = 0

            for risk in risks['items']:
                if count < 1:
                    if 'level' in risk:
                        record['risk_level'] = risk['level']
                    else:
                        record['risk_level'] = None
                else:
                    risk_areas.append(risk)

                count = count + 1
        else:
            record['risk_level'] = None

        if len(risk_areas) < 1:
            record['risk_regions'] = None
        else:
            record['risk_regions'] = json.dumps(risk_areas)

        insert_record(table_name, record)
