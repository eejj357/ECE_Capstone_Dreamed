from django.shortcuts import render, HttpResponseRedirect
from .forms import YearForm


def main1(request):
    form = YearForm(initial={'year': 2000})
    template_name = 'main1.html'

    if request.method == 'POST':
        form = YearForm(request.POST)
        if form.is_valid():
            year = form.cleaned_data['year']
            # year 변수에 입력받은 연도 값이 저장됨
            # 추가적인 로직 수행
            print('year=', year)
            return HttpResponseRedirect('/main1')

    context = {'form': form}
    return render(request, template_name, context)