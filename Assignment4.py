import os,sys
current_dir_path=os.getcwd()
p1def=[]
p1off=[]
p2def=[]
p2off=[]
error=[]
output=[]
def defread(x,y):
    for i in range(len(x)):
        if x[i][0]==";":
            y.append("-")
        for j in range(len(x[i])):
            if j+1<len(x[i]) and x[i][j]==";" and x[i][j+1]==";":
                y.append("-")
            if x[i][j]=="C":
                y.append(x[i][j])
            if x[i][j]=="B":
                y.append(x[i][j])
            if x[i][j]=="D":
                y.append(x[i][j])
            if x[i][j]=="S":
                y.append(x[i][j])
            if x[i][j]=="P":
                y.append(x[i][j])
        if x[i][-1]==";":
            y.append("-")
def fread():
    global p1off
    global p2off
    if len(sys.argv)!=5:
        raise IndexError(output.append("IndexError: amount of input file is less than expected.\n"))
    try:
        liststep=[]
        x=sys.argv[1]
        reading_file_name=x
        reading_file_path=os.path.join(current_dir_path,reading_file_name)
        with open(reading_file_path,"r") as i:
            count = 0
            while True:
                count += 1
                line = i.readline()
                if not line:
                    break
                liststep+=line.splitlines()
            i.close()
        defread(liststep,p1def)
    except IOError:
        output.append("IOError: input file {} is not reachable.\n".format(x))
    try:
        liststep=[]
        y=sys.argv[2]
        reading_file_name=y
        reading_file_path=os.path.join(current_dir_path,reading_file_name)
        with open(reading_file_path,"r") as i:
            count = 0
            while True:
                count += 1
                line = i.readline()
                if not line:
                    break
                liststep+=line.splitlines()
            i.close()   
        defread(liststep,p2def)
    except IOError:
        output.append("IOError: input file {} is not reachable.\n".format(y))
    try:
        z=sys.argv[3]
        reading_file_name=z
        reading_file_path=os.path.join(current_dir_path,reading_file_name)
        with open(reading_file_path,"r") as i:
            stepstr=""
            line=i.read()
            step=line.split("\n")
            for str in step:
                stepstr+=str
            p1off+=stepstr.split(";")
            p1off.pop()
            #pop() is to remove each '' list element caused by semicolons in the end of the files.
            i.close()
    except IOError:
        output.append("IOError: input file {} is not reachable.\n.".format(z))
    try:
        t=sys.argv[4]
        reading_file_name=t
        reading_file_path=os.path.join(current_dir_path,reading_file_name)
        with open(reading_file_path,"r") as i:
            stepstr=""
            line=i.read()
            step=line.split("\n")
            for str in step:
                stepstr+=str
            p2off+=stepstr.split(";")
            p2off.pop()
            i.close()
    except IOError:
        output.append("IOError: input file {} is not reachable.\n.".format(t))
p1play=[]
p2play=[]
def generate():
    for i in range(10):
        for j in range(10):
            p1play.append("-")
            p2play.append("-")
def board(y,x):
        strboard=""
        for j in range(10):
            if j+1==10:
                strboard+="{}".format(j+1)
            else:
                strboard+="{} ".format(j+1)
            for i in range(j*10,(j+1)*10):
                strboard+=y[i]
                strboard+=" "
            strboard+="\t"
            if j+1==10:
                strboard+="{}".format(j+1)
            else:
                strboard+="{} ".format(j+1)
            for i in range(j*10,(j+1)*10):
                strboard+=x[i]
                strboard+=" "
            strboard+="\n"
        return strboard
