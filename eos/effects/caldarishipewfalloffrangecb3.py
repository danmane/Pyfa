# caldariShipEwFalloffRangeCB3
#
# Used by:
# Ship: Scorpion
# Ship: Scorpion Ishukone Watch
type = "passive"
def handler(fit, ship, context):
    level = fit.character.getSkill("Caldari Battleship").level
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "ECM",
                                  "falloff", ship.getModifiedItemAttr("shipBonusCB3") * level)