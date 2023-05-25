from flask import *
from flask import session




from flask_restful import Api, Resource
from database import db
from resources import routes
from database.models import Admin, bookings, Rooms, Guests, Complains
import datetime
at=datetime.datetime.now()
dt=datetime.datetime.now()


from flask_session import Session



app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost:27017/Hotel_Management'
}


app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = 'your_secret_key'

Session(app)



api = Api(app)
db.initialize_db(app)
routes.initialize_routes(api)


@app.route('/')
def addContacts():  # put application's code here
    return render_template("hotel.html")




@app.route('/')
def index():  # put application's code here
    return render_template("hotel.html")


@app.route('/hotel')
def hotel():  # put application's code here
    return render_template("hotel.html")


@app.route('/service')
def service():  # put application's code here
    return render_template("service.html")


@app.route('/login')
def loginPage():  # put application's code here
    return render_template("login.html")


@app.route('/booking')
def booking():  # put application's code here
    return render_template("booking.html")


@app.route('/contact')
def contact():  # put application's code here
    return render_template("contact.html")


@app.route('/more')
def more():  # put application's code here
    return render_template("more.html")


@app.route('/complain')
def complain():  # put application's code here
    return render_template("complain.html")


@app.route('/admin')
def a():  # put application's code here
    return render_template("admin.html")


@app.route('/booking2', methods=['POST'])
def booking2():  # put application's code here
    at = request.form.get('at')
    dt = request.form.get('dt')
    bookings(at=at, dt=dt).save()
    return render_template("booking2.html", at=at, dt=dt)


@app.route('/booking3', methods=['POST'])
def booking3():
    bill = request.form.get('val')
    rooms = request.form.get('tCount')
    aT = request.form.get('aT')
    dT = request.form.get('dT')
    print(bill)
    print(rooms)
    print(aT)
    print(dT)
    return render_template("booking3.html", bill=bill, rooms=rooms, aT=aT, dT=dT)


@app.route('/booking4', methods=['POST'])
def booking4():
    gName=request.form.get('g_name')
    gEmail=request.form.get('g_email')
    gPhone=request.form.get('g_PN')
    gState=request.form.get('g_state')
    gCity=request.form.get('g_city')
    gCountry=request.form.get('g_country')
    gBill=request.form.get('bill')
    gRooms=request.form.get('rooms')
    aT = request.form.get('aT')
    dT = request.form.get('dT')
    Guests(g_name=gName, g_email=gEmail, g_city=gCity, g_state=gState,  g_country=gCountry, g_PN=gPhone).save()
    bookings(at=aT, dt=dT, g_name=gName, r_count=gRooms, bill=gBill).save()
    return render_template("reciept.html", gName=gName, gPhone=gPhone, gCity=gCity, gBill=gBill, gRooms=gRooms)


@app.route('/receipt')
def receipt():
    return render_template("reciept.html")


if __name__ == '__main__':
    app.run()
