from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    answer = render_template('base.html', title=title)
    return answer


if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1')