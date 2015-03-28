from django.http import HttpResponse
from django.template import RequestContext, loader


def index(request):
    template = loader.get_template('waterplants/index.html')
<<<<<<< HEAD
    context = RequestContext(request, { 'something': [1,2,3]})
    return HttpResponse(template.render(context))
=======
    myplants = [('Bob', 'Rose', 10), ('Jericho', 'Cactus', 99)] # (Name, Type, Number of seconds til Needs to be Watered)
    planttypes = ['Rose', 'Cactus', 'Venus Fly Trap'] # Plant type names
    context = RequestContext(request, { 'myplants': myplants, 'planttypes': planttypes} )
    return HttpResponse(template.render(context))

def waterplant(request):


def addplant(request):

>>>>>>> 6444104ac5871a0535a8673a980798e254cbd52b
