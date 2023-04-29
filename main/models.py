from django.db import models


class Categorys(models.Model):
	name = models.CharField('Category', max_length = 20)

	def __str__(self):
		return self.name


class Product(models.Model):
	img = models.TextField('Product Image Link')
	name = models.TextField('Product Name')
	price = models.IntegerField('Product Price (UZS)')
	pub_date = models.DateTimeField(auto_now_add = True)
	category = models.ForeignKey(Categorys, on_delete = models.CASCADE)

	def __str__(self):
		return self.img
	def __str__(self):
		return self.pub_date
	def __str__(self):
		return self.price
	def __str__(self):
		return self.name