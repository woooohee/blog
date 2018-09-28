from django.shortcuts import render

def tabularBookmark(request):
    bookmarks = Bookmark.objects.all().order_by('id')
    return render(request, 'bookmark/tabular_list.html', {'bookmarks': bookmarks})

from django.views.generic import ListView, DetailView
# �� Ŭ���� ����Ʈ
from bookmark.models import Bookmark
# �ϸ�ũ ���̺��� ��ü ���ڵ� ����Ʈ ����� ���� ��
class BookmarkLV(ListView):
    model = Bookmark
# 1) ����Ʈ ���ؽ�Ʈ ���� object_list�� ����
# 2) ����Ʈ ���ø� ���ϸ� �ҹ��ڸ𵨸�_list.html = bookmark_list.html
# �ϸ�ũ ���̺��� Ư�� ���ڵ� �� ����� ���� ��
class BookmarkDV(DetailView):
    model = Bookmark
# 1) ����Ʈ ���ؽ�Ʈ ���� object�� ����
# 2) ����Ʈ ���ø� ���ϸ� �ҹ��ڸ𵨸�_detail.html = bookmark_detail.html
# �⺻ Ű�� ��ȸ�ϴ� ���, �� Ŭ���� �� �����ϸ�,
# r'^bookmark/(?P<pk>)\d+)/$'�� ���� �⺻ Ű ���� �ڵ����� �μ� ���޵�
