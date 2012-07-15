import tkinter as tki
from tkinter import ttk
import os
import file_search3_tk
mysearch = file_search3_tk

root_list=[]

class Baseframe(tki.Frame):
    '''create GUI including functions to populate combobox'''
    
    def __init__ (self, master):
        super(Baseframe, self).__init__(master)
        self.grid()
        self.initUI()
        
    def initUI(self):
        '''create widgets'''
        
        self.master.title("File count")
        self.Frame1 = tki.ttk.Frame(self, padding=("10 10 10 10"))
        self.Frame1.grid(column=0, row=0, sticky=("N,E,S,W"))
        self.Frame1.columnconfigure(0, weight=1)
        self.Frame1.rowconfigure(0, weight=1)
        self.Entry1 = tki.ttk.Entry(self.Frame1, width="50")
        self.Entry1.grid(column=0, row=2, sticky="W", pady=5)
        self.Combo1 = tki.ttk.Combobox(self.Frame1, width="75")
        self.Combo1.grid(column=0, columnspan=2, row=4, 
            pady=5, sticky="E")
        #Buttons
        self.Button1 = tki.ttk.Button(self.Frame1, text="Submit", 
            command=self.getcombo)
        self.Button1.grid(column=1, row=5, sticky="EW")
        self.Button2 = tki.ttk.Button(self.Frame1, text="Directories",
            command=self.search_path)
        self.Button2.grid(column=0, row=5, sticky="W")
        #Labels
        self.Label1 = tki.ttk.Label(self.Frame1, relief="sunken",
            borderwidth=5)
        self.Label1.grid(column=0, columnspan=2, row=7,
                rowspan=3, pady=5, sticky="NSEW")
        self.Label2 = tki.ttk.Label(self.Frame1)
        self.Label2.grid(column=0, row=1, sticky='W')
        self.Label2['text']='1. Enter filepath below using /'
        self.Label3 = tki.ttk.Label(self.Frame1)
        self.Label3.grid(column=0, row=3, sticky='W')
        self.Label3['text']='2. Select folder below'
        self.Label4 = tki.ttk.Label(self.Frame1)
        self.Label4.grid(column=0, row=6, sticky='W', pady=5)
        self.Label4['text']='3. Output'
      
    def search_path(self):
        '''sets list of values for combobox'''
        
        root_list = self.directory_list(self.Entry1.get())
        self.Combo1['values'] = root_list
        if root_list ==[]: return
        self.Combo1.current(0) #sets initial combobox value
        
    def directory_list(self, mypath=''):
       '''creates the list of sub-directories from a given directory'''
       
       temp_list = list()
       cntFolder=0
       root_dir = mypath.rstrip("\\")
       #code below helps to fix bug with tkinter combobox
       for root, name, files in os.walk(root_dir):
          #print('Root:', root) #tests output
          cntFolder+=1
          temp_list.append(root)
       return [self.fix_tcl_string(nathan) for nathan in temp_list]  

    def fix_tcl_string(self, nathan):
        '''more code for combobox bug fix'''
        
        if '\\' in nathan and not ' ' in nathan:
            return '{'+nathan+'}'
        else:
            return nathan        
            
    def getcombo(self):
		'''calls function to count file types using path from combo'''
		
        a=self.Combo1.get()
        self.Label1['text']=mysearch.Search_Main(a)

def GUImain():
   root=tki.Tk()
   app=Baseframe(root)
   app.Entry1.focus_set()   
   root.mainloop()

#GUImain()
if __name__ == '__main__':
	print("This module should be imported not run directly")
