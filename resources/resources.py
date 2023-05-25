from flask import*
from flask_restful import Resource,Api
from database.models import Admin,bookings,Rooms,Guests,Complains
import json
from mongoengine import Q

from flask_session import Session


class AdminApi(Resource):
    def get(self):
        try:
            ta=request.get_json()
            print(ta)
            session['email']=ta['email']
            print(session['email'])
            a=session['email']
            p_data = Admin.objects(Q(email=ta['email']) & Q(password=ta['password'])).count()
            print(p_data)
            if p_data>0:
                return Response(render_template('admin.html', data=a),mimetype="application/json",status=200)

        except Exception as e:
            return ({"Error":str(e)}),201

    def post(self):
        try:
            data = request.get_json()
            print("p_data",data)

            pData=Admin(**data).save()
            id =pData.id
            return ({"Enroll":"Successfully Enrolled"}),200
        except Exception as e:
            return ({"Error":str(e)}),201


class ComplainApi(Resource):
    def get(self):
        try:
            p_data=Complains.objects().to_json()
            print(p_data)
            return Response(p_data, mimetype="application/json", status=200)
        except Exception as e:
            return ({"Error":str(e)}),201

    def post(self):
        try:
            data = request.get_json()
            print("Hello")
            print("p_data",data)

            pData=Complains(**data).save()
            id =pData.id
            return ({"Enroll":"Successfully Enrolled"}),200
        except Exception as e:
            return ({"Error":str(e)}),201




class RoomsApi(Resource):
    def get(self):
        try:
            p_data = Rooms.objects().to_json()
            print(p_data)
            return Response(p_data,mimetype="application/json",status=200)
        except Exception as e:
            return ({"Error":str(e)}),201

    def post(self):
        try:
            data = request.get_json()
            print('hello')
            print("p_data",data)
            pData=Rooms(r_id=data['r_id'],r_number=data['r_number'],r_type=data['r_type'],r_price=data['r_price'],r_status=data['r_status']).save()

            return ({"Enroll":"Successfully Enrolled"}),200
        except Exception as e:
            return ({"Error":str(e)}),201


class RoomsApiByNumber(Resource):
    def get(self,r_number):
        try:
            p_data = Rooms.objects().to_json()
            print(p_data)
            return Response(p_data,mimetype="application/json",status=200)
        except Exception as e:
            return ({"Error":str(e)}),201

    def delete(self,r_number):
        try:
            print("I amm in Rooms Api")
            Rooms.objects.get(r_number=r_number).delete()
            return ({"status": "Deleted"}), 200
        except Exception as e:
            return ({"Error": str(e)}), 201


class GuestApi(Resource):
    def get(self):
        try:
            p_data = Guests.objects().to_json()
            print(p_data)
            return Response(p_data,mimetype="application/json",status=200)
        except Exception as e:
            return ({"Error":str(e)}),201

    def post(self):
        try:

            data = request.get_json()
            print("p_data",data)
            Guests( g_name = data['g_name'], g_email = data['g_email'], g_city = data['g_city'], g_state = data[
                'g_state'], g_country = data['g_country'], g_PN = data['g_PN']).save()

            # bookings(at=data['aT'],dt=data['dT'],g_name=data['g_name'],r_count=data['tCount'],bill=data['bill']).save()
            render_template('reciept.html', data=data)
            return ({"Enroll":"Successfully Enrolled"}),200
        except Exception as e:
            return ({"Error":str(e)}),201








class  RoomsApi(Resource):
    def get(self):
        try:
            p_data = Rooms.objects().to_json()
            print(p_data)
            return Response(p_data,mimetype="application/json",status=200)
        except Exception as e:
            return ({"Error":str(e)}),201

    def post(self):
        try:
            print("Hello")
            data = request.get_json()
            print("p_data",data)
            pData=Rooms(**data).save()

            return ({"Enroll":"Successfully Enrolled"}),200
        except Exception as e:
            return ({"Error":str(e)}),201



class BookingApi(Resource):
    def get(self):
        try:
            p_data = bookings.objects().to_json()
            print(p_data)
            return Response(p_data,mimetype="application/json",status=200)
        except Exception as e:
            return ({"Error":str(e)}),201

    def post(self):
        try:
            data = request.get_json()
            bookings(**data).save()
            return ({"Enroll": "Successfully Enrolled"}), 200
        except Exception as e:
            return ({"Error": str(e)}), 201




class  FinalBookingApi(Resource):
    def get(self):
        try:

            p_data = bookings.objects().to_json()
            print(p_data)
            return Response(p_data,mimetype="application/json",status=200)
        except Exception as e:
            return ({"Error":str(e)}),201

    def post(self):
        try:

            data = request.get_json()
            print("p_data",data)
            print("Hello")
            pData=bookings(**data).save()
            return redirect('/booking2')

        except Exception as e:
            return ({"Error":str(e)}),201










class  AvailabilityApi(Resource):
    def get(self):
        try:
            p_data = Rooms.objects.filter(r_status="Available").to_json()


            print(p_data)
            return Response(p_data,mimetype="application/json",status=200)
        except Exception as e:
            return ({"Error":str(e)}),201

    def post(self):
        try:
            print("Hello")
            data = request.get_json()
            print("p_data",data)
            pData=Rooms(**data).save()

            return ({"Enroll":"Successfully Enrolled"}),200
        except Exception as e:
            return ({"Error":str(e)}),201


class AvailabilityAllApi(Resource):
    def get(self):
        try:
            p_data = Rooms.objects(Q(r_status="Available") & Q(r_type="Deluxe")).to_json()
            Deluxe= Rooms.objects(Q(r_status="Available") & Q(r_type="Deluxe")).count()
            Single = Rooms.objects(Q(r_status="Available") & Q(r_type="Single")).count()
            Double = Rooms.objects(Q(r_status="Available") & Q(r_type="Double")).count()
            result = {"Deluxe": Deluxe, "single": Single,"Double": Double}
            print(Deluxe,Single,Double)
            return Response(response=json.dumps(result), status=200, mimetype='application/json')
        except Exception as e:
            return ({"Error": str(e)}), 201


class CountApi(Resource):
    def get(self):
        try:
            count1 = Rooms.objects.count()
            count2 = Guests.objects.count()
            result = {"Guests": count2}

            # result = {"Rooms": count1, "Guests": count2}
            print(result)
            return Response(response=json.dumps(result), status=200, mimetype='application/json')

        except Exception as e:
            return {"error": str(e)}, 201

    def post(self):
        try:
            print("Hello")
            data = request.get_json()
            print("p_data",data)
            pData=Rooms(**data).save()

            return ({"Enroll":"Successfully Enrolled"}),200
        except Exception as e:
            return ({"Error":str(e)}),201


