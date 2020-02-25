from django.shortcuts import render, get_object_or_404


from .models import Listing, Dutie, Academic, Skill, Benefit

# Create your views here.
def vacancies(request):
    listings = Listing.objects.order_by('-vacancy_date').filter(is_published=True)
    duties = Dutie.objects.all()
    academics = Academic.objects.all()
    skills = Skill.objects.all()
    benefits = Benefit.objects.all()

    context = {
        'listings': listings,
        'duties': duties,
        'academics': academics,
        'skills': skills,
        'benefits': benefits,
    }

    return render(request, 'vacancies/vacancies.html', context)


def vacancy(request, pk):
    vacancy = get_object_or_404(Listing, id=pk)

    context = {
        'vacancy': vacancy,
    }

    return render(request, 'vacancies/vacancy.html', context)