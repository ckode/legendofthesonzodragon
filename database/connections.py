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
    logger = logging.getLogger(__name__)

    logger.info("Verifying game data in the database...")
    print("Verifying game data in the database...")
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

        print(f"Weapons: {w_count}")
        if w_count == 0:
            print(f"Found {w_count} weapons, yet my dumbass is still adding them again.")
            logger.info("Adding weapons to the database.")
            session.add_all(weapons_list)
        if a_count == 0:
            logger.info("Updating armor in the database.")
            session.add_all(armor_list)
        if p_count == 0:
            logger.info("Updating players in the database.")
            session.add_all(players_list)
        if m_count == 0:
            logger.info("Updating monsters in the database.")
            session.add_all(monsters_list)

        session.commit()



async def lookup_player_by_username(name: str):
    """
    Retrieve a player from the database by their username.

    :param name: The username of the player.
    :return: The player object if found, None otherwise.
    """
    logger = logging.getLogger(__name__)
    with Session(engine) as session:
        statement = select(Player).where(Player.username == name)
        result = session.exec(statement)
        player = result.first()

    return player


async def lookup_player_by_name(name: str):
    """
    Retrieve a player from the database by their username.

    :param name: The username of the player.
    :return: The player object if found, None otherwise.
    """
    logger = logging.getLogger(__name__)
    with Session(engine) as session:
        statement = select(Player).where(Player.name == name)
        result = session.exec(statement)
        player = result.first()

    return player



################################################################
# Save Objects to Database
################################################################

async def save_player(updated_player: Player) -> None:
    """
    Save a player to the database.

    :param player: The player object to save.
    :return:
    """
    logger = logging.getLogger(__name__)
    with Session(engine) as session:
        statement = select(Player).where(Player.id == updated_player.id)
        result = session.exec(statement)
        player = result.one()
        player.username = updated_player.username
        player.password = updated_player.password
        player.name = updated_player.name
        player.level = updated_player.level
        player.health = updated_player.health
        player.exp = updated_player.exp
        player.weapon = updated_player.weapon
        player.armor = updated_player.armor
        player.gold = updated_player.gold
        player.bank = updated_player.bank
        player.description = updated_player.description
        session.add(player)
        session.commit()

################################################################
# Initialize Game Database
################################################################
engine = create_engine("sqlite:///game_database.db", echo=False)
SQLModel.metadata.create_all(bind=engine)
verify_game_data()