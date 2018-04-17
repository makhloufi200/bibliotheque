from django.shortcuts import render
from django.utils import timezone
from .models import Book
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response
# Create your views here.

def biblio(request):
    books = Book.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    return render(request,'home.html',{'books': books, 'num_visits':num_visits})


def search(request):
    print (request)
    query = request.GET.get('q', '')
    print("query")
    print (query)
    if query:
        qset = (
        Q(title__icontains=query)
        )
        results = Book.objects.filter(qset).distinct()
    else:
        results = []

    return render(request,'home.html', {
        'books': results
    })

def listing(request):
    contact_list = Book.objects.all()
    paginator = Paginator(contact_list, 10) # Show 25 contacts per page

    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request, 'home.html', {'pages': contacts})