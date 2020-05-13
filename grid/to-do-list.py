import tkinter
from tkinter import messagebox 
import random
#root
root = tkinter.Tk()
#Change root bacground color
root.configure(bg="white")

#change the title
root.title("To-Do List")
#change the root size
root.geometry("250x250")

tasks = []

#for testing
#tasks = ["a","b","c","f","e"]

#Functions
def update_listbox():
	clear_listbox()
	for task in tasks:
		lb_list_box.insert("end",task)

def clear_listbox():
	lb_list_box.delete(0,"end")

def add_task():
	task = txt_input.get()
	#append to the list if input is not empty
	if task !="":
		tasks.append(task)
		update_listbox()
	else:
		messagebox.showwarning("Warning","You need to enter a task")
	txt_input.delete(0,"end")

def del_all():
#global as we are changing the list
#the tasks list has to be updated globally
	global tasks
	confirm = messagebox.askyesno("Confirm: Delete all","Do you want to delete all?")
	if confirm:	
		tasks = []
	update_listbox()

def del_one():
	task = lb_list_box.get("active")
	confirm = messagebox.askyesno("Confirm: Delete ","Do you want to delete?")
	if task in tasks and confirm:
		tasks.remove(task)
	update_listbox()

def sort_asc():
	tasks.sort()
	update_listbox()

def sort_dsc():
	tasks.sort()
	task.reverse()

def choose_random():
	task = random.choice(tasks)
	lbl_display["text"] = task

def show_number_tasks():
	tasks_number = len(tasks)
	msg = f"Number of Tasks: {tasks_number}"
	lbl_display["text"] = msg


#setup
lbl_title = tkinter.Label(root,text="To-Do List",bg="white")
lbl_title.grid(row=0,column=0)

lbl_display = tkinter.Label(root,text="",bg="white")	
lbl_display.grid(row=0,column=1)

txt_input = tkinter.Entry(root,width = 15)
txt_input.grid(row=1,column=1)

btn_add_task = tkinter.Button(root,text="Add Task",fg="green",bg="white",command=add_task)
btn_add_task.grid(row=0,column=0)

btn_del_all = tkinter.Button(root,text="Delete All",fg="green",bg="white",command=del_all)
btn_del_all.grid(row=1,column=0)

btn_del_one = tkinter.Button(root,text="Delete",fg="green",bg="white",command=del_one)
btn_del_one.grid(row=2,column=0)

btn_sort_asc = tkinter.Button(root,text="Sort(Asc)",fg="green",bg="white",command=sort_asc)
btn_sort_asc.grid(row=3,column=0)

btn_sort_dsc = tkinter.Button(root,text="Sort(Dsc)",fg="green",bg="white",command=sort_dsc)
btn_sort_dsc.grid(row=4,column=0)

btn_choose_random = tkinter.Button(root,text="Choose random",fg="green",bg="white",command = choose_random)
btn_choose_random.grid(row=5,column=0)

btn_show_number_tasks = tkinter.Button(root,text="Number of Tasks",fg="green",bg="white",command=show_number_tasks)
btn_show_number_tasks.grid(row=6,column=0)

btn_exit = tkinter.Button(root,text="Exit",fg="green",bg="white",command=exit)
btn_exit.grid(row=7,column=0)

lb_list_box = tkinter.Listbox(root)
lb_list_box.grid(row=2,column=1,rowspan=7)

root.mainloop()

