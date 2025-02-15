from django.shortcuts import render
from .models import Conference
from userApp.models import Reservation
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import ConferenceForm
from django.urls import reverse_lazy

# Create your views here.
def conferenceList(req):
    liste = Conference.objects.all()
    # Select * from Conference 
    return render(req, 'conference_list.html', {'conferences': liste})

class ConferenceListView(ListView):
    model = Conference
    context_object_name = "conferences" #objects
    template_name = "conference_list.html"
    
class ConferenceDetailsView(DetailView):
    model = Conference
    template_name = "conference_detail.html"
    context_object_name = "conference"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        conference = self.get_object()
        # Récupérer les réservations associées à cette conférence
        context['reservations'] = Reservation.objects.filter(conference=conference)
        return context
    
class ConferenceCreateView(CreateView):
    model = Conference
    template_name = "conference_form.html"
    form_class = ConferenceForm
    success_url = reverse_lazy("conference_listView")
    
class ConferenceUpdateView(UpdateView):
    model = Conference
    template_name = "conference_form.html"
    form_class = ConferenceForm
    success_url = reverse_lazy("conference_listView")
    
class ConferenceDeleteView(DeleteView):
    model = Conference
    success_url = reverse_lazy("conference_listView")
    template_name = "conference_confirm_delete.html"
    
