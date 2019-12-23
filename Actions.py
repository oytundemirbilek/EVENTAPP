def CreateEvent (event):
    f = open("events.txt", "a+")
    f.write("\n"+ event)
    f.close()

def ReadEvents():
    f = open("events.txt", "r")
    contents =f.read()
    print(contents)
    f.close()

def SearchEvent(eventName):
    f = open("events.txt", "r")
    f1 = f.readlines()
    for i in f1:
        if (i.__contains__(eventName)):
            print(i)   	

def DeleteEvent(eventName):
	newContent = []
	f = open("events.txt", "r+")
	f1 = f.readlines()
	for i in f1:
		if (not (i.__contains__(eventName))):
			newContent.append(i)
	f.close()
	f2 = open("events.txt","w")
	for x in newContent:
		f2.write(x)
	f.close()

	

def GetContatcts() :
	f = open("contacts.txt", "r")
	contents =f.read()
	print(contents)
	f.close()

def GetContact(contact):
	f = open("contacts.txt", "r")
	f1 = f.readlines()
	for i in f1:
		if (i.__contains__(contact)):
			print(i)  

		
DeleteEvent("event1")
input('Press ENTER to exit')
