from django.shortcuts import render,redirect

# Create your views here.
from app1.models import student
from app1.form import st_form

def details(request):
    data = student.objects.all()

    context = {
        'data' : data
    }
    return render(request, 'home.html', context)


def studentfrom(request):
    form = st_form()
    if request.method == 'POST':
        form = st_form(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home1')
    else:
        form = st_form()
    context = {
        'form' : form
    }

    return render(request, 'stdform.html', context)

