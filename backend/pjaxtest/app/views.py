from django.shortcuts import render_to_response, get_object_or_404, HttpResponseRedirect
from django.template import Context, RequestContext

# PRUEBA CON UN VIEW INICIAL
def entry_index(request):
    return render_to_response('entry_index.html', {}, context_instance = RequestContext(request))

# PRUEBA CON UN VIEW SECUNDARIO Y DE CARGA
def entry_index1(request):
    return render_to_response('entry_index1.html', {}, context_instance = RequestContext(request))