# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class MatchPlayer(models.Model):
    player_id = models.IntegerField(blank=True, null=True)
    club_id = models.IntegerField(blank=True, null=True)
    match_id = models.IntegerField(blank=True, null=True)
    is_lineup_11 = models.SmallIntegerField(blank=True, null=True, db_comment='in luneup?')
    played_min = models.SmallIntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, db_comment='7|82')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='8|82')
    deleted_at = models.DateTimeField(blank=True, null=True, db_comment='9|82')
    created_by = models.IntegerField(blank=True, null=True, db_comment='10|41')
    updated_by = models.IntegerField(blank=True, null=True, db_comment='11|41')
    deleted_by = models.IntegerField(blank=True, null=True, db_comment='12|41')

    class Meta:
        managed = False
        db_table = '_match_player'


class UserMatch(models.Model):
    starts_at = models.DateTimeField(blank=True, null=True)
    is_finished = models.SmallIntegerField(blank=True, null=True)
    team_id = models.IntegerField()
    match_id = models.IntegerField(blank=True, null=True)
    is_postphoned = models.BooleanField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, db_comment='7|82')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='8|82')
    deleted_at = models.DateTimeField(blank=True, null=True, db_comment='9|82')
    created_by = models.IntegerField(blank=True, null=True, db_comment='10|41')
    updated_by = models.IntegerField(blank=True, null=True, db_comment='11|41')
    deleted_by = models.IntegerField(blank=True, null=True, db_comment='12|41')

    class Meta:
        managed = False
        db_table = '_user_match'


class Account(models.Model):
    id = models.IntegerField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account'


class Action(models.Model):
#     id = models.AutoField()
    position = models.TextField(blank=True, null=True)  # This field type is a guess.
    type = models.TextField(blank=True, null=True)  # This field type is a guess.
    point = models.SmallIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, db_comment='7|82')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='8|82')
    deleted_at = models.DateTimeField(blank=True, null=True, db_comment='9|82')
    created_by = models.IntegerField(blank=True, null=True, db_comment='10|41')
    updated_by = models.IntegerField(blank=True, null=True, db_comment='11|41')
    deleted_by = models.IntegerField(blank=True, null=True, db_comment='12|41')

    class Meta:
        managed = False
        db_table = 'action'


class Actors(models.Model):
    first_name = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actors'


class Addresses(models.Model):
    name = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    postal_code = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'addresses'


class Alter(models.Model):
    title = models.TextField(blank=True, null=True)
    author = models.TextField(blank=True, null=True)
    metadata = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alter'


class Arraytest(models.Model):
    id = models.IntegerField()
    textarray = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'arraytest'


class Books(models.Model):
    title = models.TextField(blank=True, null=True)
    author = models.TextField(blank=True, null=True)
    metadata = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'books'


class BoxOffice(models.Model):
    bo_date = models.DateField(primary_key=True)  # The composite primary key (bo_date, film_id) found, that is not supported. The first column is selected.
    film = models.ForeignKey('Films', models.DO_NOTHING)
    gross_revenue = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'box_office'
        unique_together = (('bo_date', 'film'),)


class Card(models.Model):
#     id = models.AutoField()
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


