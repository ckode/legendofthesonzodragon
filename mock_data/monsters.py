"""
The Legend of the Sonzo Dragon

Copyright [2025] David C. Brown

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from models.monsters import Monster


monsters_list = [
        Monster(id=1, name="Goblin", level=3, health=10, exp=10, weapon=1, armor=1, description="A small, pointed eared creature with a piercing bite.",
                image_url="../../../static/images/items/monster_goblin.png"),
        Monster(id=2, name="Minotaur", level=15, health=110, exp=200, weapon=1, armor=1, description="A massive, half-horse, half-human creature with large horns.",
                image_url="../../../static/images/items/monster_minotaur.png"),
        Monster(id=3, name="Orc", level=10, health=25, exp=25, weapon=1, armor=1, description="A dumb, yet extremely aggressive creature that reeks of death.",
                image_url="../../../static/images/items/monster_orc.png"),
        Monster(id=4, name="Rat", level=1, health=2, exp=2, weapon=1, armor=1, description="A small, nocturnal creature with a propensity to steal your food at night.",
                image_url="../../../static/images/items/monster_rat.png"),
        Monster(id=5, name="Sonzo She-Dragon", level=50, health=1000, exp=2000, weapon=1, armor=1,
                description="A majestic, silver-white dragon with a pair of wings that shimmer like jewels.",
                image_url="../../../static/images/items/monster_sonzo_she-dragon.png"),
]