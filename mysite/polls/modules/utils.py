from random import randint
from django.contrib.auth import authenticate


def uniqueid():
    n = 8
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


def validateUser(request):
    user = authenticate(username=request.POST.get(
        'username'), password=request.POST.get('password'))
    print(request.POST.get('username'))
    print(request.POST.get('password'))
    print(user)
    if user is not None:
        return True
    else:
        return False
