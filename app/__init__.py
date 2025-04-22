from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.context_processor
def inject_current_year():
    return {'current_year': datetime.now().year}


@app.route('/')
def home():
    return render_template('home.html', current_page='home')


@app.route('/services')
def services():
    return render_template('service.html', current_page='services')


@app.route('/about')
def about():
    return render_template('about.html', current_page='about')


@app.route('/contact')
def contact():
    return render_template('contact.html', current_page='contact')
