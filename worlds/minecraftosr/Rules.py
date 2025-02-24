from BaseClasses import CollectionState
from worlds.generic.Rules import exclusion_rules

from . import Constants
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import MinecraftOsrWorld


# Helper functions
# moved from logicmixin

def has_iron_ingots(world: "MinecraftOsrWorld", state: CollectionState, player: int) -> bool:
    return state.has("iron ingot", player)


def has_gold_ingots(world: "MinecraftOsrWorld", state: CollectionState, player: int) -> bool:
    return state.has("gold ingot", player)


def has_aluminium_ingots(world: "MinecraftOsrWorld", state: CollectionState, player: int) -> bool:
    return state.has("aluminium ingot", player)


def has_silver_ingots(world: "MinecraftOsrWorld", state: CollectionState, player: int) -> bool:
    return state.has("silver ingot", player)


def has_lead_ingots(world: "MinecraftOsrWorld", state: CollectionState, player: int) -> bool:
    return state.has("lead ingot", player)


def has_nickel_ingots(world: "MinecraftOsrWorld", state: CollectionState, player: int) -> bool:
    return state.has("nickel ingot", player)


def has_osmium_ingots(world: "MinecraftOsrWorld", state: CollectionState, player: int) -> bool:
    return state.has("osmium ingot", player)


def has_tin_ingots(world: "MinecraftOsrWorld", state: CollectionState, player: int) -> bool:
    return state.has("tin ingot", player)


def has_copper_ingots(world: "MinecraftOsrWorld", state: CollectionState, player: int) -> bool:
    return state.has("copper ingot", player)

def has_redstone_alloy_ingots(world: "MinecraftOsrWorld", state: CollectionState, player: int) -> bool:
    return state.has("redstone alloy ingot", player)

def has_netherite_ingots(world: "MinecraftOsrWorld", state: CollectionState, player: int) -> bool:
    return state.has("netherite ingot", player)

def has_conductive_alloy_ingots(world: "MinecraftOsrWorld", state: CollectionState, player: int) -> bool:
    return state.has("conductive alloy ingot", player)

def has_item_conduit(world: "MinecraftOsrWorld", state: CollectionState, player: int) -> bool:
    return state.has("item conduit", player)

def has_fluid_conduit(world: "MinecraftOsrWorld", state: CollectionState, player: int) -> bool:
    return state.has("fluid conduit", player)

def has_redstone_ingot(world: "MinecraftOsrWorld", state: CollectionState, player: int) -> bool:
    return state.has("redstone ingot", player)

def has_dark_steel_ingot(world: "MinecraftOsrWorld", state: CollectionState, player: int) -> bool:
    return state.has("dark steel ingot", player)

def has_soulium_ingot(world: "MinecraftOsrWorld", state: CollectionState, player: int) -> bool:
    return state.has("soulium ingot", player)

def has_ender_eye(world: "MinecraftOsrWorld", state: CollectionState, player: int) -> bool:
    return state.has("soulium ingot", player)

def has_thermal_machine_frame(world: "MinecraftOsrWorld", state: CollectionState, player: int) -> bool:
    return state.has("thermal machine frame", player) and has_soularium_ingot(world,state,player)

def has_soularium_ingot(world: "MinecraftOsrWorld", state: CollectionState, player: int) -> bool:
    return state.has("soularium_ingot", player)

def has_gear_mold(world: "MinecraftOsrWorld", state: CollectionState, player: int) -> bool:
    return state.has("gear_mold", player)


