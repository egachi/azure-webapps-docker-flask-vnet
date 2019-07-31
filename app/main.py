from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == '__main__':
    port=os.environ.get('PORT')
    print(str(port))
    app.run(host='0.0.0.0', debug=False, port=port)