import tkinter as TK
import time
import datetime
from database import data_insert as INS
from database import display_records as SEL
from database import data_remove as REM
from database import display_records_by_month as SELBYM
from database import display_records_by_income_expense as SELBYIE


# refresh records in the table - first DELETE all records then ADD
# then back by SELECTing * records FROM finances TABLE
def refresh_table(tree):
    x = tree.get_children()
    for child in x:
        tree.delete(child)
    SEL(tree)

# getting values from fields, sending them to finances TABLE and
# clearing fields
def get_values_send_and_clear(description, income_expense, total, entry_description, entry_money):
    current_date = current_date_plus_time()
    INS(current_date, description.get(), income_expense, total.get())
    entry_description.delete(0, 'end')
    entry_money.delete(0, 'end')

# getting id from fields, deleting them from finances TABLE and
# clearing fields
def get_values_remove_and_clear(idd, entry_idd):
    REM(idd.get())
    entry_idd.delete(0, 'end')

#def get_month_and_display(tree, month):
    
def refresh_table_by_month(tree, value):
    x = tree.get_children()
    for child in x:
        tree.delete(child)
    SELBYM(tree, value)

def refresh_table_by_income_expense(tree, value):
    x = tree.get_children()
    for child in x:
        tree.delete(child)
    SELBYIE(tree, value)     

def current_date_plus_time():
    current_time = time.time()
    date = str(datetime.datetime.fromtimestamp(current_time).strftime('%Y-%B-%d %H:%M:%S'))
    return date

    
    
    
