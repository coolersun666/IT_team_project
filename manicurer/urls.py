from django.conf.urls import url

from IT_team_project import settings
from manicurer import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'about/$', views.about, name='about'),
    url(r'contact/$', views.contact, name='contact'),
    url(r'^hotest/$', views.hotest, name='hotest'),
    # url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
    # url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
    url(r'^hotest/$', views.like_Picture, name='like_Picture'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^media/myupload/$', views.myupload, name='myupload'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url( r'greatest/$', views.greatest, name="greatest" ),
]