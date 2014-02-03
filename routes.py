import webapp2
from app.views import *
from webapp2_extras.routes import RedirectRoute

SITE_URLS = [
    webapp2.Route('/', handler=Home),
    RedirectRoute('/demo', handler=DemoHome, name='DemoHome', strict_slash=True),
    RedirectRoute('/demo/<page>', handler=DemoSub, name='DemoSub', strict_slash=True),
    RedirectRoute('/tutorial', handler=TutorialHome, name='TutorialHome', strict_slash=True),
    RedirectRoute('/tutorial/<page>', handler=TutorialSub, name='TutorialSub', strict_slash=True),
    webapp2.Route('/<page>', handler=SubPage)
]

app = webapp2.WSGIApplication(SITE_URLS, debug=True)