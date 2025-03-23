from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from .models import * 
from django.contrib.auth import authenticate, login, logout
from django.core import serializers
import json
from .forms import DocumentForm
# Create your views here.
def load(request):
    return render(request,'index.html')
def index(request,message=None):
    if message is not None:
        context={'message':message}
    else:
        context={}
    return render(request,'uniqueid.html',context)
def pwd(request):
    try:
        if request.method=="GET":
            user_name=request.GET.get('uniqueid','')
            
            user=User.objects.get(username=user_name)
            full_name=user.get_full_name()
            
            ud=UserDetails.objects.get(user=user)
            dob=ud.date_of_birth
            gender=ud.gender
            context={'full_name':full_name,'dob':dob,'gender':gender,'user':user,'user_details':ud}
            
        return render(request,'welcome.html',context)
    except:
        return index(request,"No Users Found!!")
def login_view(request):
    if request.method=="POST":
        print("done")
        username=request.POST.get('username',None)
        passwd=request.POST.get('password',None)
        print(username,passwd)
        if (username and passwd):
            user= authenticate(username=username,password=passwd)
            if user is not None:
                login(request,user)
                return download_docs(request)
            else:
                user=User.objects.get(username=username)
                full_name=user.get_full_name()
                #email=User.email
                ud=UserDetails.objects.get(user=user)
                dob=ud.date_of_birth
                gender=ud.gender
                context={'full_name':full_name,'dob':dob,'gender':gender,'user':user,'msg':"invalid credencials"}
                #context={"msg":"Invalid Credencials","user":user}
                return render(request,'welcome.html',context)    
    return HttpResponse("error")
def logout_view(request):
    logout(request)
    return redirect('home')
# def download_information(request):
#     if request.user.is_authenticated:
#         user=request.user
#         userDetailes=serializers.serialize("json",UserDetails.objects.filter(user=user))
        
#         user_detail=User.objects.get(username=user.username)
        
#         userDetailes=json.loads(userDetailes)[0]['fields']
#         userDetailes['Name']=user_detail.get_full_name()

        
#         return JsonResponse(userDetailes)
#     else:
#         index(request,"Please Login Before You Can Download info!!")
def download_information(request):
    if request.user.is_authenticated:
        user = request.user
        userDetailes = serializers.serialize("json", UserDetails.objects.filter(user=user))
        user_detail = User.objects.get(username=user.username)
        # Parse the serialized JSON and extract the 'fields'
        userDetailes = json.loads(userDetailes)[0]['fields']
        name_value = user_detail.get_full_name()
        
        # Create an ordered dictionary to reposition "Name" as the second field.
        ordered_data = {}
        keys = list(userDetailes.keys())
        
        if keys:
            # Add the first field as is.
            first_key = keys[0]
            ordered_data[first_key] = userDetailes[first_key]
            
            # Insert "Name" as the second field.
            ordered_data["Name"] = name_value
            
            # Add the remaining fields.
            for key in keys[1:]:
                ordered_data[key] = userDetailes[key]
        else:
            # If no fields exist, just add "Name".
            ordered_data["Name"] = name_value
        
        return JsonResponse(ordered_data)
    else:
        return index(request, "Please Login Before You Can Download info!!")
def download_info_view(request):
    return render(request,"download_information.html")  




def download_docs(request):
    if request.user.is_authenticated:
        docs=documents.objects.filter(user=request.user)
        # for d in docs:
        #     print(d.document_name)
        context={'docs':docs}
        return render(request,'download.html',context)
    else:
        return HttpResponse("Please Login First!!!")
def download_reports(request):
    if request.user.is_authenticated:
        docs=documents.objects.filter(user=request.user)
        # for d in docs:
        #     print(d.document_name)
        context={'docs':docs}
        return render(request,'sidenav_documents_display.html',context)
    else:
        return HttpResponse("Please Login First!!!")
def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            # Create an instance but don't commit it to the database yet
            document = form.save(commit=False)
            # Assign the current user as the owner of the document
            document.user = request.user
            document.save()
            # Optionally, redirect to a success page or document list page
            return redirect('download_reports')  # Change 'document_list' to your desired URL name
    else:
        form = DocumentForm()
    
    return render(request, 'upload_document.html', {'form': form})