# importing required modules
import PyPDF2
import json
import glob
import os
import base64
import requests
# import the Elasticsearch low-level client library
from elasticsearch import Elasticsearch
from PyPDF2 import PdfFileReader
# creating a pdf file object

os.chdir("C:\\Users\\HP ELITEBOOK G6\\Documents\\GitHub\\Projet-2-daar\\cv") #Répertoire à changer!
files = glob.glob("*.*") #Prendre tout les cv au sein du répertoire 

def index_pdf(file,i,phrase):
    reader = PyPDF2.PdfFileReader(file)

    #metadata = reader.getDocumentInfo()
    #print (metadata)

    #fields = reader.getFields()

    # creating a page object and extracting text from page

    #pdftext = ""
    #for page in range(reader.numPages):
        #pageObj = reader.getPage(page)
        #pdftext += pageObj.extractText().replace('\n','')

    #print(pageObj)

    # get the read object's meta info
    pdf_meta = reader.getDocumentInfo()

    # printing number of pages in pdf file
    num = reader.getNumPages()
    ##########print ("PDF pages:", num)###############

    # create a dictionary object for page data
    all_pages = {}

    # put meta data into a dict key
    all_pages["meta"] = {}

    # Use 'iteritems()` instead of 'items()' for Python 2
    for meta, value in pdf_meta.items():
        ##########print (meta, value)###############
        all_pages["meta"][meta] = value

    # iterate the page numbers
    for page in range(num):
        data = reader.getPage(page)
        #page_mode = read_pdf.getPageMode()

        # extract the page's text
        page_text = data.extractText()

        # put the text data into the dict
        all_pages[page] = page_text

    #res = requests.get('http://localhost:9200')
    #print(res.content)
    # create a JSON string from the dictionary
    json_data = json.dumps(all_pages)
    #####print ("\nJSON:", json_data)####################

    # convert JSON string to bytes-like obj
    #bytes_string = bytes(json_data, 'utf-8')
    #print ("\nbytes_string:", bytes_string)

    # convert bytes to base64 encoded string
    #encoded_pdf = base64.b64encode(bytes_string)
    #encoded_pdf = str(encoded_pdf)
    #print ("\nbase64:", encoded_pdf)


    # put the PDF data into a dictionary body to pass to the API request
    body_doc = {"data": json_data}

    # call the index() method to index the data
    elastic_client = Elasticsearch([{'host': 'localhost', 'port': 9200}])
    result = elastic_client.index(index="pdf", doc_type="_doc", id=i, body= body_doc)

    # print the returned results
    print ("\nindex result:", result['result'])

    result = elastic_client.get(index="pdf", id=i)
    
    #print(result['_source'])

    elastic_client.indices.refresh(index="pdf")

    #result = elastic_client.search(index="pdf", query={"match_all": {}})
    #print("Got %d Hits:" % result['hits']['total']['value'])

    result = elastic_client.search(index="pdf", body={"query": {"match": {"data": str(phrase)}}})
    ##########print("Got %d Hits:" % result['hits']['total']['value'])##########


    #index result: created

    #curl -XGET "localhost:9200/pdf/_doc/42?pretty=true"
    hits=result['hits']['total']['value']
    return hits
    
    
print("--------------------------------------------------------------------------")
phrase=input("Quelle est la phrase a rechercher?\n")
i=0
for file in files:
    hits=index_pdf(file,i,phrase)
    i+=1
print("L'occurence de "+phrase+" est :"+str(hits))
print("--------------------------------------------------------------------------")