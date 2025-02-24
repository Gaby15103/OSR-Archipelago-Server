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
    return state.has("netherite ingot", player) and state.can_reach_location("403922E054130670:Into the Nether:4627768438978446960", player)

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
    return state.has("soularium ingot", player)

def has_gear_mold(world: "MinecraftOsrWorld", state: CollectionState, player: int) -> bool:
    return state.has("gear mold", player)

def has_infusion_crystal(world: "MinecraftOsrWorld", state: CollectionState, player: int) -> bool:
    return state.has("infusion_crystal", player)

def has_master_infusion_crystal(world: "MinecraftOsrWorld", state: CollectionState, player: int) -> bool:
    return state.has("master infusion crystal", player)

def has_black_iron_ingot(world: "MinecraftOsrWorld", state: CollectionState, player: int) -> bool:
    return state.has("black iron ingot", player)

def has_basic_crafting_table(world: "MinecraftOsrWorld", state: CollectionState, player: int) -> bool:
    return state.has("basic crafting table", player) and has_black_iron_ingot(world,state,player)

def has_inferium_growth_accelerator(world: "MinecraftOsrWorld", state: CollectionState, player: int) -> bool:
    return state.has("inferium growth accelerator", player)

def has_prudentium_growth_accelerator(world: "MinecraftOsrWorld", state: CollectionState, player: int) -> bool:
    return state.has("prudentium growth accelerator", player)

def has_tertium_growth_accelerator(world: "MinecraftOsrWorld", state: CollectionState, player: int) -> bool:
    return state.has("tertium growth accelerator", player)

def has_imperium_growth_accelerator(world: "MinecraftOsrWorld", state: CollectionState, player: int) -> bool:
    return state.has("imperium growth accelerator", player)

def has_supremium_growth_accelerator(world: "MinecraftOsrWorld", state: CollectionState, player: int) -> bool:
    return state.has("supremium growth accelerator", player)

def has_electrum_ingot(world: "MinecraftOsrWorld", state: CollectionState, player: int) -> bool:
    return state.has("electrum ingot", player)

def has_end_steel_ingot(world: "MinecraftOsrWorld", state: CollectionState, player: int) -> bool:
    return state.has("end steel ingot", player)

def has_vibrant_alloy_ingot(world: "MinecraftOsrWorld", state: CollectionState, player: int) -> bool:
    return state.has("vibrant alloy ingot", player)

def has_enderium_ingot(world: "MinecraftOsrWorld", state: CollectionState, player: int) -> bool:
    return state.has("enderium ingot", player)

def has_awakned_draconium(world: "MinecraftOsrWorld", state: CollectionState, player: int) -> bool:
    return state.has("awakned draconium", player)

def has_neutronium_ingot(world: "MinecraftOsrWorld", state: CollectionState, player: int) -> bool:
    return state.has("neutronium ingot", player)

def has_energetic_alloy_ingot(world: "MinecraftOsrWorld", state: CollectionState, player: int) -> bool:
    return state.has("energetic alloy ingot", player)

def has_steel_ingot(world: "MinecraftOsrWorld", state: CollectionState, player: int) -> bool:
    return state.has("steel ingot", player)

def has_pulsating_alloy_ingot(world: "MinecraftOsrWorld", state: CollectionState, player: int) -> bool:
    return state.has("pulsating alloy ingot", player)
# COPPER ALLOY NEED COPPER
def has_copper_alloy_ingot(world: "MinecraftOsrWorld", state: CollectionState, player: int) -> bool:
    return state.has("copper alloy ingot", player)

def has_tesseract(world: "MinecraftOsrWorld", state: CollectionState, player: int) -> bool:
    return state.has("tesseract", player)

def has_ender_ingot(world: "MinecraftOsrWorld", state: CollectionState, player: int) -> bool:
    return state.has("ender ingot", player)

def has_invar_ingot(world: "MinecraftOsrWorld", state: CollectionState, player: int) -> bool:
    return state.has("invar ingot", player)

def has_signalum_ingot(world: "MinecraftOsrWorld", state: CollectionState, player: int) -> bool:
    return state.has("signalum ingot", player)

def has_lumium_ingot(world: "MinecraftOsrWorld", state: CollectionState, player: int) -> bool:
    return state.has("lumium ingot", player)



