# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response, get_object_or_404, HttpResponseRedirect
from django.template import Context, RequestContext
from app.models import Item, Category, Picture
from app.forms import CategoryForm, ItemForm

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
	items = Item.objects.all()
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

def add_category(request):
	if request.method == "POST":
		form = CategoryForm(request.POST)
		if form.is_valid():
			# Crear un nuevo category
			category = Category.objects.create(
				name = form.cleaned_data['name'],
				slug = form.cleaned_data['slug'],
			)
			# Siempre que cree el dato correctamente redireccionar
			return HttpResponseRedirect('/categories/%s/' % category.slug)
	else:
		form = CategoryForm()

	context = Context({'title':'Creación de categorias', 'form': form})
	return render_to_response('add-category.html', context, context_instance=RequestContext(request))

def add_item(request):
	if request.method == "POST":
		form = ItemForm(request.POST)
		if form.is_valid():
			# Crear un nuevo item
			item = Item.objects.create(
				listing = form.cleaned_data['listing'],
				name = form.cleaned_data['name'],
				category=form.cleaned_data['category'],
				department=form.cleaned_data['department'],
				description = form.cleaned_data['description'],
				update_item = form.cleaned_data['update_item'],
			)
			# Siempre que cree el dato correctamente redireccionar
			return HttpResponseRedirect('/items/%s/' % item.id)
	else:
		form = ItemForm()

	context = Context({'title' : 'Adicionar item', 'form' : form})
	return render_to_response('add-item.html', context, context_instance=RequestContext(request))

