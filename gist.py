#!/usr/bin/env python

"""Post GitHub Gists."""

from __future__ import print_function

import argparse
from collections import OrderedDict
import getpass
from os.path import basename

import requests


def post_gist(files, description=None, public=None, auth=None):
    data = dict(files=files)
    if description is not None:
        data['description'] = description
    if public is not None:
        data['public'] = public
    resp = requests.post('https://api.github.com/gists', json=data, auth=auth)
    resp.raise_for_status()

    return resp.json()


def get_userpass(user):
    try:
        user, passwd = user.split(':', 1)
    except ValueError:
        user, passwd = user, getpass.getpass()

    return user, passwd


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--description')
    parser.add_argument('-P', '--public', action='store_true')
    parser.add_argument('-u', '--user')
    parser.add_argument('file', nargs='+', type=argparse.FileType('r'))
    args = parser.parse_args()

    auth = get_userpass(args.user) if args.user else None
    files = OrderedDict(
            ((basename(f.name), {'content': f.read()}) for f in args.file))

    resp = post_gist(files, args.description, args.public, auth=auth)
    print('Created {} gist: {}'.format('public' if args.public else 'private',
                                       resp['html_url']))


if __name__ == '__main__':
    main()
