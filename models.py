# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Action(models.Model):
    position = models.TextField(blank=True, null=True)  # This field type is a guess.
    type = models.TextField(blank=True, null=True)  # This field type is a guess.
    point = models.SmallIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, db_comment='7|82')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='8|82')
    deleted_at = models.DateTimeField(blank=True, null=True, db_comment='9|82')
    created_by = models.IntegerField(blank=True, null=True, db_comment='10|41')
    updated_by = models.IntegerField(blank=True, null=True, db_comment='11|41')
    deleted_by = models.IntegerField(blank=True, null=True, db_comment='12|41')
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'action'
        db_table_comment = '1'


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
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

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


class Banner(models.Model):
    start_date = models.DateField(db_comment=' reklamaning boshlanishi ')
    end_date = models.DateField(db_comment='reklamaning tugashi  ')
    price = models.IntegerField(db_comment='narxi')
    is_active = models.BooleanField(db_comment='activligi')
    link = models.CharField(max_length=255, blank=True, null=True, db_comment='reklama linki')
    content_url = models.CharField(max_length=255, blank=True, null=True, db_comment='rasm yoki video uchun havola')
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, db_comment='7|82')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='8|82')
    deleted_at = models.DateTimeField(blank=True, null=True, db_comment='9|82')
    created_by = models.IntegerField(blank=True, null=True, db_comment='10|41')
    deleted_by = models.IntegerField(blank=True, null=True, db_comment='12|41')
    updated_by = models.IntegerField(blank=True, null=True, db_comment='11|41')
    banner_type = models.TextField(blank=True, null=True)  # This field type is a guess.
    view_count = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'banner'
        db_table_comment = '2\r\nBanner: {start_date} - {end_date}-{price}'


class BannerView(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    banner_id = models.IntegerField()
    views = models.BigIntegerField(blank=True, null=True)
    device = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, db_comment='7|82')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='8|82')
    deleted_at = models.DateTimeField(blank=True, null=True, db_comment='9|82')
    created_by = models.IntegerField(blank=True, null=True, db_comment='10|41')
    deleted_by = models.IntegerField(blank=True, null=True, db_comment='12|41')
    updated_by = models.IntegerField(blank=True, null=True, db_comment='11|41')

    class Meta:
        managed = False
        db_table = 'banner_view'


class Card(models.Model):
    player_id = models.IntegerField(blank=True, null=True)
    card_type = models.CharField(max_length=10, blank=True, null=True)
    match_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, db_comment='7|82')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='8|82')
    deleted_at = models.DateTimeField(blank=True, null=True, db_comment='9|82')
    created_by = models.IntegerField(blank=True, null=True, db_comment='10|41')
    updated_by = models.IntegerField(blank=True, null=True, db_comment='11|41')
    deleted_by = models.IntegerField(blank=True, null=True, db_comment='12|41')

    class Meta:
        managed = False
        db_table = 'card'
        db_table_comment = '3\n'


class Club(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    competition_name = models.CharField(max_length=255, blank=True, null=True)
    name_ru = models.CharField(max_length=255, blank=True, null=True)
    competition_id = models.IntegerField(blank=True, null=True)
    club_link = models.CharField(max_length=255, blank=True, null=True)
    country_id = models.IntegerField(blank=True, null=True)
    native = models.CharField(max_length=255, blank=True, null=True)
    form_img = models.CharField(max_length=255, blank=True, null=True)
    slug = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    trainer = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, db_comment='7|82')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='8|82')
    deleted_at = models.DateTimeField(blank=True, null=True, db_comment='9|82')
    flag_url = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True, db_comment='10|41')
    updated_by = models.IntegerField(blank=True, null=True, db_comment='11|41')
    deleted_by = models.IntegerField(blank=True, null=True, db_comment='12|41')
    html_pahts = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'club'
        db_table_comment = '4'


