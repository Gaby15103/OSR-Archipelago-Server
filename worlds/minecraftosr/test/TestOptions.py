from . import MCOSRTestBase
from .. import Options

from BaseClasses import ItemClassification
from ..Constants import region_info


class GoalTestBase(MCOSRTestBase):
    options = {
        "quest_goals": Options.QuestGoal.option_simple_achievement
    }
    # beatability test implicit

class CompassTestBase(MCOSRTestBase):
    def test_compasses_in_pool(self):
        structures = [x[1] for x in region_info["default_connections"]]
        itempool_str = {item.name for item in self.multiworld.itempool}
        for struct in structures:
            assert f"Structure Compass ({struct})" in itempool_str


class NoBeeTestBase(MCOSRTestBase):
    options = {
        "bee_traps": Options.BeeTraps.range_start
    }

    # With no bees, there are no traps in the pool
    def test_bees(self):
        for item in self.multiworld.itempool:
            assert item.classification != ItemClassification.trap


class AllBeeTestBase(MCOSRTestBase):
    options = {
        "bee_traps": Options.BeeTraps.range_end
    }

    # With max bees, there are no filler items, only bee traps
    def test_bees(self):
        for item in self.multiworld.itempool:
            assert item.classification != ItemClassification.filler
