from django.conf.urls import url
from . import views

app_name = 'blog'

urlpatterns = [
	url(r'^$',views.index, name = 'index'),
	url(r'^view/(?P<slug>[^\.]+).html', views.view_post, name = 'view_post'),
	url(r'^category/(?P<slug>[^\.]+).html', views.view_category,name = 'view_category'),
]