from django.db import models

class Jungi_Audition(models.Model):
    planning_agency = models.CharField(max_length=100) # 기획사 이름
    audition_name = models.CharField(max_length=100) # 오디션 이름
    recruitment_field = models.CharField(max_length=50) # 모집 분야
    age_group1 = models.IntegerField() # 시작나이
    age_group2 = models.IntegerField() # 끝나이
    gender = models.CharField(max_length=10) # 성별 남성/여성/무관
    due_date = models.DateField() # 년월일을 다루는 필드
    url = models.URLField() # URL넣는곳
    data_number = models.IntegerField() # 데이터 분류용 번호

    class Meta:
        app_label = 'mainpage2'