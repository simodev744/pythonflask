from flask import Flask, render_template_string

app = Flask(__name__)

# HTML template for navigation
HTML_TEMPLATE = """
<!doctype html>
<title>Simple Flask App</title>
<h1>Simple Flask App</h1>
<nav>
    <a href="/">Home</a> | 
    <a href="/about">About</a> | 
    <a href="/contact">Contact</a>
</nav>
<hr>
{% block content %}{% endblock %}
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE + '<h2>Home Page</h2>')

@app.route('/about')
def about():
    return render_template_string(HTML_TEMPLATE + '<h2>About Page</h2>')

@app.route('/contact')
def contact():
    return render_template_string(HTML_TEMPLATE + '<h2>Contact Page</h2>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
