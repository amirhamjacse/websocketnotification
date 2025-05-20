# settings.py or utils.py
FLOW_GROUPS = {
    1: "Manager",
    2: "Supervisor",
    3: "Admin",
}


from django.contrib.auth.models import Group

def get_group_by_level(level):
    from django.conf import settings
    group_name = settings.FLOW_GROUPS.get(level)
    return group_name

def user_in_group(user, group_name):
    return user.groups.filter(name=group_name).exists()
