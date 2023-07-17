import sqlite3

class Data:
    def __init__(self, name):
        self.conn = sqlite3.connect('name.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1 (id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER)''')

    def process_arguments(self, *args):
        if len(args) == 1:
            first_arg = args[0]
            value = 3
            self.cursor.execute('''INSERT INTO tab_1 (col_1) VALUES (?)''', (value, ))
            self.conn.commit()
        elif len(args) == 2:
            second_arg = args[1]
            if isinstance(second_arg, int):
                self.cursor.execute('''DELETE FROM tab_1 WHERE id = 1''') # удаляет 1 строку, limit выводит указанное кол-во строк из таблицы
                self.conn.commit()
        elif len(args) == 3:
            third_arg = args[2]
            if isinstance(third_arg, int):
                self.cursor.execute('''UPDATE tab_1 SET col_1 = (?) WHERE id = 3''', (77,))
                self.conn.commit()
        

    def output(self, *args):
        self.cursor.execute(''' SELECT col_1 FROM tab_1''')
        oo = self.cursor.fetchall()
        return oo


data = Data("name.db")

for i in range(3):
    data.process_arguments(1) # добавляет три записи  в базу данных  
print(data.output())


data.process_arguments(1, 2, "string")   # Не обновит запись, так как третий аргумент не является числом
print(data.output())

data.process_arguments(1, "string", 3) # перезапишет третью запись (3 -> 77)
print(data.output())

data.process_arguments(1, 2)      # Удалит первую запись
print(data.output())


