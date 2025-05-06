import os
import json
import settings
import typing
from base64 import b64encode, b64decode
from typing import Dict, Any

from BaseClasses import Region, Entrance, Item, Tutorial, ItemClassification, Location
from worlds.AutoWorld import World, WebWorld

from . import Constants
from .Options import MinecraftOsrOptions
from .Structures import shuffle_structures
from .ItemPool import build_item_pool, get_junk_item_names
from .Rules import set_rules

client_version = 9

class MinecraftOsrSettings(settings.Group):
    class ForgeDirectory(settings.OptionalUserFolderPath):
        pass

    class ReleaseChannel(str):
                """
        release channel, currently "release", or "beta"
        any games played on the "beta" channel have a high likelihood of no longer working on the "release" channel.
        """

    forge_directory: ForgeDirectory = ForgeDirectory("Minecraft Osr Forge server")
    max_heap_size: str = "2G"
    release_channel: ReleaseChannel = ReleaseChannel("release")


class MinecraftOsrWebWorld(WebWorld):
    theme = "jungle"
    bug_report_page = "https://gitlab.com/gabrielmorin1/natif-4-polite-ap/-/issues"

    setup = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Archipelago Minecraft software on your computer. This guide covers"
        "single-player, multiworld, and related software.",
        "English",
        "minecraft_en.md",
        "minecraft/en",
        ["Kono Tyran"]
    )

    tutorials = [setup]

class MinecraftOsrWorld(World):
    """
    Minecraft is a game about creativity. In a world made entirely of cubes, you explore, discover, mine,
    craft, and try not to explode. Delve deep into the earth and discover abandoned mines, ancient
    structures, and materials to create a portal to another world. Defeat the Ender Dragon, and claim
    victory!
    """
    game = "Minecraft OSR"
    options_dataclass = MinecraftOsrOptions
    options: MinecraftOsrOptions
    settings: typing.ClassVar[MinecraftOsrSettings]
    topology_present = True
    web = MinecraftOsrWebWorld()

    item_name_to_id = Constants.item_name_to_id
    location_name_to_id = Constants.location_name_to_id

    def _get_mc_data(self) -> Dict[str, Any]:
        exits = [connection[0] for connection in Constants.region_info["default_connections"]]
        quest_mapping = {
            0: "18E8E67F431E99E4:Simple Achievements:1794937885768456676",
            1: "46F450DDEAECE702:minecraft:dragon_egg:5112800391031744258",
            2: "0B4FE52E8C83C177:constructionwand:infinity_wand:815122045666050423",
            3: "69912119C98D6247:Conquor the Twilight:7606897640244863559",
            4: "79E30F3A54F84EA4:botania:gaia_ingot:8782880441510678180",
            5: "187CE1DC0DC4AF2D:bigreactors:insanite_block:1764533489262440237",
            6: "2F89C9A81F049F60:betterfurnacesreforged:ultimate_forge:3425490715504058208",
            7: "4A3ED57B133E0F5C:ad_astra:tier_4_rocket:5349948131943255900",
            8: "46DCFABCE6CA89BC:projectexpansion:transmutation_interface:5106231766764128700",
            9: "2218FD98BD04A52E:draconicevolution:chaos_shard:2456992429178660142",
            10: "725C86A23081A0F6:avaritia:infinity_ingot:8240609449337790710",
            11: "030AD281CFAFB320:Infinity Tools:219218986857902880",
            12: "51F3D3ABAD3D00CC:Infinity Armor:5905296270712176844"
        }
        return {
            'world_seed': self.random.getrandbits(32),
            'seed_name': self.multiworld.seed_name,
            'player_name': self.player_name,
            'player_id': self.player,
            'client_version': client_version,
            'structures': {exit: self.multiworld.get_entrance(exit, self.player).connected_region.name for exit in exits},
            'quest_goal': quest_mapping.get(self.options.quest_goal.value),
            'MC35': bool(self.options.send_defeated_mobs.value),
            'death_link': bool(self.options.death_link.value),
            'starting_items': json.dumps(self.options.starting_items.value),
            'race': self.multiworld.is_race,
        }

    def create_item(self, name: str) -> Item:
        item_class = ItemClassification.filler
        if name in Constants.item_info["progression_items"]:
            item_class = ItemClassification.progression
        if name in Constants.item_info["useful_items"]:
            item_class = ItemClassification.useful
        if name in Constants.item_info["trap_items"]:
            item_class = ItemClassification.trap

        return MinecraftOsrItem(name, item_class, self.item_name_to_id.get(name, None), self.player)

    def create_event(self, region_name: str, event_name: str) -> None:
        region = self.multiworld.get_region(region_name, self.player)
        loc = MinecraftOsrLocation(self.player, event_name, None, region)
        loc.place_locked_item(self.create_event_item(event_name))
        region.locations.append(loc)

    def create_event_item(self, name: str) -> Item:
        item = self.create_item(name)
        item.classification = ItemClassification.progression
        return item

    def create_regions(self) -> None:
        # Create regions
        for region_name, exits in Constants.region_info["regions"]:
            r = Region(region_name, self.player, self.multiworld)
            for exit_name in exits:
                r.exits.append(Entrance(self.player, exit_name, r))
            self.multiworld.regions.append(r)

        # Bind mandatory connections
        for entr_name, region_name in Constants.region_info["mandatory_connections"]:
            e = self.multiworld.get_entrance(entr_name, self.player)
            r = self.multiworld.get_region(region_name, self.player)
            e.connect(r)

        # Add locations
        for region_name, locations in Constants.location_info["locations_by_region"].items():

            region = self.multiworld.get_region(region_name, self.player)
            for loc_name in locations:
                loc = MinecraftOsrLocation(self.player, loc_name,
                    self.location_name_to_id.get(loc_name, None), region)
                region.locations.append(loc)

        # Add events
        #self.create_event("Nether Fortress", "Blaze Rods")
        #self.create_event("The End", "Ender Dragon")
        #self.create_event("Nether Fortress", "Wither")

        # Shuffle the connections
        shuffle_structures(self)

    def create_items(self) -> None:
        self.multiworld.itempool += build_item_pool(self)

    set_rules = set_rules

    def generate_output(self, output_directory: str) -> None:
        data = self._get_mc_data()
        filename = f"{self.multiworld.get_out_file_name_base(self.player)}.apmc"
        with open(os.path.join(output_directory, filename), 'wb') as f:
            f.write(b64encode(bytes(json.dumps(data), 'utf-8')))

    def fill_slot_data(self) -> Dict:
        return self._get_mc_data()

    def get_filler_item_name(self) -> str:
        return get_junk_item_names(self.random, 1)[0]

class MinecraftOsrLocation(Location):
    game = "Minecraft OSR"

class MinecraftOsrItem(Item):
    game = "Minecraft OSR"

def mc_update_output(raw_data, server, port):
    data = json.loads(b64decode(raw_data))
    data['server'] = server
    data['port'] = port
    return b64encode(bytes(json.dumps(data), 'utf-8'))