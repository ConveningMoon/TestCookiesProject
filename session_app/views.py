from django.http import HttpResponse
from django.shortcuts import redirect

def cookie_session(request):
    request.session.set_test_cookie()
    return HttpResponse("<h1>Testing Cookie</h1>")

def cookie_delete(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        response = HttpResponse("<h1>Cookie created successfully</h1>")
    else:
        response = HttpResponse("<h1>Your browser does not accept cookies</h1>")
    return response

def create_session(request):
    request.session['name'] = 'username'
    request.session['password'] = 'password123'
    return HttpResponse("<h1>Session is set</h1>")

def access_session(request):
    response = "<h1>Welcome to Sessions Demo</h1><br>"
    if request.session.get('name'):
        response += "Name: {0} <br>".format(request.session.get('name'))
    if request.session.get('password'):
        response += "Password: {0} <br>".format(request.session.get('password'))
        return HttpResponse(response)
    else:
        return redirect('create/')

def delete_session(request):
    try:
        del request.session['name']
        del request.session['password']
    except KeyError:
        pass
    return HttpResponse("<h1>Session data cleared</h1>")
