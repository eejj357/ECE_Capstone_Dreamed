from django.shortcuts import render
from detail.data_utils import save_auditions_from_csv
from detail.models import Audition
import csv

def detail(request):
    # 데이터가 이미 존재하는지 확인
    if not Audition.objects.exists():
        # 데이터가 없으면 CSV 파일에서 가져와서 저장
        save_auditions_from_csv('C:\\Users\\heinh\\django_work\\mysite\\detail\\임시상시데이터.csv')

    # 데이터 조회
    auditions = Audition.objects.all()

    return render(request, 'detail1.html', {'auditions': auditions})