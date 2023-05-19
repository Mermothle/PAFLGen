import tkinter as tk
from tkinter import messagebox
import customtkinter
import gens.mutants as mtn
import gens.scientists as sts
import gens.stalkers as stk
import os



mut = mtn.mutantGen()
sci = sts.scientistGen()
stl = stk.stalkerGen()

class myGUI:

    def __init__(self):

        customtkinter.set_appearance_mode("system")
        customtkinter.set_default_color_theme("dark-blue")

        self.root = customtkinter.CTk()
        self.root.geometry("800x500")
        self.root.title("PAFLGen Enhanced")


        self.label = customtkinter.CTkLabel(self.root, text="Welcome to PAFLGen Enhanced! Have fun!", font=('Arial', 16), wraplength=500, justify="center")
        self.label.pack(padx=10, pady=10)

        self.masterLabel = customtkinter.CTkLabel(self.root, text="", font=('Arial', 16), wraplength=500, justify="center")

        self.savedLabel = customtkinter.CTkLabel(self.root, text="", font=('Arial', 16), justify="center")

        self.savedEntryLabel = customtkinter.CTkLabel(self.root, text="Type your filename below, then hit save!", font=('Arial', 16), justify="center")
        self.savedEntryTip = customtkinter.CTkLabel(self.root, text="Note: Files will be saved to /generated/ as a .txt file!\nPutting PAFLGen Enhanced in its own folder is recommended.", font=('Arial', 10), justify="center")
        self.savedEntry = customtkinter.CTkEntry(self.root, font=('Arial', 12))

        
        def mutantPress():
            mut = mtn.mutantGen()
            self.masterLabel.configure(text=mut)
            self.masterLabel.update()

        def stalkerPress():
            stl = stk.stalkerGen()
            self.masterLabel.configure(text=stl)
            self.masterLabel.update()

        def scientistPress():
            sci = sts.scientistGen()
            self.masterLabel.configure(text=sci)
            self.masterLabel.update()

        #def printMutant():
            #self.masterLabel.configure(text=mut)

            
        def saveToFile():
            #ocCounter = 0
            #currentDirectory = os.getcwd()
            currentDirectory = os.path.dirname(__file__)
            relDirectory = "generated"
            filePath = os.path.join(currentDirectory, relDirectory) 
            if not os.path.exists(filePath):
                os.makedirs(filePath)
            #while os.path.exists(filePath + "/PAFL%s.txt" % ocCounter):
                #ocCounter += 1
            self.masterLabel.update()
            self.lastOC = self.masterLabel.cget("text")
            strLastOC = str(self.lastOC)
            #print(strLastOC)

            ocFile = self.savedEntry.get()
            with open(filePath + "/%s" % ocFile + '.txt', 'w', encoding='utf-8') as f:
                f.write(strLastOC)
                f.close

            self.savedLabel.configure(text="Saved %s" % ocFile + '.txt!')
            #ocFile = open(filePath + "/PAFL%s.txt" % ocCounter, "w")
            #ocFile.write(strLastOC)
            #ocFile.close
            #self.savedLabel.configure(text="Saved PAFL%s.txt!" % ocCounter)

        '''def saveToFile():
            ocCounter = 0
            #currentDirectory = os.getcwd()
            currentDirectory = os.path.dirname(__file__)
            relDirectory = "generated"
            filePath = os.path.join(currentDirectory, relDirectory) 
            if not os.path.exists(filePath):
                os.makedirs(filePath)
            while os.path.exists(filePath + "/PAFL%s.txt" % ocCounter):
                ocCounter += 1
            self.masterLabel.update()
            self.lastOC = self.masterLabel.cget("text")
            strLastOC = str(self.lastOC)
            #print(strLastOC)
            ocFile = open(filePath + "/PAFL%s.txt" % ocCounter, "w")
            ocFile.write(strLastOC)
            ocFile.close
            self.savedLabel.configure(text="Saved PAFL%s.txt!" % ocCounter)'''
            

        #self.masterLabelVariable = customtkinter.StringVar()
        self.masterLabel = customtkinter.CTkLabel(self.root, text="", font=('Arial', 16), wraplength=750, justify="center")

        self.buttonFrame = customtkinter.CTkFrame(self.root)
        self.buttonFrame.columnconfigure(0, weight=1)
        self.buttonFrame.columnconfigure(1, weight=1)
        self.buttonFrame.columnconfigure(2, weight=1)

        # self.stalkerLabel = customtkinter.CTkLabel(self.root, text="x", font=('Arial', 12))
        self.stalkerButton = customtkinter.CTkButton(self.buttonFrame, text="Stalkers", font=('Arial', 12), command=stalkerPress)
        self.stalkerButton.grid(row=0, column=0, padx=5, sticky=tk.W+tk.E)

        self.mutantButton = customtkinter.CTkButton(self.buttonFrame, text="Mutants", font=('Arial', 12), command=mutantPress)
        self.mutantButton.grid(row=0, column=1, padx=5, sticky=tk.W+tk.E)

        self.scientistButton = customtkinter.CTkButton(self.buttonFrame, text="Scientists", font=('Arial', 12), command=scientistPress)
        self.scientistButton.grid(row=0, column=2, padx=5, sticky=tk.W+tk.E)

        #self.saveButton = customtkinter.CTkButton(self.buttonFrame, text="Save!", font=('Arial', 12), command=saveToFile)
        self.saveButton = customtkinter.CTkButton(self.buttonFrame, text="Save!", font=('Arial', 12), command=saveToFile)
        self.saveButton.grid(row=1, column=1, padx=5, pady=10, sticky=tk.W+tk.E)

        self.buttonFrame.pack(fill='x')
        self.savedEntryLabel.pack(padx=10, pady=5)
        self.savedEntryTip.pack(padx=10)
        self.savedEntry.pack(padx=10, pady=5)
        self.masterLabel.pack(padx=10, pady=10)

        self.savedLabel.pack(pady=10)

        '''self.anotherBtn = tk.Button(self.root, text="TEST")
        self.anotherBtn.place(x=200, y=200, height=100, width=100)'''


        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()
        #self.root.destroy()

    

    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit? Your progress will be lost."):
            self.root.destroy()


myGUI()



