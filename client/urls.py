from django.urls import path
from .import views
urlpatterns = [
    path('', views.listall, name='list'),
    path('create', views.createClient, name='create'),
    path('update/<int:id>', views.Update, name='update'),
    path('delete/<int:id>', views.delete, name='delete')
]
