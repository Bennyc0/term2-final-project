from flask import Flask, render_template, request, redirect, url_for
from api_functions import get_calories, get_more_info
from datetime import datetime
import db_functions as dbf

app = Flask(__name__)
logged_in_username = ""

@app.route('/')
def index():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    global logged_in_username

    email = request.form['email']
    password = request.form['password']

    logged_in_username = dbf.validate_user(email, password)

    if logged_in_username != "":
        return redirect(url_for('home'))

    else:
        return redirect(url_for('index'))


@app.route('/sign-up')
def sign_up():
    return render_template('sign-up.html')


@app.route('/store-user', methods=['GET', 'POST'])
def store_user():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']

    dbf.sign_up_user(username, email, password)

    return redirect(url_for('index'))


@app.route('/home', methods=['GET', 'POST'])
def home():
    global logged_in_username
    
    try:
        current_datetime = datetime.now()

        time = current_datetime.strftime("%m/%d/%Y %H:%M:%S")
        food_item = request.form['food_item'].capitalize()
        amount = request.form['amount']
        calories = get_calories(food_item, amount)

        dbf.store_information(logged_in_username, time, food_item, amount, calories)

    except:
        pass
    
    if logged_in_username == "":
        return redirect(url_for('index'))

    elif request.method == 'POST' or request.method == 'GET':
        user_information = dbf.get_user_information(logged_in_username)

        return render_template('home.html', logged_in_username=logged_in_username, user_information=user_information)
    
    else:
        return render_template('home.html', logged_in_username=logged_in_username)


@app.route('/todays-intake', methods=['GET', 'POST'])
def todays_intake():
    current_datetime = datetime.now()
    date = current_datetime.strftime("%m/%d/%Y")

    user_information = dbf.get_date_information(logged_in_username, date)
    todays_calories = 0

    for instance in user_information:
        todays_calories += float(instance['calories'])

    if logged_in_username != "":
        return render_template('todays-intake.html', user_information=user_information, todays_calories=todays_calories)

    else:
        return redirect(url_for('index'))



@app.route('/more-information/<rowid>', methods=['GET', 'POST'])
def more_information(rowid):
    row_information = dbf.get_row_information(rowid)
    extra_information = dbf.get_more_info(row_information['food_item'], row_information['amount'])

    if logged_in_username != "":
        return render_template('more-information.html', extra_information=extra_information)

    else:
        return redirect(url_for('index'))


@app.route('/edit/<rowid>')
def edit(rowid):
    row_information = dbf.get_row_information(rowid)

    if logged_in_username != "":
        return render_template('edit.html', row_information=row_information)

    else:
        return redirect(url_for('index'))


@app.route('/process-edit/<rowid>', methods=['POST'])
def process_edit(rowid):

    food_item = request.form['food_item']
    amount = request.form['amount']
    calories = get_calories(food_item, amount)

    dbf.edit_information(food_item, amount, calories, rowid)

    return redirect(url_for('home'))


@app.route('/delete/<rowid>')
def delete(rowid):
    dbf.delete_information(rowid)

    return redirect(url_for('home'))


if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')
