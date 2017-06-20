from .cart import Cart
from .forms import CartAddOneProductForm, CartAddTenProductForm, CartOptProductForm

def cart(request):
    ctx = {
        'cart': Cart(request),
        'cart_product_form_1' : CartAddOneProductForm(),
        'cart_product_form_10' : CartAddTenProductForm(),  
        'cart_opt_product_form' : CartOptProductForm(),
    }
    return ctx