from django.http import HttpResponse
from django.template import RequestContext, loader
from waterplants.models import Plant
from waterplants.models import UserPlants

def index(request):
    template = loader.get_template('waterplants/index.html')
    
    myplants = UserPlants.objects.all() # (Name, Type, Number of seconds til Needs to be Watered)
    planttypes = Plant.objects.all() # Plant type names
    context = RequestContext(request, { 'myplants': myplants, 'planttypes': planttypes} )
    return HttpResponse(template.render(context))

# def waterplant(request):
    

# def addplant(request):
# plantName 
# plantType
