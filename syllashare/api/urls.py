from django.urls import path

from syllatokens.views import exchange_google_code, reassign_google_token
from user_data.views import get_class_schedule, modify_user, get_user, get_schools, search_classes

urlpatterns = [
    path(r'exchangegoogle', exchange_google_code),
    path(r'reassigngoogle', reassign_google_token),
    path(r'modifyuser', modify_user),
    path(r'getuser', get_user),
    path(r'getschools', get_schools),
    path(r'classschedule', get_class_schedule),
    path(r'searchclasses', search_classes),
]