class Company(models.Model):
    name = models.CharField(unique=True, max_length=255, blank=True, null=True, db_comment='44')
    location = models.TextField(blank=True, null=True, db_comment='88')
    address = models.TextField(blank=True, null=True, db_comment='88')
    inn = models.CharField(max_length=255, blank=True, null=True, db_comment='44')
    mfo = models.CharField(max_length=255, blank=True, null=True, db_comment='44')
    rs = models.CharField(max_length=255, blank=True, null=True, db_comment='44')
    logo = models.CharField(max_length=255, blank=True, null=True, db_comment='44')
    phone = models.CharField(max_length=255, blank=True, null=True, db_comment='44')
    website = models.CharField(max_length=255, blank=True, null=True, db_comment='44')
    founded = models.DateTimeField(blank=True, null=True, db_comment='44')
    expiration_time = models.DateTimeField(blank=True, null=True, db_comment='44')
    last_notified = models.DateTimeField(blank=True, null=True, db_comment='44')
    telegram_notification = models.BooleanField(blank=True, null=True, db_comment='44')
    email_notification = models.BooleanField(blank=True, null=True, db_comment='44')
    sms_notification = models.BooleanField(blank=True, null=True, db_comment='44')
    notification_date = models.IntegerField(blank=True, null=True, db_comment='22')
    created_at = models.DateTimeField(blank=True, null=True, db_comment='7|44')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='8|44')
    deleted_at = models.DateTimeField(blank=True, null=True, db_comment='9|44')
    created_by = models.ForeignKey('User', models.DO_NOTHING, db_column='created_by', blank=True, null=True, db_comment='10|22')
    updated_by = models.ForeignKey('User', models.DO_NOTHING, db_column='updated_by', related_name='company_updated_by_set', blank=True, null=True, db_comment='11|22')
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, db_column='deleted_by', related_name='company_deleted_by_set', blank=True, null=True, db_comment='12|22')

    class Meta:
        managed = False
        db_table = 'company'
        db_table_comment = '\r\n{location} - {address}'


class Competition(models.Model):
    title = models.CharField(max_length=255)
    counter = models.CharField(max_length=255, blank=True, null=True, db_comment='number of fixtures ,')
    country_id = models.IntegerField(blank=True, null=True)
    flag = models.CharField(max_length=255, blank=True, null=True)
    id = models.AutoField()
    name = models.CharField(max_length=255, blank=True, null=True)
    name_ru = models.CharField(max_length=255, blank=True, null=True)
    slug = models.CharField(max_length=255, blank=True, null=True)
    competition_link = models.CharField(max_length=255, blank=True, null=True)
    can_register = models.BooleanField(blank=True, null=True)
    team_count = models.IntegerField(blank=True, null=True)
    average_team_point = models.FloatField(blank=True, null=True)
    sum_of_team_point = models.IntegerField(blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, db_comment='7|82')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='8|82')
    deleted_at = models.DateTimeField(blank=True, null=True, db_comment='9|82')
    created_by = models.IntegerField(blank=True, null=True, db_comment='10|41')
    updated_by = models.IntegerField(blank=True, null=True, db_comment='11|41')
    deleted_by = models.IntegerField(blank=True, null=True, db_comment='12|41')

    class Meta:
        managed = False
        db_table = 'competition'
        db_table_comment = '6'


class Country(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=255, blank=True, null=True)
    flag_url = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, db_comment='7|82')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='8|82')
    deleted_at = models.DateTimeField(blank=True, null=True, db_comment='9|82')
    created_by = models.IntegerField(blank=True, null=True, db_comment='10|41')
    updated_by = models.IntegerField(blank=True, null=True, db_comment='11|41')
    deleted_by = models.IntegerField(blank=True, null=True, db_comment='12|41')

    class Meta:
        managed = False
        db_table = 'country'
        db_table_comment = '7'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

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


class Documents(models.Model):
    modification_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documents'


