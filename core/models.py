from django.db import models
# from django.contrib.auth import g
# Create your models here.
from django.contrib import admin  
from django.db import models
# from django_countries.fields import CountryField
# from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from django.conf import settings
from sympy import true



LABEL_CHOICES = (
         ('P','primary'),
	     ('S','secondary'),
	     ('D','danger'),
	     ('W','warning'),
		 ('F','default')
)

TIME_CHOICES = (
         ('N','new'),
	     ('LS','last-week'),
	     ('LM','last-month'),
		 ('D','default')
)
class Brand(models.Model):
		title = models.CharField('اسم الفائة',max_length=100,null=True)
		image =models.ImageField(upload_to='Brand_Photos',null =True)

			
		@property
		def imageur(self):
				try:
					url = self.image.url
				except:
					url = ''
				return url
		def __str__(self):
			return f"{self.id} \t {self.title }"

class Item(models.Model):
		name = models.CharField('الاسم',max_length=100)
		price = models.FloatField('السعر')
		discount_price = models.FloatField('الخصم',null=True, blank=True)
		image = models.ImageField(upload_to='Items_Photos', null=True, blank=True)
		selection= models.ManyToManyField(Brand,related_name='brands')
		label= models.CharField(choices=LABEL_CHOICES, max_length=2)
		Version= models.CharField(choices=TIME_CHOICES, max_length=2,null= True)
		slug =models.SlugField(unique=False, null= False)
		discription = models.TextField(null=True, blank=True)

		@property
		@admin.display(
			ordering='enter order',
			description='enter name ',
			)
		def get_full_name(self):
				return self.name +"  "+self.description
		def __str__(self):
				return f"id {self.id} name :{self.name} and price :{self.price}" 

		def get_add_to_cart_url(self):
					return reverse("core:add-to-cart",kwargs={
							'slug':self.slug
					})	
		def get_add_to_summary(self):
					return reverse("core:add-to-summary",kwargs={
							'slug':self.slug
					})	
		def get_add_to_cart(self):
					return reverse("core:add-to-home",kwargs={
							'slug':self.slug})
					
		def get_remove_from_cart(self):
				return reverse("core:remove-from-cart",kwargs={
						'slug':self.slug
				})	
		def get_remove_all_from_cart_url(self):
				return reverse("core:remove-all",kwargs={
					
						'slug':self.slug	
				})		
		


		def get_Absolute_url(self):
				brandID = self.selection.all()
				# print(brandID)
				return reverse("core:product",kwargs={
						'slug':self.slug
				})	

		@property
		def imageURL(self):
				try:
					url = self.image.url
				except:
					url = ''
				return url

class PersonAdmin(admin.ModelAdmin):
	  list_display=['get_full_name']


	


class OrderItem(models.Model):
				user= models.ForeignKey(settings.AUTH_USER_MODEL,
											on_delete=models.CASCADE)
				item = models.ForeignKey(Item,on_delete=models.CASCADE)
				quantity = models.IntegerField(default=0) 
				ordered = models.BooleanField(default=False)

				def __str__(self):
						return f" {self.quantity } of  {self.item.name} "
				
				def get_total_price(self):
					return self.quantity * self.item.price
				
			
				
				
				def get_save_price(self):
					return self.quantity * self.item.discount_price	 
				def get_move_price(self):
						return self.get_total_price() - self.get_save_price()
				def get_final_price(self):
						if self.item.discount_price:
							return self.get_save_price()
						return self.get_total_price()	
				
			
			
class Order(models.Model):
				user = models.ForeignKey(settings.AUTH_USER_MODEL,
										              on_delete=models.SET_NULL,null=True)
				items= models.ManyToManyField(OrderItem,blank=True)
				start_date= models.DateTimeField(auto_now_add=True)
				ordered_date= models.DateTimeField()
				ordered = models.BooleanField(default=False,blank=True)
				billing_address =models.ForeignKey('Information', on_delete=models.SET_NULL,blank=True,null=True)

				def __str__(self):
					return f"{self.user.username} and Item : {self.item}" 
				def get_total(self):
					total=0
					for order_item in self.items.all():
						
						total += order_item.get_final_price()
					return total
                	
				def get_total_item(self):
					totalItem= self.items.all()
					totalItem=sum(item.quantity for item in totalItem)
					return totalItem
			

class Bank(models.Model):
			name = models.CharField(max_length=15)
			image = models.ImageField(null=True, blank=True)
			def __str__(self):
					return self.name
			

			@property
			def imageurl(self):
				try:
					url = self.image.url
				except:
					url = ''
				return url
			
class Information(models.Model):
			user = models.ForeignKey(settings.AUTH_USER_MODEL,
										on_delete=models.CASCADE,blank=True ,null=True)
						
			first =models.CharField(max_length=15 , null =True)
			last =models.CharField(max_length=15 , null =True)
			email =models.EmailField()
			address =models.CharField(max_length=20)
			state = models.TextField(max_length=50)
			# countries = CountryField(multiple=True)

			def __str__(self):
				return self.user.username


