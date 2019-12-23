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

#def DeleteEvent(eventName):
#	f = open("events.txt", "r+")
#	f1 = f.readlines()
#	for i in f1:
#		if (i.__contains__(eventName)):
#			f.
#	f.close()

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

		
input('Press ENTER to exit')
