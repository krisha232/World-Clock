from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
import pytz
import time

root=Tk()
root.geometry("600x900")
india_image=ImageTk.PhotoImage(Image.open("India.jpg"))
USA_image=ImageTk.PhotoImage(Image.open("USA.jpg"))
australia_image=ImageTk.PhotoImage(Image.open("Australia.jpg"))
japan_image=ImageTk.PhotoImage(Image.open("Japan.jpg"))
#___________INDIA________________________
heading=Label(root,text="India")
heading.place(relx=0.25,rely=0.02,anchor=CENTER)
    
india_map=Label(root)
india_map["image"]=india_image
india_map.place(relx=0.25,rely=0.21,anchor=CENTER)

india_time=Label(root)
india_time.place(relx=0.25,rely=0.4,anchor=CENTER)

#___________USA_________________________

heading2=Label(root,text="USA")
heading2.place(relx=0.75,rely=0.02,anchor=CENTER)
    
usa_map=Label(root)
usa_map["image"]=USA_image
usa_map.place(relx=0.75,rely=0.21,anchor=CENTER)

usa_time=Label(root)
usa_time.place(relx=0.75,rely=0.4,anchor=CENTER)


#___________AUSTRALIA________________________
heading3=Label(root,text="Australia")
heading3.place(relx=0.25,rely=0.5,anchor=CENTER)
    
australia_map=Label(root)
australia_map["image"]=australia_image
australia_map.place(relx=0.25,rely=0.69,anchor=CENTER)

australia_time=Label(root)
australia_time.place(relx=0.25,rely=0.88,anchor=CENTER)

#___________JAPAN_________________________

heading4=Label(root,text="Japan")
heading4.place(relx=0.75,rely=0.5,anchor=CENTER)
    
japan_map=Label(root)
japan_map["image"]=japan_image
japan_map.place(relx=0.75,rely=0.69,anchor=CENTER)

japan_time=Label(root)
japan_time.place(relx=0.75,rely=0.88,anchor=CENTER)


class India():
    def times(self):
        home=pytz.timezone('Asia/Kolkata')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        india_time["text"]="Time : "+current_time
        india_time.after(200,self.times)
        
class USA():
    def times(self):
        home=pytz.timezone('US/Central')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        usa_time["text"]="Time : "+current_time
        usa_time.after(200,self.times)
        
class Australia():
    def times(self):
        home=pytz.timezone('Australia/ACT')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        australia_time["text"]="Time : "+current_time
        australia_time.after(200,self.times)
        
class Japan():
    def times(self):
        home=pytz.timezone('Japan')
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        japan_time["text"]="Time : "+current_time
        japan_time.after(200,self.times)
        
obj_india=India()
obj_USA=USA()
obj_australia=Australia()
obj_japan=Japan()
india=Button(root,text="Show Time",command=obj_india.times)
india.place(relx=0.25,rely=0.44,anchor=CENTER)

usa=Button(root,text="Show Time",command=obj_USA.times)
usa.place(relx=0.75,rely=0.44,anchor=CENTER)

japan=Button(root,text="Show Time",command=obj_japan.times)
japan.place(relx=0.75,rely=0.92,anchor=CENTER)

Australia=Button(root,text="Show Time",command=obj_australia.times)
Australia.place(relx=0.25,rely=0.92,anchor=CENTER)

root.mainloop()