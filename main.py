#Импорт
from flask import Flask, render_template, request, redirect, session
#Подключение библиотеки баз данных
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


#Подключение SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diary.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Создание db
db = SQLAlchemy(app)
#Создание таблицы

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)


#Запуск страницы с контентом
@app.route('/')
def index():
    return render_template('index.html')
#Динамичные скиллы
@app.route('/', methods=['POST'])
def process_form():
    button_python = None
    button_discord = None
    button_html = None
    button_db = None

    if request.method == 'POST':
        if 'email' in request.form and 'text' in request.form:
            email = request.form['email']
            text = request.form['text']
            id = request.form.get('id')
            feedback = Feedback(id=id, email=email, text=text)
            db.session.add(feedback)
            db.session.commit()
        else:
            button_python = request.form.get('button_python')
            button_discord = request.form.get('button_discord')
        
    return render_template('index.html', button_python=button_python, button_discord=button_discord, button_html=button_html, button_db=button_db)



if __name__ == "__main__":
    app.run(debug=True)