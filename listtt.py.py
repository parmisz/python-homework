



list=[]
list_menu=input("1.sakht account 2.login:")

while True:
    match list_menu:
        case"1":
            username=input("esm vared kon:")
            password=int(input("pass vared kon:"))
            list.append(username)
            list.append(password)
            break
        case"2":
            karbari=input("name karbari:")
            ramz=int(input("ramz vared kon:"))
            if karbari=="admin" and ramz=="123":
                print("okye vared sho")
            else:
                print("gheyre mojaz")

            name=input("esm vared kon")
            nomre_riazi=float(input("nomre riazi vared kon":))
            list.append(username)
            list.append( nomre_riazi)
            break
