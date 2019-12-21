from django.urls import path, include
import sio.views

urlpatterns = [
    path('sio/', include('sio.urls')),
    path('sio.html', sio.views.home),
    # path('sio/create-student', sio.views.add_student),
]
