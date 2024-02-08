from flask import Flask, render_template, request
from report import generate_report, data

app = Flask(__name__)



# Your existing functions for generating reports go here


@app.route("/inputs")
def index():
    return render_template("index.html")


@app.route('/outputs', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        # Receive form data
        form_data = request.form
        # Generate report based on form data
        report = generate_report(data,
                                 item_code=form_data['item'],
                                 branch=form_data['branch'],
                                 startdate=form_data['startdate'],
                                 enddate=form_data['enddate'])
        # Pass report data to the outputs page
        return render_template("index2.html", report=report)

if __name__ == '__main__':
    app.run(debug=True)
