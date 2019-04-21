import xml.etree.ElementTree

root = xml.etree.ElementTree.parse("student.xml")
print("利用getiterator访问：")
nodes = root.getiterator() # 得到每个分类节点的可迭代集合

for node in nodes:
    print("{}--{}".format(node.tag,node.text))

print("利用find和findall方法：")
ele_teacher = root.find("Teacher")
print(type(ele_teacher))
print("{}--{}".format(ele_teacher.tag, ele_teacher.text))
print("Q"*30)
ele_stus = root.findall("Student")
print(type(ele_stus))

for ele in ele_stus:
    print("{}--{}".format(ele.tag, ele.text))
    for sub in ele.getiterator():
        if sub.tag == 'Name':
            if "Other" in sub.attrib.keys():
                print(sub.attrib["Other"])
