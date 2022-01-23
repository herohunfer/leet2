def remove(s: str):
    pos = 0
    slow = 0
    if s == "":
        return ""
    slist = list(s)
    print(slist)
    while pos < len(slist):
        if slist[pos] == ' ' and (pos == 0 or slist[pos-1] == ' '):
            pos += 1
        else:
            slist[slow] = slist[pos]
            slow += 1
            pos += 1
        # print(f"slist={slist} slow={slow} pos={pos}")
    if s[-1] == ' ':
        return ''.join(slist[:slow-1])
    else:
        return ''.join(slist[:slow])

if __name__ == "__main__":
    print(f"remove 'abc_de_de__de__':[{remove('abc de de  de  ')}]")
    print(f"remove '___abc__de__':[{remove('   abc  de  ')}]")
