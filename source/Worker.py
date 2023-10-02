'''
i -- intelligence
s -- Strength
c -- charisma
e -- endurance
'''

import random
import sqlite3


class Worker:
    def __init__(self):
        self.fname = open("./namelist/fname.txt").read().split()
        self.sname = open("./namelist/sname.txt").read().split()

    def create_worker(self, count, i=[1, 10], s=[1, 10], c=[1, 10], e=[1, 10]):
        con = self.connect_base()
        for element in range(count):
            id = random.randint(1, 1000000000)
            name = random.choice(self.fname) + " " + random.choice(self.sname)
            skills = {
                "i": random.randint(i[0], i[1]),
                "s": random.randint(s[0], s[1]),
                "c": random.randint(c[0], c[1]),
                "e": random.randint(e[0], e[1])
            }

            con.cursor().execute("INSERT INTO "
                                 "users (Id, Name, Strength, Endurance, Intelligence, Charisma) "
                                 "VALUES (?, ?, ?, ?, ?, ?)",
                                 (id, name, skills['s'], skills['e'], skills['i'], skills['c']))
            con.commit()

    def connect_base(self):
        return sqlite3.connect("../db_dlya_nero.db")
