import requests
import http

class Website:
  all = []
  def __init__(self, url):
    self.url = url
    self.status = 0
    Website.all.append(self)

  def check(self):
    try:
        r = requests.get(self.url)
        self.status = r.status_code
        self.message = http.client.responses[self.status]
        self.color = "green" if self.status == 200 else "red"
    except Exception:
        self.status = "ERR"
        self.message = "Not a valid URL"
        self.color = "red"

  @staticmethod
  def check_all():
    for website in Website.all:
      website.check()

    