import tkinter as tk
from tkinter import filedialog
import os
import subprocess
import shutil

def repair_rootfs():
    file_path = file_entry.get()
    if not os.path.exists(file_path):
        result_label.config(text="No file selected.")
        return

    try:
        subprocess.check_output(["mkfs.cramfs", "-F", file_path])
        result_label.config(text="Repair successful.")
        new_file_path = os.path.splitext(file_path)[0] + "_repaired.cramfs"
        shutil.copy(file_path, new_file_path)
        result_label.config(text="File repaired: {}".format(new_file_path))
    except subprocess.CalledProcessError:
        result_label.config(text="Error: Failed to repair file.")

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("RootFS Files", "*.cramfs")])
    file_entry.delete(0, tk.END)
    file_entry.insert(tk.END, file_path)

root = tk.Tk()
root.title("Repair RootFS by Dragon-Noir 2023")
root.geometry("400x200")

frame = tk.Frame(root, borderwidth=2, relief="groove")
frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

file_label = tk.Label(frame, text="Choose RootFS:")
file_label.pack(pady=10)

file_entry = tk.Entry(frame, width=40)
file_entry.pack()

browse_button = tk.Button(frame, text="Browse", command=browse_file)
browse_button.pack(pady=10)

repair_button = tk.Button(frame, text="Repair", command=repair_rootfs)
repair_button.pack(pady=10)

result_label = tk.Label(frame, text="")
result_label.pack(pady=10)

root.mainloop()
