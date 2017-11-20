import re
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class TopMenu(tk.Tk):

    def __init__(self, master):

        self.master = master
        
        self.menubar = tk.Menu(master) 

        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label='Exit', command=master.destroy)
        self.menubar.add_cascade(label='File', menu=self.filemenu)

class ExcelFrame(tk.Frame):

    def fileCallBack(self):
        self.filetype = (('Microsoft Excel 2007-2013','*.xlsx'), ('Microsoft Excel 97-2003','*.xls'),
                    ('ODF Spreadsheet','*.ods'), ('All Files','*.*'))
        self.filePath = filedialog.askopenfilename(initialdir='.',
                                              title='Select File', filetypes=self.filetype)

        self.fileRegex = re.compile(r'''
                        [\w\.-]+      # one or more letters, digits, periods, hyphens
                        \.            # one period
                        [\w-]+$       # one or more letters, digits, hyphens.
                        ''', re.VERBOSE)
        self.fileMo = self.fileRegex.search(self.filePath)
        if (self.fileMo):
            self.fileString.set(self.fileMo.group())


    def inputValidation(self, d, s, S, condition):
        '''Input must be a digit, and the string cannot exceed 4 characters in length'''
        
        if d == '1':  # insertion
            
            if condition == 'isAlpha':   # letters only
                condition = S.isalpha()
            elif condition == 'isDigit': # digits only
                condition = S.isdigit()
            else:
                condition = True
                
            return condition and len(s) < 4
        else:
            return True # deletion; always allowed


    def __init__(self, master):

        tk.Frame.__init__(self, master)
        
        self.master = master

        self.letterEntries = ['.!excelframe.!entry2', '.!excelframe.!entry3']
        
        self.excelLabel = tk.Label(self, text='Excel File:')

        self.fileString = tk.StringVar()
        self.fileString.set('No File Selected')
        self.excelEntry = tk.Entry(self, textvariable=self.fileString, state='readonly', width=25)

        self.excelButton = tk.Button(self, text='Open File', command=self.fileCallBack)



        self.SorocImage = Image.open('soroc-logo-small.png') # load image
        self.ImageWidth, self.ImageHeight = self.SorocImage.size # get image dimensions
        self.SorocImageNewSize = (self.ImageWidth * 0.5, self.ImageHeight * 0.5) # create new image size
       
        self.SorocImage.thumbnail(self.SorocImageNewSize, Image.ANTIALIAS) # resize image
        
        self.SorocNewImage = ImageTk.PhotoImage(self.SorocImage) # convert to tkinter compatible object
                
        
        self.SorocLabel = tk.Label(self, image=self.SorocNewImage) 
        self.SorocLabel.image = self.SorocNewImage # keep reference to image object

        
        # %s substitution is the value of entry prior to editing
        # %S substitution is the text string being stored, if any
        self.vcmd = self.register(self.inputValidation)
        self.subs = ['%d', '%s', '%S']

        
        self.serialLabel = tk.Label(self, text='Serial # Column:')
        self.serialEntry = tk.Entry(self, width=4, validate='key',
                                    validatecommand=
                                    (self.vcmd, *self.subs, 'isAlpha'))

        self.assetLabel = tk.Label(self, text='Asset Tag Column:')
        self.assetEntry = tk.Entry(self, width=4, validate='key',
                                   validatecommand=
                                   (self.vcmd, *self.subs, 'isAlpha'))
       
        self.startRowLabel = tk.Label(self, text='Starting Row:')
        self.startRowEntry = tk.Entry(self, width=4, validate='key',
                                      validatecommand=
                                      (self.vcmd, *self.subs, 'isDigit'))
       
        self.endRowLabel = tk.Label(self, text='Ending Row:')
        self.endRowEntry = tk.Entry(self, width=4, validate='key',
                                    validatecommand=
                                    (self.vcmd, *self.subs, 'isDigit'))


        # Avoided using loops for grid placement clarity

        self.excelLabel.grid(row=0, column=0)
        self.excelEntry.grid(row=0, column=1)
        self.excelButton.grid(row=1, column=0)
        self.SorocLabel.grid(row=1, column=1)
        
        self.serialLabel.grid(row=2, column=0)
        self.serialEntry.grid(row=2, column=1)

        self.startRowLabel.grid(row=2, column=2)
        self.startRowEntry.grid(row=2, column=3)
        
        self.assetLabel.grid(row=3, column=0)
        self.assetEntry.grid(row=3, column=1)
        
        self.endRowLabel.grid(row=3, column=2)
        self.endRowEntry.grid(row=3, column=3)


