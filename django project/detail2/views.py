from django.shortcuts import render
from detail2.data_utils import save_auditions_from_csv
from detail2.models import Jungi_Audition
import csv

def detail2(request):
    # 데이터가 이미 존재하는지 확인
    if not Jungi_Audition.objects.exists():
        # 데이터가 없으면 CSV 파일에서 가져와서 저장
        save_auditions_from_csv('C:\\Users\\heinh\\django_work\\mysite\\detail2\\임시정기데이터.csv')

    # 데이터 조회
    jungi_auditions = Jungi_Audition.objects.all()

    return render(request, 'detail2.html', {'jungi_auditions': jungi_auditions})