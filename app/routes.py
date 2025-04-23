import os
from collections import deque
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

@main.route('/status')
def status():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    production_base = "/mnt/c/Midterm(DevOps)/production"
    live_link = os.path.join(production_base, 'live')
    if os.path.islink(live_link):
        current_env = os.path.basename(os.readlink(live_link))
    else:
        current_env = "none"

   
    log_path = os.path.join(project_root, 'deployment_health.log')
    try:
        with open(log_path) as f:
            last_lines = deque(f, maxlen=20)
    except FileNotFoundError:
        last_lines = ["No log file found at {}".format(log_path)]

    return render_template(
        'status.html',
        current_env=current_env,
        log_lines=list(last_lines),

    )

