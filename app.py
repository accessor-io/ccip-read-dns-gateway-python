from flask import Flask, request, render_template_string
import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

DOH_GATEWAY_URL = os.getenv('DOH_GATEWAY_URL', 'http://localhost:8081/resolve')

# Simple HTML form for input
HTML_FORM = """
<!doctype html>
<title>DNS Query</title>
<h1>Enter DNS Query</h1>
<form method=post>
  Domain Name: <input type=text name=name>
  Query Type: <input type=number name=qtype>
  <input type=submit value=Submit>
</form>
{% if result %}
<h2>Result</h2>
<pre>{{ result }}</pre>
{% endif %}
"""

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    result = None
    if request.method == 'POST':
        name = request.form['name']
        qtype = int(request.form['qtype'])

        # Send request to aiohttp server
        response = requests.post(DOH_GATEWAY_URL, json={'name': name, 'qtype': qtype})
        if response.status_code == 200:
            result = response.json()
        else:
            result = f"Error: {response.status_code}"

    return render_template_string(HTML_FORM, result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8082)
