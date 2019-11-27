import logging

import json
import requests

from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


class AbstractIndustry(object):
    def __init__(self,title,children):
        logger.info("Creating industry {}".format(title))
        self.title = title
        self.children = children
    @property
    def level(self):
        raise NotImplementedError("Abstract industry doesn´t contains level.")

    def add_child(self,child):
        self.children.append(child)

    def to_dict(self):
        return {
            "title": self.title,
            "children": [
            child.to_dict() for child in self.children
            ]
        }

    def jsonify(self):
        return json.dumps(self.to_dict)

    class Division(AbstractIndustry):
        level = "SIC Division"

    class MajorGroup(AbstractIndustry):
        level = "SIC Major Group"

    class Group(AbstractIndustry):
        level = "SIC Group"

    class Single(AbstractIndustry):
        level = "SIC Industry"

    class SIC(AbstractIndustry):
        level = "Standard Industry Clasification"

    @staticmethod
    def load_json(filename):
        with open(filename, "r") as file:
            sic_industries = json.loads(file.read())
        return sic_industries

    @staticmethod
    def from_url(url):
        response =

class SIC:
    pass
