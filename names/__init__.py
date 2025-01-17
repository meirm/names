from __future__ import unicode_literals
from os.path import abspath, join, dirname
import random


__title__ = 'names'
__version__ = '0.3.0.post1'
__author__ = 'Trey Hunner'
__license__ = 'MIT'


full_path = lambda filename: abspath(join(dirname(__file__), filename))


FILES = {
    'first:male': full_path('dist.male.first'),
    'first:female': full_path('dist.female.first'),
    'last': full_path('dist.all.last'),
}


def get_name(filename, seed=None):
    if seed is not None:
        random.seed(seed)
    selected = random.random() * 90
    with open(filename) as name_file:
        for line in name_file:
            name, _, cummulative, _ = line.split()
            if float(cummulative) > selected:
                return name
    return ""  # Return empty string if file is empty


def get_first_name(gender=None, seed=None):
    if seed is not None:
        random.seed(seed)
    if gender is None:
        gender = random.choice(('male', 'female'))
    if gender not in ('male', 'female'):
        raise ValueError("Only 'male' and 'female' are supported as gender")
    return get_name(FILES['first:%s' % gender], seed=seed).capitalize()


def get_last_name(seed=None):
    if seed is not None:
        random.seed(seed)
    return get_name(FILES['last'], seed=seed).capitalize()


def get_full_name(gender=None, seed=None):
    if seed is not None:
        random.seed(seed)
    return "{0} {1}".format(get_first_name(gender, seed), get_last_name(seed))
