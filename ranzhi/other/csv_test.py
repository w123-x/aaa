# import csv
# with open(r'D:\workspace\selenium\ranzhi\sample.csv','r',encoding='utf-8') as f:
#     info=f.read()
#     newinfo=list(info.split('\n')[1:])
#     b=[]
#     for i in newinfo:
#         a=[]
#         i1=i.split(',')
#         a=tuple(i1)
#         b.append(a)
#     print(b)


# import csv
# with open(r'D:\workspace\selenium\ranzhi\sample.csv','r',encoding='utf-8') as f:
#     reader=csv.reader(f)
#     for row in reader:
#         print(row)
#         a=[]
#         a.append(row)
#         print(a)
#         a=tuple(a)
#         print(a)







    # r=[tuple(e.strip() for e in line.split(',')) for line in lines]
    # print(r)
# s=('a','b','c')
# s.split(',')
# print(s)

with open(r'D:\workspace\selenium\ranzhi\data\sample.csv','r',encoding='utf-8') as file:
    lines=file.readlines()
    r=[tuple(e.strip() for e in line.split(',')) for line in lines]
    print(r)



