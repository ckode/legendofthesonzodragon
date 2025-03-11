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

from models.armor import Armor

armor_list = [
    Armor(ac=2, weight=5, damage_buffer=0, buy_value=0, sell_value=0, monster_only=False,
          name="cloth rags",
          description="These are cloth rags stitched together as general body coverings and provide very"
                      "little protection."),
    Armor(ac=5, weight=10, damage_buffer=0, buy_value=30, sell_value=5, monster_only=False,
          name="leather patch armor",
          description="Similar to cloth rags, but made with dry rough scraps of leather stitched together.  "
                      "It provides but better protection from the elements and small arms."),
    Armor(ac=20, weight=15, damage_buffer=2, buy_value=100, sell_value=30, monster_only=False,
          name="leather armor",
          description="Finely crafted soft well oiled leather armor that tailored to fit perfectly and therefore "
                      "is far more comfortable to wear and move in while providing improved protection."),
    Armor(ac=25, weight=50, damage_buffer=5, buy_value=150, sell_value=50, monster_only=False,
          name="basic chainmail armor",
          description="This chainmail armor is designed to provide better protection than leather against edged "
                      "and blunt weapons alike.  Its added protection comes at a price.  It's heavier and makes "
                      "more noise when the chain links clink together hampering stealthy movements."),
    Armor(ac=25, weight= 70, damage_buffer=8, buy_value=500, sell_value=250, monster_only=False,
          name="Dragon Scale Armor",
          description="Extremely rare, Grand Dragon Scale armor glistens in the sunshine and draws "
                      "attention like an ass-clown in church.  It is quite a bit heavier than plate mail, "
                      "but provides better protection at the cost of it's heavier weight.")
]