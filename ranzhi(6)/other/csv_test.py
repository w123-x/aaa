with open(r'ranzhi\sample.csv','r',encoding='utf-8') as file:
    lines = file.readlines()
    r = [tuple(e.strip() for e in line.split(',')) for line in lines]
    print(r)