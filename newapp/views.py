from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Review


def home(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        message = request.POST.get("message", "").strip()
        rating_value = request.POST.get("rating", "")

        try:
            rating = int(rating_value)
        except (TypeError, ValueError):
            rating = 0

        if name and message and 1 <= rating <= 5:
            Review.objects.create(
                name=name,
                message=message,
                rating=rating,
            )

        return redirect(reverse("home") + "#reviews")

    reviews = Review.objects.order_by("-created_at")
    return render(request, "home.html", {"reviews": reviews})