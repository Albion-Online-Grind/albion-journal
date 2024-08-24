import xml.etree.ElementTree as ET

jtree = ET.parse('ao-bin-dumps/albionjournal.xml')
jroot = jtree.getroot()

itree = ET.parse('ao-bin-dumps/items.xml')
iroot = itree.getroot()

etree = ET.parse('ao-bin-dumps/expeditions.xml')
eroot = etree.getroot()

ltree = ET.parse('ao-bin-dumps/localization.xml')
lroot = ltree.getroot()

for category in jroot.findall(".//category"):
    # Skip any categories that aren't applicable
    if category.get('hideinjournal') == "true":
        break

    # Determine localized category name
    categoryID = category.get('uniquename')
    categoryNameID = category.get('displayname')
    categoryName = lroot.find(".//*[@tuid='" + categoryNameID + "']/tuv/seg").text
    print(categoryName)
    print("====================")

    for subcategory in jroot.findall(".//*[@uniquename='" + categoryID + "']/subcategory"):
        # Determine localized subcategory name
        subcategoryID = subcategory.get('uniquename')
        subcategoryNameID = subcategory.get('displayname')
        subcategoryName = lroot.find(".//*[@tuid='" + subcategoryNameID + "']/tuv/seg").text
        print(subcategoryName)
        print("--------------------")
        
        for achievement in jroot.findall(".//*[@uniquename='" + subcategoryID + "']/achievement"):
            # Determine localized achievement description
            achievementNameID = "@" + achievement.get('name') + "_DESCRIPTION"
            achievementName = lroot.find(".//*[@tuid='" + achievementNameID + "']/tuv/seg").text

            # Determine localized reward description
            rewardID = achievement.get('rewarditem')
            if lroot.find(".//*[@tuid='@ITEMS_" + rewardID + "']/tuv/seg") is None:
                reward = "Item Not Found"
            else:
                reward = lroot.find(".//*[@tuid='@ITEMS_" + rewardID + "']/tuv/seg").text

            # Append reward amount where present
            amount = 1 if achievement.get('rewardamount') is None else achievement.get('rewardamount')
            reward = reward if amount == 1 else reward + " (x" + amount + ")"

            print("                  <tr>")
            print("                    <td>" + achievementName + "</td>")
            print("                    <Reward")
            print("                      id=\"" + rewardID + "\"")
            print("                      title=\"" + reward + "\"")
            print("                    />")
            print("                  </tr>")
