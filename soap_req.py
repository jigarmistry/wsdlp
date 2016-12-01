import os
import base64
from suds.client import Client
from suds.xsd.doctor import Import, ImportDoctor

soap_url = 'https://soapbeta.streamflow.ca/ipl/soap'

cwd = os.getcwd()
wsdl_url = 'file://%s/soapfinal.wsdl' % cwd

imp = Import('http://schemas.xmlsoap.org/soap/encoding/', location='http://schemas.xmlsoap.org/soap/encoding/')
imp.filter.add('http://xml.apache.org/xml-soap')

username = "ipl"
password = "xg8229jf"
base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')

authenticationHeader = {
    "SOAPAction" : "ActionName",
    "Authorization" : "Basic %s" % base64string
}

client = Client(url=wsdl_url, location=soap_url, plugins=[ImportDoctor(imp)], headers=authenticationHeader)

# Get Part Models
a = client.factory.create("ns2:Map")
a.item.key = "partNumber"
a.item.value = "341241"
print client.service.getPartModels(a)

# Get Model Sections
b = client.factory.create("ns2:Map")
b.item.key = "modelId"
b.item.value = "87048"
print client.service.getModelSections(b)

# Search Models
c = client.factory.create("ns2:Map")
c.item.key = "modelNumber"
c.item.value = "mav600"
print client.service.searchModels(c)

# Get Model Sections Parts
d = client.factory.create("ns2:Item")
d.key = "modelId"
d.value = "87048"

e = client.factory.create("ns2:Item")
e.key = "sectionId"
e.value = "525454"

f = client.factory.create("ns2:Map")
f.item = [d,e]
print client.service.getModelSectionsParts(f)

# Model Search Parts
g = client.factory.create("ns2:Item")
g.key = "keyword"
g.value = "motor"

h = client.factory.create("ns2:Map")
h.item = [d,g]

print client.service.modelSearchParts(h)