class Goal(models.Model):
    id = models.AutoField()
    player_id = models.IntegerField(blank=True, null=True)
    match_id = models.IntegerField(blank=True, null=True)
    is_own_goal = models.SmallIntegerField(blank=True, null=True)
    time = models.CharField(max_length=10, blank=True, null=True)
    is_penalty = models.SmallIntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, db_comment='7|82')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='8|82')
    deleted_at = models.DateTimeField(blank=True, null=True, db_comment='9|82')
    created_by = models.IntegerField(blank=True, null=True, db_comment='10|41')
    updated_by = models.IntegerField(blank=True, null=True, db_comment='11|41')
    deleted_by = models.IntegerField(blank=True, null=True, db_comment='12|41')

    class Meta:
        managed = False
        db_table = 'goal'
        db_table_comment = '8\ngoal: {player_id}-{match_id}'


class Match(models.Model):
    id = models.AutoField()
    home_club_id = models.IntegerField(blank=True, null=True, db_comment='table:club_id')
    away_club_id = models.IntegerField(blank=True, null=True, db_comment='table:club_id')
    started_date = models.DateTimeField(blank=True, null=True)
    season_id = models.IntegerField(blank=True, null=True)
    postphoned_date = models.DateTimeField(blank=True, null=True)
    winner_club_id = models.IntegerField(blank=True, null=True, db_comment='home|away|draw')
    finished_date = models.DateTimeField(blank=True, null=True)
    tour_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    home_club_result = models.SmallIntegerField(blank=True, null=True)
    away_club_result = models.SmallIntegerField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)  # This field type is a guess.
    competition_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, db_comment='7|82')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='8|82')
    deleted_at = models.DateTimeField(blank=True, null=True, db_comment='9|82')
    created_by = models.IntegerField(blank=True, null=True, db_comment='10|41')
    updated_by = models.IntegerField(blank=True, null=True, db_comment='11|41')
    deleted_by = models.IntegerField(blank=True, null=True, db_comment='12|41')

    class Meta:
        managed = False
        db_table = 'match'
        db_table_comment = '9\r\n{competition_id} - {tour_id}  {home_club_id} &  {away_club_id}'


class News(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=255, blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    author_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, db_comment='7|82')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='8|82')
    deleted_at = models.DateTimeField(blank=True, null=True, db_comment='9|82')
    created_by = models.IntegerField(blank=True, null=True, db_comment='10|41')
    updated_by = models.IntegerField(blank=True, null=True, db_comment='11|41')
    deleted_by = models.IntegerField(blank=True, null=True, db_comment='12|41')

    class Meta:
        managed = False
        db_table = 'news'
        db_table_comment = '10'


class PayBalance(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    system = models.TextField(blank=True, null=True)  # This field type is a guess.
    transaction_id = models.IntegerField(blank=True, null=True)
    currency_code = models.SmallIntegerField(blank=True, null=True)
    state = models.SmallIntegerField(blank=True, null=True)
    updated_time = models.DateTimeField(blank=True, null=True)
    detail = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, db_comment='7|82')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='8|82')
    deleted_at = models.DateTimeField(blank=True, null=True, db_comment='9|82')
    created_by = models.IntegerField(blank=True, null=True, db_comment='10|41')
    updated_by = models.IntegerField(blank=True, null=True, db_comment='11|41')
    deleted_by = models.IntegerField(blank=True, null=True, db_comment='12|41')

    class Meta:
        managed = False
        db_table = 'pay_balance'
        db_table_comment = '11\n{system}-{price}'


