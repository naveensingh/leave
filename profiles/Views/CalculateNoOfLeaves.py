from leavebase.models import LeaveBase



def get_no_of_leaves_by_user(user_id):

    get_leaves_of_user = LeaveBase.objects.filter(user_id=user_id)
    get_no_of_days = get_leaves_of_user.values_list("no_of_days")
    total_no_of_days = sum(get_no_of_days)
    return total_no_of_days
