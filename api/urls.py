from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getPara/', views.get_paragrahs, name='getPara'),
    path('addPara/', views.add_paragraph, name='addPara'),
    path('updatePara/<str:id_to_update>/', views.update_paragraph, name='updatePara'),
    path('deletePara/<str:id_to_delete>/', views.delete_paragraph, name='deletePara'),
    path('getStats/', views.get_stats, name='getStats'),
    path('addStat/', views.add_stat, name='addStat')
]