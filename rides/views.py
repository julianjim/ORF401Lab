import os
from django.shortcuts import render, redirect
from .models import Person
from .forms import RideForm, NewRideForm
from django.db.models import Q 
from transformers import pipeline
from transformers import GPT2Tokenizer, GPT2LMHeadModel

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

def format_person_for_ai(person):
    return (f"{person.first_name} from {person.origination_city} to {person.destination_city} on {person.date}, "
            f"{person.vehicle_make}.")



def ai_interaction(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')

        rides_data = Person.objects.all()


        # Combine system message and user input
        formatted_rides = [format_person_for_ai(person) for person in rides_data]
        rides_summary = " ".join(formatted_rides)
        prompt = f"Given these available rides: {rides_summary} Find a suitable ride based on this request: {user_input}"
        
        # Load the text generation pipeline with the desired model
        generator = pipeline("text-generation", model="openai-community/gpt2")
        
        # Generate text based on combined prompt
        ai_text = generator(prompt, max_new_tokens=100, num_return_sequences=1)[0]['generated_text']
        
        final_ai_text = ai_text.split("AI:")[-1].strip()

        return render(request, 'index_view.html', {'ai_text': final_ai_text})
    
    return render(request, 'index_view.html')

def search_page(request):
    user_query = request.GET.get('query', '')
    user_history = request.session.get('search_history', [])
    ai_response = generate_ai_response(user_query, user_history)
    
    # Save the current query to the session history
    user_history.append(user_query)
    request.session['search_history'] = user_history
    
    return render(request, 'search_page.html', {'ai_response': ai_response})

def generate_ai_response(query, history):
    # Contextual data can be passed to the model to generate more relevant responses
    combined_context = f"Previous searches: {history}. Current search: {query}"
    generator = pipeline('text-generation', model='openai-community/gpt2')
    response = generator(combined_context, max_length=50, num_return_sequences=1)
    return response[0]['generated_text']