class PayExpense(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=255, blank=True, null=True)
    pay_package_id = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    team_id = models.IntegerField(blank=True, null=True)
    pay_package_type = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_at = models.DateTimeField(blank=True, null=True, db_comment='7|82')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='8|82')
    deleted_at = models.DateTimeField(blank=True, null=True, db_comment='9|82')
    created_by = models.IntegerField(blank=True, null=True, db_comment='10|41')
    updated_by = models.IntegerField(blank=True, null=True, db_comment='11|41')
    deleted_by = models.IntegerField(blank=True, null=True, db_comment='12|41')
    amount = models.FloatField(blank=True, null=True)
    tour_id = models.IntegerField(blank=True, null=True)
    competition_id = models.IntegerField(blank=True, null=True)
    system = models.TextField(blank=True, null=True)  # This field type is a guess.
    transaction_id = models.IntegerField(blank=True, null=True)
    currency_code = models.SmallIntegerField(blank=True, null=True)
    state = models.SmallIntegerField(blank=True, null=True)
    updated_time = models.DateTimeField(blank=True, null=True)
    detail = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pay_expense'
        db_table_comment = '12\n{system}-{pay_package_type}'


class PayPackage(models.Model):
    id = models.AutoField()
    name_uz = models.CharField(max_length=255, blank=True, null=True)
    type = models.TextField(blank=True, null=True)  # This field type is a guess.
    amount = models.FloatField(blank=True, null=True)
    priority = models.SmallIntegerField(blank=True, null=True)
    name_ru = models.CharField(max_length=255, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, db_comment='7|82')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='8|82')
    deleted_at = models.DateTimeField(blank=True, null=True, db_comment='9|82')
    created_by = models.IntegerField(blank=True, null=True, db_comment='10|41')
    updated_by = models.IntegerField(blank=True, null=True, db_comment='11|41')
    deleted_by = models.IntegerField(blank=True, null=True, db_comment='12|41')

    class Meta:
        managed = False
        db_table = 'pay_package'
        db_table_comment = '13'


class Player(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=255, blank=True, null=True)
    position = models.TextField(blank=True, null=True)  # This field type is a guess.
    price = models.FloatField(blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    shirt_number = models.SmallIntegerField(blank=True, null=True)
    club_id = models.IntegerField(blank=True, null=True)
    point = models.IntegerField(blank=True, null=True)
    name_ru = models.CharField(max_length=255, blank=True, null=True)
    player_link = models.CharField(max_length=255, blank=True, null=True)
    native = models.CharField(max_length=255, blank=True, null=True)
    slug = models.CharField(max_length=255, blank=True, null=True)
    competition_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, db_comment='7|82')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='8|82')
    deleted_at = models.DateTimeField(blank=True, null=True, db_comment='9|82')
    created_by = models.IntegerField(blank=True, null=True, db_comment='10|41')
    updated_by = models.IntegerField(blank=True, null=True, db_comment='11|41')
    deleted_by = models.IntegerField(blank=True, null=True, db_comment='12|41')
    team_count = models.IntegerField(blank=True, null=True)
    percentage = models.IntegerField(blank=True, null=True)
    is_actualized = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'player'
        db_table_comment = '14'


class PlayerPoint(models.Model):
    id = models.AutoField()
    player_id = models.IntegerField(blank=True, null=True)
    club_id = models.IntegerField(blank=True, null=True)
    competition_id = models.IntegerField(blank=True, null=True)
    match_id = models.IntegerField(blank=True, null=True)
    tour_id = models.IntegerField(blank=True, null=True)
    point = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    goal = models.SmallIntegerField(blank=True, null=True)
    goal_asist = models.SmallIntegerField(blank=True, null=True)
    missed_penalty = models.SmallIntegerField(blank=True, null=True)
    every_2_missed_goals = models.SmallIntegerField(blank=True, null=True)
    is_red_card = models.SmallIntegerField(blank=True, null=True)
    yellow_card = models.SmallIntegerField(blank=True, null=True)
    is_lineup = models.SmallIntegerField(blank=True, null=True)
    is_shutout = models.SmallIntegerField(blank=True, null=True)
    is_lineup_more_60 = models.SmallIntegerField(blank=True, null=True)
    player_result_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, db_comment='7|82')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='8|82')
    deleted_at = models.DateTimeField(blank=True, null=True, db_comment='9|82')
    created_by = models.IntegerField(blank=True, null=True, db_comment='10|41')
    updated_by = models.IntegerField(blank=True, null=True, db_comment='11|41')
    deleted_by = models.IntegerField(blank=True, null=True, db_comment='12|41')
    season_id = models.IntegerField(blank=True, null=True)
    blocked_penalty = models.IntegerField(blank=True, null=True)
    autogoal = models.IntegerField(blank=True, null=True)
    match_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'player_point'
        db_table_comment = '15\r\n{player_id}'


