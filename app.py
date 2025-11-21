from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/main", methods=["GET", "POST"])

def index():
    return(render_template("index.html"))

@app.route("/main

def main():
    return(render_template("main.html"))
    q = request.form.get("q")
    print(q)
    
if __name__ == "__main__":
    app.run()
