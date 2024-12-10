from django.db.models.signals import post_save, post_delete
from django.db.models import Sum
from django.dispatch import receiver
from cars.models import Car, CarInventory

def car_inventory_update():
    cars_cout = Car.objects.all().count()
    cars_value = Car.objects.aggregate(
        total_value = Sum('value')
    )['total_value']
    CarInventory.objects.create(
        cars_cout = cars_cout,
        cars_value = cars_value
    )

@receiver(post_save,sender=Car)
def car_post_save(sender, intance, **kwargs):
    car_inventory_update()

@receiver(post_delete,sender=Car)
def car_post_delete(sender, intance, **kwargs):
    car_inventory_update()