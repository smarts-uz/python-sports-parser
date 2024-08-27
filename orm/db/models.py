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
    club = models.ForeignKey('Club', models.DO_NOTHING, blank=True, null=True)
    match = models.ForeignKey('Match', models.DO_NOTHING, blank=True, null=True)
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
    team = models.ForeignKey('Team', models.DO_NOTHING)
    match = models.ForeignKey('Match', models.DO_NOTHING, blank=True, null=True)
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


class Club(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    flag_url = models.CharField(max_length=255, blank=True, null=True)
    country = models.ForeignKey('Country', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, db_comment='7|82')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='8|82')
    deleted_at = models.DateTimeField(blank=True, null=True, db_comment='9|82')
    created_by = models.IntegerField(blank=True, null=True, db_comment='10|41')
    updated_by = models.IntegerField(blank=True, null=True, db_comment='11|41')
    deleted_by = models.IntegerField(blank=True, null=True, db_comment='12|41')
    name_ru = models.CharField(max_length=255, blank=True, null=True)
    club_link = models.CharField(max_length=255, blank=True, null=True)
    native = models.CharField(max_length=255, blank=True, null=True)
    form_img = models.CharField(max_length=255, blank=True, null=True)
    slug = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    trainer = models.CharField(max_length=255, blank=True, null=True)
    competition_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'club'


class Company(models.Model):
    name = models.CharField(unique=True, max_length=255, blank=True, null=True)
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
    created_by = models.ForeignKey('User', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    updated_by = models.ForeignKey('User', models.DO_NOTHING, db_column='updated_by', related_name='company_updated_by_set', blank=True, null=True)
    deleted_by = models.ForeignKey('User', models.DO_NOTHING, db_column='deleted_by', related_name='company_deleted_by_set', blank=True, null=True)
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
    country_id = models.IntegerField(blank=True, null=True)
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


class Match(models.Model):
    home = models.ForeignKey(Club, models.DO_NOTHING, blank=True, null=True, db_comment='table:club_id')
    away = models.ForeignKey(Club, models.DO_NOTHING, related_name='match_away_set', blank=True, null=True, db_comment='table:club_id')
    starts_at = models.DateTimeField(blank=True, null=True)
    is_finished = models.SmallIntegerField(blank=True, null=True)
    season = models.ForeignKey('Season', models.DO_NOTHING, blank=True, null=True)
    is_postphoned = models.SmallIntegerField(blank=True, null=True)
    postphoned_date = models.DateTimeField(blank=True, null=True)
    win = models.CharField(max_length=255, blank=True, null=True, db_comment='home|away|draw')
    result = models.CharField(max_length=255, blank=True, null=True)
    finished_at = models.DateTimeField(blank=True, null=True)
    tour = models.ForeignKey('Tour', models.DO_NOTHING, blank=True, null=True)
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


class Player(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=100)  # This field type is a guess.
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
    name_ru = models.CharField(max_length=255, blank=True, null=True)
    player_link = models.CharField(max_length=255, blank=True, null=True)
    native = models.CharField(max_length=255, blank=True, null=True)
    slug = models.CharField(max_length=255, blank=True, null=True)
    competition_id = models.IntegerField(blank=True, null=True)

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


class Season(models.Model):
    number = models.IntegerField(blank=True, null=True, db_comment='number of which fixture(tur)')
    competition = models.ForeignKey(Competition, models.DO_NOTHING)
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
    name = models.CharField(max_length=255, blank=True, null=True)
    club = models.ForeignKey(Club, models.DO_NOTHING, blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    balance = models.IntegerField(blank=True, null=True)
    captain_id = models.IntegerField(blank=True, null=True)
    competition_id = models.IntegerField(blank=True, null=True)
    formation = models.TextField(blank=True, null=True)  # This field type is a guess.
    def_field = models.SmallIntegerField(db_column='DEF', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    mid = models.SmallIntegerField(db_column='MID', blank=True, null=True)  # Field name made lowercase.
    str = models.SmallIntegerField(db_column='STR', blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True, db_comment='7|82')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='8|82')
    deleted_at = models.DateTimeField(blank=True, null=True, db_comment='9|82')
    created_by = models.IntegerField(blank=True, null=True, db_comment='10|41')
    updated_by = models.IntegerField(blank=True, null=True, db_comment='11|41')
    deleted_by = models.IntegerField(blank=True, null=True, db_comment='12|41')
    tour = models.ForeignKey('Tour', models.DO_NOTHING, blank=True, null=True)

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


class Tour(models.Model):
    season = models.ForeignKey(Season, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    status = models.TextField(blank=True, null=True)  # This field type is a guess.
    competition = models.ForeignKey(Competition, models.DO_NOTHING, blank=True, null=True)
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
    guid = models.UUIDField(blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING, blank=True, null=True)
    role = models.TextField(blank=True, null=True)  # This field type is a guess.
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey('self', models.DO_NOTHING, db_column='created_by', blank=True, null=True)
    updated_by = models.ForeignKey('self', models.DO_NOTHING, db_column='updated_by', related_name='user_updated_by_set', blank=True, null=True)
    deleted_by = models.ForeignKey('self', models.DO_NOTHING, db_column='deleted_by', related_name='user_deleted_by_set', blank=True, null=True)
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
