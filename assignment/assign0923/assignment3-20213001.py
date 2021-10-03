#박지민-20213001
import pickle

dbfilename = 'assignment3-20213001'

def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb =  pickle.load(fH)
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()


def doScoreDB(scdb):
    while(True):
        inputstr = (input("Score DB > "))
        if inputstr == "": continue
        parse = inputstr.split(" ")
        if parse[0] == 'add':
            try:
                record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
                scdb += [record]
            except IndexError:
                print(" name , age, Score 을 입력하세요")
                
        elif parse[0] == 'del':
            try :
                for i in scdb:              
                    if i['Name'] == parse[1] :
                        for j in scdb:    
	                        scdb.remove(i)
                
            except IndexError:
                print("name을 입력하세요") 
                    
        elif parse[0] == 'show':
            sortKey ='Name' if len(parse) == 1 else parse[1]
            showScoreDB(scdb, sortKey)
            
        elif parse[0] == 'quit':
            break
                      
        elif parse[0] == 'find':
            try :
                for i in scdb:
                    if i['Name'] == parse[1]:
                        print(i)
            except IndexError:
                print("name을 입력하세요")
                    
        elif parse[0] == 'inc':
            try :
                for i in scdb:
                    if i['Name'] == parse[1]:
                        i['Score'] = str(int(i['Score'])+ int(parse[2]))
            except IndexError:
                    print("name을 입력하세요")


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + p[attr], end=' ')
        print()


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
