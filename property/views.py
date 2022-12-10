from lib2to3.pgen2.token import GREATEREQUAL
from math import floor
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from library.settings import LOGIN_REDIRECT_URL
from django.contrib import messages
from property.models import Project, Property
from property.register import NewUserForm
from property.serializer import Projectserializers, Propertyserializers
from .forms import SearchingForm
from django.contrib.auth import login
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q


@login_required
#### Here we start the function that filter to the property's according to the Form  
def result(request):
    final_proj = []
    new_form = SearchingForm(request.POST, request.FILES)
    new_form= new_form.get_form()
    found_apt = Property.objects.filter(room__lte = new_form[0],floor__lte = new_form[1],property_type__contains = new_form[2],square_meter__lte = new_form[3],location__contains = new_form[4],street__contains = new_form[5],price__lte = new_form[6]).values()
    if found_apt:
    
        
        for apt in found_apt:
            
            
            found_apt1 = {
            'id':apt['id'],
            'room':apt['room'],
            'floor':apt['floor'],
            'property_type':apt['property_type'],
            'square_meter':apt['square_meter'],
            'location':apt['location'],
            'street':apt['street'],
            'street_number':int(apt['street_number']),
            'price':apt['price']
            }
            
            final_proj.append(found_apt1)
            apt_price=apt['price']
            found_project = Project.objects.filter(street__contains= apt['street']).values()
            

            for proj in found_project:
                apt['street_number']= int(apt['street_number'])
                proj['street_number']= int(proj['street_number'])
                if int(apt['street_number']) in range (int(proj['street_number']-15),int(proj['street_number']+1)) or int(apt['street_number']) in range (int(proj['street_number']),int(proj['street_number']+16)) :
                    our_date = proj['dates']-2022
                    if int(new_form[7])>= our_date:
                        

                        
                        new_price = apt_price*proj['value']
                        apt_price = apt_price+new_price
                        final_proj1={
                            'final_price': apt_price,
                            'type_project':proj['type_project'],
                            'size_project':proj['size_project'],
                            'company':proj['company'],
                            'location':proj['location'],
                            'street':proj['street'],
                            'street_number':proj['street_number'],
                            'dates':proj['dates'],
                            'value':proj['value'],
                            'years':our_date
                            }
                        final_proj.append(final_proj1)
                    
            context = {
                
                'final_proj':final_proj,
                
            }
        
        return render(request,'result.html',{'final_proj':final_proj})
    else:
        city=Property.objects.filter(location__contains = new_form[4]).values()
        text = "Hmmm... It's looks like we don't have properties  that match your search.. please try again with different parameters"
        text1="Here are some examples for some other properties that may interest you:"
        return render(request,'result.html',{'text':text,'city':city,'text1':text1})


####Here it's our homepage
@login_required
def home(request):
  
   return render(request,'index.html',{})

####Here it's a function that does all the Form that sends all the results to function result
@login_required
def searchproperty(request):
   searchingform = SearchingForm(request.POST, request.FILES)
   context = ({
            'searchingform' : searchingform 
        })
   return render(request,'searchproperty.html', context = context)  

#### Register Function 
def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("login")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})



####That function returns property according to the ID in the URL


def telaviva(request):
    tlv = Property.objects.filter(location__contains = 'Tel-aviv')
    return render(request,'tlv.html',{'tlv':tlv})


def ramatgan(request):
    rmg = Property.objects.filter(location__contains = 'Ramat-gan')
    return render(request,'Ramat-gan.html',{'rmg':rmg})


def rishon(request):
    rishon = Property.objects.filter(location__contains = 'Rishon-lezion')
    return render(request,'rishon.html',{'rishon':rishon})


def all_projects(request):
    projects_all = Project.objects.all()
    return render(request,'projects.html',{'projects_all':projects_all})

###This function it's for the single property includes filter to know the projects depends on the investment range
def single_apt(request,id):
    final_proj = []
    property = Property.objects.get(id=id)
    futureprice = request.GET.get('num')
    if futureprice == None:
        futureprice = "-100"
    if int(futureprice) in range(1,11):
        apt_price=property.price
        
        print(property.street)
        print('hello')
        found_project = Project.objects.filter(street__contains= property.street).values()
        
        for proj in found_project:
            property.street_number= int(property.street_number)
            proj['street_number']= int(proj['street_number'])
            if int(property.street_number) in range (int(proj['street_number']-15),int(proj['street_number']+1)) or int(property.street_number) in range (int(proj['street_number']),int(proj['street_number']+16)) :
                our_date = proj['dates']-2022
                if int(futureprice)>= our_date:
                    
                    new_price = apt_price*proj['value']
                    apt_price = apt_price+new_price
                    final_proj1={
                        'final_price': apt_price,
                        'type_project':proj['type_project'],
                        'size_project':proj['size_project'],
                        'company':proj['company'],
                        'location':proj['location'],
                        'street':proj['street'],
                        'street_number':proj['street_number'],
                        'dates':proj['dates'],
                        'value':proj['value'],
                        'years':our_date
                        }
                    final_proj.append(final_proj1)
                

    return render(request, 'single-property.html', {'property':property,'final_proj':final_proj})
    

##This function for single projcet
def single_project(request,id):
    project = Project.objects.get(id=id)
    
    return render(request, 'single-project.html', {'project':project})

###This function it's API for properties  
@api_view(['GET','POST'])
def property_api(request):
   
    if request.method == "POST":
        property_ser= Propertyserializers(data=request.data)
        if property_ser.is_valid():
            property_ser.save()
            print('hello')
        else:
            print(property_ser.errors)

    property_ser=Property.objects.all()
    serializedprop = Propertyserializers(property_ser,many=True)
    return Response (serializedprop.data)

###This function it's API for project
@api_view(['GET','POST'])
def project_api(request):
   
    if request.method == "POST":
        project_ser= Projectserializers(data=request.data)
        if project_ser.is_valid():
            project_ser.save()
            print('hello')
        else:
            print(project_ser.errors)

    project_ser=Project.objects.all()
    serializedproj = Projectserializers(project_ser,many=True)
    return Response (serializedproj.data)

###This is for search in the navbar
def nav_search(request):
    if request.method=="POST":
        searched=request.POST["search1"]
        A_property=Property.objects.filter(Q(location__contains = searched) | Q(street__contains = searched)| Q(room__contains = searched)| Q(floor__contains = searched)| Q(property_type__contains = searched)| Q(square_meter__contains = searched)| Q(street_number__contains = searched)| Q(price__contains = searched))
        B_projects=Project.objects.filter(Q(type_project__contains = searched) | Q(size_project__contains = searched)| Q(company__contains = searched)| Q(value__contains = searched)| Q(location__contains = searched)| Q(street__contains = searched)| Q(street_number__contains = searched)| Q(dates__contains = searched))
    if searched == None:
        searched="nothing"

           
    return render (request,"search_all.html",{"A_property":A_property, "B_projects":B_projects, "searched":searched})
