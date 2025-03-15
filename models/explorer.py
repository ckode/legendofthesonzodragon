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

from fastapi import APIRouter, Request, Form, Query
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from mock_data.weapons import weapons_list
from mock_data.armor import armor_list
from mock_data.players import players_list
from mock_data.monsters import monsters_list

from database.connections import lookup_player_by_username, lookup_player_by_name, get_all_players
from database.connections import lookup_monster_by_name, lookup_armor_by_name, lookup_weapon_by_name
from database.connections import save_player, save_monster, save_armor, save_weapon
from typing import Annotated

from models.monsters import Monster
from models.players import Player
from models.weapons import Weapon
from models.armor import Armor
from pathlib import Path
from os.path import join
import json

import logging
# Set up logging.
logger = logging.getLogger("explorer")

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
@router.get("/search/player/", response_class=HTMLResponse)
async def get_player_by_name(request: Request) -> HTMLResponse:
    """
    Legend of the Sonzo Dragon Explorer: Get player information by name.

    :param request:\n
    :return:\n
    """
    return templates.TemplateResponse(request=request, name="player_search.html")


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


# @router.get("/player/by_name/{name}", response_class=HTMLResponse)
# async def get_player_by_name(name: str, request: Request) -> HTMLResponse:
#     """
#     Legend of the Sonzo Dragon Explorer: Get player information by name.
#
#     :param name:\n
#     :param request:\n
#     :return:\n
#     """
#
#     player = await lookup_player_by_name(name)
#     if player:
#         if player.name == name:
#             return templates.TemplateResponse(request=request, name="lookup_player.html", context={"player": player})
#
#     return HTMLResponse(status_code=404, content="Player not found.")

@router.get("/player/by_name/", response_class=HTMLResponse)
async def get_player_by_name(request: Request, name: Annotated[str | None, Query(max_length=25)] = None) -> HTMLResponse:
    """
    Legend of the Sonzo Dragon Explorer: Get player information by name.

    :param name:\n
    :param request:\n
    :return:\n
    """
    player = None

    if name:
        player = await lookup_player_by_name(name)

    if player:
        return templates.TemplateResponse(request=request, name="lookup_player.html", context={"player": player})
    else:
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
    player = await lookup_player_by_name(name)
    if player:
        if player.name == name:
            await save_player(data)

            # Send "data" back instead of the "player" since data is already updated and async player isn't.
            return templates.TemplateResponse(request=request, name="lookup_player.html", context={"player": data})

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
@router.get("/search/monster/", response_class=HTMLResponse)
async def get_monster_by_name(request: Request) -> HTMLResponse:
    """
    Legend of the Sonzo Dragon Explorer: Search for Monster information by name.

    :param request:\n
    :return:\n
    """
    return templates.TemplateResponse(request=request, name="monster_search.html")

@router.get("/monster/by_name/", response_class=HTMLResponse)
async def get_player_by_name(request: Request, name: Annotated[str | None, Query(max_length=25)] = None) -> HTMLResponse:
    """
    Legend of the Sonzo Dragon Explorer: Get monster information by name.

    :param name:\n
    :param request:\n
    :return:\n
    """
    monster = None

    if name:
        monster = await lookup_monster_by_name(name)

    if monster:
        return templates.TemplateResponse(request=request, name="lookup_monster.html", context={"monster": monster})
    else:
        return HTMLResponse(status_code=404, content="Monster not found.")


@router.get("/monster/{name}", response_class=HTMLResponse)
async def get_monster_by_name(name: str, request: Request) -> HTMLResponse:
    """
    Legend of the Sonzo Dragon Explorer: Get monster information by name.

    :param name:\n
    :param request:\n
    :return:\n
    """
    monster = await lookup_monster_by_name(name)
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
    monster = await lookup_monster_by_name(name)
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
    monster = await lookup_monster_by_name(name)
    if monster.name == name:
        await save_monster(data)

        # Send "data" back instead of the "monster" since data is already updated and (async) player isn't.
        return templates.TemplateResponse(request=request, name="lookup_monster.html", context={"monster": data})

    return HTMLResponse(status_code=200, content="None")

################################
# Weapon Methods
################################
@router.get("/search/weapon/", response_class=HTMLResponse)
async def get_weapon_by_name(request: Request) -> HTMLResponse:
    """
    Legend of the Sonzo Dragon Explorer: Search for Weapon information by name.

    :param request:\n
    :return:\n
    """
    return templates.TemplateResponse(request=request, name="weapon_search.html")

@router.get("/weapon/by_name/", response_class=HTMLResponse)
async def get_weapon_by_name(request: Request, name: Annotated[str | None, Query(max_length=25)] = None) -> HTMLResponse:
    """
    Legend of the Sonzo Dragon Explorer: Get weapon information by name.

    :param name:\n
    :param request:\n
    :return:\n
    """
    weapon = None

    if name:
        weapon = await lookup_weapon_by_name(name)

    if weapon:
        return templates.TemplateResponse(request=request, name="lookup_weapon.html", context={"weapon": weapon})
    else:
        return HTMLResponse(status_code=404, content="Weapon not found.")


@router.get("/weapon/{name}", response_class=HTMLResponse)
async def get_weapon_by_name(name: str, request: Request) -> HTMLResponse:
    """
    Legend of the Sonzo Dragon Explorer: Get weapon information by name.

    :param name:\n
    :param request:\n
    :return:\n
    """
    weapon = await lookup_weapon_by_name(name)
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
    weapon = await lookup_weapon_by_name(name)
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
    weapon = await lookup_weapon_by_name(name)
    if weapon.name == name:
        await save_weapon(data)

        # Send "data" back instead of the "weapon" since data is already updated and (async) player isn't.
        return templates.TemplateResponse(request=request, name="lookup_weapon.html", context={"weapon": data})

    return HTMLResponse(status_code=200, content="None")


################################
# Armor Methods
################################
@router.get("/search/armor/", response_class=HTMLResponse)
async def get_armor_by_name(request: Request) -> HTMLResponse:
    """
    Legend of the Sonzo Dragon Explorer: Search for Armor information by name.

    :param request:\n
    :return:\n
    """
    return templates.TemplateResponse(request=request, name="armor_search.html")

@router.get("/armor/by_name/", response_class=HTMLResponse)
async def get_armor_by_name(request: Request, name: Annotated[str | None, Query(max_length=25)] = None) -> HTMLResponse:
    """
    Legend of the Sonzo Dragon Explorer: Get armor information by name.

    :param name:\n
    :param request:\n
    :return:\n
    """
    armor = None

    if name:
        armor = await lookup_armor_by_name(name)

    if armor:
        return templates.TemplateResponse(request=request, name="lookup_armor.html", context={"armor": armor})
    else:
        return HTMLResponse(status_code=404, content="Armor not found.")


@router.get("/armor/{name}", response_class=HTMLResponse)
async def get_armor_by_name(name: str, request: Request) -> HTMLResponse:
    """
    Legend of the Sonzo Dragon Explorer: Get armor information by name.

    :param name:\n
    :param request:\n
    :return:\n
    """
    armor = await lookup_armor_by_name(name)
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
    armor = await lookup_armor_by_name(name)
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
    armor = await lookup_armor_by_name(name)
    if armor.name == name:
        await save_armor(data)

        # Send "data" back instead of the "armor" since data is already updated and (async) player isn't.'
        return templates.TemplateResponse(request=request, name="lookup_armor.html", context={"armor": data})

    return HTMLResponse(status_code=200, content="None")