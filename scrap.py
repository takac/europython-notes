import urllib3
import functools
from bs4 import BeautifulSoup


def memoize(func):
    cache = {}
    @functools.wraps(func)
    def f(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return f


def clean_text(func):
    @functools.wraps(func)
    def f(*args, **kwargs):
        return func(*args, **kwargs).strip().encode('utf-8')
    return f


def memprop(func):
    '''Memoized property field decorator.'''
    return property(memoize(func))


http = urllib3.PoolManager()
@memoize
def get_euro_python_page(relative_url, base_url="http://ep2014.europython.eu"):
    yield http.request('GET', base_url + relative_url).data

class PageParser(object):
    def __init__(self, content_gen=None, content=None, url=None, soup=None):
        self.url = url
        self.content = content
        self._soup = soup
        self.content_gen = content_gen

    @property
    def soup(self):
        if self.content is None:
            self.content = next(self.content_gen)
        if self._soup is None:
            self._soup =  BeautifulSoup(self.content)
        return self._soup

    @classmethod
    def talk_from_url(cls, url):
        return cls(content_gen=get_euro_python_page(url), url=url)

    @classmethod
    def talk_from_file(cls, filename):
        return cls(content=open(filename, 'r'))


class AuthorPageParser(PageParser):

    @memprop
    def info(self):
        return self.soup.find('p', {'class': 'infoline'})

    @memprop
    def website(self):
        return self.info.find('i', {'class': 'fa-link'}).parent['href']

    @memprop
    def twitter(self):
        return self.info.find('i', {'class': 'fa-twitter'}).parent['href']

    @memprop
    def office(self):
        return self.info.find('i', {'class': 'fa-building-o'}).parent.text.strip()


class TalkPageParser(PageParser):

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
        return self.soup.find('h1', {'id': 'site-title'}).text.strip().encode('utf-8')

    @memprop
    @clean_text
    def abstract(self):
        return self.details.find('div', {'class': 'abstract'}).text

    @memprop
    def when(self):
        return self.details.findAll('dd')[2].text.strip().encode('utf-8')

    @memprop
    def where(self):
        return self.details.findAll('dd')[1].text.strip().encode('utf-8')

    @memprop
    def speakerdeck(self):
        return self.soup.find('script', {'class': 'speakerdeck-embed'})

sched = "/en/schedule/sessions/14/"
print "=" * 40
talk = TalkPageParser.talk_from_url(sched)
props = [ i for i in dir(talk) if not i.startswith('_') ]
props.remove('content')
props.remove('details')
props.remove('soup')
for i in props:
    print('{0}: {1}'.format(i, getattr(talk, i)))
