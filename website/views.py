from django.shortcuts import render, redirect
from website.forms import ContactForm, NewsLetterForm  # Corrected the import

def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    if request.method == 'POST':  
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('website:contact')  
    else:
        form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})

def newsletter_view(request):
    if request.method == 'POST':  
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('website:contact')  # Redirect to contact if successful
        else:
            return redirect('website:index')  # Redirect to index if there is a mistake
    else:
        form = NewsLetterForm()
    return render(request, 'website/newsletter.html', {'form': form})