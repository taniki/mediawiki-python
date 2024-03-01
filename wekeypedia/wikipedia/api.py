# -*- coding: utf-8 -*-
import requests

class api:
  """
  Parameters
  ----------
  lang : string, optional
  """

  def __init__(self, lang="en"):
    self.lang = lang
    self.url = "http://%s.wikipedia.org/w/api.php" % (self.lang)

  def get(self, query, method="get"):
    """
    Parameters
    ----------
    query : dict

    Returns
    -------
    result : dict
    """

    if method == "get":
      r = requests.get(self.url, params=query)
    elif method == "post":
      r = requests.post(self.url, data=query)

    try:
      result = r.json()
    except ValueError:
      print(self.url)
      print(query)

      result = r

    return result

  def post(self, query):
    return self.get(query, method="post")
