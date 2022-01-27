import sqlite3
def reg_user(id):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(""" CREATE TABLE IF NOT EXISTS user_time (
        id,
        status,
        privat_or_intim
        ) """)
    db.commit()
    sql.execute(f"SELECT id FROM user_time WHERE id ={id}")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO user_time VALUES (?,?,?)", (id,0,'0'))
        db.commit()


    sql.execute(""" CREATE TABLE IF NOT EXISTS status_bot (
            lol,
            privat
            ) """)
    db.commit()
    sql.execute(f"SELECT privat FROM status_bot")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO status_bot VALUES (?,?)", ('gav','0'))
        db.commit()


    sql.execute(""" CREATE TABLE IF NOT EXISTS black_list (
                lol,
                id
                ) """)
    db.commit()






def members_list():
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    a = sql.execute(f'SELECT COUNT(*) FROM user_time').fetchone()[0]
    return a



def change_bot(num):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(f"UPDATE status_bot SET privat = '{num}'")
    db.commit()

def cheack_status():
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    return sql.execute(f"SELECT privat FROM status_bot").fetchone()

def black(id):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(f"INSERT INTO black_list VALUES (?,?)", ('gav', id))
    db.commit()


def cheack_black():
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    return sql.execute(f"SELECT id FROM black_list").fetchall()