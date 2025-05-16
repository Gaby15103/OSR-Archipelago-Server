from . import MCOSRTestBase


# Format:
# [location, expected_result, given_items, [excluded_items]]
# Every advancement has its own test, named by its internal ID number. 
class TestAdvancements(MCOSRTestBase):
    options = {
        "shuffle_structures": False,
        "structure_compasses": False
    }

    def test_42000(self):
        self.run_location_tests([
            ["0366E4C57024B5E1:exdeorum:wooden_hammer:245134766379415009", True, []],
        ])

    def test_42001(self):
        self.run_location_tests([
            ["3267B5D26EB6EDAC:Space Suit:3632071539902836140", False, []],
            ["3267B5D26EB6EDAC:Space Suit:3632071539902836140", False, ["iron ingot"
            ]],
            ["3267B5D26EB6EDAC:Space Suit:3632071539902836140", False, ["iron ingot","osmium ingot"
            ]],
            ["3267B5D26EB6EDAC:Space Suit:3632071539902836140", False, ["iron ingot","osmium ingot", "redstone ingot"
            ]],
            ["3267B5D26EB6EDAC:Space Suit:3632071539902836140", False, ["iron ingot","osmium ingot", "redstone ingot",
              "soularium ingot"
            ]],
            ["3267B5D26EB6EDAC:Space Suit:3632071539902836140", False, ["iron ingot","osmium ingot", "redstone ingot",
              "soularium ingot", "thermal machine frame"
            ]],
            ["3267B5D26EB6EDAC:Space Suit:3632071539902836140", False, ["iron ingot","osmium ingot", "redstone ingot",
              "soularium ingot", "thermal machine frame", "gear mold"
            ]],
            ["3267B5D26EB6EDAC:Space Suit:3632071539902836140", False, ["iron ingot","osmium ingot", "redstone ingot",
              "soularium ingot", "thermal machine frame", "gear mold", "steel ingot"
            ]],
            ["3267B5D26EB6EDAC:Space Suit:3632071539902836140", False, ["iron ingot","osmium ingot", "redstone ingot",
              "soularium ingot", "thermal machine frame", "gear mold", "steel ingot", "invar ingot"
            ]],
            ["3267B5D26EB6EDAC:Space Suit:3632071539902836140", False, ["iron ingot","osmium ingot", "redstone ingot",
              "soularium ingot", "thermal machine frame", "gear mold", "steel ingot", "invar ingot","refined obsidian ingot"
            ]],
        ])
