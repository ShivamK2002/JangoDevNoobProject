from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    peoples = [
        {'name': 'Shivam Kawale', 'age': 22},
        {'name': 'Sanket Kawale', 'age': 18},
        {'name': 'Ajay Rojekar', 'age': 22},
        {'name': 'Shreyas Kulkarni', 'age': 22},
    ]

    for people in peoples:
        print(people)
    return render(request, 'index.html', {'peoples': peoples})
