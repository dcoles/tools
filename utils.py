import getpass


def get_userpass(user):
    """
    Returns a username, password tuple.

    `user` is of the form "username:password".
    If no password is provided then the user will be interactively prompted for
    one.
    """
    try:
        user, passwd = user.split(':', 1)
    except ValueError:
        user, passwd = user, getpass.getpass()

    return user, passwd
