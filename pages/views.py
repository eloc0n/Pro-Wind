from django.shortcuts import render

from .models import About, Work, Experts

# Create your views here.
def index(request):

    works = Work.objects.all()
    abouts = About.objects.all()
    expert = Experts.objects.all()

    context = {
        'abouts': abouts,
        'works': works,
        'expert': expert,
    }

    return render(request, 'pages/index.html', context)


def vacancies(request):
    return render(request, 'vacancies/vacancies.html')


def vacancy(request):
    return render(request, 'vacancies/vacancy.html')