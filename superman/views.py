from django.shortcuts import render, HttpResponse
from datetime import datetime
from superman.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "variable": "this is sent"
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        discribe = request.POST.get('discribe')  # Correctly fetch discribe

        # Ensure discribe is present in the form submission
        if not discribe:
            return HttpResponse("Description is required.")
        
        if not email:
            return HttpResponse("Email is required.")

        # Save the contact info to the database
        contact = Contact(
            name=name,
            email=email,
            phone=phone,
            discribe=discribe,
            date=datetime.today()
        )
        contact.save()
        messages.success(request, "Yours message has been sent!")


        return render(request, 'contact.html', {'message': 'Your message has been saved successfully!'})

    return render(request, 'contact.html')
