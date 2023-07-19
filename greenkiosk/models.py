# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CartCartItems(models.Model):
    cart = models.ForeignKey('CartCart', models.DO_NOTHING)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cart_cart_items'
        unique_together = (('cart', 'product'),)


class CategoryCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=50)
    image = models.CharField(max_length=100)
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()
    stock = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'category_category'


class CustomerCustomer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=254)
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'customer_customer'


class DeliveryDelivery(models.Model):
    customer_name = models.CharField(max_length=100)
    delivery_address = models.CharField(max_length=200)
    delivery_status = models.CharField(max_length=50)
    delivery_date = models.IntegerField()
    delivery_method = models.CharField(max_length=50)
    order_id = models.CharField(max_length=50)
    delivery_cost = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'delivery_delivery'


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class FeedbackFeedback(models.Model):
    feedback = models.TextField()
    date = models.DateTimeField()
    ratings = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'feedback_feedback'


class InventoryProduct(models.Model):
    name = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    description = models.TextField()
    image = models.CharField(max_length=100)
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()
    stock = models.PositiveIntegerField()
    vendor = models.ForeignKey('VendorVendor', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventory_product'


class NotificationNotification(models.Model):
    message = models.CharField(max_length=255)
    date = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    notification_type = models.CharField(max_length=50)
    subject = models.CharField(max_length=255)
    sender_id = models.IntegerField()
    recipient_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'notification_notification'


class PaymentPayment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    payment_method = models.CharField(max_length=50)
    payment_status = models.CharField(max_length=50)
    payment_date = models.IntegerField()
    payment_amount = models.IntegerField()
    currency_used = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'payment_payment'


class ProductProduct(models.Model):
    product_id = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=5)  # max_digits and decimal_places have been guessed, as this database handles decimal fields as float
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    image_url = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'product_product'


class ReviewReview(models.Model):
    customer_id = models.IntegerField()
    product_name = models.CharField(max_length=255)
    rating = models.IntegerField()
    review_text = models.TextField()
    review_date = models.IntegerField()
    review_status = models.CharField(max_length=50)
    review_title = models.TextField()

    class Meta:
        managed = False
        db_table = 'review_review'


class VendorVendor(models.Model):
    vendor_name = models.CharField(max_length=255)
    email = models.CharField(max_length=254)
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'vendor_vendor'