class Child(models.Model):
    id = models.OneToOneField('Parent', models.DO_NOTHING, db_column='id', primary_key=True)
    name = models.TextField(blank=True, null=True)
    father = models.ForeignKey('Parent', models.DO_NOTHING, db_column='father', related_name='child_father_set', blank=True, null=True)
    mother = models.ForeignKey('Parent', models.DO_NOTHING, db_column='mother', related_name='child_mother_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'child'


class Cities(models.Model):
    name = models.TextField(blank=True, null=True)
    country = models.ForeignKey('Countries', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cities'


class Club(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    flag_url = models.CharField(max_length=255, blank=True, null=True)
    country_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, db_comment='7|82')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='8|82')
    deleted_at = models.DateTimeField(blank=True, null=True, db_comment='9|82')
    created_by = models.IntegerField(blank=True, null=True, db_comment='10|41')
    updated_by = models.IntegerField(blank=True, null=True, db_comment='11|41')
    deleted_by = models.IntegerField(blank=True, null=True, db_comment='12|41')
    sports_url = models.CharField(max_length=255, blank=True, null=True)
    name_ru = models.CharField(max_length=255, blank=True, null=True)
    slug = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    trainer = models.CharField(max_length=255, blank=True, null=True)
    club_link = models.CharField(max_length=255, blank=True, null=True)
    native = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'club'


class Company(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    inn = models.CharField(max_length=255, blank=True, null=True)
    mfo = models.CharField(max_length=255, blank=True, null=True)
    rs = models.CharField(max_length=255, blank=True, null=True)
    logo = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    founded = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)
    expiration_time = models.DateTimeField(blank=True, null=True)
    last_notified = models.DateTimeField(blank=True, null=True)
    telegram_notification = models.BooleanField(blank=True, null=True)
    email_notification = models.BooleanField(blank=True, null=True)
    sms_notification = models.BooleanField(blank=True, null=True)
    notification_date = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company'


class Competition(models.Model):
    title = models.CharField(max_length=255)
    counter = models.CharField(max_length=255, blank=True, null=True, db_comment='number of fixtures ,')
    country = models.ForeignKey('Country', models.DO_NOTHING, blank=True, null=True)
    flag = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, db_comment='7|82')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='8|82')
    deleted_at = models.DateTimeField(blank=True, null=True, db_comment='9|82')
    created_by = models.IntegerField(blank=True, null=True, db_comment='10|41')
    updated_by = models.IntegerField(blank=True, null=True, db_comment='11|41')
    deleted_by = models.IntegerField(blank=True, null=True, db_comment='12|41')
    name_ru = models.CharField(max_length=255, blank=True, null=True)
    slug = models.CharField(max_length=255, blank=True, null=True)
    competition_link = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'competition'


class Competitions(models.Model):
    name = models.TextField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'competitions'


class Countries(models.Model):
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'countries'


class Countriess(models.Model):
    id = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)  # This field type is a guess.
    languages = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'countriess'


class Country(models.Model):
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


class Customers(models.Model):
    metadata = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'customers'


class Directors(models.Model):
    first_name = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'directors'


class Employees(models.Model):
    first_name = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)
    supervisor = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employees'


class Files(models.Model):
    blob = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'files'


class Films(models.Model):
    director = models.ForeignKey(Directors, models.DO_NOTHING, blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    language = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'films'


class Foo(models.Model):
    id = models.BigAutoField(primary_key=True)
    bar = models.TextField(blank=True, null=True)
    baz = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'foo'


class Formation(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, db_comment=' ex: 4x3x3')
    created_at = models.DateTimeField(blank=True, null=True)
    is_public = models.SmallIntegerField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'formation'


class Goal(models.Model):
#     id = models.AutoField()
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


class Grandparent(models.Model):
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grandparent'


class Lines(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    geom = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'lines'


class Match(models.Model):
    home_id = models.IntegerField(blank=True, null=True, db_comment='table:club_id')
    away_id = models.IntegerField(blank=True, null=True, db_comment='table:club_id')
    starts_at = models.DateTimeField(blank=True, null=True)
    is_finished = models.SmallIntegerField(blank=True, null=True)
    season_id = models.IntegerField(blank=True, null=True)
    is_postphoned = models.SmallIntegerField(blank=True, null=True)
    postphoned_date = models.DateTimeField(blank=True, null=True)
    win = models.CharField(max_length=255, blank=True, null=True, db_comment='home|away|draw')
    result = models.CharField(max_length=255, blank=True, null=True)
    finished_at = models.DateTimeField(blank=True, null=True)
    tour_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, db_comment='7|82')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='8|82')
    deleted_at = models.DateTimeField(blank=True, null=True, db_comment='9|82')
    created_by = models.IntegerField(blank=True, null=True, db_comment='10|41')
    updated_by = models.IntegerField(blank=True, null=True, db_comment='11|41')
    deleted_by = models.IntegerField(blank=True, null=True, db_comment='12|41')

    class Meta:
        managed = False
        db_table = 'match'
        db_table_comment = '\r\n{club_id} - {club_id}\r\n'


