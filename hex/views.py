from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .models import Volunteer, Benefactor, Organizer, Events, EventRegistration
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.db.models import Count

TYPEOFEVENTS = {'Arts and Entertainment' : 'AE',
               'Business' : 'BZ',
               'Biological and Physical Sciences' : 'BP',
               'Education' : 'ED',
               'Environment' : 'EV',
               'Government' : 'GV',
               'Health &amp; Medicine' : 'HM',
               'International' : 'IT',
               'Law and Public Policy' : 'LP',
               'Nonprofit' : 'NP',
               'Society' : 'SO',
               'Technology' : 'TC'}
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
    vol_nr = None
    userType = getUserType(request.user.id)
    if (userType == "Volunteer"):
        vol = Volunteer.objects.get(user = request.user.id)
        city = vol.location
        choices = vol.preferences
        #choices = "AA, BB, DD"
        print(choices)
        choice_list = str(choices)
        choice_list = choice_list.split(",")
        print(choice_list)
        set_events = Events.objects.filter(type__in = choice_list)[:20].annotate(count = Count('eventregistration'))
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
    userType = getUserType(request.user.id)
    if not event:
        raise Http404
    return render(request, 'hex/eventpage.html', {"event":event,
                                            "userType": userType,})

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
        event = Events(title=dictionary.get("formTitle"),
                                date = dictionary.get("eventDate"),
                            	description = dictionary.get("formDescription"),
                                city = dictionary.get("myCity"),
                                adress = dictionary.get("myAdress"),
                                organizer = request.user,
                                duration = dictionary.get("formDistance"),
                                type = TYPEOFEVENTS.get(dictionary.get("formName")))
        event.save()
        return redirect(event_view, event_id=event.id )
    else:
        return render(request, 'hex/create-event.html',)

def event_register(request, event_id):
    reg_event = Events.objects.get(pk=event_id)
    new_registration = EventRegistration(user = request.user, event =  reg_event)
    new_registration.save()
    return HttpResponse(status=200)

def event_deregister(request, event_id):
    reg_event = Events.objects.get(pk=event_id)
    event = EventRegistration.objects.get(user = request.user, event = reg_event).delete()
    return HttpResponse(status=200)

@login_required
def setup(request):
    if (getUserType(request.user.id) == "Volunteer"):
        vol = Volunteer.objects.get(user = request.user.id)
        choices = vol.preferences
        choice_list = str(choices)
        choice_list = choice_list.split
        return render(request, 'hex/setup.html', {"list": choice_list})
    return render(request, 'hex/setup.html', )


def profile(request, userid):
    u = User.objects.get(pk=userid)
    type = getUserType(userid)
    p = None
    if type == "Volunteer":
        p = Volunteer.objects.get(user_id = userid)
    if type == "Organizer":
        p = Organizer.objects.get(user_id = userid)
    if type == "Benefactor":
        p = Benefactor.objects.get(user_id = userid)
    return render(request, 'hex/profile_page.html', {"user":u,
                                                    "profile":p})
