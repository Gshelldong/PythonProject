import json

#student是一个字典
student={
    "name":"gong",
    "age":18,
    "mobile":"13048303441"
}
print(type(student))
print("0"*50)
stu_json = json.dumps(student)
print(type(stu_json))
print("JSON对象:{0}".format(stu_json))
print("1"*50)
stu_dict = json.loads(stu_json)
print(type(stu_dict))
print(stu_dict)