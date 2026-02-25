def monkeys():
    s=""
    for i in range(5,0,-1):
        n=["Five","Four","Three","Two","One"][5-i]
        s+=f"{n} little monkey{'s'*(i>1)} jumping on the bed,\n{'He'if i==1 else'One'} fell off and bumped his head.\nMother called the doctor and the doctor said:\n{'No more monkeys jumping on the bed!'if i>1 else'Put those monkeys right to bed!'}"
        if i>1:s+="\n"*2
    return s