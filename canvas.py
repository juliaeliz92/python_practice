from tkinter import *
import tkinter.messagebox as tmsg 
from tkinter.filedialog import askopenfilename, asksaveasfilename #for saving files in a directory
import pickle #save draw object in pickle file
from tkinter.colorchooser import askcolor #custom color palates

# Starting point of mouse dragging or shapes
prev_x = 0 
prev_y = 0 
# Current x,y position of mouse cursor or end position of dragging
x = 0 
y = 0
created_element_info = [] #list of all shapes objects for saving drawing
new = [] # Each shapes of canvas
created = [] # Temporary list to hold info on every drag
shape = "Line" # Shape to draw
color = "blue" # Color of the shape
line_width = 3 # Width of the line shape

# All the functions and logics go here
#Capture Motions on every mouse position change
def captureMotion(e=""):
    #Update Status Bar
    status.set(f"Position : x - {e.x} , y - {e.y}")
    statusbar.update()


# Update the previous position on mouse left click
def recordPosition(e=""):
    global prev_x
    global prev_y
    prev_x = e.x
    prev_y = e.y

# Color Picker
def colorPicker(e=""):
    global color
    color = askcolor(color=color)[1]
    #Set the color of shapes
    root.config(cursor=f'cursor {color} {color}', insertbackground=f"{color}")

# Update the current shape
def shapechanger(e=""):
    global shape
    shape = radiovalue.get() #selected radio value

# Runs On scale value change and update line width
def setlinewidth(e=""):
    global line_width
    line_width = scale.get()
    # Save the drawing on a file

# After Every drawing create info of drawing and add the element to new list and assign empty list to created
def generateShapesObj(e=""):
    global created,created_element_info
    new.append(created[-1])
    created = []
    created_element_info_obj = {
        "type": shape,
        "color": color,
        "prev_x": prev_x,
        "prev_y": prev_y,
        "x": x,
        "y": y
    }
    created_element_info.append(created_element_info_obj)

# Create Elements on canvas based on shape variable
def createElms():
    if shape == "Rectangle":
        a = canvas.create_rectangle(prev_x, prev_y, x, y, fill=color)
    elif shape == "Oval":
        a = canvas.create_oval(prev_x, prev_y, x, y, fill=color)
    elif shape == "Arc":
        a = canvas.create_arc(prev_x, prev_y, x, y, fill=color)
    elif shape == "Line":
        a = canvas.create_line(prev_x, prev_y, x, y,
                               width=line_width, fill=color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=3)
    return a

# Create shapes on mouse dragging and resize and show the shapes on the canvas
def drawShapesOnDragging(e=""):
    global x,y
    try:
        # Update current Position
        x = e.x
        y = e.y

        #Generate Element
        element = createElms()
        deleteUnwanted(element) # Delete unwanted shapes
    except Exception as e:
        tmsg.showerror("Some Error Occurred!", e)

def deleteUnwanted(element):
    global created
    created.append(element) #Elements that created
    for item in created[:-1]: 
        canvas.delete(item)

# Save the list of shapes objects on a pickle file
def saveDrawingFile(e=""):
    global created_element_info
    filename = asksaveasfilename(initialfile="drawing",defaultextension=".pkl",filetypes=[("Pickle Files", "*.pkl")]) #Save as
    if filename != None: 
        with open(filename, "wb") as f:
            pickle.dump(created_element_info, f)

def getsavedrawing():
    global x, y, prev_x, prev_y, shape, color
    filename = askopenfilename(defaultextension=".pkl", filetypes = [("Pickle Files", "*.pkl")])
    if filename != None:
        with open(filename, "rb") as f:
            data = pickle.load(f)
            for draw_info in data:
                x = draw_info["x"]
                y = draw_info["y"]
                prev_x = draw_info["prev_x"]
                prev_y = draw_info["prev_y"]
                shape = draw_info["type"]
                color = draw_info["color"]
                createElms() #Draw each shapes

# Clear the Canvas
def clearCanvas(e=""):
    global created_element_info, canvas, created, new
    canvas.delete("all")
    created_element_info = []
    created = []
    new = []

root = Tk()
root.title("Drawing Pad")
root.minsize(600,300) #Minimum Size of the window
# All Widgets here such as canvas, buttons etc

# Canvas
CANVAS_WIDTH = 600
CANVAS_HEIGHT = 400
canvas = Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
canvas.pack()

# Binding Events to canvas
# Structure: canvas.bind("<eventcodename>", function-name)
canvas.bind("<1>", recordPosition) #On Mouse left click
canvas.bind("<B1-Motion>", drawShapesOnDragging) #Capture Mouse left click + move (dragging)
canvas.bind("<ButtonRelease-1>", generateShapesObj) #When Mouse left click release
canvas.bind("<Motion>", captureMotion) #Mouse Motion
frame = Frame(root)
frame.pack(side=BOTTOM)
radiovalue = StringVar()
geometry_shapes = ["Line", "Rectangle", "Arc", "Oval"]
radiovalue.set("Line") #Default Select

# Manupulates Radios from the list
for shape in geometry_shapes:
    radio = Radiobutton(frame, text=shape, variable=radiovalue, font="comicsans     12 bold", value=shape, command=shapechanger).pack(side=LEFT, padx=6,pady=3)

#Buttons
Button(frame, text="Save", font="comicsans 12 bold",
       command=saveDrawingFile).pack(side=BOTTOM, padx=6, pady=6)
Button(frame, text="Clear", font="comicsans 12 bold",
       command=clearCanvas).pack(side=BOTTOM, padx=6)
Button(frame, text="Color", font="comicsans 12 bold",
       command=colorPicker).pack(side=BOTTOM, padx=6)
Button(frame, text="Get", font="comicsans 12 bold",
       command=getsavedrawing).pack(side=BOTTOM, padx=6)

# Scale
scale = Scale(root, from_=1, to=20, orient=HORIZONTAL, command=setlinewidth)
scale.pack(side=BOTTOM)

# Status Bar
status = StringVar()
status.set("Position : x - 0 , y - 0")
statusbar = Label(root, textvariable=status, anchor="w", relief=SUNKEN)
statusbar.pack(side=BOTTOM, fill=X)
root.mainloop()