class PlayerResult(models.Model):
    id = models.AutoField()
    player_id = models.IntegerField(blank=True, null=True)
    club_id = models.IntegerField(blank=True, null=True)
    played_min = models.SmallIntegerField(blank=True, null=True)
    position = models.TextField(blank=True, null=True)  # This field type is a guess.
    competition_id = models.IntegerField(blank=True, null=True)
    match_id = models.IntegerField(blank=True, null=True)
    tour_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    is_lineup = models.BooleanField(blank=True, null=True)
    is_lineup_more_60 = models.BooleanField(blank=True, null=True)
    goal = models.SmallIntegerField(blank=True, null=True)
    goal_asist = models.SmallIntegerField(blank=True, null=True)
    missed_penalty = models.SmallIntegerField(blank=True, null=True)
    every_2_missed_goals = models.SmallIntegerField(blank=True, null=True)
    yellow_card = models.SmallIntegerField(blank=True, null=True)
    is_shutout = models.BooleanField(blank=True, null=True)
    is_red_card = models.BooleanField(blank=True, null=True)
    season_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, db_comment='7|82')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='8|82')
    deleted_at = models.DateTimeField(blank=True, null=True, db_comment='9|82')
    created_by = models.IntegerField(blank=True, null=True, db_comment='10|41')
    updated_by = models.IntegerField(blank=True, null=True, db_comment='11|41')
    deleted_by = models.IntegerField(blank=True, null=True, db_comment='12|41')
    blocked_penalty = models.IntegerField(blank=True, null=True)
    autogoal = models.IntegerField(blank=True, null=True)
    match_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'player_result'
        db_table_comment = '16\n{player_id}'


class Prize(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=255, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    competition_id = models.IntegerField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)  # This field type is a guess.
    order = models.SmallIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, db_comment='7|82')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='8|82')
    deleted_at = models.DateTimeField(blank=True, null=True, db_comment='9|82')
    created_by = models.IntegerField(blank=True, null=True, db_comment='10|41')
    deleted_by = models.IntegerField(blank=True, null=True, db_comment='12|41')
    updated_by = models.IntegerField(blank=True, null=True, db_comment='11|41')
    name_ru = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prize'
        db_table_comment = '17'


class Season(models.Model):
    id = models.AutoField()
    number = models.IntegerField(blank=True, null=True, db_comment='number of which fixture(tur)')
    name = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, db_comment='7|82')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='8|82')
    deleted_at = models.DateTimeField(blank=True, null=True, db_comment='9|82')
    created_by = models.IntegerField(blank=True, null=True, db_comment='10|41')
    updated_by = models.IntegerField(blank=True, null=True, db_comment='11|41')
    deleted_by = models.IntegerField(blank=True, null=True, db_comment='12|41')

    class Meta:
        managed = False
        db_table = 'season'
        db_table_comment = '18'


