from django.conf.urls import url
from Credential import views

app_name = 'Credential'

urlpatterns = [
    url(r'^Register/$',views.register,name='Register'),
    url(r'^user_login/$',views.user_login,name='user_login')
]