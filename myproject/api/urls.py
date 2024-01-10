from django.urls import path,include
from home.views import PersonView

urlpatterns = [
    path('person/',PersonView.as_view(),name='PersonView')
]
