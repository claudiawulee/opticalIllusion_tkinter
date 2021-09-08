def drawIllusion(canvas, size):
    for row in range(size):
        y1 = row * 20
        y2 = 400 - (row *20)
        x1 = row * 20
        x2 = 400 - (row*20)
        if row % 2 == 0:
            color = "black"
        else:
            color = "white"
        canvas.create_rectangle(x1, y1, x2, y2, fill=color) #x1,y1,x2,y2

import tkinter
def runDrawIllusion():
    root = tkinter.Tk()
    canvas = tkinter.Canvas(root, width=400,
                            height=400)
    canvas.configure(bd=0,
                     highlightthickness=0)
    canvas.pack()

    drawIllusion(canvas, 10) # your call here!
    print(canvas)

    root.mainloop()