def get_rules_lookup(world, player: int):
    rules_lookup = {
        "entrances": {
            "Nether Portal": lambda state: state.can_reach_location("4632C8C4F1622D5D:Into the End:5058326079679376733"),
            "End Portal": lambda state: enter_stronghold(world, state, player)
                                        and state.has('3 Ender Pearls', player, 4),
            "Overworld Structure 1": lambda state: can_adventure(world, state, player)
                                                   and has_structure_compass(world, state, "Overworld Structure 1",
                                                                             player),
            "Overworld Structure 2": lambda state: can_adventure(world, state, player)
                                                   and has_structure_compass(world, state, "Overworld Structure 2",
                                                                             player),
            "Nether Structure 1": lambda state: can_adventure(world, state, player)
                                                and has_structure_compass(world, state, "Nether Structure 1", player),
            "Nether Structure 2": lambda state: can_adventure(world, state, player)
                                                and has_structure_compass(world, state, "Nether Structure 2", player),
            "The End Structure": lambda state: can_adventure(world, state, player)
                                               and has_structure_compass(world, state, "The End Structure", player),
        },
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
                             (has_soulium_ingot(world,state,player) and state.can_reach_location("403922E054130670:Into the Nether:4627768438978446960"))),

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
            "29AE56F399A8006A:storagedrawers:obsidian_storage_upgrade:3003433605757665386": lambda
                state: state.can_reach_location("418CF7FDF846BE84:storagedrawers:oak_full_drawers_1:4723422779368980100"),
            "6C87B43D15407718:storagedrawers:iron_storage_upgrade:7820417452394706712": lambda
                state: state.can_reach_location("29AE56F399A8006A:storagedrawers:obsidian_storage_upgrade:3003433605757665386")
                        and has_iron_ingots(world,state,player),
            "502368BBB9DF42A3:storagedrawers:gold_storage_upgrade:5774574302705697443": lambda
                state: state.can_reach_location("6C87B43D15407718:storagedrawers:iron_storage_upgrade:7820417452394706712")
                        and has_gold_ingots(world,state,player),
            "27D0E09429A5BC58:storagedrawers:diamond_storage_upgrade:2869039889593515096": lambda
                state: state.can_reach_location("502368BBB9DF42A3:storagedrawers:gold_storage_upgrade:5774574302705697443"),
            "51ADDE07480D68C7:storagedrawers:emerald_storage_upgrade:5885604410898081991": lambda
                state: state.can_reach_location("27D0E09429A5BC58:storagedrawers:diamond_storage_upgrade:2869039889593515096"),
            "5C7DC5405B9EAA96:storagedrawers:void_upgrade:6664699903783905942": lambda
                state: state.can_reach_location("51ADDE07480D68C7:storagedrawers:emerald_storage_upgrade:5885604410898081991"),
            "59F498EBB5FE2C2C:storagedrawers:compacting_drawers_3:6481973901831056428": lambda
                state: state.can_reach_location("418CF7FDF846BE84:storagedrawers:oak_full_drawers_1:4723422779368980100")
                        and has_iron_ingots(world,state,player),
            "4A224F9E3C15B5C8:storagedrawers:controller:5341919649046312392": lambda
                state: state.can_reach_location("59F498EBB5FE2C2C:storagedrawers:compacting_drawers_3:6481973901831056428")
                        and has_redstone_alloy_ingots(world,state,player),
            "3D181D1398577D0E:storagedrawers:controller_slave:4402300605752114446": lambda
                state: state.can_reach_location("4A224F9E3C15B5C8:storagedrawers:controller:5341919649046312392")
                        and has_gold_ingots(world,state,player),
            "2249AFBFF8152AC5:storagedrawers:drawer_key:2470699109625178821": lambda
                state: state.can_reach_location("418CF7FDF846BE84:storagedrawers:oak_full_drawers_1:4723422779368980100")
                        and has_gold_ingots(world,state,player),
            "769DBFCAAF546990:storagedrawers:quantify_key:8547198545064913296": lambda
                state: state.can_reach_location("2249AFBFF8152AC5:storagedrawers:drawer_key:2470699109625178821"),
            "24226A5DB7C6CC00:storagedrawers:shroud_key:2603760485321329664": lambda
                state: state.can_reach_location("769DBFCAAF546990:storagedrawers:quantify_key:8547198545064913296"),
            "16B57C4BD4C33843:storagedrawers:oak_full_drawers_2:1636350704752998467": lambda
                state: state.can_reach_location("418CF7FDF846BE84:storagedrawers:oak_full_drawers_1:4723422779368980100"),
            "6042D5F44B5F0A5F:storagedrawers:oak_full_drawers_4:6936341621317241439": lambda
                state: state.can_reach_location("16B57C4BD4C33843:storagedrawers:oak_full_drawers_2:1636350704752998467"),
            "0D6E9FD75AE47D03:storagedrawers:oak_half_drawers_1:967886717222944003": lambda
                state: state.can_reach_location("6042D5F44B5F0A5F:storagedrawers:oak_full_drawers_4:6936341621317241439"),
            "5EFC686F406A2689:storagedrawers:oak_half_drawers_2:6844460360727668361": lambda
                state: state.can_reach_location("0D6E9FD75AE47D03:storagedrawers:oak_half_drawers_1:967886717222944003"),
            "7C7DD6CC1A5E66F4:storagedrawers:oak_half_drawers_4:8970562204895962868": lambda
                state: state.can_reach_location("5EFC686F406A2689:storagedrawers:oak_half_drawers_2:6844460360727668361"),
            "561A5FF8F7E1F164:ironchests:iron_chest:6204376959571587428": lambda
                state: state.can_reach_location("755ABBE38C75AE31:ironchests:copper_chest:8456277836330020401")
                        and has_iron_ingots(world,state,player),
            "41D57481AD08B1C4:ironchests:gold_chest:4743825882807316932": lambda
                state: state.can_reach_location("561A5FF8F7E1F164:ironchests:iron_chest:6204376959571587428")
                        and has_gold_ingots(world,state,player),
            "69021BE4507E3022:ironchests:diamond_chest:7566640991352795170": lambda
                state: state.can_reach_location("41D57481AD08B1C4:ironchests:gold_chest:4743825882807316932"),
            "2297686A02AF6553:ironchests:obsidian_chest:2492575723293730131": lambda
                state: state.can_reach_location("69021BE4507E3022:ironchests:diamond_chest:7566640991352795170"),
            "345C7F6955DCBF95:ironchests:netherite_chest:3773030678218456981": lambda
                state: state.can_reach_location("2297686A02AF6553:ironchests:obsidian_chest:2492575723293730131")
                        and has_netherite_ingots(world,state,player),

            # Delta
            "17DCD0325F76FF0C:mysticalagriculture:inferium_essence:1719478072517263116": lambda
                state: state.can_reach_location("3EE16F0264052C50:Getting Started:4531024756170107984"),
            "1FB5B6707BBFB0CC:mysticalagriculture: prudentium_essence:2284932980189147340": lambda
                state: state.can_reach_location("17DCD0325F76FF0C:mysticalagriculture:inferium_essence:1719478072517263116")
                        and state.can_reach_location("00C14C1B77ACFCD2:mysticalagriculture:infusion_crystal:54408351360810194"),
            "6B1A8D1CE3D65BA0:mysticalagriculture:tertium_essence:7717636066673843104": lambda
                state: state.can_reach_location("1FB5B6707BBFB0CC:mysticalagriculture: prudentium_essence:2284932980189147340"),
            "1111A4212E59B734:mysticalagriculture:imperium_essence:1229944635667363636": lambda
                state: state.can_reach_location("6B1A8D1CE3D65BA0:mysticalagriculture:tertium_essence:7717636066673843104"),
            "4DCF187529D58214:mysticalagriculture:supremium_essence:5606726952591655444": lambda
                state: state.can_reach_location("1111A4212E59B734:mysticalagriculture:imperium_essence:1229944635667363636"),
            "29A2B58D200D65F9:mysticalagriculture:awakened_supremium_essence:3000159919514936825": lambda
                state: state.can_reach_location("4DCF187529D58214:mysticalagriculture:supremium_essence:5606726952591655444")
                        and has_gold_ingots(world,state,player) and state.can_reach_location("403922E054130670:Into the Nether:4627768438978446960")
                        and state.can_reach_location("574E54FFCA5C2F39:extendedcrafting:basic_table:6291059187071594297")
                        and state.can_reach_location("4140645DC360472A:Enchanter:4701868364847400746")
                        and state.can_reach_location("29E40CD5EF7495FB:mysticalagriculture:nether_star_seeds:3018551763230037499"),
            "60665C65C798C959:mysticalagradditions:insanium_essence:6946341067475700057": lambda
                state: state.can_reach_location("4DCF187529D58214:mysticalagriculture:supremium_essence:5606726952591655444"),
            "27E92F9CAD2E8201:mysticalagriculture:inferium_furnace:2875882187019682305": lambda
                state: state.can_reach_location("17DCD0325F76FF0C:mysticalagriculture:inferium_essence:1719478072517263116"),
            "29631AAEB3EE862C:mysticalagriculture:prudentium_furnace:2982256715894785580": lambda
                state: state.can_reach_location("27E92F9CAD2E8201:mysticalagriculture:inferium_furnace:2875882187019682305")
                        and state.can_reach_location("1FB5B6707BBFB0CC:mysticalagriculture: prudentium_essence:2284932980189147340"),
            "73E0BFE574AB4221:mysticalagriculture:tertium_furnace:8349884701370696225": lambda
                state: state.can_reach_location("29631AAEB3EE862C:mysticalagriculture:prudentium_furnace:2982256715894785580")
                        and state.can_reach_location("6B1A8D1CE3D65BA0:mysticalagriculture:tertium_essence:7717636066673843104"),
            "0FE358C58400C6A0:mysticalagriculture:imperium_furnace:1144856335628682912": lambda
                state: state.can_reach_location("73E0BFE574AB4221:mysticalagriculture:tertium_furnace:8349884701370696225")
                        and state.can_reach_location("1111A4212E59B734:mysticalagriculture:imperium_essence:1229944635667363636"),
            "3FEBBF71D957867B:mysticalagriculture:supremium_furnace:4605985539615065723": lambda
                state: state.can_reach_location("0FE358C58400C6A0:mysticalagriculture:imperium_furnace:1144856335628682912")
                        and state.can_reach_location("4DCF187529D58214:mysticalagriculture:supremium_essence:5606726952591655444"),
            "0F7268F1692BA6DD:mysticalagriculture:awakened_supremium_furnace:1113067443974809309": lambda
                state: state.can_reach_location("3FEBBF71D957867B:mysticalagriculture:supremium_furnace:4605985539615065723")
                        and state.can_reach_location("29A2B58D200D65F9:mysticalagriculture:awakened_supremium_essence:3000159919514936825"),
            "12F74E49F266865A:mysticalagriculture:inferium_chestplate:1366647091436619354": lambda
                state: state.can_reach_location("17DCD0325F76FF0C:mysticalagriculture:inferium_essence:1719478072517263116"),
            "1F8E2FAFA333804D:mysticalagriculture:prudentium_chestplate:2273807293272522829": lambda
                state: state.can_reach_location("12F74E49F266865A:mysticalagriculture:inferium_chestplate:1366647091436619354")
                        and state.can_reach_location("1FB5B6707BBFB0CC:mysticalagriculture: prudentium_essence:2284932980189147340"),
            "74A2874A636757AA:mysticalagriculture:tertium_chestplate:8404428608191813546": lambda
                state: state.can_reach_location("1F8E2FAFA333804D:mysticalagriculture:prudentium_chestplate:2273807293272522829")
                        and state.can_reach_location("6B1A8D1CE3D65BA0:mysticalagriculture:tertium_essence:7717636066673843104"),
            "7FF2C44C6839D48C:mysticalagriculture:imperium_chestplate:9219647219626005644": lambda
                state: state.can_reach_location("74A2874A636757AA:mysticalagriculture:tertium_chestplate:8404428608191813546")
                        and state.can_reach_location("1111A4212E59B734:mysticalagriculture:imperium_essence:1229944635667363636"),
            "6E285CDF62E9EBB8:mysticalagriculture:supremium_chestplate:7937696457747459000": lambda
                state: state.can_reach_location("7FF2C44C6839D48C:mysticalagriculture:imperium_chestplate:9219647219626005644")
                        and state.can_reach_location("4DCF187529D58214:mysticalagriculture:supremium_essence:5606726952591655444"),
            "40812D2012C3068B:mysticalagriculture:awakened_supremium_chestplate:4648045906200037003": lambda
                state: state.can_reach_location("6E285CDF62E9EBB8:mysticalagriculture:supremium_chestplate:7937696457747459000")
                        and state.can_reach_location("29A2B58D200D65F9:mysticalagriculture:awakened_supremium_essence:3000159919514936825"),
            "2613CCF6E2B3A19F:mysticalagriculture:inferium_growth_accelerator:2743761958736208287": lambda
                state: state.can_reach_location("17DCD0325F76FF0C:mysticalagriculture:inferium_essence:1719478072517263116")
                        and has_inferium_growth_accelerator(world,state,player),
            "6D3E1A586AB3F99A:mysticalagriculture:prudentium_growth_accelerator:7871758165739829658": lambda
                state: state.can_reach_location("2613CCF6E2B3A19F:mysticalagriculture:inferium_growth_accelerator:2743761958736208287")
                        and has_prudentium_growth_accelerator(world,state,player),
            "034786603D7FDD18:mysticalagriculture:tertium_growth_accelerator:236305253367012632": lambda
                state: state.can_reach_location("6D3E1A586AB3F99A:mysticalagriculture:prudentium_growth_accelerator:7871758165739829658")
                        and has_tertium_growth_accelerator(world,state,player),
            "5B196B44909E59C9:mysticalagriculture:imperium_growth_accelerator:6564395874097453513": lambda
                state: state.can_reach_location("034786603D7FDD18:mysticalagriculture:tertium_growth_accelerator:236305253367012632")
                        and has_imperium_growth_accelerator(world,state,player),
            "7041A7651D54436A:mysticalagriculture:supremium_growth_accelerator:8088930458459718506": lambda
                state: state.can_reach_location("5B196B44909E59C9:mysticalagriculture:imperium_growth_accelerator:6564395874097453513")
                        and has_supremium_growth_accelerator(world,state,player),
            "24DBF5D8CCA1CE79:Basic Watering Can:2655986716759936633": lambda
                state: state.can_reach_location("2613CCF6E2B3A19F:mysticalagriculture:inferium_growth_accelerator:2743761958736208287")
                        and has_iron_ingots(world,state,player),
            "413D5F6672C5B552:Sprinklers!:4701018479661528402": lambda
                state: state.can_reach_location("24DBF5D8CCA1CE79:Basic Watering Can:2655986716759936633")
                        and has_electrum_ingot(world,state,player),
            "3FA2C4EFEA686EF2:botanypots:terracotta_botany_pot:4585443905325526770": lambda
                state: state.can_reach_location("413D5F6672C5B552:Sprinklers!:4701018479661528402")
                        and state.can_reach_location("60665C65C798C959:mysticalagradditions:insanium_essence:6946341067475700057"),
            "7CA502DB7EC311B0:patchouli:guide_book:8981588173608128944": lambda
                state: state.can_reach_location("17DCD0325F76FF0C:mysticalagriculture:inferium_essence:1719478072517263116"),
            "12612B561581014B:mysticalagriculture:prosperity_shard:1324387414151594315": lambda
                state: state.can_reach_location("7CA502DB7EC311B0:patchouli:guide_book:8981588173608128944")
                        and state.can_reach_location("17DCD0325F76FF0C:mysticalagriculture:inferium_essence:1719478072517263116"),
            "00C14C1B77ACFCD2:mysticalagriculture:infusion_crystal:54408351360810194": lambda
                state: state.can_reach_location("12612B561581014B:mysticalagriculture:prosperity_shard:1324387414151594315")
                        and state.can_reach_location("17DCD0325F76FF0C:mysticalagriculture:inferium_essence:1719478072517263116")
                        and has_infusion_crystal(world,state,player),
            "56CC6260E5B09B5A:mysticalagriculture:master_infusion_crystal:6254482150820715354": lambda
                state: state.can_reach_location("00C14C1B77ACFCD2:mysticalagriculture:infusion_crystal:54408351360810194")
                        and has_master_infusion_crystal(world,state,player),
            "04846D1F54DF981C:mysticalagriculture:infusion_altar:325505054412871708": lambda
                state: state.can_reach_location("7CA502DB7EC311B0:patchouli:guide_book:8981588173608128944")
                        and has_gold_ingots(world,state,player),
            "2CB97A9EECD58E88:mysticalagriculture:seed_reprocessor:3222741831357140616": lambda
                state: state.can_reach_location("04846D1F54DF981C:mysticalagriculture:infusion_altar:325505054412871708")
                        and has_iron_ingots(world,state,player) and has_soulium_ingot(world,state,player)
                        and has_redstone_ingot(world,state,player) and has_thermal_machine_frame(world,state,player),
            "6543E32C66892345:mysticalagriculture:tinkering_table:7296925601108665157": lambda
                state: state.can_reach_location("2CB97A9EECD58E88:mysticalagriculture:seed_reprocessor:3222741831357140616")
                        and state.can_reach_location("403922E054130670:Into the Nether:4627768438978446960"),
            "5C9ECD8109413F70:mysticalagriculture:flight_augment:6673997651899400048": lambda
                state: state.can_reach_location("6543E32C66892345:mysticalagriculture:tinkering_table:7296925601108665157")
                        and state.can_reach_location("4DCF187529D58214:mysticalagriculture:supremium_essence:5606726952591655444"),
            "0AC66AFEA56D0F81:mysticalagriculture:air_seeds:776425627697614721": lambda
                state: state.can_reach_location("04846D1F54DF981C:mysticalagriculture:infusion_altar:325505054412871708"),
            "7E31F38928E965F2:mysticalagriculture:earth_seeds:9093316893060195826": lambda
                state: state.can_reach_location("04846D1F54DF981C:mysticalagriculture:infusion_altar:325505054412871708"),
            "09999790B789A604:mysticalagriculture:water_seeds:691750665588418052": lambda
                state: state.can_reach_location("04846D1F54DF981C:mysticalagriculture:infusion_altar:325505054412871708"),
            "19297AF6271B1473:mysticalagriculture:fire_seeds:1813115522629964915": lambda
                state: state.can_reach_location("04846D1F54DF981C:mysticalagriculture:infusion_altar:325505054412871708"),
            "21EBF76CE1C8DD44:mysticalagriculture:end_steel_seeds:2444319269795192132": lambda
                state: state.can_reach_location("04846D1F54DF981C:mysticalagriculture:infusion_altar:325505054412871708")
                        and has_end_steel_ingot(world,state,player)
                        and state.can_reach_location("4DCF187529D58214:mysticalagriculture:supremium_essence:5606726952591655444"),
            "4AE8A5DD70731DC5:mysticalagriculture:vibrant_alloy_seeds:5397746523896487365": lambda
                state: state.can_reach_location("04846D1F54DF981C:mysticalagriculture:infusion_altar:325505054412871708")
                        and has_vibrant_alloy_ingot(world,state,player)
                        and state.can_reach_location("4DCF187529D58214:mysticalagriculture:supremium_essence:5606726952591655444"),
            "3D514FFE4B4FABD0:mysticalagriculture:uraninite_seeds:4418400663030967248": lambda
                state: state.can_reach_location("04846D1F54DF981C:mysticalagriculture:infusion_altar:325505054412871708")
                        and state.can_reach_location("4DCF187529D58214:mysticalagriculture:supremium_essence:5606726952591655444"),
            "488BE929D223408C:mysticalagriculture:enderium_seeds:5227528158322049164": lambda
                state: state.can_reach_location("04846D1F54DF981C:mysticalagriculture:infusion_altar:325505054412871708")
                        and has_enderium_ingot(world,state,player)
                        and state.can_reach_location("4DCF187529D58214:mysticalagriculture:supremium_essence:5606726952591655444"),
            "645144B65DD8C33D:mysticalagriculture:diamond_seeds:7228634426955580221": lambda
                state: state.can_reach_location("04846D1F54DF981C:mysticalagriculture:infusion_altar:325505054412871708")
                        and state.can_reach_location("4DCF187529D58214:mysticalagriculture:supremium_essence:5606726952591655444"),
            "1BBED5317DB102D4:mysticalagriculture:niotic_crystal_seeds:1999269693137945300": lambda
                state: state.can_reach_location("04846D1F54DF981C:mysticalagriculture:infusion_altar:325505054412871708")
                        and state.can_reach_location("4DCF187529D58214:mysticalagriculture:supremium_essence:5606726952591655444"),
            "721DE48EB10F97EE:mysticalagriculture:netherite_seeds:8222979796155471854": lambda
                state: state.can_reach_location("04846D1F54DF981C:mysticalagriculture:infusion_altar:325505054412871708")
                        and has_netherite_ingots(world,state,player)
                        and state.can_reach_location("4DCF187529D58214:mysticalagriculture:supremium_essence:5606726952591655444"),
            "4C4BFB01B08B9B41:mysticalagriculture:flux_infused_gem_seeds:5497763754811300673": lambda
                state: state.can_reach_location("04846D1F54DF981C:mysticalagriculture:infusion_altar:325505054412871708")
                        and state.can_reach_location("4DCF187529D58214:mysticalagriculture:supremium_essence:5606726952591655444"),
            "626FBCC4BE843CEB:mysticalagriculture:wither_skeleton_seeds:7093095491327769835": lambda
                state: state.can_reach_location("04846D1F54DF981C:mysticalagriculture:infusion_altar:325505054412871708")
                        and state.can_reach_location("4DCF187529D58214:mysticalagriculture:supremium_essence:5606726952591655444")
                        and state.can_reach_region('The Nether', player),
            "3BFF866B32E6FD5A:mysticalagriculture:spirited_crystal_seeds:4323321962272587098": lambda
                state: state.can_reach_location("04846D1F54DF981C:mysticalagriculture:infusion_altar:325505054412871708")
                        and state.can_reach_location("4DCF187529D58214:mysticalagriculture:supremium_essence:5606726952591655444"),
            "10AB6EF714EC6571:mysticalagriculture:emerald_seeds:1201175733111383409": lambda
                state: state.can_reach_location("04846D1F54DF981C:mysticalagriculture:infusion_altar:325505054412871708")
                        and state.can_reach_location("4DCF187529D58214:mysticalagriculture:supremium_essence:5606726952591655444"),
            "2DF4726B8D54971D:mysticalagriculture:yellorium_seeds:3311397432282355485": lambda
                state: state.can_reach_location("04846D1F54DF981C:mysticalagriculture:infusion_altar:325505054412871708")
                        and state.can_reach_location("4DCF187529D58214:mysticalagriculture:supremium_essence:5606726952591655444")
                        and state.can_reach_location("74076796EE6A84BE:bigreactors:yellorium_ingot:8360765131179328702"),
            "6B30912D3790F068:mysticalagriculture:nitro_crystal_seeds:7723832984332202088": lambda
                state: state.can_reach_location("04846D1F54DF981C:mysticalagriculture:infusion_altar:325505054412871708")
                        and state.can_reach_location("60665C65C798C959:mysticalagradditions:insanium_essence:6946341067475700057"),
            "631886694B190186:mysticalagriculture:gaia_spirit_seeds:7140604995985539462": lambda
                state: state.can_reach_location("04846D1F54DF981C:mysticalagriculture:infusion_altar:325505054412871708")
                        and state.can_reach_location("60665C65C798C959:mysticalagradditions:insanium_essence:6946341067475700057")
                        and state.can_reach_location("79E30F3A54F84EA4:botania:gaia_ingot:8782880441510678180"),
            "1F2933C86F227F89:mysticalagriculture:awakened_draconium_seeds:2245382825171910537": lambda
                state: state.can_reach_location("04846D1F54DF981C:mysticalagriculture:infusion_altar:325505054412871708")
                        and state.can_reach_location("60665C65C798C959:mysticalagradditions:insanium_essence:6946341067475700057")
                        and has_awakned_draconium(world,state,player),
            "29E40CD5EF7495FB:mysticalagriculture:nether_star_seeds:3018551763230037499": lambda
                state: state.can_reach_location("04846D1F54DF981C:mysticalagriculture:infusion_altar:325505054412871708")
                        and state.can_reach_location("60665C65C798C959:mysticalagradditions:insanium_essence:6946341067475700057"),
            "0C20C02B76C10512:mysticalagriculture:dragon_egg_seeds:873909620618364178": lambda
                state: state.can_reach_location("04846D1F54DF981C:mysticalagriculture:infusion_altar:325505054412871708")
                        and state.can_reach_location("60665C65C798C959:mysticalagradditions:insanium_essence:6946341067475700057")
                        and state.can_reach_location("46F450DDEAECE702:minecraft:dragon_egg:5112800391031744258"),
            "28ADE47BE9ED4B9F:mysticalagriculture:neutronium_seeds:2931250153344813983": lambda
                state: state.can_reach_location("04846D1F54DF981C:mysticalagriculture:infusion_altar:325505054412871708")
                        and state.can_reach_location("60665C65C798C959:mysticalagradditions:insanium_essence:6946341067475700057")
                        and has_neutronium_ingot(world,state,player),


            # Epsilon
            "304C3DA255E8BEA1:enderio:basic_capacitor:3480224379485863585": lambda
                state: state.can_reach_location("3EE16F0264052C50:Getting Started:4531024756170107984")
                       and has_copper_ingots(world, state, player),
            "2AFC300B86665BAB:enderio: double_layer_capacitor:3097403469781687211": lambda
                state: state.can_reach_location("304C3DA255E8BEA1:enderio:basic_capacitor:3480224379485863585")
                        and has_energetic_alloy_ingot(world,state,player),
            "62DE39B1BEF752BA:enderio:octadic_capacitor:7124195096122577594": lambda
                state: state.can_reach_location("2AFC300B86665BAB:enderio: double_layer_capacitor:3097403469781687211")
                        and has_vibrant_alloy_ingot(world,state,player)
                        and state.can_reach_location("24F3DD2D706EBFB6:3x3 Pressure Chamber:2662714991935668150"),
            "4BB8FBE275D2AE7F:Pipez:5456387898617278079": lambda
                state: state.can_reach_location("304C3DA255E8BEA1:enderio:basic_capacitor:3480224379485863585")
                        and has_item_conduit(world,state,player) and has_fluid_conduit(world,state,player)
                        and has_steel_ingot(world,state,player),
            "599D753764477C22:Conduit Upgrades:6457446321485216802": lambda
                state: state.can_reach_location("304C3DA255E8BEA1:enderio:basic_capacitor:3480224379485863585")
                        and has_energetic_alloy_ingot(world,state,player) and has_redstone_ingot(world,state,player)
                        and has_iron_ingots(world,state,player) and has_redstone_alloy_ingots(world,state,player)
                        and has_conductive_alloy_ingots(world,state,player) and has_soularium_ingot(world,state,player)
                        and has_energetic_alloy_ingot(world,state,player)
                        and state.can_reach_location("236AB7E3C6AE1F38:enderio:slice_and_splice:2552054327777566520"),
            "6F25BC39A243FB15:enderio:basic_capacitor_bank:8009014468069817109": lambda
                state: state.can_reach_location("304C3DA255E8BEA1:enderio:basic_capacitor:3480224379485863585"),
            "6D75D785EB89AFAF:enderio:advanced_capacitor_bank:7887447292591583151": lambda
                state: state.can_reach_location("6F25BC39A243FB15:enderio:basic_capacitor_bank:8009014468069817109")
                        and state.can_reach_location("2AFC300B86665BAB:enderio: double_layer_capacitor:3097403469781687211"),
            "2B2FB3D50B29B04F:enderio:vibrant_capacitor_bank:3111903595132989519": lambda
                state: state.can_reach_location("6D75D785EB89AFAF:enderio:advanced_capacitor_bank:7887447292591583151")
                        and state.can_reach_location("62DE39B1BEF752BA:enderio:octadic_capacitor:7124195096122577594"),
            "123F1D4B1509DA03:enderio:energetic_photovoltaic_module:1314801824528194051": lambda
                state: state.can_reach_location("304C3DA255E8BEA1:enderio:basic_capacitor:3480224379485863585")
                        and has_gold_ingots(world,state,player)
                        and state.can_reach_location("41D4504AFE0D80F8:enderio:alloy_smelter:4743504590548074744"),
            "110127114AE2FDA9:enderio:pulsating_photovoltaic_module:1225303528845802921": lambda
                state: state.can_reach_location("123F1D4B1509DA03:enderio:energetic_photovoltaic_module:1314801824528194051")
                        and has_pulsating_alloy_ingot(world,state,player),
            "783FDD210C8E8C93:enderio:vibrant_photovoltaic_module:8664887342098451603": lambda
                state: state.can_reach_location("110127114AE2FDA9:enderio:pulsating_photovoltaic_module:1225303528845802921")
                        and state.can_reach_location("62DE39B1BEF752BA:enderio:octadic_capacitor:7124195096122577594")
                        and has_vibrant_alloy_ingot(world,state,player),
            "1467C86B0DB6BF13:ironjetpacks:capacitor:1470364165476892435": lambda
                state: state.can_reach_location("62DE5FA1C1F76537:immersiveengineering:workbench:7124236808895292727")
                        and has_redstone_alloy_ingots(world,state,player) and has_copper_alloy_ingot(world,state,player),
            "0497D308100CEA7E:ironjetpacks:capacitor:330965129217501822": lambda
                state: state.can_reach_location("1467C86B0DB6BF13:ironjetpacks:capacitor:1470364165476892435"),
            "39822004CF85610A:ironjetpacks:capacitor:4143909812167860490": lambda
                state: state.can_reach_location("0497D308100CEA7E:ironjetpacks:capacitor:330965129217501822")
                        and has_conductive_alloy_ingots(world,state,player),
            "602AC0D72EC760E3:ironjetpacks:capacitor:6929563007098249443": lambda
                state: state.can_reach_location("39822004CF85610A:ironjetpacks:capacitor:4143909812167860490"),
            "16FC2C94F09D2335:ironjetpacks:capacitor:1656247781169111861": lambda
                state: state.can_reach_location("602AC0D72EC760E3:ironjetpacks:capacitor:6929563007098249443")
                        and has_energetic_alloy_ingot(world,state,player),
            "4D1D60A606D7525A:ironjetpacks:capacitor:5556703781440672346": lambda
                state: state.can_reach_location("16FC2C94F09D2335:ironjetpacks:capacitor:1656247781169111861")
                        and has_vibrant_alloy_ingot(world,state,player),
            "3BC52195653A9011:enderio:stirling_generator:4306885544181927953": lambda
                state: state.can_reach_location("304C3DA255E8BEA1:enderio:basic_capacitor:3480224379485863585")
                        and has_dark_steel_ingot(world,state,player) and has_gear_mold(world,state,player),
            "0DA6D312F162E68A:tesseract:tesseract:983705646939694730": lambda
                state: state.can_reach_location("3BC52195653A9011:enderio:stirling_generator:4306885544181927953")
                        and state.can_reach_location("45C50B63083377EB:botania:mana_pool:5027437078996285419")
                        and has_tesseract(world,state,player),
            "0DCAF4BD7DA81E0C:Dim/Ender Storage:993875762482781708": lambda
                state: state.can_reach_location("0DA6D312F162E68A:tesseract:tesseract:983705646939694730")
                        and state.can_reach_location("77D5B7D22F8D1B8E:minecraft:blaze_rod:8635009973921586062"),
            "41D4504AFE0D80F8:enderio:alloy_smelter:4743504590548074744": lambda
                state: state.can_reach_location("3BC52195653A9011:enderio:stirling_generator:4306885544181927953"),
            "430434760D2EC53D:enderio:dark_steel_sword:4829042382079968573": lambda
                state: state.can_reach_location("41D4504AFE0D80F8:enderio:alloy_smelter:4743504590548074744"),
            "3C5C46275635B639:enderio:xp_obelisk:4349428474897086009": lambda
                state: state.can_reach_location("41D4504AFE0D80F8:enderio:alloy_smelter:4743504590548074744")
                        and has_soularium_ingot(world,state,player) and has_energetic_alloy_ingot(world,state,player),
            "3D039057F963BF8A:enderio:travel_anchor:4396516368764354442": lambda
                state: state.can_reach_location("3C5C46275635B639:enderio:xp_obelisk:4349428474897086009"),
            "192279D2382F35DD:enderio:sag_mill:1811143943949071837": lambda
                state: state.can_reach_location("41D4504AFE0D80F8:enderio:alloy_smelter:4743504590548074744"),
            "236AB7E3C6AE1F38:enderio:slice_and_splice:2552054327777566520": lambda
                state: state.can_reach_location("192279D2382F35DD:enderio:sag_mill:1811143943949071837")
                        and has_soularium_ingot(world,state,player) and has_energetic_alloy_ingot(world,state,player),
            "321D17BD61F59DE0:enderio:powered_spawner:3611068578380750304": lambda
                state: state.can_reach_location("236AB7E3C6AE1F38:enderio:slice_and_splice:2552054327777566520")
                        and has_vibrant_alloy_ingot(world,state,player)
                        and (state.can_reach_location("77F0DF050A474878:Into the Twilight Forest:8642652897664256120")
                             or state.can_reach_location("403922E054130670:Into the Nether:4627768438978446960")),
            "6BE482A7F8998527:enderio:soul_binder:7774482514690278695": lambda
                state: state.can_reach_location("236AB7E3C6AE1F38:enderio:slice_and_splice:2552054327777566520")
                        and has_vibrant_alloy_ingot(world,state,player),
            "3C94C3249C635B5B:enderio:staff_of_travelling:4365328500838849371": lambda
                state: state.can_reach_location("6BE482A7F8998527:enderio:soul_binder:7774482514690278695"),
            "3BAAF007B830AD10:enderio:staff_of_levity:4299512710224194832": lambda
                state: state.can_reach_location("6BE482A7F8998527:enderio:soul_binder:7774482514690278695")
                        and state.can_reach_location("46F450DDEAECE702:minecraft:dragon_egg:5112800391031744258"),


            #Zeta
            "5D7D2A4C3BA37750:Into the Aether:6736587124522579792": lambda state:
            state.can_reach_location("3EE16F0264052C50:Getting Started:4531024756170107984")
                        and has_iron_ingots(world,state,player),
            "77F0DF050A474878:Into the Twilight Forest:8642652897664256120": lambda state: state.can_reach_location(
                "3EE16F0264052C50:Getting Started:4531024756170107984"),
            "3C93642728A0CAAA:Into the Undergarden:4364942583200271018": lambda
                state: state.can_reach_location("3EE16F0264052C50:Getting Started:4531024756170107984")
                        and has_iron_ingots(world,state,player) and has_gold_ingots(world,state,player)
                        and has_redstone_ingot(world,state,player) and has_netherite_ingots(world,state,player),
            "403922E054130670:Into the Nether:4627768438978446960": lambda
                state: state.can_reach_location("3EE16F0264052C50:Getting Started:4531024756170107984"),
            "4632C8C4F1622D5D:Into the End: 5058326079679376733": lambda
                state: state.can_reach_location("26B34910CE753FB9:Clouds:2788652930804563897")
                        and state.can_reach_location("1759B24EE5751EF7:Into the Mining Dimensions:1682571987726442231")
                        and state.can_reach_location("1D639216999D7353:minecraft:ghast_tear:2117696875558433619"),
            "1759B24EE5751EF7:Into the Mining Dimensions:1682571987726442231": lambda
                state: state.can_reach_location("5D7D2A4C3BA37750:Into the Aether:6736587124522579792")
                        and state.can_reach_location("3C93642728A0CAAA:Into the Undergarden:4364942583200271018")
                        and state.can_reach_location("36DE9BE5B9E817D5:minecraft:wither_skeleton_skull:3953768933846685653")
                        and has_ender_ingot(world,state,player)
                        and state.can_reach_location("31A628554F318833:botania:pure_daisy:3577591300858415155"),
            "69912119C98D6247:Conquor the Twilight:7606897640244863559": lambda
                state: state.can_reach_location("77F0DF050A474878:Into the Twilight Forest:8642652897664256120"),
            "77D5B7D22F8D1B8E:minecraft:blaze_rod:8635009973921586062": lambda
                state: state.can_reach_location("403922E054130670:Into the Nether:4627768438978446960"),
            "0B023FB0978509B7:minecraft:nether_wart:793266512059500983": lambda
                state: state.can_reach_location("403922E054130670:Into the Nether:4627768438978446960"),
            "36DE9BE5B9E817D5:minecraft:wither_skeleton_skull:3953768933846685653": lambda
                state: state.can_reach_location("403922E054130670:Into the Nether:4627768438978446960"),
            "1D639216999D7353:minecraft:ghast_tear:2117696875558433619": lambda
                state: state.can_reach_location("403922E054130670:Into the Nether:4627768438978446960"),
            "51A0F9A5FD72B84C:Dungeon Master:5881975604662941772": lambda
                state: state.can_reach_location("5D7D2A4C3BA37750:Into the Aether:6736587124522579792"),
            "0187148CB8910C44:New Resources:110079310518357060": lambda
                state: state.can_reach_location("5D7D2A4C3BA37750:Into the Aether:6736587124522579792"),
            "1892F7D6B155AADD:aether:enchanted_gravitite:1770750104980269789": lambda
                state: state.can_reach_location("5D7D2A4C3BA37750:Into the Aether:6736587124522579792"),
            "26B34910CE753FB9:Clouds:2788652930804563897": lambda
                state: state.can_reach_location("5D7D2A4C3BA37750:Into the Aether:6736587124522579792"),
            "0332B6BA96B14AD1:undergarden:cloggrum_sword:230447443457690321": lambda
                state: state.can_reach_location("3C93642728A0CAAA:Into the Undergarden:4364942583200271018"),
            "009DC6680176855E:undergarden:utherium_sword:44409721347016030": lambda
                state: state.can_reach_location("3C93642728A0CAAA:Into the Undergarden:4364942583200271018"),
            "4ED75332CE21FB62:undergarden:forgotten_sword:5681100932622973794": lambda
                state: state.can_reach_location("3C93642728A0CAAA:Into the Undergarden:4364942583200271018")
                        and state.can_reach_location("0332B6BA96B14AD1:undergarden:cloggrum_sword:230447443457690321"),
            "7995042AD8710998:undergarden:froststeel_sword:8760913232185592216": lambda
                state: state.can_reach_location("3C93642728A0CAAA:Into the Undergarden:4364942583200271018"),
            "46F450DDEAECE702:minecraft:dragon_egg:5112800391031744258": lambda
                state: state.can_reach_location("4632C8C4F1622D5D:Into the End: 5058326079679376733"),
            "130498751078C956:minecraft:elytra:1370387815182420310": lambda
                state: state.can_reach_location("4632C8C4F1622D5D:Into the End: 5058326079679376733"),
            "1C49E92D224E3EB3:minecraft:dragon_head:2038416686420213427": lambda
                state: state.can_reach_location("4632C8C4F1622D5D:Into the End: 5058326079679376733"),
            "6634C250A453D27A:minecraft:shulker_shell:7364724942267732602": lambda
                state: state.can_reach_location("4632C8C4F1622D5D:Into the End: 5058326079679376733"),
            "0754204BD1B84C6E:chunkloaders:basic_chunk_loader:528082566322343022": lambda
                state: state.can_reach_location("3EE16F0264052C50:Getting Started:4531024756170107984")
                        and has_iron_ingots(world,state,player),
            "1C49D56AD66A9A18:chunkloaders:advanced_chunk_loader:2038394961202420248": lambda
                state: state.can_reach_location("0754204BD1B84C6E:chunkloaders:basic_chunk_loader:528082566322343022")
                        and has_gold_ingots(world,state,player),
            "41ACAC42D3ECF8A9:chunkloaders:ultimate_chunk_loader:4732346711482890409": lambda
                state: state.can_reach_location("1C49D56AD66A9A18:chunkloaders:advanced_chunk_loader:2038394961202420248"),
            "77120C4E9ECB9A5B:angelring:diamond_ring:8579933771905342043": lambda
                state: state.can_reach_location("1467C86B0DB6BF13:ironjetpacks:capacitor:1470364165476892435")
                        and state.can_reach_location("130498751078C956:minecraft:elytra:1370387815182420310")
                        and state.can_reach_location("1D639216999D7353:minecraft:ghast_tear:2117696875558433619"),
            "4F2E868BE8E4EDBD:angelring:angel_ring:5705645713390890429": lambda
                state: state.can_reach_location("77120C4E9ECB9A5B:angelring:diamond_ring:8579933771905342043")
                        and has_gold_ingots(world,state,player)
                        and state.can_reach_location("77D5B7D22F8D1B8E:minecraft:blaze_rod:8635009973921586062"),
            "67E3E6364520C852:angelring:energetic_angel_ring:7486080126382295122": lambda
                state: state.can_reach_location("4F2E868BE8E4EDBD:angelring:angel_ring:5705645713390890429")
                        and has_netherite_ingots(world,state,player),
            "0076047DA7FD61DF:angelring:leadstone_angel_ring:33218984987681247": lambda
                state: state.can_reach_location("67E3E6364520C852:angelring:energetic_angel_ring:7486080126382295122")
                        and has_lead_ingots(world,state,player) and has_invar_ingot(world,state,player)
                        and has_gear_mold(world,state,player)
                        and state.can_reach_location("4FFD39276D8238DF:thermal:machine_smelter:5763825939607861471"),
            "3E2361BEEA7F85CD:angelring:hardened_angel_ring:4477529927142311373": lambda
                state: state.can_reach_location("0076047DA7FD61DF:angelring:leadstone_angel_ring:33218984987681247")
                        and has_electrum_ingot(world,state,player) and has_signalum_ingot(world,state,player)
                        and has_silver_ingots(world,state,player),
            "0AFEE76D3204FB5B:angelring:reinforced_angel_ring:792325040640424795": lambda
                state: state.can_reach_location("3E2361BEEA7F85CD:angelring:hardened_angel_ring:4477529927142311373")
                        and state.can_reach_location("007A44E227967158:thermal:machine_crucible:34415685276168536")
                        and (state.can_reach_location("56FBAF04FEC1E0F8:thermal:machine_bottler:6267795742405026040")
                             or (state.can_reach_location("7AC647D823CD6523:immersiveengineering:light_engineering:8846837511655089443")
                             and state.can_reach_location("4B61E75F57941931:immersiveengineering:steel_scaffolding_standard:5431877022262761777"))),
            "0E591671C9C77C30:angelring:resonant_angel_ring:1033882267430648880": lambda
                state: state.can_reach_location("0AFEE76D3204FB5B:angelring:reinforced_angel_ring:792325040640424795")
                        and has_enderium_ingot(world,state,player) and has_lumium_ingot(world,state,player)
                        and state.can_reach_location("5D7D2A4C3BA37750:Into the Aether:6736587124522579792"),

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
            "5104ACF37E471F1A:extendedcrafting:basic_catalyst:5837981178774626074": lambda
                state: state.can_reach_location("3EE16F0264052C50:Getting Started:4531024756170107984")
                        and has_basic_crafting_table(world,state,player),
            "": lambda
                state: state.can_reach_location(""),
            "": lambda
                state: state.can_reach_location(""),

            # Omega
            "546C44F3B917BB85:Creative Items:6083313010243779461": lambda state: state.can_reach_location(
                "3EE16F0264052C50:Getting Started:4531024756170107984"),




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
