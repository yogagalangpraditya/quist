from flask import Flask, session, redirect, url_for
from pages import *

app = Flask(__name__, template_folder='template') #newwwwwwww
app.add_url_rule('/', 'index', index)
app.add_url_rule('/signup', 'signup', signup)
app.add_url_rule('/commit', 'commit', commit, methods=['post', 'get'])
app.add_url_rule('/tanya', 'tanya', tanya, methods=['post', 'get'])
app.add_url_rule('/answer', 'answer', answer, methods=['post', 'get'])

if __name__ == '__main__':
    app.run()