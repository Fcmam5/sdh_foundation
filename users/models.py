from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager
import hashlib

class CustomUserManager(BaseUserManager):

    def _create_user(self, email , password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, True , False,
                                 **extra_fields)


    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True,
                                 **extra_fields)



class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Creating a CustomUser model which defines
    """

    ACCOUNT_TYPES = {
        (1, _('Scientist')),
        (2, _('Staff'))
    }

    email = models.EmailField(_('Email address'), max_length=254, unique=True)
    first_name = models.CharField(_('First name'),max_length = 25)
    last_name = models.CharField(_('Last name'),max_length = 25)
    image = models.ImageField(_('Photo'),blank = True)
    phone_number = models.CharField(_('Phone number'),max_length = 25)
    speciality = models.CharField(_('Speciality'),max_length = 25 , blank = True)
    grad = models.CharField(_('Academic rank'),max_length = 25 , blank = True)
    cv = models.FileField(_('CV'),blank = True)
    account_type = models.IntegerField(_('Account typ'),default=1, choices=ACCOUNT_TYPES)
    career_describ = models.TextField()


    is_superuser = models.BooleanField(_('superuser status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_staff = models.BooleanField(_('staff status'), default=True,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active= models.BooleanField(_('staff status'), default=True,
        help_text=_('Designates whether the user has the permission to publish articles'))


    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_absolute_url(self):
        return reverse("profile", kwargs={"id" : self.id})

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()
    get_full_name.short_description = _("Full name")

    def get_short_name(self):
        "Returns the short name for the user."
        return self.email

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email])

    def get_gavatar(self):
        return '%s/%s?s=400' % ("https://www.gravatar.com/avatar", hashlib.md5(self.email).hexdigest())
