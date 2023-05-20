from django.shortcuts import render

from detail.data_utils import save_auditions_from_csv
from detail.models import Audition
import csv

def detail(request):
    return render(request, 'detail1.html', {})
    # 데이터가 이미 존재하는지 확인
    if not Audition.objects.exists():
        # 데이터가 없으면 CSV 파일에서 가져와서 저장
        save_auditions_from_csv('static/data/정기 샘플 데이터.csv')

    # 데이터 조회
    auditions = Audition.objects.all()

    return render(request, 'detail1.html', {'auditions': auditions})