class MatchPlayer(models.Model):
#     id = models.AutoField()
    player_id = models.IntegerField(blank=True, null=True)
    club_id = models.IntegerField(blank=True, null=True)
    match_id = models.IntegerField(blank=True, null=True)
    is_lineup_11 = models.SmallIntegerField(blank=True, null=True, db_comment='in luneup?')
    played_min = models.SmallIntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, db_comment='7|82')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='8|82')
    deleted_at = models.DateTimeField(blank=True, null=True, db_comment='9|82')
    created_by = models.IntegerField(blank=True, null=True, db_comment='10|41')
    updated_by = models.IntegerField(blank=True, null=True, db_comment='11|41')
    deleted_by = models.IntegerField(blank=True, null=True, db_comment='12|41')

    class Meta:
        managed = False
        db_table = 'match_player'


class MatchResult(models.Model):
#     id = models.AutoField()
    player_id = models.IntegerField(blank=True, null=True)
    club_id = models.IntegerField(blank=True, null=True)
    match_id = models.IntegerField(blank=True, null=True)
    count = models.SmallIntegerField(blank=True, null=True, db_comment='in luneup?')
    point = models.IntegerField(blank=True, null=True)
    action = models.TextField(blank=True, null=True)  # This field type is a guess.
    tour_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, db_comment='7|82')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='8|82')
    deleted_at = models.DateTimeField(blank=True, null=True, db_comment='9|82')
    created_by = models.IntegerField(blank=True, null=True, db_comment='10|41')
    updated_by = models.IntegerField(blank=True, null=True, db_comment='11|41')
    deleted_by = models.IntegerField(blank=True, null=True, db_comment='12|41')

    class Meta:
        managed = False
        db_table = 'match_result'


class Members(models.Model):
    user = models.OneToOneField('Users', models.DO_NOTHING, primary_key=True)  # The composite primary key (user_id, team_id) found, that is not supported. The first column is selected.
    team = models.ForeignKey('Team', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'members'
        unique_together = (('user', 'team'),)


class Nominations(models.Model):
    competition = models.OneToOneField(Competitions, models.DO_NOTHING, primary_key=True)  # The composite primary key (competition_id, film_id) found, that is not supported. The first column is selected.
    film = models.ForeignKey(Films, models.DO_NOTHING)
    rank = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nominations'
        unique_together = (('competition', 'film'),)


class Orders(models.Model):
    name = models.TextField(blank=True, null=True)
    billing_address = models.ForeignKey(Addresses, models.DO_NOTHING, blank=True, null=True)
    shipping_address = models.ForeignKey(Addresses, models.DO_NOTHING, related_name='orders_shipping_address_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class Parent(models.Model):
    name = models.TextField(blank=True, null=True)
    parent = models.ForeignKey(Grandparent, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'parent'


class People(models.Model):
    first_name = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)
    job = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'people'


class Persons(models.Model):
    id = models.BigAutoField(primary_key=True)
    age = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    deceased = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'persons'


class Player(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    position = models.TextField(blank=True, null=True)  # This field type is a guess.
    price = models.IntegerField(blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    shirt_number = models.SmallIntegerField(blank=True, null=True)
    club = models.ForeignKey(Club, models.DO_NOTHING, blank=True, null=True)
    ochko = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, db_comment='7|82')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='8|82')
    deleted_at = models.DateTimeField(blank=True, null=True, db_comment='9|82')
    created_by = models.IntegerField(blank=True, null=True, db_comment='10|41')
    updated_by = models.IntegerField(blank=True, null=True, db_comment='11|41')
    deleted_by = models.IntegerField(blank=True, null=True, db_comment='12|41')
    player_link = models.CharField(max_length=255, blank=True, null=True)
    native = models.CharField(max_length=255, blank=True, null=True)
    name_ru = models.CharField(max_length=255, blank=True, null=True)
    slug = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'player'


class PlayerPoint(models.Model):
#     id = models.AutoField()
    player_id = models.IntegerField(blank=True, null=True)
    club_id = models.IntegerField(blank=True, null=True)
    competition_id = models.IntegerField(blank=True, null=True)
    match_id = models.IntegerField(blank=True, null=True)
    tour_id = models.IntegerField(blank=True, null=True)
    point = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, db_comment='7|82')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='8|82')
    deleted_at = models.DateTimeField(blank=True, null=True, db_comment='9|82')
    created_by = models.IntegerField(blank=True, null=True, db_comment='10|41')
    updated_by = models.IntegerField(blank=True, null=True, db_comment='11|41')
    deleted_by = models.IntegerField(blank=True, null=True, db_comment='12|41')

    class Meta:
        managed = False
        db_table = 'player_point'


