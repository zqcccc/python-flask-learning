from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World!"

@app.route('/hello/<name>')
def hello(name=None):
    # return render_template('hello.html', name=name)
    return f'hello {name}'
# if __name__ == '__main__':
#         app.run('localhost', 5555)