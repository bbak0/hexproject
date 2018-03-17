from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .models import Volunteer, Benefactor, Organizer
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.
def signup(request):
    #print(request.POST)
    if request.method == 'POST':
        dictionary = request.POST
        print(dictionary)
        dummy_data = {"username" : "dupex",
                        "fullname" : "Jan Boratynski",
                        "password" : "dupa123",
                        "telephone" : "997",
                        "email" : "jan@wsadzicitam.pl",
                        "usertype" : "Benefactor"}

        #TODO INPUT VERIFICATION
        errors = {"username" : False, "email" : False, "passwordmatch" : False,
                }
        if User.objects.filter(username=dictionary.get("username")).exists():
            pass


        User.objects.create_user(username=dictionary.get("username"),
                                email=dictionary.get("email"),
                                password=dictionary.get("password"))
        user = authenticate(username=dictionary.get("username"),
                            password=dictionary.get("password"))
        login(request,user)
        if (dictionary.get("usertype") == "Benefactor"):
            Benefactor.objects.get_or_create(user = user)
        elif (dictionary.get("usertype") == "Volunteer"):
            Volunteer.objects.get_or_create(user = user)
        elif(dictionary.get("usertype") == "Organizer"):
            Organizer.objects.get_or_create(user = user)

        return redirect('feed')
    else:
        return render(request,'hex/signin.html',)

def login_view(request):
    return render(request, 'hex/login.html', )

def feed(request):
    userType = getUserType(request.user.id)
    if userType == "Volunteer":
        events = getVolunteerEvents(request)
    return render(request, 'hex/feed.html', {"userType": userType})


def index(request):
    return render(request, 'hex/index.html', )


def event_view(request, event_id):
    event = Events.objects.get(pk=event_id)
    if not event:
        raise Http404
    return render(request, 'hex/eventpage.html', {"event" : event})

def getUserType(id):
    if Volunteer.objects.filter(user=id):
        return "Volunteer"
    if Organizer.objects.filter(user=id):
        return "Organizer"
    if Benefactor.objects.filter(user=id):
        return "Benefactor"

def getVolunteerEvents(request):
    pass

def create_event(request):

    return render(request, 'hex/create-event.html', )
