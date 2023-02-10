from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    answer = render_template('base.html', title=title)
    return answer


@app.route("/training/<prof>")
def training(prof):
    pr = 0
    if "инженер" in prof.lower():
        pr = "ing"
    elif "строитель" in prof.lower():
        pr = "sinse"
    answer = render_template('training.html', title="training", prof=pr)
    return answer


if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1')
