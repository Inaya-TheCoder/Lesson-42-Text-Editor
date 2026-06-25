from tkinter import *

def calculate():
    p = float(principal_entry.get())
    r = float(rate_entry.get())
    t = float(time_entry.get())

    si = (p * r * t) / 100

    amount = p * ((1 + r/100) ** t)
    ci = amount - p

    si_label.config(text=f"Simple Interest = {si:.2f}")
    ci_label.config(text=f"Compound Interest = {ci:.2f}")

root = Tk()
root.title("Interest Calculator")
root.geometry("350x300")

Label(root, text="Principal Amount").pack(pady=5)
principal_entry = Entry(root)
principal_entry.pack(pady=5)

Label(root, text="Rate of Interest (%)").pack(pady=5)
rate_entry = Entry(root)
rate_entry.pack(pady=5)

Label(root, text="Time Period (Years)").pack(pady=5)
time_entry = Entry(root)
time_entry.pack(pady=5)

Button(root, text="Calculate", command=calculate).pack(pady=10)

si_label = Label(root, text="")
si_label.pack(pady=5)

ci_label = Label(root, text="")
ci_label.pack(pady=5)

root.mainloop()