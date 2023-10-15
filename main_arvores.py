import tkinter as tk
from tkinter import ttk
from arvores import Tree
from arvores import Node
import matplotlib.pyplot as plt

VALID_ARVORES = [
    "Pequeno", "Medio", "Grande"
]

# Define a global variable for the image
image = None

class ArvoreWidget(ttk.Widget):
    def __init__(self, master, **kw):
        super().__init__(master, "ttk::frame", kw)
        self.from_label =  ttk.Label(self, text="Criar uma árvore:")
        self.from_label.pack()
        self.from_box = ttk.Combobox(self, values=VALID_ARVORES)
        self.from_box.pack()

    def get(self):
        tamanho = self.from_box.get()

        if tamanho == 'Pequeno':
            tree= Tree()
            tree, root = tree.random_tree(4)
            return tree, root
        elif tamanho == 'Medio':
            tree= Tree()
            tree, root = tree.random_tree(8)
            return tree, root
        elif tamanho == 'Grande':
            tree= Tree()
            tree, root = tree.random_tree(32)
            return tree, root
        else:
            pass

def plotar():
    global image  # Use the global image variable
    tree, root = arvore_widget.get()
    arvore = tree.plot_tree(root)
    plt.savefig("arvore.png")

    # Display the image on the canvas
    canvas.delete("all")  # Clear previous drawings
    image = tk.PhotoImage(file="arvore.png")
    canvas.create_image(0, 0, anchor=tk.NW, image=image)
    label.config(image=image)  # Update the label with the new image

def main():
    global arvore_widget, canvas, label  # Make them global so that other functions can access them

    window = tk.Tk()
    window.title("Tkinter Image Display")

    mainframe = ttk.Frame(window, padding=32)
    mainframe.pack()

    arvore_widget = ArvoreWidget(mainframe)
    arvore_widget.pack()

    button = ttk.Button(mainframe, text="Plotar", command=plotar)
    button.pack()

    # Create a Canvas widget to display the plot
    canvas = tk.Canvas(mainframe, width=800, height=800)
    canvas.pack()

    # Create a Label to display the image
    label = ttk.Label(mainframe)
    label.pack()

    window.mainloop()
    print("Acabou soncronizado")

if __name__ == '__main__':
    main()
