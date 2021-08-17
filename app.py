from flask import Flask , render_template ,request
from flask_mail import Mail , Message


app = Flask(__name__)

mail = Mail(app)

@app.route('/')
def index():
    return render_template("contact.html")

@app.route('/send_message' , methods = ['GET' , 'POST'] )
def send_message():
    if request.method == "POST" :
        

if __name__ == "__main__" :
    app.run(debug=True)