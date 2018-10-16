import xmltodict

def processXML(filename):
    with open(filename) as myXMLFile:
        filestring = myXMLFile.read()
        xmldictionary = xmltodict.parse(filestring)
        return xmldictionary

artikeldict = processXML('producten.xml')
artikelen = artikeldict['artikelen']['artikel']

for artikel in artikelen:
    if artikel['nummer'] is not None:
        print(artikel['nummer'])
