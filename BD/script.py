import sqlite3 as sq

info_users = [
    (3, 'Сергей', 1, 19, 900),
    (4, 'Мария', 2, 18, 1500),
    (5, 'Александр', 1, 20, 1000)
]

with sq.connect('saper.db') as con:
    cur = con.cursor()
    # cur.execute("CREATE TABLE IF NOT EXISTS users ("
    #             "user_id INTEGER PRIMARY KEY AUTOINCREMENT,"
    #             "name TEXT NOT NULL,"
    #             "sex INTEGER NOT NULL DEFAULT 1,"
    #             "old INTEGER,"
    #             "score INTEGER)")
    # cur.executemany("INSERT INTO users VALUES(?, ?, ?, ?, ?)", info_users)
    result = cur.execute("SELECT * FROM users").fetchall()
    print('Все игроки таблицы:\n', *result)

    result = cur.execute("SELECT * FROM users where sex = 2").fetchall()
    print('Все игроки женского пола:\n', *result)

    result = cur.execute('SELECT * FROM users WHERE score < 1000').fetchall()
    print('Все игроки с результатом меньше 1000\n', *result)

    result = cur.execute("SELECT * FROM users ORDER BY score DESC").fetchone()
    print('Игрок с наилучшим результатом:\n', result)

    result = cur.execute("SELECT * FROM users WHERE old BETWEEN 18 AND 20").fetchall()
    print('Все игроки с возрастом 18-20 лет:\n', *result)