class SystemConfig(models.Model):
    id = models.BigAutoField(db_comment='1|41')
    key = models.TextField(db_comment='2|82')  # This field type is a guess.
    value = models.TextField(blank=True, null=True, db_comment='3|164')
    type = models.TextField(blank=True, null=True, db_comment='4|82')  # This field type is a guess.
    is_list = models.BooleanField(blank=True, null=True, db_comment='5|82')
    group = models.CharField(max_length=255, blank=True, null=True, db_comment='6|82')
    name = models.CharField(max_length=255, blank=True, null=True, db_comment='13|82')
    created_at = models.DateTimeField(blank=True, null=True, db_comment='7|82')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='8|82')
    deleted_at = models.DateTimeField(blank=True, null=True, db_comment='9|82')
    created_by = models.IntegerField(blank=True, null=True, db_comment='10|41')
    updated_by = models.IntegerField(blank=True, null=True, db_comment='11|41')
    deleted_by = models.IntegerField(blank=True, null=True, db_comment='12|41')

    class Meta:
        managed = False
        db_table = 'system_config'
        db_table_comment = '19\n{key}-{type}'


class SystemLanguage(models.Model):
    id = models.AutoField(db_comment='ID')
    name = models.CharField(max_length=255, blank=True, null=True, db_comment='Nomi')
    uz = models.TextField(blank=True, null=True, db_comment='Manzili')
    ru = models.TextField(blank=True, null=True)
    en = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, db_comment='Yaratilgan vaqti')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='Yangilangan vaqti')
    deleted_at = models.DateTimeField(blank=True, null=True, db_comment="O'chirilgan vaqti")
    created_by = models.IntegerField(blank=True, null=True, db_comment='Kim tomonidan yaratilgan')
    updated_by = models.IntegerField(blank=True, null=True, db_comment='Kim tomonidan yangilangan')
    deleted_by = models.IntegerField(blank=True, null=True, db_comment="Kim tomonidan o'chirilgan")

    class Meta:
        managed = False
        db_table = 'system_language'
        db_table_comment = '20'


class SystemNotification(models.Model):
    id = models.AutoField()
    user_id = models.IntegerField(blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    read_at = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)
    is_broadcast = models.BooleanField(blank=True, null=True)
    is_sms = models.BooleanField(blank=True, null=True)
    is_email = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'system_notification'
        db_table_comment = '21'


class SystemTable(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    t_tables = models.TextField(blank=True, null=True)  # This field type is a guess.
    field_hidden = models.JSONField(blank=True, null=True)
    field_readonly = models.JSONField(blank=True, null=True)
    role = models.TextField(blank=True, null=True)  # This field type is a guess.
    deny_read = models.BooleanField(blank=True, null=True)
    deny_edit = models.BooleanField(blank=True, null=True)
    deny_create = models.BooleanField(blank=True, null=True)
    deny_delete = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'system_table'
        db_table_comment = '22\n{t_table}-{role}'


class Team(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    competition_id = models.IntegerField(blank=True, null=True)
    formation = models.TextField(blank=True, null=True)  # This field type is a guess.
    def_field = models.SmallIntegerField(db_column='DEF', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    mid = models.SmallIntegerField(db_column='MID', blank=True, null=True)  # Field name made lowercase.
    str = models.SmallIntegerField(db_column='STR', blank=True, null=True)  # Field name made lowercase.
    registered_tour_id = models.IntegerField(blank=True, null=True)
    season_id = models.IntegerField(blank=True, null=True)
    point = models.FloatField(blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    balance = models.FloatField(blank=True, null=True)
    is_team_created = models.BooleanField()
    count_of_transfers = models.IntegerField(blank=True, null=True)
    transfers_from_one_team = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, db_comment='7|82')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='8|82')
    deleted_at = models.DateTimeField(blank=True, null=True, db_comment='9|82')
    created_by = models.IntegerField(blank=True, null=True, db_comment='10|41')
    updated_by = models.IntegerField(blank=True, null=True, db_comment='11|41')
    deleted_by = models.IntegerField(blank=True, null=True, db_comment='12|41')
    last_tour_point = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'team'
        db_table_comment = '23'


class TeamPlayer(models.Model):
    id = models.AutoField()
    player_id = models.IntegerField(blank=True, null=True)
    order_number = models.SmallIntegerField(blank=True, null=True, db_comment='in which position is set?')
    is_captain = models.BooleanField(blank=True, null=True)
    team_id = models.IntegerField(blank=True, null=True)
    position = models.TextField(blank=True, null=True)  # This field type is a guess.
    club_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    tour_id = models.IntegerField(blank=True, null=True)
    competition_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, db_comment='7|82')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='8|82')
    deleted_at = models.DateTimeField(blank=True, null=True, db_comment='9|82')
    created_by = models.IntegerField(blank=True, null=True, db_comment='10|41')
    updated_by = models.IntegerField(blank=True, null=True, db_comment='11|41')
    deleted_by = models.IntegerField(blank=True, null=True, db_comment='12|41')
    point = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'team_player'
        db_table_comment = '24'