def play():
    p1win=False
    p2win=False
    print("Battle of Ships Game\n")
    output.append("Battle of Ships Game\n")
    p1cstats="Carrier\t\t_"
    p1bstats="Battleship\t_ _"
    p1dstats="Destroyer\t_"
    p1sstats="Submarine\t_"
    p1pstats="Patrol Boat\t_ _ _ _"
    p2cstats="Carrier\t\t_"
    p2bstats="Battleship\t_ _"
    p2dstats="Destroyer\t_"
    p2sstats="Submarine\t_"
    p2pstats="Patrol Boat\t_ _ _ _"
    for z in range(len(p1off)):
        print("\nPlayer1's Move\n\n")
        print("Round : {}\t\t Grid Size: 10x10\n\n".format(z+1))
        print("Player1's Hidden Board\tPlayer2's Hidden Board\n")
        print("  A B C D E F G H I J\t  A B C D E F G H I J\n")
        output.append("\nPlayer1's Move\n\n")
        output.append("Round : {}\t\t Grid Size: 10x10\n\n".format(z+1))
        output.append("Player1's Hidden Board\tPlayer2's Hidden Board\n")
        output.append("  A B C D E F G H I J\t  A B C D E F G H I J\n")
        stepp1=p1off[z].split(",")
        try:
            stepp1num=int(stepp1[0])
            assert stepp1num<11
        except ValueError:
            print("ValueError: Non-integer item used as integer in Player1.in file.\n")
        try:
            stepp1alp=stepp1[1]
            len(stepp1alp)==1
            assert ord(stepp1alp)<75
            #75 is ascii value for 'K'
        except ValueError:
            print("ValueError: Invalid item used as character detected in Player1.in file.\n")
        if p2def[(stepp1num-1)*10+(ord(stepp1alp)-65)]=="-":
            #65 is ascii value for 'A'
            p1play.pop(10*(stepp1num-1)+(ord(stepp1alp)-65))
            p1play.insert(10*(stepp1num-1)+(ord(stepp1alp)-65),"O")
            p2def.pop(10*(stepp1num-1)+(ord(stepp1alp)-65))
            p2def.insert(10*(stepp1num-1)+(ord(stepp1alp)-65),"O")            
        else:
            p1play.pop(10*(stepp1num-1)+(ord(stepp1alp)-65))               
            p1play.insert(10*(stepp1num-1)+(ord(stepp1alp)-65),"X")
            p2def.pop(10*(stepp1num-1)+(ord(stepp1alp)-65))
            p2def.insert(10*(stepp1num-1)+(ord(stepp1alp)-65),"X")
        strboard=board(p2play,p1play)
        output.append("{}".format(strboard))
        print(strboard)
        strp2def=""
        for i in p2def:
            strp2def+=i
        if strp2def.find("C")==-1:
            p2cstats=p2cstats.replace("_","X")
        if strp2def.find("D")==-1:
            p2dstats=p2dstats.replace("_","X")
        if strp2def.find("S")==-1:
            p2sstats=p2sstats.replace("_","X")
        if strp2def.find("B")==-1:
            p2bstats=p2bstats.replace("_","X")
        if strp2def.find("P")==-1:
            p2pstats=p2pstats.replace("_","X")        
        output.append("{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n".format(p1cstats,p2cstats,p1bstats,p2bstats,p1dstats,p2dstats,p1sstats,p2sstats,p1pstats,p2pstats))
        print("{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n".format(p1cstats,p2cstats,p1bstats,p2bstats,p1dstats,p2dstats,p1sstats,p2sstats,p1pstats,p2pstats))
        output.append("\nEnter your move: {}\n".format(p1off[z]))
        print("\nEnter your move: {}\n".format(p1off[z]))
        if strp2def.find("C")==-1 and strp2def.find("B")==-1 and strp2def.find("D")==-1 and strp2def.find("S")==-1 and strp2def.find("P")==-1:
            p1win=True
        output.append("\nPlayer2's Move\n\n")
        output.append("Round : {}\t\t Grid Size: 10x10\n\n".format(z+1))
        output.append("Player1's Hidden Board\tPlayer2's Hidden Board\n")
        output.append("  A B C D E F G H I J\t  A B C D E F G H I J\n")
        print("\nPlayer2's Move\n\n")
        print("Round : {}\t\t Grid Size: 10x10\n\n".format(z+1))
        print("Player1's Hidden Board\tPlayer2's Hidden Board\n")
        print("  A B C D E F G H I J\t  A B C D E F G H I J\n")
        stepp2=p2off[z].split(",")
        try:
            stepp2num=int(stepp2[0])
            assert stepp2num<11
        except ValueError:
            print("ValueError: Non-integer item used as integer in Player2.in file.\n")
        try:
            stepp2alp=stepp2[1]
            len(stepp2alp)==1
            assert ord(stepp2alp)<75
        except ValueError:
            print("ValueError: Invalid item used as character detected in Player2.in file.\n")
        if p1def[(stepp2num-1)*10+(ord(stepp2alp)-65)]=="-":
            p2play.pop(10*(stepp2num-1)+(ord(stepp2alp)-65))
            p2play.insert(10*(stepp2num-1)+(ord(stepp2alp)-65),"O")
            p1def.pop(10*(stepp2num-1)+(ord(stepp2alp)-65))
            p1def.insert(10*(stepp2num-1)+(ord(stepp2alp)-65),"O")
        else:
            p2play.pop(10*(stepp2num-1)+(ord(stepp2alp)-65))               
            p2play.insert(10*(stepp2num-1)+(ord(stepp2alp)-65),"X")
            p1def.pop(10*(stepp2num-1)+(ord(stepp2alp)-65))
            p1def.insert(10*(stepp2num-1)+(ord(stepp2alp)-65),"X")
        strboard=board(p2play,p1play)
        output.append("{}".format(strboard))
        print(strboard)
        strp1def=""
        for i in p1def:
            strp1def+=i
        if strp1def.find("C")==-1:
            p1cstats=p1cstats.replace("_","X")
        if strp1def.find("D")==-1:
            p1dstats=p1dstats.replace("_","X")
        if strp1def.find("S")==-1:
            p1sstats=p1sstats.replace("_","X")
        if strp1def.find("B")==-1:
            p1bstats=p1bstats.replace("_","X")
        if strp1def.find("P")==-1:
            p1pstats=p1pstats.replace("_","X")
        output.append("{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n".format(p1cstats,p2cstats,p1bstats,p2bstats,p1dstats,p2dstats,p1sstats,p2sstats,p1pstats,p2pstats))
        print("{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n".format(p1cstats,p2cstats,p1bstats,p2bstats,p1dstats,p2dstats,p1sstats,p2sstats,p1pstats,p2pstats))
        output.append("\nEnter your move: {}\n".format(p2off[z]))
        print("\nEnter your move: {}\n".format(p2off[z]))
        if strp1def.find("C")==-1 and strp1def.find("B")==-1 and strp1def.find("D")==-1 and strp1def.find("S")==-1 and strp1def.find("P")==-1:
            p2win=True
        if p1win==True or p2win==True:
            break
    if p1win==True and p2win==False:
        output.append("Player1 Wins!\n\n")
        print("Player1 Wins!\n\n")
    if p1win==True and p2win==True:
        output.append("It is a Draw!\n\n")
        print("It is a Draw!\n\n")
    if p1win==False and p2win==True:
        output.append("Player2 Wins!\n\n")
        print("Player2 Wins!\n\n")
    output.append("Final Information\n\n")
    output.append("Player1's Board\t\tPlayer2's Board\n")
    output.append("  A B C D E F G H I J\t  A B C D E F G H I J\n")
    print("Final Information\n\n")
    print("Player1's Board\t\tPlayer2's Board\n")
    print("  A B C D E F G H I J\t  A B C D E F G H I J\n")
    strboard=board(p1def,p2def)
    output.append("{}".format(strboard))
    print(strboard)
    output.append("{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n".format(p1cstats,p2cstats,p1bstats,p2bstats,p1dstats,p2dstats,p1sstats,p2sstats,p1pstats,p2pstats))
    print("{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n{}\t{}\n".format(p1cstats,p2cstats,p1bstats,p2bstats,p1dstats,p2dstats,p1sstats,p2sstats,p1pstats,p2pstats))
def fwrite():
    writing_file_name = "Battleship.out"
    writing_file_path = os.path.join(current_dir_path, writing_file_name)
    with open(writing_file_path,"w") as o:
        stroutput=""
        for x in output:
            stroutput += x
        o.write(stroutput)
    o.close()
try:
    fread()
    generate()
    play()
    fwrite()
except Exception as e:
    output.append("kaBOOM: run for your life!\n")
