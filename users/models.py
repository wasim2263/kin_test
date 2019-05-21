from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils.translation import ugettext_lazy as _

GENDER_CHOICES = (
    (0, _('male')),
    (1, _('female')),
    (2, _('not specified')),
)

DEPOSIT_WITHDRAWAL_STATUS_CHOICES = (
    (-1, _('pending')),
    (0, _('rejected')),
    (1, _('accepted')),
)


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='avatar.jpg', upload_to='images/profile_pic')
    gender = models.IntegerField(choices=GENDER_CHOICES,
                                 default=2)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


#
class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    public_key = models.CharField(max_length=255, null=True, blank=True)
    private_key = models.CharField(max_length=255, null=True, blank=True)
    balance = models.DecimalField(decimal_places=8, max_digits=21, default=0)
    is_backup = models.BooleanField(default=False)

#
# class Deposit(models.Model):
#     wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
#     amount = models.DecimalField(decimal_places=8, max_digits=21)
#     status = models.ImageField(choices=DEPOSIT_WITHDRAWAL_STATUS_CHOICES, default=-1)
#     invoice_number = models.CharField(max_length=150)
#
#
# class Withdrawal(models.Model):
#     wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
#     amount = models.DecimalField(decimal_places=8, max_digits=21)
#     status = models.ImageField(choices=DEPOSIT_WITHDRAWAL_STATUS_CHOICES, default=-1)
#     invoice_number = models.CharField(max_length=150, blank=True, null=True)
#     accepted_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.PROTECT)
