

from django.urls import path
import app.views
from app import views
app_name = 'Users'
urlpatterns = [
    path('base/',views.RepUsers.as_view(),name='rep'),
    path('base/<int:year>/<int:month>/<int:day>/<int:hour>/<int:minute>/<int:second>',
         views.reported,
         name='reported'),
]
