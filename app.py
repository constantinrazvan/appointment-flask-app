from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    date = db.Column(db.String(1000))
    db.create_all()

@app.before_first_request
def create_tables():
    db.create_all()

@app.route("/appointment", methods=["GET", "POST"])
def makeAppointment(): 
    if request.method == "POST":
        new_appointment = Appointment( 
            email = request.form.get('email'), 
            date = request.form.get('date')
        )

        db.session.add(new_appointment)
        db.session.commit()

        flash('Your appointments has been registered!')

    return render_template("appointment_page.html")

@app.route("/appointments")
def appointments(): 

    appointment = Appointment.query.all()
    
    return render_template("appointments.html", appointments = appointment)

if __name__ == "__main__":
    app.run(debug=False)
