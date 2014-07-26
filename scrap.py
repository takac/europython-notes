import urllib3
from bs4 import BeautifulSoup

http = urllib3.PoolManager()

baseurl = "http://ep2014.europython.eu"
sched = "/en/schedule/sessions/14/"

def talk_from_path(url):
    resp = http.request('GET', baseurl + url)
    return TalkPageParser(resp.data)

# soup = BeautifulSoup(resp.data)

# Doesn't work for kwargs
def memprop(func):
    cache = {}
    def f(*args, **kwargs):
        if args not in cache:
            cache[args] = func(*args, **kwargs)
        return cache[args]
    return property(f)

# class AuthorPageParser(object):
#     def __init__(self, content):
#         self.soup = BeautifulSoup(content)


class TalkPageParser(object):
    def __init__(self, content):
        self.soup = BeautifulSoup(content)

    @memprop
    def details(self):
        return self.soup.find('div', {'id': 'details'})

    @memprop
    def speakers(self):
        return [ self._parse_speaker(i)
                for i in self.soup.findAll('div', {'class': 'speaker-box'})]

    def _parse_speaker(self, speakerSoup):
        return {
                'img': speakerSoup.find('img').get('src'),
                'name': speakerSoup.find('span').text,
                'acc': speakerSoup.find('a').get('href'),
               }
    @memprop
    def youtube(self):
        return self.soup.find('iframe').get('src').split('/embed/')[1].split('?')[0]

    @memprop
    def title(self):
        return self.soup.find('h1', {'id': 'site-title'}).text

    @memprop
    def abstract(self):
        return self.details.find('div', {'class': 'abstract'}).text.strip()

    @memprop
    def when(self):
        return self.details.findAll('dd')[2].text.strip()

    @memprop
    def where(self):
        return self.details.findAll('dd')[1].text.strip()

    @memprop
    def speakerdeck(self):
        return self.soup.find('script', {'class': 'speakerdeck-embed'})

talk = TalkPageParser(open('speakerdump.txt', 'r').read())

props = [ i for i in dir(talk) if not i.startswith('_') ]
props.remove('details')
props.remove('soup')
for i in props:
    print('{0}: {1}'.format(i, getattr(talk, i)))
