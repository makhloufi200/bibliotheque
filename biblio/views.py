from django.shortcuts import render
from django.utils import timezone
from .models import Book
from django.db.models import Q
from django.shortcuts import render_to_response
# Create your views here.

def biblio(request):
    books = Book.objects.filter(created_date__lte=timezone.now()).order_by('created_date')

    return render(request,'home.html',{'books': books})


#def search(request):
#    query = request.GET.get('q', '')
#    if query:
#        qset = (
#        Q(title__icontains=query) |
#        Q(author__icontains=query)
#        )
#        results = Book.objects.filter(qset).distinct()
#    else:
#        results = []
#    return render("home.html", {
#        "books": results
#    })