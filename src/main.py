import tkinter as tk
from polygon_editor import PolygonEditor

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Polygon Editor")
    app = PolygonEditor(root)
    root.mainloop()