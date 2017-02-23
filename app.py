import os
import os.path
import cherrypy
from helpers import rds
import json
from jinja2 import Environment, PackageLoader, select_autoescape
env = Environment(
    loader=PackageLoader('helpers', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)


class Nifty50app(object):
    @cherrypy.expose
    def index(self):
        card_content = json.loads(rds.get("nif_top_ten"))
        print card_content
        template = env.get_template('index.html')
        return template.render(content=card_content)


if __name__ == '__main__':
    conf = {
        '/': {
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
    cherrypy.quickstart(Nifty50app(), '/', conf)

# import urllib2
# from bs4 import BeautifulSoup
# data = urllib2.urlopen('https://www.nseindia.com/live_market/dynaContent/live_analysis/gainers/niftyGainers1.json').read()
# soup = BeautifulSoup(urllib2.urlopen('http://www.nseindia.com/live_market/dynaContent/live_analysis/top_gainers_losers.htm?cat=G').read())
# for tr in soup.find_all('tr')[2:]:
