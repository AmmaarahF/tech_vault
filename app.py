import tkinter as tk

class InvalidInputError(Exception):
    pass

class Bank:
    def __init__(self):
        self.balance = 0
        self.transaction_log = []

    def check_balance(self):
        # Update label text to display current balance
        balance_label.config(text=f"Current Balance: R{self.balance}")

    def make_deposit(self, amount):
        try:
            amount = float(amount)
            if amount <= 0:
                raise InvalidInputError("Invalid deposit amount.")
            self.balance += amount
            self.transaction_log.append(f"Deposit: +R{amount}")
            result_label.config(text="Deposit successful.")
            self.check_balance()
        except ValueError:
            result_label.config(text="Invalid input for deposit amount.")
        except InvalidInputError as e:
            result_label.config(text=str(e))

    def make_withdrawal(self, amount):
        try:
            amount = float(amount)
            if amount <= 0 or amount > self.balance:
                raise InvalidInputError("Invalid withdrawal amount.")
            self.balance -= amount
            self.transaction_log.append(f"Withdrawal: -R{amount}")
            result_label.config(text="Withdrawal successful.")
            self.check_balance()
        except ValueError:
            result_label.config(text="Invalid input for withdrawal amount.")
        except InvalidInputError as e:
            result_label.config(text=str(e))

def open_deposit_window():
    deposit_window = tk.Toplevel(root)
    deposit_window.title("Deposit")
    deposit_window.geometry("300x150")
    deposit_window.configure(bg="white")

    amount_label = tk.Label(deposit_window, text="Enter deposit amount:", bg="white")
    amount_label.pack()

    deposit_entry = tk.Entry(deposit_window)
    deposit_entry.pack()

    deposit_button = tk.Button(deposit_window, text="Deposit", command=lambda: bank.make_deposit(deposit_entry.get()))
    deposit_button.pack()

def open_withdrawal_window():
    withdrawal_window = tk.Toplevel(root)
    withdrawal_window.title("Withdrawal")
    withdrawal_window.geometry("300x150")
    withdrawal_window.configure(bg="white")


    amount_label = tk.Label(withdrawal_window, text="Enter withdrawal amount:", bg="white")
    amount_label.pack()

    withdrawal_entry = tk.Entry(withdrawal_window)
    withdrawal_entry.pack()

    withdrawal_button = tk.Button(withdrawal_window, text="Withdraw", command=lambda: bank.make_withdrawal(withdrawal_entry.get()))
    withdrawal_button.pack()

root = tk.Tk()
root.title("TechVault")

label = tk.Label(root, text="Transaction or Withdrawal")
label.pack(padx = 20, pady=20)

bank = Bank()

transaction_label = tk.Label(root, text="Select transaction:")
transaction_label.pack()
root.geometry("300x300")

deposit_button = tk.Button(root, text="Deposit", command=open_deposit_window)
deposit_button.pack(padx=20, pady=20)

withdrawal_button = tk.Button(root, text="Withdrawal", command=open_withdrawal_window)
withdrawal_button.pack(padx=20, pady=20)

result_label = tk.Label(root, text="")
result_label.pack()

balance_label = tk.Label(root, text="")
balance_label.pack()

root.mainloop()
