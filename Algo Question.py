import sqlite3

conn = sqlite3.connect('question.db')

cur = conn.cursor()

#id = 9

# cur.execute('CREATE TABLE questions (id INT(255), quest TEXT, answer VARCHAR(255))')

# while True:
#     nomor = int(input('Masukkan quiz id: '))
#     quest = input('Masukkan pertanyaan: ')
#     ans = input('Masukkan jawaban: ')
#     sure = input('Apa kamu yakin? y = ya, t = tidak, e = exit: ')
#     if sure == 'y':
#         sql = "INSERT INTO questions (id, quest, answer) VALUES (?, ?, ?)"
#         value = (nomor, quest, ans)
#         cur.execute(sql, value)
#         conn.commit()
#         print('Quest sudah dmasukkan!')
#     elif sure == 'e':
#         break
#     else:
#         pass

cur.execute("SELECT * FROM questions")
result = cur.fetchall()
for i in result:
    id_ku, question, answer = i
    print("id: ", id_ku)
    print("question: ", question)
    print("answer: ", answer)
    print("=====================")