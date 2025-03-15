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

from os.path import exists
import logging

from sqlmodel import SQLModel, select, create_engine, Session, func

from models.weapons import Weapon
from models.armor import Armor
from models.players import Player
from models.monsters import Monster

from mock_data.weapons import weapons_list
from mock_data.armor import armor_list
from mock_data.players import players_list
from mock_data.monsters import monsters_list

from typing import List


def verify_game_data() -> None:
    """
    Verify the database contains the game data.
    
    :return: 
    """
    logger.info("Verifying game data in the database...")
    with Session(engine) as session:
        weapon_statement = select(Weapon)
        armor_statement = select(Armor)
        player_statement = select(Player)
        monster_statement = select(Monster)
        weapon_result = session.exec(weapon_statement)
        armor_result = session.exec(armor_statement)
        player_result = session.exec(player_statement)
        monster_result = session.exec(monster_statement)

        w_count = len(weapon_result.all())
        a_count = len(armor_result.all())
        p_count = len(player_result.all())
        m_count = len(monster_result.all())

        if w_count == 0:
            logger.info("Injecting game weapons to the database.")
            session.add_all(weapons_list)
        if a_count == 0:
            logger.info("Injecting game armor in the database.")
            session.add_all(armor_list)
        if p_count == 0:
            logger.info("Injecting mock players in the database.")
            session.add_all(players_list)
        if m_count == 0:
            logger.info("Injecting game monsters in the database.")
            session.add_all(monsters_list)

        session.commit()


async def get_all_players() -> List[Player]:
    """
    Retrieve a player from the database by their name.

    :param name: The name of the player.
    :return: The player object if found, None otherwise.
    """
    with Session(engine) as session:
        statement = select(Player)
        result = session.exec(statement)
        players = result.all()

    return players


async def lookup_player_by_username(name: str):
    """
    Retrieve a player from the database by their username.

    :param name: The username of the player.
    :return: The player object if found, None otherwise.
    """
    with Session(engine) as session:
        statement = select(Player).where(func.lower(Player.username) == name.lower())
        result = session.exec(statement)
        player = result.first()

    return player


async def lookup_player_by_name(name: str):
    """
    Retrieve a player from the database by their name.

    :param name: The name of the player.
    :return: The player object if found, None otherwise.
    """
    with Session(engine) as session:
        statement = select(Player).where(func.lower(Player.name) == name.lower())
        result = session.exec(statement)
        player = result.first()

    return player


async def lookup_monster_by_name(name: str):
    """
    Retrieve a monster from the database by their name.

    :param name: The name of the monster.
    :return: The monster object if found, None otherwise.
    """
    with Session(engine) as session:
        statement = select(Monster).where(func.lower(Monster.name) == name.lower())
        result = session.exec(statement)
        monster = result.first()

    return monster


async def lookup_armor_by_name(name: str):
    """
    Retrieve a armor from the database by it's name.

    :param name: The name of the armor.
    :return: The armor object if found, None otherwise.
    """
    with Session(engine) as session:
        statement = select(Armor).where(func.lower(Armor.name) == name.lower())
        result = session.exec(statement)
        armor = result.first()

    return armor


async def lookup_weapon_by_name(name: str):
    """
    Retrieve a weapon from the database by it's name.

    :param name: The name of the weapon.
    :return: The weapon object if found, None otherwise.
    """
    with Session(engine) as session:
        statement = select(Weapon).where(func.lower(Weapon.name) == name.lower())
        result = session.exec(statement)
        weapon = result.first()

    return weapon

################################################################
# Save Objects to Database
################################################################

async def save_player(updated_player: Player) -> None:
    """
    Save a player to the database.

    :param player: The player object to save.
    :return:
    """
    with Session(engine) as session:
        statement = select(Player).where(Player.id == updated_player.id)
        result = session.exec(statement)
        player = result.one()

        player.sqlmodel_update(updated_player)
        session.add(player)
        session.commit()


async def save_monster(updated_monster: Monster) -> None:
    """
    Save a monster to the database.

    :param monster: The monster object to save.
    :return:
    """
    with Session(engine) as session:
        statement = select(Monster).where(Monster.id == updated_monster.id)
        result = session.exec(statement)
        monster = result.one()

        monster.sqlmodel_update(updated_monster)
        session.add(monster)
        session.commit()


async def save_armor(updated_armor: Armor) -> None:
    """
    Save an armor to the database.

    :param armor: The armor object to save.
    :return:
    """
    with Session(engine) as session:
        logger.info(f"Looking up armor by id: {updated_armor.id} in {Armor.id}")
        statement = select(Armor).where(Armor.id == updated_armor.id)
        result = session.exec(statement)
        armor = result.one()

        armor.sqlmodel_update(updated_armor)
        session.add(armor)
        session.commit()


async def save_weapon(updated_weapon: Weapon) -> None:
    """
    Save an weapon to the database.

    :param weapon: The weapon object to save.
    :return:
    """
    with Session(engine) as session:
        statement = select(Weapon).where(Weapon.id == updated_weapon.id)
        result = session.exec(statement)
        weapon = result.one()

        weapon.sqlmodel_update(updated_weapon)
        session.add(weapon)
        session.commit()

################################################################
# Initialize Game Database
################################################################
logger = logging.getLogger("database")
engine = create_engine("sqlite:///game_database.db", echo=False)
SQLModel.metadata.create_all(bind=engine)
verify_game_data()