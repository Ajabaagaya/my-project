from tkinter.tix import Tree
from django import forms
from django.conf import LazySettings
from django.contrib.contenttypes.admin import GenericTabularInline
from django.contrib.admin.sites import AdminSite
from.models import *
from django.contrib.admin import ModelAdmin
# Register your models here.

# @admin.register(Item,Order,OrderItem,Brand)
class OrderAdmin(admin.ModelAdmin):
      list_display = ['user','start_date','ordered']

# class ImageInline(GenericTabularInline):
#     model = Section


# class ProductAdmin(admin.ModelAdmin):
#     inlines = [
#         ImageInline,
#     ]


# admin.site.register(Section, ProductAdmin)
 

#     filter_horizontal=('items',)
#     list_display =('user' , 'ordered', 'start_date')
#     # date_hierarchy=['start_date']
#     list_filter=('user' , 'ordered', 'start_date')
#     # list_select_related =('user',)
class OrderItemAdmin(forms.ModelForm):
    list_filter=('user','quantity')
    search_fields=('user','quantity')    
    
class ItemAdmin(admin.ModelAdmin):
 list_display=('name','price','discount_price','discription')
# list_editable=('price','discription',)
 ff=search_fields=('name','price')
 list_filter=('name','slug')
# class ItemAdmin(admin.ModelAdmin):
#      list_filter =[
#           ("selection",admin.RelatedOnlyFieldListFilter)
#      ]
class BrandAdmin(admin.ModelAdmin):
      list_filter =[
           ("title")
      ]
      search_fields =['title']
      list_display = ['title','image']
      view_on_site =True
      actions_on_top =False
      actions_on_bottom =True
      change_form_template=True
admin.site.register(OrderItem)
admin.site.site_header='Store Management System'
admin.site.index_title='الموج الارق'
# admin.site.register(ItemType) 
# admin.sites.site.logout_template
admin.site.disable_action("delete_selected")
AdminSite.enable_nav_sidebar =False
admin.site.register(Brand,BrandAdmin)
admin.site.register(Order,OrderAdmin)

admin.site.register(Bank)
admin.site.register(Information)

admin.site.register(Item,ItemAdmin)


# from django.contrib import admin
# from .models import Item, Attribute, Feature

# class AttributeInline(admin.StackedInline):
#     model = Brand
#     extra = 1

# class FeatureInline(admin.StackedInline):
#     model = Item
#     extra = 1

# class ItemAdmin(admin.ModelAdmin):
#     list_display = ('name', 'description', 'title', )
#     inlines = [AttributeInline, FeatureInline, ]

#     fieldsets = (
#         ('Main', {
#             'fields': ('name', ),
#             'classes': ('baton-tabs-init', 'baton-tab-inline-Item', 'baton-tab-fs-content', 'baton-tab-group-fs-tech--inline-OrderItem', ),
#             'description': 'This is a description text'

#         }),
#         ('Content', {
#             'fields': ('description', ),
#             'classes': ('tab-fs-content', ),
#             'description': 'This is another description text'

#         }),
#         ('Tech', {
#             'fields': ('title', ),
#             'classes': ('tab-fs-tech','baton-tab-inline-' ),
#             'description': 'This is another description text'

#         }),

#)
