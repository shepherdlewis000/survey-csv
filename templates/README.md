Implementation of a Python Flask/Jinja/Bootstrap web app that enables a user to 
 - fill out a form (a la Google Forms), the results of which are saved to a comma-separated value (CSV) file on the server
- view a table of all submissions received (a la Google Sheets)

app.py: the web app's controller. Imports csv, and from flask import Flask, redirect and render_template. Configures Flask, defines routes, server-side form validation, writes to survey.csv & redirects to /sheet. get_sheet reads past submissions and displays in HTML table

templates/layout.html: the app's layout in an HTML structure all views will share

templates/form.html: the actual form styled with Bootstrap, Javascript for form validation

templates/error.html: template for error message(s)

templates/sheet.html: Bootstrap styled table enhanced via BS4/jQuery DataTables to sort selected table columns 

static/styles.css: CSS properties for the app's views