class HardwareFrame(tk.Frame):

    def changeFrame(self):

        self.dynamicFrame.grid_forget()

        self.whatString.set(self.condLists[self.hardwareVariable.get()])
        
        self.dynamicFrame.grid(row=1, column=0)


    def __init__(self, master):

        tk.Frame.__init__(self, master)

        self.master = master

        master.title('Test')
        
        self.hardwareLabel = tk.Label(self, text='Type of Hardware:')

        self.hardwareVariable = tk.IntVar()
        self.hardwareVariable.set(0) # initialization
        
##        self.hardwareTypes = ['Laptop', 'Desktop', 'Hard Drive', 'Monitor']

##        for v in range(len(self.hardwareTypes)):
##            self.hardwareRadio = tk.Radiobutton(self, text=self.hardwareTypes[v],
##                                   variable=self.hardwareVariable, value=v)
##
##            self.hardwareRadio.grid(row=1, column=v)

  
        
        self.laptopRadio = tk.Radiobutton(self, text='Laptop',
                                          variable=self.hardwareVariable,
                                          value=0, command=self.changeFrame)
        self.desktopRadio = tk.Radiobutton(self, text='Desktop',
                                           variable=self.hardwareVariable,
                                           value=1, command=self.changeFrame)
        self.hardDriveRadio = tk.Radiobutton(self, text='Hard Drive',
                                             variable=self.hardwareVariable,
                                             value=2, command=self.changeFrame)
        self.monitorRadio = tk.Radiobutton(self, text='Monitor',
                                           variable=self.hardwareVariable,
                                           value=3, command=self.changeFrame)



        self.condLists = ['Raptop:', '80G3:', 'Size: (GB):', 'Inches:']
        self.whatString = tk.StringVar()
        self.whatString.set(self.condLists[0])

        self.dynamicFrame = tk.Frame(self) # frame that changes depending on value of radio button
        
        self.dynamicLabel = tk.Label(self.dynamicFrame, textvariable=self.whatString)
        self.dynamicEntry = tk.Entry(self.dynamicFrame)


        self.hardwareLabel.grid(row=0, column=0)
        
        self.laptopRadio.grid(row=0, column=1)
        self.desktopRadio.grid(row=0, column=2)
        self.hardDriveRadio.grid(row=0, column=3)
        self.monitorRadio.grid(row=0, column=4)



        self.dynamicLabel.grid(row=0, column=0)
        self.dynamicEntry.grid(row=0, column=1)

        self.dynamicFrame.grid(row=1, column=0)




class App(tk.Frame):

    def __init__(self, master):

        self.master = master
        #self.master.minsize(width=555, height=555)
        
        frame1 = ExcelFrame(master)
        frame2 = HardwareFrame(master)
        
        frame1.grid(row=0, column=0)
        frame2.grid(row=1, column=0)


##    def wrapperY(self, wid1, wid2):
##
##        self.wid1.grid_forget()
##        self.wid2.grid(row=0, column=1)

if __name__ == '__main__':
    
    root = tk.Tk()
    ####### * put in App() root.minsize(width=555, height=555)
    my_gui = App(root)
    mmmenu = TopMenu(root)
    root.config(menu=mmmenu.menubar)
    root.mainloop()

