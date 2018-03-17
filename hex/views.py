from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .models import Volunteer, Benefactor, Organizer, Events
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('feed')
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
    if request.user.is_authenticated:
        return redirect('feed')
    if request.method == 'POST':
        dictionary = request.POST
        user = authenticate(username=dictionary.get("username"),
                            password=dictionary.get("password"))
        login(request,user)
        return redirect('feed')
    else:
        return render(request, 'hex/login.html', )

@login_required
def feed(request):
    userType = getUserType(request.user.id)
    if (userType == "Volunteer"):
        vol = Volunteer.objects.get(user = request.user.id)
        city = vol.location
        choices = vol.preferences
        choices = "AA, BB, DD"
        print(choices)
        choice_list = choices.split(", ")
        print(choice_list)
        set_events = Events.objects.filter(type__in = choice_list)[:20]
    if (userType == "Organizer"):
        set_events = Events.objects.filter(organizer_id = request.user.id)
    if (userType == "Benefactor"):
        set_events = None
    return render(request, 'hex/feed.html', {"userType": userType,
                                                "events": set_events,})


def index(request):
    if request.user.is_authenticated:
        return redirect('feed')
    return render(request, 'hex/index.html', )


def event_view(request, event_id):
    event = Events.objects.get(pk=event_id)
    if not event:
        raise Http404
    return render(request, 'hex/eventpage.html', {"event":event})

def getUserType(id):
    if Volunteer.objects.filter(user=id):
        return "Volunteer"
    if Organizer.objects.filter(user=id):
        return "Organizer"
    if Benefactor.objects.filter(user=id):
        return "Benefactor"


@login_required
def create_event(request):
    if request.method == 'POST':
        dictionary = request.POST
        print(dictionary)
        User.objects.create_user(title=dictionary.get("formTitle"),
                                date = dictionary.get("eventDate"),
                            	description = models.TextField(),
                            	organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE),
                                duration = dictionary.get("formDistance"))
    else:
        return render(request, 'hex/create-event.html',)

def event_register(request, event_id):
    pass

def event_deregister(request, event_id):
    pass

@login_required
def setup(request):
    return render(request, 'hex/setup.html', )
