from flask import Flask, render_template, request, redirect, url_for
from db_functions import store_information, edit_information, delete_information, get_row_information, get_user_information
from api_functions import get_calories, get_more_info
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        current_datetime = datetime.now()

        username = request.form['username']
        time = current_datetime.strftime("%D/%M/%Y %H:%M:%S")
        food_item = request.form['food_item'].capitalize()
        amount = request.form['amount']
        calories = get_calories(food_item, amount)

        store_information(username, time, food_item, amount, calories)

    except:
        pass

    return render_template('index.html')


@app.route('/search-result', methods=['GET', 'POST'])
def search_result():
    if request.method == 'POST':
        username = request.form['search_username']

        user_information = get_user_information(username)

    return render_template('search-result.html', user_information=user_information)


@app.route('/more-information/<rowid>', methods=['GET', 'POST'])
def more_information(rowid):
    row_information = get_row_information(rowid)
    extra_information = get_more_info(row_information['food_item'], row_information['amount'])

    return render_template('more-information.html', extra_information=extra_information)


@app.route('/edit/<rowid>')
def edit(rowid):
    row_information = get_row_information(rowid)

    return render_template('edit.html', row_information=row_information)


@app.route('/process-edit/<rowid>', methods=['POST'])
def process_edit(rowid):

    food_item = request.form['food_item']
    amount = request.form['amount']
    calories = get_calories(food_item, amount)

    edit_information(food_item, amount, calories, rowid)

    return redirect(url_for('index'))


@app.route('/delete/<rowid>')
def delete(rowid):
    delete_information(rowid)

    return redirect(url_for('index'))


if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')