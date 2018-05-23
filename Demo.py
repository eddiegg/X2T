from zipfile import ZipFile
import re
from xml.etree import ElementTree as  ET
from xml.etree.ElementTree import Element

content={}
with ZipFile('/Users/eddie/Documents/Demo.xmind') as xmind:
    for f in xmind.namelist():
        if f == 'content.xml':
            content['content']= xmind.open(f).read().decode('utf-8')

xml_content = re.sub(r'\sxmlns="[^"]+"', '', content['content'], count=1)

root = ET.fromstring(xml_content.encode('utf-8'))

root_suite = root.find('sheet').find('topic')

def get_child_suite(node):
    try:
        child_suite = root_suite.find('children').find('topics').findall('topic')
    except:
        print('格式不正确')
    return child_suite

for child_node in get_child_suite(root_suite):
    try:
        if 'flag' in (child_node.find('marker-refs').find('marker-ref').get('marker-id')):
            print('node_suite')
        elif 'star' in (child_node.find('marker-refs').find('marker-ref').get('marker-id')):
            print('node')
    except:
        print('格式不正确，suite请加旗标，case请加星标')
