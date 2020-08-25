import requests

class Website:
  all = []
  def __init__(self, url):
    self.url = url
    Website.all.append(self)

  def check(self):
    print(self.url)
    r = requests.get(self.url)
    self.status = r.status

  @staticmethod
  def check_all():
    for website in Website.all:
      website.check
    return Website.all