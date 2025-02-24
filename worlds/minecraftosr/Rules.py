from BaseClasses import CollectionState
from worlds.generic.Rules import exclusion_rules

from . import Constants
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import MinecraftOsrWorld


# Helper functions
# moved from logicmixin

def has_iron_ingots(world: "minecraftOsrWorld", state: CollectionState, player: int) -> bool:
    return state.has('Progressive Tools', player) and state.has('Progressive Resource Crafting', player)

