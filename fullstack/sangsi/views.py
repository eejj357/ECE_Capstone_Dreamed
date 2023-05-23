from django.shortcuts import render, get_object_or_404
from sangsi.data_utils import save_auditions_from_csv
from sangsi.models import Sangsi_Audition
from django.template.loader import render_to_string
from django.db.models import Q
import csv
from .forms import YearForm

def sangsi_list(request):
    # 오디션 목록 조회 로직

    if not Sangsi_Audition.objects.exists():  # 데이터가 이미 존재하는지 확인
        # 데이터가 없으면 CSV 파일에서 가져와서 저장
        save_auditions_from_csv('static/data/상시data.csv')

    sangsi_auditions = Sangsi_Audition.objects.all()  # 데이터 조회

    form = YearForm(initial={'year': 2000})  # 나이 form 생성

    if request.method == 'POST':
        form = YearForm(request.POST)
        if form.is_valid():
            year = form.cleaned_data['year']
            # year 변수에 입력받은 연도 값이 저장됨
            # 추가적인 로직 수행
            print('year=', year)
            return HttpResponseRedirect('/sangsi_')

    return render(request, 'sangsi_list.html', {'sangsi_auditions': sangsi_auditions, 'form': form})

def sangsi_detail(request, pk):
    # 특정 오디션 상세 정보 조회 로직
    audition = get_object_or_404(Sangsi_Audition, pk=pk)
    return render(request, 'sangsi_detail.html', {'audition': audition})


def filtered_sangsi_list(request):
    print('---- search_form request ----')
    # POST 요청인 경우 필터링 옵션 받기
    recruitment_field_f = request.GET.getlist('recruitment_field[]')
    print(recruitment_field_f)
    gender_f = request.GET.get('gender')
    # birth_year_f = request.GET.get('birth_year')
    print(gender_f)

    q = Q()
    if recruitment_field_f:
        for option in recruitment_field_f:
            q &= Q(recruitment_field__contains=option)
        
    # if birth_year_f:
    #     age = int(birth_year_f)
    #     q &= Q(age_group1__gte=age) & Q(age_group2__lte=age)
    #     q &= Q(age_group1=0) & Q(age_group2__lte = age)
    #     q &= Q(age_group1__gte=age) & Q(age_group2=0)

    if gender_f:
        q &= Q(gender__contains=gender_f)

    result = Sangsi_Audition.objects.filter(q)
    print(result)
    return render(request, 'sangsi_list.html', {'sangsi_auditions': result})
