from flask import Flask, render_template, request, redirect, url_for
import re

app = Flask(__name__)

def is_xss(payload):
    # Basic XSS check using common patterns
    pattern = re.compile(r"<script.*?>|<.*?on\w+=.*?>|javascript:", re.IGNORECASE)
    return pattern.search(payload) is not None

def is_sql_injection(payload):
    # Basic SQLi check (e.g., tautologies, UNION, comments, etc.)
    pattern = re.compile(r"(?:')|(?:--)|(?:\b(SELECT|UPDATE|DELETE|INSERT|UNION|DROP)\b)", re.IGNORECASE)
    return pattern.search(payload) is not None

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        term = request.form.get('term', '')
        if is_xss(term):
            return render_template('index.html', term='')
        elif is_sql_injection(term):
            return render_template('result.html', term='Possible SQLi detected!')
        else:
            return render_template('result.html', term=term)
    return render_template('index.html')

@app.route('/home')
def go_home():
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)