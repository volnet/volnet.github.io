import sqlite3

conn = sqlite3.connect('coachdata.sqlite')
cursor = conn.cursor()

import glob
import athletemodel

data_files = glob.glob('../data/*.txt')
athletes = athletemodel.put_to_store(data_files)

for each_ath in athletes:
    name = athletes[each_ath].name
    dob = athletes[each_ath].dob

    cursor.execute("INSERT INTO athletes (name, dob) VALUES (?, ?)", (name, dob))
    conn.commit()

conn.close()