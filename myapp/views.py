from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import Book
from .forms import BookForm
# Create your views here.

def index(request):
	return HttpResponse("<h1>USOS 2.0 very primitive model</h1>")

def books_index(request):
	template = loader.get_template("myapp/index.html")
	context = {"books": Book.objects.all()}
	return HttpResponse(template.render(context, request))

def book_detail(request, book_id):
	book = get_object_or_404(Book, pk=book_id)
	return render(request, "myapp/book.html", {"book":book})


def book_add(request):
	if request.method == 'POST':
		form = BookForm(request.POST)
		if(form.is_valid()):
			form.save()
			return HttpResponseRedirect(reverse('books-index'))
	else:
		form = BookForm()
		return render(request, "myapp/book_add.html", {'form': form})