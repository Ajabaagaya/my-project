from django import forms
# from django_countries.fields import CountryField
PAYMENT_CHOICES = (
    ( 'S', 'الكريمي'),
    ('C', 'التضامن '),
    ('K', 'كاش ')
)
STATE_CHOICES = (
    ( 'A', 'صنعاء'),
    ('T', 'تعز'),
    ('H', 'ذمار'),
   
)
class CheckoutForm(forms.Form):
        Image = forms.ImageField()
        first = forms.CharField( widget =forms.TextInput(attrs ={
            'placeholder':'First name ','class':'form-control last'
        }))
        last = forms.CharField(widget =forms.TextInput(attrs ={
            'placeholder':'last name ' ,'class':'form-control last'
        }))
        email = forms.CharField(widget =forms.TextInput(attrs ={
        'placeholder':'youremail@example.com' ,'type':'email','id':'email','class':'form-control last'
         }))
        address = forms.CharField(label='address',widget = forms.TextInput(attrs = {
            'placeholder':'address','width':'80%','class':'form-control last'
        }))
     

        # country = CountryField(blank_label='(select country)').formfield(attrs={
        #     'class':'custom-select last d-block w-100'
        # })
        state= forms.ChoiceField(choices= STATE_CHOICES,widget=forms.Select(attrs={
            'class':'custom-select last  w-40 mb-3 ml-3 mr-3 d-block '}))
        payment_option= forms.ChoiceField(widget=forms.RadioSelect, choices = PAYMENT_CHOICES)
