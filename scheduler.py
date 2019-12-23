def CreateEvent (name, date):
    f = open("events.txt", "a+")
    f.write(name + "," + date +"\n")
    f.close()
    return "Event created!"

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

		
