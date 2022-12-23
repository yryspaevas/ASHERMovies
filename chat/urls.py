# from django.urls import path

# from . import views

# urlpatterns = [ 
#     path('', views.index, name='index'),
#     path('<str:room_name>/', views.room, name='room')
# ]

# from django.contrib import admin
# from django.urls import path
# from chat.views import chat_box

# urlpatterns = [
#     # path("admin/", admin.site.urls),
#     path("<str:chat_box_name>/", chat_box, name="chat")
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('chat/', views.home, name='home'),
    path('<str:room>/', views.room, name='room'),
    path('chat/checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]

