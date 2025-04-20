from flask import Blueprint, render_template, request, redirect, url_for, flash

main = Blueprint('main', __name__)

messages = []

@main.route('/')
def index():
    return render_template('index.html', messages=messages)

@main.route('/add_message', methods=['POST'])
def add_message():
    message = request.form.get('message')
    if message:
        messages.append(message)
    return redirect(url_for('main.index'))