import tkinter as tk

LARGE_FONT = ("Arial", 12) #Constant font 

class MyApp(tk.Tk): #tk.Tk as inheritance for MyApp
    
    def __init__(self, *args, **kwargs): #Initializes stuff each time MyApp class is called. args catches single arguments, and kwargs catches all dictionaries (any object with keys)
        
        tk.Tk.__init__(self, *args, **kwargs)
        
        container = tk.Frame(self) #Because we'll always gonna have a container
        
        container.pack(side="top", fill="both", expand=True) #Pack is simpler but limited
        
        container.grid_rowconfigure(0, weight=1) #0 as minimum size, weight is prioritization level for the element
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {} #Empty dict, we will store pages/frames here
        
        #Add new pages here
        for F in (StartPage, PageOne, About):
            frame = F(container, self) #Initial page we will run
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew") #Another method to create grids. More configurable than Pack. sticky is alignment + stretch.
        
        #Initialize with StartPage
        self.show_frame(StartPage)
        
        
    def show_frame(self, cont): #Controller is page to view aka StartPage key above
        
        frame = self.frames[cont]
        frame.tkraise() #Built-in tk method which raises frame to the front based on controller

def qf(param):
    print(param)
        
class StartPage(tk.Frame): #Inherit tk.Frame
    
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent) #Parent Class is MyApp
        label = tk.Label(self, text="Start Page", font=LARGE_FONT) #Now we have a tk.Label object called label
        label.pack(pady=10, padx=10) #Use pack to add label to the page
        
        # button1 = tk.Button(self, text="Visit Page 1", command=qf("This will only run once, on load.")) #Upon button click, command executes any function you pass in.
        #MASSIVE CAVEAT with command is you cannot pass in a param just like you normally would IF you are using a function.
        #A workaround is to use lambda function:
        # button1 = tk.Button(self, text="Visit Page ", command=lambda: qf("This can run as many times as the button is clicked."))
        
        button1 = tk.Button(self, text="Visit PageOne", command=lambda: controller.show_frame(PageOne)) #This button uses controller from tk.Frame and applies show_frame() method from MyApp class
        button1.pack()
        
        button2 = tk.Button(self, text="About", command=lambda: controller.show_frame(About)) #This button uses controller from tk.Frame and applies show_frame() method from MyApp class
        button2.pack()
        
class PageOne(tk.Frame):
    
    def __init__(self, parent, controller): #Most of the time you are going to program every part of your page in an init method
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=f"You are on PageOne", font=LARGE_FONT) #Now we have a tk.Label object called label
        label.pack(pady=10, padx=10) #Use pack to add label to the page
        
        button1 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage)) #This button uses controller from tk.Frame and applies show_frame() method from MyApp class
        button1.pack()
        
class About(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=f"This is a tkinter template created for fast\nprototyping of GUIs for my projects.", font=LARGE_FONT) #Now we have a tk.Label object called label
        label.pack(pady=10, padx=10) #Use pack to add label to the page
        
        button1 = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage)) #This button uses controller from tk.Frame and applies show_frame() method from MyApp class
        button1.pack()

#Run app
app = MyApp()
app.mainloop()