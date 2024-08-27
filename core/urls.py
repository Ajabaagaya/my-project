from django.urls import path
from . views import *
app_name = "core"
urlpatterns = [
        path('', main, name='main'),
        # path('item-list/<id>/',Home, name='item-list'),
        path('item-list/',ListItem.as_view(), name='item-list'),

        path('nav/',Nav ,name="nav"),
        # path('email/',send_email,name='email'),
        path('checkout/',CheckoutView.as_view(), name='checkout'),
        path('Order-summary/',OrderSummaryView.as_view(),name='Order-summary'),
        path('remove-all/<slug>/',Remove_All,name='remove-all'),
        path('UpdateItem/',UpdateItem,name='UpdateItem'),
        ##path('product/<slug>/',ItemDetailView.as_view(), name='product'),
        path('product/<slug>/',listItem, name='product'),
        path('add-to-summary/<int:item_id>/', add_to_Summary , name='add-to-summary'),
        path('remove-from-summary/<int:item_id>/', Remove_from_Summary , name='remove-from-summary'),
        path('add-to-cart/<slug>/', add_to_cart , name='add-to-cart'),
        path('add-to-home/<int:item_id>/', add_to_home , name='add-to-home'),
        path('remove-from-cart/<slug>/', remove_from_card , name='remove-from-cart'),
        path('payment/<payment_option>/',PaymentView.as_view(),name='payment'),
]