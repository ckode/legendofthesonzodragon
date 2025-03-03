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

from models.players import Player

players_list = [
    Player(username='Frag', password='password1', name='Mock_Dave',
           level=1, health=100, exp=0, armor=1, weapon=1, gold=10, bank=100,
           description='A friendly and mischievous slaughter machine.'),
    Player(username='Omegus', password='password1', name='Mock_Mark',
           level=1, health=100, exp=0, armor=1, weapon=1, gold=10, bank=100,
           description="A flippant dilrod who is always searching for a victim."),
    Player(username='AbsoluteZero', password='password1', name='Mock_Mike',
           level=1, health=100, exp=0, armor=1, weapon=1, gold=10, bank=100,
           description="A humble (not) and helpful Orc who always screams, \"Who wants to do some shootin'?\""),
    Player(username = 'Idyil', password = 'password1', name = 'Mock_Rick',
           level = 1, health = 100, exp = 0, armor = 1, weapon = 1, gold = 10, bank = 100,
           description = 'The old wise man who is helpful and friendly to noone.'),
]

