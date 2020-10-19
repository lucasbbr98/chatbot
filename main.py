from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('chat.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=8000, debug=True)