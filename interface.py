from tkinter import *
import numpy
import time
import threading

def turn_on_off_lights(lights_switch):
    global lightson
    if lightson==True:
        lightson=False
        lights_switch.config(text="OFF")
        lights_switch.config(bg='RED')
        #send command to turn lights off
    else:
        lightson=True
        lights_switch.config(text="ON")
        lights_switch.config(bg="GREEN")
        #send command to turn lights on

def run_pump_1(pump1_switch,runtime,rate):
    if float(runtime)!=float(0) and float(rate)!=float(0):
        pump1_switch.config(state="disabled")
        pump1_switch.config(text="ON")
        pump1_switch.config(bg="GREEN")
        threading.Thread(target=run_pump_1_thread,args=(pump1_switch,runtime,rate)).start()

def run_pump_1_thread(pump1_switch,runtime,rate):
    #send command to turn on pump for desired time/Rate
    time.sleep(float(runtime))
    pump1_switch.config(state="normal")
    pump1_switch.config(text="OFF")
    pump1_switch.config(bg='RED')

window = Tk()

window.title("Container Monitor")

window.grid_rowconfigure([0,1,2,3,4,5,6,7], weight=1)
window.grid_columnconfigure([0,1,2,3], weight=1)

#pH Column
pH_read_title=Label(window, text="pH Reading") #Title Label for pH Reading
pH_read_title.grid(column=0,row=0, sticky='NSEW') #placing the label in the window
pH_read_value=StringVar() #Initialize a string variable for storing the value read from the pH sensor
pH_read_value.set("{:.2f}".format(7.0)) #Set the variable to 7.0 before reading sensor
pH_read_label=Label(window,textvariable=pH_read_value,fg='Red',font=('Arial',60)) #Reading Label to show the pH reading
pH_read_label.grid(column=0,row=1, sticky='NSEW') # place the label in the window
pH_set_title=Label(window, text="pH Set Point") #Title label for ph Set Point
pH_set_title.grid(column=0,row=3, sticky='NSEW') #Place the label on the window
pH_set_value=StringVar() #Initialize a string variable for the setpoint from user.
pH_set_value.set("{:.2f}".format(7.0)) #Default the setting to 7.0
pH_set_entry=Entry(window, textvariable=pH_set_value) #Create a text entry box for inputting the pH setpoint
pH_set_entry.grid(column=0,row=4, sticky='NSEW') #Place it in the window
pH_set_label=Label(window,text="7.00",fg='Red',font=('Arial',60)) #Create a label for the pH setpoint
pH_set_label.grid(column=0,row=5, sticky='NSEW') #place it in the window

#EC Column
ec_read_title=Label(window, text="EC Reading") #Title Label for pH Reading
ec_read_title.grid(column=1,row=0, sticky='NSEW') #placing the label in the window
ec_read_value=StringVar() #Initialize a string variable for storing the value read from the pH sensor
ec_read_value.set("{:.2f}".format(2.0)) #Set the variable to 2.0 before reading sensor
ec_read_label=Label(window,textvariable=ec_read_value,fg='Red',font=('Arial',60)) #Reading Label to show the pH reading
ec_read_label.grid(column=1,row=1, sticky='NSEW') # place the label in the window
ec_set_title=Label(window, text="EC Set Point") #Title label for ph Set Point
ec_set_title.grid(column=1,row=3, sticky='NSEW') #Place the label on the window
ec_set_value=StringVar() #Initialize a string variable for the setpoint from user.
ec_set_value.set("{:.2f}".format(2.0)) #Default the setting to 2.0
ec_set_entry=Entry(window, textvariable=ec_set_value) #Create a text entry box for inputting the pH setpoint
ec_set_entry.grid(column=1,row=4, sticky='NSEW') #Place it in the window
ec_set_label=Label(window,text="2.00",fg='Red',font=('Arial',60)) #Create a label for the pH setpoint
ec_set_label.grid(column=1,row=5, sticky='NSEW') #place it in the window

#RTD/Ambient Temp column
rtd_read_title=Label(window, text="RTD Reading") #Title Label for pH Reading
rtd_read_title.grid(column=2,row=0, sticky='NSEW') #placing the label in the window
rtd_read_value=StringVar() #Initialize a string variable for storing the value read from the pH sensor
rtd_read_value.set("{:.2f}".format(22.0)) #Set the variable to 2.0 before reading sensor
rtd_read_label=Label(window,textvariable=rtd_read_value,fg='Blue',font=('Arial',60)) #Reading Label to show the pH reading
rtd_read_label.grid(column=2,row=1, sticky='NSEW') # place the label in the window
ambt_read_title=Label(window, text="Ambient Temp Reading") #Title Label for pH Reading
ambt_read_title.grid(column=2,row=3,rowspan=2, sticky='NSEW') #placing the label in the window
ambt_read_value=StringVar() #Initialize a string variable for storing the value read from the pH sensor
ambt_read_value.set("{:.2f}".format(1.23)) #Set the variable to 2.0 before reading sensor
ambt_read_label=Label(window,textvariable=ambt_read_value,fg='Blue',font=('Arial',60)) #Reading Label to show the pH reading
ambt_read_label.grid(column=2,row=5, sticky='NSEW') # place the label in the window

