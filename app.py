import csv

from flask import Flask, redirect, render_template, request

# Configure application
app = Flask(__name__)

# Reload templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET"])
def get_index():
    return redirect("/form")


@app.route("/form", methods=["GET"])
def get_form():
    return render_template("form.html")


@app.route("/form", methods=["POST"])
def post_form():
    if not request.form.get("fname") or not request.form.get("lname"):
        return render_template("error.html", message="Please provide your first and last name.")
    if not request.form.get("email"):
        return render_template('error.html', message="Please provide your email.")
    if not request.form.get("isVoting"):
        return render_template('error.html', message="Please indicate whether you are planning on voting in the 2020 Democratic primary.")

    # myData = [[1, 2, 3], ['Good Morning', 'Good Evening', 'Good Afternoon']]
    fname = request.form.get("fname")
    lname = request.form.get("lname")
    email = request.form.get("email")
    party = request.form.get("party")
    isVoting = request.form.get("isVoting")
    data = [fname, lname, email, party, isVoting]


    f = open('survey.csv', 'a')
    with f:
        writer = csv.writer(f)
        writer.writerow(data)
    return redirect("/sheet")

@app.route("/sheet", methods=["GET"])
def get_sheet():
    table = ''
    with open("survey.csv", encoding="utf8") as csvFile:
        reader = csv.DictReader(csvFile, delimiter=',')
        table = '<tr>{}</tr>'.format(''.join(['<td>{}</td>'.format(header) for header in reader.fieldnames]))
        for row in reader:
            table_row = '<tr>'
            for fn in reader.fieldnames:
                table_row += '<td>{}</td>'.format(row[fn])
            table_row += '</tr>'
            table += table_row
    return render_template("sheet.html", table=table)
