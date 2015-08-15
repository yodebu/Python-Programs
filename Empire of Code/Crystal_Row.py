#Crystal Row

def check_line(line):
    for i in range(1,len(line)):
        print(line[i]+' and '+line[i-1])
        if line[i] == line[i-1] :
            return False;
    return True
