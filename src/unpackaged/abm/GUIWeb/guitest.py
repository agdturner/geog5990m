# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 19:12:48 2018

@author: geoagdt
"""
#import matplotlib
#matplotlib.use('TkAgg') # Needs to be before any other matplotlb imports
#matplotlib.use('TkInter')
import tkinter
import tkinter.ttk as ttk
import threading
import time
import queue

class GUI:
    def __init__(self, master):
        self.master = master
        self.bstart = ttk.Button(self.master, command=self.b_start)
        self.bstart.configure(text="Start")
        self.bstart.pack(side='top')
        self.bstop = ttk.Button(self.master, command=self.b_stop)
        self.bstop.configure(text="Stop")
        self.bstop.configure(state='disabled')
        self.bstop.pack(side='top')
        self.queue = queue.Queue()
        self.pb = ttk.Progressbar(
            self.master, orient="horizontal",
            length=200, mode="determinate"
            )
        self.pb.pack(side='top')
        self.value = 0
        
    def b_start(self):
        self.pb.start(interval='50')
        print("Start Task")
        self.bstart.configure(state='disabled')
        self.bstop.configure(state='normal')
        self.t = ThreadedTask(self.queue).start()
        self.master.after(100, self.process_queue)
        
    def b_stop(self):
        print("Stop Task", self.value)
        self.bstart.configure(state='normal')
        self.bstop.configure(state='disabled')
        self.pb.
        
    def process_queue(self):
        try:
            msg = self.queue.get(0)
            print(msg)
            self.bstart.configure(state='normal')
            self.bstop.configure(state='disabled')
            self.pb.stop()
            #self.pb.destroy()
        except queue.Empty:
            self.master.after(100, self.process_queue)

print("<Initialise GUI>")
root = tkinter.Tk() # Main window.
root.wm_title("Model")
print("</Initialise GUI>")
main_ui = GUI(root)
root.mainloop()

class ThreadedTask(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
    def run(self):
        time.sleep(5)  # Simulate long running process
        self.queue.put("Task finished")