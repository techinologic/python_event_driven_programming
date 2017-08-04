import tkinter
import time

# event handlers

# handler for timer event
def alarm():
    print('Calling the pizza company.')

# handler for ringing the doorbell
def doorbell():
    print('Ding Dong!')
    time.sleep(3)
    print('Opening the door')

# handler for when the phone rings
def phonecall():
    print('Answering the call')

# create buttons and assign callbacks
root = tkinter.Tk()
tkinter.Button(root, text='Ring Doorbell', command=doorbell).pack()
tkinter.Button(root, text='Call Phone', command=phonecall).pack()

# set timer for 1 second
root.after(4000, alarm())

# start the event loop
root.mainloop()

