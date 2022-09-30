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

    review =  Review.objects.create(title=title, content=content)
    review_pk = Review.objects.get(pk=review.pk)
    context = {"title": title, "content": content}

    return redirect("reviews:detail", review_pk.pk )


def new(request):
    return render(request, "reviews/new.html")


def detail(request, pk):
    review = Review.objects.get(pk=pk)
    context = {"review": review}
    return render(request, "reviews/detail.html", context)

def delete(request, pk):
    Review.objects.get(pk=pk).delete()
    return redirect("reviews:index")

def edit(request, pk):
    review = Review.objects.get(pk=pk)
    context = {
        "review" : review
    }
    return render(request, "reviews/edit.html", context)

def update(request, pk):
    review = Review.objects.get(pk=pk)

    title_ = request.GET.get('title')
    content_ = request.GET.get('content')

    review.title = title_
    review.content = content_

    review.save()

    return redirect("reviews:detail", review.pk)