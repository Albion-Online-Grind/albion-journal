import xml.etree.ElementTree as ET

jtree = ET.parse('ao-bin-dumps/albionjournal.xml')
jroot = jtree.getroot()

itree = ET.parse('ao-bin-dumps/items.xml')
iroot = itree.getroot()

etree = ET.parse('ao-bin-dumps/expeditions.xml')
eroot = etree.getroot()

ltree = ET.parse('ao-bin-dumps/localization.xml')
lroot = ltree.getroot()

showRequirements = [
    "SA_EXPEDITION_FINISH_ALL",
    "JOURNAL_PVE_EXPEDITION_FINISH_ALL_HARDCORE",
    "SA_EXPLORATION_CITIES",
    "JOURNAL_EXPLORATION_CITIES_VISIT_REST_CITY_ALL",
    "JOURNAL_EXPLORATION_TRAVEL_RIDE_ADC_MOUNT",
    "JOURNAL_EXPLORATION_TRAVEL_RIDE_FW_ALL"
    ]

showRequirementsSkipTags = [
    "and",
    "or",
    "killmob"
    ]

# Print file header in `journal.md` format
# TBD: Create print functions
print("```tsx")
print("const Journal = () => {")
print("  return (")
print("    <div>")

for category in jroot.findall(".//category"):
    # Skip any categories that aren't applicable
    if category.get('hideinjournal') == "true":
        continue

    # Determine localized category name
    categoryID = category.get('uniquename')
    categoryNameID = category.get('displayname')
    categoryName = lroot.find(".//*[@tuid='" + categoryNameID + "']/tuv/seg").text

    # Count subcategories and achievements
    subcategoryCount = len(category.findall("subcategory"))
    achievementCount = len(category.findall("subcategory/achievement"))

    # Print category name with total achievement count in `journal.md` format
    print("")
    print("      {/* " + categoryName + " */}")
    print("      <Section>")
    print("        <UncontrolledAccordion id=\"" + categoryID.lower() + "\">")
    print("          <AccordionItem>")
    print("            <AccordionHeader targetId=\"" + categoryID.lower() + "\">")
    print("              " + categoryName + " (" + str(achievementCount) + ")")
    print("            </AccordionHeader>")
    print("            <AccordionBody accordionId=\"" + categoryID.lower() + "\">")

    for subcategory in jroot.findall(".//*[@uniquename='" + categoryID + "']/subcategory"):
        # Determine localized subcategory name
        subcategoryID = subcategory.get('uniquename')
        subcategoryNameID = subcategory.get('displayname')
        subcategoryName = lroot.find(".//*[@tuid='" + subcategoryNameID + "']/tuv/seg").text

        # Count achievements
        achievementCount = len(subcategory.findall("achievement"))

        # Print subcategory name with achievement count in `journal.md` format
        print("")
        print("              <h4>" + subcategoryName + " (" + str(achievementCount) + ")</h4>")
        print("              <Table responsive striped borderless hover dark>")
        print("                <thead>")
        print("                  <tr>")
        print("                    <th>Name</th>")
        print("                    <th style={{ width: 500 }}>Reward</th>")
        print("                  </tr>")
        print("                </thead>")
        print("                <tbody>")
        
        for achievement in jroot.findall(".//*[@uniquename='" + subcategoryID + "']/achievement"):
            # Determine localized achievement description
            achievementID = achievement.get('name')
            achievementNameID = "@" + achievementID + "_DESCRIPTION"
            achievementName = lroot.find(".//*[@tuid='" + achievementNameID + "']/tuv/seg").text
            rewardItem = achievement.get('rewarditem')

            # TBD: Determine reward item icon
            # rewardItemUISprite = iroot.find(".//*[@uniquename='" + rewardItem + "']").get('uisprite')
            # rewardID = "" if rewardItemUISprite is None else rewardItemUISprite
            rewardID = rewardItem

            # Determine reward item localized name
            # TBD: Create lookup function(s)
            rewardItemLookup = iroot.find(".//*[@uniquename='" + rewardItem + "']")
            if rewardItemLookup is None:
                rewardItemLookup = iroot.find(".//*[@uniquename='" + rewardItem + "_TEMPLATE']")
                if "namelocatag" in rewardItemLookup.attrib:
                    # Use `namelocatag` attribute if present
                    rewardItem = rewardItemLookup.get('namelocatag')
                    reward = lroot.find(".//*[@tuid='" + rewardItem + "']/tuv/seg").text
                else:
                    # If `namelocatag` attribute is not present, prepend common usage for lookup
                    reward = lroot.find(".//*[@tuid='@ITEMS_" + rewardItem + "']/tuv/seg").text
            else:
                if "namelocatag" in rewardItemLookup.attrib:
                    # Use `namelocatag` attribute if present
                    rewardItem = rewardItemLookup.get('namelocatag')
                    reward = lroot.find(".//*[@tuid='" + rewardItem + "']/tuv/seg").text
                else:
                    # If `namelocatag` attribute is not present, prepend common usage for lookup
                    reward = lroot.find(".//*[@tuid='@ITEMS_" + rewardItem + "']/tuv/seg").text

            # Append reward amount where present
            amount = 1 if achievement.get('rewardamount') is None else achievement.get('rewardamount')
            reward = reward if amount == 1 else reward + " (x" + amount + ")"

            # Print achievement detail in `journal.md` format
            if achievementID in showRequirements:
                # Determine requirements for certain achievements
                requirementsList = []
                for requirement in jroot.findall(".//*[@name='" + achievementID + "']//"):
                    # Skip any subelements that aren't applicable
                    if requirement.tag in showRequirementsSkipTags:
                        continue

                    if "nameloca" in requirement.attrib:
                        requirementID = requirement.get('nameloca')
                        requirementsList.append(lroot.find(".//*[@tuid='" + requirementID + "']/tuv/seg").text)
                    elif "namelocatag" in requirement.attrib:
                        requirementID = requirement.get('namelocatag')
                        requirementsList.append(lroot.find(".//*[@tuid='" + requirementID + "']/tuv/seg").text)
                    elif "itemid" in requirement.attrib:
                        requirementID = "@ITEMS_" + requirement.get('itemid')
                        requirementsList.append(lroot.find(".//*[@tuid='" + requirementID + "']/tuv/seg").text)
                    else:
                        # This condition should not happen.
                        # TBD: Use error logging
                        requirementsList.append("Requirement Name Not Found")

                # Include requirements with certain achievements
                # TBD: Use error logging
                print("                  <tr>")
                print("                    <td>")
                print("                      " + achievementName)
                print("                      <br />")
                print("                      <span className=\"text-muted\">")
                print("                        ", end="")
                print(*requirementsList, sep=", ")
                print("                      </span>")
                print("                    </td>")
                print("                    <Reward")
                print("                      id=\"" + rewardID + "\"")
                print("                      title=\"" + reward + "\"")
                print("                    />")
                print("                  </tr>")
            else:
                # Most achievements will not include their requirements
                # TBD: Use error logging
                print("                  <tr>")
                print("                    <td>" + achievementName + "</td>")
                print("                    <Reward")
                print("                      id=\"" + rewardID + "\"")
                print("                      title=\"" + reward + "\"")
                print("                    />")
                print("                  </tr>")

        # Print subcategory end tags in `journal.md` format
        print("                </tbody>")
        print("              </Table>")
        
    # Print category end tags in `journal.md` format
    print("            </AccordionBody>")
    print("          </AccordionItem>")
    print("        </UncontrolledAccordion>")
    print("      </Section>")

# Print file footer in `journal.md` format
print("    </div>")
print("  );")
print("};")
print("```")
