from django.db import models

# Create your models here.
from django.utils import timezone
import datetime

class Poll (models.Model):
    question_txt = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_txt

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    # 관리자 화면의 목록에서 변경위해 추가.
    was_published_recently.admin_order_field = pub_date
    was_published_recently.boolean = True
    was_published_recently.short_description = '최근에 publish되었는가?'

class Choice (models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_txt = models.CharField(max_length=300)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_txt