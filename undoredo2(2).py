class TextEditor:
    def __init__(self):
        self.undo_stack = []  
        self.redo_stack = []
        self.document = ""    

    def make_change(self, new_text):
        
        self.undo_stack.append(self.document)
        
        self.redo_stack.clear()
      
        self.document = new_text
        print(f"Change done: {self.document}")

    def undo(self):
        if not self.undo_stack:
            print("Nothing to undo")
            return
     
        self.redo_stack.append(self.document)
       
        self.document = self.undo_stack.pop()
        print(f"Undo has Done . Current document: {self.document}")

    def redo(self):
        if not self.redo_stack:
            print("Nothing to redo")
            return
     
        self.undo_stack.append(self.document)
        
        self.document = self.redo_stack.pop()
        print(f"Redo has Done. Current document: {self.document}")

    def display(self):
        print(f"Current document is :\n{self.document}")

if __name__ == "__main__":
    editor = TextEditor()

    editor.make_change("Hii")
    editor.make_change("Hii, World!")
    editor.make_change("Hii, World! nice to see you ")

    editor.display()  

    editor.undo()   
    editor.display()

    editor.undo()    
    editor.display()

    editor.redo()     
    editor.display()

    editor.redo()   
    editor.display()

    editor.undo()
    editor.make_change("Hii, World! nice to see you")
    editor.display()
    editor.redo()  