from django.conf.urls import url
from.import views

app_name='accounts'

urlpatterns = [
    url(r'^$',views.main,name="account_main")
]
