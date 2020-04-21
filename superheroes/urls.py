from django.conf.urls.static import static
from django.urls import path

from example import settings
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('hero/<int:hero_id>/', hero_detail, name='hero_detail'),
    path('create-hero/', create_hero, name="create_hero"),
    path('update-hero/<str:pk>/', update_hero, name="update_hero"),
    path('delete-hero/<str:pk>/', delete_hero, name="delete_hero"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)