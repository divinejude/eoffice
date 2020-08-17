from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    secretary = models.BooleanField(default=False)
    ssg = models.BooleanField(default=False)
    perm_sec_political = models.BooleanField(default=False)
    perm_sec_cas = models.BooleanField(default=False)
    perm_sec_general_admin = models.BooleanField(default=False)
    director_cabinet_affairs = models.BooleanField(default=False)
    director_security = models.BooleanField(default=False)
    director_internal_affairs = models.BooleanField(default=False)
    def __str__(self):
        return str(self.user)


class File(models.Model):
    file_name = models.CharField(max_length=1000)
    file_number = models.CharField(max_length=100, null=True, blank=True, default=None)
    file = models.FileField()
    date_of_file = models.DateField(null=True, blank=True, default=None)
    # secretary
    comment_from_secretary = models.TextField(max_length=1000, null=True, default=None, blank=True)
    # ssg
    moved_to_ssg = models.BooleanField(default=False)
    comment_from_ssg = models.TextField(max_length=1000, null=True, default=None, blank=True)
    moved_from_ssg = models.BooleanField(default=False)
    # perm sec cas
    moved_to_perm_sec_cas = models.BooleanField(default=False)
    comment_from_perm_sec_cas = models.TextField(max_length=1000, null=True, default=None, blank=True)
    moved_from_perm_sec_cas = models.BooleanField(default=False)
    # directors under perm sec cas
    # director security
    moved_to_director_security = models.BooleanField(default=False)
    comment_from_director_security = models.TextField(max_length=1000, null=True, default=None, blank=True)
    moved_from_director_security = models.BooleanField(default=False)
    # director internal affairs
    moved_to_director_internal_affairs = models.BooleanField(default=False)
    comment_from_director_internal_affairs = models.TextField(max_length=1000, null=True, default=None, blank=True)
    moved_from_director_internal_affairs = models.BooleanField(default=False)
    # director cabinet affairs
    moved_to_director_cabinet_affairs = models.BooleanField(default=False)
    comment_from_director_cabinet_affairs = models.TextField(max_length=1000, null=True, default=None, blank=True)
    moved_from_director_cabinet_affairs = models.BooleanField(default=False)
    # perm sec political
    moved_to_perm_sec_political = models.BooleanField(default=False)
    comment_from_perm_sec_political = models.TextField(max_length=1000, null=True, default=None, blank=True)
    moved_from_perm_sec_political = models.BooleanField(default=False)
    # perm sec general admin
    moved_to_perm_sec_general_admin = models.BooleanField(default=False)
    comment_from_perm_sec_general_admin = models.TextField(max_length=1000, null=True, default=None, blank=True)
    moved_from_perm_sec_general_admin = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('secretary:append_file_no', kwargs={'file_id': self.pk})

    def __str__(self):
        return self.file_name
# emmamech121@gmail.com
