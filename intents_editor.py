with open("type.txt", "w") as f:
    for i in range(1, 121):
        print(i)
        stri = str(i)
        if len(stri)==1:
            stri='00'+stri
        if len(stri)==2:
            stri='0'+stri
        f.write('{\n'+'\"name\": \"'+stri+'\"\n'+"},\n")