#Humidity/CO2 column
ambh_read_title=Label(window, text="Ambient Humidity Reading") #Title Label for pH Reading
ambh_read_title.grid(column=3,row=0, sticky='NSEW') #placing the label in the window
ambh_read_value=StringVar() #Initialize a string variable for storing the value read from the pH sensor
ambh_read_value.set("{:.2f}".format(3.21)) #Set the variable to 2.0 before reading sensor
ambh_read_label=Label(window,textvariable=ambh_read_value,fg='Blue',font=('Arial',60)) #Reading Label to show the pH reading
ambh_read_label.grid(column=3,row=1, sticky='NSEW') # place the label in the window
co2_read_title=Label(window, text="CO2 Reading") #Title Label for pH Reading
co2_read_title.grid(column=3,row=3,rowspan=2, sticky='NSEW') #placing the label in the window
co2_read_value=StringVar() #Initialize a string variable for storing the value read from the pH sensor
co2_read_value.set("{:.2f}".format(1.23)) #Set the variable to 2.0 before reading sensor
co2_read_label=Label(window,textvariable=co2_read_value,fg='Blue',font=('Arial',60)) #Reading Label to show the pH reading
co2_read_label.grid(column=3,row=5, sticky='NSEW') # place the label in the window

#Light Control
lightson=False
lights_title=Label(window,text='Lights on/off') #title for lights on/off switch
lights_title.grid(column=0,columnspan=4,row=6)
lights_switch=Button(window,text="OFF",width=10,command=lambda: turn_on_off_lights(lights_switch),bg='RED')
lights_switch.grid(column=0,columnspan=4,row=7)

#Pump1 Control
pump1on=False
pump1_title=Label(window,text='Pump 1 Control: ') #title for lights on/off switch
pump1_title.grid(column=0,row=8)
pump1_time_label=Label(window,text='Run Time (s)')
pump1_time_label.grid(column=1,row=8)
pump1_time_var=StringVar()
pump1_time_var.set(0.0)
pump1_time_entry=Entry(window, textvariable=pump1_time_var) #Create a text entry box for inputting the pH setpoint
pump1_time_entry.grid(column=2,row=8)
pump1_rate_label=Label(window,text='Rate (ml/s)')
pump1_rate_label.grid(column=3,row=8)
pump1_rate_var=StringVar()
pump1_rate_var.set(0.0)
pump1_rate_entry=Entry(window, textvariable=pump1_rate_var) #Create a text entry box for inputting the pH setpoint
pump1_rate_entry.grid(column=4,row=8)
pump1_switch=Button(window,text="OFF",width=10,command=lambda: run_pump_1(pump1_switch,pump1_time_var.get(),pump1_rate_var.get()),bg='RED')
pump1_switch.grid(column=5,row=8)

def update_readouts(): #this function reads the sensors and updates the text labels to reflect sensor readings
    global pH_read_value
    global ec_read_value
    temp_value = numpy.add(numpy.random.normal(loc=0,scale=.1),7.0) #get the current pH value from sensor
    pH_read_value.set("{:.2f}".format(temp_value)) #set the pH value to the StringVariable for the pH Read Label
    temp_value = numpy.add(numpy.random.normal(loc=0,scale=.1),2.0) #get the current EC value from sensor
    ec_read_value.set("{:.2f}".format(temp_value)) #set the pH value to the StringVariable for the pH Read Label
    temp_value = numpy.add(numpy.random.normal(loc=0,scale=.1),20.0) #get the current RTD value from sensor
    rtd_read_value.set("{:.2f}".format(temp_value)) #set the pH value to the StringVariable for the pH Read Label
    temp_value = numpy.add(numpy.random.normal(loc=0,scale=.1),20.0) #get the current Ambient Temp value from sensor
    ambt_read_value.set("{:.2f}".format(temp_value)) #set the pH value to the StringVariable for the pH Read Label
    temp_value = numpy.add(numpy.random.normal(loc=0,scale=.1),2.0) #get the current Ambient Humidity value from sensor
    ambh_read_value.set("{:.2f}".format(temp_value)) #set the pH value to the StringVariable for the pH Read Label
    temp_value = numpy.add(numpy.random.normal(loc=0,scale=.1),2.0) #get the current CO2 value from sensor
    co2_read_value.set("{:.2f}".format(temp_value)) #set the pH value to the StringVariable for the pH Read Label
    window.after(100,update_readouts) #reschedule to run again after 100 ms.

def fix_zeros(): #this function fixes the formatting of the user input, if the user inputs 6, this function will show 6.00.  If the user inputs blank, this will default the pH to 7.00
    try:
        pH_set_label.config(text="{:.2f}".format(float(pH_set_value.get())))
        ec_set_label.config(text="{:.2f}".format(float(ec_set_value.get())))
    except:
        pH_set_label.config(text="7.00")
        pH_set_value.set(7.00)
        ec_set_label.config(text="2.00")
        pH_set_value.set(2.00)
    window.after(10,fix_zeros)

window.after(100,update_readouts)
window.after(10,fix_zeros)
#window.after(1000,pump_control)
window.mainloop()
