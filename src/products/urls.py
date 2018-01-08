from django.conf.urls import url

from .views import (
    ProductListView,
    ProductDetailView,)

urlpatterns = [
    url(r'(?P<slug>[\w-]+)/$', ProductDetailView.as_view(),name='detail'),
    url(r'^$', ProductListView.as_view(),name='list'),
]
