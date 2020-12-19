import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
#질문 치는곳이랑 날짜 적는거를 이 클래스가 만들어줌 ㅎㅅㅎ
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date= models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >=timezone.now()- datetime.timedelta(days=1)

# was_published_recently 를 아이콘으로 변경 ox모양
    was_published_recently.admin_order_field='pub_date'
    was_published_recently.boolean=True
    was_published_recently.short_ddscription= 'Published recently?'

class Choice(models.Model):
    question= models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text= models.CharField(max_length=200)
    votes= models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

