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
    name = achievement.get('name')
    lname = lroot.find(".//*[@tuid='@" + name + "_DESCRIPTION']/tuv/seg").text

    # Determine localize reward description
    reward = achievement.get('rewarditem')
    if lroot.find(".//*[@tuid='@ITEMS_" + reward + "']/tuv/seg") is None:
        lreward = "Item Not Found"
    else:
        lreward = lroot.find(".//*[@tuid='@ITEMS_" + reward + "']/tuv/seg").text

    # Append reward amount where present
    amount = 1 if achievement.get('rewardamount') is None else achievement.get('rewardamount')
    lreward = lreward if amount == 1 else lreward + " (x" + amount + ")"

    # print(name,reward,amount)
    print(lname,lreward)
