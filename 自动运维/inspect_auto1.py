# #coding = utf-8
import re
a =  ['主机名:hadoop-master11|', '内存:77%|', 'CPU使用率:2.52%|', '存储:3%|', 'hadoop进程正常(巡检关键字:hadoop)|',
'主机名:hadoop-master12|' ,'内存:58%|', 'CPU使用率:10.86%|', '存储:3%|', 'hadoop进程正常(巡检关键字:hadoop)|']
for i in a :
    pattern = r"主机名"
    m = re.search(pattern, i)
    if m != None:
        with open('test.txt','a') as f:
            f.write('\n'+i)
    with open('test.txt', 'a') as f:
        f.write(i)

# result_list_info=[]
# back_info = 'hadoop-salver5'
# result_list_info.append("主机名:" + back_info + "| ")
# print(result_list_info)

# fond_kwords_hadoop = re.compile(r"hadoop")
# fond_kwords = fond_kwords_hadoop.search('hadoop-slaver501')
# fond_kwords.group()