import tkinter as TK
from tkinter import ttk as TTK
from usefulfeatures import refresh_table_by_month as REFM
from usefulfeatures import refresh_table_by_income_expense as REFIE

# FilterWindow
class FilterWindow(TK.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_filter_window()

    # initializing of objects and window widgets
    def init_filter_window(self):
        self.title("Фильтры")
        self.geometry("650x450+300+200")
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

        # Date Filter record button
        btn_FilterM = TK.Button(self, text="GO!",
                            command=lambda: REFM(
                                self.tree, self.date_combobox.get()))
        btn_FilterM.place(x=245, y=1)
        btn_FilterM.bind("<Button-1>")    
        # END Date Filter record button

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

        # Income-outcome Filter record button
        btn_FilterIO = TK.Button(self, text="GO!",
                            command=lambda: REFIE(self.tree,
                                self.income_expense_combobox.get()))
        btn_FilterIO.place(x=245, y=31)
        btn_FilterIO.bind("<Button-1>")    
        # END Income-outcome Filter record button        
        
    # END Income-outcome
    
    # Cancel button
        btn_cancel = TK.Button(self, text="Отмена",
                               command=self.destroy)
        btn_cancel.place(x=550, y=90)
    # END Cancel button
    
# table with records
        self.tree = TTK.Treeview(self, columns=("id", "current_date",
                                                "description",
                                                "income_expense",
                                                "total"),
                                 height=15, show="headings")
        self.tree.column("id", width=30, anchor=TK.CENTER)
        self.tree.column("current_date", width=150, anchor=TK.CENTER)
        self.tree.column("description", width=215, anchor=TK.CENTER)
        self.tree.column("income_expense", width=150, anchor=TK.CENTER)
        self.tree.column("total", width=100, anchor=TK.CENTER)

        # giving displayment names for columns
        self.tree.heading("id", text="id")
        self.tree.heading("current_date", text="Дата")        
        self.tree.heading("description", text="Наименование")
        self.tree.heading("income_expense", text="Доход / Расход")
        self.tree.heading("total", text="Сумма")
      
        # display table
        self.tree.pack(side=TK.BOTTOM)
# END table with records    
        
        # grabbing all events from app (???)
        self.grab_set()
        # focus on app
        self.focus_set()     
# END FilterWindow

