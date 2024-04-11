#import modules/functions from flask
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

class wells_calc:
    def __init__(self, form_data):
        self.form_data = form_data

    def calculate_score(self):
        score = 0

        if self.form_data.get('dvt') == 'Yes':
            score += 3
        if self.form_data.get('alt-diag') == 'Yes':
            score += 3
        if self.form_data.get('HR') == 'Yes':
            score += 1.5
        if self.form_data.get('immob') == 'Yes':
            score += 1.5
        if self.form_data.get('dvt-pe') == 'Yes':
            score += 1.5
        if self.form_data.get('haemop') == 'Yes':
            score += 1
        if self.form_data.get('pmh') == 'Yes':
            score += 1

        return score

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        form_data = request.form
        Wells_Calc = wells_calc(form_data)
        score = Wells_Calc.calculate_score()

        if score < 4:
            advice = "Given that the Wells score is less than 4, PE is unlikely"
        else:
            advice = "Given that the Wells score is 4 or higher, PE is likely"

        return render_template('result.html', score=score, advice=advice)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

