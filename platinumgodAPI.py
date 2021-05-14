import requests
from bs4 import BeautifulSoup

from subclasses.isaac_item import *


class platinumgod():

    def __init__(self):
        self._link = 'https://platinumgod.co.uk'
        self._soup = BeautifulSoup(requests.get(self._link).content, 'html.parser')
        self.items = self._soup.select('li.textbox')

    def find_item_by_id(self, id: str):
        i = 0
        for item in self.items:
            i += 1
            elements = item.select('p.r-itemid')
            if len(elements) > 0:
                temp = elements[0].text.split(': ')
                if temp[0].lower() == 'itemid' and temp[1] == id:
                    name = item.select('p.item-title')[0].text
                    pickup_desc = item.select('p.pickup')[0].text
                    add_ons = item.select('ul')[0].text.split('\n')
                    type = add_ons[1].split(': ')[-1]
                    if type.lower() == 'active':
                        recharge = add_ons[2].split(': ')[-1]
                        pool = add_ons[3].split(': ')[-1]
                    else:
                        recharge = None
                        pool = add_ons[2].split(': ')[-1]
                    desc = item.select('span > p:not([class])')
                    desc = "\n\n".join([line.text for line in desc])

                    try:
                        unlock = item.select('p.r-unlock')[0].text.split(': ')[-1]
                    except IndexError:
                        unlock = None

                    return Item(int(id), name, pickup_desc, desc, type, pool, recharge, unlock)

    def find_item_by_name(self, name: str):
        i = 0
        for item in self.items:
            i += 1
            elements = item.select('p.item-title')
            if len(elements) > 0:
                if name.lower() == elements[0].text.lower():
                    name = elements[0].text
                    id = item.select('p.r-itemid')[0].text
                    temp = id.split(': ')
                    id = temp[-1]
                    pickup_desc = item.select('p.pickup')[0].text
                    add_ons = item.select('ul')[0].text.split('\n')
                    type = add_ons[1].split(': ')[-1]
                    if type.lower() == 'active':
                        recharge = add_ons[2].split(': ')[-1]
                        pool = add_ons[3].split(': ')[-1]
                    else:
                        recharge = None
                        pool = add_ons[2].split(': ')[-1]
                    desc = item.select('span > p:not([class])')
                    desc = "\n\n".join([line.text for line in desc])

                    try:
                        unlock = item.select('p.r-unlock')[0].text.split(': ')[-1]
                    except IndexError:
                        unlock = None

                    return Item(int(id), name, pickup_desc, desc, type, pool, recharge, unlock)

    def find_trinket_by_id(self, id: str):
        i = 0
        for item in self.items:
            i += 1
            elements = item.select('p.r-itemid')
            if len(elements) > 0:
                temp = elements[0].text.split(': ')
                if temp[0].lower() == 'trinketid' and temp[1] == id:
                    name = item.select('p.item-title')[0].text
                    pickup_desc = item.select('p.pickup')[0].text
                    desc = item.select('span > p:not([class])')
                    desc = "\n\n".join([line.text for line in desc])

                    try:
                        unlock = item.select('p.r-unlock')[0].text.split(': ')[-1]
                    except IndexError:
                        unlock = None

                    return Trinket(int(id), name, pickup_desc, desc, unlock)

    def find_trinket_by_name(self, name: str):
        i = 0
        for item in self.items:
            i += 1
            elements = item.select('p.item-title')
            if len(elements) > 0:
                if name.lower() == elements[0].text.lower():
                    name = elements[0].text
                    id = item.select('p.r-itemid')[0].text
                    temp = id.split(': ')
                    id = temp[-1]
                    pickup_desc = item.select('p.pickup')[0].text
                    desc = item.select('span > p:not([class])')
                    desc = "\n\n".join([line.text for line in desc])

                    try:
                        unlock = item.select('p.r-unlock')[0].text.split(': ')[-1]
                    except IndexError:
                        unlock = None

                    return Trinket(int(id), name, pickup_desc, desc, unlock)