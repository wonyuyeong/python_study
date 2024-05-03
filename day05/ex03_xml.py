import xml.etree.ElementTree as ET

tree = ET.parse("day05/data/xml_data.xml")
root = tree.getroot()
print("tag", root.tag)
print("attrib",root.attrib)
print("text",root.text)
print("-" * 50)

for i in root :
    print(i.tag, i.attrib, i.text)
print("-" * 50)

data="""<?xml version="1.0"?>
    <data>
    <student>
        <name>peter</name>
        <age>24</age>
        <score math="80" english="97"/>
    </student>
    <student>
        <name>elgar</name>
        <age>21</age>
        <score math="67" english="56"/>
    </student>
    <student>
        <name>hong</name>
        <age>36</age>
        <score math="76" english="81"/>
    </student>
</data>
"""

# string을 xml 로 만들어서 파싱하기
root2 = ET.fromstring(data)
print(type(root2))

for i in (root.findall('student')):
    name = i.find("name").text
    age = i.find("age").text
    score = i.find("score").attrib
    
    print(name,"\t",age,"\t",score,"\t")
print("-" * 50 )

# 리스트
lis = []
for i in (root.findall('student')):
    name = i.find("name").text
    age = i.find("age").text
    score = i.find("score").attrib
    lis.append(name)
    lis.append(age)
    lis.append(score)
print(lis)
print("-" * 50 )

