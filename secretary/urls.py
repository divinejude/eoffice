from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'secretary'
urlpatterns = [
    url(r'^$', views.dashboard, name='s_dashboard'),
    url(r'^history$', views.FileIndexView.as_view(), name='history'),
    url(r'^login$', views.LoginFormView.as_view(), name='login'),
    url(r'^upload$', views.FileCreate.as_view(), name='upload'),
    # url(r'^(?P<file_id>[0-9]+)/$', views.append_file_no, name='append_file_no'),
    url(r'^(?P<pk>[0-9]+)/$', views.FileDetailView.as_view(), name='detail'),
    path('append/<int:file_id>/', views.append_file_no, name="append_file_no"),
    path('<int:file_id>/<int:user_id>/', views.comment, name="comment")
]