def get_rules_lookup(world, player: int):
    rules_lookup = {
        "locations": {
            # Alpha
            "0366E4C57024B5E1:exdeorum:wooden_hammer:245134766379415009": lambda state:
            state.can_reach_location("3EE16F0264052C50:Getting Started:4531024756170107984"),
            "3FC54D16CC751DE7:exdeorum:string_mesh:4595163755116305895": lambda state: state.can_reach_location(
                "3EE16F0264052C50:Getting Started:4531024756170107984"),
            "2E11E2DE34806504:woodenbucket:wooden_bucket:3319683844340212996": lambda state: state.can_reach_location(
                "3EE16F0264052C50:Getting Started:4531024756170107984"),
            "30DA803A12E35624:Cobblestone and Lava Generation:3520267045656811044": lambda
                state: state.can_reach_location("3EE16F0264052C50:Getting Started:4531024756170107984")
                        and (state.can_reach_location("45B40527613AF29C:exdeorum:porcelain_bucket:5022645151118062236")
                             or has_iron_ingots(world,state,player)),
            "5139878FF928711F:Starting Power:5852858243174920479": lambda state: state.can_reach_location(
                "3EE16F0264052C50:Getting Started:4531024756170107984")
                        and has_conductive_alloy_ingots(world,state,player) and has_item_conduit(world, state, player)
                        and has_fluid_conduit(world, state,player) and has_gold_ingots(world, state, player)
                        and has_copper_ingots(world, state,player),
            "1DBA3366F50A27DD:exdeorum:stone_hammer:2142081090058856413": lambda
                state: state.can_reach_location("0366E4C57024B5E1:exdeorum:wooden_hammer:245134766379415009"),
            "37D1B059E4217163:exdeorum:iron_hammer:4022189842344538467": lambda
                state: state.can_reach_location("1DBA3366F50A27DD:exdeorum:stone_hammer:2142081090058856413")
                        and has_iron_ingots(world,state,player),
            "0299EC5E270E0F04:exdeorum:golden_hammer:187440748638899972": lambda
                state: state.can_reach_location("37D1B059E4217163:exdeorum:iron_hammer:4022189842344538467")
                        and has_gold_ingots(world,state,player),
            "3480CD4B028D3084:exdeorum:diamond_hammer:3783249409040265348": lambda
                state: state.can_reach_location("0299EC5E270E0F04:exdeorum:golden_hammer:187440748638899972"),
            "4CE5EA6C8E105623:exdeorum:netherite_hammer:5541092668510066211": lambda
                state: state.can_reach_location("3480CD4B028D3084:exdeorum:diamond_hammer:3783249409040265348")
                        and has_netherite_ingots(world,state,player),
            "2386929E75F58990:minecraft:iron_pickaxe:2559894647488219536": lambda
                state: state.can_reach_location("3FC54D16CC751DE7:exdeorum:string_mesh:4595163755116305895")
                        and has_iron_ingots(world,state,player),
            "11B0D33506A1E4B7:Mechanical Hammer:1274750919243850935": lambda
                state: state.can_reach_location("5139878FF928711F:Starting Power:5852858243174920479")
                        and has_iron_ingots(world,state,player),
            "423FCA2A7EF09109:Mechanical Sieve: 4773756413903147273": lambda
                state: state.can_reach_location("11B0D33506A1E4B7:Mechanical Hammer:1274750919243850935"),
            "49117C982012A5F6": lambda
                state: state.can_reach_location("423FCA2A7EF09109:Mechanical Sieve: 4773756413903147273")
                        and has_redstone_ingot(world,state,player),
            "2EAEA784ACD625B6:cobblefordays:tier_2:3363810159969576374": lambda
                state: state.can_reach_location("30DA803A12E35624:Cobblestone and Lava Generation:3520267045656811044"),
            "3105EE93AE0C62BF:cobblefordays:tier_3:3532491800789672639": lambda
                state: state.can_reach_location("2EAEA784ACD625B6:cobblefordays:tier_2:3363810159969576374")
                        and has_iron_ingots(world,state,player),
            "62F15DDF575F4605:cobblefordays:tier_4:7129582898929157637": lambda
                state: state.can_reach_location("3105EE93AE0C62BF:cobblefordays:tier_3:3532491800789672639")
                        and has_gold_ingots(world,state,player),
            "702B0D773193BB64:cobblefordays:tier_5:8082568761830521700": lambda
                state: state.can_reach_location("62F15DDF575F4605:cobblefordays:tier_4:7129582898929157637"),
            "45B40527613AF29C:exdeorum:porcelain_bucket:5022645151118062236": lambda
                state: state.can_reach_location("2E11E2DE34806504:woodenbucket:wooden_bucket:3319683844340212996"),
            "1B56B0A5C3158499:minecraft:bucket:1969956113010230425": lambda
                state: state.can_reach_location("45B40527613AF29C:exdeorum:porcelain_bucket:5022645151118062236")
                        and has_iron_ingots(world,state,player),
            "2EC618F53E619F73:exdeorum:flint_mesh:3370408812726034291": lambda
                state: state.can_reach_location("3FC54D16CC751DE7:exdeorum:string_mesh:4595163755116305895"),
            "7FEFE2387B9C77E4:exdeorum:iron_mesh:9218835694470592484": lambda
                state: state.can_reach_location("2EC618F53E619F73:exdeorum:flint_mesh:3370408812726034291")
                        and has_iron_ingots(world,state,player),
            "59DB37E04DE34EBD:exdeorum:golden_mesh:6474830325794164413": lambda
                state: state.can_reach_location("7FEFE2387B9C77E4:exdeorum:iron_mesh:9218835694470592484")
                        and has_gold_ingots(world,state,player),
            "50FA8A733EE88840:exdeorum:diamond_mesh:5835128494793197632": lambda
                state: state.can_reach_location("59DB37E04DE34EBD:exdeorum:golden_mesh:6474830325794164413"),
            "2BC7CCC03A2AB01A:exdeorum:netherite_mesh:3154715189977985050": lambda
                state: state.can_reach_location("50FA8A733EE88840:exdeorum:diamond_mesh:5835128494793197632")
                        and has_netherite_ingots(world,state,player),
            "12DC5146FBF6131B:trashcans:item_trash_can:1359050552875815707": lambda
                state: state.can_reach_location("2386929E75F58990:minecraft:iron_pickaxe:2559894647488219536"),
            "09CD6F61EF329771:trashcans:liquid_trash_can:706343182982616945": lambda
                state: state.can_reach_location("12DC5146FBF6131B:trashcans:item_trash_can:1359050552875815707"),
            "57D82F63CCCAFC6A:trashcans:energy_trash_can:6329861381953354858": lambda
                state: state.can_reach_location("09CD6F61EF329771:trashcans:liquid_trash_can:706343182982616945"),
            "516F027BF3428F94:trashcans:ultimate_trash_can:5867911570872504212": lambda
                state: state.can_reach_location("57D82F63CCCAFC6A:trashcans:energy_trash_can:6329861381953354858"),
            "092E17F60451DB2F:minecraft:enchanting_table:661492540671908655": lambda
                state: state.can_reach_location("2386929E75F58990:minecraft:iron_pickaxe:2559894647488219536"),
            "4140645DC360472A:Enchanter:4701868364847400746": lambda
                state: state.can_reach_location("092E17F60451DB2F:minecraft:enchanting_table:661492540671908655")
                        and (has_dark_steel_ingot(world,state,player) or
                             (has_soulium_ingot(world,state,player) and state.can_reach_region('The Nether', player))),

            # Beta
            "4B2825C257986EF8:mob_grinding_utils:absorption_hopper:5415620068536512248": lambda
                state: state.can_reach_location("3EE16F0264052C50:Getting Started:4531024756170107984")
                        and has_iron_ingots(world,state,player),
            "4BE855C08DE7BDC4:mob_grinding_utils:fan:5469716032944324036": lambda
                state: state.can_reach_location("3EE16F0264052C50:Getting Started:4531024756170107984")
                        and has_iron_ingots(world,state,player),
            "252FF7E709D75DBB:mob_grinding_utils:spikes:2679632874983349691": lambda
                state: state.can_reach_location("3EE16F0264052C50:Getting Started:4531024756170107984")
                       and has_iron_ingots(world, state, player),
            "09EAF3F7ABE5840E:cookingforblockheads:recipe_book:714651735958062094": lambda
                state: state.can_reach_location("3EE16F0264052C50:Getting Started:4531024756170107984"),
            "0D002DB1FBB8EFA3:farmingforblockheads:market:936798964948725667": lambda
                state: state.can_reach_location("3EE16F0264052C50:Getting Started:4531024756170107984"),
            "42E5E12B9230AD31:cookingforblockheads: crafting_book:4820506553422490929": lambda
                state: state.can_reach_location("09EAF3F7ABE5840E:cookingforblockheads:recipe_book:714651735958062094"),
            "37774FFF19A446DF:cookingforblockheads:no_filter_edition:3996751151380055775": lambda
                state: state.can_reach_location("09EAF3F7ABE5840E:cookingforblockheads:recipe_book:714651735958062094"),
            "64593A765B84CBFE:Build a Kitchen:7230874956736023550": lambda
                state: state.can_reach_location("09EAF3F7ABE5840E:cookingforblockheads:recipe_book:714651735958062094")
                        and has_iron_ingots(world,state,player),
            "20B034D16EE93E07:Pam's Kitchen Tools:2355440679228358151": lambda
                state: state.can_reach_location("09EAF3F7ABE5840E:cookingforblockheads:recipe_book:714651735958062094")
                        and has_copper_ingots(world,state,player),
            "3966F96406BF7DF4:mob_grinding_utils:absorption_upgrade:4136267515791638004": lambda
                state: state.can_reach_location("4B2825C257986EF8:mob_grinding_utils:absorption_hopper:5415620068536512248"),
            "4109CFAABCC43103:mob_grinding_utils:tank:4686505219474075907": lambda
                state: state.can_reach_location("4B2825C257986EF8:mob_grinding_utils:absorption_hopper:5415620068536512248"),
            "755E8742EEC1D006:mob_grinding_utils:xp_tap:8457345871791640582": lambda
                state: state.can_reach_location("4109CFAABCC43103:mob_grinding_utils:tank:4686505219474075907"),
            "16AD6B208C1D9CF2:mob_grinding_utils:ender_inhibitor_on:1634080027339234546": lambda
                state: state.can_reach_location("755E8742EEC1D006:mob_grinding_utils:xp_tap:8457345871791640582")
                        and has_ender_eye(world,state,player),
            "31A6D9ACF02F1721:mob_grinding_utils:nutritious_chicken_feed:3577786290779658017": lambda
                state: state.can_reach_location("4B2825C257986EF8:mob_grinding_utils:absorption_hopper:5415620068536512248")
                        and ((state.can_reach_location("7AC647D823CD6523:immersiveengineering:light_engineering:8846837511655089443")
                        and state.can_reach_location("4B61E75F57941931:immersiveengineering:steel_scaffolding_standard:5431877022262761777"))
                             or (has_thermal_machine_frame(world,state,player) and has_gear_mold(world,state,player))),
            "4A05549794AC770B:mob_grinding_utils:golden_egg:5333762343701346059": lambda
                state: state.can_reach_location("31A6D9ACF02F1721:mob_grinding_utils:nutritious_chicken_feed:3577786290779658017"),
            "35FB3DDDD991DB3E:mob_grinding_utils:gm_chicken_feed_cursed:3889770726211836734": lambda
                state: state.can_reach_location("4B2825C257986EF8:mob_grinding_utils:absorption_hopper:5415620068536512248")
                        and ((state.can_reach_location("7AC647D823CD6523:immersiveengineering:light_engineering:8846837511655089443")
                        and state.can_reach_location("4B61E75F57941931:immersiveengineering:steel_scaffolding_standard:5431877022262761777"))
                             or (has_thermal_machine_frame(world,state,player) and has_gear_mold(world,state,player))),
            "04CD02B4D3E60A08:mob_grinding_utils:rotten_egg:345935722049833480": lambda
                state: state.can_reach_location("35FB3DDDD991DB3E:mob_grinding_utils:gm_chicken_feed_cursed:3889770726211836734"),
            "0E5632983BB97532:mob_grinding_utils:saw:1033068793946535218": lambda
                state: state.can_reach_location("252FF7E709D75DBB:mob_grinding_utils:spikes:2679632874983349691"),
            "47FCC3324190FA2A:mob_grinding_utils:saw_upgrade_fire:5187235491439770154": lambda
                state: state.can_reach_location("0E5632983BB97532:mob_grinding_utils:saw:1033068793946535218")
                        and has_gold_ingots(world,state,player),
            "570BF316442B3B31:mob_grinding_utils:saw_upgrade_smite:6272374183002061617": lambda
                state: state.can_reach_location("0E5632983BB97532:mob_grinding_utils:saw:1033068793946535218")
                        and has_gold_ingots(world,state,player),
            "3827000B3451BAD7:mob_grinding_utils:saw_upgrade_arthropod:4046202838338091735": lambda
                state: state.can_reach_location("0E5632983BB97532:mob_grinding_utils:saw:1033068793946535218")
                        and has_gold_ingots(world,state,player),
            "7854EB31D875B927:mob_grinding_utils:saw_upgrade_sharpness:8670813781912566055": lambda
                state: state.can_reach_location("0E5632983BB97532:mob_grinding_utils:saw:1033068793946535218")
                        and has_gold_ingots(world,state,player),
            "221B5FD698E5AF4A:mob_grinding_utils:saw_upgrade_looting:2457663396953567050": lambda
                state: state.can_reach_location("0E5632983BB97532:mob_grinding_utils:saw:1033068793946535218")
                        and has_gold_ingots(world,state,player),
            "7FDCFD25D848F2C7:mob_grinding_utils:saw_upgrade_beheading:9213517276677468871": lambda
                state: state.can_reach_location("0E5632983BB97532:mob_grinding_utils:saw:1033068793946535218")
                        and has_gold_ingots(world,state,player),
            "18A1A7997D19A8F2:mob_grinding_utils:fan_upgrade_height:1774884005831354610": lambda
                state: state.can_reach_location("4BE855C08DE7BDC4:mob_grinding_utils:fan:5469716032944324036"),
            "2D42B0ECBDAA096C:mob_grinding_utils:fan_upgrade_width:3261363611010468204": lambda
                state: state.can_reach_location("4BE855C08DE7BDC4:mob_grinding_utils:fan:5469716032944324036"),
            "65516A8FE8B185F1:mob_grinding_utils:fan_upgrade_speed:7300733637261100529": lambda
                state: state.can_reach_location("4BE855C08DE7BDC4:mob_grinding_utils:fan:5469716032944324036"),

            # Gamma
            "418CF7FDF846BE84:storagedrawers:oak_full_drawers_1:4723422779368980100": lambda
                state: state.can_reach_location("3EE16F0264052C50:Getting Started:4531024756170107984"),
            "755ABBE38C75AE31:ironchests:copper_chest:8456277836330020401": lambda
                state: state.can_reach_location("3EE16F0264052C50:Getting Started:4531024756170107984"),

            # Epsilon
            "304C3DA255E8BEA1:enderio:basic_capacitor:3480224379485863585": lambda
                state: state.can_reach_location("3EE16F0264052C50:Getting Started:4531024756170107984")
                       and has_copper_ingots(world, state, player),

            #Zeta
            "5D7D2A4C3BA37750:Into the Aether:6736587124522579792": lambda state: state.can_reach_location(
                "3EE16F0264052C50:Getting Started:4531024756170107984"),
            "77F0DF050A474878:Into the Twilight Forest:8642652897664256120": lambda state: state.can_reach_location(
                "3EE16F0264052C50:Getting Started:4531024756170107984"),
            "3C93642728A0CAAA:Into the Undergarden:4364942583200271018": lambda
                state: state.can_reach_location("3EE16F0264052C50:Getting Started:4531024756170107984"),
            "403922E054130670:Into the Nether:4627768438978446960": lambda
                state: state.can_reach_location("3EE16F0264052C50:Getting Started:4531024756170107984"),

            # Zeta
            "0754204BD1B84C6E:chunkloaders:basic_chunk_loader:528082566322343022": lambda
                state: state.can_reach_location("3EE16F0264052C50:Getting Started:4531024756170107984"),

            # Eta
            "6450516E0A3A74DF:mekanism:ingot_osmium:7228366934989501663": lambda
                state: state.can_reach_location("3EE16F0264052C50:Getting Started:4531024756170107984")
                       and has_osmium_ingots(world, state, player),

            # Theta
            "6EB5A813D4088C7E:botania:lexicon:7977467118071876734": lambda state: state.can_reach_location(
                "3EE16F0264052C50:Getting Started:4531024756170107984"),

            # Iota
            "3CE059588A2A9A97:patchouli:guide_book:4386604273868905111": lambda state: state.can_reach_location(
                "3EE16F0264052C50:Getting Started:4531024756170107984"),

            # Kappa
            "1BBAE3C2176C6BA6:Engineer's Tools:1998159807448378278": lambda
                state: state.can_reach_location("3EE16F0264052C50:Getting Started:4531024756170107984")
                        and has_iron_ingots(world, state, player) and has_copper_ingots(world, state, player),
            "7CE3C90007447787:Thermal Series:8999257482375493511": lambda state: state.can_reach_location(
                "3EE16F0264052C50:Getting Started:4531024756170107984")
                        and has_iron_ingots(world, state,player),

            # Lambda
            "61764BC9112A7918:patchouli:guide_book:7022883995879373080": lambda state: state.can_reach_location(
                "3EE16F0264052C50:Getting Started:4531024756170107984"),
            "70A23413D989C094:hangglider:hang_glider:8116106738333761684": lambda
                state: state.can_reach_location("3EE16F0264052C50:Getting Started:4531024756170107984")
                       and has_iron_ingots(world, state, player),

            # Delta
            "17DCD0325F76FF0C:mysticalagriculture:inferium_essence:1719478072517263116": lambda
                state: state.can_reach_location("3EE16F0264052C50:Getting Started:4531024756170107984"),

            # Mu
            "4F263B60E4157BCA:constructionwand:stone_wand:5703311265440824266": lambda state: state.can_reach_location(
                "3EE16F0264052C50:Getting Started:4531024756170107984"),
            "0226202FC2B70325:constructionwand:iron_wand:154846626693186341": lambda
                state: state.can_reach_location("4F263B60E4157BCA:constructionwand:stone_wand:5703311265440824266")
                       and has_iron_ingots(world, state, player),
            "66EB0CF3E7120F96:constructionwand:diamond_wand:7416035453088960406": lambda
                state: state.can_reach_location("0226202FC2B70325:constructionwand:iron_wand:154846626693186341"),
            "0B4FE52E8C83C177:constructionwand:infinity_wand:815122045666050423": lambda
                state: state.can_reach_location("66EB0CF3E7120F96:constructionwand:diamond_wand:7416035453088960406"),
            "08C08FE6676AF787:constructionwand:core_angel:630662167572182919": lambda
                state: state.can_reach_location("0B4FE52E8C83C177:constructionwand:infinity_wand:815122045666050423")
                       and has_gold_ingots(world, state, player),
            "17E5A5A650EC804A:constructionwand:core_destruction:1721964566279913546": lambda
                state: state.can_reach_location("0B4FE52E8C83C177:constructionwand:infinity_wand:815122045666050423"),

            # Nu
            "089F8808A64381C3:powah:book:621364844330975683": lambda state: state.can_reach_location(
                "3EE16F0264052C50:Getting Started:4531024756170107984"),

            # Xi
            "7D8D05F2066559D6:mekanismtools:wood_paxel:9046893763504724438": lambda state: state.can_reach_location(
                "3EE16F0264052C50:Getting Started:4531024756170107984"),
            "3E9ACFA8AF8D7DA5:betterfurnacesreforged:copper_furnace:4511146300171713957": lambda
                state: state.can_reach_location("3EE16F0264052C50:Getting Started:4531024756170107984")
                       and has_copper_ingots(world, state, player),

            # Omicron
            "0632775165BACE5A:bigreactors:graphite_ingot:446550504545898074": lambda state: state.can_reach_location(
                "3EE16F0264052C50:Getting Started:4531024756170107984"),
            "56269978214E1D5A:patchouli:guide_book:6207817877610700122": lambda state:
            state.can_reach_location("3EE16F0264052C50:Getting Started:4531024756170107984")
            and state.can_reach_location("74076796EE6A84BE:bigreactors:yellorium_ingot:8360765131179328702"),
            "74076796EE6A84BE:bigreactors:yellorium_ingot:8360765131179328702": lambda state:
            state.can_reach_location("0632775165BACE5A:bigreactors:graphite_ingot:446550504545898074"),

            # Pi
            "47686031CE8F3478:pneumaticcraft:ingot_iron_compressed:5145468341305947256": lambda
                state: state.can_reach_location("3EE16F0264052C50:Getting Started:4531024756170107984")
                       and has_iron_ingots(world, state, player),
            #Rho

            # Sigma


            # Tau
            "556A26FD1821B382:solarflux:sp_1:6154774709228647298": lambda
                state: state.can_reach_location("3EE16F0264052C50:Getting Started:4531024756170107984")
                       and has_redstone_alloy_ingots(world, state, player),

            # Upsilon


            # Phi


            # Chi


            # Psi

            # Omega
            "546C44F3B917BB85:Creative Items:6083313010243779461": lambda state: state.can_reach_location(
                "3EE16F0264052C50:Getting Started:4531024756170107984"),

            "": lambda
                state: state.can_reach_location(""),
            "": lambda
                state: state.can_reach_location(""),
            "": lambda
                state: state.can_reach_location(""),
            "": lambda
                state: state.can_reach_location(""),
            "": lambda
                state: state.can_reach_location(""),
            "": lambda
                state: state.can_reach_location(""),
            "": lambda
                state: state.can_reach_location(""),
            "": lambda
                state: state.can_reach_location(""),
            "": lambda
                state: state.can_reach_location(""),
        }
    }
    return rules_lookup


def set_rules(self: "MinecraftOsrWorld") -> None:
    multiworld = self.multiworld
    player = self.player

    rules_lookup = get_rules_lookup(self, player)

    # Set entrance rules
    for entrance_name, rule in rules_lookup["entrances"].items():
        multiworld.get_entrance(entrance_name, player).access_rule = rule

    # Set location rules
    for location_name, rule in rules_lookup["locations"].items():
        multiworld.get_location(location_name, player).access_rule = rule

    goal = self.options.quest_goal

    def location_count(state: CollectionState) -> int:
        return len([location for location in multiworld.get_locations(player) if
                    location.address is not None and
                    location.can_reach(state)])

    completion_requirements = lambda state: (location_count(state) >= self.options.quest_goal
                                             and state.has("Dragon Egg Shard", player))
    multiworld.completion_condition[player] = lambda state: completion_requirements(state)
