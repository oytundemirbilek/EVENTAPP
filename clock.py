
import turtle
import datetime
import time
import tkinter
import math
import csv
import scheduler as sc

class WeeklyClock:
    def __init__(self):
        self.clockscreen = tkinter.Tk()
        self.marker= None

    def adjust_screen(self):
        
        canvas = tkinter.Canvas(master = self.clockscreen, width = 700, height = 700, bg='light cyan')
        canvas.grid(padx=2, pady=2, row=0, column=0, rowspan=10, columnspan=10) # , sticky='nsew')
        self.marker= turtle.RawTurtle(canvas)

        #self.clockscreen.configure(bg="light cyan")
        self.clockscreen.title("Weekly Analog Clock")
        #self.clockscreen.tracer(0)

    def adjust_pen(self):
        self.marker.hideturtle()
        self.marker.speed(0)
        self.marker.pensize(3) #line thickness

    def create_clock(self):
        # OUTER CIRCLE
        self.marker.up()

        self.marker.setheading(180)
        self.marker.color("black")
        
        self.marker.goto(0,300)
        self.marker.pendown()
        self.marker.circle(300)

        self.marker.goto(0,150)
        self.marker.circle(150)

        self.marker.penup()
        self.marker.goto(0,0)
        self.marker.setheading(90)
        # 7 = Monday
        daylist = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        for days in daylist:
            
            self.marker.fd(100)
            self.marker.write(days, align='Center', font=('Arial', 12, 'bold'))
            self.marker.fd(40)
            self.marker.pendown()
            self.marker.fd(200)
            self.marker.penup()
            self.marker.goto(0,0)
            self.marker.rt(360.0/7.0)
    def put_hand(self):
        day = datetime.datetime.today().weekday()
        hour = datetime.datetime.today().hour
        print(datetime.datetime.today())
        # DAY HAND
        self.marker.penup()
        self.marker.goto(0,0)
        self.marker.color("navy")
        self.marker.setheading(90)
        angle = (day/7)*360
        angle = angle + (hour/(24*7))*360
        self.marker.rt(angle)
        
        self.marker.pendown()
        self.marker.shape('arrow')
        self.marker.pensize(6)
        self.marker.fd(100)

    def show_events(self):
        file = open("events.txt", "r")
        events = csv.reader(file)
        for event in events:
            eventdate = datetime.datetime.strptime(event[1], '%Y-%m-%d')
            eventday = eventdate.weekday()
            angle = (2*eventday)*(math.pi/7.0)+0.4
        
            b4=tkinter.Button(self.clockscreen,text=event[0], width=10)
            b4.place(x=350+(math.sin(angle)*230),y=350-(math.cos(angle)*230))
                
    def options(self):
        eventname=tkinter.StringVar()
        e1=tkinter.Entry(self.clockscreen,textvariable=eventname)
        e1.place(x=600,y=575)

        eventdate=tkinter.StringVar()
        e2=tkinter.Entry(self.clockscreen,textvariable=eventdate)
        e2.place(x=600,y=550)


        print(eventname)
        b1=tkinter.Button(self.clockscreen,text="CREATE EVENT", width=15,)#command=EventCreate
        b1.place(x=600,y=600)
        b2=tkinter.Button(self.clockscreen,text="CANCEL EVENT", width=15,)#command=EventCancel
        b2.place(x=600,y=625)


        b3=tkinter.Button(self.clockscreen,text="SETTINGS", width=15)
        b3.place(x=0,y=625)
        b4=tkinter.Button(self.clockscreen,text="LOGIN", width=15)
        b4.place(x=0,y=0)

    def loop(self):
        self.clockscreen.mainloop()
    
#def EventCreate(self):
#		eventName = e1.get()
#		eventDate = e2.get()
#		Actions.CreateEvent(eventName + eventDate)
#
#def EventCancel(self):
#	eventName = e1.get()
#	Actions.DeleteEvent(eventName)
#