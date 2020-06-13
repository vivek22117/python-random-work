import json
from datetime import datetime

import boto3
from elasticsearch import Elasticsearch, helpers, RequestsHttpConnection
from requests_aws4auth import AWS4Auth

host = 'https://search-ria-search-arp7smypu7ru2ew6qyip343zdi.us-east-1.es.amazonaws.com/'       # ES Domain Name
my_region = 'us-east-1'

service = 'es'
credentials = boto3.Session(region_name='us-east-1', profile_name='default').get_credentials()

access_key = credentials.access_key
secret_key = credentials.secret_key
token = credentials.token

aws_auth = AWS4Auth(
    access_key,
    secret_key,
    my_region,
    service
)

es_client = Elasticsearch(
    hosts=[host],
    http_auth=aws_auth,
    use_ssl=True,
    verify_certs=True,
    connection_class=RequestsHttpConnection
)

es_client.count()


def portfolio_cost(file_name):
    """
     Read file and persist data in ES
    :param file_name: name of the file
    """
    key_words_list = []
    with open(file_name, 'r') as f:
        count = 0
        for line in f:
            # if count == 15000:
            #     break
            line = line.strip()  # Removes the blank spaces
            parts = line.split(';')
            parts[0] = parts[0].strip('"')
            if 'C11' in parts[1]:                                   # Need to update the the code 'C11' to run for multiple codes, like F01, F02...& C01 to C11
                parts[1] = parts[1].strip('"').replace(".", '')[1:]
                dict_doc = {"title": parts[0], "code": int(parts[1]), "timestamp": datetime.now().strftime("%Y-%m-%d")}
                key_words_list.append(dict_doc)
                key_words_list.sort(key=lambda item: item['code'])

        print("Dict docs length:", len(key_words_list))

    final_list = []
    for item in key_words_list:
        temp_dict = {"title": item['title'], "subcodes": [], "timestamp": datetime.now().strftime("%Y-%m-%d")}
        for otherItems in key_words_list[key_words_list.index(item)+1:]:
            code_one = str(otherItems['code'])
            code_two = str(item['code'])
            if code_two in code_one and len(code_one) - len(code_two) == 3:
                temp_dict['subcodes'].append(otherItems['title'])
                if(len(temp_dict['subcodes'])) >= 4:
                    break
            else:
                otherItems = None
                continue
        final_list.append(temp_dict)

    from elasticsearch import Elasticsearch, helpers, RequestsHttpConnection

    print(len(final_list))
    resp = helpers.bulk(es_client, final_list, index='indications', doc_type="_doc")
    # print the response returned by Elasticsearch
    print("helpers.bulk() RESPONSE:", resp)
    # for data in key_words_list:
    #     try:
    #         print("\nAttempting to index the list of docs using helpers.bulk()")
    #         print(data)
    #         resp = es_client.index(index='indications_one', doc_type="_doc", body=data)
    #         # resp = helpers.bulk(es_client, key_words_list, index='indications', doc_type="_doc")
    #         # print the response returned by Elasticsearch
    #         print("helpers.bulk() RESPONSE:", resp)
    #         print("helpers.bulk() RESPONSE:", json.dumps(resp, indent=4))
    #     except Exception as err:
    #         print("Elasticsearch helpers.bulk() ERROR:", err)


portfolio_cost('../data/mtrees2019.bin')
