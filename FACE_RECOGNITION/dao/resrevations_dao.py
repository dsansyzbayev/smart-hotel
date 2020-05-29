from db.models import Reservation


def get_all_reservations():
    all_reservations = Reservation.objects.all()
    return all_reservations
