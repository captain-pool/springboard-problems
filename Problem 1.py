def balanced(l):
    stk = []
    op = []
    v = "N" 
    bracs = {"{":"}","(":")","[":"]"}
    for i in l:
        if i in bracs.keys():
            stk.append(i)
            op.append(i)
        elif i in bracs.values():
            op.append(i)
            if len(stk)>0:
                if i==bracs[stk[-1]]:
                    stk.pop()
            else:
                stk.append(i)
    if len(stk)==0:
        v = "Y" 
    return v+" "+"".join(op)
    
if __name__  == "__main__":
    inp = list(input())
    print(balanced(inp))

