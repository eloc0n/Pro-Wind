from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core.mail import send_mail
from vacancies.models import Listing
from .models import Contact

# Create your views here.
def contact(request, pk):

    if request.method == 'POST':
        vacancy_id = request.POST['vacancy_id']
        vacancy = request.POST['vacancy']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        cover_letter = request.POST['cover_letter']
        user_id = request.POST['user_id']
        doc_file = request.FILES['document']
        

        # Check if user has applied already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(vacancy_id=vacancy_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'Already applied for this position')
                return redirect('/contacts/contact/'+vacancy_id)

        contact = Contact(vacancy=vacancy, 
                            vacancy_id=vacancy_id, 
                            name=name, 
                            email=email, 
                            phone=phone, 
                            cover_letter=cover_letter, 
                            user_id=user_id,
                            doc_file=doc_file)

        contact.save()

        # Send email
        # send_mail(
        #     'New vacancy application received',
        #     'There has been an application for ' + vacancy + '. Sign into the admin panel for more info.',
        #     'jani.bratja@gmail.com',
        #     ['johnisb.21@gmail.com'],
        #     fail_silently=False
        # )

        messages.success(request, 'Your request has been submitted!')

    vacancy = get_object_or_404(Listing, id=pk)
    
    context = {
        'vacancy': vacancy,
    }
    
    return render(request, 'contacts/contact.html', context)