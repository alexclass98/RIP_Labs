from django.http import HttpResponse
from django.shortcuts import render


from datetime import date

def hello(request):
    return render(request, 'index.html', { 'data' : {
        'current_date': date.today(),
        'list': ['python', 'django', 'html']
    }})
def GetOrders(request):
    return render(request, 'orders.html', {'data' : {
        'current_date': date.today(),
        'orders': [
            {'title': 'Книга с картинками', 'settings': 'Очень крутая книга, картинки пушка', 'id': 1},
            {'title': 'Бутылка с водой', 'settings': 'Вкусная вода!', 'id': 2},
            {'title': 'Коврик для мышки', 'settings': 'Удобный)', 'id': 3},
        ],
    }})
def GetOrder(request, id):
    return render(request, 'order.html', {'data' : {
        'current_date': date.today(),
        'id': id,
        'options': ['Стоимость книги 500р', 'Стоимость бутылки 200р', 'Стоимость коврика 300р']
    }})
from bmstu_lab.models import Book

def bookList(request):
    return render(request, 'books.html', {'data' : {
        'current_date': date.today(),
        'books': Book.objects.all()
    }})

def GetBook(request, id):
    return render(request, 'book.html', {'data' : {
        'current_date': date.today(),
        'book': Book.objects.filter(id=id)[0]
    }})