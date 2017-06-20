from .forms import SubscribeForm

def sellups(request):
    ctx = {}
    ctx['subscribe_form'] = SubscribeForm()
    return ctx