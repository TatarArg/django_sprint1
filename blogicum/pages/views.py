from django.shortcuts import render


def about(request):
    template_html = 'pages/about.html'
    return render(request, template_html)


def rules(request):
    template_html = 'pages/rules.html'
    return render(request, template_html)
