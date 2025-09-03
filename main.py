import tkinter as tk
from sistema_principal import SistemaPrincipal

def main():
    root = tk.Tk()
    app = SistemaPrincipal(root)
    root.eval('tk::PlaceWindow . center')
    root.mainloop()

if __name__ == "__main__":
    main()