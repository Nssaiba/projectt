from django.shortcuts import render,redirect
import io
from django.http import HttpResponse
from .models import Offre
from django.contrib import messages
from .models import Evenements
from .models import Client
from django.db.models import Count
import matplotlib.pyplot as plt
from django.utils import timezone
from .models import Destination
from .models import Commentaire
from .models import Admins




# Create your views here.
def search_offers(request):
    # Get the value of 'type' from the request's POST parameters
    offer_type = request.POST.get('type')
    
    
    results = Offre.objects.filter(type=offer_type)

    if offer_type == "All" :
        results = Offre.objects.all()

    # Pass the filtered offers and other necessary data to the template
    context = {
        'data': results,
        'selected_offer_type': offer_type,
        
    }
    return render(request, "index.html", context)

def search_events(request):
    # Get the value of 'type' from the request's POST parameters
    event_type = request.POST.get('categorie')
    
    
    results = Evenements.objects.filter(categorie=event_type)

    if event_type== "All" :
        results = Evenements.objects.all()

    # Pass the filtered offers and other necessary data to the template
    context = {
        'data': results,
        'selected_offer_type': event_type,
        
    }
    return render(request, "GestionEven.html", context)

def search_clients(request):
    
    client_name = request.POST.get('client_name')
    # Utilisez le nom du client pour effectuer la recherche dans votre base de données
    data = Client.objects.filter(Nom=client_name)

    if client_name== "" :
        data = Client.objects.all()
        # Renvoyer les résultats à un autre template pour les afficher
    context = {
        'client_name': client_name,
        'data': data,
        
    }
        
    return render(request, 'team.html',context)
   
def index(request):
    data=Offre.objects.all()
    num_offers = Offre.objects.count()
    context={"data":data,
             'num_offers': num_offers,}    

    return render(request,"index.html",context)

def insertData(request):
    
    if request.method=="POST":
      nameP=request.POST.get('name')
      type=request.POST.get('type')
      price=request.POST.get('price')
      description=request.POST.get('description')
      date=request.POST.get('date')
      image= request.FILES.get('image')
      date_added = timezone.now()
      print(nameP,type,price,description,date,image)
      query=Offre(nameP=nameP,type=type,price=price,description=description,date=date,image=image,date_added=date_added)
      query.save()
      messages.success(request,"Data Inserted successffully")
      return redirect("chatbot:/")
    
    return render(request,"index.html")

def updateData(request, id):

    if request.method=="POST":
      nameP=request.POST['name']
      type=request.POST['type']
      price=request.POST['price']
      description=request.POST['description']
      date=request.POST['date']
      image= request.FILES['image']

      edit= Offre.objects.get(id=id)
      edit.nameP=nameP
      edit.type=type
      edit.price=price
      edit.description=description
      edit.date=date
      edit.image=image
      edit.save()
      messages.warning(request,"Data updated successffully")

      return redirect("chatbot:index")
    
    d= Offre.objects.get(id=id)
    context = {"d": d}
    return render(request, "update.html", context)


def deleteData(request,id):
    data=Offre.objects.get(id=id)
    data.delete()
    messages.error(request,"Data deleted successffully")
    return redirect("chatbot:/")






def gestion_even(request):
    data=Evenements.objects.all()
    num_events = Evenements.objects.count()
    context={"data":data,
             'num_events': num_events,}
    return render(request,"GestionEven.html",context)

 

def insertEvent(request):
     if request.method=="POST":
      lieu=request.POST.get('lieu')
      categorie=request.POST.get('categorie')
      date=request.POST.get('date')
      time = request.POST.get('time')
      price=request.POST.get('price')
      description=request.POST.get('description')
      image= request.FILES.get('image')
      print(lieu,categorie,price,description,date,time,image)
      query=Evenements(lieu=lieu,categorie=categorie,price=price,description=description,date=date,time=time,image=image)
      query.save()
      messages.success(request,"Data Inserted successffully")
      return redirect("chatbot:gestion_even") 
     
     return render(request,"GestionEven.html")

