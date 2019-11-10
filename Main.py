# -*- coding: utf-8 -*-

import tkinter as tk
from Application import Application


def main():
    window = tk.Tk()
    app = Application(master=window)
    app.mainloop()


if __name__ == "__main__":
    main()
