import os

import image as image

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IT_team_project.settings')

import django

django.setup()
from manicurer.models import Picture, Comment


def populate():
    image = [{"name": "picture1", "owner": "Kite", "numberofrate": 6, "avgrate": 4.2,},
            {"name": "picture2", "owner": "Lucy", "numberofrate": 10, "avgrate": 3.3},
            {"name": "picture3", "owner": "Alice", "numberofrate": 0, "avgrate": 4.0},
            {"name": "picture4", "owner": "Dante", "numberofrate": 8, "avgrate": 3.1},
            {"name": "picture5", "owner": "Lily", "numberofrate": 9, "avgrate": 4.4},
             {"name": "picture7", "owner": "Lily", "numberofrate": 21, "avgrate": 4.3},
             {"name": "picture8", "owner": "Jully", "numberofrate": 16, "avgrate": 4.1},
             {"name": "picture10", "owner": "Cathy", "numberofrate": 11, "avgrate": 2.5},
             {"name": "picture11", "owner": "Lily", "numberofrate": 25, "avgrate": 4.0},
    ]

    comments = [{"User": "Sun", "Picture": "picture1", "Content": "Awesome!!!!!" },
             {"name": "Sun", "Picture": "picture6", "Content": "Awesome!!!!!"},
             {"name": "Sunny", "Picture": "picture7", "Content": "Awesome!!!!!"},
             {"name": "Sunny", "Picture": "picture8", "Content": "Awesome!!!!!"},
             {"name": "HuangHuang", "Picture": "picture4", "Content": "Awesome!!!!!"},
             {"name": "HuangHuang", "Picture": "picture5", "Content": "Awesome!!!!!"},
             {"name": "Sun", "Picture": "picture2", "Content": "Awesome!!!!!"},
             {"name": "Sunny", "Picture": "picture3", "Content": "Awesome!!!!!"},
             {"name": "HuangHuang","Picture": "picture9", "Content": "Awesome!!!!!"},
             ]




    for i in image:
        add_Picture(i["name"], i["owner"], i["numberofrate"], i["avgrate"])


def add_Picture(image, owner, numberofrate, avgrate ,):
    p = Picture.objects.get_or_create(name=image)[0]
    p.owner = owner
    p.NumberOfRates = numberofrate
    p.avgrate = avgrate
    p.save()
    return p





if __name__ == '__main__':
    print("Starting manicurer population script...")
    populate()