def updateEvent(request,id):
    if request.method=="POST":
       
       lieu=request.POST['lieu']
       categorie=request.POST['categorie']
       date=request.POST['date']
       time = request.POST['time']
       price=request.POST['price']
       description=request.POST['description']
       image= request.FILES['image']

       edit= Evenements.objects.get(id=id)
       edit.lieu=lieu
       edit.categorie=categorie
       edit.date=date
       edit.time=time
       edit.price=price
       edit.description=description
       edit.image=image
       edit.save()
       messages.warning(request,"Evenement updated successffully")

       return redirect("chatbot:gestion_even")
    
    d= Evenements.objects.get(id=id)
    context = {"d": d}
    return render(request, "updateEven.html", context)




def deleteEvent(request,id):
    data=Evenements.objects.get(id=id)
    data.delete()
    messages.error(request,"Event deleted successffully")
    return redirect("chatbot:gestion_even")


def Dashboard(request):
    num_offers = Offre.objects.count()
    num_events = Evenements.objects.count()
    num_Client = Client.objects.count()

    cs_no = Evenements.objects.filter(categorie='Culturel').count()
    ce_no = Evenements.objects.filter(categorie='Aventure').count()
    se_no = Evenements.objects.filter(categorie='Fêtes').count()
    sec_no = Evenements.objects.filter(categorie='Artisanat et Marchés').count()
    bal_no = Evenements.objects.filter(categorie='Balade').count()
    gas_no = Evenements.objects.filter(categorie='Gastronomique').count()

    categorie_list = ['Culturel', 'Aventure', 'Fêtes', 'Artisanat et Marchés', 'Balade', 'Gastronomique']
    number_list = [cs_no, ce_no, se_no, sec_no, bal_no, gas_no]

    recent_offers = Offre.objects.order_by('-date_added')[:7]

    context = {
        'num_offers': num_offers,
        'num_events': num_events,
        'num_Client': num_Client,
        'categorie_list': categorie_list,
        'number_list': number_list,
        'recent_offers': recent_offers,
    }

    return render(request, "Dashboard.html", context)

def team(request):
    data=Client.objects.all()
    num_Client = Client.objects.count()
    context = {
        'data': data,
        'num_Client': num_Client,
    }
    return render(request, "team.html", context)

def GestionDest(request):
    data=Destination.objects.all()
    num_Rest = Destination.objects.filter(categorie="Restaurant").count()
    num_Heberg= Destination.objects.filter(categorie="Hebergement").count()
    num_Activite= Destination.objects.filter(categorie="Activité").count()
    DestRest= Destination.objects.filter(categorie="Restaurant")
    DestHeberg= Destination.objects.filter(categorie="Hebergement")
    DestActivite= Destination.objects.filter(categorie="Activité")
    context = {
        'data': data,
        'num_Rest': num_Rest,
        'num_Heberg': num_Heberg,
        'num_Activite': num_Activite,
        'DestRest':DestRest,
        'DestHeberg':DestHeberg,
        'DestActivite':DestActivite,
    }
    return render(request, "GestionDest.html", context)  
   
   

def insertDestination(request):
     if request.method=="POST":
      lieu=request.POST.get('lieu')
      categorie=request.POST.get('categorie')
      price=request.POST.get('price')
      description=request.POST.get('description')
      image= request.FILES.get('image')
      
      query=Destination(lieu=lieu,categorie=categorie,price=price,description=description,image=image)
      query.save()
      messages.success(request,"Data Inserted successffully")
      return redirect("chatbot:GestionDest") 
     
     return render(request,"GestionDest.html")

# def about(request):
#     return render(request,"about.html")

def updateDest(request,id):
    if request.method=="POST":
       
       lieu=request.POST['lieu']
       categorie=request.POST['categorie']
       price=request.POST['price']
       description=request.POST['description']
       image= request.FILES['image']

       edit= Destination.objects.get(id=id)
       edit.lieu=lieu
       edit.categorie=categorie
       edit.price=price
       edit.description=description
       edit.image=image
       edit.save()
       messages.warning(request,"Destination updated successffully")

       return redirect("chatbot:GestionDest")
    
    d= Destination.objects.get(id=id)
    context = {"d": d}
    return render(request, "updateDest.html", context)




def deleteDest(request,id):
    data=Destination.objects.get(id=id)
    data.delete()
    messages.error(request,"Destination deleted successffully")
    return redirect("chatbot:GestionDest")


def home(request):
    return render(request, "Home.html")


def clientDestinations(request):
    data= Destination.objects.filter(categorie="Activité")
    context = {"data": data}
    return render(request, "ClientDestinations.html",context)

def clientEvent(request):
    data= Evenements.objects.all()
    context = {"data": data}
    return render(request, "ClientEvent.html",context)

