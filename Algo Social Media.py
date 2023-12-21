import sqlite3

conn1 = sqlite3.connect('user_data.db')
conn2 = sqlite3.connect('user_content.db')

cur1 = conn1.cursor()
cur2 = conn2.cursor()

# cur1.execute('CREATE TABLE user_data (nama VARCHAR(255), username VARCHAR(255), email VARCHAR(255), password VARCHAR(255))')
# cur2.execute('CREATE TABLE user_content (username VARCHAR(255), content TEXT, like INT)')

while True:
    mode = input('Apa yang anda inginkan? daftar atau masuk (s untuk stop)?\n>> ')
    if mode == 'daftar':
        nama = input('Masukkan namamu: ')
        username = input('Masukkan nama usernamemu: ')
        email = input('Masukkan E-Mailmu: ')
        password = input('Masukkan Passwordmu: ')
        confirm_pass = input('Masukkan ulang passwordmu: ')
        if password == confirm_pass:
            sql = "INSERT INTO user_data (nama, username, email, password) VALUES (?, ?, ?, ?)"
            value = (nama, username, email, password)
            cur1.execute(sql, value)
            conn1.commit()
        else:
            print("password tidak sama")

    elif mode == "test":
        cur1.execute("SELECT * FROM user_data")
        result = cur1.fetchall()
        print(result)
    
    elif mode == "masuk":
        username = input("Masukkan usernamemu: ")
        password = input('Masukkan passwordmu: ')
        sql = "SELECT * FROM user_data WHERE username = ? AND password = ?"
        value = (username, password)
        cur1.execute(sql, value)
        result = cur1.fetchall()
        # print(result)
        for baris in result:
            nama, username, email, password = baris
            print("Selamat datang kembali", nama)

    elif mode == "s":
        print("Sampai jumpa lagi")
        break

