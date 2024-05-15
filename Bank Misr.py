import tkinter as tk
from tkinter import messagebox

def calculate_loan():
    try:
        job = job_var.get()
        loan_amount = float(amount_entry.get())
        loan_years = int(years_var.get())
        
        if loan_years == 1:
            interest_rate = 13.76
        elif loan_years == 3:
            interest_rate = 14.06
        elif loan_years == 5:
            interest_rate = 14.87
        elif loan_years == 7:
            interest_rate = 15.71
        else:
            raise ValueError("Invalid number of years")
        
        total_interests = loan_amount * interest_rate / 100 * loan_years
        
        total_loan = loan_amount + total_interests
        
        monthly_payment = total_loan / (loan_years * 12)
        
        total_lon.config(text=f"Your Total Loan: L.E {total_loan}")
        result_label.config(text=f"Monthly Payment: L.E {monthly_payment:.2f}")
        total_int.config(text=f"Total Interest: L.E {total_interests}")
        fixed_interest.config(text=f"Fixed Interest:  %{interest_rate}")
        
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

def clear_fields():
    job_var.set("Programmer")
    amount_entry.delete(0, tk.END)
    years_var.set(5)
    total_lon.config(text="Your Total Loan: (L.E)  ")
    result_label.config(text="Monthly Payment: (L.E)  ")
    fixed_interest.config(text="Fixed Interest: %  ")
    total_int.config(text="Your Total Loan: (L.E)  ")

bank = tk.Tk()
bank.title("Bank Misr - Plan Your Loan Application")
bank.geometry("700x600+330+80")

# I made a comment because if the image path is not working, there will be no error for the code
# logo=tk.PhotoImage(file="Logo.Banque_Misr.png")
# logo_lable=tk.Label(bank,image=logo)
# logo_lable.pack()

welcome = tk.Label(bank, text="Welcome To Bank Misr - Plan Your Loan",pady=10,fg='brown3',font=("Arial Bold", 17))
welcome.pack()

job_label = tk.Label(bank, text="Select your job:",font=("Arial Bold",12))
job_label.pack()

job_var = tk.StringVar()
job_var.set("Programmer")
job_options = ["Programmer","Doctor","Acountant", "Engineer", "Teacher", "Other"]
job_menu = tk.OptionMenu(bank, job_var, *job_options)
job_menu.pack(pady=(0,12))

amount_label = tk.Label(bank, text="Enter Loan Amount (EGP): ",font=("Arial Bold",12))
amount_label.pack()

amount_entry = tk.Entry(bank,width=30,fg='brown3',font=("Arial Bold",13))
amount_entry.pack(pady=(0,12))

years_label = tk.Label(bank, text="Select number of years:",font=("Arial Bold",12))
years_label.pack()

years_var = tk.IntVar()
years_var.set(5)
years_options = [1, 3, 5, 7] 
years_menu = tk.OptionMenu(bank, years_var, *years_options)
years_menu.pack(pady=(0,10))

calculate_button = tk.Button(bank, text="Calculate",padx=10,background='limegreen',bd=3,pady=5 ,font=("Arial Bold",10), command=calculate_loan)
calculate_button.pack(pady=(0,10))

total_lon = tk.Label(bank, text="Your Total Loan: L.E ",bg="gray74",font=("Arial Bold",11))
total_lon.pack()

result_label = tk.Label(bank, text="Monthly Payment: L.E ",bg="gray74",font=("Arial Bold",11))
result_label.pack()

fixed_interest = tk.Label(bank, text="Fixed Interest: % ",bg="gray74",font=("Arial Bold",11))
fixed_interest.pack()

total_int = tk.Label(bank, text="Total Interest: L.E",bg="gray74",font=("Arial Bold",11))
total_int.pack()

clear_button = tk.Button(bank, text="Clear",fg="white",font=("Arial Bold",10),bg='cadetblue4', command=clear_fields,bd=3,width=10)
clear_button.pack(pady=(5,0))

exit_button = tk.Button(bank, text="Exit",width=4,bg='brown3' ,fg='white',font=("Arial Bold",10),padx=20,command=bank.destroy)
exit_button.pack(pady=(10,0))

bank.mainloop()


