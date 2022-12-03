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

# def list(request):
#    return HttpResponse("Hello DJANGO library")

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SearchingForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchingForm()

    return render(request, 'result.html', {'form': form})

@login_required
#### Here we start the function that filter to the property's according to the Form  
def result(request):
    final_proj = []
    my_search = request.POST.get('searchproperty')
    new_form = SearchingForm(request.POST, request.FILES)
    new_form= new_form.get_form()
    found_apt = Property.objects.filter(room__lte = new_form[0],floor__lte = new_form[1],property_type__contains = new_form[2],square_meter__lte = new_form[3],location__contains = new_form[4],street__contains = new_form[5],price__lte = new_form[6]).values()
    
    list_id = []
    for apt in found_apt:
        list_id.append(apt['id'])
        
        found_apt1 = {
        'id':apt['id'],
        'id1':Property.id,
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
    
    return render(request,'result.html',{'final_proj':final_proj,'list_id':list_id})






####here it's our homepage
@login_required
def home(request):
   context = {
       
   }
  
   return render(request,'index.html',context)

####Here it's function that doing all the Form that sending all the result to function result
@login_required
def searchproperty(request):
   my_search = request.GET.get('searchproperty') 
   my_property = Property.objects.all()
   searchingform = SearchingForm(request.POST, request.FILES)
   context = ({
            'searchingform' : searchingform
            
           
        })
   return render(request,'searchproperty.html', context = context)  


### This is the the function that return all the form to result.html
@login_required
def get_form(request):

    if request.method == 'POST':
        form = SearchingForm(request.POST)
        if form.is_valid():
            context = {
            'room' : form.cleaned_data['room'],
            'floor' : form.cleaned_data['floor'],
            'property_type' : form.cleaned_data['property_type'],
            'square_meter' : form.cleaned_data['square_meter'],
            'location' : form.cleaned_data['location'],
            'street' : form.cleaned_data['street'],
            'street_number' : form.cleaned_data['street_number'],
            'price' : form.cleaned_data['price']
            }
            
          

            return HttpResponseRedirect('/result',  context_instance=RequestContext(request))
    else:
        form = SearchingForm()
        rendered_form = form.render("searchproperty.html")
        context = {'form': rendered_form}
        
        return render(request, 'property/result.html', context)


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



####That function return property according to the ID in the url




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







def single_apt(request,id):
    num_list = []
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
                
        context = {
            
            'final_proj':final_proj,
            
        }

    return render(request, 'single-property.html', {'property':property,'final_proj':final_proj})
    


def single_project(request,id):
    project = Project.objects.get(id=id)
    
	
    return render(request, 'single-project.html', {'project':project})


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


