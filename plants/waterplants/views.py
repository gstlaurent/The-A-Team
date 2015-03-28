from django.http import HttpResponse
from django.template import RequestContext, loader

from waterplants.models import Plant

def index(request):
    template = loader.get_template('waterplants/index.html')

    myplants = Plant.objects.all()
    # myplants = [('Bob', 'Rose', 10), ('Jericho', 'Cactus', 99)] # (Name, Type, Number of seconds til Needs to be Watered)
    planttypes = ['Rose', 'Cactus', 'Venus Fly Trap'] # Plant type names


    context = RequestContext(request, { 'myplants': myplants, 'planttypes': planttypes} )
    return HttpResponse(template.render(context))

# def waterplant(request):

# def addplant(request):
# plantName 
# plantType
