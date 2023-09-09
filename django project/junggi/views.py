from django.shortcuts import render, get_object_or_404
from junggi.data_utils import save_auditions_from_csv
from junggi.models import Jungi_Audition
import csv
from .forms import YearForm

def junggi_list(request):
    # 오디션 목록 조회 로직

    if not Jungi_Audition.objects.exists():  # 데이터가 이미 존재하는지 확인
        # 데이터가 없으면 CSV 파일에서 가져와서 저장
        save_auditions_from_csv('static/data/정기data.csv')

    jungi_auditions = Jungi_Audition.objects.all().order_by('data_number')  # 데이터 조회

    form = YearForm(initial={'year': 2000})  # 나이 form 생성

    if request.method == 'POST':
        form = YearForm(request.POST)
        if form.is_valid():
            year = form.cleaned_data['year']
            # year 변수에 입력받은 연도 값이 저장됨
            # 추가적인 로직 수행
            print('year=', year)
            return HttpResponseRedirect('/junggi')

    return render(request, 'junggi_list.html', {'jungi_auditions': jungi_auditions, 'form': form})

def junggi_detail(request, pk):
    # 특정 오디션 상세 정보 조회 로직
    audition = get_object_or_404(Jungi_Audition, pk=pk)
    return render(request, 'junggi_detail.html', {'audition': audition})