from __future__ import unicode_literals

from account.conf import settings
from account.models import Account
from account.forms import LoginUsernameForm

def account(request):
    ctx = {
        "account": Account.for_request(request),
        "ACCOUNT_OPEN_SIGNUP": settings.ACCOUNT_OPEN_SIGNUP,
        'login_form' : LoginUsernameForm(),
    }
    return ctx
