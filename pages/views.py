from django.shortcuts import render

from .models import About, Work, Expert

# Create your views here.
def index(request):

    works = Work.objects.all()
    abouts = About.objects.all()
    expert = Expert.objects.all()

    context = {
        'abouts': abouts,
        'works': works,
        'expert': expert,
    }

    return render(request, 'pages/index.html', context)


