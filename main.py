import tkinter as tk

class Calculator:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        
        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(self.root, textvariable=self.entry_var)
        self.entry.grid(row=0, column=0, columnspan=4)
        
        self.create_buttons()
        
    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
        ]
        
        row_num , col_num = 1, 0
        
        for button_text in buttons:
            tk.Button(self.root, text=button_text, command=lambda text=button_text: self.button_click(text)).grid(row=row_num, column=col_num)
            col_num += 1
            if col_num > 3:
                col_num = 0
                row_num += 1
                
    def button_click(self, text):
        if text == '=':
            result = eval(self.entry_var.get())
            self.entry_var.set(result)
        else:
            self.entry_var.set(self.entry_var.get() + text)
            
if __name__ == '__main__':
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()