from .resources import AdminApi,RoomsApi,GuestApi,BookingApi,RoomsApiByNumber,AvailabilityApi,CountApi,AvailabilityAllApi,ComplainApi

def initialize_routes(api):

    api.add_resource(AdminApi, '/api/Admin')
    api.add_resource(RoomsApi, '/api/Rooms')
    api.add_resource(RoomsApiByNumber,'/api/RoomsApi<r_number>')
    api.add_resource(GuestApi, '/api/Guest')
    api.add_resource(BookingApi, '/api/Bookings')
    api.add_resource(AvailabilityApi, '/api/Availabilty')
    api.add_resource(ComplainApi, '/api/Complains')
    api.add_resource(AvailabilityAllApi,'/api/AvailabiltyAll')
    api.add_resource(CountApi,'/api/Count')