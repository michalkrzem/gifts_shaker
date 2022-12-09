from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('all_gifts', views.gifts, name="all_gifts"),
    path('all_shakers', views.shakers, name="all_shakers"),
    path('new_shaker', views.create_shaker, name="new_shaker"),
    path('new_shaker/add_person/<str:pk>/', views.add_person_to_shaker, name="add_person"),
    path('new_gift', views.create_gift, name="new_gift"),
    # path('invite', views.new_gift, name="new_gift"),
    path('invite', views.create_invitation, name="invite"),
    path('all_invitations', views.invitations, name="all_invitations"),
    path('all_invitations/invitation/delete/<str:pk>/', views.delete_invitation, name="delete_invitation"),
    path('all_gifts/gift/delete/<str:pk>/', views.delete_gift, name="delete_gift"),
    path('all_gifts/gift/update/<str:pk>/', views.update_gift, name="update_gift"),
    # path('save_gift', views.save_gift, name="save_gift"),

]