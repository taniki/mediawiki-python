# -*- coding: utf-8 -*-
from wekeypedia.wikipedia.api import api as API

class WikipediaUser:
  """ create a new wikipedia user object

  Keyword Arguments
  -----------------
  name : string
  lang : string

  Example
  -------
  >>> from wekeypedia.wikipedia_user import WikipediaUser as User
  >>>
  >>> u = User(name="taniki")
  """

  def __init__(self, lang="en", name=None):
    self.lang = lang
    self.name = name


  def fetch_contribs(self):
    """ get all contributions from a user """
    api = API(lang=self.lang)

    contribs = []

    params = {
      "action":"query",
      "format": "json",
      "list":"usercontribs",
      "ucuser": self.name,
      "uclimit": "500",
      "continue": ""
    }

    while True:
      r = api.get(params)
      contribs += r["query"]["usercontribs"]

      if "continue" in r:
#        print r["continue"]
        params.update(r["continue"])
      else:
        break

    return contribs

 
  def fetch_contribs_full(self):
    """ get all contributions from a user """
    api = API(lang=self.lang)

    contribs = []

    params = {
      "action":"query",
      "format": "json",
      "list":"allrevisions",
      "arvuser": self.name,
      "arvlimit": "50",
      "arvprop": "user|userid|timestamp|size|ids|sha1|comment",
      "arvdiffto": "prev",
      "continue": ""
    }

    while True:
      r = api.get(params)
      contribs += r["query"]["allrevisions"]

      if "continue" in r:
#        print r["continue"]
        params.update(r["continue"])
      else:
        break

    return contribs
