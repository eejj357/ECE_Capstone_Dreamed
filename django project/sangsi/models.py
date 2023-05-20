from django.db import models

class Audition(models.Model):
    planning_agency = models.CharField(max_length=100) #기획사 이름
    recruitment_field = models.CharField(max_length=50) #모집 분야
    age_group1 = models.IntegerField() #시작나이 예시로 2000이라 입력되면 2000년생 이전태생 int필드이기 때문에 2099를 넣는 것으로 제한 없음을 표현 csv에서 제한 없음을 읽으면 2099로 가공하는 과정 필요
    age_group2 = models.IntegerField() # 끝나이 예시로 1990이라 입력되면 1990이후 태생
    gender = models.CharField(max_length=10) #성별 남성/여성/무관
    url = models.URLField() # URL넣는곳
    data_number =models.IntegerField() # 데이터 분류용 번호

    class Meta:
        app_label = 'sangsi'