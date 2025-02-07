#!/usr/bin/env python3
"""
Parse data files from the Albion Online Data Project (AODP) to extract achievements and rewards for
the Albion Journal. Produce output compatible with `journal.md` format.
"""

import html
import re
import xml.etree.ElementTree as ET
from pathlib import Path

# The AODP binary file dumps must be available for extraction.
# If the AODP dumps are not at the parent directory level, modify the `parseDir` variable below.
# https://github.com/ao-data/ao-bin-dumps
AODPBINDUMPSDIRNAME = "ao-bin-dumps"
JOURNALXMLFILE = "albionjournal.xml"
ITEMSXMLFILE = "items.xml"
MOBSXMLFILE = "mobs.xml"
LOCALIZATIONXMLFILE = "localization.xml"
currentDir = Path(__file__).parent
parseDir = currentDir.parent / AODPBINDUMPSDIRNAME

jtree = ET.parse(parseDir / JOURNALXMLFILE)
jroot = jtree.getroot()

itree = ET.parse(parseDir / ITEMSXMLFILE)
iroot = itree.getroot()

mtree = ET.parse(parseDir / MOBSXMLFILE)
mroot = mtree.getroot()

ltree = ET.parse(parseDir / LOCALIZATIONXMLFILE)
lroot = ltree.getroot()

# This file will be overwritten each time this script runs.
OUTPUTFILE = "journal.md"
journalFile = open(OUTPUTFILE, "w", encoding="utf-8")

# Define list of achievements to display their requirements (e.g., quest, creature, location)
# NOTE 1: There are quite a few of these to potentially display, so we're intentionally
#   choosing a subset of them for aesthetics.
# NOTE 2: Displaying these introduces significant complexity when parsing the various XML files,
#   so we must also specify how to handle special cases.
showRequirements = {
    "achievement list": [
        "SA_EXPEDITION_FINISH_ALL",
        "JOURNAL_PVE_EXPEDITION_FINISH_ALL_HARDCORE",
        "SA_PVE_TRACKING_HUNT_ALL",
        "JOURNAL_PVE_TRACKING_KILL_RARE_MOBS_GROUP_7",
        "JOURNAL_PVE_WORLDBOSS_KILL_T8_WORLDBOSSES_ALL",
        "JOURNAL_PVE_WORLDBOSS_KILL_WORLDBOSSES_IN_ALL_LOCATIONS",
        "SA_PVE_KILL_RD_ELITE_01",
        "JOURNAL_GATHERING_SKINNING_ANIMAL_ALL",
        "JOURNAL_GATHERING_SKINNING_LOOT_BABY_ALL",
        "JOURNAL_GATHERING_FISHING_CATCH_ALL",
        "SA_PVE_KILL_MINIGUARDIANS",
        "JOURNAL_GATHERING_CRITTERS_CRITTERS_UNIQUE_ALL",
        "SA_EXPLORATION_CITIES",
        "JOURNAL_EXPLORATION_CITIES_VISIT_REST_CITY_ALL",
        "JOURNAL_EXPLORATION_TRAVEL_RIDE_ADC_MOUNT",
        "JOURNAL_EXPLORATION_TRAVEL_RIDE_FW_ALL",
        "SA_PVE_MISTS_HUNTER",
        "JOURNAL_EXPLORATION_SMUGGLERS_VISIT_BLACKBANKS_08",
        "SA_FACTIONWARFARE_KILLBOSS_ALL"
    ],
    "tags to skip": ["alternative"],
    "include tier": [""],
    "include count": ["SA_FACTIONWARFARE_KILLBOSS_ALL"],
    "correct SBI naming mistakes": {
        "XML tag to match": {
            "attribute to swap out": [
                "ID_TO_SWAP_OUT"
            ],
            "attribute to swap in": [
                "ID_TO_SWAP_IN"
            ]
        },
        "item": {
            "name": [
                "ID_TO_SWAP_OUT"
            ],
            "namelocatag": [
                "ID_TO_SWAP_IN"
            ]
        },
        "DroppedByMob": {
            "name": [
                "T4_MOB_CRITTER_HIDE_COUGAR",
                "T8_MOB_CRITTER_HIDE_COUGAR"
            ],
            "namelocatag": [
                "@MOB_T4_MOB_CRITTER_HIDE_COUGAR",
                "@MOB_T8_MOB_CRITTER_HIDE_COUGAR"
            ]
        }
    }
}

