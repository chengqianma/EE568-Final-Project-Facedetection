import tkinter as tk
import fp
#import tkinter.messagebox as tkmb
#from tkinter import filedialog

root = tk.Tk()
root.title('EE568 Final Project (Name: Chengqian Ma, Student ID: 1868621)')
root.geometry('1920x1080+0+0')
#canvas = tk.Canvas(root,bg='blue',height = 640, width = 320)

B1 = tk.Button(root,text = "choose an image",width = 20, height = 2,command = fp.ip)
#B1.pack()
B1.grid(row=0, column=0, padx=5,pady=5)
#image_path = file_path
#canvas.create_image(960,640,image = image_path)
B2 = tk.Button(root,text = "mosaic",width = 20, height = 2, command = fp.face_mask)
#canvas.pack()
B2.grid(row=1, column=0, padx=5,pady=5)
#B2.pack()
B3 = tk.Button(root,text = "choose a mask image",width = 20, height = 2,command = fp.ip2)
B3.grid(row=2, column=0, padx=5,pady=5)
B4 = tk.Button(root,text = "mask",width = 20, height = 2, command = fp.face_mask2)
B4.grid(row=3, column=0, padx=5,pady=5)
B5 = tk.Button(root,text = "handdraw",width = 20, height = 2, command = fp.handdraw)
B5.grid(row=4, column=0, padx=5,pady=5)
label = tk.Label(root, text = "Attention: Please press any key before you close the image window")
label.grid(row=5, column=0, padx=5,pady=5)
"""
im = Image.open("E:/myself.jpg")
#img = ImageTk.PhotoImage(im)
#im = cv.imread("E:/myself.jpg")
#x2, y2 = im.shape[0:2]
#img = cv.resize(im,(480,320),fx = 480/x2,fy = 320/y2)
img = ImageTk.PhotoImage(im)
imcanvas = tk.Canvas(root,bg = 'gray')
imcanvas.create_image(480,320,image = img)
#imlabel = tk.Label(root, image = img, width = 300, height = 300)
imcanvas.grid(row=0, column=3, padx=5,pady=5)
"""
root.mainloop()
"""
top = tkinter.Tk()
#top.withdraw()
def hello():
    tkmb.showinfo("Hello Python","Hello EE568 Final Project")

#B = tkinter.Button(top,text = "input",command = fp.input )

#T = tkinter.Button(top,text = "transform",command = fp.face_mask(B))
def show_img():
    temp = Image.open("E:/myself.jpg")
    img = ImageTk.PhotoImage(temp)
    tkinter.Label(top,image=img).pack()
    
#B.pack()
#T.pack()
    
show_img()
top.mainloop()
"""
