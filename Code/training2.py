import xml.etree.ElementTree as ET
import numpy as np

tree = ET.parse('2012-11-20_10_09_40.xml')
root = tree.getroot()

x = []
for space in root.findall('space'):
    for rotatedRect in space.find('rotatedRect'):
        c = rotatedRect.find('center').attrib
        s = rotatedRect.find('size').attrib
        a = rotatedRect.find('angle').attrib
        x = c['x']
        y = c['y']
        w = s['w']
        h = s['h']
        d = a['d']
    for contour in space.find('contour'):
        for point in contour.iter('point'):
            x.append(point.attrib)




