



#mojodi = 10000000
mojodi= int(input("mojodi khod r vared konnid:"))
mablagh= int(input("mablagh:"))
if mablagh>0:
    print ("welcome")
if mablagh <=0 :
    print("mablagh mojaz nist.")
if mablagh> mojodi:
    print("adam mojodi")
else:
    mojodi_jadid=abs(mojodi - mablagh)
    if mablagh<0:
        mojodi_jadid=mojodi
        print("mojodi jadid:", mojodi_jadid)
