from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, RSVP

def event_list(request):
    events = Event.objects.all().order_by('date')
    return render(request, "event_list.html", {"events": events})

def rsvp_view(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    if request.method == "POST":
        status = request.POST.get("status")
        RSVP.objects.create(
            user_id=1,  # temporary — you can replace with request.user.id if auth is enabled
            event=event,
            status=status
        )
        return redirect("events")

    return render(request, "rsvp_form.html", {"event": event})
