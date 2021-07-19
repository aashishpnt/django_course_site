from django.shortcuts import render
# Create your views here.

def index(request):
    meetups = [
        {
            "title":"A first meetups",
            "location": "Kathmandu",
            "slug": "a-first-meetups",
        },
        {
            "title": "A second meetups",
            "location": "Dhangadhi",
            "slug": "A-second-meetups",
        }
    ]
    return render(request, "meetups/index.html",{
        "meetups": meetups
    })
def meetup_detail(request, meetup_slug):
    print(meetup_slug)
    selected_meetup = {
            "title": "A first meetups",
            "description": "This is the first meetup!",
        }
    return render(request, "meetups/meetup-detail.html", {
        'meetups_title' : selected_meetup["title"],
        'meetups_description' : selected_meetup["description"] 
    })
    