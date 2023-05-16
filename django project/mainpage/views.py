from django.shortcuts import render
from .forms import YearForm


def main1(request):
    # if request.method == 'POST':
    #     form = YearForm(request.POST)
    #     if form.is_valid():
    #         year = form.cleaned_data['year']
    #         # year 변수에 입력받은 연도 값이 저장됨
    #         # 추가적인 로직 수행
    # else:
    #     form = YearForm()

    return render(request, 'main1.html', {})  # 'form':form