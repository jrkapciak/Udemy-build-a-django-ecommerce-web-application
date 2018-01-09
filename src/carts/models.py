from django.db import models
from django.conf import settings
from products.models import Product
from django.db.models.signals import pre_save, m2m_changed
User = settings.AUTH_USER_MODEL


class CartManager(models.Manager):

    def new_or_get(self, request):
        cart_id = request.session.get('cart_id', None)
        qs = self.get_queryset().filter(id=cart_id)
        if qs.count() == 1:
            new_object = False
            cart_obj = qs.first()
            if request.user.is_authenticated() and cart_obj.user is None:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            cart_obj = self.new(user=request.user)
            new_object = True
            request.session['cart_id'] = cart_obj.id
        return cart_obj,new_object

    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated():
                user_obj = user
        return self.model.objects.create(user=user_obj)


class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True)
    products = models.ManyToManyField(Product, blank=True)
    total = models.DecimalField(default=0.00, max_digits=12, decimal_places=2)
    subtotal = models.DecimalField(default=0.00, max_digits=12, decimal_places=2)

    time_stamp = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    objects = CartManager()

    def __str__(self):
        return str(self.id)


def m2m_changed_cart_reciver(sender,instance,action,*args,**kwargs):
    if action == 'post_add' or action =='post_remove' or action == 'post_clear':
        products = instance.products.all()
        total = 0
        for i in products:
            total += i.price
        if instance.subtotal != total:
            instance.subtotal = total
            instance.save()

m2m_changed.connect(m2m_changed_cart_reciver, sender=Cart.products.through)

def pre_save_cart_reciver(sender,instance,*args,**kwargs):
    instance.total = instance.subtotal

pre_save.connect(pre_save_cart_reciver, sender=Cart)