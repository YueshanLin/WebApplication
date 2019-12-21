from django.urls import path
import sio.views

urlpatterns = [
    #path('sio/', include('sio.urls')),
    path('sio.html', sio.views.home),
    path('create-student', sio.views.add_student),
]
