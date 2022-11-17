from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('all_gifts', views.gifts, name="all_gifts"),
    path('new_gift', views.new_gift, name="new_gift"),
    # path('save_gift', views.save_gift, name="save_gift"),

]