from django.shortcuts import render


def homepage(request):
    template_dir = "homepage.html"
    context = {}
    return render(request, template_dir, context=context)
