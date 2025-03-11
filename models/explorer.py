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

from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from mock_data.weapons import weapons_list
from mock_data.armor import armor_list
from mock_data.players import players_list
from mock_data.monsters import monsters_list

from database.connections import lookup_player_by_username, lookup_player_by_name
from database.connections import save_player
from typing import Annotated

from models.monsters import Monster
from models.players import Player
from models.weapons import Weapon
from models.armor import Armor
from pathlib import Path
from os.path import join

import logging
# Set up logging.
logger = logging.getLogger("main")

# Get the parent directory to set up the Jinja2 templates.
top = Path(__file__).resolve().parent
# Extra double dots ".." to escape /explorer prefix on the router.
templates = Jinja2Templates(directory=join(f"{top}", "..", "templates"))

# Define the Object Explorer API router.
router = APIRouter(prefix = "/explorer")

@router.get("/", response_class=HTMLResponse)
async def explorer_home(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(request=request, name="explorer_home.html")



################################
# Player Methods
################################
@router.get("/player/by_username/{username}", response_class=HTMLResponse)
async def get_player_by_username(username: str, request: Request) -> HTMLResponse:
    """
    Legend of the Sonzo Dragon Explorer: Get player information by username.

    :param username:\n
    :param request:\n
    :return:\n
    """
    logger.info(f"Looking up player '{username}' in the database.")
    player = await lookup_player_by_username(username)
    if player:
        if player.username == username:
            return templates.TemplateResponse(request=request, name="lookup_player.html", context={"player": player})

    return HTMLResponse(status_code=404, content="Player not found.")


@router.get("/player/by_name/{name}", response_class=HTMLResponse)
async def get_player_by_name(name: str, request: Request) -> HTMLResponse:
    """
    Legend of the Sonzo Dragon Explorer: Get player information by name.

    :param name:\n
    :param request:\n
    :return:\n
    """

    player = await lookup_player_by_name(name)
    if player:
        if player.name == name:
            return templates.TemplateResponse(request=request, name="lookup_player.html", context={"player": player})

    return HTMLResponse(status_code=404, content="Player not found.")


@router.post("/player/by_name/{name}", response_class=HTMLResponse)
async def update_player_by_name(request: Request, name: str, data: Annotated[Player, Form()]) -> HTMLResponse:
    """
    Legend of the Sonzo Dragon Explorer: Update player information by name.

    :param name:\n
    :param request:\n
    :param data:\n
    :return:\n
    """
    for player in players_list:
        player = await lookup_player_by_name(name)
        if player:
            if player.name == name:
                player.username = data.username
                player.password = data.password
                player.name = data.name
                player.level = data.level
                player.health = data.health
                player.exp = data.exp
                player.weapon = data.weapon
                player.armor = data.armor
                player.gold = data.gold
                player.bank = data.bank
                player.description = data.description

                await save_player(player)

            return templates.TemplateResponse(request=request, name="lookup_player.html", context={"player": player})

    return HTMLResponse(status_code=200, content="None")

@router.post("/player/{name}/edit", response_class=HTMLResponse)
async def edit_player_by_name(name: str, request: Request) -> HTMLResponse:
    """
    Legend of the Sonzo Dragon Explorer: Edit player information by name.

    :param name:\n
    :param request:\n
    :return:\n
    """
    player = await lookup_player_by_name(name)
    if player:
        if player.name == name:
            return templates.TemplateResponse(request=request, name="edit_player.html", context={"player": player})

    return HTMLResponse(status_code=404, content="Player not found.")

###########################################
# Monster Methods
###########################################
@router.get("/monster/{name}", response_class=HTMLResponse)
async def get_monster_by_name(name: str, request: Request) -> HTMLResponse:
    """
    Legend of the Sonzo Dragon Explorer: Get monster information by name.

    :param name:\n
    :param request:\n
    :return:\n
    """
    for monster in monsters_list:
        if monster.name == name:
            return templates.TemplateResponse(request=request, name="lookup_monster.html", context={"monster": monster})

    return HTMLResponse(status_code=404, content="Monster not found.")

@router.post("/monster/{name}/edit", response_class=HTMLResponse)
async def edit_monster_by_name(name: str, request: Request) -> HTMLResponse:
    """
    Legend of the Sonzo Dragon Explorer: Edit monster information by name.

    :param name:\n
    :param request:\n
    :return:\n
    """
    for monster in monsters_list:
        if monster.name == name:
            return templates.TemplateResponse(request=request, name="edit_monster.html", context={"monster": monster})

    return HTMLResponse(status_code=404, content="Monster not found.")




@router.post("/monster/{name}", response_class=HTMLResponse)
async def update_monster_by_name(request: Request, name: str, data: Annotated[Monster, Form()]) -> HTMLResponse:
    """
    Legend of the Sonzo Dragon Explorer: Update monster information by name.

    :param name:\n
    :param request:\n
    :param data:\n
    :return:\n
    """
    for monster in monsters_list:
        if monster.name == name:
            monster.name = data.name
            monster.level = data.level
            monster.health = data.health
            monster.exp = data.exp
            monster.weapon = data.weapon
            monster.armor = data.armor
            monster.description = data.description

            return templates.TemplateResponse(request=request, name="lookup_monster.html", context={"monster": monster})

    return HTMLResponse(status_code=200, content="None")

################################
# Weapon Methods
################################
@router.get("/weapon/{name}", response_class=HTMLResponse)
async def get_weapon_by_name(name: str, request: Request) -> HTMLResponse:
    """
    Legend of the Sonzo Dragon Explorer: Get weapon information by name.

    :param name:\n
    :param request:\n
    :return:\n
    """
    for weapon in weapons_list:
        if weapon.name == name:
            return templates.TemplateResponse(request=request, name="lookup_weapon.html", context={"weapon": weapon})

    return HTMLResponse(status_code=404, content="Weapon not found.")

@router.post("/weapon/{name}/edit", response_class=HTMLResponse)
async def edit_weapon_by_name(name: str, request: Request) -> HTMLResponse:
    """
    Legend of the Sonzo Dragon Explorer: Edit weapon information by name.

    :param name:\n
    :param request:\n
    :return:\n
    """
    for weapon in weapons_list:
        if weapon.name == name:
            return templates.TemplateResponse(request=request, name="edit_weapon.html", context={"weapon": weapon})

    return HTMLResponse(status_code=404, content="Weapon not found.")


@router.post("/weapon/{name}", response_class=HTMLResponse)
async def update_weapon_by_name(request: Request, name: str, data: Annotated[Weapon, Form()]) -> HTMLResponse:
    """
    Legend of the Sonzo Dragon Explorer: Update weapon information by name.

    :param name:\n
    :param request:\n
    :param data:\n
    :return:\n
    """
    for weapon in weapons_list:
        if weapon.name == name:
            weapon.name = data.name
            weapon.min_damage = data.min_damage
            weapon.max_damage = data.max_damage
            weapon.buy_value = data.buy_value
            weapon.sell_value = data.sell_value
            weapon.monster_only = data.monster_only
            weapon.description = data.description

            return templates.TemplateResponse(request=request, name="lookup_weapon.html", context={"weapon": weapon})

    return HTMLResponse(status_code=200, content="None")

################################
# Armor Methods
################################
@router.get("/armor/{name}", response_class=HTMLResponse)
async def get_armor_by_name(name: str, request: Request) -> HTMLResponse:
    """
    Legend of the Sonzo Dragon Explorer: Get armor information by name.

    :param name:\n
    :param request:\n
    :return:\n
    """
    for armor in armor_list:
        if armor.name == name:
            return templates.TemplateResponse(request=request, name="lookup_armor.html", context={"armor": armor})

    return HTMLResponse(status_code=404, content="Armor not found.")

@router.post("/armor/{name}/edit", response_class=HTMLResponse)
async def edit_armor_by_name(name: str, request: Request) -> HTMLResponse:
    """
    Legend of the Sonzo Dragon Explorer: Edit armor information by name.

    :param name:\n
    :param request:\n
    :return:\n
    """
    for armor in armor_list:
        if armor.name == name:
            return templates.TemplateResponse(request=request, name="edit_armor.html", context={"armor": armor})

    return HTMLResponse(status_code=404, content="Armor not found.")


@router.post("/armor/{name}", response_class=HTMLResponse)
async def update_armor_by_name(request: Request, name: str, data: Annotated[Armor, Form()]) -> HTMLResponse:
    """
    Legend of the Sonzo Dragon Explorer: Update armor information by name.

    :param name:\n
    :param request:\n
    :param data:\n
    :return:\n
    """
    for armor in armor_list:
        if armor.name == name:
            armor.name = data.name
            armor.damage_buffer = data.damage_buffer
            armor.buy_value = data.buy_value
            armor.sell_value = data.sell_value
            armor.monster_only = data.monster_only
            armor.description = data.description

            return templates.TemplateResponse(request=request, name="lookup_armor.html", context={"armor": armor})

    return HTMLResponse(status_code=200, content="None")