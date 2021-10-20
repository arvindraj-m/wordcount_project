from . import veiw
from django.urls import path


urlpatterns = [
    path('',veiw.home,name='home'),
    path('count/',veiw.count , name='count')
]
