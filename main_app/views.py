from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Finch
# Import the FeedingForm
from .forms import FeedingForm

# finches = [
#   {'name': 'Tweety Bird', 'breed': 'yellow canary', 'description': 'too smart and cute for his own good', 'age': 3},
#   {'name': 'Precious', 'breed': 'chaffinch', 'description': 'cute song bird, with a relaxing and gentle song', 'age': 2},
# ]

# Create your views here.
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  # We pass data to a template very much like we did in Express!
  finches = Finch.objects.all()
  return render(request, 'finches/index.html', {    
    'finches': finches
})

def finches_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    # instantiate FeedingForm to be rendered in the template
    feeding_form = FeedingForm()
    return render(request, 'finches/detail.html', {
       'finch': finch,
       'feeding_form': feeding_form
})

class FinchCreate(CreateView):
   model = Finch
   fields = '__all__'

class FinchUpdate(UpdateView):
    model = Finch
    fields = ['breed', 'description', 'age']

class FinchDelete(DeleteView):
   model = Finch
   success_url = '/finches'

def add_feeding(request, finch_id):
    # create a ModelForm instance using the data in request.POST
    form = FeedingForm(request.POST)
    # validate the form
    if form.is_valid():
       # don't save the form to the db until it
       # has the finch_id assigned
       new_feeding = form.save(commit=False)
       new_feeding.finch_id = finch_id
       new_feeding.save()

    return redirect('detail', finch_id=finch_id)