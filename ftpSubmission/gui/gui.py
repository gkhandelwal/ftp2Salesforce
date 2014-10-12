from Tkinter import *
import ftpSalesforce


def buttonOkay():
	with open("configuration.txt", "w") as myfile:
		myfile.write("filename = ")        
		myfile.write(entry1.get())
		myfile.write("\n")
		
		myfile.write("ftpUsername = ")        
		myfile.write(entry2.get())
		myfile.write("\n")
		
		myfile.write("ftpUserPassword = ")        
		myfile.write(entry3.get())
		myfile.write("\n")
		
		myfile.write("ftpServer = ")        
		myfile.write(entry4.get())
		myfile.write("\n")
		
		myfile.write("salesforceUserName  = ")        
		myfile.write(entry5.get())
		myfile.write("\n")
		
		myfile.write("salesforcepassword  = ")        
		myfile.write(entry6.get())
		myfile.write("\n")
		
		myfile.write("salesforcesecurityToken  = ")        
		myfile.write(entry7.get())
		myfile.write("\n")
		
		myfile.write("salesforceinstance  = ")        
		myfile.write(entry8.get())
		myfile.write("\n")

		myfile.write("targetFoldername  = ")        
		myfile.write(entry9.get())

	myfile.close()
	root.destroy()
	ftpSalesforce.runner()
	
	
	
	
root = Tk()
frame1 = Frame(root)
frame1.pack(fill=X)

Label1= Label(frame1,text="Filename",bg='orange') # Label with color orange and text of Filename added
Label1.pack(side = LEFT)
entry1 = Entry(frame1)
entry1.pack(side = RIGHT)

frame2 = Frame(root)
frame2.pack(fill=X)

Label2= Label(frame2,text="ftpUsername",bg='orange') # Label with color orange and text of Filename added
Label2.pack(side = LEFT)
entry2 = Entry(frame2)
entry2.pack(side = RIGHT)

frame3 = Frame(root)
frame3.pack(fill=X)

Label3= Label(frame3,text="ftpUserPassword",bg='orange') # Label with color orange and text of Filename added
Label3.pack(side = LEFT)
entry3 = Entry(frame3)
entry3.pack(side = RIGHT)

frame4 = Frame(root)
frame4.pack(fill=X)

Label4= Label(frame4,text="ftpServer",bg='orange') # Label with color orange and text of Filename added
Label4.pack(side = LEFT)
entry4 = Entry(frame4)
entry4.pack(side = RIGHT)

frame5 = Frame(root)
frame5.pack(fill=X)

Label5= Label(frame5,text="salesforceUserName",bg='orange') # Label with color orange and text of Filename added
Label5.pack(side = LEFT)
entry5 = Entry(frame5)
entry5.pack(side = RIGHT)

frame6 = Frame(root)
frame6.pack(fill=X)

Label6= Label(frame6,text="salesforcepassword",bg='orange') # Label with color orange and text of Filename added
Label6.pack(side = LEFT)
entry6 = Entry(frame6)
entry6.pack(side = RIGHT)

frame7 = Frame(root)
frame7.pack(fill=X)

Label7= Label(frame7,text="salesforcesecurityToken",bg='orange') # Label with color orange and text of Filename added
Label7.pack(side = LEFT)
entry7 = Entry(frame7)
entry7.pack(side = RIGHT)

frame8 = Frame(root)
frame8.pack(fill=X)

Label8= Label(frame8,text="salesforceinstance",bg='orange') # Label with color orange and text of Filename added
Label8.pack(side = LEFT)
entry8 = Entry(frame8)
entry8.pack(side = RIGHT)

frame9 = Frame(root)
frame9.pack(fill=X)

Label9= Label(frame9,text="targetFoldername",bg='orange') # Label with color orange and text of Filename added
Label9.pack(side = LEFT)
entry9 = Entry(frame9)
entry9.pack(side = RIGHT)

frame10 = Frame(root)
frame10.pack()
buttonOk = Button(frame10,text="OK",command=buttonOkay)
buttonOk.pack()



root.mainloop()
