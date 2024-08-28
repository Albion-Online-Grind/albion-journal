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

    # Count subcategories and achievements
    subcategoryCount = len(category.findall("subcategory"))
    achievementCount = len(category.findall("subcategory/achievement"))

    # Print category name with relevant counts
    # TBD: This output does not conform to `journal.md` format.
    print(categoryName + " (" + str(subcategoryCount) + " subcategories & " + str(achievementCount) + " achievements)")
    print("====================")

    for subcategory in jroot.findall(".//*[@uniquename='" + categoryID + "']/subcategory"):
        # Determine localized subcategory name
        subcategoryID = subcategory.get('uniquename')
        subcategoryNameID = subcategory.get('displayname')
        subcategoryName = lroot.find(".//*[@tuid='" + subcategoryNameID + "']/tuv/seg").text

        # Count achievements
        achievementCount = len(subcategory.findall("achievement"))

        # Print subcategory name with achievement count
        # TBD: This output does not conform to `journal.md` format.
        print(subcategoryName + " (" + str(achievementCount) + " achievements)")
        print("--------------------")
        
        for achievement in jroot.findall(".//*[@uniquename='" + subcategoryID + "']/achievement"):
            # Determine localized achievement description
            achievementNameID = "@" + achievement.get('name') + "_DESCRIPTION"
            achievementName = lroot.find(".//*[@tuid='" + achievementNameID + "']/tuv/seg").text
            rewardItem = achievement.get('rewarditem')

            # TBD: Determine reward item icon
            # rewardItemUISprite = iroot.find(".//*[@uniquename='" + rewardItem + "']").get('uisprite')
            # rewardID = "" if rewardItemUISprite is None else rewardItemUISprite
            rewardID = rewardItem

            # Determine reward item attributes
            rewardItemLookup = iroot.find(".//*[@uniquename='" + rewardItem + "']")
            if rewardItemLookup is None:
                rewardItemLookup = iroot.find(".//*[@uniquename='" + rewardItem + "_TEMPLATE']")
                rewardItemNameTag = None if rewardItemLookup is None else rewardItemLookup.get('namelocatag')
                rewardItemDescTag = None if rewardItemLookup is None else rewardItemLookup.get('descriptionlocatag')
            else:
                rewardItemNameTag = rewardItemLookup.get('namelocatag')
                rewardItemDescTag = rewardItemLookup.get('descriptionlocatag')

            # Determine reward item localized name
            if rewardItemNameTag is None and rewardItemDescTag is None:
                rewardLookup = lroot.find(".//*[@tuid='@ITEMS_" + rewardItem + "']/tuv/seg")
                if rewardLookup is None:
                    reward = "Item Not Found"
                else:
                    reward = rewardLookup.text
            # Use `descriptionlocatag` attribute if `namelocatag` attribute is not present
            elif rewardItemNameTag is None:
                # Determine a few localized names differently
                rewardLookupExceptions = ["@ITEMS_MEAL_SOUP_DESC", "@ITEMS_MEAL_SOUP_FISH_DESC", "@ITEMS_RANDOM_DUNGEON_TOKEN_DESC", "@ITEMS_POTION_MOB_RESET_DESC", "@ITEMS_RANDOM_DUNGEON_ELITE_TOKEN_DESC", "@ITEMS_ARTEFACT_WEAPON_DESC", "@ITEMS_FOCUSPOTION_NONTRADABLE_DESC", "@ITEMS_UNIQUE_UNLOCK_WARDROBE", "@ITEMS_MEAL_PIE_DESC", "@ITEMS_UNIQUE_FURNITUREITEM_ADC_GLASS_SPHERE_A_DESC"]
                if rewardItemDescTag in rewardLookupExceptions:
                    reward = lroot.find(".//*[@tuid='@ITEMS_" + rewardItem + "']/tuv/seg").text
                else:
                    reward = lroot.find(".//*[@tuid='" + rewardItemDescTag + "']/tuv/seg").text
                    # This condition usually requires an exception like those above.
                    # Display text to make this condition easy to locate.
                    print("********************")
                    print("No Name Tag & No Exception")
                    print("********************")
            else:
            # Prefer `namelocatag` attribute if `descriptionlocatag` attribute is present
                reward = lroot.find(".//*[@tuid='" + rewardItemNameTag + "']/tuv/seg").text

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
