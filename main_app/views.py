from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Finch

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
    return render(request, 'finches/detail.html', {
       'finch': finch
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