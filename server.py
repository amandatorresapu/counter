from flask import Flask, render_template, request, redirect, session #import flask & render template
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes





@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

count = 1

@app.route("/counter", methods = ["POST"])
def counter():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 1
    return render_template("counter.html")


@app.route("/destroy_session")
def destroy_session():
    session.clear()
    return redirect("/dashboard")



if __name__ == "__main__":
    app.run(debug=True)