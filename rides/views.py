from django.shortcuts import render, redirect
from .models import Person
from .forms import RideForm, NewRideForm
from django.db.models import Q  

def index(request):
    form = RideForm(request.GET or None)  # Instantiate RideForm 
    context = {
        "form": form,
        "new_ride_form": NewRideForm()
    }

    if request.method == 'GET' and form.is_valid():
        # Get form data for separate origination and destination
        origination_city = form.cleaned_data.get('origination_city', '')
        origination_state = form.cleaned_data.get('origination_state', '').upper()  # Convert to uppercase
        destination_city = form.cleaned_data.get('destination_city', '')
        destination_state = form.cleaned_data.get('destination_state', '').upper()

        # Construct query based on input
        origination_query = Q()
        destination_query = Q()
        
        if origination_city:
            origination_query &= Q(origination_city__iexact=origination_city)
        if origination_state:
            origination_query &= Q(origination_state__iexact=origination_state)
        if destination_city:
            destination_query &= Q(destination_city__iexact=destination_city)
        if destination_state:
            destination_query &= Q(destination_state__iexact=destination_state)

        # Combine queries: show results matching either origination or destination
        combined_query = origination_query & destination_query
        context['people'] = Person.objects.filter(combined_query)
    else:
        context['people'] = Person.objects.none()  # No results if form is invalid or not GET

    return render(request, "index_view.html", context)

def create(request):
    if request.method == "POST":
        form = NewRideForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  
        else:
            return render(request, 'form.html', {'new_ride_form': form})
    return redirect('form')

def form(request):
  context = {}
  context["form"] = RideForm()
  context["new_ride_form"] = NewRideForm()
  return render(request, "form.html", context)
