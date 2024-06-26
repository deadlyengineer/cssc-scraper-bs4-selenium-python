from turtle import home
import emoji
import string
import json
import os
import random
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
import re
import urllib.parse
import requests
import unicodedata
import sys
from constants import *
import time
from difflib import SequenceMatcher
from bs4 import BeautifulSoup


def slugify(value, allow_unicode=False):
    """
    Normalizes string, converts to lowercase, removes non-alpha characters,
    and converts spaces to hyphens.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode(
            'ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '-', value).strip('-_')


def remove_emoji(text):
    return emoji.get_emoji_regexp().sub(u'', text)


def clean_songtitle(songtitle):
    songtitle = songtitle.strip()
    songtitle = songtitle.replace('$', 's')
    songtitle = songtitle.replace('_', ' ')
    songtitle = songtitle.replace('.mp3', '')
    songtitle = songtitle.replace('mp3', '')
    songtitle = songtitle.replace('.Mp3', '')
    songtitle = songtitle.replace('Mp3', '')
    songtitle = songtitle.replace('.MP3', '')
    songtitle = songtitle.replace('MP3', '')
    songtitle = songtitle.replace('.m4a', '')
    songtitle = songtitle.replace('m4a', '')
    songtitle = songtitle.replace('.M4a', '')
    songtitle = songtitle.replace('M4a', '')
    songtitle = songtitle.replace('.M4A', '')
    songtitle = songtitle.replace('M4A', '')
    songtitle = songtitle.replace('.wav', '')
    songtitle = songtitle.replace('wav', '')
    songtitle = songtitle.replace('.Wav', '')
    songtitle = songtitle.replace('Wav', '')
    songtitle = songtitle.replace('.WAV', '')
    songtitle = songtitle.replace('WAV', '')
    songtitle = songtitle.replace('.mp4', '')
    songtitle = songtitle.replace('mp4', '')
    songtitle = songtitle.replace('.Mp4', '')
    songtitle = songtitle.replace('Mp4', '')
    songtitle = songtitle.replace('.MP4', '')
    songtitle = songtitle.replace('MP4', '')
    songtitle = songtitle.replace('!', '')
    songtitle = songtitle.replace('demo', '')
    songtitle = songtitle.replace('Demo', '')
    songtitle = songtitle.replace('snippet', '')
    songtitle = songtitle.replace('Snippet', '')
    songtitle = songtitle.replace('download', '')
    songtitle = songtitle.replace('Download', '')
    songtitle = songtitle.replace('*', '')
    songtitle = songtitle.replace('^', '')
    songtitle = songtitle.replace('=', '')
    songtitle = songtitle.replace(':', '')
    songtitle = songtitle.replace(';', '')
    songtitle = songtitle.replace('~', '')
    songtitle = songtitle.replace('`', '')
    songtitle = songtitle.replace('@', '')
    songtitle = songtitle.replace('(', '')
    songtitle = songtitle.replace(')', '')
    songtitle = songtitle.replace('[', '')
    songtitle = songtitle.replace(']', '')
    songtitle = songtitle.replace(':)', '')
    songtitle = songtitle.replace(':(', '')
    songtitle = songtitle.replace(':;', '')
    songtitle = songtitle.replace('<3', '')
    songtitle = songtitle.replace('<33', '')
    songtitle = songtitle.replace('<333', '')
    songtitle = songtitle.replace('<3333', '')
    songtitle = songtitle.replace('</3', '')
    songtitle = songtitle.replace('<//3', '')
    songtitle = songtitle.replace('<///3', '')
    songtitle = songtitle.replace('<////3', '')
    songtitle = songtitle.replace('<4', '')
    songtitle = songtitle.replace('<', '')
    songtitle = songtitle.replace('>', '')
    songtitle = songtitle.replace('nigga', 'ni**a')
    songtitle = songtitle.replace('Nigga', 'Ni**a')
    songtitle = songtitle.replace('niggas', 'ni**as')
    songtitle = songtitle.replace('Niggas', 'Ni**as')
    songtitle = songtitle.replace('nigger', 'ni**er')
    songtitle = songtitle.replace('Nigger', 'Ni**er')
    songtitle = songtitle.replace('niggers', 'ni**ers')
    songtitle = songtitle.replace('niggers', 'Ni**ers')
    songtitle = songtitle.replace('part 1.', '')
    songtitle = songtitle.replace('Part 1.', '')
    songtitle = songtitle.replace('part 1', '')
    songtitle = songtitle.replace('Part 1', '')
    songtitle = songtitle.replace('part 2.', '')
    songtitle = songtitle.replace('Part 2.', '')
    songtitle = songtitle.replace('part 2', '')
    songtitle = songtitle.replace('Part 2', '')
    songtitle = songtitle.replace('part 3.', '')
    songtitle = songtitle.replace('Part 3.', '')
    songtitle = songtitle.replace('part 3', '')
    songtitle = songtitle.replace('Part 3', '')
    songtitle = songtitle.replace('part 4.', '')
    songtitle = songtitle.replace('Part 4.', '')
    songtitle = songtitle.replace('part 4', '')
    songtitle = songtitle.replace('Part 4', '')
    songtitle = songtitle.replace('part 5.', '')
    songtitle = songtitle.replace('Part 5.', '')
    songtitle = songtitle.replace('part 5', '')
    songtitle = songtitle.replace('Part 5', '')
    songtitle = songtitle.replace('part 6.', '')
    songtitle = songtitle.replace('Part 6.', '')
    songtitle = songtitle.replace('part 6', '')
    songtitle = songtitle.replace('Part 6', '')
    songtitle = songtitle.replace('part 7.', '')
    songtitle = songtitle.replace('Part 7.', '')
    songtitle = songtitle.replace('part 7', '')
    songtitle = songtitle.replace('Part 7', '')
    songtitle = songtitle.replace('part 8.', '')
    songtitle = songtitle.replace('Part 8.', '')
    songtitle = songtitle.replace('part 8', '')
    songtitle = songtitle.replace('Part 8', '')
    songtitle = songtitle.replace('part 9.', '')
    songtitle = songtitle.replace('Part 9.', '')
    songtitle = songtitle.replace('part 9', '')
    songtitle = songtitle.replace('Part 9', '')
    songtitle = songtitle.replace('pt1', '')
    songtitle = songtitle.replace('Pt1', '')
    songtitle = songtitle.replace('pt 1', '')
    songtitle = songtitle.replace('pt. 1', '')
    songtitle = songtitle.replace('Pt 1', '')
    songtitle = songtitle.replace('Pt. 1', '')
    songtitle = songtitle.replace('PT. 1', '')
    songtitle = songtitle.replace('PT 1', '')
    songtitle = songtitle.replace('pt2', '')
    songtitle = songtitle.replace('Pt2', '')
    songtitle = songtitle.replace('pt 2', '')
    songtitle = songtitle.replace('pt. 2', '')
    songtitle = songtitle.replace('Pt 2', '')
    songtitle = songtitle.replace('Pt. 2', '')
    songtitle = songtitle.replace('PT. 2', '')
    songtitle = songtitle.replace('PT 2', '')
    songtitle = songtitle.replace('pt3', '')
    songtitle = songtitle.replace('Pt3', '')
    songtitle = songtitle.replace('pt 3', '')
    songtitle = songtitle.replace('pt. 3', '')
    songtitle = songtitle.replace('Pt 3', '')
    songtitle = songtitle.replace('Pt. 3', '')
    songtitle = songtitle.replace('PT. 3', '')
    songtitle = songtitle.replace('PT 3', '')
    songtitle = songtitle.replace('pt4', '')
    songtitle = songtitle.replace('Pt4', '')
    songtitle = songtitle.replace('pt 4', '')
    songtitle = songtitle.replace('pt. 4', '')
    songtitle = songtitle.replace('Pt 4', '')
    songtitle = songtitle.replace('Pt. 4', '')
    songtitle = songtitle.replace('PT. 4', '')
    songtitle = songtitle.replace('PT 4', '')
    songtitle = songtitle.replace('Vol. 1', '')
    songtitle = songtitle.replace('Vol. 2', '')
    songtitle = songtitle.replace('Vol. 2', '')
    songtitle = songtitle.replace('Vol. 3', '')
    songtitle = songtitle.replace('Vol. 4', '')
    songtitle = songtitle.replace('Vol. 5', '')
    songtitle = songtitle.replace('Vol. 6', '')
    songtitle = songtitle.replace('Vol. 7', '')
    songtitle = songtitle.replace('Vol. 8', '')
    songtitle = songtitle.replace('Vol. 9', '')
    songtitle = songtitle.replace('Vol. 10', '')
    songtitle = songtitle.replace('Vol. 11', '')
    songtitle = songtitle.replace('Vol. 12', '')
    songtitle = songtitle.replace('Vol. 13', '')
    songtitle = songtitle.replace('Vol. 14', '')
    songtitle = songtitle.replace('Vol. 15', '')
    songtitle = songtitle.replace('Vol. 16', '')
    songtitle = songtitle.replace('Vol. 17', '')
    songtitle = songtitle.replace('Vol. 18', '')
    songtitle = songtitle.replace('Vol. 19', '')
    songtitle = songtitle.replace('Vol. 20', '')
    songtitle = songtitle.replace('Vol. 21', '')
    songtitle = songtitle.replace('Vol. 22', '')
    songtitle = songtitle.replace('Vol. 23', '')
    songtitle = songtitle.replace('Vol. 24', '')
    songtitle = songtitle.replace('Vol. 25', '')
    songtitle = songtitle.replace('Vol. 26', '')
    songtitle = songtitle.replace('Vol. 27', '')
    songtitle = songtitle.replace('Vol. 28', '')
    songtitle = songtitle.replace('Vol. 29', '')
    songtitle = songtitle.replace('Vol. 30', '')
    songtitle = songtitle.replace('Vol. 31', '')
    songtitle = songtitle.replace('Vol. 32', '')
    songtitle = songtitle.replace('Vol. 33', '')
    songtitle = songtitle.replace('Vol. 34', '')
    songtitle = songtitle.replace('Vol. 35', '')
    songtitle = songtitle.replace('Vol. 36', '')
    songtitle = songtitle.replace('Vol. 37', '')
    songtitle = songtitle.replace('Vol. 38', '')
    songtitle = songtitle.replace('Vol. 39', '')
    songtitle = songtitle.replace('Vol. 40', '')
    songtitle = songtitle.replace('Vol. 41', '')
    songtitle = songtitle.replace('Vol. 42', '')
    songtitle = songtitle.replace('Vol. 43', '')
    songtitle = songtitle.replace('Vol. 44', '')
    songtitle = songtitle.replace('Vol. 45', '')
    songtitle = songtitle.replace('Vol. 46', '')
    songtitle = songtitle.replace('Vol. 47', '')
    songtitle = songtitle.replace('Vol. 48', '')
    songtitle = songtitle.replace('Vol. 49', '')
    songtitle = songtitle.replace('Vol. 50', '')
    songtitle = songtitle.replace('Vol. 51', '')
    songtitle = songtitle.replace('vol. 1', '')
    songtitle = songtitle.replace('vol. 2', '')
    songtitle = songtitle.replace('vol. 3', '')
    songtitle = songtitle.replace('vol. 4', '')
    songtitle = songtitle.replace('vol. 5', '')
    songtitle = songtitle.replace('vol. 6', '')
    songtitle = songtitle.replace('vol. 7', '')
    songtitle = songtitle.replace('vol. 8', '')
    songtitle = songtitle.replace('vol. 9', '')
    songtitle = songtitle.replace('vol. 10', '')
    songtitle = songtitle.replace('vol. 11', '')
    songtitle = songtitle.replace('vol. 12', '')
    songtitle = songtitle.replace('vol. 13', '')
    songtitle = songtitle.replace('vol. 14', '')
    songtitle = songtitle.replace('vol. 15', '')
    songtitle = songtitle.replace('vol. 16', '')
    songtitle = songtitle.replace('vol. 17', '')
    songtitle = songtitle.replace('vol. 18', '')
    songtitle = songtitle.replace('vol. 19', '')
    songtitle = songtitle.replace('vol. 20', '')
    songtitle = songtitle.replace('vol. 21', '')
    songtitle = songtitle.replace('vol. 22', '')
    songtitle = songtitle.replace('vol. 23', '')
    songtitle = songtitle.replace('vol. 24', '')
    songtitle = songtitle.replace('vol. 25', '')
    songtitle = songtitle.replace('vol 1', '')
    songtitle = songtitle.replace('vol 2', '')
    songtitle = songtitle.replace('vol 3', '')
    songtitle = songtitle.replace('vol 4', '')
    songtitle = songtitle.replace('vol 5', '')
    songtitle = songtitle.replace('vol 6', '')
    songtitle = songtitle.replace('vol 7', '')
    songtitle = songtitle.replace('vol 8', '')
    songtitle = songtitle.replace('vol 9', '')
    songtitle = songtitle.replace('01.', '')
    songtitle = songtitle.replace('01', '')
    songtitle = songtitle.replace('1.', '')
    songtitle = songtitle.replace('02.', '')
    songtitle = songtitle.replace('02', '')
    songtitle = songtitle.replace('2.', '')
    songtitle = songtitle.replace('03.', '')
    songtitle = songtitle.replace('03', '')
    songtitle = songtitle.replace('3.', '')
    songtitle = songtitle.replace('04.', '')
    songtitle = songtitle.replace('04', '')
    songtitle = songtitle.replace('4.', '')
    songtitle = songtitle.replace('05.', '')
    songtitle = songtitle.replace('05', '')
    songtitle = songtitle.replace('5.', '')
    songtitle = songtitle.replace('06.', '')
    songtitle = songtitle.replace('06', '')
    songtitle = songtitle.replace('6.', '')
    songtitle = songtitle.replace('07.', '')
    songtitle = songtitle.replace('07', '')
    songtitle = songtitle.replace('7.', '')
    songtitle = songtitle.replace('08.', '')
    songtitle = songtitle.replace('08', '')
    songtitle = songtitle.replace('8.', '')
    songtitle = songtitle.replace('09.', '')
    songtitle = songtitle.replace('09', '')
    songtitle = songtitle.replace('9.', '')
    songtitle = songtitle.replace('10.', '')
    songtitle = songtitle.replace('11.', '')
    songtitle = songtitle.replace('12.', '')
    songtitle = songtitle.replace('13.', '')
    songtitle = songtitle.replace('14.', '')
    songtitle = songtitle.replace('15.', '')
    songtitle = songtitle.replace('16.', '')
    songtitle = songtitle.replace('17.', '')
    songtitle = songtitle.replace('18.', '')
    songtitle = songtitle.replace('19.', '')
    songtitle = songtitle.replace('20.', '')
    songtitle = songtitle.replace('21.', '')
    songtitle = songtitle.replace('22.', '')
    songtitle = songtitle.replace('23.', '')
    songtitle = songtitle.replace('24.', '')
    songtitle = songtitle.replace('25.', '')
    songtitle = songtitle.replace('26.', '')
    songtitle = songtitle.replace('27.', '')
    songtitle = songtitle.replace('28.', '')
    songtitle = songtitle.replace('29.', '')
    songtitle = songtitle.replace('30.', '')
    songtitle = songtitle.replace('31.', '')
    songtitle = songtitle.replace('32.', '')
    songtitle = songtitle.replace('33.', '')
    songtitle = songtitle.replace('34.', '')
    songtitle = songtitle.replace('35.', '')
    songtitle = songtitle.replace('01', '')
    songtitle = songtitle.replace('02', '')
    songtitle = songtitle.replace('03', '')
    songtitle = songtitle.replace('04', '')
    songtitle = songtitle.replace('05', '')
    songtitle = songtitle.replace('06', '')
    songtitle = songtitle.replace('07', '')
    songtitle = songtitle.replace('08', '')
    songtitle = songtitle.replace('09', '')
    songtitle = songtitle.replace('10', '')
    songtitle = songtitle.replace('11', '')
    songtitle = songtitle.replace('12', '')
    songtitle = songtitle.replace('13', '')
    songtitle = songtitle.replace('14', '')
    songtitle = songtitle.replace('15', '')
    songtitle = songtitle.replace('16', '')
    songtitle = songtitle.replace('17', '')
    songtitle = songtitle.replace('18', '')
    songtitle = songtitle.replace('19', '')
    songtitle = songtitle.replace('20', '')
    songtitle = songtitle.replace('21', '')
    songtitle = songtitle.replace('22', '')
    songtitle = songtitle.replace('23', '')
    songtitle = songtitle.replace('24', '')
    songtitle = songtitle.replace('25', '')
    songtitle = songtitle.replace('26', '')
    songtitle = songtitle.replace('27', '')
    songtitle = songtitle.replace('28', '')
    songtitle = songtitle.replace('29', '')
    songtitle = songtitle.replace('30', '')
    songtitle = songtitle.replace('31', '')
    songtitle = songtitle.replace('32', '')
    songtitle = songtitle.replace('33', '')
    songtitle = songtitle.replace('34', '')
    songtitle = songtitle.replace('35', '')
    songtitle = songtitle.replace('new single', '')
    songtitle = songtitle.replace('New single', '')
    songtitle = songtitle.replace('New Single', '')
    songtitle = songtitle.replace('out now', '')
    songtitle = songtitle.replace('Out now', '')
    songtitle = songtitle.replace('Out Now', '')
    songtitle = songtitle.replace('itunes', '')
    songtitle = songtitle.replace('Itunes', '')
    songtitle = songtitle.replace('iTunes', '')
    songtitle = songtitle.replace('ITunes', '')
    songtitle = songtitle.replace('spotify', '')
    songtitle = songtitle.replace('Spotify', '')

    songtitle = string.capwords(songtitle)
    return songtitle


def clean_artistname(artistname):
    artistname = artistname.strip()
    artistname = artistname.replace('$', 's')
    artistname = artistname.replace('official', '')
    artistname = artistname.replace('Official', '')
    artistname = artistname.replace('OFFICIAL', '')
    artistname = artistname.replace('"', '')
    artistname = artistname.replace('_', ' ')
    artistname = artistname.replace('!', '')
    artistname = artistname.replace('?', '')
    artistname = artistname.replace('*', ' ')
    artistname = artistname.replace('^', '')
    artistname = artistname.replace('=', '')
    artistname = artistname.replace('+', '')
    artistname = artistname.replace(':', '')
    artistname = artistname.replace(';', '')

    if len(artistname) > 2 and artistname[-2:] == '//':
        artistname = artistname[:-2]
    if len(artistname) > 1 and artistname[-1] == '.':
        artistname = artistname[:-1]
    if len(artistname) > 1 and artistname[-1] == '/':
        artistname = artistname[:-1]
    if len(artistname) > 1 and artistname[0] == "'":
        artistname = artistname[1:]
    if len(artistname) > 1 and artistname[-1] == "'":
        artistname = artistname[:-1]
    if artistname[:4].lower() == 'user' and artistname[5:].isnumeric():
        artistname = 'man'

    artistname = string.capwords(artistname)

    return artistname.strip()


def get_bio_excludes():
    excludes = []
    try:
        if os.path.exists('json/bio.exclude.json'):
            with open('json/bio.exclude.json') as fd:
                obj = json.loads(fd.read())
                excludes = obj['excludes']
                return excludes
    except Exception as ex:
        print("JSON reading failed for json/bio.exclude.json.")
        print(ex)
    return excludes


def get_title_excludes():
    excludes = []
    try:
        if os.path.exists('json/title.exclude.json'):
            with open('json/title.exclude.json') as fd:
                obj = json.loads(fd.read())
                excludes = obj['excludes']
                # print("title excludes returned: ", excludes)
                return excludes
    except Exception as ex:
        print("JSON reading failed for json/title.exclude.json.")
        print(ex)
    return excludes


def get_famous_rapper_excludes():
    excludes = []
    try:
        if os.path.exists('json/famous_rapper.exclude.json'):
            with open('json/famous_rapper.exclude.json') as fd:
                obj = json.loads(fd.read())
                excludes = obj['excludes']
                return excludes
    except Exception as ex:
        print("JSON reading failed for json/famous_rapper.exclude.json.")
        print(ex)
    return excludes


def get_email_excludes():
    excludes = []
    try:
        if os.path.exists('json/email.exclude.json'):
            with open('json/email.exclude.json') as fd:
                obj = json.loads(fd.read())
                excludes = obj['excludes']
                return excludes
    except Exception as ex:
        print("JSON reading failed for json/email.exclude.json.")
        print(ex)
    return excludes


def get_repost_excludes():
    excludes = []
    try:
        if os.path.exists('json/repost.exclude.json'):
            with open('json/repost.exclude.json') as fd:
                obj = json.loads(fd.read())
                excludes = obj['excludes']
                return excludes
    except Exception as ex:
        print("JSON reading failed for json/repost.exclude.json.")
        print(ex)
    return excludes


def get_genre_includes():
    includes = []
    try:
        if os.path.exists('json/genre.include.json'):
            with open('json/genre.include.json') as fd:
                obj = json.loads(fd.read())
                includes = obj['includes']
                return includes
    except Exception as ex:
        print("JSON reading failed for json/genre.include.json.")
        print(ex)
    return includes


def am_get_genre_excludes():
    excludes = []
    try:
        if os.path.exists('json/am.genre.exclude.json'):
            with open('json/am.genre.exclude.json') as fd:
                obj = json.loads(fd.read())
                excludes = obj['excludes']
                return excludes
    except Exception as ex:
        print("JSON reading failed for json/genre.exclude.json.")
        print(ex)
    return excludes


def get_genre_excludes():
    excludes = []
    try:
        if os.path.exists('json/genre.exclude.json'):
            with open('json/genre.exclude.json') as fd:
                obj = json.loads(fd.read())
                excludes = obj['excludes']
                return excludes
    except Exception as ex:
        print("JSON reading failed for json/genre.exclude.json.")
        print(ex)
    return excludes


def get_LA_includes():
    includes = []
    try:
        if os.path.exists('json/LA.include.json'):
            with open('json/LA.include.json') as fd:
                obj = json.loads(fd.read())
                includes = obj['includes']
                return includes
    except Exception as ex:
        print("JSON reading failed for json/LA.include.json.")
        print(ex)
    return includes


def get_manager_bio_detect():
    includes = []
    try:
        if os.path.exists('json/managerbiodetect.json'):
            with open('json/managerbiodetect.json') as fd:
                obj = json.loads(fd.read())
                includes = obj['includes']
                return includes
    except Exception as ex:
        print("JSON reading failed for json/managerbiodetect.json.")
        print(ex)
    return includes


def get_manager_email_detect():
    includes = []
    try:
        if os.path.exists('json/managermaildetect.json'):
            with open('json/managermaildetect.json') as fd:
                obj = json.loads(fd.read())
                includes = obj['includes']
                return includes
    except Exception as ex:
        print("JSON reading failed for json/managermaildetect.json.")
        print(ex)
    return includes


def generate_password(size=10):
    chars = string.ascii_uppercase + string.digits + string.ascii_lowercase
    return ''.join(random.choice(chars) for _ in range(size))


def months(d1, d2):
    return d1.month - d2.month + 12*(d1.year - d2.year)


def get_non_GO_track_link(soup):
    for index, item in enumerate(soup.find_all(class_='sound__body')):
        goplus = item.find(class_='tierIndicator__smallGoPlus')
        if not goplus:
            continue
        if not 'sc-hidden' in goplus['class']:
            print('A track skipped as it is a GO+.')
            continue
        return item.find(class_="soundTitle__title").attrs['href'], item.find(class_="soundTitle__title").get_text().strip()
    print("All songs are GO+ tracks.")
    return "none", "none"


def get_popularity(soup, followers):
    for index, item in enumerate(soup.find_all(class_='sound__body')):
        goplus = item.find(class_='tierIndicator__smallGoPlus')
        if not goplus:
            continue
        if not 'sc-hidden' in goplus['class']:
            print('A track skipped as it is a GO+.')
            continue
        uploaddate = item.find(class_='soundTitle__uploadTime').find('time')[
            'datetime'].split('T')[0]
        uploaddateobj = datetime.fromisoformat(uploaddate)
        uploadedmonth = months(datetime.today(), uploaddateobj)
        if uploadedmonth >= 2:
            print(
                '{}th upload is selected for popularity verification.'.format(index + 1))
            try:
                songplay = int(item.find('li', class_='sc-ministats-item').find(
                    class_='sc-visuallyhidden').text.split()[0].replace(',', ''))
            except:
                songplay = 0
                pass

            try:
                comments = int(item.find_all(
                    'li', class_='sc-ministats-item')[1]['title'].split()[0].replace(',', ''))
            except:
                comments = 0
                pass

            if songplay / followers < 0.04 and comments < 5:
                return 'fake'
            else:
                return 'True'


def am_get_popularity(soup, followers):
    for index, item in enumerate(soup.find_all(class_='music-detail-container')):
        uploaddate = item.find(
            class_='music__meta-released').find('time')['datetime'].split('T')[0]
        uploaddateobj = datetime.fromisoformat(uploaddate)
        uploadedmonth = months(datetime.today(), uploaddateobj)
        if uploadedmonth >= 2 or index + 1 == len(soup.find_all(class_='music-detail-container')):
            print(
                '{}th upload is selected for popularity verification.'.format(index + 1))
            try:
                songplay = int(
                    item.find(class_='music-interaction__inner').text.split()[0].replace(',', ''))
            except:
                songplay = 0
                pass

            # try:
            #     comments = int(item.find('a', class_='music-interaction--comments').find(
            #         class_='music-interaction__count').text.split()[0].replace(',', ''))
            # except:
            #     comments = 0
            #     pass

            if songplay / followers < 0.04:
                return 'fake'
            else:
                return 'True'


def get_email_and_instagram_info_of_rapper(bio, web_profiles):

    email = None

    instagram_username = None

    instagram_url = None

    if web_profiles != None:
        instagram_username = web_profiles.select_one(
            "a[href*=instagram]")  # select href with instagram in it

        if instagram_username:

            try:
                instagram_username = urllib.parse.unquote(
                    instagram_username.attrs['href']).split(".com/")[1]  # split username from link
                if instagram_username[:2] == 'p/':
                    instagram_username = instagram_username[2:]
                if '/' in instagram_username:
                    instagram_username = instagram_username.split('/')[0]
                if '#' in instagram_username:
                    instagram_username = instagram_username.split('#')[0]
                if '?' in instagram_username:
                    instagram_username = instagram_username.split('?')[0]
                if '&' in instagram_username:
                    instagram_username = instagram_username.split('&')[0]

            except:
                instagram_username = None
                pass

    if bio != None:

        # Searches href with mailto: in it
        email = bio.select_one("a[href*=mailto]")

        if email:
            # get email address after mailto:
            email = email.attrs['href'].split(":")[1]
            bio = bio.text

        else:
            bio = bio.text
            # if email is not found as a link, searches email from texts
            email = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', bio)

            if email:
                email = email.group(0)

        if instagram_username == None:
            # if instagram_username is not found in web_profiles
            searched = INSTAGRAM_USERNAME_REGEX.search(bio)

            if searched:
                instagram_username = searched.group(2)

    if instagram_username:
        instagram_url = "https://www.instagram.com/" + \
            instagram_username  # generate url from username

    if email:
        email = email.encode("ascii", "ignore")
        email = email.decode()
        if not email.find(":") == -1:
            email = email.split(":")[1]
        if not email.find("/") == -1:
            email = email.split("//")[1]
        email_excludes = get_email_excludes()
        for item in email_excludes:
            if item in email:
                return None, None, None

    print("Email: ", email)

    print("Instagram: ", instagram_username)

    return email, instagram_username, instagram_url


def get_email_and_instagram_info_of_rapper(bio, web_profiles):

    email = None

    instagram_username = None

    instagram_url = None

    if web_profiles != None:
        instagram_username = web_profiles.select_one(
            "a[href*=instagram]")  # select href with instagram in it

        if instagram_username:

            try:
                instagram_username = urllib.parse.unquote(
                    instagram_username.attrs['href']).split(".com/")[1]  # split username from link
                if instagram_username[:2] == 'p/':
                    instagram_username = instagram_username[2:]
                if '/' in instagram_username:
                    instagram_username = instagram_username.split('/')[0]
                if '#' in instagram_username:
                    instagram_username = instagram_username.split('#')[0]
                if '?' in instagram_username:
                    instagram_username = instagram_username.split('?')[0]
                if '&' in instagram_username:
                    instagram_username = instagram_username.split('&')[0]

            except:
                instagram_username = None
                pass

    if bio != None:

        # Searches href with mailto: in it
        email = bio.select_one("a[href*=mailto]")

        if email:
            # get email address after mailto:
            email = email.attrs['href'].split(":")[1]
            bio = bio.text

        else:
            bio = bio.text
            # if email is not found as a link, searches email from texts
            email = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', bio)

            if email:
                email = email.group(0)

        if instagram_username == None:
            # if instagram_username is not found in web_profiles
            searched = INSTAGRAM_USERNAME_REGEX.search(bio)

            if searched:
                instagram_username = searched.group(2)

    if instagram_username:
        instagram_url = "https://www.instagram.com/" + \
            instagram_username  # generate url from username

    if email:
        email = email.encode("ascii", "ignore")
        email = email.decode()
        if not email.find(":") == -1:
            email = email.split(":")[1]
        if not email.find("/") == -1:
            email = email.split("//")[1]
        email_excludes = get_email_excludes()
        for item in email_excludes:
            if item in email:
                return None, None, None

    print("Email: ", email)

    print("Instagram: ", instagram_username)

    return email, instagram_username, instagram_url


def get_other_info_of_rapper(rapper_soup, permalink):
    try:
        songlink, songtitlefull = get_non_GO_track_link(rapper_soup)
        username = rapper_soup.find(
            class_='profileHeaderInfo__userName').get_text().strip()
    except:
        print("Cannot find username. This profile will be excluded")
        return "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded"

    for i in range(0, 100):

        try:
            user_search = json.loads(requests.get(profile_search_api.format(
                urllib.parse.quote(permalink))).content.decode('utf-8'))
        except:
            print(
                "Error occured while using user search API in https://soundcloud.com/" + permalink + "\n")
            print("Consider updating your API.")
            sys.exit()

        try:
            len(user_search['collection'])
            break
        except:
            if i == 99:
                print(
                    "Error occured while using user search API in https://soundcloud.com/" + permalink + "\n")
                print(
                    "No object returned in search of 100 times. Nothing to worry, but if this persists, contact developer.")
                return "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded"
            else:
                print("No object returned. Trying again for {}th lap.".format(i + 2))
                continue

    if len(user_search['collection']) == 0:
        try:
            user_search = json.loads(requests.get(profile_search_api.format(
                urllib.parse.quote(username))).content.decode('utf-8'))
        except:
            print(
                "Error occured while using user search API in https://soundcloud.com/" + permalink + "\n")
            print("Consider updating your API.")
            sys.exit()

    if len(user_search['collection']) == 0:
        print("Cannot retrieve user information from API search. This profile will be excluded.")
        return "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded"

    flag = False
    for item in user_search['collection']:
        if permalink.lower() in item['permalink'].lower():
            user_object = item
            flag = True
            break
    if not flag:
        print("User search failed. Selected user cannot be searched by the API search. This may be due to keyword problems. This profile will be excluded.")
        return "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded"

    followers = user_object['followers_count']
    popularity = 'unknown'
    if followers >= 10000:
        popularity = 'trending'
    if followers >= 50000:
        popularity = 'hot'
    if followers >= 100000:
        popularity = 'popular'
    if followers >= 250000:
        popularity = 'famous'
    if followers >= 500000:
        popularity = 'infamous'
    location = user_object['city']
    country = user_object['country_code']
    permalink = user_object['permalink']
    fullname = user_object['full_name']
    username = user_object['username']

    songtitlefull = unicodedata.normalize('NFKC', songtitlefull)

    search_entity = []
    search_entity.append(username)
    search_entity.append(fullname)
    # search_entity.append(artistname)
    search_entity.append(songtitlefull)
    title_excludes = get_title_excludes()
    for entity in search_entity:
        for item in title_excludes:
            if entity is not None and item in entity:
                print("The username or fullname or songtitlefull includes a word in title.exclude.json: ",
                      item,	' This profile will be excluded.')
                return "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded"

    if not fullname:
        fullname = username

    artistname = username

    songtitle = songtitlefull

    # checklist = songtitle.split()
    # all_capital_single = True
    # for item in checklist:
    # 	if not item.isupper():
    # 		all_capital_single = False

    # if all_capital_single:
    # 	wordlist = songtitlefull.split('	')
    # 	songtitle = " ".join([''.join(x.split()) for x in wordlist])

    username = remove_emoji(username)
    username = re.sub(r'[^\x00-\x7f]', r'', username)
    username = username.strip()
    try:
        if username[0] == '(' and ')' in username:
            username = username[1:].replace(')', '')
        if username[0] == '@':
            username = username[1:]
        if username[0] == '|':
            username = username[1:]
        if username[0] == '#':
            username = username[1:]
        if username[0] == '[' and ']' in username:
            username = username[1:].replace(']', '')
        if username[0] == '{' and '}' in username:
            username = username[1:].replace('}', '')
        if username[0] == '<' and '>' in username:
            username = username[1:].replace('>', '')
        if '@' in username:
            username = username.split('@')[0]
        if '#' in username:
            username = username.split('#')[0]
        if '(' in username:
            username = username.split('(')[0]
        if '[' in username:
            username = username.split('[')[0]
        if '{' in username:
            username = username.split('{')[0]
        if '|' in username:
            username = username.split('|')[0]
        username = username.strip()
    except:
        pass

    preceding_words = ["Prod. by", "Prod. By", "prod. by", "prod by", "Prod by", "Prod By", "PROD. BY", "PROD BY",
                       "Produced by", "ProducedBy", "produced by", "beat by", "Beat By", "Beat by", "Beat By", "Prod", "prod"]
    if username in songtitlefull:
        for word in preceding_words:
            if word + username in songtitlefull or '-' + word in songtitlefull or '- ' + word in songtitlefull:
                print(
                    'The songtitlefull includes prod-related part. This profile will be excluded.')
                return "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded"

    # if re.search(r'\(([^)]+)-([^)]+)\)', songtitlefull):
    # 	print(re.search(r'\(([^)]+)-([^)]+)\)', songtitlefull))
    username_list = username.split()
    artistname_list = artistname.split()
    songtitle = re.sub("[\{].*[\}]", "", songtitle)
    songtitle = re.sub("[\(].*[\)]", "", songtitle)
    songtitle = re.sub("[\[].*[\]]", "", songtitle)
    songtitle = re.sub("[\*].*[\*]", "", songtitle)
    songtitle = ' '.join(word for word in songtitle.split(
        ' ') if not word.startswith('#'))
    songtitle = ' '.join(word for word in songtitle.split(
        ' ') if not word.startswith('@'))
    songtitle = ' '.join(word for word in songtitle.split(
        ' ') if not word.startswith('*'))
    songtitle = ' '.join(word for word in songtitle.split(
        ' ') if not word.startswith('['))

    if ' - ' in songtitle:
        candidates = songtitle.split(' - ')
        popout_amounts = []
        for index1, candidateitem in enumerate(candidates):
            popout_list = []
            for index, item in enumerate(candidateitem.split()):
                for usernameitem in username_list:
                    if SequenceMatcher(None, a=item.lower(), b=usernameitem.lower()).ratio() > 0.5:
                        popout_list.append(index)
                for artistnameitem in artistname_list:
                    if SequenceMatcher(None, a=item.lower(), b=artistnameitem.lower()).ratio() > 0.5:
                        popout_list.append(index)
            popout_amounts.append(len(popout_list))
        if max(popout_amounts) > 1:
            songtitle = candidates[popout_amounts.index(min(popout_amounts))]
    elif ' ~ ' in songtitle:
        candidates = songtitle.split('~')
        popout_amounts = []
        for index1, candidateitem in enumerate(candidates):
            popout_list = []
            for index, item in enumerate(candidateitem.split()):
                for usernameitem in username_list:
                    if SequenceMatcher(None, a=item.lower(), b=usernameitem.lower()).ratio() > 0.5:
                        popout_list.append(index)
                for artistnameitem in artistname_list:
                    if SequenceMatcher(None, a=item.lower(), b=artistnameitem.lower()).ratio() > 0.5:
                        popout_list.append(index)
            popout_amounts.append(len(popout_list))
        if max(popout_amounts) > 1:
            songtitle = candidates[popout_amounts.index(min(popout_amounts))]
    else:
        popout_list = []
        songtitle_list = songtitle.split()
        for index, item in enumerate(songtitle_list):
            for usernameitem in username_list:
                if SequenceMatcher(None, a=item.lower(), b=usernameitem.lower()).ratio() > 0.5:
                    popout_list.append(index)
            for artistnameitem in artistname_list:
                if SequenceMatcher(None, a=item.lower(), b=artistnameitem.lower()).ratio() > 0.5:
                    popout_list.append(index)

        if len(popout_list) > 0:
            popout_list = list(set(popout_list))
            popout_list.sort(reverse=True)
            for item in popout_list:
                songtitle_list.pop(item)
            songtitle = ' '.join(songtitle_list)

    if songtitle.strip() == '':
        songtitle = songtitlefull
    try:
        if not songtitle[0] == '(':
            songtitle = songtitle.split('(')[0]
        if not songtitle[0] == "[":
            songtitle = songtitle.split('[')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('Feat')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('Feat.')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('feat')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('feat.')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('FEAT')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('FEAT.')[0]
    except:
        pass
    try:
        songtitle = songtitle.split(' x ')[0]
    except:
        pass
    try:
        songtitle = songtitle.split(' X ')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('ft')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('ft.')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('Ft')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('Ft.')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('FT')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('FT.')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('/')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('|')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('+')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('FREE] ')[1]
    except:
        pass
    try:
        songtitle = songtitle.split(':')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('?')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('Mixed by')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('Mixed By')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('mixed by')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('-prod')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('-prod.')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('-Prod')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('-Prod.')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('-PROD')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('-PROD.')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('_prod')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('_prod.')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('_Prod')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('_Prod.')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('_PROD.')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('Prod')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('Prod.')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('prod')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('prod.')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('PROD')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('PROD.')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('produced by')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('Produced by')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('Produced By')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('PRODUCED')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('beat by')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('Beat by')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('Beat By')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('BEAT BY')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('¨')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('feat.')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('Feat.')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('FEAT.')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('@')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('#')[0]
    except:
        pass
    try:
        songtitle = songtitle.split(',')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('featuring')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('Featuring')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('FEATURING')[0]
    except:
        pass
    try:
        songtitle = songtitle.split(' prod')[0]
    except:
        pass
    try:
        songtitle = songtitle.split(' prod.')[0]
    except:
        pass
    try:
        songtitle = songtitle.split(' pro')[0]
    except:
        pass
    try:
        songtitle = songtitle.split(' Pro')[0]
    except:
        pass
    try:
        songtitle = songtitle.split(' by')[0]
    except:
        pass
    try:
        songtitle = songtitle.split(' By')[0]
    except:
        pass
    try:
        tempsongtitle = songtitle.split('-')[0]
        if tempsongtitle[-2:].lower() != 're' or tempsongtitle[-2:].lower() != 'un':
            songtitle = tempsongtitle
    except:
        pass
    try:
        songtitle = songtitle.split('*')[0]
    except:
        pass
    try:
        if songtitle[0] == '@':
            songtitle = ' '.join(songtitle.split()[1:])
    except:
        pass
    try:
        if songtitle[0] == '#':
            songtitle = ' '.join(songtitle.split()[1:])
    except:
        pass
    try:
        songtitle = songtitle.replace('"', '')
        songtitle = songtitle.replace("'", "")
    except:
        pass
    src_str = re.compile("freestyle", re.IGNORECASE)
    songtitle = src_str.sub('', songtitle)

    artistname = username
    famous_rapper_excludes = get_famous_rapper_excludes()
    for item in famous_rapper_excludes:
        if item in artistname:
            artistname = 'man'
            break

    songtitle = songtitle.strip()
    if songtitle:
        songtitle = songtitle.encode("ascii", "ignore")
        songtitle = songtitle.decode()
    else:
        print('Failed to convert songtitle to ASCII friendly letters. This profile will be excluded.')
        return "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded"
    if artistname:
        artistname = artistname.encode("ascii", "ignore")
        artistname = artistname.decode()

    artistnamecleaned = clean_artistname(artistname)
    print('cleaned artistname ', artistname)
    songtitle = clean_songtitle(songtitle)
    print('cleaned songtitle ', songtitle)

    for prec_word in preceding_words:
        if prec_word in songtitlefull:
            second_half = songtitlefull.split(prec_word)[1].strip()
            # check for artistname
            if len(artistnamecleaned.split()) <= len(second_half.split()):
                candidate_string = ' '.join(
                    second_half.split()[0:len(artistnamecleaned.split())])
                if SequenceMatcher(None, a=candidate_string.lower(), b=artistnamecleaned.lower()).ratio() > 0.5:
                    print(
                        'The sonetitlefull includes prod related word immediately followed by artistname. This profile will be excluded')
                    return "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded"
            # check for username
            if len(username.split()) <= len(second_half.split()):
                candidate_string = ' '.join(
                    second_half.split()[0:len(username.split())])
                if SequenceMatcher(None, a=candidate_string.lower(), b=username.lower()).ratio() > 0.5:
                    print(
                        'The sonetitlefull includes prod related word immediately followed by artistname. This profile will be excluded')
                    return "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded"

    if len(artistname) > 5:
        artistname = artistname.strip('.')
    if len(artistnamecleaned) > 5:
        artistname = artistnamecleaned.strip('.')
    if len(songtitle) > 5:
        songtitle = songtitle.strip('.')
    if len(username) > 5:
        username = username.strip('.')
    if len(fullname) > 5:
        fullname = fullname.strip('.')

    return username, fullname, artistname, artistnamecleaned, location, country, songtitle, songtitlefull, followers, popularity, songlink


def click_cookie_button(driver):

    print("See if there is cookie button.")
    try:
        l = driver.find_element_by_css_selector(
            "button#onetrust-accept-btn-handler")
        l.click()
        print("Cookie button found and clicked.")
    except:
        print("Cookie button not found.")
        pass


def take_screenshot(url, username, title, gostatus):
    print("Opening driver for screenshot...")
    service = webdriver.chrome.service.Service(executable_path=DRIVER_PATH)
    driver = webdriver.Chrome(options=DRIVER_OPTIONS,
                              service=service)
    driver.set_page_load_timeout(10000)
    print("Getting screenshot from: ", url)
    driver.get(url)
    homepage = False
    try:
        blocked = driver.find_element_by_class_name('blockedTrackMessage')
        if blocked:
            print("The song deleted. Getting the home page.")
            driver.get(url.rsplit('/', 1)[0])
            homepage = True
    except:
        pass

    time.sleep(2)

    click_cookie_button(driver)

    try:
        if gostatus == 'No' and not homepage:
            print('Driver opened. Now moving cursor...')
            target = driver.find_element_by_class_name(
                'playbackTimeline__progressBar')
            playbutton = driver.find_element_by_class_name('sc-button-play')
            # bar = driver.find_element_by_class_name('listenContext')
            action = ActionChains(driver)
            # action.move_to_element_with_offset(WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, 'playbackTimeline__progressBar'))), 100, 0).click().perform()
            action.move_to_element_with_offset(
                target, 100, 0).click().perform()
            time.sleep(1)
            action.move_to_element(playbutton).click().perform()
            time.sleep(1)
            # action.move_to_element_with_offset(bar, 10, 10).perform()
            print('Cursor moved. Now taking screenshot...')
        elif homepage:
            print("Taking screenshot of main page.")
        else:
            print('All the tracks are GO+, taking screenshot of main page.')
            homepage = True
            # click_cookie_button(driver)

        filename = '{}_{}.png'.format(
            slugify(username), slugify(title)).lower()
        if homepage:
            click_cookie_button(driver)
            print("Logging URL with homepage screenshot.")
            with open('main_txt/rapper_with_deleted_song.txt', 'a') as f:
                f.write(url.rsplit('/', 1)[0])
                f.write('\n')
        time.sleep(1)
        driver.save_screenshot(os.path.join('screenshots', filename))
        driver.close()
        print('Screenshot saved in the name of {}'.format(filename))
        print('\n')
        return filename
    except Exception as e:
        print(e)
        print('screenshot failed to be created.')
        pass

    try:
        driver.close()
    except:
        pass
    return 'None'


def check_genre(all_genres, n, rescrape):

    if not rescrape:
        genre_includes = get_genre_includes()
        if len(all_genres) > n:
            all_genres = all_genres[0:n]
        elif len(all_genres) == 0:
            print("This profile does not have any song. This will be ignored.")
            return False
        for genre in all_genres:
            if not genre in genre_includes:
                print(
                    "This profile has words not in genre include list. This will be ignored.")
                return False
    else:
        genre_excludes = get_genre_excludes()
        for item in genre_excludes:
            if item in all_genres:
                print("This profile have this genre: ", item)
                print("Ignoring profile...")
                return False
    return True


def am_check_genre(all_genres, n, rescrape):

    if not rescrape:
        genre_includes = get_genre_includes()
        if len(all_genres) > n:
            all_genres = all_genres[0:n]
        elif len(all_genres) == 0:
            print("This profile does not have any song. This will be ignored.")
            return False
        for genre in all_genres:
            if genre in genre_includes:
                print(
                    "This profile has words in genre include list. This will be included.")
                return True
    else:
        genre_excludes = get_genre_excludes()
        for item in genre_excludes:
            if item in all_genres:
                print("This profile have this genre: ", item)
                print("Ignoring profile...")
                return False
    return True


def get_endless_scroll_content(url):
    service = webdriver.chrome.service.Service(executable_path=DRIVER_PATH)
    tempdriver = webdriver.Chrome(
        options=DRIVER_OPTIONS, service=service)
    tempdriver.set_page_load_timeout(10000)
    tempdriver.set_script_timeout(10000)
    tempdriver.get(url)
    time.sleep(1)
    click_cookie_button(tempdriver)
    # scroll_threshold = 500
    scroll_threshold = 10
    scroll_pause_time = 2

    i = 0
    while True:
        i += 1
        try:
            last_height = tempdriver.execute_script(
                "return document.body.scrollHeight")
            tempdriver.execute_script(
                "window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(scroll_pause_time)
            new_height = tempdriver.execute_script(
                "return document.body.scrollHeight")
            print('{}th scroll made.'.format(i))
        except Exception as e:
            print(e)
            print("error in getting data. Passing to next iteration")
            return

        if last_height == new_height or i == scroll_threshold:
            print("Scroll finished. Now scraping... 12")
            break

    soup = BeautifulSoup(tempdriver.page_source, "html.parser")
    tempdriver.close()
    return soup


def check_bio(soup):
    bio_excludes = get_bio_excludes()
    bio_text = soup.text

    if 'soundcloud' in bio_text:
        print("Soundcloud detected in bio.")

    flag = 0
    checklist = ["rapper", "Rapper", "rappers", "Rappers", "rap", "Rap"]
    for item in checklist:
        if item in bio_text:
            flag = 1
            break

    if flag == 1:
        print('Bio includes inclusion word, changing the exclude list...')
        bio_excludes = ["producer", "Producer", "Rapper/Producer", "rapper/producer",
                        "Rapper/producer", "rapper/Producer", "email me for beats", "DJ"]

    flag = 0
    for item in bio_excludes:
        if item in bio_text:
            flag = 1
            break
    if flag == 1:
        print('Bio includes exception word. Passing to next url.')
        return False
    return True

# return username, fullname, artistname, artistnamecleaned, location, country, songtitle, songtitlefull, followers, popularity, songlink, phoneno1, phoneno2


def am_get_other_info_of_rapper(rapper_soup, rapper_url):
    username = rapper_soup.select_one(
        'p[class*="ArtistHeader-module__slug"]').get_text().strip()
    print(f"Username: {username}")

    fullname = rapper_soup.select_one(
        'h1[class*="ArtistHeader-module__name"]').get_text().strip()
    print(f"Fullname: {fullname}")

    artistname = fullname
    artistname_cleaned = clean_artistname(artistname)
    print(f"Cleaned artistname: {artistname_cleaned}")

    songtitlefull = rapper_soup.find(
        class_='music__heading--title').get_text().strip()
    songtitlefull = unicodedata.normalize('NFKC', songtitlefull)

    search_entity = []
    search_entity.append(username)
    search_entity.append(fullname)
    # search_entity.append(artistname)
    search_entity.append(songtitlefull)
    title_excludes = get_title_excludes()
    for entity in search_entity:
        for item in title_excludes:
            if entity is not None and item in entity:
                print("The username or fullname or songtitlefull includes a word in title.exclude.json: ",
                      item,	' This profile will be excluded.')
                return "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded"

    preceding_words = ["Prod. by", "Prod. By", "prod. by", "prod by", "Prod by", "Prod By", "PROD. BY", "PROD BY",
                       "Produced by", "ProducedBy", "produced by", "beat by", "Beat By", "Beat by", "Beat By", "Prod", "prod"]
    if username in songtitlefull:
        for word in preceding_words:
            if word + username in songtitlefull or '-' + word in songtitlefull or '- ' + word in songtitlefull:
                print(
                    'The songtitlefull includes prod-related part. This profile will be excluded.')
                return "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded", "excluded"

    songtitle = songtitlefull

    songtitle = re.sub("[\{].*[\}]", "", songtitle)
    songtitle = re.sub("[\(].*[\)]", "", songtitle)
    songtitle = re.sub("[\[].*[\]]", "", songtitle)
    songtitle = re.sub("[\*].*[\*]", "", songtitle)
    songtitle = ' '.join(word for word in songtitle.split(
        ' ') if not word.startswith('#'))
    songtitle = ' '.join(word for word in songtitle.split(
        ' ') if not word.startswith('@'))
    songtitle = ' '.join(word for word in songtitle.split(
        ' ') if not word.startswith('*'))
    songtitle = ' '.join(word for word in songtitle.split(
        ' ') if not word.startswith('['))

    if songtitle.strip() == '':
        songtitle = songtitlefull
    try:
        if not songtitle[0] == '(':
            songtitle = songtitle.split('(')[0]
        if not songtitle[0] == "[":
            songtitle = songtitle.split('[')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('Feat')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('Feat.')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('feat')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('feat.')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('FEAT')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('FEAT.')[0]
    except:
        pass
    try:
        songtitle = songtitle.split(' x ')[0]
    except:
        pass
    try:
        songtitle = songtitle.split(' X ')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('ft')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('ft.')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('Ft')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('Ft.')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('FT')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('FT.')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('/')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('|')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('+')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('FREE] ')[1]
    except:
        pass
    try:
        songtitle = songtitle.split(':')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('?')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('Mixed by')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('Mixed By')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('mixed by')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('-prod')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('-prod.')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('-Prod')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('-Prod.')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('-PROD')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('-PROD.')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('_prod')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('_prod.')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('_Prod')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('_Prod.')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('_PROD.')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('Prod')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('Prod.')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('prod')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('prod.')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('PROD')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('PROD.')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('produced by')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('Produced by')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('Produced By')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('PRODUCED')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('beat by')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('Beat by')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('Beat By')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('BEAT BY')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('¨')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('feat.')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('Feat.')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('FEAT.')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('@')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('#')[0]
    except:
        pass
    try:
        songtitle = songtitle.split(',')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('featuring')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('Featuring')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('FEATURING')[0]
    except:
        pass
    try:
        songtitle = songtitle.split(' prod')[0]
    except:
        pass
    try:
        songtitle = songtitle.split(' prod.')[0]
    except:
        pass
    try:
        songtitle = songtitle.split(' pro')[0]
    except:
        pass
    try:
        songtitle = songtitle.split(' Pro')[0]
    except:
        pass
    try:
        songtitle = songtitle.split(' by')[0]
    except:
        pass
    try:
        songtitle = songtitle.split(' By')[0]
    except:
        pass
    try:
        songtitle = songtitle.split('*')[0]
    except:
        pass
    try:
        if songtitle[0] == '@':
            songtitle = ' '.join(songtitle.split()[1:])
    except:
        pass
    try:
        if songtitle[0] == '#':
            songtitle = ' '.join(songtitle.split()[1:])
    except:
        pass
    try:
        songtitle = songtitle.replace('"', '')
        songtitle = songtitle.replace("'", "")
    except:
        pass
    src_str = re.compile("freestyle", re.IGNORECASE)
    songtitle = src_str.sub('', songtitle)

    songtitle = clean_songtitle(songtitle)
    print('cleaned songtitle ', songtitle)

    songlinks = rapper_soup.find_all(class_='music-detail__link')

    songlink = ''
    for link in songlinks:
        if 'album' in link.attrs['href']:
            continue
        songlink = link.attrs['href']

    if 'album' in songlink:
        print("album found")

    bio_text = rapper_soup.get_text()

    phonematch = re.search(PHONE_NO_PATTERN, bio_text)

    phoneno1 = ''

    if phonematch != None:
        print(f'Fullmatch: {phonematch.group(1)}')
        phoneno1 = phonematch.group(1)

    phoneno2 = ''
    followers = None

    try:
        user_stats = rapper_soup.select_one('ul[class*="ArtistHeader-module__stats"]').find_all('li')
        for stat in user_stats:
            text = stat.get_text()
            if 'Followers' in text:
                followers = stat
                break
        followers = followers.get_text().replace('Followers', '').strip()
        followers = text_to_num(followers)
    except:
        followers = 0
        pass

    popularity = 'unknown'
    if followers >= 10000:
        popularity = 'trending'
    if followers >= 50000:
        popularity = 'hot'
    if followers >= 100000:
        popularity = 'popular'
    if followers >= 250000:
        popularity = 'famous'
    if followers >= 500000:
        popularity = 'infamous'

    artistnamecleaned = clean_artistname(artistname)
    location = ''
    country = ''

    location_search_url = 'https://audiomack.com/search?q=' + \
        urllib.parse.quote(fullname)
    html = BeautifulSoup(requests.get(location_search_url).text, 'html.parser')
    try:
        user = html.find(class_='user-detail')
        location_candidates = user.find_all(class_='u-trunc')
        for location_candidate in location_candidates:
            try:
                p = location_candidate.find('p')
                strong = p.find('strong')
                if 'Hometown' in strong:
                    location = p.find(text=True, recursive=False)
            except:
                pass
    except:
        print("No user retrieved. Location remains blank.")
        pass

    return username, fullname, artistname, artistnamecleaned, location, country, songtitle, songtitlefull, followers, popularity, songlink, phoneno1, phoneno2


def text_to_num(text, bad_data_val=0):
    d = {
        'K': 1000,
        'M': 1000000,
        'B': 1000000000
    }
    if not isinstance(text, str):
        # Non-strings are bad are missing data in poster's submission
        return bad_data_val

    elif text[-1] in d:
        # separate out the K, M, or B
        num, magnitude = text[:-1], text[-1]
        return int(float(num) * d[magnitude])
    else:
        return float(text)


def am_close_ad(driver):

    try:
        ad = driver.find_element_by_class_name('fs-close-button')
        ad.click()
        print("Ad closed.")
    except:
        print("No Ad found.")
        pass

    return driver
