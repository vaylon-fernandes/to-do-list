import tkinter
from tkinter import messagebox
from sys import exit
import random
import sqlite3 as sq
#root
root = tkinter.Tk()
#Change root bacground color
root.configure(bg="#f0f0f0")

#change the title
root.title("To-Do List")
#change the root size
root.geometry("200x500")

tasks = []

#for testing
#tasks = ["a","b","c","f","e"]

#sql setup 
conn = sq.connect('todo.db')
cur = conn.cursor()

#create a table in the datbase
cur.execute("CREATE TABLE IF NOT EXISTS tasks (task text)")
#Functions
def update_listbox():
	"""
    Clears the listbox and 
    then updates the listbox
    """
	clear_listbox()
	for task in tasks:
		lb_list_box.insert("end",task)
	conn.commit()
def clear_listbox():
	'''Clears the listbox'''
	lb_list_box.delete(0,"end")

def add_task():
    """Adds a task entered from the input field to the listbox.
    Also appends the task to the list.
    Shows a warning if the input box is empty"""
     
    task = txt_input.get() 
    
     #append to the list if input field is not empty
    if task !="":
        tasks.append(task)
        cur.execute('INSERT INTO tasks values(?)',(task,))
        conn.commit()
        update_listbox()
    else:
        messagebox.showwarning("Warning","You need to enter a task")

    #clear the input field
    txt_input.delete(0,"end")

def on_return(event):
    '''Calls the add_task() function
    when the "Enter" key is pressed
    in the Entry widget'''
    add_task()

def del_all():
    """
    Deletes all listbox entries.
    Shows warning if list is empty.
    """
    #global as we are changing the list
    #the tasks list has to be updated globally
    global tasks
    
    if tasks != []:
        confirm = messagebox.askyesno("Confirm: Delete all","Do you want to delete all?")
        if confirm:
            tasks = []

            cur.execute("DELETE FROM tasks")
            conn.commit()
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
            cur.execute('DELETE FROM tasks where task is (?)',(task,))
            conn.commit()
            update_listbox()
    else:
        messagebox.showwarning("Warning","The list is empty!!")


def choose_random():
    """
    Chooses a task at random and displays it on the label
    """
    task = random.choice(tasks)
    lbl_display["text"] = task

def show_number_tasks():
    '''Displays the number of tasks 
    currently present in the listbox '''
    tasks_number = len(tasks)
    msg = f"Number of Tasks: {tasks_number}"
    lbl_display["text"] = msg

def ex():
    '''Asks the user if they would like to 
    leave the app. If true closes the app.'''
    confirm = messagebox.askyesno("Exit","Do you want to exit")
    if confirm:
        exit()
    
def reload_data():
    '''Retrieves tasks from the database 
    if it is not empty and displays them 
    in the listbox'''
    global tasks
    tasks = []
    for data in cur.execute('SELECT task from tasks'):
        tasks.append(data)
    update_listbox()

#setup
lbl_title = tkinter.Label(root,text="To-Do List",bg="white")
lbl_title.pack()

lbl_display = tkinter.Label(root,text="",bg="white")	
lbl_display.pack()

txt_input = tkinter.Entry(root,width = 15)
txt_input.bind("<Return>",on_return)
txt_input.pack()

btn_add_task = tkinter.Button(root,text="Add Task",fg="green",bg="white",command=add_task)
btn_add_task.pack()

btn_del_all = tkinter.Button(root,text="Delete All",fg="red",bg="white",command=del_all)
btn_del_all.pack()

btn_del_one = tkinter.Button(root,text="Delete",fg="red",bg="white",command=del_one)
btn_del_one.pack()


btn_choose_random = tkinter.Button(root,text="Choose random",fg="blue",bg="white",command = choose_random)
btn_choose_random.pack()

btn_show_number_tasks = tkinter.Button(root,text="Number of Tasks",fg="blue",bg="white",command=show_number_tasks)
btn_show_number_tasks.pack()

btn_exit = tkinter.Button(root,text="Exit",fg="black",bg="white",command=ex)
btn_exit.pack()

lb_list_box = tkinter.Listbox(root)
lb_list_box.pack()

#retrieving data from the database
reload_data()
update_listbox()

root.mainloop()


#close database connection
conn.close()