import serial, time
from tkinter import *
arduino = False
readings_loop = False 
def port_disconnnect():
	global arduino
	global readings_loop
	readings_loop = False
	arduino.close()
	arduino = False
	connect_btn.config(text="Connect")
	connection_status.config(text="Status: Disconnected")
	error_list.insert(0, ' ')
	error_list.insert(1, 'Disconnected')
	error_list.insert(2, ' ')
	disconnect_btn.grid_forget()
	connect_btn.grid(columnspan=3,row=5, padx = 5, pady =5)
def port_connnect():
	global readings_loop
	global arduino
	readings_loop = True
	try:
		arduino = serial.Serial(port_location.get(), baud_location.get(), timeout=timeout_location.get())
	except:
		arduino = False
	if arduino == False:
		error_list.insert(0, " ")
		error_list.insert(1, "Error While connecting %s" % (port_location.get()))
		error_list.insert(2, "Baud : %d   Timeout : %d" % (baud_location.get(), timeout_location.get()))
		error_list.insert(3, " ")
		connect_btn.config(text="Connect")
		connection_status.config(text="Status: Disconnected")
	else:
		error_list.insert(0,' ')
		error_list.insert(1,'successfully Connected!')
		error_list.insert(2, "Baud : %d   Timeout : %d" % (baud_location.get(), timeout_location.get()))
		error_list.insert(3,' ')
		connect_btn.config(text="Disconnect")
		connection_status.config(text="Status: Connected")
		disconnect_btn.grid(columnspan=3,row=5, padx = 5, pady =5)
		connect_btn.grid_forget()
		
		while readings_loop:
			readings = arduino.readline().decode()
			if readings != '':
				error_list.insert(0, readings)
			root.update()
			
def send_data():
	arduino.write(b'%d' % serial_location.get())
root = Tk()
root.title('Arduino (Build By: Lemuel E. Diergos)')
root.geometry('795x650')

port_location = StringVar()
baud_location = IntVar()
timeout_location = IntVar()
serial_location = IntVar()

settings = Frame(root, padx = 10, pady=10, borderwidth=5, relief=SUNKEN)
body = Frame(root, padx = 10, pady=10)
status = Frame(root,borderwidth=3,relief=SUNKEN)

lbl_settings = Label(settings, text="Settings", font = ('arial Bold',10))
# ------------- PORT ------------
port_label = Label(settings, text="Port: ")
port = Entry(settings, textvariable=port_location)
port_location.set('COM4') 

#  --------------- PORT ------------
# ------------ BAUD ----------------
baud_label = Label(settings, text="Baud: ")
baud = OptionMenu(settings, baud_location, 300, 1200, 2400, 4800, 9600,19200,38400,57600,74880,115200,230400,250000,500000,1000000,2000000)
baud.config(width=14)
baud_location.set(9600) 
# ----------- BAUD -----------------
# ------- TIMEOUT ------------------
timeout_label = Label(settings, text="Timeout: ")
timeout = Entry(settings, textvariable=timeout_location)
timeout_location.set(0) 
# ------- TIMEOUT ------------------

connect_btn = Button(settings, text="Connect", width=25,command=port_connnect)
disconnect_btn = Button(settings, text="Disconnect", width=25,command=port_disconnnect)
connection_status = Label(settings, text="Status: Disconnected", font=('arial bold', 7))

serial_print = Entry(status, width=100, borderwidth=0.5, textvariable=serial_location)
serial_send = Button(status, text="Send",width=25, borderwidth=0.5, command=send_data)
error_list = Listbox(status, width=130)
# ======================================

status.pack(side=BOTTOM, fill=X)
serial_print.grid(row=0, column=0)
serial_send.grid(row=0, column=1)
error_list.grid(row=1,columnspan=2)
 # -------------------------------------------

 
settings.pack(side=LEFT, fill=Y)

lbl_settings.grid(columnspan=10, ipady=10)

port_label.grid(column=0,row=1, padx = 5, pady =5)
port.grid(column=1,row=1, padx = 5, pady =5)

baud_label.grid(column=0,row=2, padx = 5, pady =5)
baud.grid(column=1,row=2, padx = 5, pady =5)

timeout_label.grid(column=0,row=3, padx = 5, pady =5)
timeout.grid(column=1,row=3, padx = 5, pady =5)


# ---- 
connect_btn.grid(columnspan=3,row=5, padx = 5, pady =5)
connection_status.grid(columnspan=3,row=6, padx = 5, pady =5)
 # ----------------------------------------
body.pack(side=RIGHT)
 
 # ========================================
 # ---------- READINGS -----------------

 
 # ---------------- READINGS ----------------

 
 
root.mainloop()