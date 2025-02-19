import xml.etree.ElementTree as et

tree = et.parse(r"to_edit.xml")
root = tree.getroot()

for e in root.iter("Name"):
    print(e.text)

for stu in root.iter("Student"):
    name = stu.find('Name')

    if name !=None:
        name.set('test', name.text *2)

stu = root.find('Student') #查找元素
#生成一个新的元素
e = et.Element('Adder')#生成一个标签对象
e.attrib= {"a":"b"} # 添加属性
e.text = '我加的' #标签内容

stu.append(e)
# 要把修改后的内容写回文件
tree.write('to_edit.xml')