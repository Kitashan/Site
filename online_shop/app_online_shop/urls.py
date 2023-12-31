from django.urls import path
from .views import index, top_sellers, advert, advert_post, login, profile, register

urlpatterns = [
    path('', index, name= 'main-page'),
    path('top-sellers/', top_sellers, name = 'top-sellers'),
    path('advertisement/', advert, name='advertisement'),
    path('advertisement-post/', advert_post, name='advertisement-post'),
    path('login/', login, name = 'login'),
    path('profile/', profile, name = 'profile'),
    path('register/', register, name = 'register')
]