import json

from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from myapp.models import Book


# Create your views here.
@require_http_methods(["GET"])
def add_book(request):
    response = {}
    try:
        book = Book(book_name=request.GET.get('book_name'))
        print("add book: " + book.book_name)
        book.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def show_books(request):
    response = {}
    try:
        books = Book.formatted_time(Book.objects.filter())
        print("book list: " + str(books))
        response['list'] = json.loads(serializers.serialize("json", books))
        print(response['list'])
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        print(e)
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)
