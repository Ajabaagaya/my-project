from django.shortcuts import render
import struct 
import json
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from.form import CheckoutForm
from django.views.generic import ListView,DetailView,View,UpdateView

from django.utils import timezone
from . models import *
from django.contrib import messages
from django.core.mail import send_mail,BadHeaderError
 



class ListItem(ListView):
      print("goood work")
      model = Item
      paginate_by =4
      template_name = 'home-page.html'

# def Home(request,id):
#        bransID = Brand.objects.get(id=id)
#        item = Item.objects.all()
#        order =Order.objects.get(user=request.user,ordered=False)
#        items = bransID.brands.all()
#        section=Brand.objects.all()
#        # order =Order.objects.get(user=request.user,ordered= False)
       

      

#        return render(request,"home-page.html",{
#               "object_list":items,
#               "object":order,
#        })
def  Nav(request):
       return render(request,"")



class CheckoutView(View):
       def get(self , *args,**kwargs):
                order=Order.objects.filter(user = self.request.user,ordered =False)
                # total = order.get_total_item
                bank=Bank.objects.all()

                context = {
                    'form' :CheckoutForm(),
                    'object':order,
                    'pays':bank,
                }
                return render(self.request,'checkout-page.html',context)


       def post(self , *args,**kwargs):
           form = CheckoutForm(self.request.POST or None)
          
           print(self.request.POST)
           try:
              order=Order.objects.get(user = self.request.user,ordered=False)
              if form.is_valid():
                     first=form.clean_data.get('first')
                     last=form.clean_data.get('last')
                     email=form.clean_data.get('email')
                     address=form.clean_data.get('address')
                     # country=form.clean_data.get('country')
                     state = form.clean_data.get('state')
                     payment_option = form.clean_data.get('payment_option')
                     billing_address = Informtion(
                            user = self.request,
                            first=first,
                            last=last,
                            email=email,
                            address=address,
                            state=state,
                            # country=country
                     )
                     print(self.request.POST)
                     print(form.cleaned_data) 
                     billing_address.save()
                     order.billing_address=billing_address
                     order.save()
                     return redirect('core:checkout')
              messages.error(self.request,"ليسا لديك اي عنصر بعد")   
              return redirect("core:checkout")
           except ObjectDoesNotExist:
                  messages.warning(self.request,"فشل في تسجيل معلوماتك")
                  return redirect('core:checkout')

class PaymentView(View):
      def get(self,*args,**kwargs):
           return render(self.request,"payment.html")
      def post(self,*args,**kwargs):
             return render(self.request,"core:checkout")
def UpdateItem(request):
       # data = json.loads(request.body)
       # productId = data['productId']
       # action = data['action']
       # print('productId  :',productId)
       # print('action  :',action)
       return JsonResponse("is there do not worry ",safe=False)

# class ScrollView(ListView):
#        model = Item
# #        template_name = "product.html"
# class ItemDetailView(DetailView,View):
#        model = Item
#        template_name = "product.html" 
    
def listItem(request,slug):
       
       item = Item.objects.get(slug=slug)
       # brands= Brand.objects.get(pk=id)
       print(item)
       # order =Order.objects.filter(user=request.user,ordered= False)
       items = Item.objects.all()
       return render(request,"product.html",{
              "object":item,
              "items":items,

       })  
@login_required
def main(request):
       item= Item.objects.all()
       section=Brand.objects.all()
       # order =Order.objects.get(user=request.user,ordered= False)
       

       context={
       "items":item,
       # "objec":order
       'sections':section

       }
       return render(request,"selection-page.html",context)
 

       

class OrderSummaryView(LoginRequiredMixin,View):
     def get(self,*args,**kwargs):
            try:
                order =Order.objects.get(user=self.request.user,ordered= False)
                context = {
                       "object": order,
               }
                return render (self.request, "Order_Summary.html",context)
            except ObjectDoesNotExist:
                   messages.error(self.request,"ليسا لديك اي عناصر بعد")
                   return redirect ( "/")   


#     def post(self, request, *args, **kwargs):
#            return render(request,"home.html",)
       


 
# def watch(request):
#        context={
#              'object':Watch.objects.get(user=self.request.user)
#        }
#        return render(request,"watch.html",context)
login_required
def add_to_Summary(request,item_id):
       item  = Item.objects.get(id=item_id)
       order_item, created  = OrderItem.objects.get_or_create(
                     item = item ,
                     user =request.user,
                     ordered=False
              )
       order_qs = Order.objects.filter(user=request.user,ordered =False) 
       if order_qs.exists():
              order = order_qs[0]
              if order.items.filter(item__id = item.id).exists():
                     order_item.quantity += 1
                     order_item.save()
                     messages.info(request,"the item quantity was updated successfully")
              else:
                     messages.info(request,"the item was added to your cart successfully")
                     order.items.add(order_item)
       else:
              ordered_date = timezone.now()
              order = Order.objects.create(
              user=request.user,
              ordered_date=ordered_date,
              )
              Order.items.add(order_item)
              messages.info(request,"the item quantity was updated .")
              return redirect("core:Order-summary" )
       return redirect("core:Order-summary")



