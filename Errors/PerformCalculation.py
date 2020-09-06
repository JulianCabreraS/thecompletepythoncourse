def email_engaged_user(user):
    try:
        perform_calculation(user.engagement_metrics)
    except KeyError:
        print('Incorrect values provided to our calculation function')
    else:
        if user.score > 500:
            send_engagement_notification(user)


def get_user_score(user):
    try:
        perform_calculation(user.engagement_metrics)
    except KeyError:
        print('Incorrect values provided to our calculation function.')
    else:
        send_engagement_notification(user)


def perform_calculation(metrics):
    return metrics['clicks'] * 5 + metrics['hits'] * 2


def send_engagement_notification(user):
    print(f'Notification sent to {user}')

my_user = User('Rolf', {'clicks': 61, 'hits':100})
