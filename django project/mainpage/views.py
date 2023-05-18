from django.shortcuts import render
from .forms import YearForm
from detail.data_utils import save_auditions_from_csv
from detail.models import Audition
import csv

def main1(request):
    # if request.method == 'POST':
    #     form = YearForm(request.POST)
    #     if form.is_valid():
    #         year = form.cleaned_data['year']
    #         # year 변수에 입력받은 연도 값이 저장됨
    #         # 추가적인 로직 수행
    # else:
    #     form = YearForm()
    if not Audition.objects.exists():
        # 데이터가 없으면 CSV 파일에서 가져와서 저장
        save_auditions_from_csv('C:\\Users\\heinh\\django_work\\mysite\\mainpage\\임시상시데이터.csv')

    # 데이터 조회
    auditions = Audition.objects.all()

    return render(request, 'main1.html', {'auditions': auditions})