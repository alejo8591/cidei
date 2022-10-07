from django.shortcuts import render_to_response, get_object_or_404
from django.template import Context
from list.models import Item

def index(request):
	items = Item.objects.all()
	context = Context({'title' : 'Hola CIDEI', 'items' : items})
	return render_to_response('index.html', context)

def details(request, item_id):
	item = get_object_or_404(Item, id=item_id)
	context = Context({
		'title' : 'Detalle de: %s' % item.name,
		'item' : item
	})
	return render_to_response('details.html', context)