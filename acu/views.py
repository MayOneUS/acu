from django.contrib.auth import logout, authenticate, login

from django.shortcuts import render

# def login_view(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(username=username, password=password)
#     if user is not None:
#         if user.is_active:
#             login(request, user)
#             # Redirect to a success page.
#         else:
#             pass # Return a 'disabled account' error message
#     else:
#         pass # Return an 'invalid login' error message.
#
#
# def logout_view(request):
#     logout(request)
#     # Redirect to a success page.


def home(request):
    return render(request, 'home.html')
