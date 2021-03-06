import tkinter as TK
from tkinter import ttk as TTK
from database import display_records as SEL
from usefulfeatures import refresh_table as REFRESH
from IncomeOutcome import IncomeOutcome
from RemoveWindow import RemoveWindow
from FilterWindow import FilterWindow
from CalcWindow import CalcWindow

# Main Window
class Main(TK.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        
    # initializing of objects and window widgets
    def init_main(self):
        # тулбар bg - цвет фона, bb - граница 
        toolbar = TK.Frame(bg="#d7d8e0", bd=2)
        # side=TK.TOP - закрепляет тулбар в верхней части окна
        # fill=TK.X - растягивает по горизонтали
        toolbar.pack(side=TK.TOP, fill=TK.X)
    # END initializing of objects and window widgets 

# income_outcome button
        self.add_img = TK.PhotoImage(file="img/add.gif")
        btn_open_dialog = TK.Button(toolbar, text="Добавить",
                                    command=self.open_income_outcome,
                                    bg="#FFFFFF", bd=2,
                                    compound=TK.TOP,
                                    image=self.add_img)
        btn_open_dialog.pack(side=TK.LEFT)
# END income_outcome button

# remove record button
        self.remove_img = TK.PhotoImage(file="img/remove.gif")
        btn_open_remove_record = TK.Button(toolbar, text="Удалить",
                                    command=self.open_remove_record,
                                    bg="#FFFFFF", bd=2,
                                    compound=TK.TOP,
                                    image=self.remove_img)
        btn_open_remove_record.pack(side=TK.LEFT)
# END remove record button

# filter button
        self.filter_img = TK.PhotoImage(file="img/filter.gif")
        btn_open_filter = TK.Button(toolbar, text="Фильтр",
                                    command=self.open_filter,
                                    bg="#FFFFFF", bd=2,
                                    compound=TK.TOP,
                                    image=self.filter_img)
        btn_open_filter.pack(side=TK.LEFT)
# END filter button

# calc button
        self.calc_img = TK.PhotoImage(file="img/calc.gif")
        btn_open_calc = TK.Button(toolbar, text="Калькулятор",
                                    command=self.open_calc,
                                    bg="#FFFFFF", bd=2,
                                    compound=TK.TOP,
                                    image=self.calc_img)
        btn_open_calc.pack(side=TK.LEFT)
# END calc button

# refresh button
        self.add_img2 = TK.PhotoImage(file="img/refresh.gif")
        btn_refresh = TK.Button(toolbar, text="Обновить БД",
                                    command=lambda: REFRESH(self.tree),
                                    bg="#FFFFFF", bd=2,
                                    compound=TK.TOP,
                                    image=self.add_img2)
        btn_refresh.pack(side=TK.RIGHT)
# END refresh button

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

        # displaying all data in the table by calling SEL function 
        SEL(self.tree)
      
        # display table
        self.tree.pack(side=TK.BOTTOM)
# END table with records

    # функция вызова дочернего окна
    def open_income_outcome(self):
        IncomeOutcome()

    def open_remove_record(self):
        RemoveWindow()

    def open_filter(self):
        FilterWindow()

    def open_calc(self):
        CalcWindow()
# END Main Window

# if script is running as main programm the it's content will execute
# if script is imported the it's content will NOT execute
if __name__ == "__main__":
    root = TK.Tk()
    app = Main(root)
    app.pack()
    # name of the window
    root.title("Finance Holder v2.0")
    # size of the window and point where it will appear
    root.geometry("650x450+300+200")
    # turn off possibility of resize by width and height
    root.resizable(False, False)
    root.mainloop()
