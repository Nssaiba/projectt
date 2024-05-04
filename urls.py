
from django.urls import path
from DreamT import views
from django.conf import settings
from django.conf.urls.static import static
from .views import Dashboard
# from chatbot.views import chatbot


app_name = 'chatbot'
urlpatterns = [
   path('',views.index,name="index"),
   path('gestion-even/', views.gestion_even, name='gestion_even'),
   # path('about',views.about,name="about"),
   path('insert',views.insertData, name="insertData"),
   path('update/<id>',views.updateData, name="insertData"),
   path('delete/<id>',views.deleteData, name="insertData"),
   path('insertEvent',views.insertEvent, name="insertEvent"),
   # path('updateEven/<id>',views.updateEven, name="updateEven"),
   path('deleteEvent/<id>',views.deleteEvent, name="deleteEvent"),
   path('updateEvent/<id>', views.updateEvent, name="updateEvent"),
   path('Dashboard',views.Dashboard,name="Dashboard"),
   path('Dashboard/', Dashboard, name='dashboard'),
   path('search/',views.search_offers, name='search_offers'),
   path('searchEvent/',views.search_events, name='search_events'),
   path('team/', views.team, name='team'),
   path('search_clients/',views.search_clients, name='search_clients'),
   path('GestionDest/', views.GestionDest, name='GestionDest'),
   path('insertDestination',views.insertDestination, name="insertDestination"),
   path('deleteDest/<id>',views.deleteDest, name="deleteDest"),
   path('updateDest/<id>', views.updateDest, name="updateDest"),  
   path('home/', views.home, name='home'),
   path('clientDestinations/', views.clientDestinations, name='clientDestinations'), 
   path('clientEvent/', views.clientEvent, name='clientEvent'), 
   path('clientPackages/', views.clientPackages, name='clientPackages'), 
   path('clientRestaurants/', views.clientRestaurants, name='clientRestaurants'), 
   path('chatbot_home/', views.chatbot, name='chatbot_home'),
   path('subscribe/',views.subscribe, name='subscribe'),
   path('login/',views.login, name='login'),
   path('comment/', views.comment, name='comment'),
   path('addComment/', views.addComment, name='addComment'),
   path('loginAdmin/', views.loginAdmin, name='loginAdmin'),
   path('LoginAdminPage/', views.LoginAdminPage, name='LoginAdminPage'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    