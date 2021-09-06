import tkinter

root = tkinter.Tk()
root.geometry("400x300")
canvas = tkinter.Canvas(root, width = 400, height = 300)
canvas.create_rectangle(0,0,400,300,fill='green')
canvas.place(x=0,y=0)
root.mainloop()