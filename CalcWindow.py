import tkinter as TK
from tkinter import ttk as TTK

# CalcWindow
class CalcWindow(TK.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_calc_window()

    # initializing of objects and window widgets
    def init_calc_window(self):
        self.title("Калькулятор")
        self.geometry("400x220+400+300")
        self.resizable(False, False)
    # END initializing of objects and window widgets        
        
    # Date
        # Date drop-down menu
        months = ["01", "02", "03", "04", "05", "06", "07", "08",
                  "09", "10", "11", "12"]
        self.date_combobox = TTK.Combobox(self, values=months)
        self.date_combobox.current(0)
        self.date_combobox.place(x=95, y=5)
        label_date_combobox = TK.Label(self, text="Месяц")
        label_date_combobox.place(x=5, y=5)
        # END Date drop-down menu

        # Date Calc record button
        btn_CalcM = TK.Button(self, text="GO!",
                            command=lambda: REFM(
                                self.tree, self.date_combobox.get()))
        btn_CalcM.place(x=245, y=1)
        btn_CalcM.bind("<Button-1>")    
        # END Date Calc record button

    # END Date

    # Income-outcome
        # drop-down income_expense menu
        self.income_expense_combobox = TTK.Combobox(
            self, values=["Доход","Расход"])
        self.income_expense_combobox.current(0)
        self.income_expense_combobox.place(x=95, y=35)
        label_income_expense_combobox = TK.Label(self,
                                                 text="Доход/Расход")
        label_income_expense_combobox.place(x=5, y=35)
        # END drop-down income_expense menu

        # Income-outcome Calc record button
        btn_CalcIO = TK.Button(self, text="GO!",
                            command=lambda: REFIE(self.tree,
                                self.income_expense_combobox.get()))
        btn_CalcIO.place(x=245, y=31)
        btn_CalcIO.bind("<Button-1>")    
        # END Income-outcome Calc record button        
        
    # END Income-outcome
    
    # Cancel button
        btn_cancel = TK.Button(self, text="Отмена",
                               command=self.destroy)
        btn_cancel.place(x=550, y=90)
    # END Cancel button
    
        # grabbing all events from app (???)
        self.grab_set()
        # focus on app
        self.focus_set()     
# END CalcWindow

