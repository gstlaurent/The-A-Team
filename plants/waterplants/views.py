from django.http import HttpResponse
from django.template import RequestContext, loader


def index(request):
    template = loader.get_template('waterplants/index.html')
    context = RequestContext(request, { 'something': [1,2,3]})
    return HttpResponse(template.render(context))