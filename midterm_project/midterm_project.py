# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 10:22:10 2019

@author: Jonathan Boryla
"""

#Import librarys for use in program
import tkinter as tk
from tkinter import messagebox
import os

#Open log file and add items to seen_files list
with open('log.txt', 'r') as seen_file_path:
    seen_files = []
    for line in seen_file_path:
        seen_files.append(line.replace('\n', ''))

#open annotation file and import the file path as well as the coordinates of the bounding box
with open('annotation.txt', 'r') as input_file_path:
    photo=[]
    for line in input_file_path:
        entry = line.replace('\n', '').split(' ')
        thermal_path=os.path.join(*entry[0].split('/'))
        #Check to make sure the thermal path is not in the seen files list
        if thermal_path not in seen_files:
            rgb_path = thermal_path.replace('thermal', 'rgb')
            anno_boxes = entry[1:]
            photo.append((rgb_path, thermal_path, anno_boxes))
    photo.sort()
    
#Create a class for the GUI
class TkinterApp:
    
    #Initialize the GUI
    def __init__(self, root):
        self.index = 0
        self.root = root
        self.root.protocol('WM_DELETE_WINDOW', self.exit_gui)
        self.window_setup()
        self.window_layout()
        self.save_list = []
        self.seen_list = []         
        
        self.log_file = open("log.txt", "w")
    
        with open ('save.txt', 'r') as f:
            for line in f:
                self.save_list.append(line.replace('\n' , ''))
        
        for item in seen_files:
            self.log_file.write(item + '\n')
    
    #Setup the window frame    
    def window_setup(self):
        
        self.canvas = tk.Canvas(self.root, width =640, height = 500, bg='white')
        self.canvas2 = tk.Canvas(self.root, width =640, height = 500, bg='white')
        self.rgb_button = tk.Button(self.root, text='RGB', command=self.load_rbg)
        self.thermal_button = tk.Button(root, text='Thermal', command=self.load_thermal)
        self.anno_button = tk.Button(root, text='Annotation', command=self.load_annotation)
        self.next_button = tk.Button(root, text='Next', command=self.load_next_image)
        self.previous_button = tk.Button(root, text='Previous', command=self.load_previous_image)
        self.save_button = tk.Button(root, text='SAVE', command=self.save)
        self.log_button = tk.Button(root, text='Log', command=self.log)
        self.clear_log_button = tk.Button(root, text='Clear Log', command=self.clear_log)
      
    #Create the window layout    
    def window_layout(self):
        self.canvas.grid(column= 1 , row =0 , rowspan=5, columnspan = 5)
        self.canvas2.grid(column=6 , row=0 , rowspan=5 , columnspan = 5)
        self.rgb_button.config(width = 8)
        self.rgb_button.grid(column=0 , row=0)
        self.thermal_button.config(width = 8)
        self.thermal_button.grid(column=0 , row=1)
        self.anno_button.grid(column=0 , row=2)
        self.log_button.config(width = 8)
        self.log_button.grid(column=0 , row=3)
        self.clear_log_button.config(width = 8)
        self.clear_log_button.grid(column=0 , row=4)
        self.next_button.config(width = 8)
        self.next_button.grid(column=6 , row=6, columnspan=5)
        self.save_button.config(width = 8)
        self.save_button.grid(column=5 , row=6, columnspan=2)
        self.previous_button.config(width = 8)
        self.previous_button.grid(column=1 , row=6, columnspan=5)
    
    '''Function that is called when the save button is pressed
        the function creates a save item, and checks the save list
        to verify that save item has not already been added to the save
        list.'''
    def save(self):
        annotations = ''
        for annotation in photo[self.index][2]:
            annotations = str(annotations + ' ' + annotation)
        save_item = str(photo[self.index][1] + annotations)
        
        if save_item not in self.save_list:
            self.save_list.append(save_item)
    '''Function called for a log button press, the function writes all files 
        seen at that point to the log file.'''

    def log(self):
        for item in self.seen_list:
            self.log_file.write(item + '\n')
            
    '''Function for the clear log button, clears the log when pressed'''
    def clear_log(self):
        self.log_file.close()
        with open('log.txt' , 'w'):
            pass
    
    '''Function for the next button, the function loads the next RGB and
        thermal images, as well as the annotations. The function also checks
        to make sure the index of the next images to load are not exceeding 
        the total number of images.'''
    def load_next_image(self):
        self.index += 1
        #Disables the next button if the index exceeds the number of images
        if self.index > len(photo)-1:
            self.next_button.config(state = "disabled")
            
        if self.index > len(photo)-1:
            if  len(photo) == 0:
                 pass
            else:     
                tk.messagebox.showinfo(title="WARNING!!!", message="WARNING LAST IMAGE!")
                self.index = (len(photo)-1)
            
        self.load_rbg()
        self.load_thermal()
        self.load_annotation()
        
        #Re-enable previous button if the length of the photo array is not 0
        if len(photo) != 0:
            self.previous_button.config(state = "normal")
    '''Funtion the previous button, loads the previous RGB and thermal images,
        and the annotations.'''
    def load_previous_image(self):
        self.index -= 1
        #Disable previous button if index is less than 0
        if self.index < 0:
            self.previous_button.config(state = "disabled")
            
        if self.index < 0:
            if  len(photo) == 0:
                pass
            else:
                tk.messagebox.showinfo(title="WARNING!!!", message="WARNING FIRST IMAGE!")
                self.index = 0  
            
        self.load_rbg()
        self.load_thermal()
        self.load_annotation()
        
        #Re-enables the next button given the photo array is not empty        
        if len(photo) != 0:
            self.next_button.config(state = "normal")
    
    #Function to load the annotations on both pictures
    def load_annotation(self):
        if  len(photo) == 0:
            tk.messagebox.showinfo(title="WARNING!!!", message="WARNING NO MORE ANNOTATIONS!")
        
        for annotation in photo[self.index][2]:
            box = annotation.split(',')
            x1 = box[0]
            x2 = box[1]
            y1 = box[2]
            y2 = box[3]
            self.canvas.create_rectangle(x1,x2,y1,y2, outline='orange')
            self.canvas2.create_rectangle(x1,x2,y1,y2, outline='orange')
    
    #Function to load the RBG image    
    def load_rbg(self):
        if  len(photo) == 0:
            tk.messagebox.showinfo(title="WARNING!!!", message="WARNING NO MORE COLOR IMAGES!")
        if len(photo) != 0:
            self.rgb_image=tk.PhotoImage(file = photo[self.index][0])
            self.canvas.create_image( 0,0,  image=self.rgb_image, anchor='nw')
    
    #Function to load the thermal image    
    def load_thermal(self):
        if  len(photo) == 0:
            tk.messagebox.showinfo(title="WARNING!!!", message="WARNING NO MORE THERMAL IMAGES!")
        
        else:
            self.thermal_image = tk.PhotoImage(file = photo[self.index][1])
            self.canvas2.create_image( 0,0,  image=self.thermal_image, anchor='nw')
            if str(photo[self.index][1]) not in self.seen_list:
                self.seen_list.append(str(photo[self.index][1])) 
                
    #Function that is called when the [X] button is hit to close the GUI  
    def exit_gui(self):
        log_list = []
        self.log_file.close()
        
        with open('save.txt','w') as save_file:
            for item in self.save_list:
                save_file.write(item + '\n')
         
        with open ('log.txt', 'r') as log:
            for line in log:
                if str(line) not in log_list:
                    log_list.append(str(line))
                    
        with open ('log.txt' , 'w') as log:
            for line in log_list:
                log.write(line)
        self.root.destroy()   

root = tk.Tk()
TkApp = TkinterApp(root)
root.mainloop()