from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import Profile, Contact
import datetime
from .forms import ContactForm
from .utils.analytics import get_info
# Create your views here.


def index(request):
    get_info(request)
    template = loader.get_template('index.html')
    profile= Profile.objects.get(id = 1)
    context = {}
    year = datetime.datetime.today().year
    context['profile'] = profile
    context['year'] = year
    profile.list_titles()
    return HttpResponse(template.render(context, request))

def recieve_contact(request):
    get_info(request)
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            new_record = form.save(commit=False)
            new_record.date = datetime.datetime.now()
            new_record.save()

            return JsonResponse({'success':True})
        else:
            print(form.errors)
            return JsonResponse({'success':False})

