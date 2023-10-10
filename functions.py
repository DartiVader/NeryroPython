import sqlite3


connection = sqlite3.connect('db_glagoli.db')
cursor = connection.cursor()


def add_new_verb(glag, sr_spec):
    cursor.execute(f"SELECT * FROM glagolnew WHERE Glag ='{glag}'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO glagolnew VALUES (?, ?, ?, ?, ?, ?)", (1, glag, sr_spec[0], sr_spec[1], sr_spec[2], sr_spec[3],))
        connection.commit()
    else:
        string = cursor.fetchall()
        vhodi = string[0] + 1
        cursor.execute('''UPDATE glagolnew SET vhod = ? WHERE Glag = ?''', (vhodi, glag))

    '''
    поиск glag (строка с глаголом) в новой табллице
    если нашли измененяем характеристики и увеличиваем колво вхождений слова в в таблицу на 1
        если колво вхождений стало == n (n обговорим), то добавляем глагол и его характеристики в старую таблицу, а из этой убираем
    если не нашли то добавляем в таблицу глагол характеристики и 1 как колво вхождений

    '''
    pass
