from typing import Tuple
from django.contrib.auth.models import User
from django.db import models


class AccountsComments(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)
    userdetails = models.ForeignKey('AccountsUserdetails', models.DO_NOTHING)
    rating = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'accounts_comments'


class AccountsUserdetails(models.Model):
    province = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    municipality = models.CharField(max_length=100, blank=True, null=True)
    ward = models.IntegerField(blank=True, null=True)
    skilldetails = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField()
    age = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)
    skills = models.CharField(max_length=300, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'accounts_userdetails'
        unique_together = (('id', 'user'),)


class AccountsUserdetailsLikes(models.Model):
    userdetails = models.ForeignKey(AccountsUserdetails, models.DO_NOTHING)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'accounts_userdetails_likes'
        unique_together = (('userdetails', 'user'),)


class AccountsViewstracker(models.Model):
    timestamp = models.DateTimeField()
    userdetails = models.ForeignKey(AccountsUserdetails, models.DO_NOTHING)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'accounts_viewstracker'


class AuthGroup(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'
        unique_together = (('id', 'name'),)


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
    is_superuser = models.IntegerField()
    username = models.CharField(max_length=150)
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    last_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'
        unique_together = (('id', 'username'),)


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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.SmallIntegerField()

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


class SearchesFeatureditem(models.Model):
    name = models.CharField(max_length=100)
    featured = models.IntegerField()
    startdate = models.DateField()
    enddate = models.DateField()
    userdetails = models.ForeignKey(AccountsUserdetails, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'searches_featureditem'
        unique_together = (('id', 'userdetails'),)


class SearchesSearchquery(models.Model):
    query = models.CharField(max_length=150)
    timestamp = models.DateTimeField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'searches_searchquery'


class SqliteSequence(models.Model):
    name = models.TextField(blank=True, null=True)
    seq = models.TextField(blank=True, null=True)
    trial959 = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sqlite_sequence'


class TaggitTag(models.Model):
    name = models.CharField(unique=True, max_length=100)
    slug = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'taggit_tag'


class TaggitTaggeditem(models.Model):
    object_id = models.IntegerField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    tag = models.ForeignKey(TaggitTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'taggit_taggeditem'
        unique_together = (('content_type', 'object_id', 'tag'),)