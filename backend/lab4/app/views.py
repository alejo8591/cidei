from django.shortcuts import render_to_response, get_object_or_404
from django.template import Context
from app.models import Item, Category, Picture

def index(request):
	context = Context({'title' : 'Hola CIDEI'})
	return render_to_response('index.html', context)

def categories(request):
	categories = Category.objects.all()
	context = Context({'title' : 'Hola CIDEI', 'categories' : categories})
	return render_to_response('categories.html', context)

def category(request, slug):
	category = get_object_or_404(Category, slug=slug)
	context = Context({'title' : 'Detalle categoria', 'category' : category})
	return render_to_response('category-details.html', context)

def items(request):
	items = Category.objects.all()
	context = Context({'title' : 'Hola CIDEI', 'items' : items})
	return render_to_response('items.html', context)

def item(request, item_id):
	item = get_object_or_404(Item, id=item_id)
	pictures = Picture.objects.filter(item=item)
	count_pictures = pictures.count()
	context = Context({
		'title' : 'Hola CIDEI',
		'item' : item,
		'pictures':pictures,
		'count_pictures' : count_pictures
	})
	return render_to_response('item-details.html', context)