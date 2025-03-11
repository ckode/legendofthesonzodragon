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

from typing import Optional
from sqlmodel import SQLModel, Field
from models.weapons import Weapon
from models.armor import Armor


class Monster(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True, index=True)
    name: str = Field(index=True)
    level: int
    health: int
    exp: int
    weapon: int = Field(default=None, foreign_key="weapon.id")
    armor: int = Field(default=None, foreign_key="armor.id")
    description: str