login_required
def add_to_cart(request,slug): 
       item  = get_object_or_404(Item, slug=slug)
       order_item  , created  = OrderItem.objects.get_or_create(
              item = item ,
              user =request.user,
              ordered=False
       )
       order_qs = Order.objects.filter(user=request.user,ordered = False) 
       if order_qs.exists():
              order = order_qs[0]
              if order.items.filter(item__slug = item.slug).exists():
                     order_item.quantity += 1
                     order_item.save()
                     messages.info(request,"the item quantity was updated successfully")
              else:
                     messages.info(request,"the item was added to your cart successfully")
                     order.items.add(order_item)
       else:
              ordered_date = timezone.now()
              order = Order.objects.create(
              user=request.user,
              ordered_date=ordered_date,
              )
              Order.items.add(order_item)
              messages.info(request,"the item quantity was updated .")
              return redirect("core:product",slug=slug )
       return redirect("core:product",slug=slug)



login_required
def remove_from_card(request,slug):
       item  = get_object_or_404(Item, slug=slug)
       order_sq= Order.objects.filter(
              user=request.user,
              ordered = False
              ) 
     
       if order_sq.exists():
              order=order_sq[0]
              if order.items.filter(item__slug=item.slug).exists():
                     order_item = OrderItem.objects.filter(
                                   item = item,
                                   user= request.user,
                                   ordered = False

                            )[0]
                     if order_item.quantity > 0:
                            order_item.quantity -=1
                            order_item.save()
                     else:
                            order_item.adelete()

                     messages.info(request,"the item was removed from your cart successfully")
              else:
                      messages.info(request,"the item was not in your cart")
                     # redirect("core:product",kwargs={slug==slug})
                    
       else:
              messages.info(request,"you did not have an active order")
              return redirect("core:product",slug=slug )
       return redirect("core:product",slug=slug)
        



def Remove_from_Summary(request,item_id):
       item  = get_object_or_404(Item, id=item_id)
       order_sq= Order.objects.filter(
              user=request.user,
              ordered = False
              ) 
     
       if order_sq.exists():
              order=order_sq[0]
              if order.items.filter(item__id=item.id).exists():
                     order_item = OrderItem.objects.filter(
                                   item = item,
                                   user= request.user,
                                   ordered = False

                            )[0]
                     if order_item.quantity >0:
                            order_item.quantity -=1
                            order_item.save()
                     messages.info(request,"the item was removed from your cart successfully")
              else:
                      messages.info(request,"the item was not in your cart")
                     # redirect("core:product",kwargs={slug==slug})
                    
       else:
              messages.info(request,"you did not have an active order")
              return redirect("core:Order-summary" )
       return redirect("core:Order-summary")

def Remove_All(request,slug):
       item  = get_object_or_404(Item, slug=slug)
       order_sq= Order.objects.filter(
              user=request.user,
              ordered = False
              ) 
     
       if order_sq.exists():
              order=order_sq[0]
              if order.items.filter(item__slug=item.slug).exists():
                     order_item = OrderItem.objects.filter(
                                   item = item,
                                   user= request.user,
                                   ordered = False

                            )[0]
                     if order_item.quantity >=0:
                            order_item.delete()
                           
                     messages.info(request,"the item was removed from your cart successfully")
           
       else:
              messages.info(request,"you did not have an active order")
              redirect("core:Order-summary")
        
       return redirect("core:Order-summary")
       
class OrderList(LoginRequiredMixin,View):
     def get(self,*args,**kwargs):
            try:
              
                return render (self.request, "item-list.html",context)
            except ObjectDoesNotExist:
                   messages.error(self.request,"ليسا لديك اي عناصر بعد")
                   return redirect ( "/") 
                   
login_required
def add_to_home(request,item_id):
       item  = Item.objects.get(id=item_id)
       order_item  , created  = OrderItem.objects.get_or_create(
              item = item ,
              user =request.user,
              ordered=False
       )
       order_qs = Order.objects.filter(user=request.user,ordered = False) 
       if order_qs.exists():
              order = order_qs[0]
              if order.items.filter(item__id = item.id).exists():
                     order_item.quantity += 1
                     order_item.save()
                     messages.info(request,"the item quantity was updated successfully")
              else:
                     messages.info(request,"the item was added to your cart successfully")
                     order.items.add(order_item)
       else:
              ordered_date = timezone.now()
              order = Order.objects.create(
              user=request.user,
              ordered_date=ordered_date,
              )
              Order.items.add(order_item)
              messages.info(request,"the item quantity was updated .")
              return redirect("core:item-list" )
       return redirect("core:item-list")
