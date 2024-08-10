import xml.etree.ElementTree as ET

jtree = ET.parse('ao-bin-dumps/albionjournal.xml')
jroot = jtree.getroot()

itree = ET.parse('ao-bin-dumps/items.xml')
iroot = itree.getroot()

etree = ET.parse('ao-bin-dumps/expeditions.xml')
eroot = etree.getroot()

ltree = ET.parse('ao-bin-dumps/localization.xml')
lroot = ltree.getroot()

for achievement in jroot.findall(".//*[@uniquename='PVE']/subcategory/achievement"):
    # Determine localized achievement description
    nameID = achievement.get('name')
    name = lroot.find(".//*[@tuid='@" + nameID + "_DESCRIPTION']/tuv/seg").text + "\n"

    # Determine localized reward description
    rewardID = achievement.get('rewarditem')
    if lroot.find(".//*[@tuid='@ITEMS_" + rewardID + "']/tuv/seg") is None:
        reward = "Item Not Found"
    else:
        reward = lroot.find(".//*[@tuid='@ITEMS_" + rewardID + "']/tuv/seg").text

    # Append reward amount where present
    amount = 1 if achievement.get('rewardamount') is None else achievement.get('rewardamount')
    reward = reward if amount == 1 else reward + " (x" + amount + ")"

    # print(nameID,rewardID,amount)
    print(name,"<Reward id=\"" + rewardID + "\" title=\"" + reward + "\" />")
