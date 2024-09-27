

from django.urls import path
import app.views
from app import views

app_name = 'app'
urlpatterns = [
    path('base/',views.RepUsers.as_view(),name='rep'),
    path('base/<int:year>/<int:month>/<int:day>/<int:hour>/<int:minute>/<int:second>',
         views.reported,
         name='reported'),
    path('',views.skarga, name="skarga"),
    path('logowanie/',views.logowanie, name="logowanie"),
    # path('zmiana/',views.edit_note,name="edit_note"),
]
