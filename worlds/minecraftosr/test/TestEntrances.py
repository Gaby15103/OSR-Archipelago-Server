from . import MCOSRTestBase
from .. import Constants


class TestEntrances(MCOSRTestBase):
    options = {
        "shuffle_structures": False,
        "structure_compasses": False
    }

    def testPortals(self):
        self.run_entrance_tests([
            ['Nether Portal', True, []],

            ['Aether Portal', False, []],
            ['Aether Portal', True, ['iron ingot']],

            ['Undergarden Portal', False, []],
            ['Undergarden Portal', False, ['iron ingot']],
            ['Undergarden Portal', False, ['iron ingot', 'gold ingot']],
            ['Undergarden Portal', False, ['iron ingot', 'gold ingot', 'redstone ingot']],
            ['Undergarden Portal', True, ['iron ingot', 'gold ingot', 'redstone ingot', 'netherite ingot']],

            ['Aether Portal and Nether Portal', False, []],
            ['Aether Portal and Nether Portal', True, ['iron ingot']],

            ['Twilight Forest Portal', False, []],
            ['Twilight Forest Portal', True, ['redstone ingot']],

            ['Tier 1 rocket', False, []],
            ['Tier 1 rocket', False, [
                "iron ingot"
            ]],
            ['Tier 1 rocket', False, [
                "iron ingot", "osmium ingot"
            ]],
            ['Tier 1 rocket', False, [
                "iron ingot", "osmium ingot", "copper ingot"
            ]],
            ['Tier 1 rocket', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot"
            ]],
            ['Tier 1 rocket', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot"
            ]],
            ['Tier 1 rocket', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot",
                "thermal machine frame"
            ]],
            ['Tier 1 rocket', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot",
                "thermal machine frame", "gear mold"
            ]],
            ['Tier 1 rocket', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot",
                "thermal machine frame", "gear mold", "steel ingot"
            ]],
            ['Tier 1 rocket', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot",
                "thermal machine frame", "gear mold", "steel ingot", "invar ingot"
            ]],
            ['Tier 1 rocket', True, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot",
                "thermal machine frame", "gear mold", "steel ingot", "invar ingot", "refined obsidian ingot"
            ]],

            ['Tier 2 rocket', False, []],
            ['Tier 2 rocket', False, [
                "iron ingot"
            ]],
            ['Tier 2 rocket', False, [
                "iron ingot", "osmium ingot"
            ]],
            ['Tier 2 rocket', False, [
                "iron ingot", "osmium ingot", "copper ingot"
            ]],
            ['Tier 2 rocket', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot"
            ]],
            ['Tier 2 rocket', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot"
            ]],
            ['Tier 2 rocket', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot",
                "thermal machine frame"
            ]],
            ['Tier 2 rocket', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot",
                "thermal machine frame", "gear mold"
            ]],
            ['Tier 2 rocket', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot",
                "thermal machine frame", "gear mold", "steel ingot"
            ]],
            ['Tier 2 rocket', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot",
                "thermal machine frame", "gear mold", "steel ingot", "invar ingot"
            ]],
            ['Tier 2 rocket', True, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot",
                "thermal machine frame", "gear mold", "steel ingot", "invar ingot", "refined obsidian ingot"
            ]],

            ['Tier 3 rocket', False, []],
            ['Tier 3 rocket', False, [
                "iron ingot"
            ]],
            ['Tier 3 rocket', False, [
                "iron ingot", "osmium ingot"
            ]],
            ['Tier 3 rocket', False, [
                "iron ingot", "osmium ingot", "copper ingot"
            ]],
            ['Tier 3 rocket', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot"
            ]],
            ['Tier 3 rocket', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot"
            ]],
            ['Tier 3 rocket', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot",
                "thermal machine frame"
            ]],
            ['Tier 3 rocket', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot",
                "thermal machine frame", "gear mold"
            ]],
            ['Tier 3 rocket', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot",
                "thermal machine frame", "gear mold", "steel ingot"
            ]],
            ['Tier 3 rocket', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot",
                "thermal machine frame", "gear mold", "steel ingot", "invar ingot"
            ]],
            ['Tier 3 rocket', True, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot",
                "thermal machine frame", "gear mold", "steel ingot", "invar ingot", "refined obsidian ingot"
            ]],

            ['Tier 4 rocket', False, []],
            ['Tier 4 rocket', False, [
                "iron ingot"
            ]],
            ['Tier 4 rocket', False, [
                "iron ingot", "osmium ingot"
            ]],
            ['Tier 4 rocket', False, [
                "iron ingot", "osmium ingot", "copper ingot"
            ]],
            ['Tier 4 rocket', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot"
            ]],
            ['Tier 4 rocket', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot"
            ]],
            ['Tier 4 rocket', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot",
                "thermal machine frame"
            ]],
            ['Tier 4 rocket', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot",
                "thermal machine frame", "gear mold"
            ]],
            ['Tier 4 rocket', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot",
                "thermal machine frame", "gear mold", "steel ingot"
            ]],
            ['Tier 4 rocket', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot",
                "thermal machine frame", "gear mold", "steel ingot", "invar ingot"
            ]],
            ['Tier 4 rocket', True, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot",
                "thermal machine frame", "gear mold", "steel ingot", "invar ingot", "refined obsidian ingot"
            ]],

            ['Rocket tier 2 and Twilight Portal', False, []],
            ['Rocket tier 2 and Twilight Portal', False, [
                "iron ingot"
            ]],
            ['Rocket tier 2 and Twilight Portal', False, [
                "iron ingot", "osmium ingot"
            ]],
            ['Rocket tier 2 and Twilight Portal', False, [
                "iron ingot", "osmium ingot", "copper ingot"
            ]],
            ['Rocket tier 2 and Twilight Portal', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot"
            ]],
            ['Rocket tier 2 and Twilight Portal', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot"
            ]],
            ['Rocket tier 2 and Twilight Portal', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot",
                "thermal machine frame"
            ]],
            ['Rocket tier 2 and Twilight Portal', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot",
                "thermal machine frame", "gear mold"
            ]],
            ['Rocket tier 2 and Twilight Portal', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot",
                "thermal machine frame", "gear mold", "steel ingot"
            ]],
            ['Rocket tier 2 and Twilight Portal', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot",
                "thermal machine frame", "gear mold", "steel ingot", "invar ingot"
            ]],
            ['Rocket tier 2 and Twilight Portal', True, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot",
                "thermal machine frame", "gear mold", "steel ingot", "invar ingot", "refined obsidian ingot"
            ]],

            ['Rocket and Nether Portal', False, []],
            ['Rocket and Nether Portal', False, [
                "iron ingot"
            ]],
            ['Rocket and Nether Portal', False, [
                "iron ingot", "osmium ingot"
            ]],
            ['Rocket and Nether Portal', False, [
                "iron ingot", "osmium ingot", "copper ingot"
            ]],
            ['Rocket and Nether Portal', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot"
            ]],
            ['Rocket and Nether Portal', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot"
            ]],
            ['Rocket and Nether Portal', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot",
                "thermal machine frame"
            ]],
            ['Rocket and Nether Portal', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot",
                "thermal machine frame", "gear mold"
            ]],
            ['Rocket and Nether Portal', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot",
                "thermal machine frame", "gear mold", "steel ingot"
            ]],
            ['Rocket and Nether Portal', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot",
                "thermal machine frame", "gear mold", "steel ingot", "invar ingot"
            ]],
            ['Rocket and Nether Portal', True, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot",
                "thermal machine frame", "gear mold", "steel ingot", "invar ingot", "refined obsidian ingot"
            ]],

            ['End Portal', False, []],
            ['End Portal', False, [
                "iron ingot"
            ]],
            ['End Portal', False, [
                "iron ingot", "gold ingot"
            ]],
            ['End Portal', False, [
                "iron ingot", "gold ingot", "netherite ingot"
            ]],
            ['End Portal', False, [
                "iron ingot", "gold ingot", "netherite ingot", "redstone ingot"
            ]],
            ['End Portal', False, [
                "iron ingot", "gold ingot", "netherite ingot", "redstone ingot", "black iron ingot"
            ]],
            ['End Portal', False, [
                "iron ingot", "gold ingot", "netherite ingot", "redstone ingot", "black iron ingot",
                "basic crafting table"
            ]],
            ['End Portal', True, [
                "iron ingot", "gold ingot", "netherite ingot", "redstone ingot", "black iron ingot",
                "basic crafting table","ender ingot"
            ]],

            ['Rocket and The End Portal', False, []],
            ['Rocket and The End Portal', False, [
                "iron ingot"
            ]],
            ['Rocket and The End Portal', False, [
                "iron ingot", "osmium ingot"
            ]],
            ['Rocket and The End Portal', False, [
                "iron ingot", "osmium ingot", "copper ingot"
            ]],
            ['Rocket and The End Portal', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot"
            ]],
            ['Rocket and The End Portal', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot"
            ]],
            ['Rocket and The End Portal', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot",
                "thermal machine frame"
            ]],
            ['Rocket and The End Portal', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot",
                "thermal machine frame", "gear mold"
            ]],
            ['Rocket and The End Portal', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot",
                "thermal machine frame", "gear mold", "steel ingot"
            ]],
            ['Rocket and The End Portal', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot",
                "thermal machine frame", "gear mold", "steel ingot", "invar ingot"
            ]],
            ['Rocket and The End Portal', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot",
                "thermal machine frame", "gear mold", "steel ingot", "invar ingot", "refined obsidian ingot"
            ]],
            ['Rocket and The End Portal', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot",
                "thermal machine frame", "gear mold", "steel ingot", "invar ingot", "refined obsidian ingot",
                "gold ingot"
            ]],
            ['Rocket and The End Portal', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot",
                "thermal machine frame", "gear mold", "steel ingot", "invar ingot", "refined obsidian ingot",
                "gold ingot", "netherite ingot"
            ]],
            ['Rocket and The End Portal', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot",
                "thermal machine frame", "gear mold", "steel ingot", "invar ingot", "refined obsidian ingot",
                "gold ingot", "netherite ingot", "black iron ingot"
            ]],
            ['Rocket and The End Portal', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot",
                "thermal machine frame", "gear mold", "steel ingot", "invar ingot", "refined obsidian ingot",
                "gold ingot", "netherite ingot", "black iron ingot", "basic crafting table"
            ]],
            ['Rocket and The End Portal', True, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot",
                "thermal machine frame", "gear mold", "steel ingot", "invar ingot", "refined obsidian ingot",
                "gold ingot", "netherite ingot", "black iron ingot","basic crafting table", "ender ingot"
            ]],

            ['Rocket tier 3 and The end', False, []],
            ['Rocket tier 3 and The end', False, [
                "iron ingot"
            ]],
            ['Rocket tier 3 and The end', False, [
                "iron ingot", "osmium ingot"
            ]],
            ['Rocket tier 3 and The end', False, [
                "iron ingot", "osmium ingot", "copper ingot"
            ]],
            ['Rocket tier 3 and The end', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot"
            ]],
            ['Rocket tier 3 and The end', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot"
            ]],
            ['Rocket tier 3 and The end', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot",
                "thermal machine frame"
            ]],
            ['Rocket tier 3 and The end', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot",
                "thermal machine frame", "gear mold"
            ]],
            ['Rocket tier 3 and The end', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot",
                "thermal machine frame", "gear mold", "steel ingot"
            ]],
            ['Rocket tier 3 and The end', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot",
                "thermal machine frame", "gear mold", "steel ingot", "invar ingot"
            ]],
            ['Rocket tier 3 and The end', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot",
                "thermal machine frame", "gear mold", "steel ingot", "invar ingot", "refined obsidian ingot"
            ]],
            ['Rocket tier 3 and The end', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot",
                "thermal machine frame", "gear mold", "steel ingot", "invar ingot", "refined obsidian ingot",
                "gold ingot"
            ]],
            ['Rocket tier 3 and The end', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot",
                "thermal machine frame", "gear mold", "steel ingot", "invar ingot", "refined obsidian ingot",
                "gold ingot", "netherite ingot"
            ]],
            ['Rocket tier 3 and The end', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot",
                "thermal machine frame", "gear mold", "steel ingot", "invar ingot", "refined obsidian ingot",
                "gold ingot", "netherite ingot", "black iron ingot"
            ]],
            ['Rocket tier 3 and The end', False, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot",
                "thermal machine frame", "gear mold", "steel ingot", "invar ingot", "refined obsidian ingot",
                "gold ingot", "netherite ingot", "black iron ingot", "basic crafting table"
            ]],
            ['Rocket tier 3 and The end', True, [
                "iron ingot", "osmium ingot", "copper ingot", "redstone ingot", "soularium ingot",
                "thermal machine frame", "gear mold", "steel ingot", "invar ingot", "refined obsidian ingot",
                "gold ingot", "netherite ingot", "black iron ingot", "basic crafting table", "ender ingot"
            ]],

        ])