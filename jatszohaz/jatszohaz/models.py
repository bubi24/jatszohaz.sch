import logging
from django.conf import settings
from django.contrib.auth import user_logged_in
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

logger = logging.getLogger(__name__)


class JhUser(AbstractUser):
    mobile = models.CharField(
        verbose_name=_('mobile'),
        max_length=100,
        help_text=_('Mobile number for helping communication if necessery.'),
        blank=True
    )
    room = models.CharField(
        verbose_name=_('room'),
        max_length=100,
        help_text=_('Room number.'),
        blank=True
    )

    def get_entitlements(self):
        """
        Gets all auth.sch group memberships.
        Map keys:
         - title (list): all titles in VIR
         - status (str): öregtag tag or körvezető
         - start (date): join date
         - end (date): leave date
        :return: data map of the specified group.
        """
        if self.has_social_auth():
            for i in self.social_auth.first().extra_data['eduPersonEntitlement']:
                if i['id'] == settings.EDU_PERSON_ENTITLEMENT_ID:
                    return i

    def has_social_auth(self):
        return self.social_auth.count() > 0

    @receiver(user_logged_in)
    def user_logged_in(sender, user, request, **kwargs):
        user.update_permissions()

    def update_permissions(self):
        """
        Update user rights according to its entitlements
        """
        if self.get_entitlements() is not None:
            # TODO chage superuser status to actual permissions
            self.is_staff = True
            self.is_superuser = True
            self.save()
            logger.info("Updated permissions for user %d." % self.pk)

    def full_name(self):
        """
        :return: First name + lLst name
        """
        return "%s %s" % (self.first_name, self.last_name)

    def full_name2(self):
        """
        :return: Last name + First name
        """
        return "%s %s" % (self.last_name, self.first_name)

    def __str__(self):
        return "%s - %s" % (self.full_name2(), self.email)