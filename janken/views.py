from django.http.response import HttpResponse

def index(request):
    body = 'じゃんけんのページです。'
    body += '<br><a href="/janken/rock-paper-scissors/">じゃんけんをする</a>'
    return HttpResponse(body)