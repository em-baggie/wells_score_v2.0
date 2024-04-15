#import modules/functions from flask
from flask import Flask, render_template, request, redirect, url_for

#create an instance of the Flask class
app = Flask(__name__)

#create a wells score class which takes the web form data as an input
class wells_calc:
    def __init__(self, form_data):
        self.form_data = form_data

# Calculation logic for the Wells score based on form data
# Increment score based on form input
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

#Define the route for the base URL
#Use the methods parameter to specify which HTTP request methods this route can handle (GET and POST)
#GET request - used for retrieving data from the server
#POST request - used for sending data to the server - e.g. submitting a form on a webpage
#Setting POST and GET allows the route to handle both types of request - view page (GET request) or submit a form (POST request)
@app.route('/', methods=['GET', 'POST'])
#Set the view function - handles HTTP requests made to the URL route
#defines the behaviour of the application when users access the homepage/submit data to the root URL
def index():
    if request.method == 'POST':
        #retrieve form data submitted by the user
        form_data = request.form
        #create new instance of wells_calc
        Wells_Calc = wells_calc(form_data)
        score = Wells_Calc.calculate_score()

        #define the advice
        if score < 4:
            advice = "Given that the Wells score is less than 4, PE is unlikely"
        else:
            advice = "Given that the Wells score is 4 or higher, PE is likely"

        #render a template with calculated score and advice
        return render_template('result.html', score=score, advice=advice)
    else:
        #if the request method is not POST (and therefore is GET), it renders the form page
        return render_template('index.html')

#If script is executed directly, will start the development server in debug mode
if __name__ == '__main__':
    app.run(debug=True)

