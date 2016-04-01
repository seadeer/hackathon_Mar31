from apps.logreg.models import User
from apps.findpad.models import Listing
from django.utils import timezone
from datetime import datetime, timedelta
from django.db.models import Sum

# b1 = Brand(name='Gucci', created_at=timezone.now())
# b2 = Brand(name='Burbury', created_at=timezone.now())
# b3 = Brand(name='Versaci', created_at=timezone.now())
# b4 = Brand(name='Prada', created_at=timezone.now())
# # b5 = Brand(name='Value Village', created_at=timezone.now())
# b1_id = Brand.objects.get(id=1)
# b2_id = Brand.objects.get(id=2)
# b3_id = Brand.objects.get(id=3)
# b4_id = Brand.objects.get(id=4)
# b5_id = Brand.objects.get(id=5)

# p1 = Product(name='Shades', price=299.99, brand=b1_id, created_at=timezone.now())
# p2 = Product(name='Trench Coat', price=2000.03, brand=b2_id, created_at=timezone.now())
# p3 = Product(name='Sneakers', price=220.35, brand=b3_id, created_at=timezone.now())
# p4 = Product(name='Panties', price=60.23, brand=b4_id, created_at=timezone.now())
# p5 = Product(name='Jean Jacket', price=5.00, brand=b5_id, created_at=timezone.now())

User.objects.all().delete()
Listing.objects.all().delete()