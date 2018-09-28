
from django.contrib import admin
# �ϸ�ũ �� �𵨿��� Ŭ���� ����Ʈ
from bookmark.models import Bookmark
# ���� Ŭ�������� ����Ʈ ��� �ʵ� �׸��� 2�� ����


class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')


admin.site.register(Bookmark, BookmarkAdmin)
