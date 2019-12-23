
import turtle
import datetime
import time
import tkinter
import math

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
        self.marker.pendown()
        self.marker.goto(0,300)
        self.marker.circle(300)
        self.marker.goto(0,150)
        self.marker.circle(150)

        self.marker.up()
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
            self.marker.fd(20)
            self.marker.goto(0,0)
            self.marker.rt(360.0/7.0)
    def put_hand(self):
        day = datetime.datetime.today().weekday()
        hour = datetime.datetime.today().hour
        print(day)
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
        event = ' '
        eventday = 0
        angle = (eventday)*(360.0/7.0)
        i = 5
        while event is not '':
            event = file.readline().rstrip()
            if event is not '':
                for i in range(7):
                    b4=tkinter.Button(self.clockscreen,text=i, width=10)
                    b4.place(x=350+(math.cos((i)*(360.0/7.0))*200),y=350-(math.sin((i)*(360.0/7.0))*200))#,sticky='nsew')
                    
    def loop(self):
        self.clockscreen.mainloop()
    

