import flask import flask ,render_template,requests
from flask_mail import Mail,Message
app = Flask(__name__)
mail = Mail(app)
@app.route(/)
def index():
    return render_template("contact.html")

if __name__ == "__main__" :
    app.run(debug=True)