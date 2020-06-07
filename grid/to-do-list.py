import tkinter
from tkinter import messagebox
import random
from ttkthemes import themed_tk as tk
import sys 
#root
#root = tkinter.Tk()
root = tk.ThemedTk()
root.get_themes()                 # Returns a list of all themes that can be set
root.set_theme("clearlooks")         # Sets an available theme

#Change root background color
root.configure(bg="#ffffff")

#change the title
root.title("To-Do List")
#change the root size
root.geometry("250x250")
#theme

tasks = []

#for testing
#tasks = ["a","b","c","f","e"]

#Functions
def update_listbox():
    """
    Clears the list and then updates the listbox
    """
    clear_listbox()
    for task in tasks:
        lb_list_box.insert("end",task)

def clear_listbox():
   '''Clears the listbox'''
   lb_list_box.delete(0,"end")

def on_return(event):
    add_task()

def add_task():
    """Adds a task entered from the input to the listbox.
        Shows a warning if the input box is empty"""
    task = txt_input.get()
     #append to the list if input is not empty
    if task !="":
        tasks.append(task)
        update_listbox()
    else:
        messagebox.showwarning("Warning","You need to enter a task")
    txt_input.delete(0,"end")
#root.bind("<Return>", add_task())
def del_all():
    """
    Deletes all listbox entries
    """
#global as we are changing the list
#the tasks list has to be updated globally
    global tasks
    if tasks != []:
        confirm = messagebox.askyesno("Confirm: Delete all","Do you want to delete all?")
        if confirm:
            tasks = []
        update_listbox()
    else:
        messagebox.showwarning("Warning","The list is empty!!")

def del_one():
    """
    Deletes selcted task from the list box.
    If no task is selected, the tasks are
    deleted in a First In First Out order
    """
    task = lb_list_box.get("active")
    if tasks != []:
        confirm = messagebox.askyesno("Confirm: Delete ","Do you want to delete?")
        if task in tasks and confirm:
            tasks.remove(task)
        update_listbox()
    else:
        messagebox.showwarning("Warning","The list is empty!!")

def sort_asc():
    tasks.sort()
    update_listbox()

def sort_dsc():
    tasks.sort()
    tasks.reverse()
    update_listbox()


def choose_random():
    """
    Chooses a task at random and displays it on the label
    """
    task = random.choice(tasks)
    lbl_display["text"] = task

def show_number_tasks():
	tasks_number = len(tasks)
	msg = f"Number of Tasks: {tasks_number}"
	lbl_display["text"] = msg

def ex():
    sys.exit()


#setup
lbl_title = tkinter.Label(root,text="To-Do List",bg="white")
lbl_title.grid(row=0,column=0)

lbl_display = tkinter.Label(root,text="",bg="white")
lbl_display.grid(row=0,column=1)

txt_input = tkinter.Entry(root,width = 15)
txt_input.bind("<Return>",on_return)
txt_input.grid(row=1,column=1)

btn_add_task = tkinter.Button(root,text="Add Task",fg="#0000ff",bg="white",command=add_task)
btn_add_task.grid(row=0,column=0)

btn_del_all = tkinter.Button(root,text="Delete All",fg="red",bg="white",command=del_all)
btn_del_all.grid(row=1,column=0)

btn_del_one = tkinter.Button(root,text="Delete",fg="red",bg="white",width=7,command=del_one)
btn_del_one.grid(row=2,column=0)

btn_sort_asc = tkinter.Button(root,text="Sort(Asc)",fg="#010101",bg="white",command=sort_asc)
btn_sort_asc.grid(row=3,column=0)

btn_sort_dsc = tkinter.Button(root,text="Sort(Dsc)",fg="#0f0f0f",bg="white",command=sort_dsc)
btn_sort_dsc.grid(row=4,column=0)

btn_choose_random = tkinter.Button(root,text="Choose random",fg="#0f0f0f",bg="white",command = choose_random)
btn_choose_random.grid(row=5,column=0)

btn_show_number_tasks = tkinter.Button(root,text="Number of Tasks",fg="#0f0f0f",bg="white",command=show_number_tasks)
btn_show_number_tasks.grid(row=6,column=0)

btn_exit = tkinter.Button(root,text="Exit",fg="green",bg="white",command=ex)
btn_exit.grid(row=7,column=0)

lb_list_box = tkinter.Listbox(root)
lb_list_box.grid(row=2,column=1,rowspan=7)


root.mainloop()
