from unicodedata import name
from django import forms

class SearchingForm(forms.Form):
   room = forms.IntegerField(label='room',widget=forms.TextInput(attrs={'placeholder': '1-5'}))
   floor = forms.IntegerField(label='floor',widget=forms.TextInput(attrs={'placeholder': 'Max floor 50'}))
   property_type = forms.CharField(label='property_type ',widget=forms.TextInput(attrs={'placeholder': 'apartment/house'}))
   square_meter = forms.IntegerField(label='square_meter',widget=forms.TextInput(attrs={'placeholder': 'Max 1000'}))
   location = forms.CharField(label='location',widget=forms.TextInput(attrs={'placeholder': 'Tel-aviv/Ramat-gan'}))
   street=forms.CharField(label='street',widget=forms.TextInput(attrs={'placeholder': 'Enter your street'}))
   price= forms.IntegerField(label='price',widget=forms.TextInput(attrs={'placeholder': 'Enetr your price'}))
   investment_range = forms.IntegerField(label='investment_range',widget=forms.TextInput(attrs={'placeholder': 'Range for investment'}))
   fields = '__all__'


   def __str__(self):
      return self.room +","+ self.floor+","+ self.property_type+","+ self.square_meter+","+ self.location+","+ self.street+","+ self.price+","+self.investment_range
   def __repr__(self):
         return self.__str__() 

   def get_form(self):
      return self.data.get('room'), self.data.get('floor'),self.data.get('property_type'),self.data.get('square_meter'),self.data.get('location'),self.data.get('street'),self.data.get('price'),self.data.get('investment_range')
      
