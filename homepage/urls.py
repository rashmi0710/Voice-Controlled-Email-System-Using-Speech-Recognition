from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('compose.html', views.compose_view, name='compose'),
    path('inbox.html', views.inbox_view, name='inbox'),
    path('sent.html', views.sent_view, name='sent'),
    path('trash.html', views.trash_view, name='trash'),
    path('options.html', views.options_view, name='options')
]