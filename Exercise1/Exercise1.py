#import BeautifulSoup Python library
from bs4 import BeautifulSoup
from datetime import date

# importing datetime module for now()
import datetime


import xml.etree.ElementTree as ET
filename = "test_payload1.xml"
xmlTree = ET.parse(filename)


def update_depart_return_inxml(x, y):
    currentdate = date.today()
    departdate = currentdate + datetime.timedelta(days=x)
    returndate = currentdate + datetime.timedelta(days=y)

    #Update XML in xmlTree
    rootElement = xmlTree.getroot()

    for dep in rootElement.iter('DEPART'):
        # updates the DEPART value
        dep.text = str(departdate.strftime('%Y%m%d'))

    for ret in rootElement.iter('RETURN'):
        # updates the RETURN value
        ret.text = str(returndate.strftime('%Y%m%d'))

    # Write the modified xml file.
    xmlTree.write(filename, encoding='UTF-8', xml_declaration=True)

    # Create a new file with updated data.
    xmlTree.write('test_payload_new.xml')


#Method calling with two INT values.
update_depart_return_inxml(2, 3);
