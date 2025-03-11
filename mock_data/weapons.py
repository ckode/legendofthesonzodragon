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

from models.weapons import Weapon

# id: Optional[int] = Field(primary_key=True, index=True)
# name: str
# weight: int
# min_damage: int
# max_damage: int
# description: str
# buy_value: int
# sell_value: int
# monster_only: bool = Field(default=False)

weapons_list = [
    Weapon(weight=5, min_damage=0, max_damage=3, buy_value=0, sell_value=0, monster_only=False,
           name="small club",
           description="This is a small rough-hewn tree limb to function as a club."),

    Weapon(weight=5, min_damage=0, max_damage=3, buy_value=0, sell_value=0, monster_only=False,
           name="small dagger",
           description="This is a small utility dagger that can be used for self-defense if required."),

    Weapon(weight=10, min_damage=1, max_damage=4, buy_value=10, sell_value=5, monster_only=False,
           name="rapier",
           description="This rapier is primarily a thrust weapon with a vary sharp point."),

    Weapon(weight=12, min_damage=1, max_damage=5, buy_value=12, sell_value=6, monster_only=False,
           name="cutlass",
           description="This cutlass is short sabre style slashing sword with a slight upward curved blade with "
                       "a basket shared guard."),
    Weapon(weight=15, min_damage=3, max_damage=8, buy_value=20, sell_value=10, monster_only=False,
           name="Norse field axe",
           description="A teak wood shaft attaches to the tempered carbon steel axe head through "
                       "a single socket. The haft has a wrapped leather grip. This axe features a "
                       "slightly flared, bearded axe blade.")
]