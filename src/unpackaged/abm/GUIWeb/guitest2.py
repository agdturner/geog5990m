# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 23:59:08 2018

@author: geoagdt
"""
import tkinter
import tkinter.ttk as ttk
#import ttk.Button as Button
#import ttk.ProgressBar as ProgressBar
#import ttk.Label as Label
#import threading
#import time
#import queue

class GUI():
    def __init__(self, master):
        self.master = master
        self.max_increment = 100
        self.started = False
        self.running = False
        self.bstart = ttk.Button(self.master, command=self.b_start)
        self.bstart.configure(text="Start")
        self.bstart.pack(side='top')
        self.bstop = ttk.Button(self.master, command=self.b_stop)
        self.bstop.configure(text="Stop")
        self.bstop.configure(state='disabled')
        self.bstop.pack(side='top')
        #self.queue = queue.Queue()
        self.pb = ttk.Progressbar(
            self.master, orient="horizontal",
            length=200, mode="determinate"
            )
        self.pb.pack(side='top')
        self.increment = 0
        self.l = ttk.Label(self.master)
        self.l.pack(fill='x', side='bottom')
        
    def b_start(self):
        self.pb.start(interval='50')
        if self.started:
            print("Start Task")
        else:
            print("Continue Task")    
        self.bstart.configure(state='disabled')
        self.bstop.configure(state='normal')
        self.started = True
        self.running = True
        self.advance_bar()
        
    def b_stop(self):
        print("Stop Task", str(self.increment))
        self.bstart.configure(state='normal')
        self.bstop.configure(state='disabled')
        self.running = False
        self.pb.stop()
        
    def advance_bar(self):
        if self.running:
            self.l.config(text="iteration " + str(self.increment))
            self.pb.step(1)
            self.increment += 1
            if ((self.increment < self.max_increment) & self.running):
                self.master.after(250, self.advance_bar)
            else:
                if self.running:
                    self.master.quit()



print("<Initialise GUI>")
root = tkinter.Tk() # Main window.
root.wm_title("Model")
print("</Initialise GUI>")
GUI(root)
root.mainloop()