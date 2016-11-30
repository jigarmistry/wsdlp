from suds.client import Client
from suds.xsd.doctor import Import, ImportDoctor

# The service URL
soap_url = 'https://soapbeta.streamflow.ca/ipl/soap'

# wsdl_url = 'http://myapp.example.notreal/path/to/soap?wsdl' 

import os
import base64

cwd = os.getcwd()
wsdl_url = 'file://%s/soap.wsdl' % cwd

imp = Import('http://schemas.xmlsoap.org/soap/encoding/', location='http://schemas.xmlsoap.org/soap/encoding/')
imp.filter.add('https://soapbeta.streamflow.ca/ipl/soap')

username = "ipl"
password = "xg8229jf"
base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
authenticationHeader = {
    "SOAPAction" : "ActionName",
    "Authorization" : "Basic %s" % base64string
}

client = Client(url=wsdl_url, location=soap_url,plugins=[ImportDoctor(imp)],headers=authenticationHeader)
print client

print client.wsdl.services[0].ports[0].methods.values()
# print client.service.getPartModels(partNumber=341241)