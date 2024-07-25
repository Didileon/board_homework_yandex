from django.urls import path
from .views import *


urlpatterns = [
    path('', AdvertList.as_view(), name="advert-list"),
    path('<int:pk>', AdvertDetail.as_view(), name="advert-detail"),
    #path('<slug:category>/<slug:slug>/', AdvertDetail.as_view(), name="advert-detail"),
    path('create/', AdvertCreate.as_view(), name='advert_create'),
    path('<int:pk>/update/', AdvertUpdate.as_view(), name='advert_update'),
    #path('<slug:category>/<slug:slug>/update/', AdvertUpdate.as_view(), name='advert_update'),
    path('<int:pk>/delete/', AdvertDelete.as_view(), name='advert_delete'),
    #path('<slug:category>/<slug:slug>/delete/', AdvertDelete.as_view(), name='advert_delete'),

]