with open('file_log.txt', 'r', encoding='utf-8') as f:
    for i in f:
        s = i.split()
        #print(s)
        data = s[0]
        with open(data+'.log', 'a', encoding='utf-8') as ff:
            ff.write(i)
            ff.flush()