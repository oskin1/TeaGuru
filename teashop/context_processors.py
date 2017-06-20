from .models import ShopConfig, Category, ForeignPage
from .forms import ProductSearchForm
    
def common(request):
    ctx = {
        'common' : ShopConfig.objects.get(name='teaguru'),
        'categories' : Category.objects.filter(active=True),
        'links' : ForeignPage.objects.filter(group__slug='footer_links'),
    }
    return ctx
    
def user_agent(request):
    return {
        'is_mobile' : request.user_agent.is_mobile,
        'is_tablet' : request.user_agent.is_tablet,
        'is_touch' : request.user_agent.is_touch_capable,
        'ua_family' : request.user_agent.browser.family,
    }
    
def search(request):
    search_form = ProductSearchForm()
    return { 'search_form' : search_form }