class TeamPlayerClub(models.Model):
    id = models.BigAutoField()
    team_id = models.IntegerField(blank=True, null=True)
    club_id = models.IntegerField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    slug = models.CharField(blank=True, null=True)
    tour_id = models.IntegerField(blank=True, null=True)
    competition_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, db_comment='7|82')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='8|82')
    deleted_at = models.DateTimeField(blank=True, null=True, db_comment='9|82')
    created_by = models.IntegerField(blank=True, null=True, db_comment='10|41')
    updated_by = models.IntegerField(blank=True, null=True, db_comment='11|41')
    deleted_by = models.IntegerField(blank=True, null=True, db_comment='12|41')
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'team_player_club'
        db_table_comment = '25\n{competition_id}-{team_id}-{club_id}'


class Tour(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    competition_name = models.CharField(max_length=255, blank=True, null=True)
    season_name = models.CharField(blank=True, null=True)
    competition_id = models.IntegerField(blank=True, null=True)
    season_id = models.IntegerField(blank=True, null=True)
    datetime_start = models.DateTimeField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)  # This field type is a guess.
    order = models.IntegerField(blank=True, null=True)
    datetime_end = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, db_comment='7|82')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='8|82')
    deleted_at = models.DateTimeField(blank=True, null=True, db_comment='9|82')
    created_by = models.IntegerField(blank=True, null=True, db_comment='10|41')
    updated_by = models.IntegerField(blank=True, null=True, db_comment='11|41')
    deleted_by = models.IntegerField(blank=True, null=True, db_comment='12|41')
    is_last = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tour'
        db_table_comment = '26'


class TourTeam(models.Model):
    id = models.AutoField()
    user_id = models.IntegerField(blank=True, null=True)
    tour_id = models.IntegerField(blank=True, null=True)
    purchased_players = models.SmallIntegerField(blank=True, null=True)
    is_purchase_locked = models.BooleanField(blank=True, null=True)
    team_id = models.IntegerField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    point = models.FloatField(blank=True, null=True)
    competition_id = models.IntegerField(blank=True, null=True)
    season_id = models.IntegerField(blank=True, null=True)
    captain_id = models.IntegerField(blank=True, null=True)
    current_count_of_transfers = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, db_comment='7|82')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='8|82')
    deleted_at = models.DateTimeField(blank=True, null=True, db_comment='9|82')
    created_by = models.IntegerField(blank=True, null=True, db_comment='10|41')
    updated_by = models.IntegerField(blank=True, null=True, db_comment='11|41')
    deleted_by = models.IntegerField(blank=True, null=True, db_comment='12|41')
    name = models.CharField(max_length=255, blank=True, null=True)
    is_last = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tour_team'
        db_table_comment = '27\r\n{competition_id}-{tour_id}-{team_id}'


