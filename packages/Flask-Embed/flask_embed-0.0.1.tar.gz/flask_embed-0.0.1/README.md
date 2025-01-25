# Flask-Embed Project 🚀🐍

![Flask-Embed Logo](https://raw.githubusercontent.com/Masterjx9/Flask-Embed/main/logo.png)

Flask-Embed is a Flask extension that allows you to run Python code directly from your HTML templates. This can be incredibly useful for convience of running python from the HTML templates as a convience. 🎉

## Installation 📦

You can install Flask-Embed using pip:

```sh
pip install Flask-Embed
```

## Usage Example 💻

Here's a simple example of how to use Flask with the Flask-Embed library:

```python
from flask import Flask
from flask_embed import Embed

app = Flask(__name__)
embed = Embed()

@app.route('/')
def hello_world():
    return embed.render_template('index.html', embed=embed)

if __name__ == '__main__':
    app.run(debug=True)
```

## How It Works 🛠️

Flask-Embed allows you to embed Python code within your HTML templates using special tags. The embedded Python code is executed on the server side, and the output is rendered in the HTML.

### Example HTML Template 📄

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reactive Flask</title>
</head>
<body>
    <h1>Python Embed Test</h1>
    <p>Python code:</p>
    <FlaskOutput></FlaskOutput>
</body>
</html>
```

### Embedded Python Code 🐍

```python
<Flask>
import urllib.request
import json

with urllib.request.urlopen("https://jsonplaceholder.typicode.com/posts") as response:
    data = response.read()
    posts = json.loads(data)
    output = posts[:5]
</Flask>
```

The above code fetches data from an API and displays the first five posts in the HTML template. 🌐

## Conclusion 🎯

Flask-Embed makes it easy to integrate Python code into your HTML templates, providing a seamless way to create dynamic web applications. Give it a try and see how it can simplify your Flask projects! 🚀
