# -*- coding: utf-8 -*-

import re
import os

from worker import store_revisions, dataset_blocks, dataset_timeline
from pymongo import MongoClient


mongodb_host = os.environ['MONGODB_PORT_27017_TCP_ADDR']

client = MongoClient("mongodb://%s/" % (mongodb_host))
db = client["datasets"]


def build_revisions():
  for page_url in open("/data/sources/wicrimea-seeds.extended.txt", "r"):
    print page_url.strip()
    store_revisions.delay(page_url.strip())

# regex = re.compile("|$([a-z]*)/(!/*)/revision/([0-9]*)$|")

def build_blocks():
  all_revisions = db.datasets.find({ "url": {"$regex": "^([a-z]*)\/(.*)\/revision\/([0-9]*)$" }})

  for revision in all_revisions:
    key =  "%s/blocks" % ( revision["url"] )

    test = db.datasets.find_one({ "url" : key })

    print revision["url"].encode("utf8")

    if test is None:
      print "... computing!"  

      #print revision["dataset"][0]["*"]
      dataset_blocks.delay(revision["url"])

def build_timelines():
  for page_url in open("/data/sources/wicrimea-seeds.extended.txt", "r"):
    dataset_timeline.delay(page_url.strip())

build_timelines()