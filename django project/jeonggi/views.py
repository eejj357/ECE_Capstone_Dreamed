from django.shortcuts import render, get_object_or_404
from jeonggi.data_utils import save_auditions_from_csv
from jeonggi.models import Jeonggi_Audition
from django.template.loader import render_to_string
from django.db.models import Q
import csv
from .forms import YearForm

def jeonggi_list(request):
    # 오디션 목록 조회 로직

    if not Jeonggi_Audition.objects.exists():  # 데이터가 이미 존재하는지 확인
        # 데이터가 없으면 CSV 파일에서 가져와서 저장
        save_auditions_from_csv('static/data/임시정기데이터.csv')

    jeonggi_auditions = Jeonggi_Audition.objects.all()  # 데이터 조회

    form = YearForm(initial={'year': 2000})  # 나이 form 생성

    if request.method == 'POST':
        form = YearForm(request.POST)
        if form.is_valid():
            year = form.cleaned_data['year']
            # year 변수에 입력받은 연도 값이 저장됨
            # 추가적인 로직 수행
            print('year=', year)
            return HttpResponseRedirect('/jeonggi')

    return render(request, 'jeonggi_list.html', {'jeonggi_auditions': jeonggi_auditions, 'form': form})

def jeonggi_detail(request, pk):
    # 특정 오디션 상세 정보 조회 로직
    audition = get_object_or_404(Jeonggi_Audition, pk=pk)
    return render(request, 'jeonggi_detail.html', {'audition': audition})

def filtered_jeonggi_list(request):
    # POST 요청인 경우 필터링 옵션 받기
    recruitment_field_f = request.GET.getlist('recruitment_field[]')
    gender_f = request.GET.get('gender')

    q = Q()
    if recruitment_field_f:
        for option in recruitment_field_f:
            q &= Q(recruitment_field__contains=option)

    if gender_f:
        q &= Q(gender__contains=gender_f)

    result = Jeonggi_Audition.objects.filter(q)
    return render(request, 'jeonggi_list.html', {'jeonggi_auditions': result})