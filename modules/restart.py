import tkinter as tk
from tkinter import messagebox
import subprocess

def main():
    root = tk.Tk()
    root.withdraw()  # hide main window

    if messagebox.askyesno("Restart Mac", "Are you sure you want to restart your Mac?"):
        try:
            # This command will require your password in a prompt
            subprocess.run(["sudo", "shutdown", "-r", "now"])
        except Exception as e:
            messagebox.showerror("Error", f"Failed to restart: {e}")
    else:
        messagebox.showinfo("Cancelled", "Restart cancelled.")

if __name__ == "__main__":
    main()
