##### .../myapp/urls.py #####

from django.urls import path

#* Import parent app 'views' module.
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('db/', views.db_page, name='db'),
    path('form/', views.form_page, name='form'),
    path('form/submit-name/', views.submit_name, name='submit-name'),
    path('form/submit-shirt/', views.submit_shirt, name='submit-shirt'),
    path('form/submit-expense/', views.submit_expense, name='submit-expense'),
    path('form/thanks/', views.thanks, name='thanks'),
    path('form/test/submit_name', views.test_form_submit_name, name='test-submit-name'),
    path('ip', views.client_ip_view, name='ip'),
    path('testsimple/', views.test_simple, name='test-simple'),
    path('test/', views.test_page, name='test-page'),
]
