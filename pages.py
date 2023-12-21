import sqlite3
from flask import Flask, session, render_template, request, redirect, url_for

conn = sqlite3.connect('question.db', check_same_thread=False)
cur = conn.cursor()
conn1 = sqlite3.connect('user_data.db', check_same_thread=False)
cur1 = conn1.cursor()

def index():
    return render_template('index.html')

def signup():
    return render_template('signup.html')

def commit():
    username = request.form['signup-username']
    nama = request.form['signup-nama']
    email = request.form['signup-email']
    password = request.form['signup-password']
    sql = "INSERT INTO user_data (nama, username, email, password) VALUES (?, ?, ?, ?)"
    value = (nama, username, email, password)
    cur1.execute(sql, value)
    conn1.commit
    return redirect('/')


def tanya():
    username = request.form['login-username']
    password = request.form['login-password']
    sql = "SELECT * FROM user_data WHERE username = ? AND password = ?"
    value = (username, password)
    cur1.execute(sql, value)
    result1 = cur1.fetchall()
    if len(result1) == 0:
        return 'Username tidak ditemukan'
    else:
        nama, username, email, password = result1[0]
        cur.execute('SELECT * FROM questions')
        result2 = cur.fetchall()
        id_ku, quest1, answer = result2[0]
        id_ku, quest2, answer = result2[1]
        id_ku, quest3, answer = result2[2]
        id_ku, quest4, answer = result2[3]
        id_ku, quest5, answer = result2[4]
        id_ku, quest6, answer = result2[5]
        id_ku, quest7, answer = result2[6]
        id_ku, quest8, answer = result2[7]
        id_ku, quest9, answer = result2[8]
        id_ku, quest10, answer = result2[9]
        my_temp = render_template('question.html',  
                                  nama=nama, 
                                  quest1=quest1, 
                                  quest2=quest2, 
                                  quest3=quest3, 
                                  quest4=quest4, 
                                  quest5=quest5, 
                                  quest6=quest6, 
                                  quest7=quest7, 
                                  quest8=quest8, 
                                  quest9=quest9,
                                  quest10=quest10)
        return my_temp

def answer():
    list_ans = [
    request.form['quest1'],
    request.form['quest2'],
    request.form['quest3'],
    request.form['quest4'],
    request.form['quest5'],
    request.form['quest6'],
    request.form['quest7'],
    request.form['quest8'],
    request.form['quest9'],
    request.form['quest10']
    ]
    a = 0
    point = 0
    cur.execute('SELECT * FROM questions')
    result = cur.fetchall()
    for i in result:
        id_ku, question, answer = i
        if list_ans[a].lower() == answer.lower():
            point += 1
        else:
            point += 0
        a += 1
    my_temp = render_template('answer.html', score=str(point))
    return my_temp