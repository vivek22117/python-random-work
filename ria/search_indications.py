import json
from datetime import datetime

import boto3
from elasticsearch import Elasticsearch, helpers, RequestsHttpConnection
from requests_aws4auth import AWS4Auth

host = 'https://search-ria-search-domain-cmcjo35zedg67zxibszoftjrvi.us-east-1.es.amazonaws.com'
region = 'us-east-1'

service = 'es'
credentials = boto3.Session().get_credentials()

es_client = Elasticsearch(
    hosts=[host],
    http_auth=AWS4Auth("AKIARP6EPALIQ3CFYRHA", "Nev3HODeib3hbjwydPRqHqUHGPyinvNpObssG0kF", 'us-east-1', 'es'),
    use_ssl=True,
    verify_certs=True,
    connection_class=RequestsHttpConnection
)


def portfolio_cost(file_name):
    """
     Read file and persist data in ES
    :param file_name: name of the file
    """

    key_words_list = []
    with open(file_name, 'r') as f:
        count = 0
        for line in f:
            if count == 59248:
                break
            line = line.strip()  # Removes the blank spaces
            parts = line.split(';')
            parts[0] = parts[0].strip('"')
            parts[1] = parts[1].strip('"')
            dict_doc = {"title": parts[0], "code": parts[1], "timestamp": datetime.now().strftime("%Y-%m-%d")}
            key_words_list.append(dict_doc)
            count += 1

        print("Dict docs length:", len(key_words_list))

    resp = helpers.bulk(es_client, key_words_list, index='indications', doc_type="_doc")
    # print the response returned by Elasticsearch
    print("helpers.bulk() RESPONSE:", resp)


portfolio_cost('../data/mtrees2019.bin')
