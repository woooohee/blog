from django.db import models
# �����
# ���̺��� (django.dbmodels.Model�� ��ӹ޴�) Ŭ������ �����ϰ�,
# ���̺� �÷��� Ŭ���� ������ ������


class Bookmark(models.Model):
    # id �ʵ�(Integer, PK, Auto Increment)�� �ڵ� ������
    title = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField('url', unique=True)

def __str__(self):
    return self.title