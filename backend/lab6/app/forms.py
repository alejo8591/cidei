from django import forms

from app.models import L_TYPES, Category, Item

class CategoryForm(forms.Form):
	name = forms.CharField(max_length=255)
	slug = forms.SlugField(max_length=255)
	"""
	class Meta:
		model = Category
	"""
class ItemForm(forms.Form):
	listing = forms.ChoiceField(choices=L_TYPES, initial='t')
	name = forms.CharField(max_length=255)
	category = forms.ModelChoiceField(Category.objects.all())
	department = forms.CharField(max_length=255)
	description = forms.CharField(widget=forms.Textarea)
	update_item = forms.DateTimeField()