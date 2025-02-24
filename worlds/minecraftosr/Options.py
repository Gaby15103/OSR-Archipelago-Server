from Options import Choice, Toggle, DefaultOnToggle, Range, OptionList, DeathLink, PlandoConnections, \
    PerGameCommonOptions
from .Constants import region_info
from dataclasses import dataclass


#optional chapter
#    -Omega
#    -Psi
#    -Chi
#    -Phi

class QuestGoal(Choice):
    """Quest required to finish the game."""
    display_name = "Objective"
    option_simple_achievement = 0
    option_dragon_egg = 1
    option_infinite_wand = 2
    option_conquor_the_twilight = 3
    option_gaia_spirit_ingot = 4
    option_insanite_block = 5
    option_ultimate_forge = 6
    option_tier_4_rocket = 7
    option_transmutation_interface = 8
    option_chaos_shard = 9
    option_infinity_ingot = 10
    option_infinity_tools = 11
    option_infinity_armor = 12
    option_creative_item  = 13
    default = 0

class ShuffleStructures(DefaultOnToggle):
    """Enables shuffling of villages, outposts, fortresses, bastions, and end cities."""
    display_name = "Shuffle Structures"

class StructureCompasses(DefaultOnToggle):
    """Adds structure compasses to the item pool, which point to the nearest indicated structure."""
    display_name = "Structure Compasses"

class BeeTraps(Range):
    """Replaces a percentage of junk items with bee traps, which spawn multiple angered bees around every player when
    received."""
    display_name = "Bee Trap Percentage"
    range_start = 0
    range_end = 100
    default = 0


class CombatDifficulty(Choice):
    """Modifies the level of items logically required for exploring dangerous areas and fighting bosses."""
    display_name = "Combat Difficulty"
    option_easy = 0
    option_normal = 1
    option_hard = 2
    default = 1

class SendDefeatedMobs(Toggle):
    """Send killed mobs to other Minecraft worlds which have this option enabled."""
    display_name = "Send Defeated Mobs"

class StartingItems(OptionList):
    """Start with these items. Each entry should be of this format: {item: "item_name", amount: #}
    `item` can include components, and should be in an identical format to a `/give` command with
    `"` escaped for json reasons.

    `amount` is optional and will default to 1 if omitted.

    example:
    ```
    starting_items: [
        { "item": "minecraft:stick[minecraft:custom_name=\"{'text':'pointy stick'}\"]" },
        { "item": "minecraft:arrow[minecraft:rarity=epic]", amount: 64 }
    ]
    ```
    """
    display_name = "Starting Items"

class MCPlandoConnections(PlandoConnections):
    entrances = set(connection[0] for connection in region_info["default_connections"])
    exits = set(connection[1] for connection in region_info["default_connections"])

    @classmethod
    def can_connect(cls, entrance, exit):
        if exit in region_info["illegal_connections"] and entrance in region_info["illegal_connections"][exit]:
            return False
        return True

@dataclass
class MinecraftOsrOptions(PerGameCommonOptions):
    plando_connections: MCPlandoConnections
    quest_goal:QuestGoal
    shuffle_structures: ShuffleStructures
    structure_compasses: StructureCompasses

    combat_difficulty: CombatDifficulty
    bee_traps: BeeTraps
    send_defeated_mobs: SendDefeatedMobs
    death_link: DeathLink
    starting_items: StartingItems