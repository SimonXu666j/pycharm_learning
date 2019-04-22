#!/usr/bin/env python
# -*-coding:utf-8-*-
__author__ = 'simon'
__date__ = '2019/4/22 10:10'
import xml.etree.ElementTree as ET

# tree = ET.parse("testxml.xml")
# root = tree.getroot()
# print(root.tag)

# 遍历xml文档
# for child in root:
#     print('--------',child.tag, child.attrib)
#     for i in child:
#         print(i.tag)
#         for j in i:
#             print(j.tag,j.text)
#
# # 只遍历name节点
# for node in root.iter("name"):
#     print(node.tag, node.text)

# 修改和删除xml文档内容

# for node in root.iter('age'):
#     new_age=int(node.text)+1
#     node.text=str(new_age)
#     node.set("updated","yes")
#
# tree.write("testxml.xml")

# 删除node
# tree = ET.parse("xmltest")
# root = tree.getroot()
# for student in root.findall('student'):
#     # print(student)
#     age = int(student.find('age').text)
#     if age > 30:
#         root.remove(student)
# tree.write('output.xml')

# 自动创建xml文档
root = ET.Element("namelist")  # root
name = ET.SubElement(root, "name", attrib={"enrolled": "yes"})
age = ET.SubElement(name, "age", attrib={"checked": "no"})
sex = ET.SubElement(name, "sex")
n = ET.SubElement(name, "name")
n.text = "Alex Li"
sex.text = 'male'

name2 = ET.SubElement(root, "name", attrib={"enrolled": "no"})
age = ET.SubElement(name2, "age")
age.text = '19'

et = ET.ElementTree(root)  # 生成文档对象

et.write("build_out.xml", encoding="utf-8", xml_declaration=True)
