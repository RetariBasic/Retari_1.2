from os.path import exists
import pickle
va = 0 #latest variable address
la = 0 #latest list address
cof = 0
listdata = None
while True:
    cod = input("> ")
    if cod[0:2] == "-$":
        if exists(f"variables\{cod[2:len(cod)]}.txt"):
            rvf = open(f"variables\{cod[2:len(cod)]}.txt", "r")
            print(rvf.read())
            rvf.close()
        else:
            print(f"the variable {cod[2:len(cod)]} does not exist")
    elif cod[0:2] == "-#":
        va = va + 1
        cvf = open(f"variables\{va}.txt", "w")
        cvf.write(cod[2:len(cod)])
        cvf.close()
        print(f"var {va} set to {cod[2:len(cod)]}")
    elif cod[0:1] == "!":
        print(cod[1:len(cod)])
    elif cod[0:2] == "@$":
        if exists(f"lists\{cod[2:len(cod)]}.ob"):
            with open (f"lists/{cod[2:len(cod)]}.ob", "rb") as rlf:
                print(pickle.load(rlf))
        else:
            print(f"the list {cod[2:len(cod)]} does not exist")
    elif cod[0:2] == "@#":
        la = la + 1
        listdata = cod[2:len(cod)].split(" ")
        with open(f"lists/{la}.ob", "wb") as clf:
            pickle.dump(listdata, clf)
        print(f"list {la} set to {listdata}")
    elif cod[0:3] == "@s|":
        if exists(f"lists\{cod[3:len(cod)]}.ob"):
            with open (f"lists/{cod[3:len(cod)]}.ob", "rb") as rlf:
                listdata = pickle.load(rlf)
                listslipwhat = input("slipwhat> ")  #what to insert
                listslipwhere = input("slipwhere> ")
                listdata.insert(int(listslipwhere), listslipwhat)
                with open(f"lists/{cod[3:len(cod)]}.ob", "wb") as clf:
                    pickle.dump(listdata, clf)
                print(f"appended {listslipwhat} to {cod[3:len(cod)]}")
        else:
            print(f"the list {cod[3:len(cod)]} does not exist")
    else:
        print("syntax error")
    
