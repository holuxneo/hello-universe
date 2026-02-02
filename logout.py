import tkinter as tk
from tkinter import messagebox

def logout():
    """Handle logout functionality"""
    response = messagebox.askyesno("Logout", "Are you sure you want to logout?")
    if response:
        messagebox.showinfo("Logout", "You have been logged out successfully! go home!")
        root.destroy()

# Create main window
root = tk.Tk()
root.title("Logout")
root.geometry("300x150")
root.configure(bg='lightgray')

# Create label
label = tk.Label(root, text="User Session", font=("Arial", 14), bg='lightgray')
label.pack(pady=20)

# Create logout button
logout_button = tk.Button(root, text="Logout", command=logout, bg='red', fg='white', 
                          font=("Arial", 12), padx=20, pady=10, cursor="hand2")
logout_button.pack(pady=20)

if __name__ == "__main__":
    root.mainloop()