# Write file header in `journal.md` format
# TBD: Create writing functions
print("```tsx", file=journalFile)
print(
    "const Journal = ({ reward }: { reward: string }) => {", file=journalFile)
print("  return (", file=journalFile)
print("    <div>", file=journalFile)

for category in jroot.findall(".//category"):
    # Skip any categories that aren't applicable
    if category.get('hideinjournal') == "true":
        continue

    categoryID = category.get('uniquename')
    # Swap categories to match in-game order
    if categoryID == "GATHERING":
        category = jroot.find(".//category[@uniquename='ECONOMY']")
        categoryID = category.get('uniquename')
    elif categoryID == "ECONOMY":
        category = jroot.find(".//category[@uniquename='GATHERING']")
        categoryID = category.get('uniquename')

    # Determine localized category name
    categoryNameID = category.get('displayname')
    categoryName = lroot.find(
        ".//*[@tuid='" + categoryNameID + "']/tuv/seg").text

    # Count subcategories and achievements
    subcategoryCount = len(category.findall("subcategory"))
    achievementCount = len(category.findall("subcategory/achievement"))

    # Write category name with total achievement count in `journal.md` format
    print("", file=journalFile)
    print("      {/* " + categoryName + " */}", file=journalFile)
    print("      <Section>", file=journalFile)
    print("        <UncontrolledAccordion id=\"" +
          categoryID.lower() + "\">", file=journalFile)
    print("          <AccordionItem>", file=journalFile)
    print("            <AccordionHeader targetId=\"" +
          categoryID.lower() + "\">", file=journalFile)
    print("              " + categoryName +
          " (" + str(achievementCount) + ")", file=journalFile)
    print("            </AccordionHeader>", file=journalFile)
    print("            <AccordionBody accordionId=\"" + categoryID.lower() + "\">",
          file=journalFile)

    for subcategory in jroot.findall(".//*[@uniquename='" + categoryID + "']/subcategory"):
        # Determine localized subcategory name
        subcategoryID = subcategory.get('uniquename')
        subcategoryNameID = subcategory.get('displayname')
        subcategoryName = lroot.find(
            ".//*[@tuid='" + subcategoryNameID + "']/tuv/seg").text

        # Count achievements
        achievementCount = len(subcategory.findall("achievement"))

        # Write subcategory name with achievement count in `journal.md` format
        print("", file=journalFile)
        print("              <h4>" + subcategoryName + " (" + str(achievementCount) + ")</h4>",
              file=journalFile)
        print("              <Table responsive striped borderless hover dark>",
              file=journalFile)
        print("                <thead>", file=journalFile)
        print("                  <tr>", file=journalFile)
        print("                    <th>Name</th>", file=journalFile)
        print(
            "                    <th style={{ width: 500 }}>Reward</th>", file=journalFile)
        print("                  </tr>", file=journalFile)
        print("                </thead>", file=journalFile)
        print("                <tbody>", file=journalFile)

        for achievement in jroot.findall(".//*[@uniquename='" + subcategoryID + "']/achievement"):
            # Determine localized achievement description
            achievementID = achievement.get('name')
            achievementNameID = "@" + achievementID + "_DESCRIPTION"
            achievementName = lroot.find(
                ".//*[@tuid='" + achievementNameID + "']/tuv/seg").text
            rewardItem = achievement.get('rewarditem')

            # TBD: Determine reward item icon
            # rewardItemUISprite = iroot.find(
            #   ".//*[@uniquename='" + rewardItem + "']").get('uisprite')
            # rewardID = "" if rewardItemUISprite is None else rewardItemUISprite

            # Replace ID suffix for certain reward items
            rewardID = re.sub("D1@[1-3]$", "1", rewardItem)
            # Remove enchantment designation when searching for reward items
            rewardItem = re.sub("@[1-3]$", "", rewardItem)

            # Determine reward item localized name
            # TBD: Create lookup function(s)
            rewardItemLookup = iroot.find(
                ".//*[@uniquename='" + rewardItem + "']")
            if rewardItemLookup is None:
                rewardItemLookup = iroot.find(
                    ".//*[@uniquename='" + rewardItem + "_TEMPLATE']")
                if "namelocatag" in rewardItemLookup.attrib:
                    # Use `namelocatag` attribute if present
                    rewardItem = rewardItemLookup.get('namelocatag')
                    reward = lroot.find(
                        ".//*[@tuid='" + rewardItem + "']/tuv/seg").text
                else:
                    # If `namelocatag` attribute is not present, prepend common usage for lookup
                    reward = lroot.find(
                        ".//*[@tuid='@ITEMS_" + rewardItem + "']/tuv/seg").text
            else:
                if "namelocatag" in rewardItemLookup.attrib:
                    # Use `namelocatag` attribute if present
                    rewardItem = rewardItemLookup.get('namelocatag')
                    reward = lroot.find(
                        ".//*[@tuid='" + rewardItem + "']/tuv/seg").text
                else:
                    # If `namelocatag` attribute is not present, prepend common usage for lookup
                    reward = lroot.find(
                        ".//*[@tuid='@ITEMS_" + rewardItem + "']/tuv/seg").text

            # Replace progress variables where present (usually an error)
            if "$$absoluteprogressmax$" in achievementName:
                achievementName = achievementName.replace(
                    "$$absoluteprogressmax$", achievement.get('absoluteprogressmax'))

            # Replace description variables where present
            if "{0}" in reward:
                rewardItemVariableLookup = lroot.find(
                    ".//*[@tuid='" + rewardItemLookup.get('descvariable0') + "']/tuv/seg").text
                reward = reward.replace("{0}", rewardItemVariableLookup)
            if "{1}" in reward:
                rewardItemVariableLookup = lroot.find(
                    ".//*[@tuid='" + rewardItemLookup.get('descvariable1') + "']/tuv/seg").text
                reward = reward.replace("{1}", rewardItemVariableLookup)

            # Append reward amount where present
            amount = achievement.get('rewardamount')
            amount = "1" if amount is None else amount
            reward = reward if amount == "1" else reward + " (x" + amount + ")"

            # Write achievement entry in `journal.md` format
            print("                  <Entry", file=journalFile)
            print("                    reward={reward}", file=journalFile)
            print("                    entryID=\"" +
                  html.escape(achievementID).replace("#x27", "apos") + "\"", file=journalFile)

            if achievementID in showRequirements["achievement list"]:
                # Determine requirements for certain achievements
                requirementsList = []
                REQUIREMENTCOUNT = ""
                for requirement in jroot.findall(".//*[@name='" + achievementID + "']//"):
                    REQUIREMENTID = ""
                    REQUIREMENTTIER = ""

                    # Skip any subelements that aren't applicable
                    if requirement.tag in showRequirements["tags to skip"]:
                        continue

                    # Handle special cases
                    # CASE 1: There are situations when a `gather` or `killmob` element includes the
                    # requirement, but it's children aren't applicable.
                    if (requirement.tag == "gather" and "DroppedByMob"
                            not in showRequirements["tags to skip"]):
                        showRequirements["tags to skip"].append("DroppedByMob")
                    elif (requirement.tag == "killmob" and "nameloca" in requirement.attrib and
                            "mobid" not in showRequirements["tags to skip"]):
                        showRequirements["tags to skip"].append("mobid")
                    # CASE 2: Only use the `count` attribute when we know we need it and
                    # requirements are within an `any` tag.
                    if (achievementID in showRequirements["include count"] and
                            requirement.tag == "any" and "count" in requirement.attrib):
                        REQUIREMENTCOUNT = "Any " + \
                            requirement.get('count') + " of<br />"

                    if "nameloca" in requirement.attrib:
                        REQUIREMENTID = requirement.get('nameloca')
                    elif "namelocatag" in requirement.attrib:
                        REQUIREMENTID = requirement.get('namelocatag')
                    elif "itemid" in requirement.attrib:
                        REQUIREMENTID = "@ITEMS_" + requirement.get('itemid')
                    elif "name" in requirement.attrib:
                        if requirement.tag == "item":
                            if (requirement.get('name') in
                                showRequirements["correct SBI naming mistakes"]
                                    ["item"]["name"]):
                                correctionIndex = (showRequirements["correct SBI naming mistakes"]
                                                   ["item"]["name"].index(
                                                       requirement.get('name')))
                                REQUIREMENTID = (showRequirements["correct SBI naming mistakes"]
                                                 ["item"]["namelocatag"][correctionIndex])
                            else:
                                REQUIREMENTID = "@ITEMS_" + \
                                    requirement.get('name')
                        elif requirement.tag == "DroppedByMob":
                            if (requirement.get('name') in
                                showRequirements["correct SBI naming mistakes"]
                                    ["DroppedByMob"]["name"]):
                                correctionIndex = (showRequirements["correct SBI naming mistakes"]
                                                   ["DroppedByMob"]["name"].index(
                                                       requirement.get('name')))
                                mobLookup = (showRequirements["correct SBI naming mistakes"]
                                             ["DroppedByMob"]["namelocatag"][correctionIndex])
                            else:
                                mobLookup = mroot.find(
                                    ".//*[@uniquename='" + requirement.get('name') +
                                    "']").get('namelocatag')

                            if mobLookup is not None:
                                if lroot.find(".//*[@tuid='" + mobLookup +
                                              "']/tuv/seg") is not None:
                                    REQUIREMENTID = mobLookup
                                else:
                                    REQUIREMENTID = re.sub(
                                        "^@", "@MOB_", mobLookup)
                            else:
                                REQUIREMENTID = "@MOB_" + \
                                    requirement.get('name')
                        elif requirement.tag == "mobid":
                            mobLookup = mroot.find(
                                ".//*[@uniquename='" +
                                requirement.get('name') + "']"
                            ).get('namelocatag')
                            if mobLookup is not None:
                                if lroot.find(".//*[@tuid='" + mobLookup +
                                              "']/tuv/seg") is not None:
                                    REQUIREMENTID = mobLookup
                                else:
                                    REQUIREMENTID = re.sub(
                                        "^@", "@MOB_", mobLookup)
                            else:
                                REQUIREMENTID = "@MOB_" + \
                                    requirement.get('name')

                            if achievementID in showRequirements["include tier"]:
                                REQUIREMENTTIER = "T" + \
                                    mroot.find(
                                        ".//*[@uniquename='" + requirement.get('name') +
                                        "']").get('tier') + " "

                        else:
                            REQUIREMENTID = requirement.get('name')

                    if REQUIREMENTID:
                        requirementAdd = REQUIREMENTTIER + lroot.find(
                            ".//*[@tuid='" + REQUIREMENTID + "']/tuv/seg").text
                        if not requirementsList or requirementsList[-1] != requirementAdd:
                            requirementsList.append(requirementAdd)

                # Handle special skip cases
                if "DroppedByMob" in showRequirements["tags to skip"]:
                    showRequirements["tags to skip"].remove("DroppedByMob")
                elif "mobid" in showRequirements["tags to skip"]:
                    showRequirements["tags to skip"].remove("mobid")

                # Use HTML encoding for all requirements
                for index, value in enumerate(requirementsList):
                    requirementsList[index] = html.escape(
                        value).replace("#x27", "apos")

                # Include requirements with certain achievements
                # TBD: Use error logging
                print("                    name={", file=journalFile)
                print("                      <>", file=journalFile)
                print("                        " +
                      html.escape(achievementName).replace("#x27", "apos"), file=journalFile)
                print("                        <br />", file=journalFile)
                print(
                    "                        <span className=\"text-muted\">", file=journalFile)
                print("                          " +
                      REQUIREMENTCOUNT, end="", file=journalFile)
                print(*requirementsList, sep=", ", file=journalFile)
                print("                        </span>", file=journalFile)
                print("                      </>", file=journalFile)
                print("                    }", file=journalFile)
            else:
                # Most achievements will not include their requirements
                # TBD: Use error logging
                print("                    name=\"" +
                      html.escape(achievementName).replace(
                          "#x27", "apos") + "\"",
                      file=journalFile)

            # Write achievement remaining detail and end tag in `journal.md` format
            print("                    id=\"" +
                  rewardID + "\"", file=journalFile)
            print("                    title=\"" +
                  reward + "\"", file=journalFile)
            print("                  />", file=journalFile)

        # Write subcategory end tags in `journal.md` format
        print("                </tbody>", file=journalFile)
        print("              </Table>", file=journalFile)

    # Write category end tags in `journal.md` format
    print("            </AccordionBody>", file=journalFile)
    print("          </AccordionItem>", file=journalFile)
    print("        </UncontrolledAccordion>", file=journalFile)
    print("      </Section>", file=journalFile)

# Write file footer in `journal.md` format
print("    </div>", file=journalFile)
print("  );", file=journalFile)
print("};", file=journalFile)
print("```", file=journalFile)
