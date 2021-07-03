from flask import Flask, render_template, request, session, jsonify, redirect, url_for, g
import models
app = Flask(__name__)
app.secret_key = 'jumpjacks'


@app.route('/', methods=['GET'])
def home():
    if 'username' in session:
        g.username = session['username']
        message = f'welcome {g.username}'
        return render_template('user_page.html', message=message)
    return render_template('index.html', message="this is the homepage")


@app.route('/about', methods=['GET'])
def about():
    return render_template('about_us.html')


@app.route('/terms_of_use', methods=['GET'])
def terms_of_use():
    return render_template('terms_of_use.html')


@app.route('/privacy', methods=['GET'])
def privacy():
    return render_template('privacy.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    else:
        form_username = request.form['username']
        form_pw = request.form['password']
        message = models.signup(form_username, form_pw)
    return render_template('signup.html', message=message)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        session.pop('username', None)
        form_username = request.form['username']
        db_pwd = models.verify_pw(form_username)
        if db_pwd == request.form['password']:
            session['username'] = request.form['username']
            return redirect(url_for('user_page'))
    return render_template('login.html', message=db_pwd)


@app.route('/user_page', methods=['GET', 'POST'])
def user_page():
    if request.method == 'GET':
        if 'username' in session:
            return redirect(url_for('home'))
        return render_template('index.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))


@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    if request.method == 'GET':
        user_tasks = models.get_tasks(session['username'])
        return jsonify(user_tasks)


@app.before_request
def before_request():
    g.username = None
    if 'username' in session:
        g.username = session['username']


@app.route('/add_task', methods=['POST'])
def insert_task():
    username = session['username']
    form_taskname = request.form['task_name']
    form_startdate = request.form['task_start_date']
    form_duedate = request.form['task_due_date']
    models.add_task(username, form_taskname, form_startdate, form_duedate)
    return redirect(url_for('user_page'))


@app.route('/delete_task', methods=['DELETE'])
def delete_task():
    task_id = request.json
    models.remove_task(task_id)
    return redirect(url_for('home'))


@app.route('/edit_task/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    if request.method == 'GET':

        return render_template('edit_task.html')
    else:
        return 'Post %d' % task_id


@app.route('/edit_task/<int:task_id>/edit')
def edit(task_id):
    task_info = models.get_task(session['username'], task_id)
    return jsonify(task_info)


if __name__ == '__main__':
    app.run(port=7000, debug=True)