class PlayerResult(models.Model):
#     id = models.AutoField()
    player_id = models.IntegerField(blank=True, null=True)
    club_id = models.IntegerField(blank=True, null=True)
    goal = models.IntegerField(blank=True, null=True)
    played_min = models.SmallIntegerField(blank=True, null=True)
    position = models.TextField(blank=True, null=True)  # This field type is a guess.
    competition_id = models.IntegerField(blank=True, null=True)
    match_id = models.IntegerField(blank=True, null=True)
    missed_penalty = models.SmallIntegerField(blank=True, null=True)
    goal_asist = models.SmallIntegerField(blank=True, null=True)
    shutout = models.SmallIntegerField(blank=True, null=True)
    every_2_missed_goals = models.SmallIntegerField(blank=True, null=True)
    yellow_card = models.SmallIntegerField(blank=True, null=True)
    red_card = models.SmallIntegerField(blank=True, null=True)
    tour_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, db_comment='7|82')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='8|82')
    deleted_at = models.DateTimeField(blank=True, null=True, db_comment='9|82')
    created_by = models.IntegerField(blank=True, null=True, db_comment='10|41')
    updated_by = models.IntegerField(blank=True, null=True, db_comment='11|41')
    deleted_by = models.IntegerField(blank=True, null=True, db_comment='12|41')

    class Meta:
        managed = False
        db_table = 'player_result'


class Premieres(models.Model):
    id = models.IntegerField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    film_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'premieres'


class Presidents(models.Model):
    first_name = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)
    predecessor = models.OneToOneField('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'presidents'


class Profiles(models.Model):
    id = models.UUIDField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profiles'


class Roless(models.Model):
    film = models.ForeignKey(Films, models.DO_NOTHING)
    actor = models.ForeignKey(Actors, models.DO_NOTHING)
    character = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'roless'
        unique_together = (('id', 'film', 'actor'),)


class Season(models.Model):
    number = models.IntegerField(blank=True, null=True, db_comment='number of which fixture(tur)')
    competition_id = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, db_comment='7|82')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='8|82')
    deleted_at = models.DateTimeField(blank=True, null=True, db_comment='9|82')
    created_by = models.IntegerField(blank=True, null=True, db_comment='10|41')
    updated_by = models.IntegerField(blank=True, null=True, db_comment='11|41')
    deleted_by = models.IntegerField(blank=True, null=True, db_comment='12|41')

    class Meta:
        managed = False
        db_table = 'season'


class SpatialRefSys(models.Model):
    srid = models.IntegerField(primary_key=True)
    auth_name = models.CharField(max_length=256, blank=True, null=True)
    auth_srid = models.IntegerField(blank=True, null=True)
    srtext = models.CharField(max_length=2048, blank=True, null=True)
    proj4text = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spatial_ref_sys'


class Student(models.Model):
    name = models.TextField(blank=True, null=True)
    range = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'student'


class Subscriptions(models.Model):
    subscriber = models.OneToOneField('Users1', models.DO_NOTHING, primary_key=True)  # The composite primary key (subscriber_id, subscribed_id) found, that is not supported. The first column is selected.
    subscribed = models.ForeignKey('Users1', models.DO_NOTHING, related_name='subscriptions_subscribed_set')
    type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscriptions'
        unique_together = (('subscriber', 'subscribed'),)


