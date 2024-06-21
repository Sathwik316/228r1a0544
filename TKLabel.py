import tkinter as tk
import _mysql_connector



def submit_info():
    name = entry_name.get()
    roll = entry_roll.get()
    record_submitted = False
    date = entry_date.get()


    print(f"Name: {name}")
    print(f"Roll: {roll}")
    print(f"Record submitted: {record_submitted}")
    print(f"Date: {date}")
    def sign_in()       :
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error', 'Enter all fields')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='sathwik@2004', database='customerdata')
            cur = con.cursor()
        except:
            messagebox.showerror('Error', 'Error in database connection')
            return
window = tk.Tk()
window.title("Student Information System")

label_name = tk.Label(window, text="Name")
label_name.grid(row=0, column=0)

entry_name = tk.Entry(window)
entry_name.grid(row=0, column=1)

label_roll = tk.Label(window, text="Roll")
label_roll.grid(row=1, column=0)

entry_roll = tk.Entry(window)
entry_roll.grid(row=1, column=1)

label_record_submitted = tk.Label(window, text="Record submitted")
label_record_submitted.grid(row=2, column=0)

entry_record_submitted = tk.Entry(window)
entry_record_submitted.grid(row=2, column=1)

label_date = tk.Label(window, text="Date")
label_date.grid(row=3, column=0)

entry_date = tk.Entry(window)
entry_date.grid(row=3, column=1)

button_submit = tk.Button(window, text="Submit", command=submit_info)
button_submit.grid(row=4, column=0, columnspan=2)

window.mainloop()