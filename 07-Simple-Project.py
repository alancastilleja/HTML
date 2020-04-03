from flask import render_template, Flask, request

app = Flask(__name__)
@app.route('/')
def index():
    reqs = ['Must have an upper case letter somewhere', 'Must have a lower case letter somewhere', 'must have a number at the end']
    return render_template('index1.html', reqs=reqs)



@app.route('/report')
def report():
    username = request.args.get('username')

    upper = any(letter.isupper() for letter in username)
    lower = any(letter.islower() for letter in username)
    num_end = username[-1].isdigit()
    result = upper == True and lower == True and num_end == True
    return render_template('report.html', username=username, upper = upper, lower=lower,num_end=num_end, result=result)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('06-404.html')


if __name__ == '__main__':
    app.run(debug=True)
