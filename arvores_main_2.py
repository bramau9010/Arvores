import tkinter as tk
from tkinter import ttk


from arvores import Tree
from arvores import Node

VALID_ARVORES = [
    "Pequeno", "Medio", "Grande"
]

class ArvoreWidget(ttk.Widget):
    def __init__(self, master, **kw):
        super().__init__(master, "ttk::frame", kw)

        self.from_label =  ttk.Label(self, text="Criar uma árvore:")
        self.from_label.pack()
        self.from_box = ttk.Combobox(self, values=VALID_ARVORES)
        self.from_box.pack()


    def get(self):
        # pega o valor do Entry
        
        tamanho = self.from_box.get()

        if tamanho == 'Pequeno':
            tree= Tree()
            tree,root = tree.random_tree(4)           

            return tree,root
        elif tamanho == 'Medio':
            tree= Tree()
            tree,root = tree.random_tree(8)           

            return tree,root
        elif tamanho == 'Grande':
            tree= Tree()
            tree,root = tree.random_tree(12)           

            return tree,root
        else:
            pass
        

def main():

    def plotar():
        # TODO: fazer voltar a funcionar
        tree,root = arvore_widget.get()
        arvore = tree.plot_tree(root)
        # Draw the plot on the canvas
        canvas.delete("all")  # Clear previous drawings
        canvas.create_image(0, 0, anchor=tk.NW, image=arvore)
        

    window = tk.Tk()

    mainframe = ttk.Frame(window, padding=32)
    mainframe.pack()

    arvore_widget = ArvoreWidget(mainframe)
    arvore_widget.pack()

    button = ttk.Button(mainframe, text="Plotar", command=plotar)
    button.pack()

    # Create a Canvas widget to display the plot
    canvas = tk.Canvas(mainframe, width=400, height=400)
    canvas.pack()

    

    window.mainloop()
    print("Acabou soncronizado")
    
    

if __name__ == '__main__':
    main()