class SystemConfig(models.Model):
#     id = models.BigAutoField(db_comment='1|41')
    key = models.TextField(db_comment='2|82')  # This field type is a guess.
    value = models.TextField(blank=True, null=True, db_comment='3|164')
    type = models.TextField(blank=True, null=True, db_comment='4|82')  # This field type is a guess.
    is_list = models.BooleanField(blank=True, null=True, db_comment='5|82')
    group = models.CharField(max_length=255, blank=True, null=True, db_comment='6|82')
    created_at = models.DateTimeField(blank=True, null=True, db_comment='7|82')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='8|82')
    deleted_at = models.DateTimeField(blank=True, null=True, db_comment='9|82')
    created_by = models.IntegerField(blank=True, null=True, db_comment='10|41')
    updated_by = models.IntegerField(blank=True, null=True, db_comment='11|41')
    deleted_by = models.IntegerField(blank=True, null=True, db_comment='12|41')
    name = models.CharField(max_length=255, blank=True, null=True, db_comment='13|82')

    class Meta:
        managed = False
        db_table = 'system_config'
        db_table_comment = '18'


class SystemLanguage(models.Model):
#     id = models.AutoField(db_comment='ID')
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


class SystemNotification(models.Model):
#     id = models.AutoField()
    company_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255)
    data = models.TextField()
    type = models.TextField(blank=True, null=True)  # This field type is a guess.
    read_at = models.DateTimeField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'system_notification'


class SystemTable(models.Model):
#     id = models.AutoField()
    name = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    t_tables = models.TextField(blank=True, null=True)  # This field type is a guess.
    field_hidden = models.JSONField(blank=True, null=True)
    field_readonly = models.JSONField(blank=True, null=True)
    role = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)
    deny_read = models.BooleanField(blank=True, null=True)
    deny_edit = models.BooleanField(blank=True, null=True)
    deny_create = models.BooleanField(blank=True, null=True)
    deny_delete = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'system_table'


class Team(models.Model):
    team_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'team'


class TeamBalance(models.Model):
#     id = models.AutoField()
    balance = models.IntegerField(blank=True, null=True)
    team_id = models.IntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, db_comment='7|82')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='8|82')
    deleted_at = models.DateTimeField(blank=True, null=True, db_comment='9|82')
    created_by = models.IntegerField(blank=True, null=True, db_comment='10|41')
    updated_by = models.IntegerField(blank=True, null=True, db_comment='11|41')
    deleted_by = models.IntegerField(blank=True, null=True, db_comment='12|41')

    class Meta:
        managed = False
        db_table = 'team_balance'


class TeamFormation(models.Model):
#     id = models.AutoField()
    formation_id = models.IntegerField(blank=True, null=True, db_comment=' ex: 4x3x3')
    team_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, db_comment='7|82')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='8|82')
    deleted_at = models.DateTimeField(blank=True, null=True, db_comment='9|82')
    created_by = models.IntegerField(blank=True, null=True, db_comment='10|41')
    updated_by = models.IntegerField(blank=True, null=True, db_comment='11|41')
    deleted_by = models.IntegerField(blank=True, null=True, db_comment='12|41')

    class Meta:
        managed = False
        db_table = 'team_formation'


class TeamPlayer(models.Model):
#     id = models.AutoField()
    player_id = models.IntegerField(blank=True, null=True)
    is_lineup11 = models.SmallIntegerField(blank=True, null=True)
    order_number = models.SmallIntegerField(blank=True, null=True, db_comment='in which position is set?')
    is_captain = models.BooleanField(blank=True, null=True)
    team_id = models.IntegerField(blank=True, null=True)
    position = models.TextField(blank=True, null=True)  # This field type is a guess.
    sold = models.BooleanField(blank=True, null=True)
    club_id = models.IntegerField(blank=True, null=True)
    point = models.IntegerField(blank=True, null=True)
    sold_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, db_comment='7|82')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='8|82')
    deleted_at = models.DateTimeField(blank=True, null=True, db_comment='9|82')
    created_by = models.IntegerField(blank=True, null=True, db_comment='10|41')
    updated_by = models.IntegerField(blank=True, null=True, db_comment='11|41')
    deleted_by = models.IntegerField(blank=True, null=True, db_comment='12|41')

    class Meta:
        managed = False
        db_table = 'team_player'