def clientPackages(request):
    data= Destination.objects.filter(categorie="Hebergement")
    context = {"data": data}
    return render(request, "ClientPakages.html",context)

def clientRestaurants(request):
    data= Destination.objects.filter(categorie="Restaurant")
    context = {"data": data}
    return render(request, "ClientRestaurants.html",context)





from django.shortcuts import render, redirect
from django.http import JsonResponse
import openai

from django.contrib import auth
from django.contrib.auth.models import User
from .models import Chat


import os
from openai import OpenAI
from django.utils import timezone
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

def ask_openai(message):
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": message,
        }
    ],
    model="gpt-3.5-turbo",
)
    
    answer = chat_completion.choices[0].message.content.strip()
    return answer



def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)

        # Assuming the user is authenticated and you have access to the user object
        user_id = request.user.id

        # Save the chat with the logged-in user
        chat = Chat(user_id=user_id, message=message, response=response, created_at=timezone.now())
        chat.save()

        return JsonResponse({'message': message, 'response': response})
    
    else:
        # Fetch previous chat messages
        chats = Chat.objects.all()  # You can add filtering as needed
        
        return render(request, 'chatbot.html', {'chats': chats})

def subscribe(request):
    if request.method == 'POST':
        Prenom = request.POST.get('first_name')
        Nom = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        tel = request.POST.get('phone')
        image = request.FILES.get('image')

        # Create and save Client object
        client = Client(Prenom=Prenom, Nom=Nom, email=email, password=password, tel=tel, image=image)
        client.save()
        
        return redirect('chatbot:home')  # Redirect to success page after form submission
    else:
        return render(request, 'Home.html')
    


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            client = Client.objects.get(email=email, password=password)
            # Authentication successful, store the email in the session
            request.session['user_email'] = email
            # Redirect to the comment page
            return redirect('chatbot:comment')
        except Client.DoesNotExist:
            # If no matching client found, redirect to the home page
            return redirect('chatbot:home')
    else:
        # If it's a GET request, just render the login page
        return render(request, 'Home.html')

def comment(request):
    # Retrieve the email from the session
    user_email = request.session.get('user_email')
    if user_email:
        # If email exists in session, render the comment page with the email
        return render(request, 'comment.html', {'user_email': user_email})
    else:
        # If email does not exist in session, redirect to the login page
        return redirect('chatbot:login') 

def addComment(request):
    if request.method == 'POST':
        # Récupérer l'email depuis la session
        user_email = request.session.get('user_email')
        email = request.POST.get('email')
        
        if email==user_email:
            # Récupérer le commentaire depuis le formulaire
            comment_text = request.POST.get('comment')
            
            # Créer un nouvel objet Comment avec l'email et le commentaire
            new_comment = Commentaire(email=email, comment=comment_text)
            
            # Sauvegarder le nouveau commentaire dans la base de données
            new_comment.save()
            
            # Ajouter un message de succès
            messages.success(request, "Votre commentaire a été ajouté avec succès !")
            return redirect('chatbot:comment')
        else:
            # Si aucun e-mail n'est trouvé dans la session, redirigez vers la page de connexion
            messages.error(request, "Veuillez vous connecter pour ajouter un commentaire.")
            return redirect('chatbot:home')
        
        # Rediriger l'utilisateur vers une autre vue ou une autre URL
        return redirect('chatbot:home')
    
    # Si la méthode de requête n'est pas POST, renvoyez simplement le modèle de formulaire vide
    return render(request, 'home.html')    


def loginAdmin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            admin = Admins.objects.get(email=email)
            
            # Check if the provided password matches the one stored in the database
            if admin.password == password:
                # Authentication successful, store the admin's email in the session
                # Redirect to the dashboard
                return redirect('chatbot:Dashboard')
            else:
                # Invalid password
                messages.error(request, 'Invalid password.')
                return redirect('chatbot:home')  # Redirect to the login page or another appropriate page
                
        except Admins.DoesNotExist:
            # If no matching admin found, display an error message
            messages.error(request, 'Admin with this email does not exist.')
            return redirect('chatbot:home')  # Redirect to the login page or another appropriate page
    else:
        # If it's a GET request, render the login page
        return render(request, 'Home.html')
    
  
    
def LoginAdminPage(request):
    
    return render(request, 'LoginAdminPage.html')    