import xml.dom.minidom as xm

doc = xm.Document() #在内存中创建一个文档
root = doc.createElement('Managers') #根节点Managers对象
root.setAttribute('company','xx科技') #root节点属性
root.setAttribute('address','科技园区')

doc.appendChild(root) #添加根节点到文档对象当中

manager_list = [{'name':'joy','age':27,"sex":"女"},
                {'name':'joy','age':27,"sex":"女"},
                {'name':'joy','age':27,"sex":"女"},
                ]
for i in manager_list:
    nodeManager = doc.createElement("Manager")
    nodeName = doc.createElement('name')
    #给叶子节点name设置一个文本节点，用于显示文本内容
    nodeName.appendChild(doc.createTextNode(str(i['name'])))

    nodeAge = doc.createElement("age")
    nodeAge.appendChild(doc.createTextNode(str(i["age"])))

    nodeSex = doc.createElement("sex")
    nodeSex.appendChild(doc.createTextNode(str(i["sex"])))
    # 将各叶子节点添加到父节点Manager中，
    # 最后将Manager添加到根节点Managers中
    nodeManager.appendChild(nodeName)
    nodeManager.appendChild(nodeAge)
    nodeManager.appendChild(nodeSex)
    root.appendChild(nodeManager)

fp = open("Manager.xml","w")
doc.writexml(fp, indent="\t",addindent="\t",newl="\n",encoding="utf-8")