from django.urls import include, path
from .import views 

urlpatterns=[
    path('', views.show, name='showinfo'),
    path('create/', views.post, name='post'),
    path('update/<int:user_id>/', views.put, name='update'),
    path('delete/<int:user_id>/', views.drop, name='delete'),
]



#path('update/<int:user_id>/', views.update, name='put'),
#path('delete/<int:user_id>/', views.delete, name='drop')