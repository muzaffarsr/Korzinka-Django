from django.forms import ModelForm, TextInput, NumberInput, Select
from main.models import Product, Categorys


class ProductForm(ModelForm):
	class Meta:
		model = Product
		fields = ['img', 'name', 'price', 'category']

		widgets = {
			'img':TextInput(attrs={
				'class':'form-control add_form',
				'placeholder':'Product Image Link'
			}),
			'name':TextInput(attrs={
				'class':'form-control add_form',
				'placeholder':'Product Name'
			}),
			'price':NumberInput(attrs={
				'class':'form-control add_form',
				'placeholder':'Product Price (UZS)'
			}),
			'category':Select(attrs={
				'class':'form-select add_form',
			})
		}


class CategoryForm(ModelForm):
	class Meta:
		model = Categorys
		fields = ['name']

		widgets = {
			'name':TextInput(attrs={
				'class':'form-control add_form',
				'placeholder':'Category Name'
			}),
		}