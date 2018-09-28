from django.conf.urls import url
from . import views # views.~ �������� �����ؾ� ��
urlpatterns = [
# �ϸ�ũ ���� ���� Ŭ���� ��� ��
# /bookmark/ ��û�� ó���� �� Ŭ������ BookmarkLV�� �����ϰ�, URL ���� �̸� ����
url(r'^bookmark/$', views.BookmarkLV.as_view(), name='index'),
# /bookmark/����/ ��û�� ó���� �� Ŭ������ BookmarkDV�� �����ϰ�, URL ���� �̸� ����
url(r'^bookmark/(?P<pk>\d+)/$', views.BookmarkDV.as_view(), name='detail'),
# tabular list
url(r'^bookmark_t_FBV/$', views.tabularBookmark, name='index_t_FBV'),
url(r'^bookmark_t_CBV/$', views.BookmarkLV.as_view(), name='index_t_CBV'),
]