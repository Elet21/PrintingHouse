from django.shortcuts import render


def kazan(requests):
    return render(requests, 'kazan.html')


def chelny(requests):
    return render(requests, 'chelny.html')