
import tkinter as tk

from methods import roll_versions, update_overlay, hash_versions

# todo: link a very simple livesplit layout - version 1 - 5, big timer
# todo: add link to submission form + make a lb on google sheets

rolled_versions: str = ""

def get_new_versions():
    title_str = "Rolled versions:"
    versions = roll_versions()
    versions_str = ""
    for i in versions[1:]:
        versions_str += f"\n{i}"
    global rolled_versions
    rolled_versions = versions_str
    label.config(text=f"{title_str}{versions_str}")
    update_overlay(versions_str)


root = tk.Tk()
root.geometry("200x200")
root.title("Version Roulette")
roll = tk.Button(root, text="Spin the roulette!", command=get_new_versions)
roll.pack(pady=(10,0))
label = tk.Label(root, text="")
label.pack()
submit_versions = tk.Button(root, text="submit versions", command=hash_versions(rolled_versions), anchor="s")
submit_versions.pack(side="bottom", pady=(10,20))
root.mainloop()