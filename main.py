from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from dotenv import load_dotenv
import os
from text_extraction import extract
from model import generate

app = Flask(__name__)
Bootstrap5(app)
load_dotenv()
UPLOAD_FOLDER = '/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
SECRET_KEY = os.getenv('SECRET_KEY')
app.config['SECRET_KEY'] = SECRET_KEY


class UploadForm(FlaskForm):
    file = FileField('File', validators=[
        FileRequired(),
        FileAllowed(['pdf', 'docx', 'txt'], 'Only pdf, docx, and txt files allowed!')
    ])
    query = StringField('Ask a question', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def home():
    form = UploadForm()
    if form.validate_on_submit():
        file = form.file.data
        file_extension = file.filename.split(".")[-1].lower()
        extracted_text = extract(file, file_extension)
        answer = generate(extracted_text, form.query.data)
        print(answer)
        with open('answer.txt', 'w') as f:
            f.write(answer)
        return redirect(url_for('answers'))
    return render_template('index.html', form=form)


@app.route('/answers')
def answers():
    with open('answer.txt', 'r') as f:
        ans = f.readlines()
    return render_template('answers.html', answer=ans)


if __name__ == "__main__":
    app.run(debug=True)