class User(models.Model):
    guid = models.UUIDField(blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING, blank=True, null=True)
    role = models.TextField(blank=True, null=True)  # This field type is a guess.
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(unique=True, max_length=255)
    phone = models.CharField(unique=True, max_length=255, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    photo = models.TextField(blank=True, null=True)
    is_super_admin = models.BooleanField(blank=True, null=True)
    phone_second = models.CharField(max_length=255, blank=True, null=True)
    phone_telegram = models.CharField(max_length=255, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    is_developer = models.BooleanField(blank=True, null=True)
    telegram_user = models.CharField(max_length=255, blank=True, null=True)
    grid_resize = models.JSONField(blank=True, null=True)
    grid_drag_drop = models.JSONField(blank=True, null=True)
    is_notified = models.BooleanField(blank=True, null=True)
    sms_code = models.CharField(max_length=255, blank=True, null=True)
    sms_created_at = models.DateTimeField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)
    middle_name = models.TextField(blank=True, null=True)
    gender = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    balance = models.FloatField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)
    language = models.TextField(blank=True, null=True)  # This field type is a guess.
    enable_notification = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class UserActivity(models.Model):
    id = models.AutoField()
    user_id = models.IntegerField(blank=True, null=True)
    activity = models.TextField(blank=True, null=True)  # This field type is a guess.
    team_id = models.IntegerField(blank=True, null=True)
    name_uz = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, db_comment='7|82')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='8|82')
    deleted_at = models.DateTimeField(blank=True, null=True, db_comment='9|82')
    created_by = models.IntegerField(blank=True, null=True, db_comment='10|41')
    updated_by = models.IntegerField(blank=True, null=True, db_comment='11|41')
    deleted_by = models.IntegerField(blank=True, null=True, db_comment='12|41')
    name_ru = models.TextField(blank=True, null=True)
    name_en = models.TextField(blank=True, null=True)
    tour_id = models.IntegerField(blank=True, null=True)
    competition_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_activity'
        db_table_comment = '29'


class UserPayment(models.Model):
    id = models.AutoField()
    user_id = models.IntegerField()
    in_amount = models.IntegerField(blank=True, null=True)
    added_balance = models.IntegerField(blank=True, null=True)
    currency = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, db_comment='7|82')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='8|82')
    deleted_at = models.DateTimeField(blank=True, null=True, db_comment='9|82')
    created_by = models.IntegerField(blank=True, null=True, db_comment='10|41')
    updated_by = models.IntegerField(blank=True, null=True, db_comment='11|41')
    deleted_by = models.IntegerField(blank=True, null=True, db_comment='12|41')

    class Meta:
        managed = False
        db_table = 'user_payment'
        db_table_comment = '30\n{user_id}-{in_amount}'


class UserPlayer(models.Model):
    id = models.AutoField()
    player_id = models.IntegerField(blank=True, null=True)
    user_match_id = models.IntegerField(blank=True, null=True)
    is_lineup_11 = models.SmallIntegerField(blank=True, null=True, db_comment='in luneup?')
    played_min = models.SmallIntegerField(blank=True, null=True)
    is_captain = models.BooleanField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, db_comment='7|82')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='8|82')
    deleted_at = models.DateTimeField(blank=True, null=True, db_comment='9|82')
    created_by = models.IntegerField(blank=True, null=True, db_comment='10|41')
    updated_by = models.IntegerField(blank=True, null=True, db_comment='11|41')
    deleted_by = models.IntegerField(blank=True, null=True, db_comment='12|41')

    class Meta:
        managed = False
        db_table = 'user_player'
        db_table_comment = '31\n{player_id}-{user_match_id}'


class UserPrize(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=255, blank=True, null=True)
    competition_id = models.IntegerField(blank=True, null=True)
    season_id = models.IntegerField(blank=True, null=True)
    team_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    prize_id = models.IntegerField(blank=True, null=True)
    team_point = models.IntegerField(blank=True, null=True)
    prize_order = models.SmallIntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True, db_comment='11|41')
    last_tour_point = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_prize'
        db_table_comment = '32\r\n{user_id}-{prize_id}'
