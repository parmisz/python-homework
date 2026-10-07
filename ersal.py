


ersal=input("ersal normal or fast")
hazine = int (input("hazine ra vard konid:"))

if ersal=="normal":
    if hazine >200000:
        print ("hazine:",hazine)
        print("ersale free")
    else:
        hazine+=50000
        print("hazine:",hazine)
elif ersal=="fast":
    hazine =+1000000
    print("hazine:",hazine)
else :print("ersale eshtebah")