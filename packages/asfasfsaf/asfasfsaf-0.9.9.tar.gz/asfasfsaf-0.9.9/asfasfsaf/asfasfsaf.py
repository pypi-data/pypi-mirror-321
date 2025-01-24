import psycopg2
from psycopg.generators import execute
from tkinter import ttk
import tkinter as tk
def con(x):
    connection = psycopg2.connect(
        dbname="Sanatorium",
        user="postgres",
        password="pg123",
        host="localhost",
        port="5432"
    )
    cursor = connection.cursor()
    cursor.execute(x)
    results = cursor.fetchall()
    return results
def function_selection(selected_value, info_window):
    print(selected_value)

    columns_heads = con(f"SELECT column_name FROM information_schema.columns WHERE table_name = \'{selected_value}\'")
    res = con(f"SELECT * FROM public.\"{selected_value}\"")
    columns_heads_list = [f'{column[0]}' for column in columns_heads]  # Кавычки вокруг каждого имени колонки
    tree = ttk.Treeview(info_window, columns=columns_heads_list, show='headings')
    for item in tree.get_children():
        tree.delete(item)

        # Перебираем результат и добавляем строки в treeview
    for row in res:
        tree.insert("", tk.END, values=row)
    # Создаем заголовки для столбцов
    for col in columns_heads_list:
        tree.heading(col, text=col)
        tree.column(col, stretch=True)

    tree.pack(fill=tk.BOTH, expand=True)