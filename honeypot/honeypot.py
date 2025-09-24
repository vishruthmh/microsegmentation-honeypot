from flask import Flask, request
import logging, datetime

app = Flask(__name__)
logging.basicConfig(filename='/logs/attacks.log', level=logging.INFO)

@app.route("/", methods=["GET", "POST"])
def fake_admin():
    if request.method == "POST":
        uname = request.form.get("username")
        pwd = request.form.get("password")
        logging.info(f"{datetime.datetime.utcnow()} | {request.remote_addr} | {uname}:{pwd}")
        return "Invalid credentials"
    return '''
        <form method="post">
          Username:<input name="username"><br>
          Password:<input type="password" name="password"><br>
          <input type="submit">
        </form>
    '''
