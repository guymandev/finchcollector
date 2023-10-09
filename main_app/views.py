from django.shortcuts import render

finches = [
  {'name': 'Tweety Bird', 'breed': 'yellow canary', 'description': 'too smart and cute for his own good', 'age': 3},
  {'name': 'Precious', 'breed': 'chaffinch', 'description': 'cute song bird, with a relaxing and gentle song', 'age': 2},
]

# Create your views here.
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def finches_index(request):
  # We pass data to a template very much like we did in Express!
  return render(request, 'finches/index.html', {
    'finches': finches
  })