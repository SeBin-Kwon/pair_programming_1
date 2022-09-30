from django.shortcuts import render, redirect
from .models import Review

# Create your views here.
def index(request):
    review = Review.objects.all()
    context = {"review": review}
    return render(request, "reviews/index.html", context)


def create(request):
    title = request.GET.get("title")
    content = request.GET.get("content")
    print(title, content)

    Review.objects.create(title=title, content=content)
    context = {"title": title, "content": content}

    return redirect("reviews:detail")


def new(request):
    return render(request, "reviews/new.html")


def detail(request, pk):
    review = Review.objects.get(pk=pk)
    context = {"review": review}
    return render(request, "reviews/detail.html", context)
