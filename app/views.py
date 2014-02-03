import jinja2
import os
import webapp2

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')
jinja_environment = \
  jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR))

class BaseHandler(webapp2.RequestHandler):

  @webapp2.cached_property
  def jinja2(self):
      return jinja2.get_jinja2(app=self.app)

  def render_template(
    self,
    filename,
    template_values,
    **template_args
    ):

    try:
      template = jinja_environment.get_template(filename)
      self.response.out.write(template.render(template_values))
    except jinja2.TemplateNotFound:
      self.response.out.write('404')

class Home(BaseHandler):
  def get(self):
    self.render_template('index.html', '')

class SubPage(BaseHandler):
  def get(self, page):
    self.render_template(page + '.html', '')

class DemoHome(BaseHandler):
  def get(self):
    self.render_template('demo/index.html', '')

class DemoSub(BaseHandler):
  def get(self, page):
    self.render_template('demo/' + page + '.html', '')

class TutorialHome(BaseHandler):
  def get(self):
    self.render_template('tutorial/index.html', '')

class TutorialSub(BaseHandler):
  def get(self, page):
    self.render_template('tutorial/' + page + '.html', '')