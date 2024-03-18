import random
import tkinter as tk

# todo: link a very simple livesplit layout - version 1 - 5, big timer
# make that a button
# todo: add link to submission form + make a lb on google sheets



version_list = ["1.0", "1.1", "1.2", "1.3", "1.4", "1.5", "1.6", "1.7", "1.8", "1.9", "1.10",
                "1.11", "1.12", "1.13", "1.14", "1.15", "1.16", "1.17", "1.18", "1.19", "1.19",
                "1.20"]


def roll_versions() -> list[str]:
    possible_versions = version_list.copy()
    rolled_versions = [str]
    for i in range(5):
        version = possible_versions[random.randint(1, len(possible_versions) - 1)]
        rolled_versions.append(version)
        possible_versions.remove(version)
    return rolled_versions


def get_versions():
    string = "Rolled versions:"
    versions = roll_versions()
    for i in versions[1:]:
        string += f"\n{i}"
    label.config(text=string)


root = tk.Tk()
root.geometry("200x250")
root.title("Version Roulette")
roll = tk.Button(root, text="Spin the roulette!", command=get_versions)
roll.pack()
label = tk.Label(root, text="")
label.pack()
root.mainloop()