class TeamPoint(models.Model):
#     id = models.AutoField()
    team_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    tour_id = models.IntegerField(blank=True, null=True)
    point = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, db_comment='7|82')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='8|82')
    deleted_at = models.DateTimeField(blank=True, null=True, db_comment='9|82')
    created_by = models.IntegerField(blank=True, null=True, db_comment='10|41')
    updated_by = models.IntegerField(blank=True, null=True, db_comment='11|41')
    deleted_by = models.IntegerField(blank=True, null=True, db_comment='12|41')

    class Meta:
        managed = False
        db_table = 'team_point'


class Teams(models.Model):
    team_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teams'


class TechnicalSpecs(models.Model):
    film = models.OneToOneField(Films, models.DO_NOTHING, primary_key=True)
    runtime = models.TimeField(blank=True, null=True)
    camera = models.TextField(blank=True, null=True)
    sound = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'technical_specs'


class Test12(models.Model):
    id = models.UUIDField(blank=True, null=True)
    name = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test12'


class Timestamps(models.Model):
    t = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'timestamps'


class Tour(models.Model):
#     id = models.AutoField()
    season_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    status = models.TextField(blank=True, null=True)  # This field type is a guess.
    competition_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, db_comment='7|82')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='8|82')
    deleted_at = models.DateTimeField(blank=True, null=True, db_comment='9|82')
    created_by = models.IntegerField(blank=True, null=True, db_comment='10|41')
    updated_by = models.IntegerField(blank=True, null=True, db_comment='11|41')
    deleted_by = models.IntegerField(blank=True, null=True, db_comment='12|41')
    deadline = models.DateTimeField(blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tour'


class TourTeam(models.Model):
#     id = models.AutoField()
    user_id = models.IntegerField(blank=True, null=True)
    tour_id = models.IntegerField(blank=True, null=True)
    purchased_players = models.SmallIntegerField(blank=True, null=True)
    is_purchase_locked = models.BooleanField(blank=True, null=True)
    team_id = models.IntegerField(blank=True, null=True)
    is_team_create = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tour_team'


class User(models.Model):
#     id = models.AutoField()
    guid = models.UUIDField(blank=True, null=True)
    company_id = models.IntegerField(blank=True, null=True)
    role = models.TextField(blank=True, null=True)  # This field type is a guess.
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    deleted_by = models.IntegerField(blank=True, null=True)
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

    class Meta:
        managed = False
        db_table = 'user'


class UserActivity(models.Model):
#     id = models.AutoField()
    user_id = models.IntegerField(blank=True, null=True)
    activity = models.TextField(blank=True, null=True)
    team_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, db_comment='7|82')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='8|82')
    deleted_at = models.DateTimeField(blank=True, null=True, db_comment='9|82')
    created_by = models.IntegerField(blank=True, null=True, db_comment='10|41')
    updated_by = models.IntegerField(blank=True, null=True, db_comment='11|41')
    deleted_by = models.IntegerField(blank=True, null=True, db_comment='12|41')

    class Meta:
        managed = False
        db_table = 'user_activity'


class UserPayment(models.Model):
#     id = models.AutoField()
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


class UserPlayer(models.Model):
#     id = models.AutoField()
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


class UserTransfer(models.Model):
#     id = models.AutoField()
    team_id = models.IntegerField(blank=True, null=True)
    player_id = models.IntegerField(blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
    transfer_type = models.CharField(max_length=255, blank=True, null=True, db_comment='buy | sell')
    name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, db_comment='7|82')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='8|82')
    deleted_at = models.DateTimeField(blank=True, null=True, db_comment='9|82')
    created_by = models.IntegerField(blank=True, null=True, db_comment='10|41')
    updated_by = models.IntegerField(blank=True, null=True, db_comment='11|41')
    deleted_by = models.IntegerField(blank=True, null=True, db_comment='12|41')

    class Meta:
        managed = False
        db_table = 'user_transfer'


class Users(models.Model):
    name = models.TextField(blank=True, null=True)
    range = models.BooleanField(blank=True, null=True)
    salary = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    bio_tsv = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'users'


class Users1(models.Model):
    first_name = models.TextField(blank=True, null=True)
    last_name = models.TextField(blank=True, null=True)
    username = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users1'
