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
        self.con = sqlite3.connect("../db_dlya_nero.db")
        self.cur = self.con.cursor()

    def create_worker(self, count, i=[1, 10], s=[1, 10], c=[1, 10], e=[1, 10]):
        for element in range(count):
            id = random.randint(1, 1000000000)
            name = random.choice(self.fname) + " " + random.choice(self.sname)
            busy = 0
            work_description = "unemployed"
            skills = {
                "i": random.randint(i[0], i[1]),
                "s": random.randint(s[0], s[1]),
                "c": random.randint(c[0], c[1]),
                "e": random.randint(e[0], e[1])
            }

            self.cur.execute("INSERT INTO "
                                 "users (Id, Name, Strength, Endurance, Intelligence, Charisma) "
                                 "VALUES (?, ?, ?, ?, ?, ?)",
                                 (id, name, skills['s'], skills['e'], skills['i'], skills['c']))
            self.cur.execute("INSERT INTO "
                             "users_zanyatost (Id, Busy, Work_description) "
                             "VALUES (?, ?, ?)",
                             (id, busy, work_description))
            self.con.commit()

    def delete_worker(self):
        self.cur.execute("DELETE FROM users WHERE id > 0")
        self.cur.execute("DELETE FROM users_zanyatost WHERE id > 0")
        self.con.commit()
