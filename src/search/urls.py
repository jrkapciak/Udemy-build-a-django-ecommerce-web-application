from django.conf.urls import url

<<<<<<< HEAD
from .views import SearchProductView
=======
from .views import (
    SearchProductView,
)
>>>>>>> 91537c5eaa003beff4a98cefe8318e7918c86fa4

urlpatterns = [
    url(r'^$', SearchProductView.as_view(),name='query'),
]
