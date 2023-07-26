from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prediction', methods=['POST'])
def prediction():
    # Retrieve form data
    loan_amount = int(request.form['loan_amnt'])
    annual_income = int(request.form['annual_inc'])
    fico_score = int(request.form['fico_avg_score'])
    mortgage = int(request.form['mort_acc'])
    employment_status = request.form['employment_status']
    home_ownership = request.form['home_ownership']
    loan_purpose = request.form['loan_purpose']


    # Perform prediction
    if (annual_income < loan_amount or
        fico_score < 630 or
        mortgage > 6 or
        (employment_status == 'Unemployed' and mortgage > 3) or
        (employment_status == 'Unemployed' and annual_income < loan_amount) or
        (home_ownership == 'MORTGAGE' and annual_income < loan_amount) or
        (employment_status == 'Unemployed' and home_ownership == 'RENT') or
        (employment_status == 'Employed' and annual_income < 25000) or
        (home_ownership == 'MORTGAGE' and employment_status == 'Unemployed')):
        result = 'Default'
    else:
        result = 'No Default'

    return render_template('prediction.html', result=result)

if __name__ == '__main__':
    app.run()
