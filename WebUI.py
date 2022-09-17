from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods = ['POST', 'GET'])
def index():
    if request.method == 'GET':
            return render_template("index.html")
    if request.method == 'POST':
        if "album" in request.form["spotifyURL"]:
            writeData = "album:" + request.form["spotifyURL"][31:].split("?si=")[0]
        else:
            writeData = "track:" + request.form["spotifyURL"][31:].split("?si=")[0]
        return render_template('index.html',form_data = "Write Me: " + writeData)
 
app.run(host='localhost', port=5000)