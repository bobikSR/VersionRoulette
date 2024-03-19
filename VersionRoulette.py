
import tkinter as tk

from methods import roll_versions, update_overlay


def get_new_versions():
    title_str = "Rolled versions:"
    versions = roll_versions()
    versions_str = ""
    for i in versions[1:]:
        versions_str += f"\n{i}"
    label.config(text=f"{title_str}{versions_str}")
    update_overlay(versions_str)


root = tk.Tk()
root.geometry("200x200")
root.title("Version Roulette")
roll = tk.Button(root, text="Spin the roulette!", command=get_new_versions)
roll.pack(pady=(10,0))
label = tk.Label(root, text="")
label.pack()
root.mainloop()