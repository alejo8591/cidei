from django import forms

from app.models import L_TYPES, Category, Item

class CategoryForm(forms.Form):
	name = forms.CharField(max_length=255)
	slug = forms.SlugField(max_length=255)
	description = forms.CharField(widget=forms.Textarea)
	update_category = forms.DateTimeField()
	
# Reference : http://stackoverflow.com/questions/11443658/how-do-i-add-a-class-to-a-choicefield-in-django
# Reference : http://stackoverflow.com/questions/7910353/django-change-the-dom-id-at-form-field-level
class ItemForm(forms.Form):
	listing = forms.ChoiceField(choices=L_TYPES, initial='t', widget=forms.Select(attrs={'id': 'id-listing','class':'cal'}))
	name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'id': 'id-name-item', 'class' : 'col'}))
	category = forms.ModelChoiceField(Category.objects.all())
	department = forms.CharField(max_length=255)
	description = forms.CharField(widget=forms.Textarea)
	update_item = forms.DateTimeField()

	def clean_department(self):

		data = self.cleaned_data['department']

		if data not in ['Desarrollo', 'Herramientas', 'Test']:
			raise forms.ValidationError('El Departamente puede ser "Desarrollo", "Herramientas" y/o "Test"')

		return data
