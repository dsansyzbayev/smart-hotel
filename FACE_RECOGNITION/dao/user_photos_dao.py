from db.models import UserPhoto


def get_user_photos():
    user_photos = UserPhoto.objects().all()
    return user_photos
