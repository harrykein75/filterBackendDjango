from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    # path('', views.index, name='index'),
    # path('<int:points_id>/', views.detail, name='detail'),
    path('', views.PointListView.as_view(), name='index'),
    path('<int:pk>/', views.PointDetailView.as_view(), name='detail'),
    path('search/', views.search_view, name='search'),
    path('order_data/', views.order_data, name='order_data'),
    path('get_data/', views.get_data, name='get_data'),    
]