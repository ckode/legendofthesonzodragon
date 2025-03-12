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

from sqlmodel import SQLModel, select, create_engine, Session

from models.weapons import Weapon
from models.armor import Armor
from models.players import Player
from models.monsters import Monster

from mock_data.weapons import weapons_list
from mock_data.armor import armor_list
from mock_data.players import players_list
from mock_data.monsters import monsters_list




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


async def lookup_player_by_username(name: str):
    """
    Retrieve a player from the database by their username.

    :param name: The username of the player.
    :return: The player object if found, None otherwise.
    """
    logger.info(f"Looking up player by username: {name}")
    with Session(engine) as session:
        statement = select(Player).where(Player.username == name)
        result = session.exec(statement)
        player = result.first()

    return player


async def lookup_player_by_name(name: str):
    """
    Retrieve a player from the database by their name.

    :param name: The name of the player.
    :return: The player object if found, None otherwise.
    """
    logger.info(f"Looking up player by name: {name}")
    with Session(engine) as session:
        statement = select(Player).where(Player.name == name)
        result = session.exec(statement)
        player = result.first()

    return player


async def lookup_monster_by_name(name: str):
    """
    Retrieve a monster from the database by their name.

    :param name: The name of the monster.
    :return: The monster object if found, None otherwise.
    """
    logger.info(f"Looking up monster by name: {name}")
    with Session(engine) as session:
        statement = select(Monster).where(Monster.name == name)
        result = session.exec(statement)
        monster = result.first()

    return monster


async def lookup_armor_by_name(name: str):
    """
    Retrieve a armor from the database by it's name.

    :param name: The name of the armor.
    :return: The armor object if found, None otherwise.
    """
    logger.info(f"Looking up armor by name: {name}")
    with Session(engine) as session:
        statement = select(Armor).where(Armor.name == name)
        result = session.exec(statement)
        armor = result.first()

    return armor


async def lookup_weapon_by_name(name: str):
    """
    Retrieve a weapon from the database by it's name.

    :param name: The name of the weapon.
    :return: The weapon object if found, None otherwise.
    """
    logger.info(f"Looking up weapon by name: {name}")
    with Session(engine) as session:
        statement = select(Weapon).where(Weapon.name == name)
        result = session.exec(statement)
        weapon = result.first()

    return weapon

################################################################
# Save Objects to Database
################################################################

async def merge_object_changes(from_obj: object, to_obj: object) -> object:
    """
    Merge object changes so the object can be saved to the database without
    overwriting important database session attributes that start with underscores.

    :param from_obj: The object with changes.
    :param to_obj: The object to merge changes into.
    :return: The merged object.
    """
    logger.info(f"Merging object changes: {type(from_obj)} -> {type(to_obj)}")
    for attr, value in vars(from_obj).items():
        if not attr.startswith("_"):
            logger.info(f"Setting attribute: {attr} = {value}")
            if not hasattr(to_obj, attr) or value!= getattr(to_obj, attr):
                setattr(to_obj, attr, value)

    return to_obj


async def save_player(updated_player: Player) -> None:
    """
    Save a player to the database.

    :param player: The player object to save.
    :return:
    """
    logger.info(f"Saving player: {updated_player.username}")
    with Session(engine) as session:
        statement = select(Player).where(Player.id == updated_player.id)
        result = session.exec(statement)
        player = result.one()

        player = await merge_object_changes(updated_player, player)
        session.add(player)
        session.commit()


async def save_monster(updated_monster: Monster) -> None:
    """
    Save a monster to the database.

    :param monster: The monster object to save.
    :return:
    """
    logger.info(f"Saving player: {updated_monster.name}")
    with Session(engine) as session:
        statement = select(Monster).where(Monster.id == updated_monster.id)
        result = session.exec(statement)
        monster = result.one()

        monster = await merge_object_changes(updated_monster, monster)
        session.add(monster)
        session.commit()


async def save_armor(updated_armor: Armor) -> None:
    """
    Save an armor to the database.

    :param armor: The armor object to save.
    :return:
    """
    logger.info(f"Saving armor: {updated_armor.name}")
    with Session(engine) as session:
        logger.info(f"Looking up armor by id: {updated_armor.id} in {Armor.id}")
        statement = select(Armor).where(Armor.id == updated_armor.id)
        result = session.exec(statement)
        armor = result.one()

        armor = await merge_object_changes(updated_armor, armor)
        session.add(armor)
        session.commit()


async def save_weapon(updated_weapon: Weapon) -> None:
    """
    Save an weapon to the database.

    :param weapon: The weapon object to save.
    :return:
    """
    logger.info(f"Saving weapon: {updated_weapon.name}")
    with Session(engine) as session:
        statement = select(Weapon).where(Weapon.id == updated_weapon.id)
        result = session.exec(statement)
        weapon = result.one()

        weapon = await merge_object_changes(updated_weapon, weapon)
        session.add(weapon)
        session.commit()

################################################################
# Initialize Game Database
################################################################
logger = logging.getLogger("database")
engine = create_engine("sqlite:///game_database.db", echo=False)
SQLModel.metadata.create_all(bind=engine)
verify_game_data()