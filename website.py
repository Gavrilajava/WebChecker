import requests
import grequests
import asyncio
import http

class Website:
  all = []
  def __init__(self, url):
    self.url = url
    self.status = 0
    Website.all.append(self)

  async def check(self):
    try:
        r = await requests.get(self.url)
        self.status = r.status_code
        self.message = http.client.responses[self.status]
        self.color = "green" if self.status == 200 else "red"
    except Exception:
        self.status = "ERR"
        self.message = "Not a valid URL"
        self.color = "red"

  @staticmethod
  async def check_all():
    # loop = asyncio.get_event_loop()
    # for website in Website.all:
    #   loop.create_task(website.check())
    #   # asyncio.create_task(website.check())
    # try:
    # # run_forever() returns after calling loop.stop()
    #     loop.run_forever()
    #     tasks = Task.all_tasks()
    #     for t in [t for t in tasks if not (t.done() or t.cancelled())]:
    #         # give canceled tasks the last chance to run
    #         loop.run_until_complete(t)
    # finally:
    #     loop.close()
    # return await "done"
    reqs = (grequests.get(website.url) for website in Website.all)
    resp = grequests.imap(reqs, grequests.Pool(10))

    for r in resp:
        result = r
    



    