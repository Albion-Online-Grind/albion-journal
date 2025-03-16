```tsx
const Journal = ({ reward }: { reward: string }) => {
  return (
    <JournalProvider reward={reward}>
      {/* PvE Activities */}
      <Section>
        <UncontrolledAccordion id="pve">
          <AccordionItem>
            <AccordionHeader targetId="pve">
              PvE Activities (225)
            </AccordionHeader>
            <AccordionBody accordionId="pve">
              <h4>Expeditions (18)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="SA_EXPEDITION_FINISH_01"
                    name="Finish a T3 Solo Expedition"
                    id="T3_SILVERBAG_NONTRADABLE"
                    title="Journeyman's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_EXPEDITION_SOLO_T4"
                    name="Finish a Tier 4 Solo Expedition"
                    id="T4_SILVERBAG_NONTRADABLE"
                    title="Adept's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_EXPEDITION_GROUP_T4"
                    name="Finish a Tier 4 Group Expedition"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_EXPEDITION_SOLO_T5"
                    name="Finish a Tier 5 Solo Expedition"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_EXPEDITION_GROUP_T5"
                    name="Finish a Tier 5 Group Expedition"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_EXPEDITION_GROUP_T6"
                    name="Finish a Tier 6 Group Expedition"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_EXPEDITION_SOLO_T5_7M"
                    name="Finish a T5 Solo Expedition within 7 minutes"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_EXPEDITION_GROUP_T6_10M"
                    name="Finish a T6 Group Expedition within 10 minutes"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_EXPEDITION_SOLO_T5_5M"
                    name="Finish a T5 Solo Expedition within 5 minutes"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="SA_EXPEDITION_FINISH_ALL"
                    name={
                      <>
                        Finish every non-hardcore Expedition
                        <br />
                        <span className="text-muted">
                          Curious Excavation, Preaching to the Dead, Fishy
                          Business, Stone Wars, Lumber Lunacy, Lurking
                          Underneath, Fungicide, Three Sisters, Fistful of
                          Silver, Eternal Battle, In the Raven&apos;s Claws
                        </span>
                      </>
                    }
                    id="QUESTITEM_EXP_TOKEN_D1_T6_EXP_HRD_HERETIC_LUMBERCAMP"
                    title="Map (Lvl. 1) - Lumber Lunacy"
                  />
                  <Entry
                    entryID="SA_EXPEDITION_HARDCORE_01"
                    name="Finish any Hardcore Expedition"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_EXPEDITION_HARDCORE_LEVEL_04"
                    name="Finish a Level 4 Hardcore Expedition"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_EXPEDITION_HARDCORE_LEVEL_08"
                    name="Finish a Level 8 Hardcore Expedition"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_EXPEDITION_HARDCORE_LEVEL_12"
                    name="Finish a Level 12 Hardcore Expedition"
                    id="UNIQUE_REPAIRPOWDER_ADC_GENERAL_01_NONTRADEABLE"
                    title="Scroll of Repair"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_EXPEDITION_HARDCORE_LEVEL_18"
                    name="Finish a Level 18 Hardcore Expedition"
                    id="UNIQUE_REPAIRPOWDER_ADC_GENERAL_01_NONTRADEABLE"
                    title="Scroll of Repair"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_EXPEDITION_HARDCORE_LEVEL_18_10M"
                    name="Finish a Level 18 Hardcore Expedition within 10 minutes"
                    id="UNIQUE_REPAIRPOWDER_ADC_GENERAL_01_NONTRADEABLE"
                    title="Scroll of Repair (x2)"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_EXPEDITION_FINISH_5_UNIQUE_HARDCORE"
                    name="Finish 5 different Level 18 Hardcore Expeditions"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x5)"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_EXPEDITION_FINISH_ALL_HARDCORE"
                    name={
                      <>
                        Finish every Hardcore Expedition on Level 18
                        <br />
                        <span className="text-muted">
                          Preaching to the Dead, Fishy Business, Stone Wars,
                          Lumber Lunacy, Lurking Underneath, Fungicide, Three
                          Sisters, Fistful of Silver, Eternal Battle, In the
                          Raven&apos;s Claws
                        </span>
                      </>
                    }
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x10)"
                  />
                </tbody>
              </Table>

              <h4>Solo Random Dungeons (26)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="SA_PVE_RANDOMDUNGEON_ENTERED_01"
                    name="Finish a T3 Solo Dungeon"
                    id="T1_MEAL_SOUP"
                    title="Carrot Soup"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_FINISH_SOLO_T4"
                    name="Finish a Tier 4 Solo Dungeon"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_FINISH_SOLO_ALLFACTIONS"
                    name="Finish a Solo Dungeon of every Faction"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    entryID="SA_PVE_RANDOMDUNGEON_LOOTCHEST_SOLO_01"
                    name="Unlock 10 chests in Solo Dungeons"
                    id="T5_RANDOM_DUNGEON_SOLO_TOKEN_1"
                    title="Expert's Dungeon Map (Solo)"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_FINISH_SOLO_T5"
                    name="Finish a Tier 5 Solo Dungeon"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_FINISH_FROM_MAP_01"
                    name="Finish 3 Solo Dungeons with a Map"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_FINISH_ENCHANTED_NO_MAP"
                    name="Finish an enchanted Solo Dungeon without using a map"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_LOOTCHEST_SOLO_02"
                    name="Unlock 30 chests in Solo Dungeons"
                    id="T4_RANDOM_DUNGEON_TOKEN_1"
                    title="Adept's Dungeon Map (Group)"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_FINISH_DIFFICULTY_02"
                    name="Finish an Enchantment Level 2 Solo Dungeon"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_FINISH_DIFFICULTY_03"
                    name="Finish an Enchantment Level 3 Solo Dungeon"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_FINISH_SOLO_T6"
                    name="Finish a Tier 6 Solo Dungeon"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_FINISH_SOLO_T5_WITH_T3_EQUIP"
                    name="Defeat a T5 boss with T3 equipment on your own"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_FINISH_DIFFICULTY_04"
                    name="Finish an Enchantment Level 4 Solo Dungeon"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_USE_SHRINE"
                    name="Use 30 combat buff shrines in Solo Dungeons"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_FINISH_SOLO_T7"
                    name="Finish a Tier 7 Solo Dungeon"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_FINISH_SOLO_T8"
                    name="Finish a Tier 8 Solo Dungeon"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_FINISH_SOLO_T8_DIFFICULTY_04"
                    name="Finish a Tier 8.4 Solo Dungeon"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="SA_PVE_RANDOMDUNGEON_LOOTCHEST_SOLO_02"
                    name="Unlock 100 chests in Solo Dungeons"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_FINISH_SOLO_T6_WITH_T3_EQUIP"
                    name="Defeat a T6 boss with T3 equipment on your own"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_FINISH_SOLO_T7_WITH_T3_EQUIP"
                    name="Defeat a T7 boss with T3 equipment on your own"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_FINISH_SOLO_T8_WITH_T3_EQUIP"
                    name="Defeat a T8 boss with T3 equipment on your own"
                    id="T5_LEARNINGPOINTS_NONTRADABLE"
                    title="Expert's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_FINISH_SOLO_01"
                    name="Finish 30 Solo Dungeons"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver (x4)"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_FINISH_SOLO_02"
                    name="Finish 100 Solo Dungeons"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver (x7)"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_FINISH_SOLO_03"
                    name="Finish 300 Solo Dungeons"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x9)"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_FINISH_SOLO_04"
                    name="Finish 600 Solo Dungeons"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x12)"
                  />
                  <Entry
                    entryID="SA_PVE_RANDOMDUNGEON_ENTERED_02"
                    name="Finish 1,000 Solo Dungeons"
                    id="T5_LEARNINGPOINTS_NONTRADABLE"
                    title="Expert's Tome of Learning"
                  />
                </tbody>
              </Table>

              <h4>Roaming Mobs (34)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="JOURNAL_PVE_ROAMINGMOBS_KILL_T3_MOBS_01"
                    name="Defeat 12 T3 Roaming Mobs"
                    id="T3_SILVERBAG_NONTRADABLE"
                    title="Journeyman's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_ROAMINGMOBS_KILL_T4_MOBS_01"
                    name="Defeat 50 T4 Roaming Mobs"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_ROAMINGMOBS_KILL_HALFMOUNTED_3"
                    name="Defeat 3 mobs with your mount standing next to you"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_ROAMINGMOBS_KILL_MOBS_IN_TIME_01"
                    name="Defeat 4 Roaming Mobs within 10 seconds"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_ROAMINGMOBS_KILL_MOB_WITH_ARMOR_HELMET_SHOES"
                    name="Defeat a Roaming Mob with any armor slot ability"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_ROAMINGMOBS_KILL_T5_MOBS_01"
                    name="Defeat 80 T5 Roaming Mobs"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_ROAMINGMOBS_KILL_MOBS_IN_TIME_02"
                    name="Defeat 10 Roaming Mobs within 30 seconds"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_ROAMINGMOBS_KILL_MOBS_FACTION_FLAGGED_50"
                    name="Defeat 50 mobs while flagged for Faction Warfare"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_ROAMINGMOBS_KILL_MOBS_IN_TIME_03"
                    name="Defeat 8 Roaming Mobs within 10 seconds"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_ROAMINGMOBS_KILL_MOBS_IN_REDZONE_5"
                    name="Defeat 5 Roaming Mobs in a Red Zone"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_ROAMINGMOBS_KILL_T6_MOBS_01"
                    name="Defeat 120 T6 Roaming Mobs"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_ROAMINGMOBS_KILL_T7_MOBS_01"
                    name="Defeat 200 T7 Roaming Mobs"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_ROAMINGMOBS_KILL_MOBS_IN_BLACKZONE_01"
                    name="Defeat 1,000 Roaming Mobs in a Black Zone"
                    id="T5_LEARNINGPOINTS_NONTRADABLE"
                    title="Expert's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_ROAMINGMOBS_KILL_T8_MOBS_01"
                    name="Defeat 300 T8 Roaming Mobs"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_ROAMINGMOBS_KILL_MOBS_CHAMPIONS_01"
                    name="Defeat 30 Roaming Mob Champions"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_ROAMINGMOBS_KILL_MOBS_CHAMPIONS_02"
                    name="Defeat 100 Roaming Mob Champions"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_ROAMINGMOBS_KILL_MOBS_CHAMPIONS_03"
                    name="Defeat 300 Roaming Mob Champions"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_ROAMINGMOBS_KILL_MOBS_CHAMPIONS_04"
                    name="Defeat 1,000 Roaming Mob Champions"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_ROAMINGMOBS_KILL_MOBS_CHAMPIONS_05"
                    name="Defeat 3,000 Roaming Mob Champions"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_ROAMINGMOBS_KILL_MOBS_MINIBOSSES_01"
                    name="Defeat 10 Roaming Mob Mini Bosses"
                    id="UNIQUE_FURNITUREITEM_ADC_ICESCULPTURE_C"
                    title="Ice Sculpture: Obsessed Cultist"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_ROAMINGMOBS_KILL_MOBS_MINIBOSSES_02"
                    name="Defeat 30 Roaming Mob Mini Bosses"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_ROAMINGMOBS_KILL_MOBS_MINIBOSSES_03"
                    name="Defeat 100 Roaming Mob Mini Bosses"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_ROAMINGMOBS_KILL_MOBS_MINIBOSSES_04"
                    name="Defeat 300 Roaming Mob Mini Bosses"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_ROAMINGMOBS_KILL_MOBS_BOSSES_01"
                    name="Defeat 3 Roaming Mob Bosses"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_ROAMINGMOBS_KILL_MOBS_BOSSES_02"
                    name="Defeat 10 Roaming Mob Bosses"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_ROAMINGMOBS_KILL_MOBS_BOSSES_03"
                    name="Defeat 30 Roaming Mob Bosses"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_ROAMINGMOBS_KILL_MOBS_BOSSES_04"
                    name="Defeat 100 Roaming Mob Bosses"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x10)"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_ROAMINGMOBS_GAIN_MOBFAME_01"
                    name="Gain 100,000 Fame from Roaming Mobs"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_ROAMINGMOBS_GAIN_MOBFAME_02"
                    name="Gain 300,000 Fame from Roaming Mobs"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_ROAMINGMOBS_GAIN_MOBFAME_03"
                    name="Gain a million Fame from Roaming Mobs"
                    id="T5_LEARNINGPOINTS_NONTRADABLE"
                    title="Expert's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_ROAMINGMOBS_GAIN_MOBFAME_04"
                    name="Gain 3 million Fame from Roaming Mobs"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_ROAMINGMOBS_GAIN_MOBFAME_05"
                    name="Gain 10 million Fame from Roaming Mobs"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_ROAMINGMOBS_GAIN_MOBFAME_06"
                    name="Gain 30 million Fame from Roaming Mobs"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x50)"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_ROAMINGMOBS_GAIN_MOBFAME_07"
                    name="Gain 100 million Fame from Roaming Mobs"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x15)"
                  />
                </tbody>
              </Table>

              <h4>Static Dungeons (23)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="JOURNAL_PVE_STATICDUNGEONS_KILL_T3_MOBS_01"
                    name="Defeat 20 mobs in a T3 Static Dungeon"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_STATICDUNGEONS_KILL_T4_MOBS_50"
                    name="Defeat 50 mobs in a T4 Static Dungeon"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_STATICDUNGEONS_KILL_T5_MOBS_100"
                    name="Defeat 100 mobs in a T5 Static Dungeon"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_STATICDUNGEONS_KILL_T6_MOBS_150"
                    name="Defeat 150 mobs in a T6 Static Dungeon"
                    id="T3_POTION_MOB_RESET"
                    title="Minor Calming Potion"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_STATICDUNGEONS_KILL_T7_MOBS_200"
                    name="Defeat 200 mobs in a T7 Static Dungeon"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_STATICDUNGEONS_KILL_T8_MOBS_300"
                    name="Defeat 300 mobs in a T8 Static Dungeon"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    entryID="SA_EXPLORATION_STATIC_DUNGEON_EVENT"
                    name="Participate in a Static Dungeon Event"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_STATICDUNGEONS_GAIN_MOBFAME_DURING_EVENT_100000"
                    name="Gain 100,000 Fame during a Static Dungeon rally"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_STATICDUNGEONS_GAIN_MOBFAME_01"
                    name="Gain 10,000 Fame in Static Dungeons"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_STATICDUNGEONS_GAIN_MOBFAME_02"
                    name="Gain 100,000 Fame in Static Dungeons"
                    id="UNIQUE_UNLOCK_SKIN_HORSE_BROWN_NON_TRADABLE"
                    title="Riding Horse Skin: Brown Mare"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_STATICDUNGEONS_GAIN_MOBFAME_03"
                    name="Gain a million Fame in Static Dungeons"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="SA_EXPLORATION_STATIC_DUNGEON_FAME"
                    name="Gain 10 million Fame in Static Dungeons"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_STATICDUNGEONS_GAIN_MOBFAME_04"
                    name="Gain 30 million Fame in Static Dungeons"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x10)"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_STATICDUNGEONS_GAIN_MOBFAME_05"
                    name="Gain 100 million Fame in Static Dungeons"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x15)"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_STATICDUNGEONS_KILL_MOBS_CHAMPIONS_01"
                    name="Kill 100 Champions in Static Dungeons"
                    id="UNIQUE_FURNITUREITEM_ADC_ICESCULPTURE_B"
                    title="Ice Sculpture: Cursed Archer"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_STATICDUNGEONS_KILL_MOBS_CHAMPIONS_02"
                    name="Kill 300 Champions in Static Dungeons"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_STATICDUNGEONS_KILL_MOBS_CHAMPIONS_03"
                    name="Kill 1,000 Champions in Static Dungeons"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_STATICDUNGEONS_KILL_MOBS_MINIBOSSES_01"
                    name="Kill 30 Mini Bosses in Static Dungeons"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_STATICDUNGEONS_KILL_MOBS_MINIBOSSES_02"
                    name="Kill 100 Mini Bosses in Static Dungeons"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_STATICDUNGEONS_KILL_MOBS_MINIBOSSES_03"
                    name="Kill 300 Mini Bosses in Static Dungeons"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x10)"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_STATICDUNGEONS_KILL_MOBS_BOSSES_01"
                    name="Kill 10 Bosses in Static Dungeons"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_STATICDUNGEONS_KILL_MOBS_BOSSES_02"
                    name="Kill 30 Bosses in Static Dungeons"
                    id="T5_LEARNINGPOINTS_NONTRADABLE"
                    title="Expert's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_STATICDUNGEONS_KILL_MOBS_BOSSES_03"
                    name="Kill 100 Bosses in Static Dungeons"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x15)"
                  />
                </tbody>
              </Table>

              <h4>Dynamic Encampments (34)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="JOURNAL_PVE_DYNAMICCAMPS_PERSONALCHEST_SMALL_01"
                    name="Unlock an open world Small Camp Cache in a Yellow Zone"
                    id="T4_SILVERBAG_NONTRADABLE"
                    title="Adept's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_DYNAMICCAMPS_MAPSHRINEDUNGEONS_MAPUSE"
                    name="Interact with a Lair Map in an Encampment"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_MAPSHRINEDUNGEONS_FINISH_SOLO_01"
                    name="Finish a Boss Lair"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_DYNAMICCAMPS_PERSONALCHEST_SMALL_02"
                    name="Unlock 10 open world Small Camp Caches in a Yellow Zone"
                    id="T4_SILVERBAG_NONTRADABLE"
                    title="Adept's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_MAPSHRINEDUNGEONS_FINISH_SOLO_02"
                    name="Finish 3 Boss Lairs"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_DYNAMICCAMPS_PERSONALCHEST_SMALL_03"
                    name="Unlock 25 open world Small Camp Caches"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_DYNAMICCAMPS_PERSONALCHEST_MEDIUM_01"
                    name="Unlock an open world Group Camp Cache in a Yellow Zone"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_MAPSHRINEDUNGEONS_FINISH_GROUP_01"
                    name="Finish a Group Boss Lair"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_DYNAMICCAMPS_PERSONALCHEST_MEDIUM_02"
                    name="Unlock 10 open world Group Camp Caches"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_DYNAMICCAMPS_PERSONALCHEST_SMALL_04"
                    name="Unlock an open world Small Camp Cache from 3 different Factions"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_DYNAMICCAMPS_PERSONALCHEST_SMALL_05"
                    name="Unlock 50 open world Small Camp Caches"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_MAPSHRINEDUNGEONS_FINISH_SOLO_03"
                    name="Finish 15 Boss Lairs"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_DYNAMICCAMPS_PERSONALCHEST_SMALL_06"
                    name="Unlock a Legendary open world Small Camp Cache"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_DYNAMICCAMPS_PERSONALCHEST_MEDIUM_03"
                    name="Unlock 15 open world Group Camp Caches"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_MAPSHRINEDUNGEONS_FINISH_GROUP_02"
                    name="Finish 5 Group Boss Lairs"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_DYNAMICCAMPS_PERSONALCHEST_MEDIUM_04"
                    name="Unlock an open world Group Camp Cache from 3 different Factions"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_DYNAMICCAMPS_PERSONALCHEST_SMALL_07"
                    name="Unlock an open world Small Camp Cache in the Outlands"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_MAPSHRINEDUNGEONS_FINISH_SOLO_04"
                    name="Finish a Boss Lair in the Outlands"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_DYNAMICCAMPS_PERSONALCHEST_SMALL_08"
                    name="Unlock 5 open world Small Camp Caches in the Outlands"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_MAPSHRINEDUNGEONS_FINISH_SOLO_05"
                    name="Finish a Tier 8 Boss Lair"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_DYNAMICCAMPS_PERSONALCHEST_MEDIUM_05"
                    name="Unlock an open world Group Camp Cache in the Outlands"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_MAPSHRINEDUNGEONS_FINISH_GROUP_03"
                    name="Finish a Group Boss Lair in the Outlands"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_DYNAMICCAMPS_PERSONALCHEST_MEDIUM_06"
                    name="Unlock 5 open world Group Camp Caches in the Outlands"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_MAPSHRINEDUNGEONS_FINISH_GROUP_04"
                    name="Clear a Tier 8 Group Boss Lair"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight (x3)"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_DYNAMICCAMPS_PERSONALCHEST_SMALL_09"
                    name="Unlock 300 open world Small Camp Caches"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_DYNAMICCAMPS_PERSONALCHEST_SMALL_10"
                    name="Unlock 600 open world Small Camp Caches"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_DYNAMICCAMPS_PERSONALCHEST_SMALL_11"
                    name="Unlock 1000 open world Small Camp Caches"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight (x2)"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_MAPSHRINEDUNGEONS_FINISH_SOLO_06"
                    name="Finish 100 Boss Lairs"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_MAPSHRINEDUNGEONS_FINISH_SOLO_07"
                    name="Finish 300 Boss Lairs"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x3)"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_DYNAMICCAMPS_PERSONALCHEST_MEDIUM_07"
                    name="Unlock 50 open world Group Camp Caches"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight (x5)"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_DYNAMICCAMPS_PERSONALCHEST_MEDIUM_08"
                    name="Unlock 100 open world Group Camp Caches"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x5)"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_DYNAMICCAMPS_PERSONALCHEST_MEDIUM_09"
                    name="Unlock 300 open world Group Camp Caches"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight (x10)"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_MAPSHRINEDUNGEONS_FINISH_GROUP_05"
                    name="Finish 30 Group Boss Lairs"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_MAPSHRINEDUNGEONS_FINISH_GROUP_06"
                    name="Finish 100 Group Boss Lairs"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x10)"
                  />
                </tbody>
              </Table>

              <h4>Group Random Dungeons (20)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_FINISH_VETERAN_T4"
                    name="Finish a Tier 4 Group Dungeon"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_FINISH_VETERAN_T5"
                    name="Finish a Tier 5 Group Dungeon"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_FINISH_VETERAN_DIFFICULTY_01"
                    name="Finish 2 Enchantment Level 1 Group Dungeons"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_FINISH_VETERAN_DIFFICULTY_02"
                    name="Finish 3 Enchantment Level 2 Group Dungeons"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_FINISH_VETERAN_DIFFICULTY_03"
                    name="Finish 5 Enchantment Level 3 Group Dungeons"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_FINISH_VETERAN_T6"
                    name="Finish a Tier 6 Group Dungeon"
                    id="UNIQUE_UNLOCK_HEAD_VANITY_BARD_NON_TRADABLE"
                    title="Wardrobe Skin: Bard's Hat"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_FINISH_VETERAN_T7"
                    name="Finish a Tier 7 Group Dungeon"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_FINISH_VETERAN_T8"
                    name="Finish a Tier 8 Group Dungeon"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_FINISH_VETERAN_T8_DIFFICULTY_04"
                    name="Finish a Tier 8.4 Group Dungeon"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="SA_PVE_RANDOMDUNGEON_LEGENDARY"
                    name="Kill the legendary Morgana Demon General, Keeper Earth Aspirant, Undead Reaper, and Heretic Shadowmask"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight (x5)"
                  />
                  <Entry
                    entryID="SA_PVE_RANDOMDUNGEON_LOOTCHEST_GROUP_01"
                    name="Unlock 10 chests in Group Dungeons"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_LOOTCHEST_GROUP_30"
                    name="Unlock 30 chests in Group Dungeons"
                    id="T6_RANDOM_DUNGEON_ELITE_TOKEN_1"
                    title="Master's Dungeon Map (Large Group)"
                  />
                  <Entry
                    entryID="SA_PVE_RANDOMDUNGEON_LOOTCHEST_GROUP_02"
                    name="Unlock 100 chests in Group Dungeons"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_LOOTCHEST_GROUP_500"
                    name="Unlock 500 chests in Group Dungeons"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_VETERAN_FINISH_01"
                    name="Finish 10 Group Dungeons"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_VETERAN_FINISH_30"
                    name="Finish 30 Group Dungeons"
                    id="T5_LEARNINGPOINTS_NONTRADABLE"
                    title="Expert's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_VETERAN_FINISH_80"
                    name="Finish 80 Group Dungeons"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x5)"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_VETERAN_FINISH_150"
                    name="Finish 150 Group Dungeons"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x15)"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_VETERAN_FINISH_300"
                    name="Finish 300 Group Dungeons"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x20)"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_VETERAN_FINISH_500"
                    name="Finish 500 Group Dungeons"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x25)"
                  />
                </tbody>
              </Table>

              <h4>Tracking (27)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="SA_PVE_TRACKING_HUNT_FIRST"
                    name="Track down a solo Rare Creature"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_TRACKING_KILL_T4_QUARRY_MOBS_SOLO"
                    name="Track down a T4 solo Rare Quarry"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_TRACKING_KILL_RARE_MOBS_SOLO_3"
                    name="Track down 3 types of solo Rare Creature"
                    id="UNIQUE_FURNITUREITEM_KEEPER_SYMBOL_OF_POWER_A"
                    title="Keeper Symbol of Power"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_TRACKING_KILL_T5_QUARRY_MOBS_SOLO"
                    name="Track down a T5 solo Rare Quarry"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_TRACKING_KILL_RARE_MOBS_SOLO_4"
                    name="Track down 4 types of solo Rare Creature"
                    id="T4_ARTEFACT_2H_SHAPESHIFTER_MORGANA"
                    title="Adept's Werewolf Remnant"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_TRACKING_KILL_T6_QUARRY_MOBS_SOLO"
                    name="Track down a T6 solo Rare Quarry"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_TRACKING_KILL_RARE_MOBS_SOLO_5"
                    name="Track down 5 types of solo Rare Creature"
                    id="T4_ARTEFACT_2H_SHAPESHIFTER_HELL"
                    title="Adept's Hellfire Imp Remnant"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_TRACKING_FINISH_HUNT_IN_FIRSTENCOUNTER"
                    name="Finish a hunt at the first encounter"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_TRACKING_KILL_RARE_MOBS_SOLO_6"
                    name="Track down 6 types of solo Rare Creature"
                    id="T4_ARTEFACT_2H_SHAPESHIFTER_KEEPER"
                    title="Adept's Runestone Golem Remnant"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_TRACKING_KILL_T7_QUARRY_MOBS_SOLO"
                    name="Track down a T7 solo Rare Quarry"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="SA_PVE_TRACKING_HUNT_ALL"
                    name={
                      <>
                        Track down 7 different solo Rare Creatures
                        <br />
                        <span className="text-muted">
                          Shadow Panther, Sylvian, Spirit Bear, Werewolf,
                          Hellfire Imp, Runestone Golem, Dawnbird
                        </span>
                      </>
                    }
                    id="T4_ARTEFACT_2H_SHAPESHIFTER_AVALON"
                    title="Adept's Dawnbird Remnant"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_TRACKING_KILL_T8_QUARRY_MOBS_SOLO"
                    name="Track down a T8 solo Rare Quarry"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_TRACKING_KILL_RARE_MOBS_GROUP_1"
                    name="Track down a group Rare Creature"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_TRACKING_KILL_RARE_MOBS_GROUP_3"
                    name="Track down 3 types of group Rare Creature"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_TRACKING_KILL_RARE_MOBS_GROUP_5"
                    name="Track down 5 types of group Rare Creature"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_TRACKING_KILL_RARE_MOBS_GROUP_7"
                    name={
                      <>
                        Track down 7 types of group Rare Creature
                        <br />
                        <span className="text-muted">
                          Shadow Panther, Sylvian, Spirit Bear, Werewolf,
                          Hellfire Imp, Runestone Golem, Dawnbird
                        </span>
                      </>
                    }
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver (x5)"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_TRACKING_KILL_T8_QUARRY_MOBS_GROUP_1"
                    name="Track down a T8 group Rare Quarry"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_TRACKING_FINISH_HUNT_SOLO_IN_TIME"
                    name="Finish a solo Rare Creature hunt in 4 minutes"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_TRACKING_FINISH_HUNT_SOLO_EAGLE_IN_TIME"
                    name="Finish a solo Dawnbird hunt in 10 minutes"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_TRACKING_FINISH_HUNT_GROUP_IN_TIME"
                    name="Finish a group Rare Creature hunt in 4 minutes"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_TRACKING_FINISH_HUNT_GROUP_EAGLE_IN_TIME"
                    name="Finish a group Dawnbird hunt in 10 minutes"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_TRACKING_FINISH_HUNT_01"
                    name="Finish 10 hunts"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_TRACKING_FINISH_HUNT_02"
                    name="Finish 20 hunts"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_TRACKING_FINISH_HUNT_03"
                    name="Finish 40 hunts"
                    id="T5_LEARNINGPOINTS_NONTRADABLE"
                    title="Expert's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_TRACKING_FINISH_HUNT_04"
                    name="Finish 80 hunts"
                    id="UNIQUE_UNLOCK_ARMOR_VANITY_PIRATE_GREEN_NON_TRADABLE"
                    title="Wardrobe Skin: Green Navigator's Coat"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_TRACKING_FINISH_HUNT_05"
                    name="Finish 200 hunts"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x8)"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_TRACKING_FINISH_HUNT_06"
                    name="Finish 500 hunts"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x15)"
                  />
                </tbody>
              </Table>

              <h4>World Bosses (20)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="JOURNAL_PVE_WORLDBOSS_KILL_HOMEBASE_MOBS_01"
                    name="Defeat 10 Elite mobs in a World Boss Area"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_WORLDBOSS_KILL_HOMEBASE_MOBS_02"
                    name="Defeat 50 Elite mobs in a World Boss Area"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_WORLDBOSS_KILL_HOMEBASE_MINIBOSSES_01"
                    name="Defeat a Mini Boss in a World Boss Area"
                    id="UNIQUE_FURNITUREITEM_MORGANA_STATUE_A"
                    title="Morgana Cultist Statue"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_WORLDBOSS_KILL_HOMEBASE_MINIBOSSES_02"
                    name="Defeat 5 Mini Bosses in a World Boss Area"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_WORLDBOSS_KILL_HOMEBASE_BOSSES_01"
                    name="Defeat a Boss in a World Boss Area"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    entryID="SA_PVE_KILL_EARTHMOTHER"
                    name="Defeat the Earth Mother"
                    id="T5_LEARNINGPOINTS_NONTRADABLE"
                    title="Expert's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_WORLDBOSS_KILL_HOMEBASE_MINIBOSSES_03"
                    name="Defeat 20 Mini Bosses in a World Boss Area"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_WORLDBOSS_KILL_HOMEBASE_BOSSES_02"
                    name="Defeat 5 Bosses in World Boss Areas"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="SA_PVE_KILL_HARVESTER"
                    name="Defeat the Harvester"
                    id="T5_LEARNINGPOINTS_NONTRADABLE"
                    title="Expert's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_WORLDBOSS_KILL_HOMEBASE_MINIBOSSES_04"
                    name="Defeat 50 Mini Bosses in World Boss Areas"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_WORLDBOSS_KILL_HOMEBASE_BOSSES_03"
                    name="Defeat 20 Bosses in World Boss Areas"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="SA_PVE_KILL_DEMONPRINCE"
                    name="Defeat the Demon Prince"
                    id="T5_LEARNINGPOINTS_NONTRADABLE"
                    title="Expert's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_WORLDBOSS_KILL_HOMEBASE_MOBS_03"
                    name="Defeat 1,000 Elite mobs in a World Boss Area"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x5)"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_WORLDBOSS_KILL_T8_WORLDBOSSES_1"
                    name="Defeat a T8 World Boss"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_WORLDBOSS_KILL_T8_WORLDBOSSES_ALL"
                    name={
                      <>
                        Defeat every T8 World Boss
                        <br />
                        <span className="text-muted">
                          Harvester of Souls, Great Mother of the Earthkeeper,
                          Prince of Morgana
                        </span>
                      </>
                    }
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x15)"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_WORLDBOSS_KILL_WORLDBOSSES_IN_ALL_LOCATIONS"
                    name={
                      <>
                        Defeat a World Boss in every possible area
                        <br />
                        <span className="text-muted">
                          Camlann, Astolat, Inis Mon, Citadel of Ash, Eye of the
                          Forest, Eldersleep, Unhallowed Cloister, Deathreach
                          Priory, Black Monastery, Wailing Bulwark, Daemonium
                          Keep
                        </span>
                      </>
                    }
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x25)"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_WORLDBOSS_KILL_HOMEBASE_MINIBOSSES_05"
                    name="Defeat 200 Mini Bosses in World Boss Areas"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x10)"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_WORLDBOSS_KILL_HOMEBASE_BOSSES_04"
                    name="Defeat 50 Bosses in World Boss Areas"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x5)"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_WORLDBOSS_KILL_WORLDBOSSES_10"
                    name="Defeat 10 World Bosses"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x10)"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_WORLDBOSS_KILL_WORLDBOSSES_30"
                    name="Defeat 30 World Bosses"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x20)"
                  />
                </tbody>
              </Table>

              <h4>Avalonian Dungeons (23)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_ELITE_T6_CLEAR"
                    name="Finish a T6 Avalonian Dungeon"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="SA_COLLECTION_ELITE_DUNGEON_BUFF"
                    name="Receive the Ascension buff at the end of an Avalonian Dungeon"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="SA_PVE_KILL_RD_ELITE_01"
                    name={
                      <>
                        Defeat every Avalonian Dungeon boss type
                        <br />
                        <span className="text-muted">
                          Avalonian Knight Captain, Avalonian Construct,
                          Avalonian Crystal Basilisk, Avalonian High Priestess,
                          Avalonian Archmage
                        </span>
                      </>
                    }
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_ELITE_T7_CLEAR"
                    name="Finish a T7 Avalonian Dungeon"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_ELITE_CLEAR_WITH_BUFF"
                    name="Defeat Sir Bedivere with the Ascension buff active"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_ELITE_T8_CLEAR"
                    name="Finish a T8 Avalonian Dungeon"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight (x6)"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_ELITE_T8_E1_CLEAR"
                    name="Finish a T8.1 Avalonian Dungeon"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight (x7)"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_ELITE_T8_E2_CLEAR"
                    name="Finish a T8.2 Avalonian Dungeon"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight (x8)"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_ELITE_T8_E3_CLEAR"
                    name="Finish a T8.3 Avalonian Dungeon"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight (x9)"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_ELITE_T8_E4_CLEAR"
                    name="Finish a T8.4 Avalonian Dungeon"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight (x10)"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_CLEAR_01"
                    name="Finish 5 Avalonian Dungeons"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x10)"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_CLEAR_02"
                    name="Finish 10 Avalonian Dungeons"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x12)"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_CLEAR_03"
                    name="Finish 20 Avalonian Dungeons"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x15)"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_CLEAR_04"
                    name="Finish 40 Avalonian Dungeons"
                    id="T5_LEARNINGPOINTS_NONTRADABLE"
                    title="Expert's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_CLEAR_05"
                    name="Finish 60 Avalonian Dungeons"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x20)"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_CLEAR_06"
                    name="Finish 100 Avalonian Dungeons"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x30)"
                  />
                  <Entry
                    entryID="SA_PVE_RANDOMDUNGEON_LOOTCHEST_ELITE_01"
                    name="Unlock 10 chests in Avalonian Dungeons"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_ELITE_LOOTCHEST_01"
                    name="Unlock 20 chests in Avalonian Dungeons"
                    id="T5_LEARNINGPOINTS_NONTRADABLE"
                    title="Expert's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_ELITE_LOOTCHEST_02"
                    name="Unlock 40 chests in Avalonian Dungeons"
                    id="UNIQUE_UNLOCK_HEAD_VANITY_BARD_BLUE_NON_TRADABLE"
                    title="Wardrobe Skin: Blue Bard's Hat"
                  />
                  <Entry
                    entryID="SA_PVE_RANDOMDUNGEON_LOOTCHEST_ELITE_02"
                    name="Unlock 100 chests in Avalonian Dungeons"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x10)"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_ELITE_LOOTCHEST_LEGENDARY"
                    name="Unlock a Legendary Chest in an Avalonian Dungeon"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_ELITE_LOOTCHEST_03"
                    name="Unlock 160 chests in Avalonian Dungeons"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x15)"
                  />
                  <Entry
                    entryID="JOURNAL_PVE_RANDOMDUNGEONS_ELITE_LOOTCHEST_04"
                    name="Unlock 300 chests in Avalonian Dungeons"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x20)"
                  />
                </tbody>
              </Table>
            </AccordionBody>
          </AccordionItem>
        </UncontrolledAccordion>
      </Section>

      {/* Economy */}
      <Section>
        <UncontrolledAccordion id="economy">
          <AccordionItem>
            <AccordionHeader targetId="economy">Economy (136)</AccordionHeader>
            <AccordionBody accordionId="economy">
              <h4>Buying Items (21)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="JOURNAL_ECONOMY_BUYING_ITEMS_WEAPON"
                    name="Buy a weapon at the Marketplace"
                    id="T2_SKILLBOOK_NONTRADABLE"
                    title="Novice's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_BUYING_ITEMS_EQUIPMENT_01"
                    name="Buy 5 Equipment Items at the Marketplace"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_BUYING_ITEMS_SILVER_VOLUME_01"
                    name="Spend 10,000 Silver on items at the Marketplace"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_BUYING_ITEMS_SILVER_VOLUME_02"
                    name="Spend 100,000 Silver on items at the Marketplace"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_BUYING_ITEMS_EQUIPMENT_02"
                    name="Buy 10 Equipment Items from the Marketplace"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_BUYING_ITEMS_SILVER_VOLUME_03"
                    name="Spend a million Silver on items at the Marketplace"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x10)"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_BUYING_ITEMS_BUY_ORDER"
                    name="Create a Buy Order"
                    id="T3_VANITY_CONSUMABLE_FIREWORKS_GREEN_NONTRADABLE"
                    title="Royal Green Fireworks (x3)"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_BUYING_ITEMS_SILVER_VOLUME_04"
                    name="Spend 10 million Silver on items at the Marketplace"
                    id="UNIQUE_UNLOCK_SHOES_VANITY_INNKEEPER_NON_TRADABLE"
                    title="Wardrobe Skin: Innkeeper's Shoes"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_BUYING_ITEMS_SILVER_VOLUME_05"
                    name="Spend 100 million Silver on items at the Marketplace"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x20)"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_BUYING_ITEMS_SILVER_VOLUME_06"
                    name="Spend a billion Silver on items at the Marketplace"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x30)"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_BUYING_ITEMS_EQUIPMENT_03"
                    name="Buy 30 Equipment Items at the Marketplace"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_BUYING_ITEMS_EQUIPMENT_04"
                    name="Buy 100 Equipment Items at the Marketplace"
                    id="T3_VANITY_CONSUMABLE_FIREWORKS_RED_NONTRADABLE"
                    title="Royal Red Fireworks (x3)"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_BUYING_ITEMS_EQUIPMENT_05"
                    name="Buy 1,000 Equipment Items at the Marketplace"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x10)"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_BUYING_ITEMS_EQUIPMENT_06"
                    name="Buy 10,000 Equipment Items at the Marketplace"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_BUYING_ITEMS_EQUIPMENT_07"
                    name="Buy 100,000 Equipment Items at the Marketplace"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_BUYING_ITEMS_VOLUME_01"
                    name="Buy 100 Items at the Marketplace"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_BUYING_ITEMS_VOLUME_02"
                    name="Buy 1,000 Items at the Marketplace"
                    id="T3_VANITY_CONSUMABLE_FIREWORKS_YELLOW_NONTRADABLE"
                    title="Royal Yellow Fireworks (x3)"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_BUYING_ITEMS_VOLUME_03"
                    name="Buy 10,000 Items at the Marketplace"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x10)"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_BUYING_ITEMS_VOLUME_04"
                    name="Buy 100,000 Items at the Marketplace"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_BUYING_ITEMS_VOLUME_05"
                    name="Buy a million Items at the Marketplace"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_BUYING_ITEMS_VOLUME_06"
                    name="Buy 10 million Items at the Marketplace"
                    id="UNIQUE_UNLOCK_OFF_VANITY_INNKEEPER_NON_TRADABLE"
                    title="Wardrobe Skin: Innkeeper's Beer Mug"
                  />
                </tbody>
              </Table>

              <h4>Selling Items (24)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="SA_TRADE_ANY_ITEM_MP"
                    name="Sell any item through the Marketplace"
                    id="T2_SKILLBOOK_NONTRADABLE"
                    title="Novice's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_SELLING_SILVER_VOLUME_01"
                    name="Sell items for 10,000 Silver at the Marketplace"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="SA_TRADE_SILVER_01"
                    name="Sell items worth 100,000 Silver at the Marketplace"
                    id="T3_VANITY_CONSUMABLE_FIREWORKS_GREEN_NONTRADABLE"
                    title="Royal Green Fireworks (x3)"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_SELLING_LUXURY_GOODS_ANY_01"
                    name="Sell 10 Luxury Goods directly to their preferred city"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_SELLING_ITEMS_SELL_ORDER_01"
                    name="Create a Sell Order"
                    id="T3_VANITY_CONSUMABLE_FIREWORKS_BLUE_NONTRADABLE"
                    title="Royal Blue Fireworks (x3)"
                  />
                  <Entry
                    entryID="SA_TRADE_SILVER_02"
                    name="Sell items worth 1,000,000 Silver at the Marketplace"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_SELLING_ITEMS_SELL_ORDER_02"
                    name="Create 20 Sell Orders"
                    id="T3_VANITY_CONSUMABLE_FIREWORKS_RED_NONTRADABLE"
                    title="Royal Red Fireworks (x3)"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_SELLING_LUXURY_GOODS_ANY_02"
                    name="Sell 1000 Luxury Goods directly to their preferred city"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="SA_TRADE_ANY_ITEM_BM"
                    name="Sell any item on the Black Market in Caerleon"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="SA_TRADE_SILVER_03"
                    name="Sell items worth 10,000,000 Silver at the Marketplace"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_SELLING_LUXURY_GOODS_ANY_03"
                    name="Sell 9999 Luxury Goods directly to their preferred city"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_TRADING_BM_SELL_ORDER"
                    name="Create a Sell Order on the Black Market"
                    id="T3_VANITY_CONSUMABLE_FIREWORKS_YELLOW_NONTRADABLE"
                    title="Royal Yellow Fireworks (x3)"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_SELLING_SILVER_VOLUME_02"
                    name="Sell items for 100 million Silver at the Marketplace"
                    id="UNIQUE_UNLOCK_HEAD_VANITY_RICH_NOBLE_PURPLE_NON_TRADABLE"
                    title="Wardrobe Skin: Purple Rich Noble's Hat"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_SELLING_SILVER_VOLUME_03"
                    name="Sell items for a billion Silver at the Marketplace"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_TRADING_BM_SILVER_VOLUME_01"
                    name="Earn a million Silver through the Black Market"
                    id="UNIQUE_FURNITUREITEM_KNIGHT_CARPET_A"
                    title="Regal Carpet"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_TRADING_BM_SILVER_VOLUME_02"
                    name="Earn 10 million Silver through the Black Market"
                    id="UNIQUE_UNLOCK_SKIN_OX_BLACKMARKET_NON_TRADABLE"
                    title="Transport Ox Skin: Black Market Ox"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_TRADING_BM_SILVER_VOLUME_03"
                    name="Earn 100 million Silver through the Black Market"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_TRADING_BM_SILVER_VOLUME_04"
                    name="Earn a billion Silver through the Black Market"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x100)"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_SELLING_LUXURY_GOODS_FORT_STERLING"
                    name="Directly sell 9999 preferred luxury goods to Fort Sterling"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x15)"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_SELLING_LUXURY_GOODS_LYMHURST"
                    name="Directly sell 9999 preferred luxury goods to Lymhurst"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x15)"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_SELLING_LUXURY_GOODS_BRIDGEWATCH"
                    name="Directly sell 9999 preferred luxury goods to Bridgewatch"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x15)"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_SELLING_LUXURY_GOODS_MARTLOCK"
                    name="Directly sell 9999 preferred luxury goods to Martlock"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x15)"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_SELLING_LUXURY_GOODS_THETFORD"
                    name="Directly sell 9999 preferred luxury goods to Thetford"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x15)"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_SELLING_LUXURY_GOODS_CAERLEON"
                    name="Directly sell 9999 preferred luxury goods to Caerleon"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x15)"
                  />
                </tbody>
              </Table>

              <h4>Refining (22)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="JOURNAL_ECONOMY_REFINING_T2_01"
                    name="Refine 30 T2 resources"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_REFINING_T3_01"
                    name="Refine 60 T3 resources"
                    id="T3_FOCUSPOTION_NONTRADABLE"
                    title="Journeyman's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_REFINING_T4_01"
                    name="Refine 100 T4 resources"
                    id="T4_FOCUSPOTION_NONTRADABLE"
                    title="Adept's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_TRANSMUTE_E1_01"
                    name="Transmute 10 resources to Uncommon"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_REFINING_T5_01"
                    name="Refine 200 T5 resources"
                    id="T5_FOCUSPOTION_NONTRADABLE"
                    title="Expert's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_TRANSMUTE_BASE_01"
                    name="Transmute 20 resources to a higher tier"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_REFINING_T6_01"
                    name="Refine 400 T6 resources"
                    id="T6_FOCUSPOTION_NONTRADABLE"
                    title="Master's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_TRANSMUTE_E2_01"
                    name="Transmute 25 resources to Rare"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_REFINING_T7_01"
                    name="Refine 400 T7 resources"
                    id="UNIQUE_FOCUSPOTION_ADC_NONTRADABLE_01"
                    title="Grandmaster's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_TRANSMUTE_E3_01"
                    name="Transmute 30 resources to Exceptional"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_REFINING_T8_01"
                    name="Refine 400 T8 resources"
                    id="T8_FOCUSPOTION_NONTRADABLE"
                    title="Elder's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_TRANSMUTE_E4_01"
                    name="Transmute 50 resources to Pristine"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_REFINING_BONUS_FORT_STERLING"
                    name="Use the Fort Sterling refining bonus"
                    id="T4_FOCUSPOTION_NONTRADABLE"
                    title="Adept's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_REFINING_BONUS_LYMHURST"
                    name="Use the Lymhurst refining bonus"
                    id="T4_FOCUSPOTION_NONTRADABLE"
                    title="Adept's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_REFINING_BONUS_BRIDGEWATCH"
                    name="Use the Bridgewatch refining bonus"
                    id="T4_FOCUSPOTION_NONTRADABLE"
                    title="Adept's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_REFINING_BONUS_MARTLOCK"
                    name="Use the Martlock refining bonus"
                    id="T4_FOCUSPOTION_NONTRADABLE"
                    title="Adept's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_REFINING_BONUS_THETFORD"
                    name="Use the Thetford refining bonus"
                    id="T4_FOCUSPOTION_NONTRADABLE"
                    title="Adept's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_REFINING_ANY_01"
                    name="Refine 1,000 Resources"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_REFINING_ANY_02"
                    name="Refine 5,000 Resources"
                    id="T3_FOCUSPOTION_NONTRADABLE"
                    title="Journeyman's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_REFINING_ANY_03"
                    name="Refine 10,000 Resources"
                    id="T4_FOCUSPOTION_NONTRADABLE"
                    title="Adept's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_REFINING_ANY_04"
                    name="Refine 50,000 Resources"
                    id="T5_FOCUSPOTION_NONTRADABLE"
                    title="Expert's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_REFINING_ANY_05"
                    name="Refine 100,000 Resources"
                    id="UNIQUE_FOCUSPOTION_ADC_NONTRADABLE_01"
                    title="Grandmaster's Focus Restoration Potion"
                  />
                </tbody>
              </Table>

              <h4>Crafting (25)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="JOURNAL_ECONOMY_CRAFTING_EQUIPMENT_T2"
                    name="Craft 3 T2 Equipment Items"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_CRAFTING_EQUIPMENT_T3"
                    name="Craft 10 T3 Equipment Items"
                    id="T3_FOCUSPOTION_NONTRADABLE"
                    title="Journeyman's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_CRAFTING_ROYAL_CITY"
                    name="Craft an item in a Royal City"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_CRAFTING_USE_SALAD_01"
                    name="Eat a salad that improves your crafting"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_CRAFTING_EQUIPMENT_T4"
                    name="Craft 40 T4 Equipment Items"
                    id="T4_FOCUSPOTION_NONTRADABLE"
                    title="Adept's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_CRAFTING_LOCAL_BONUS"
                    name="Use a city's crafting bonus"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_CRAFTING_QUALITY_3"
                    name="Craft an Outstanding quality Equipment Item"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x10)"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_CRAFTING_EQUIPMENT_T5"
                    name="Craft 60 T5 Equipment Items"
                    id="T5_FOCUSPOTION_NONTRADABLE"
                    title="Expert's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_CRAFTING_E1_01"
                    name="Craft 20 Uncommon items"
                    id="UNIQUE_FURNITUREITEM_HERETIC_STOVE_A"
                    title="Heretic Stove"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_CRAFTING_QUALITY_4"
                    name="Craft an Excellent quality Equipment Item"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_CRAFTING_EQUIPMENT_T6"
                    name="Craft 80 T6 Equipment Items"
                    id="T6_FOCUSPOTION_NONTRADABLE"
                    title="Master's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_CRAFTING_E2_01"
                    name="Craft 30 Rare items"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_CRAFTING_QUALITY_5"
                    name="Craft a Masterpiece quality Equipment Item"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_CRAFTING_EQUIPMENT_T7"
                    name="Craft 100 T7 Equipment Items"
                    id="UNIQUE_FOCUSPOTION_ADC_NONTRADABLE_01"
                    title="Grandmaster's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_CRAFTING_E3_01"
                    name="Craft 50 Epic items"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_CRAFTING_LOCAL_BONUS_HIDEOUT"
                    name="Use a crafting bonus in a Hideout"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x50)"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_CRAFTING_EQUIPMENT_T8"
                    name="Craft 100 T8 Equipment Items"
                    id="T8_FOCUSPOTION_NONTRADABLE"
                    title="Elder's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_CRAFTING_E4_01"
                    name="Craft 50 Pristine items"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_CRAFTING_T8_E4_01"
                    name="Craft a Pristine T8 item"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_CRAFTING_BESTITEM"
                    name="Craft a Pristine T8 Masterpiece"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x200)"
                  />
                  <Entry
                    entryID="SA_CRAFTING_FAME_01"
                    name="Craft Items worth 10,000 Fame"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="SA_CRAFTING_FAME_02"
                    name="Craft Items worth 100,000 Fame"
                    id="T5_FOCUSPOTION_NONTRADABLE"
                    title="Expert's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="SA_CRAFTING_FAME_03"
                    name="Craft items worth a million Fame"
                    id="UNIQUE_FOCUSPOTION_ADC_NONTRADABLE_01"
                    title="Grandmaster's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="SA_CRAFTING_FAME_04"
                    name="Craft items worth 10 million Fame"
                    id="UNIQUE_FOCUSPOTION_ADC_NONTRADABLE_01"
                    title="Grandmaster's Focus Restoration Potion (x2)"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_CRAFTING_FAME_01"
                    name="Craft items worth 100 million Fame"
                    id="UNIQUE_FOCUSPOTION_ADC_NONTRADABLE_01"
                    title="Grandmaster's Focus Restoration Potion (x3)"
                  />
                </tbody>
              </Table>

              <h4>Item Conversions (22)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="SA_CRAFTING_STUDY_01"
                    name="Study an item"
                    id="T2_SKILLBOOK_NONTRADABLE"
                    title="Novice's Tome of Insight"
                  />
                  <Entry
                    entryID="SA_COLLECTION_SALVAGE"
                    name="Salvage an item"
                    id="T2_SKILLBOOK_NONTRADABLE"
                    title="Novice's Tome of Insight"
                  />
                  <Entry
                    entryID="SA_COLLECTION_REROLL"
                    name="Reroll an item at a Repair Station"
                    id="T2_SKILLBOOK_NONTRADABLE"
                    title="Novice's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_ITEM_CONVERSIONS_MELD_01"
                    name="Meld resources into an Artifact at the Artifact Foundry"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_ITEM_CONVERSIONS_MELD_02"
                    name="Meld 10 Soul Artifacts"
                    id="UNIQUE_FURNITUREITEM_ADC_GLASS_SPHERE_A"
                    title="Glass Sphere"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_ITEM_CONVERSIONS_MELD_03"
                    name="Meld 30 T5 Artifacts"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_ITEM_CONVERSIONS_MELD_04"
                    name="Meld 100 T6 Hunter Artifacts"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_ITEM_CONVERSIONS_MELD_05"
                    name="Meld 100 T8 Avalonian Artifacts"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x30)"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_ITEM_CONVERSIONS_TRANSMUTE_01"
                    name="Create 50 Souls with Transmutation"
                    id="T4_FOCUSPOTION_NONTRADABLE"
                    title="Adept's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_ITEM_CONVERSIONS_TRANSMUTE_02"
                    name="Create a T8 Dungeon Map with Transmutation"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="SA_COLLECTION_REROLL_MASTERPIECE"
                    name="Create a Masterpiece item by rerolling it at a Repair Station"
                    id="T4_FOCUSPOTION_NONTRADABLE"
                    title="Adept's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="SA_COLLECTION_REROLL_STACK"
                    name="Reroll a full stack of 999 items at a Repair Station"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_ITEM_CONVERSIONS_SALVAGE_01"
                    name="Salvage 100 items"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_ITEM_CONVERSIONS_SALVAGE_02"
                    name="Salvage 1,000 items"
                    id="UNIQUE_FURNITUREITEM_ADC_CARNIVAL_ARCHWAY_A"
                    title="Carnival Arch"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_ITEM_CONVERSIONS_SALVAGE_03"
                    name="Salvage 10,000 items"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_ITEM_CONVERSIONS_STUDY_01"
                    name="Study 100 items"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_ITEM_CONVERSIONS_STUDY_02"
                    name="Study 1,000 items"
                    id="T4_FOCUSPOTION_NONTRADABLE"
                    title="Adept's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_ITEM_CONVERSIONS_STUDY_03"
                    name="Study 10,000 items"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_ITEM_CONVERSIONS_REROLL_01"
                    name="Reroll 100 items"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_ITEM_CONVERSIONS_REROLL_02"
                    name="Reroll 1,000 items"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_ITEM_CONVERSIONS_REROLL_03"
                    name="Reroll 10,000 items"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_ITEM_CONVERSIONS_REROLL_04"
                    name="Reroll 100,000 items"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                </tbody>
              </Table>

              <h4>Accumulate Wealth (10)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="JOURNAL_ECONOMY_ACCUMULATE_WEALTH_SILVER_01"
                    name="Own 100,000 Silver"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_ACCUMULATE_WEALTH_SILVER_02"
                    name="Own 500,000 Silver"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x10)"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_ACCUMULATE_WEALTH_GOLD_01"
                    name="Own 5 Gold"
                    id="T3_VANITY_CONSUMABLE_FIREWORKS_YELLOW_NONTRADABLE"
                    title="Royal Yellow Fireworks (x3)"
                  />
                  <Entry
                    entryID="SA_COLLECTION_SILVER"
                    name="Own 1 million Silver"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_ACCUMULATE_WEALTH_SILVER_03"
                    name="Own 5 million Silver"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_ACCUMULATE_WEALTH_SILVER_04"
                    name="Own 10 million Silver"
                    id="UNIQUE_UNLOCK_HEAD_VANITY_DRESS_BLUE_NON_TRADABLE"
                    title="Wardrobe Skin: Blue Princess Hat"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_ACCUMULATE_WEALTH_SILVER_05"
                    name="Own 50 million Silver"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_ACCUMULATE_WEALTH_SILVER_06"
                    name="Own 100 million Silver"
                    id="UNIQUE_UNLOCK_ARMOR_VANITY_DRESS_BLUE_NON_TRADABLE"
                    title="Wardrobe Skin: Blue Princess Dress"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_ACCUMULATE_WEALTH_SILVER_07"
                    name="Own 500 million Silver"
                    id="UNIQUE_UNLOCK_SKIN_OX_BISON_AH_NON_TRADABLE"
                    title="Transport Ox Skin: Auction House Ox"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_ACCUMULATE_WEALTH_SILVER_08"
                    name="Own 1 billion Silver"
                    id="T5_LEARNINGPOINTS_NONTRADABLE"
                    title="Expert's Tome of Learning"
                  />
                </tbody>
              </Table>

              <h4>City Plots (12)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="JOURNAL_ECONOMY_CITY_PLOTS_ENTER_AUCTION"
                    name="Bid at least 1 million Silver on a city plot"
                    id="UNIQUE_FURNITUREITEM_MORGANA_CARPET_A"
                    title="Morgana Carpet"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_CITY_PLOTS_OWN_PLOT_01"
                    name="Own a city plot"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_CITY_PLOTS_EARNED_SILVER_01"
                    name="Collect 1 million Silver from city plots"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_CITY_PLOTS_ENTER_OWN_AUCTION"
                    name="Bid 5 million Silver on a city plot you currently own"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_CITY_PLOTS_EARNED_SILVER_02"
                    name="Collect 3 million Silver from City Plots"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_CITY_PLOTS_OWN_PLOT_02"
                    name="Own 3 plots in the same city simultaneously"
                    id="UNIQUE_UNLOCK_CAPE_VANITY_SNOWLEOPARD_NON_TRADABLE"
                    title="Wardrobe Skin: Snow Leopard Cape"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_CITY_PLOTS_EARNED_SILVER_03"
                    name="Collect 10 million Silver from city plots"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_CITY_PLOTS_EARNED_SILVER_04"
                    name="Collect 30 million Silver from City Plots"
                    id="T6_FOCUSPOTION_NONTRADABLE"
                    title="Master's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_CITY_PLOTS_OWN_PLOT_03"
                    name="Own 5 plots in the same city simultaneously"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_CITY_PLOTS_EARNED_SILVER_05"
                    name="Collect 100 million Silver from city plots"
                    id="T5_LEARNINGPOINTS_NONTRADABLE"
                    title="Expert's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_CITY_PLOTS_EARNED_SILVER_06"
                    name="Collect 300 million Silver from City Plots"
                    id="UNIQUE_FOCUSPOTION_ADC_NONTRADABLE_01"
                    title="Grandmaster's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ECONOMY_CITY_PLOTS_EARNED_SILVER_07"
                    name="Collect 1 billion Silver from city plots"
                    id="UNIQUE_UNLOCK_SKIN_GIANTSTAG_ALPACA_BROWN"
                    title="Stag Skin: Brown Alpaca"
                  />
                </tbody>
              </Table>
            </AccordionBody>
          </AccordionItem>
        </UncontrolledAccordion>
      </Section>

      {/* Gathering */}
      <Section>
        <UncontrolledAccordion id="gathering">
          <AccordionItem>
            <AccordionHeader targetId="gathering">
              Gathering (125)
            </AccordionHeader>
            <AccordionBody accordionId="gathering">
              <h4>Resources (33)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="JOURNAL_GATHERING_RESOURCES_ANY_TYPE_T2"
                    name="Gather 80 Tier 2 resources"
                    id="T3_SILVERBAG_NONTRADABLE"
                    title="Journeyman's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_RESOURCES_ANY_TYPE_T3"
                    name="Gather 120 Tier 3 resources"
                    id="T4_SILVERBAG_NONTRADABLE"
                    title="Adept's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_RESOURCES_FAME_01"
                    name="Gather resources worth 1500 Fame"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_RESOURCES_ANY_TYPE_T4"
                    name="Gather 100 Tier 4 resources"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_RESOURCES_ANY_TYPE_E1_1"
                    name="Gather 10 resources with Enchantment Level 1"
                    id="T4_SKILLBOOK_GATHER_FIBER_NONTRADABLE"
                    title="Adept Fiber Harvester Tome"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_RESOURCES_ANY_TYPE_T5"
                    name="Gather 150 Tier 5 resources"
                    id="T4_SKILLBOOK_GATHER_ROCK_NONTRADABLE"
                    title="Adept Quarrier Tome"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_RESOURCES_ANY_TYPE_E2_1"
                    name="Gather 10 resources with Enchantment Level 2"
                    id="T4_SKILLBOOK_GATHER_WOOD_NONTRADABLE"
                    title="Adept Lumberjack Tome"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_RESOURCES_TREASURE_1"
                    name="Gather a resource from a Plentiful Resource Node"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_RESOURCES_ANY_TYPE_E3_1"
                    name="Gather 10 resources with Enchantment Level 3"
                    id="T5_SKILLBOOK_GATHER_ORE_NONTRADABLE"
                    title="Expert Ore Miner Tome"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_RESOURCES_ANY_TYPE_T6"
                    name="Gather 200 Tier 6 resources"
                    id="T5_SKILLBOOK_GATHER_WOOD_NONTRADABLE"
                    title="Expert Lumberjack Tome"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_RESOURCES_TREASURE_2"
                    name="Gather 100 resources from Plentiful Resource Nodes"
                    id="T5_SKILLBOOK_GATHER_ROCK_NONTRADABLE"
                    title="Expert Quarrier Tome"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_RESOURCES_ANY_TYPE_ANY_E_1"
                    name="Gather 300 enchanted resources"
                    id="UNIQUE_UNLOCK_ARMOR_VANITY_PRIEST_NON_TRADABLE"
                    title="Wardrobe Skin: Monk's Robe"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_RESOURCES_TREASURE_3"
                    name="Gather 500 resources from Plentiful Resource Nodes"
                    id="T6_SKILLBOOK_GATHER_WOOD_NONTRADABLE"
                    title="Master Lumberjack Tome"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_RESOURCES_TERRITORY_RAID_1"
                    name="Gather any resource at an enemy Territory"
                    id="T6_SKILLBOOK_GATHER_ORE_NONTRADABLE"
                    title="Master Ore Miner Tome"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_RESOURCES_ANY_TYPE_ANY_E_2"
                    name="Gather 750 enchanted resources"
                    id="T6_SKILLBOOK_GATHER_FIBER_NONTRADABLE"
                    title="Master Fiber Harvester Tome"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_RESOURCES_ANY_TYPE_T7"
                    name="Gather 200 Tier 7 resources"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_RESOURCES_TREASURE_4"
                    name="Gather 1,000 resources from Plentiful Resource Nodes"
                    id="T7_SKILLBOOK_GATHER_ROCK_NONTRADABLE"
                    title="Grandmaster Quarrier Tome"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_RESOURCES_TERRITORY_RAID_2"
                    name="Gather 50 resources at an enemy Territory"
                    id="T7_SKILLBOOK_GATHER_FIBER_NONTRADABLE"
                    title="Grandmaster Fiber Harvester Tome"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_RESOURCES_ANY_TYPE_ANY_E_3"
                    name="Gather 1,500 enchanted resources"
                    id="T7_SKILLBOOK_GATHER_ORE_NONTRADABLE"
                    title="Grandmaster Ore Miner Tome"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_RESOURCES_FIRST_T8"
                    name="Gather any Tier 8 resource"
                    id="T5_LEARNINGPOINTS_NONTRADABLE"
                    title="Expert's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_RESOURCES_GEAR_MAXSTACKS"
                    name="Gather a resource with maximum Gather Bonus"
                    id="T8_SKILLBOOK_GATHER_ORE_NONTRADABLE"
                    title="Elder Ore Miner Tome"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_RESOURCES_ANY_TYPE_T8"
                    name="Gather 200 Tier 8 resources"
                    id="T8_SKILLBOOK_GATHER_WOOD_NONTRADABLE"
                    title="Elder Lumberjack Tome"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_RESOURCES_ANY_TYPE_E4_1"
                    name="Gather 30 resources with Enchantment Level 4"
                    id="T8_SKILLBOOK_GATHER_ROCK_NONTRADABLE"
                    title="Elder Quarrier Tome"
                  />
                  <Entry
                    entryID="SA_GATHERING_FAME_01"
                    name="Gather resources worth 10,000 Fame"
                    id="T4_SKILLBOOK_GATHER_ORE_NONTRADABLE"
                    title="Adept Ore Miner Tome"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_RESOURCES_FAME_02"
                    name="Gather resources worth 25,000 Fame"
                    id="T5_SKILLBOOK_GATHER_FIBER_NONTRADABLE"
                    title="Expert Fiber Harvester Tome"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_RESOURCES_FAME_03"
                    name="Gather resources worth 50,000 Fame"
                    id="T6_SKILLBOOK_GATHER_ROCK_NONTRADABLE"
                    title="Master Quarrier Tome"
                  />
                  <Entry
                    entryID="SA_GATHERING_FAME_02"
                    name="Gather resources worth 100,000 Fame"
                    id="T7_SKILLBOOK_GATHER_WOOD_NONTRADABLE"
                    title="Grandmaster Lumberjack Tome"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_RESOURCES_FAME_04"
                    name="Gather resources worth 250,000 Fame"
                    id="T8_SKILLBOOK_GATHER_FIBER_NONTRADABLE"
                    title="Elder Fiber Harvester Tome"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_RESOURCES_FAME_05"
                    name="Gather resources worth 500,000 Fame"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    entryID="SA_GATHERING_FAME_03"
                    name="Gather resources worth a million Fame"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x2)"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_RESOURCES_FAME_06"
                    name="Gather resources worth 3 million Fame"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x3)"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_RESOURCES_FAME_07"
                    name="Gather resources worth 10 million Fame"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x5)"
                  />
                  <Entry
                    entryID="SA_GATHERING_TERRITORY_RAID"
                    name="Gather a T8 resource at an enemy territory"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                </tbody>
              </Table>

              <h4>Hide Animals (14)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="JOURNAL_GATHERING_SKINNING_ANIMAL_1"
                    name="Skin 3 types of Hide Animal"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_SKINNING_ANIMAL_2"
                    name="Skin 6 types of Hide Animal"
                    id="T4_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                    title="Adept Animal Skinner Tome"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_SKINNING_ANIMAL_3"
                    name="Skin 10 types of Hide Animal"
                    id="T5_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                    title="Expert Animal Skinner Tome"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_SKINNING_ANIMAL_4"
                    name="Skin 15 types of Hide Animal"
                    id="UNIQUE_UNLOCK_HEAD_VANITY_INNKEEPER_NON_TRADABLE"
                    title="Wardrobe Skin: Innkeeper's Hat"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_SKINNING_ANIMAL_5"
                    name="Skin 22 types of Hide Animal"
                    id="T6_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                    title="Master Animal Skinner Tome"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_SKINNING_ANIMAL_6"
                    name="Skin 30 types of Hide Animal"
                    id="T7_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                    title="Grandmaster Animal Skinner Tome"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_SKINNING_ANIMAL_7"
                    name="Skin 40 types of Hide Animal"
                    id="T8_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                    title="Elder Animal Skinner Tome"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_SKINNING_ANIMAL_8"
                    name="Skin 52 types of Hide Animal"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_SKINNING_ANIMAL_9"
                    name="Skin 65 types of Hide Animal"
                    id="UNIQUE_FOCUSPOTION_ADC_NONTRADABLE_01"
                    title="Grandmaster's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_SKINNING_ANIMAL_ALL"
                    name={
                      <>
                        Skin every type of Hide Animal
                        <br />
                        <span className="text-muted">
                          Bear, Boar, Wolf, Direwolf, Fox, Rabbit, Hill Marmot,
                          Wolpertinger, Snow Rabbit, Marmot, Toad, Fey Fox,
                          Impala, Snake, Cougar, Foglands Doe, Moabird, Giant
                          Toad, Mistcougar Runt, Adult Cougar, Old Mistcougar
                          Runt, Foglands Hart, Giant Stag, Monitor Lizard, Rare
                          Boar, Rare Giant Stag, Rare Monitor Lizard, Grand
                          Foglands Hart, Sabretooth Tiger, Small Mistcougar,
                          Ancient Small Mistcougar, Old Small Mistcougar, Great
                          Mystic Owl, Terrorbird, Giant Snake, Rare Bear, Rare
                          Giant Snake, Majestic Mystic Owl, Rare Terrorbird,
                          Adult Sabretooth Tiger, Mistcougar, Ancient
                          Mistcougar, Old Mistcougar, Ancient Basilisk, Old
                          White, Moose, Feral Wolfhound, Hyena, Swamp Dragon,
                          Old Basilisk Aspect, Old White&apos;s Aspect, Rare
                          Hyena, Rare Direwolf, Rare Swamp Dragon, Insatiable
                          Wolfhound, Mature Sabretooth Tiger, Large Mistcougar,
                          Ancient Large Mistcougar, Old Large Mistcougar, Feral
                          Boar, Misthide Mauler, Rhino, Rare Direboar, Ferocious
                          Misthide Mauler, Rare Rhino, Alpha Mistcougar, Alpha
                          Sabretooth Tiger, Ancient Alpha Mistcougar, Old Alpha
                          Mistcougar, Ancient Giant Basilisk, Feral Bear,
                          Dragonhawk, Mammoth, Old Giant Basilisk Aspect, Rare
                          Ancient Mammoth, Rare Direbear, Regal Dragonhawk
                        </span>
                      </>
                    }
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x5)"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_SKINNING_LOOT_BABY_1"
                    name="Loot a wild Baby Animal"
                    id="UNIQUE_FURNITUREITEM_ADC_RUG_DIREBEAR"
                    title="Direbear Rug"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_SKINNING_LOOT_BABY_2"
                    name="Loot 3 wild Baby Animals"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_SKINNING_LOOT_BABY_3"
                    name="Loot 5 different Baby Animals"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_SKINNING_LOOT_BABY_ALL"
                    name={
                      <>
                        Loot all wild Baby Animals
                        <br />
                        <span className="text-muted">
                          Adept&apos;s Fawn, Swiftclaw Cub, Direwolf Pup, Moose
                          Calf, Direboar Piglet, Swamp Dragon Pup, Direbear Cub,
                          Mammoth Calf
                        </span>
                      </>
                    }
                    id="T5_LEARNINGPOINTS_NONTRADABLE"
                    title="Expert's Tome of Learning"
                  />
                </tbody>
              </Table>

              <h4>Fishing (21)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="SA_FISHING_FAME_01"
                    name="Catch your first fish"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_FISHING_CATCH_1"
                    name="Catch 3 types of fish"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_FISHING_EAT_1"
                    name="Eat 10 fish"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_FISHING_CATCH_2"
                    name="Catch 6 types of fish"
                    id="T5_FOCUSPOTION_NONTRADABLE"
                    title="Expert's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_FISHING_EAT_2"
                    name="Eat 30 fish"
                    id="T3_SILVERBAG_NONTRADABLE"
                    title="Journeyman's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_FISHING_SALTWATER_01"
                    name="Catch a saltwater fish"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_FISHING_USE_BAIT"
                    name="Catch a fish with Fish Bait"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_FISHING_CATCH_3"
                    name="Catch 10 types of fish"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_FISHING_FAME_01"
                    name="Catch fish worth 3,000 Fame"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_FISHING_CATCH_4"
                    name="Catch 15 types of fish"
                    id="UNIQUE_UNLOCK_SHOES_VANITY_BARD_BLUE_NON_TRADABLE"
                    title="Wardrobe Skin: Blue Bard's Shoes"
                  />
                  <Entry
                    entryID="SA_FISHING_FAME_02"
                    name="Catch fish worth 10,000 Fame"
                    id="UNIQUE_FURNITUREITEM_KEEPER_CAULDRON"
                    title="Keeper Cauldron"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_FISHING_CATCH_5"
                    name="Catch 21 types of fish"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_FISHING_FAME_02"
                    name="Catch fish worth 30,000 Fame"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_FISHING_CATCH_6"
                    name="Catch 28 types of fish"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x10)"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_FISHING_CATCH_SHARK"
                    name="Catch a Shark"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_FISHING_CATCH_ALL"
                    name={
                      <>
                        Catch all types of fish
                        <br />
                        <span className="text-muted">
                          Common Rudd, Striped Carp, Albion Perch, Bluescale
                          Pike, Spotted Trout, Brightscale Zander, Danglemouth
                          Catfish, River Sturgeon, Common Herring, Striped
                          Mackerel, Flatshore Plaice, Bluescale Cod, Spotted
                          Wolffish, Strongfin Salmon, Bluefin Tuna, Steelscale
                          Swordfish, Greenriver Eel, Redspring Eel, Deadwater
                          Eel, Upland Coldeye, Mountain Blindeye, Frostpeak
                          Deadeye, Stonestream Lurcher, Rushwater Lurcher,
                          Thunderfall Lurcher, Lowriver Crab, Drybrook Crab,
                          Dusthole Crab, Greenmoor Clam, Murkwater Clam,
                          Blackbog Clam, Whitefog Snapper, Clearhaze Snapper,
                          Puremist Snapper, Shallowshore Squid, Midwater
                          Octopus, Deepwater Kraken, Shark
                        </span>
                      </>
                    }
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x15)"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_FISHING_FAME_03"
                    name="Catch fish worth 100,000 Fame"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_FISHING_FAME_04"
                    name="Catch fish worth 300,000 Fame"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="SA_FISHING_FAME_03"
                    name="Catch fish worth a million Fame"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_FISHING_FAME_06"
                    name="Catch fish worth 3 million Fame"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_FISHING_FAME_07"
                    name="Catch fish worth 10 million Fame"
                    id="T3_VANITY_CONSUMABLE_FIREWORKS_BLUE_NONTRADABLE"
                    title="Royal Blue Fireworks (x99)"
                  />
                </tbody>
              </Table>

              <h4>Resource Creatures (21)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="JOURNAL_GATHERING_CRITTERS_CRITTERS_ANY"
                    name="Harvest 30 resources from Resource Mobs"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_CRITTERS_CRITTERS_UNIQUE_1"
                    name="Harvest resources from 3 Resource Mob types"
                    id="T3_MEAL_PIE"
                    title="Chicken Pie"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_CRITTERS_CRITTERS_UNIQUE_2"
                    name="Harvest resources from 7 Resource Mob types"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_CRITTERS_CRITTERS_UNIQUE_3"
                    name="Harvest resources from 12 Resource Mob types"
                    id="T5_FOCUSPOTION_NONTRADABLE"
                    title="Expert's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_CRITTERS_GATHER_MINIGUARDIANS_01"
                    name="Harvest a resource from an Aspect"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_CRITTERS_CRITTERS_UNIQUE_4"
                    name="Harvest resources from 18 Resource Mob types"
                    id="T7_SKILLBOOK_GATHER_FIBER_NONTRADABLE"
                    title="Grandmaster Fiber Harvester Tome"
                  />
                  <Entry
                    entryID="SA_PVE_KILL_MINIGUARDIANS"
                    name={
                      <>
                        Harvest resources from Aspects in every biome
                        <br />
                        <span className="text-muted">
                          Steppe, Swamp, Mountain, Forest, Highland, Roads of
                          Avalon
                        </span>
                      </>
                    }
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_CRITTERS_CRITTERS_UNIQUE_5"
                    name="Harvest resources from 25 Resource Mob types"
                    id="T7_SKILLBOOK_GATHER_WOOD_NONTRADABLE"
                    title="Grandmaster Lumberjack Tome"
                  />
                  <Entry
                    entryID="SA_PVE_ROADS_GUARDIAN"
                    name="Harvest resources from a Guardian in the Roads of Avalon"
                    id="T6_FOCUSPOTION_NONTRADABLE"
                    title="Master's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_CRITTERS_CRITTERS_UNIQUE_6"
                    name="Harvest resources from 34 Resource Mob types"
                    id="T7_SKILLBOOK_GATHER_ORE_NONTRADABLE"
                    title="Grandmaster Ore Miner Tome"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_CRITTERS_GATHER_MINIGUARDIANS_02"
                    name="Harvest 3,000 resources from Aspects"
                    id="T6_FOCUSPOTION_NONTRADABLE"
                    title="Master's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_CRITTERS_CRITTERS_UNIQUE_7"
                    name="Harvest resources from 46 Resource Mob types"
                    id="T7_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                    title="Grandmaster Animal Skinner Tome"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_CRITTERS_GATHER_GUARDIANS_01"
                    name="Harvest 3,000 resources from Ancient Resource Mobs"
                    id="T7_SKILLBOOK_GATHER_ROCK_NONTRADABLE"
                    title="Grandmaster Quarrier Tome"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_CRITTERS_CRITTERS_UNIQUE_ALL"
                    name={
                      <>
                        Harvest resources from all Resource Mob types
                        <br />
                        <span className="text-muted">
                          Swamp Spirit, Ore Elemental, Rock Elemental, Forest
                          Spirit, Hemp Dryad, Old Hemp Dryad, Iron Elemental,
                          Old Iron Elemental, Travertine Elemental, Old
                          Travertine Elemental, Pine Spirit, Old Pine Spirit,
                          Skyflower Dryad, Ancient Skyflower Dryad, Old
                          Skyflower Dryad, Mature Ore Elemental, Ancient
                          Titanium Elemental, Old Titanium Elemental, Mature
                          Rock Elemental, Ancient Granite Elemental, Old Granite
                          Elemental, Mature Forest Spirit, Ancient Cedar Spirit,
                          Old Cedar Spirit, Amberleaf Dryad, Ancient Amberleaf
                          Dryad, Old Amberleaf Dryad, Runite Elemental, Ancient
                          Runite Elemental, Old Runite Elemental, Slate
                          Elemental, Ancient Slate Elemental, Old Slate
                          Elemental, Bloodoak Spirit, Ancient Bloodoak Spirit,
                          Old Bloodoak Spirit, Elder Swamp Spirit, Sunflax
                          Dryad, Ancient Sunflax Dryad, Old Sunflax Dryad, Elder
                          Ore Elemental, Ancient Meteorite Elemental, Old
                          Meteorite Elemental, Elder Rock Elemental, Ancient
                          Basalt Elemental, Old Basalt Elemental, Elder Forest
                          Spirit, Ancient Ashenbark Spirit, Old Ashenbark
                          Spirit, Ghost Hemp Dryad, Ancient Ghost Hemp Dryad,
                          Old Ghost Hemp Dryad, Adamantium Elemental, Ancient
                          Adamantium Elemental, Old Adamantium Elemental, Marble
                          Elemental, Ancient Marble Elemental, Old Marble
                          Elemental, Whitewood Spirit, Ancient Whitewood Spirit,
                          Old Whitewood Spirit
                        </span>
                      </>
                    }
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x200)"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_CRITTERS_CRITTERS_ANY_02"
                    name="Harvest 100 resources from Resource Mobs"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_CRITTERS_CRITTERS_ANY_03"
                    name="Harvest 300 resources from Resource Mobs"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_CRITTERS_CRITTERS_ANY_04"
                    name="Harvest 1,000 resources from Resource Mobs"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_CRITTERS_CRITTERS_ANY_05"
                    name="Harvest 10,000 resources from Resource Mobs"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_CRITTERS_GATHER_MINIGUARDIANS_03"
                    name="Harvest 10,000 resources from Aspects"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_CRITTERS_GATHER_GUARDIANS_02"
                    name="Harvest 10,000 resources from Ancient Resource Mobs"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_CRITTERS_GATHER_GUARDIANS_03"
                    name="Harvest 30,000 resources from Ancient Resource Mobs"
                    id="UNIQUE_FOCUSPOTION_ADC_NONTRADABLE_01"
                    title="Grandmaster's Focus Restoration Potion"
                  />
                </tbody>
              </Table>

              <h4>Dynamic Resource Hotspots (10)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="JOURNAL_GATHERING_RESOURCES_DYNAMIC_CAMP_01"
                    name="Gather a resource from a Dynamic Resource Hotspot"
                    id="T4_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                    title="Adept Animal Skinner Tome"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_RESOURCES_DYNAMIC_CAMP_02"
                    name="Gather 500 resources from Dynamic Resource Hotspots"
                    id="T5_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                    title="Expert Animal Skinner Tome"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_DYNAMIC_CAMP_RESOURCEMIST_01"
                    name="Enter a Resource Mist from a Dynamic Resource Hotspot in the Outlands"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_DYNAMIC_CAMP_RESOURCEMIST_02"
                    name="Gather 100 resources inside Resource Mists"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_RESOURCES_DYNAMIC_CAMP_03"
                    name="Gather 1,000 resources from Dynamic Resource Hotspots"
                    id="T6_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                    title="Master Animal Skinner Tome"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_DYNAMIC_CAMP_RESOURCEMIST_03"
                    name="Gather 500 resources inside Resource Mists"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_RESOURCES_DYNAMIC_CAMP_04"
                    name="Gather 10,000 resources from a Dynamic Resource Hotspot"
                    id="T7_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                    title="Grandmaster Animal Skinner Tome"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_DYNAMIC_CAMP_RESOURCEMIST_04"
                    name="Gather 1,000 resources inside Resource Mists"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_RESOURCES_DYNAMIC_CAMP_05"
                    name="Gather 50,000 resources from a Dynamic Resource Hotspot"
                    id="T8_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                    title="Elder Animal Skinner Tome"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_DYNAMIC_CAMP_RESOURCEMIST_05"
                    name="Gather 10,000 resources inside Resource Mists"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                </tbody>
              </Table>

              <h4>Biomes (26)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="JOURNAL_GATHERING_BIOMES_YELLOW_OPENWORLD"
                    name="Gather 250 resources in a yellow zone"
                    id="UNIQUE_FURNITUREITEM_HERETICS_TOOL_BOARD_A"
                    title="Heretic Toolboard"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_BIOMES_YELLOW_MIST"
                    name="Gather 250 resources in the yellow Mists"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_BIOMES_YELLOW_FACTION"
                    name="Gather 250 resources in a yellow zone while faction flagged"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_BIOMES_RED_OPENWORLD"
                    name="Gather 250 resources in a red zone"
                    id="T5_SKILLBOOK_GATHER_WOOD_NONTRADABLE"
                    title="Expert Lumberjack Tome"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_BIOMES_RED_FACTION"
                    name="Gather 250 resources in a red zone while faction flagged"
                    id="T5_SKILLBOOK_GATHER_ROCK_NONTRADABLE"
                    title="Expert Quarrier Tome"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_BIOMES_BLACK_OPENWORLD"
                    name="Gather 250 resources in a black zone"
                    id="T5_SKILLBOOK_GATHER_ORE_NONTRADABLE"
                    title="Expert Ore Miner Tome"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_BIOMES_BLACK_MIST"
                    name="Gather 250 resources in the black Mists"
                    id="T5_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                    title="Expert Animal Skinner Tome"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_BIOMES_BLACK_ROADS"
                    name="Gather 250 resources in the Roads of Avalon"
                    id="T5_SKILLBOOK_GATHER_FIBER_NONTRADABLE"
                    title="Expert Fiber Harvester Tome"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_BIOMES_MOUNTAIN_1"
                    name="Gather 250 resources in Mountain regions"
                    id="T4_SKILLBOOK_GATHER_ORE_NONTRADABLE"
                    title="Adept Ore Miner Tome"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_BIOMES_FOREST_1"
                    name="Gather 250 resources in Forest regions"
                    id="T4_SKILLBOOK_GATHER_WOOD_NONTRADABLE"
                    title="Adept Lumberjack Tome"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_BIOMES_STEPPE_1"
                    name="Gather 250 resources in Steppe regions"
                    id="T4_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                    title="Adept Animal Skinner Tome"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_BIOMES_HIGHLAND_1"
                    name="Gather 250 resources in Highland regions"
                    id="T4_SKILLBOOK_GATHER_ROCK_NONTRADABLE"
                    title="Adept Quarrier Tome"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_BIOMES_SWAMP_1"
                    name="Gather 250 resources in Swamp regions"
                    id="T4_SKILLBOOK_GATHER_FIBER_NONTRADABLE"
                    title="Adept Fiber Harvester Tome"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_BIOMES_MOUNTAIN_2"
                    name="Gather 1,000 resources in Mountain regions"
                    id="T6_SKILLBOOK_GATHER_ORE_NONTRADABLE"
                    title="Master Ore Miner Tome"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_BIOMES_FOREST_2"
                    name="Gather 1,000 resources in Forest regions"
                    id="T6_SKILLBOOK_GATHER_WOOD_NONTRADABLE"
                    title="Master Lumberjack Tome"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_BIOMES_STEPPE_2"
                    name="Gather 1,000 resources in Steppe regions"
                    id="T6_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                    title="Master Animal Skinner Tome"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_BIOMES_HIGHLAND_2"
                    name="Gather 1,000 resources in Highland regions"
                    id="T6_SKILLBOOK_GATHER_ROCK_NONTRADABLE"
                    title="Master Quarrier Tome"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_BIOMES_SWAMP_2"
                    name="Gather 1,000 resources in Swamp regions"
                    id="T6_SKILLBOOK_GATHER_FIBER_NONTRADABLE"
                    title="Master Fiber Harvester Tome"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_BIOMES_BLACK_OPENWORLD_02"
                    name="Gather 1,000 resources in Black Zones"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_BIOMES_MOUNTAIN_3"
                    name="Gather 10,000 resources in Mountain regions"
                    id="T8_SKILLBOOK_GATHER_ORE_NONTRADABLE"
                    title="Elder Ore Miner Tome"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_BIOMES_FOREST_3"
                    name="Gather 10,000 resources in Forest regions"
                    id="T8_SKILLBOOK_GATHER_WOOD_NONTRADABLE"
                    title="Elder Lumberjack Tome"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_BIOMES_STEPPE_3"
                    name="Gather 10,000 resources in Steppe regions"
                    id="T8_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                    title="Elder Animal Skinner Tome"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_BIOMES_HIGHLAND_3"
                    name="Gather 10,000 resources in Highland regions"
                    id="T8_SKILLBOOK_GATHER_ROCK_NONTRADABLE"
                    title="Elder Quarrier Tome"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_BIOMES_SWAMP_3"
                    name="Gather 10,000 resources in Swamp regions"
                    id="T8_SKILLBOOK_GATHER_FIBER_NONTRADABLE"
                    title="Elder Fiber Harvester Tome"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_BIOMES_BLACK_OPENWORLD_03"
                    name="Gather 10,000 resources in Black Zones"
                    id="T6_FOCUSPOTION_NONTRADABLE"
                    title="Master's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_GATHERING_BIOMES_BLACK_OPENWORLD_04"
                    name="Gather 50,000 resources in Black Zones"
                    id="T5_LEARNINGPOINTS_NONTRADABLE"
                    title="Expert's Tome of Learning"
                  />
                </tbody>
              </Table>
            </AccordionBody>
          </AccordionItem>
        </UncontrolledAccordion>
      </Section>

      {/* Exploration */}
      <Section>
        <UncontrolledAccordion id="exploration">
          <AccordionItem>
            <AccordionHeader targetId="exploration">
              Exploration (172)
            </AccordionHeader>
            <AccordionBody accordionId="exploration">
              <h4>Cities (12)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="JOURNAL_EXPLORATION_CITIES_VISIT_ROYAL_CITY_01"
                    name="Visit a Royal City"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_CITIES_VISIT_ROYAL_CITY_02"
                    name="Visit two Royal Cities"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x10)"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_CITIES_VISIT_CAERLEON"
                    name="Visit Caerleon"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_CITIES_VISIT_PORTAL_CITY"
                    name="Visit a Portal Town"
                    id="T3_VANITY_CONSUMABLE_FIREWORKS_YELLOW_NONTRADABLE"
                    title="Royal Yellow Fireworks (x3)"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_CITIES_PORTAL_CITY_INVIS_SHRINE"
                    name="Use the Invisibility Shrine in a Portal Town"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_CITIES_OUTLANDS_TELEPORTATION_PORTAL"
                    name="Use the S.A.F.E. Portal in a Portal Town"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_CITIES_OUTLANDS_TELEPORTATION_RETURN_PORTAL"
                    name="Use the S.A.F.E. Portal to return to a Portal Town"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="SA_EXPLORATION_MISTS_FIND_CITY"
                    name="Find the lost city of Brecilien"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_CITIES_MIST_CITY_NPC"
                    name="Purchase an item from Eralia Wayfarer in Brecilien"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="SA_EXPLORATION_CITIES"
                    name={
                      <>
                        Visit all six Royal Cities
                        <br />
                        <span className="text-muted">
                          Martlock, Lymhurst, Thetford, Fort Sterling,
                          Bridgewatch, Caerleon
                        </span>
                      </>
                    }
                    id="UNIQUE_UNLOCK_SHOES_VANITY_PRIEST_NON_TRADABLE"
                    title="Wardrobe Skin: Monk's Sandals"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_CITIES_VISIT_REST_CITY_01"
                    name="Visit a Rest in the Outlands"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_CITIES_VISIT_REST_CITY_ALL"
                    name={
                      <>
                        Visit all Rests in the Outlands
                        <br />
                        <span className="text-muted">
                          Arthur&apos;s Rest, Merlyn&apos;s Rest, Morgana&apos;s
                          Rest
                        </span>
                      </>
                    }
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                </tbody>
              </Table>

              <h4>Travel (36)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="JOURNAL_EXPLORATION_TRAVEL_RIDE_HORSE"
                    name="Ride a Horse"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_TRAVEL_HIDDEN_TREASURE_01"
                    name="Find a Hidden Treasure in the open world"
                    id="T3_SILVERBAG_NONTRADABLE"
                    title="Journeyman's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_TRAVEL_RIDE_OX"
                    name="Ride an Ox"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_TRAVEL_DISTANCE_01"
                    name="Travel 20 kilometers"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="SA_COLLECTION_DIREWOLF"
                    name="Ride a Direwolf"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_TRAVEL_OPENWORLD_COFFERS_01"
                    name="Find a Coffer Chest in the open world"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_TRAVEL_HIDDEN_TREASURE_02"
                    name="Find 5 Hidden Treasures in the open world"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_TRAVEL_RIDE_ADC_MOUNT"
                    name={
                      <>
                        Ride an Adventurer&apos;s Challenge Mount
                        <br />
                        <span className="text-muted">
                          Frost Ram, Saddled Terrorbird, Grizzly Bear, Black
                          Panther, Morgana Raven, Gallant Horse, Spectral
                          Direboar, Divine Owl, Heretic Combat Mule, Spectral
                          Bat, Pest Lizard, Snow Husky
                        </span>
                      </>
                    }
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_TRAVEL_OPENWORLD_COFFERS_02"
                    name="Find 5 Coffer Chests in the open world"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_TRAVEL_HIDDEN_TREASURE_03"
                    name="Find 10 Hidden Treasures in the open world"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_TRAVEL_RIDE_FW_MOUNT"
                    name="Ride a Faction Warfare mount"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_TRAVEL_OPENWORLD_COFFERS_03"
                    name="Find 10 Coffer Chests in the open world"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_TRAVEL_HIDDEN_TREASURE_04"
                    name="Find 20 Hidden Treasures in the open world"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_TRAVEL_RIDE_BRECILIEN_MOUNT"
                    name="Ride a Mystic Owl from Brecilien"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_TRAVEL_OPENWORLD_COFFERS_04"
                    name="Find 20 Coffer Chests in the open world"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_TRAVEL_HIDDEN_TREASURE_05"
                    name="Find 40 Hidden Treasures in the open world"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_TRAVEL_RIDE_FW_ELITE_MOUNT"
                    name="Ride an Elite Faction Warfare mount"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_TRAVEL_OPENWORLD_COFFERS_05"
                    name="Find 40 Coffer Chests in the open world"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_TRAVEL_HIDDEN_TREASURE_06"
                    name="Find 65 Hidden Treasures in the open world"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_TRAVEL_RIDE_BATTLE_MOUNT"
                    name="Ride a Battle Mount"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_TRAVEL_OPENWORLD_COFFERS_06"
                    name="Find 65 Coffer Chests in the open world"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x2)"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_TRAVEL_HIDDEN_TREASURE_07"
                    name="Find 100 Hidden Treasures in the open world"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x5)"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_TRAVEL_RIDE_FW_ALL"
                    name={
                      <>
                        Ride all Faction Warfare Mounts
                        <br />
                        <span className="text-muted">
                          Saddled Moabird, Saddled Winter Bear, Saddled Wild
                          Boar, Saddled Bighorn Ram, Saddled Swamp Salamander,
                          Saddled Greywolf, Elite Terrorbird, Elite Winter Bear,
                          Elite Wild Boar, Elite Bighorn Ram, Elite Swamp
                          Salamander, Elite Greywolf
                        </span>
                      </>
                    }
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_TRAVEL_OPENWORLD_COFFERS_07"
                    name="Find 100 Coffer Chests in the open world"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_TRAVEL_HIDDEN_TREASURE_08"
                    name="Find 200 Hidden Treasures in the open world"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x8)"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_TRAVEL_RIDE_MAMMOTH_TRANSPORT"
                    name="Ride a Transport Mammoth"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_TRAVEL_OPENWORLD_COFFERS_08"
                    name="Find 200 Coffer Chests in the open world"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_TRAVEL_HIDDEN_TREASURE_09"
                    name="Find 500 Hidden Treasures in the open world"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x15)"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_TRAVEL_RIDE_MAMMOTH_BATTLE"
                    name="Ride a Command Mammoth"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_TRAVEL_DISTANCE_02"
                    name="Travel 50 kilometers"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_TRAVEL_DISTANCE_03"
                    name="Travel 100 kilometers"
                    id="UNIQUE_UNLOCK_OFF_VANITY_PRIEST_NON_TRADABLE"
                    title="Wardrobe Skin: Monk's Walking Staff"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_TRAVEL_DISTANCE_04"
                    name="Travel 200 kilometers"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_TRAVEL_DISTANCE_05"
                    name="Travel 500 kilometers"
                    id="UNIQUE_FURNITUREITEM_ADC_CARNIVAL_MASK_CART"
                    title="Carnival Costume Cart"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_TRAVEL_DISTANCE_06"
                    name="Travel 1,000 kilometers"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_TRAVEL_DISTANCE_07"
                    name="Travel 3,000 Kilometers"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_TRAVEL_DISTANCE_08"
                    name="Travel 10,000 Kilometers"
                    id="UNIQUE_FURNITUREITEM_ADC_STATUE_MOUNTED_DIREWOLF_B"
                    title="Wolf Rider Statue (R)"
                  />
                </tbody>
              </Table>

              <h4>Zone Types (12)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="JOURNAL_EXPLORATION_ENTER_YELLOW"
                    name="Enter a Yellow Zone"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_ZONE_TYPES_YELLOW_FAME"
                    name="Earn 10,000 Fame in Yellow Zones"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_ZONE_TYPES_ENTER_RED"
                    name="Enter a Red Zone"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_ZONE_TYPES_RED_FAME"
                    name="Earn 40,000 Fame in Red Zones"
                    id="UNIQUE_UNLOCK_SKIN_HORSE_KEEPER_NON_TRADABLE"
                    title="Riding Horse Skin: Keeper Horse"
                  />
                  <Entry
                    entryID="SA_EXPLORATION_BLACKZONE"
                    name="Enter a black zone"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_ZONE_TYPES_BLACK_JOURNEY_BACK"
                    name="Use the Journey Back ability in a Black Zone"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_ZONE_TYPES_BLACK_FAME"
                    name="Earn 100,000 Fame in Black Zones"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_ZONE_TYPES_BLACK_Q2_FAME"
                    name="Earn 100,000 Fame in Quality Level 2 Black Zones"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_ZONE_TYPES_BLACK_Q3_FAME"
                    name="Earn 120,000 Fame in Quality Level 3 Black Zones"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_ZONE_TYPES_BLACK_Q4_FAME"
                    name="Earn 250,000 Fame in Quality Level 4 Black Zones"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_ZONE_TYPES_BLACK_Q5_FAME"
                    name="Earn 500,000 Fame in Quality Level 5 Black Zones"
                    id="T5_LEARNINGPOINTS_NONTRADABLE"
                    title="Expert's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_ZONE_TYPES_BLACK_Q6_FAME"
                    name="Earn a million Fame in Quality Level 6 Black Zones"
                    id="T5_LEARNINGPOINTS_NONTRADABLE"
                    title="Expert's Tome of Learning"
                  />
                </tbody>
              </Table>

              <h4>Reputation (7)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="SA_REPUTATION_GOOD"
                    name="Reach the first positive reputation level"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_REPUTATION_GOOD_01"
                    name="Reach the reputation level: Virtuous"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_REPUTATION_GOOD_02"
                    name="Reach the reputation level: Noble"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    entryID="SA_REPUTATION_MAX"
                    name="Reach maximum reputation level"
                    id="UNIQUE_REPAIRPOWDER_ADC_GENERAL_01_NONTRADEABLE"
                    title="Scroll of Repair"
                  />
                  <Entry
                    entryID="SA_REPUTATION_BAD"
                    name="Reach the first negative reputation level"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_REPUTATION_BAD_01"
                    name="Reach the reputation level: Nefarious"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="SA_REPUTATION_MIN"
                    name="Reach minimum reputation level"
                    id="UNIQUE_UNLOCK_ARMOR_VANITY_ENTERTAINER_NON_TRADABLE"
                    title="Wardrobe Skin: Entertainer's Costume"
                  />
                </tbody>
              </Table>

              <h4>Mists (33)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="SA_EXPLORATION_MISTS_ENTER"
                    name="Follow a Will o' Wisp into the Mists"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_MISTS_RESCUE_WISPS_1"
                    name="Rescue 10 Wisps"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_MISTS_RESCUE_CHEST_SMALL_01"
                    name="Open 3 Small Caches"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_MISTS_RESCUE_CHEST_MEDIUM_01"
                    name="Open 3 Medium Caches"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_MISTS_ENTER_MIST_DUNGEON"
                    name="Enter Knightfall Abbey"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_MISTS_DUNGEON_CHESTS_01"
                    name="Open 3 chests in Knightfall Abbey"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_MISTS_CAPTURE_TREASURE_WISP"
                    name="Deliver a Weakened Wisp to a Sanctuary"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    entryID="SA_EXPLORATION_MISTS_CITY_FRIENDLY"
                    name="Gain Accepted status with Brecilien"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_MISTS_FAME_SOLO_BLACK_01"
                    name="Earn 50,000 Fame in Solo Lethal Mists"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_MISTS_RESCUE_WISPS_SOLO_BLACK_01"
                    name="Rescue 30 Wisps in Solo Lethal Mists"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_MISTS_CAPTURE_TREASURE_WISP_SOLO_BLACK"
                    name="Deliver a Weakened Wisp in Lethal Mists"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_MISTS_DUNGEON_CHESTS_02"
                    name="Open 20 chests in Knightfall Abbey"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_MISTS_FAME_DUO_BLACK_01"
                    name="Gain 50,000 Fame in Greater Mists"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_MISTS_RESCUE_WISPS_DUO_BLACK_01"
                    name="Rescue 50 Wisps in Greater Mists"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_MISTS_CAPTURE_TREASURE_WISP_DUO_BLACK_01"
                    name="Deliver 5 Weakened Wisps in Greater Mists"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_MISTS_DUNGEON_CHESTS_03"
                    name="Open 100 chests in Knightfall Abbey"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_MISTS_CAPTURE_TREASURE_WISP_SOLO_BLACK_01"
                    name="Deliver 50 Weakened Wisps in Solo Lethal Mists"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_MISTS_FAME_SOLO_BLACK_02"
                    name="Earn 500,000 fame in Solo Lethal Mists"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_MISTS_FAME_SOLO_BLACK_03"
                    name="Earn a million Fame in Solo Lethal Mists"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_MISTS_FAME_SOLO_BLACK_04"
                    name="Earn 5 million Fame in Solo Lethal Mists"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_MISTS_FAME_SOLO_BLACK_05"
                    name="Earn 10 million Fame in Solo Lethal Mists"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_MISTS_FAME_DUO_BLACK_02"
                    name="Earn 500,000 Fame in Greater Mists"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_MISTS_FAME_DUO_BLACK_03"
                    name="Earn a million Fame in Greater Mists"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_MISTS_FAME_DUO_BLACK_04"
                    name="Earn 5 million Fame in Greater Mists"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_MISTS_FAME_DUO_BLACK_05"
                    name="Earn 10 million Fame in Greater Mists"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_MISTS_DUNGEON_CHESTS_04"
                    name="Open 500 chests in Knightfall Abbey"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_MISTS_DUNGEON_CHESTS_05"
                    name="Open 2,000 chests in Knightfall Abbey"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_MISTS_STANDING_01"
                    name="Get 'Welcomed' Brecilien standing"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_MISTS_STANDING_02"
                    name="Get 'Favored' Brecilien standing"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_MISTS_STANDING_03"
                    name="Gain 'Esteemed' Brecilien standing"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_MISTS_STANDING_04"
                    name="Gain 'Venerated' Brecilien standing"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    entryID="SA_PVE_MISTS_HUNTER"
                    name={
                      <>
                        ...and how to kill them
                        <br />
                        <span className="text-muted">
                          Veilweaver, Fey Dragon, Griffin
                        </span>
                      </>
                    }
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight (x5)"
                  />
                  <Entry
                    entryID="SA_EXPLORATION_MISTS_KILL_STRANGER"
                    name='Kill a "Mysterious Stranger" that&apos;s your friend or ally'
                    id="UNIQUE_FURNITUREITEM_ADC_GRIM_WEEPINGWOMAN"
                    title="Weeping Woman Statue"
                  />
                </tbody>
              </Table>

              <h4>Might & Favor (14)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="JOURNAL_EXPLORATION_MIGHT_GAIN_MIGHT_01"
                    name="Earn 100 Might"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_MIGHT_GAIN_FAVOR_01"
                    name="Earn 90 Favor"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_MIGHT_BUY_FAVOR_ITEM"
                    name="Trade your Favor for an item at the Energy Manipulator"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_MIGHT_GAIN_MIGHT_02"
                    name="Earn 1,000 Might"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_MIGHT_BUY_FAVOR_ITEM_02"
                    name="Trade your Favor for a Conqueror's Chest at the Energy Manipulator"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_MIGHT_GAIN_MIGHT_03"
                    name="Earn 8,000 Might"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_MIGHT_GAIN_FAVOR_02"
                    name="Earn 5,000 Favor"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_MIGHT_GAIN_MIGHT_04"
                    name="Earn 40,000 Might"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_MIGHT_GAIN_MIGHT_05"
                    name="Earn 100,000 Might"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_MIGHT_GAIN_MIGHT_06"
                    name="Earn 200,000 Might"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_MIGHT_GAIN_FAVOR_03"
                    name="Earn 120,000 Favor"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_MIGHT_GAIN_MIGHT_07"
                    name="Earn 1 million Might"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_MIGHT_GAIN_MIGHT_08"
                    name="Earn 2 million Might"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x5)"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_MIGHT_GAIN_MIGHT_09"
                    name="Earn 5 million Might"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x25)"
                  />
                </tbody>
              </Table>

              <h4>Roads of Avalon (26)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="SA_COLLECTION_ROADS_01"
                    name="Enter a Road of Avalon"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_ROADS_OF_AVALON_CHEST_MOBS_01"
                    name="Defeat 50 mobs in the Roads of Avalon"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_ROADS_OF_AVALON_CHEST_01"
                    name="Open an Avalonian Chest in the Roads of Avalon"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="SA_COLLECTION_ROADS_02"
                    name="Enter a Deep Road of Avalon"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_ROADS_OF_AVALON_CHEST_MOBS_02"
                    name="Defeat 500 mobs in the Roads of Avalon"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_ROADS_OF_AVALON_CHEST_VETERAN_01"
                    name="Open a Blue Avalonian Chest in the Roads of Avalon"
                    id="UNIQUE_FURNITUREITEM_XMAS_PRESENT"
                    title="Present Box"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_ROADS_OF_AVALON_CHEST_RARE_01"
                    name="Open a Rare Avalonian Chest in the Roads of Avalon"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_ROADS_OF_AVALON_CHEST_SOLO_01"
                    name="Open 30 Green Chests in Roads of Avalon"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_ROADS_OF_AVALON_CHEST_MOBS_03"
                    name="Defeat 2,000 mobs in the Roads of Avalon"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_ROADS_OF_AVALON_CHEST_ELITE_01"
                    name="Open a Yellow Avalonian Chest in the Roads of Avalon"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_ROADS_OF_AVALON_CHEST_MOBS_04"
                    name="Defeat 5,000 mobs in the Roads of Avalon"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x3)"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_ROADS_OF_AVALON_CHEST_VETERAN_02"
                    name="Open 50 Blue Chests in Roads of Avalon"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_ROADS_OF_AVALON_CHEST_SOLO_02"
                    name="Open 100 Green Chests in Roads of Avalon"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x5)"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_ROADS_OF_AVALON_CHEST_LEGENDARY_01"
                    name="Open a Legendary Chest in the Roads"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_ROADS_OF_AVALON_CHEST_VETERAN_03"
                    name="Open 150 Blue Chests in Roads of Avalon"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x10)"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_ROADS_OF_AVALON_CHEST_ELITE_LEGENDARY_01"
                    name="Open a Legendary Yellow Chest in the Roads of Avalon"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_ROADS_OF_AVALON_CHEST_ELITE_02"
                    name="Open 50 Yellow Chests in Roads of Avalon"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x15)"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_ROADS_OF_AVALON_CHEST_SOLO_03"
                    name="Open 500 Green Chests in Roads of Avalon"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x20)"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_ROADS_OF_AVALON_CHEST_ELITE_03"
                    name="Open 150 Yellow Chests in Roads of Avalon"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x20)"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_ROADS_OF_AVALON_CHEST_VETERAN_04"
                    name="Open 500 Blue Chests in Roads of Avalon"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x25)"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_ROADS_OF_AVALON_CHEST_ELITE_04"
                    name="Open 500 Yellow Chests in Roads of Avalon"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x25)"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_ROADS_OF_AVALON_FAME_01"
                    name="Earn 1 million Fame in the Roads of Avalon"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_ROADS_OF_AVALON_FAME_02"
                    name="Earn 3 million Fame in the Roads of Avalon"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_ROADS_OF_AVALON_FAME_03"
                    name="Earn 10 million Fame in the Roads of Avalon"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_ROADS_OF_AVALON_FAME_04"
                    name="Earn 30 million Fame in the Roads of Avalon"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x50)"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_ROADS_OF_AVALON_FAME_05"
                    name="Earn 100 million Fame in the Roads of Avalon"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x15)"
                  />
                </tbody>
              </Table>

              <h4>Smugglers (32)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="JOURNAL_EXPLORATION_SMUGGLERS_VISIT_BLACKBANKS_01"
                    name="Enter a Smuggler's Den"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_SMUGGLERS_CAGED_SMUGGLER_01"
                    name="Free a Captured Smuggler"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_SMUGGLERS_DELIVER_TOKEN_01"
                    name="Buy a Round for the Smugglers"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_SMUGGLERS_VISIT_BLACKBANKS_02"
                    name="Visit 3 Smuggler's Dens"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_SMUGGLERS_CAGED_SMUGGLER_02"
                    name="Free 4 Captured Smugglers"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_SMUGGLERS_DELIVER_TOKEN_02"
                    name="Buy 5 Rounds for the Smugglers"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_SMUGGLERS_DELIVER_CRATE_01"
                    name="Help deliver a Smuggler Crate"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_SMUGGLERS_STANDING_01"
                    name="Gain Accepted Standing with the Smugglers"
                    id="QUESTITEM_TOKEN_SMUGGLER"
                    title="Smuggler's Coin"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_SMUGGLERS_VISIT_BLACKBANKS_03"
                    name="Visit 6 Smuggler's Dens"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_SMUGGLERS_CAGED_SMUGGLER_03"
                    name="Free 10 Captured Smugglers"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_SMUGGLERS_DELIVER_TOKEN_03"
                    name="Buy 15 Rounds for the Smugglers"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_SMUGGLERS_DELIVER_CRATE_02"
                    name="Help deliver 4 Smuggler Crates"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_SMUGGLERS_VISIT_BLACKBANKS_04"
                    name="Visit 10 Smuggler's Dens"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_SMUGGLERS_CAGED_SMUGGLER_04"
                    name="Free 25 Captured Smugglers"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_SMUGGLERS_VISIT_BLACKBANKS_05"
                    name="Visit 15 Smuggler's Dens"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_SMUGGLERS_DELIVER_TOKEN_04"
                    name="Buy 50 Rounds for the Smugglers"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_SMUGGLERS_DELIVER_CRATE_03"
                    name="Help deliver 12 Smuggler Crates"
                    id="QUESTITEM_TOKEN_SMUGGLER"
                    title="Smuggler's Coin (x5)"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_SMUGGLERS_STANDING_02"
                    name="Gain Respected Standing with the Smugglers"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_SMUGGLERS_VISIT_BLACKBANKS_06"
                    name="Visit 21 Smuggler's Dens"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_SMUGGLERS_DELIVER_CRATE_RARITY_01"
                    name="Help deliver a Rare Smuggler Crate"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_SMUGGLERS_CAGED_SMUGGLER_05"
                    name="Free 65 Captured Smugglers"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_SMUGGLERS_DELIVER_CRATE_04"
                    name="Help deliver 40 Smuggler Crates"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_SMUGGLERS_DELIVER_TOKEN_05"
                    name="Buy 180 Rounds for the Smugglers"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_SMUGGLERS_DELIVER_CRATE_RARITY_02"
                    name="Help deliver a Legendary Smuggler Crate"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_SMUGGLERS_STANDING_03"
                    name="Gain Esteemed Standing with the Smugglers"
                    id="QUESTITEM_TOKEN_SMUGGLER"
                    title="Smuggler's Coin (x10)"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_SMUGGLERS_VISIT_BLACKBANKS_07"
                    name="Visit 28 Smuggler's Dens"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight (x5)"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_SMUGGLERS_CAGED_SMUGGLER_06"
                    name="Free 150 Captured Smugglers"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x3)"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_SMUGGLERS_DELIVER_TOKEN_06"
                    name="Buy 500 Rounds for the Smugglers"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x2)"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_SMUGGLERS_DELIVER_CRATE_05"
                    name="Help deliver 120 Smuggler Crates"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight (x5)"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_SMUGGLERS_VISIT_BLACKBANKS_08"
                    name={
                      <>
                        Visit 35 Smuggler&apos;s Dens
                        <br />
                        <span className="text-muted">
                          Meltwater Bog, Willowshade Icemarsh, Springsump Basin,
                          Runnelvein Sink, Willowshade Hills, Sunkenbough Woods,
                          Scuttlesink Marsh, Deadpine Forest, Westweald Thicket,
                          Timberslope Grove, Timberscar Copse, Deepwood Copse,
                          Driftwood Hollow, Rivercopse Fount, Drybasin Riverbed,
                          Sunfang Ravine, Thirstwater Steppe, Bleachskull
                          Desert, Farshore Heath, Slakesands Mesa, Sunfang
                          Wasteland, Dryvein Confluence, Sunstrand Quicksands,
                          Murdergulch Cross, Razorrock Verge, Razorrock Bank,
                          Gravemound Knoll, Murdergulch Ravine, Highstone Loch,
                          Floatshoal Floe, Iceburn Firth, Everwinter Peak,
                          Munten Fell, Frostspring Volcano, Whitepeak Tundra
                        </span>
                      </>
                    }
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight (x5)"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_SMUGGLERS_DELIVER_CRATE_06"
                    name="Help deliver 300 Smuggler Crates"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x3)"
                  />
                  <Entry
                    entryID="JOURNAL_EXPLORATION_SMUGGLERS_STANDING_04"
                    name="Gain Venerated Standing with the Smugglers"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x5)"
                  />
                </tbody>
              </Table>
            </AccordionBody>
          </AccordionItem>
        </UncontrolledAccordion>
      </Section>

      {/* PvP */}
      <Section>
        <UncontrolledAccordion id="pvp">
          <AccordionItem>
            <AccordionHeader targetId="pvp">PvP (181)</AccordionHeader>
            <AccordionBody accordionId="pvp">
              <h4>Arena (27)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="SA_ARENA_WIN_01"
                    name="Win your first Arena match"
                    id="T3_SILVERBAG_NONTRADABLE"
                    title="Journeyman's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_ARENA_WIN_COUNT_5"
                    name="Win 5 Arena or Crystal Arena Matches"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_ARENA_WIN_COUNT_10"
                    name="Win 10 Arena or Crystal Arena Matches"
                    id="T4_SILVERBAG_NONTRADABLE"
                    title="Adept's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_ARENA_DAMAGE_DEALT_01"
                    name="Deal 15,000 damage in a single Arena or Crystal Arena match"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_ARENA_WIN_COUNT_20"
                    name="Win 20 Arena or Crystal Arena Matches"
                    id="QUESTITEM_TOKEN_ARENA_CRYSTAL"
                    title="Arena Sigil (x20)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_ARENA_KILLS_01"
                    name="Get 5 kills in a single Arena or Crystal Arena match"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_ARENA_WIN_COUNT_35"
                    name="Win 35 Arena or Crystal Arena Matches"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_ARENA_CAPTURE_RUNESTONES_01"
                    name="Capture 4 Runestones in a single Arena or Crystal Arena match"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_ARENA_WIN_COUNT_50"
                    name="Win 50 Arena or Crystal Arena Matches"
                    id="T1_KILL_EMOTE_TOMBSTONE_CHARGES_NONTRADABLE"
                    title="Tombstone Victory Emote Charge (x10)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_ARENA_DAMAGE_DEALT_02"
                    name="Deal 22,000 damage in a single Arena or Crystal Arena match"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_ARENA_WIN_COUNT_75"
                    name="Win 75 Arena or Crystal Arena Matches"
                    id="QUESTITEM_TOKEN_ARENA_CRYSTAL"
                    title="Arena Sigil (x30)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_ARENA_TANKY_01"
                    name="Take 20,000 damage without dying in a single Arena or Crystal Arena match"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="SA_ARENA_WIN_02"
                    name="Win 100 Arena or Crystal Arena matches"
                    id="T1_KILL_EMOTE_SWORD_CHARGES_NONTRADABLE"
                    title="Sword Victory Emote Charge (x20)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_ARENA_HEALING_DONE_01"
                    name="Heal 15,000 health in a single Arena or Crystal Arena match"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_ARENA_WIN_COUNT_150"
                    name="Win 150 Arena or Crystal Arena Matches"
                    id="QUESTITEM_TOKEN_ARENA_CRYSTAL"
                    title="Arena Sigil (x40)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_ARENA_KILLS_02"
                    name="Get 10 kills in a single Arena or Crystal Arena match"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_ARENA_WIN_COUNT_200"
                    name="Win 200 Arena or Crystal Arena Matches"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_ARENA_DAMAGE_DEALT_03"
                    name="Deal 30,000 damage in a single Arena or Crystal Arena match"
                    id="T1_KILL_EMOTE_HAMMER_CHARGES_NONTRADABLE"
                    title="Hammer Victory Emote Charge (x20)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_ARENA_WIN_COUNT_250"
                    name="Win 250 Arena or Crystal Arena Matches"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_ARENA_CAPTURE_RUNE_STONES_02"
                    name="Capture 8 Runestones in a single Arena or Crystal Arena match"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_ARENA_WIN_COUNT_300"
                    name="Win 300 Arena or Crystal Arena Matches"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_ARENA_DAMAGE_DEALT_04"
                    name="Deal 40,000 damage in a single Arena or Crystal Arena match"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_ARENA_DAMAGE_DEALT_05"
                    name="Deal 50,000 damage in a single Arena or Crystal Arena match"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_ARENA_TANKY_02"
                    name="Take 50,000 damage without dying in a single Arena or Crystal Arena match"
                    id="UNIQUE_UNLOCK_ARMOR_VANITY_GLADIATOR_ARENA"
                    title="Wardrobe Skin: Arena Gladiator Armor"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_ARENA_HEALING_DONE_02"
                    name="Heal 30,000 health in a single Arena or Crystal Arena match"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_ARENA_HEALING_DONE_03"
                    name="Heal 50,000 health in a single Arena or Crystal Arena match"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_ARENA_HEALING_DONE_04"
                    name="Heal 75,000 health in a single Arena or Crystal Arena match"
                    id="UNIQUE_FURNITUREITEM_ADC_STATUE_MAGE_A"
                    title="Mage Statue"
                  />
                </tbody>
              </Table>

              <h4>Crystal Arena (21)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="SA_PVP_CRYSTAL_ARENA_RANKUP"
                    name="Increase your rank in the Crystal Arena"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_CRYSTALARENA_IRON3"
                    name="Reach Iron III Rank in Crystal Arena"
                    id="T4_SILVERBAG_NONTRADABLE"
                    title="Adept's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_CRYSTALARENA_IRON4"
                    name="Reach Iron IV Rank in Crystal Arena"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_CRYSTALARENA_BRONZE1"
                    name="Reach Bronze Rank in Crystal Arena"
                    id="T1_KILL_EMOTE_GHOST_CHARGES_NONTRADABLE"
                    title="Ghost Victory Emote Charge (x10)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_CRYSTALARENA_BRONZE2"
                    name="Reach Bronze II Rank in Crystal Arena"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_CRYSTALARENA_BRONZE3"
                    name="Reach Bronze III Rank in Crystal Arena"
                    id="QUESTITEM_TOKEN_ARENA_CRYSTAL"
                    title="Arena Sigil (x20)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_CRYSTALARENA_BRONZE4"
                    name="Reach Bronze IV Rank in Crystal Arena"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="SA_PVP_CRYSTAL_ARENA_SILVER1"
                    name="Reach Silver Rank in the Crystal Arena"
                    id="UNIQUE_UNLOCK_HEAD_VANITY_PRIEST_NON_TRADABLE"
                    title="Wardrobe Skin: Monk's Hood"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_CRYSTALARENA_SILVER2"
                    name="Reach Silver II Rank in the Crystal Arena"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_CRYSTALARENA_SILVER3"
                    name="Reach Silver III Rank in Crystal Arena"
                    id="T1_KILL_EMOTE_TOMBSTONE_CHARGES_NONTRADABLE"
                    title="Tombstone Victory Emote Charge (x20)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_CRYSTALARENA_SILVER4"
                    name="Reach Silver IV Rank in Crystal Arena"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_CRYSTALARENA_GOLD1"
                    name="Reach Gold Rank in Crystal Arena"
                    id="T4_TOKEN_CRYSTALLEAGUE_NONLETHAL_LVL_01"
                    title="Crystal Token (5v5 Nonlethal - Lvl. 1)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_CRYSTALARENA_GOLD2"
                    name="Reach Gold II Rank in Crystal Arena"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_CRYSTALARENA_GOLD3"
                    name="Reach Gold III Rank in Crystal Arena"
                    id="UNIQUE_UNLOCK_HEAD_VANITY_GLADIATOR_ARENA"
                    title="Wardrobe Skin: Arena Gladiator Helm"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_CRYSTALARENA_GOLD4"
                    name="Reach Gold IV Rank in Crystal Arena"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x5)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_CRYSTALARENA_CRYSTAL"
                    name="Reach Crystal Rank in Crystal Arena"
                    id="T4_TOKEN_CRYSTALLEAGUE_CITY_LVL_01"
                    title="Crystal Token (20v20 -  Lvl. 1)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_CRYSTALARENA_POINT_ADVANTAGE_01"
                    name="Win a match by a 50 point margin"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_CRYSTALARENA_POINT_ADVANTAGE_02"
                    name="Win a match by a 75 point margin"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_CRYSTALARENA_POINT_ADVANTAGE_03"
                    name="Win a match by a 100 point margin"
                    id="UNIQUE_UNLOCK_CAPE_VANITY_GLADIATOR_ARENA"
                    title="Wardrobe Skin: Arena Gladiator Cape"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_CRYSTALARENA_POINT_ADVANTAGE_04"
                    name="Win a match by a 125 point margin"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_CRYSTALARENA_POINT_ADVANTAGE_05"
                    name="Win a match by a 150 point margin"
                    id="T1_KILL_EMOTE_HAMMER_CHARGES_NONTRADABLE"
                    title="Hammer Victory Emote Charge (x50)"
                  />
                </tbody>
              </Table>

              <h4>Corrupted Dungeons (21)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="SA_PVE_CORRUPTED_DUNGEONS_01"
                    name="Defeat the final boss in a Hunter Corrupted Dungeon"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_CORRUPTEDS_INFAMY_01"
                    name="Get 666 Infamy in Corrupted Dungeons"
                    id="T4_SILVERBAG_NONTRADABLE"
                    title="Adept's Bag of Silver"
                  />
                  <Entry
                    entryID="SA_PVP_CORRUPTED_DUNGEON_02"
                    name="Defeat another player after invading their Corrupted Dungeon"
                    id="T5_CORRUPTED_NONLETHAL_MAP"
                    title="Corrupted Dungeon Map (Hunter)"
                  />
                  <Entry
                    entryID="SA_PVP_CORRUPTED_DUNGEON_01"
                    name="Defeat an invading player in a Corrupted Dungeon"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_CORRUPTEDS_INFAMY_02"
                    name="Get 2,500 Infamy in Corrupted Dungeons"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_CORRUPTEDS_HUNTER_KILL_5"
                    name="Defeat 5 players in a Hunter Corrupted Dungeon"
                    id="T1_KILL_EMOTE_SWORD_CHARGES_NONTRADABLE"
                    title="Sword Victory Emote Charge (x10)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_CORRUPTEDS_STALKER_BOSS"
                    name="Defeat the final boss in a Stalker Corrupted Dungeon"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_CORRUPTEDS_INFAMY_03"
                    name="Get 10,000 Infamy in Corrupted Dungeons"
                    id="T6_CORRUPTED_LETHAL_MAP"
                    title="Corrupted Dungeon Map (Stalker/Slayer)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_CORRUPTEDS_STALKER_KILL_01"
                    name="Defeat a player in a Stalker Corrupted Dungeon"
                    id="T1_KILL_EMOTE_HELLGATE_CHARGES_NONTRADABLE"
                    title="Hellgate Victory Emote Charge (x20)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_CORRUPTEDS_INFAMY_04"
                    name="Get 50,000 Infamy in Corrupted Dungeons"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_CORRUPTEDS_STALKER_KILL_02"
                    name="Defeat 5 players in a Stalker Corrupted Dungeon"
                    id="UNIQUE_FURNITUREITEM_ADC_HALLOWEEN_SCARECROW_A"
                    title="Halloween Scarecrow"
                  />
                  <Entry
                    entryID="SA_COLLECTION_CORRUPTED_DUNGEONS_INFAMY"
                    name="Unlock the Slayer difficulty in Corrupted Dungeons"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_CORRUPTEDS_SLAYER_KILL_01"
                    name="Defeat a player in a Slayer Corrupted Dungeon"
                    id="UNIQUE_UNLOCK_HEAD_VANITY_ENTERTAINER_NON_TRADABLE"
                    title="Wardrobe Skin: Entertainer's Mask"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_CORRUPTEDS_INFAMY_05"
                    name="Get 150,000 Infamy in Corrupted Dungeons"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_CORRUPTEDS_SLAYER_KILL_02"
                    name="Defeat 5 players in a Slayer Corrupted Dungeon"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_CORRUPTEDS_KILL_FULL_LOOT_01"
                    name="Defeat 100 players in full-loot Corrupted Dungeons"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x2)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_CORRUPTEDS_INFAMY_06"
                    name="Get 300,000 Infamy in Corrupted Dungeons"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x5)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_CORRUPTEDS_KILL_FULL_LOOT_02"
                    name="Defeat 300 players in full-loot Corrupted Dungeons"
                    id="T1_KILL_EMOTE_TOMBSTONE_CHARGES_NONTRADABLE"
                    title="Tombstone Victory Emote Charge (x50)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_CORRUPTEDS_INFAMY_07"
                    name="Get 600,000 Infamy in Corrupted Dungeons"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x10)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_CORRUPTEDS_KILL_FULL_LOOT_03"
                    name="Defeat 666 players in full-loot Corrupted Dungeons"
                    id="T1_KILL_EMOTE_HAMMER_CHARGES_NONTRADABLE"
                    title="Hammer Victory Emote Charge (x500)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_CORRUPTEDS_INFAMY_08"
                    name="Get 1,000,000 Infamy in Corrupted Dungeons"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x20)"
                  />
                </tbody>
              </Table>

              <h4>Faction Warfare (30)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="SA_FACTIONWARFARE_JOIN"
                    name="Enlist in any of the six City Factions"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="SA_FACTIONWARFARE_CAPTURE_01"
                    name="Capture an Outpost"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="SA_FACTIONWARFARE_CLUSTER_CAPTURE"
                    name="Assist in completely capturing another city's zone in Faction Warfare"
                    id="T4_SILVERBAG_NONTRADABLE"
                    title="Adept's Bag of Silver"
                  />
                  <Entry
                    entryID="SA_FACTIONWARFARE_CAPTURE_02"
                    name="Capture 10 Outposts"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_FACTION_WARFARE_DAILY_MISSION"
                    name="Earn a Faction Warfare Daily Reward"
                    id="T4_SILVERBAG_NONTRADABLE"
                    title="Adept's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_FACTION_WARFARE_PLAYER_KNOCKDOWN_01"
                    name="Knock down or assist a knockdown of an enemy faction player"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_FACTION_WARFARE_RANK_01"
                    name="Reach 15,000 standing with any Faction"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_FACTION_WARFARE_BOSSES_02"
                    name="Defeat 2 different Faction Champions"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_FACTION_WARFARE_RANK_02"
                    name="Reach 30,000 standing with any Faction"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_FACTION_WARFARE_CAPTURE_01"
                    name="Capture 30 Faction Outposts"
                    id="T1_KILL_EMOTE_FLAG_CHARGES_NONTRADABLE"
                    title="Guild Banner Victory Emote Charge (x10)"
                  />
                  <Entry
                    entryID="SA_FACTIONWARFARE_TRADEMISSION_01"
                    name="Finish a Trade Mission for any city"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_FACTION_WARFARE_RANK_03"
                    name="Reach 60,000 standing with any Faction"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_FACTION_WARFARE_RED_01"
                    name="Capture 5 Outposts in Red Zones"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_FACTION_WARFARE_BOSSES_03"
                    name="Defeat 3 different Faction Champions"
                    id="T1_KILL_EMOTE_OVERGROWN_CHARGES_NONTRADABLE"
                    title="Overgrown Victory Emote Charge (x20)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_FACTION_WARFARE_KILL_01"
                    name="Kill or assist a kill of an enemy faction player in a Red Zone"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="SA_FACTIONWARFARE_BANDIT_ASSAULT"
                    name="Help repel a Bandit Assault"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_FACTION_WARFARE_RANK_04"
                    name="Reach 240,000 standing with any Faction"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    entryID="SA_FACTIONWARFARE_CAPTURE_03"
                    name="Capture 100 Outposts"
                    id="UNIQUE_REPAIRPOWDER_ADC_GENERAL_01_NONTRADEABLE"
                    title="Scroll of Repair"
                  />
                  <Entry
                    entryID="SA_FACTIONWARFARE_STANDING_MAX"
                    name="Achieve a standing of 330,000 with any faction"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    entryID="SA_FACTIONWARFARE_KILLBOSS_ALL"
                    name={
                      <>
                        Defeat all opposing City Faction Warmasters at least
                        once
                        <br />
                        <span className="text-muted">
                          Any 5 of
                          <br />
                          Champion of Lymhurst, Champion of Martlock, Champion
                          of Fort Sterling, Champion of Bridgewatch, Champion of
                          Thetford, Bandit Ringleader
                        </span>
                      </>
                    }
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_FACTION_WARFARE_CAPTURE_02"
                    name="Capture 300 Faction Outposts"
                    id="T1_KILL_EMOTE_OVERGROWN_CHARGES_NONTRADABLE"
                    title="Overgrown Victory Emote Charge (x50)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_FACTION_WARFARE_PLAYER_KNOCKDOWN_02"
                    name="Knock down or assist knockdowns of 30 enemy faction players"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_FACTION_WARFARE_PLAYER_KNOCKDOWN_03"
                    name="Knock down or assist knockdowns of 100 enemy faction players"
                    id="T1_KILL_EMOTE_HAMMER_CHARGES_NONTRADABLE"
                    title="Hammer Victory Emote Charge (x10)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_FACTION_WARFARE_PLAYER_KNOCKDOWN_04"
                    name="Knock down or assist knockdowns of 300 enemy faction players"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_FACTION_WARFARE_PLAYER_KNOCKDOWN_05"
                    name="Knock down or assist knockdowns of 1000 enemy faction players"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_FACTION_WARFARE_KILL_02"
                    name="Kill or assist 10 enemy faction player kills in Red Zones"
                    id="UNIQUE_FURNITUREITEM_ADC_GRAVE_A"
                    title="Tomb of the Unknown"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_FACTION_WARFARE_KILL_03"
                    name="Kill or assist 30 enemy faction player kills in Red Zones"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_FACTION_WARFARE_KILL_04"
                    name="Kill or assist 100 enemy faction player kills in Red Zones"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_FACTION_WARFARE_KILL_05"
                    name="Kill or assist 300 enemy faction player kills in Red Zones"
                    id="T1_KILL_EMOTE_SWORD_CHARGES_NONTRADABLE"
                    title="Sword Victory Emote Charge (x50)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_FACTION_WARFARE_KILL_06"
                    name="Kill or assist 1,000 enemy faction player kills in Red Zones"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x5)"
                  />
                </tbody>
              </Table>

              <h4>Open World PvP (32)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="SA_EXPLORATION_TREASURE"
                    name="Open an open-world Treasure Chest"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_OPEN_WORLD_PVP_KNOCKDOWN_01"
                    name="Knock down another player in a Yellow Zone"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_OPEN_WORLD_PVP_TREASURE_01"
                    name="Open 10 open-world Treasure Chests"
                    id="T1_KILL_EMOTE_OVERGROWN_CHARGES_NONTRADABLE"
                    title="Overgrown Victory Emote Charge (x10)"
                  />
                  <Entry
                    entryID="SA_PVP_KILL_PLAYER_01"
                    name="Kill or assist a kill in PvP"
                    id="UNIQUE_FURNITUREITEM_ADC_GRAVE_B"
                    title="Memorial of the Fallen"
                  />
                  <Entry
                    entryID="SA_PVP_TERMINATOR"
                    name="Loot any armor, foot gear and a mount from a killed player at the same time"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_OPEN_WORLD_PVP_KILLFAME_01"
                    name="Get 200,000 Kill Fame"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_OPEN_WORLD_PVP_KILL_PLAYER_02"
                    name="Kill 10 players in full-loot regions"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_OPEN_WORLD_PVP_KILL_PLAYER_ROADS_01"
                    name="Kill 3 players in the Roads of Avalon"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_OPEN_WORLD_PVP_KILL_PLAYER_03"
                    name="Kill 25 players in full-loot regions"
                    id="T1_KILL_EMOTE_FLAG_CHARGES_NONTRADABLE"
                    title="Guild Banner Victory Emote Charge (x20)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_OPEN_WORLD_PVP_KILL_PLAYER_STATIC_DUNGEON_01"
                    name="Kill 10 players in Static Dungeons"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_OPEN_WORLD_PVP_KILLFAME_BLACK_01"
                    name="Get 2 million Kill Fame in the Open World"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    entryID="SA_PVP_KILL_PLAYER_MONSTER"
                    name="Kill 6 players within one minute"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_OPEN_WORLD_PVP_KILL_PLAYER_04"
                    name="Kill 100 players in full-loot regions"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_OPEN_WORLD_PVP_KILLFAME_ROADS_01"
                    name="Get 2 million Kill Fame in the Roads of Avalon"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_OPEN_WORLD_PVP_KILLFAME_STATIC_DUNGEON_01"
                    name="Get 5 million Kill Fame in Static Dungeons"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_OPEN_WORLD_PVP_KILLINGSPREE_NO_ASSIST"
                    name="Kill 6 players within one minute (not including assists)"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="SA_PVP_KILL_PLAYER_02"
                    name="Kill 300 players in the open world"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_OPEN_WORLD_PVP_KILLFAME_BLACK_02"
                    name="Get 10 million Kill Fame in Black Zones"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x5)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_OPEN_WORLD_PVP_KILLFAME_STATIC_DUNGEON_02"
                    name="Get 10 million Kill Fame in Static Dungeons"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x5)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_OPEN_WORLD_PVP_KILLFAME_ROADS_02"
                    name="Get 10 million Kill Fame in the Roads of Avalon"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x5)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_OPEN_WORLD_PVP_KILLFAME_BLACK_03"
                    name="Get 50 million Kill Fame in Black Zones"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x15)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_OPEN_WORLD_PVP_KILLFAME_BLACK_04"
                    name="Get 100 million Kill Fame in Black Zones"
                    id="T1_KILL_EMOTE_GHOST_CHARGES_NONTRADABLE"
                    title="Ghost Victory Emote Charge (x50)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_OPEN_WORLD_PVP_KILLFAME_BLACK_05"
                    name="Get 500 million Kill Fame in Black Zones"
                    id="T1_KILL_EMOTE_TOMBSTONE_CHARGES_NONTRADABLE"
                    title="Tombstone Victory Emote Charge (x500)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_OPEN_WORLD_PVP_TREASURE_02"
                    name="Open 30 open-world Treasure Chests in full-loot regions"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    entryID="SA_EXPLORATION_TREASURE_100"
                    name="Open 100 open-world Treasure Chests"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_OPEN_WORLD_PVP_TREASURE_VETERAN_01"
                    name="Open 30 Medium Treasure Chests"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_OPEN_WORLD_PVP_TREASURE_ELITE_01"
                    name="Open 10 Large Treasure Chests"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_OPEN_WORLD_PVP_TREASURE_03"
                    name="Open 500 open-world Treasure Chests"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x5)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_OPEN_WORLD_PVP_TREASURE_VETERAN_02"
                    name="Open 300 Medium Treasure Chests"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x5)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_OPEN_WORLD_PVP_TREASURE_ELITE_02"
                    name="Open 100 Large Treasure Chests"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x5)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_OPEN_WORLD_PVP_TREASURE_ELITE_LEGENDARY"
                    name="Open a Legendary Large Treasure Chest"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="SA_PVP_DIE_PLAYER"
                    name="Get killed by another player"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                </tbody>
              </Table>

              <h4>Hellgates (33)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="SA_EXPLORATION_GOTO_HELLGATE"
                    name="Enter a Hellgate"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_HELL_GATES_MINIBOSS_01"
                    name="Defeat a Mini Boss in a Hellgate"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="SA_PVP_WIN_HELLGATE_01"
                    name="Defeat a team of enemy players in any type of Hellgate"
                    id="T5_HELLGATE_2V2_NON_LETHAL_1_MAP"
                    title="Expert's Hellgate Ritual (2v2 - Nonlethal)"
                  />
                  <Entry
                    entryID="SA_EXPLORATION_CHAIN_HELLGATE_01"
                    name="Chain 2 Hellgates without returning to the surface"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_HELL_GATES_2V2_INFAMY_01"
                    name="Gain 10,000 Infamy in 2v2 Hellgates"
                    id="T1_KILL_EMOTE_HELLGATE_CHARGES_NONTRADABLE"
                    title="Hellgate Victory Emote Charge (x10)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_HELL_GATES_KNOCKDOWN_01"
                    name="Knock down 10 players in Hellgates"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_HELL_GATES_MINIBOSS_02"
                    name="Defeat 5 Mini Bosses in Hellgates"
                    id="UNIQUE_FURNITUREITEM_ADC_HALLOWEEN_PUMPKIN_LANTERN_B"
                    title="Friendly Pumpkin Lantern"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_HELL_GATES_BOSS_01"
                    name="Defeat a Boss in a Hellgate"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_HELL_GATES_2V2_INFAMY_02"
                    name="Gain 20,000 Infamy in 2v2 Hellgates"
                    id="T1_KILL_EMOTE_GHOST_CHARGES_NONTRADABLE"
                    title="Ghost Victory Emote Charge (x20)"
                  />
                  <Entry
                    entryID="SA_EXPLORATION_CHAIN_HELLGATE_02"
                    name="Chain 5 Hellgates without returning to the surface"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_HELL_GATES_KNOCKDOWN_02"
                    name="Knock down 50 players in Hellgates"
                    id="T6_HELLGATE_2V2_LETHAL_1_MAP"
                    title="Master's Hellgate Ritual (2v2 - Lethal)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_HELL_GATES_KILL_PLAYER_01"
                    name="Kill a player in a full-loot Hellgate"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_HELL_GATES_2V2_INFAMY_03"
                    name="Gain 50,000 Infamy in 2v2 Hellgates"
                    id="T7_HELLGATE_5V5_LETHAL_1_MAP"
                    title="Grandmaster's Hellgate Ritual (5v5 - Lethal)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_HELL_GATES_MINIBOSS_5V5_01"
                    name="Defeat a Mini Boss in a 5v5 Hellgate"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_HELL_GATES_WIN_5V5"
                    name="Defeat an enemy team in a 5v5 Hellgate"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_HELL_GATES_5V5_INFAMY_01"
                    name="Gain 20,000 Infamy in 5v5 Hellgates"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_HELL_GATES_KNOCKDOWN_03"
                    name="Knock down 200 players in Hellgates"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_HELL_GATES_5V5_INFAMY_02"
                    name="Gain 50,000 Infamy in 5v5 Hellgates"
                    id="T8_HELLGATE_10V10_LETHAL_1_MAP"
                    title="Elder's Hellgate Ritual (10v10 - Lethal)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_HELL_GATES_KILL_PLAYER_02"
                    name="Kill 20 players in full-loot Hellgates"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver (x5)"
                  />
                  <Entry
                    entryID="SA_EXPLORATION_CHAIN_HELLGATE_03"
                    name="Chain 10 Hellgates without returning to the surface"
                    id="T5_LEARNINGPOINTS_NONTRADABLE"
                    title="Expert's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_HELL_GATES_KILL_PLAYER_03"
                    name="Kill 50 players in full-loot Hellgates"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x5)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_HELL_GATES_MINIBOSS_10V10_01"
                    name="Defeat a Mini Boss in a 10v10 Hellgate"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_HELL_GATES_WIN_10V10"
                    name="Defeat an enemy team in a 10v10 Hellgate"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_HELL_GATES_KILL_PLAYER_04"
                    name="Kill 200 players in full-loot Hellgates"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x10)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_HELL_GATES_KILL_PLAYER_05"
                    name="Kill 500 players in full-loot Hellgates"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x20)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_HELL_GATES_KILL_PLAYER_06"
                    name="Kill 1,000 players in full-loot Helgates"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x40)"
                  />
                  <Entry
                    entryID="SA_COLLECTION_HELLGATE_01"
                    name="Gain 100,000 Infamy in 2v2 Hellgates"
                    id="T1_KILL_EMOTE_GHOST_CHARGES_NONTRADABLE"
                    title="Ghost Victory Emote Charge (x500)"
                  />
                  <Entry
                    entryID="SA_COLLECTION_HELLGATE_02"
                    name="Gain 250,000 Infamy in 2v2 Hellgates"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x20)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_HELL_GATES_5V5_INFAMY_03"
                    name="Gain 100,000 Infamy in 5v5 Hellgates"
                    id="T1_KILL_EMOTE_SWORD_CHARGES_NONTRADABLE"
                    title="Sword Victory Emote Charge (x500)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_HELL_GATES_5V5_INFAMY_04"
                    name="Gain 250,000 Infamy in 5v5 Hellgates"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x25)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_HELL_GATES_10V10_INFAMY_01"
                    name="Gain 50,000 Infamy in 10v10 Hellgates"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x8)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_HELL_GATES_10V10_INFAMY_02"
                    name="Gain 100,000 Infamy in 10v10 Hellgates"
                    id="T1_KILL_EMOTE_HELLGATE_CHARGES_NONTRADABLE"
                    title="Hellgate Victory Emote Charge (x500)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_HELL_GATES_10V10_INFAMY_03"
                    name="Gain 250,000 Infamy in 10v10 Hellgates"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x30)"
                  />
                </tbody>
              </Table>

              <h4>Crystal League (17)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="SA_PVP_CRYSTAL_PARTICIPATION"
                    name="Participate in a Crystal League Battle"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="SA_PVP_CRYSTAL_LEAGUE_WIN"
                    name="Win a 5v5 Crystal League Match"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_CRYSTAL_LEAGUE_5V5_WIN_2"
                    name="Win a Rank 2 5v5 Crystal League Match"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    entryID="SA_PVP_CRYSTAL_LEAGUE_RANK_01"
                    name="Win a Rank 3 5v5 Crystal League Match"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x50)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_CRYSTAL_LEAGUE_20V20_WIN_1"
                    name="Win a 20v20 Crystal League Match"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_CRYSTAL_LEAGUE_5V5_WIN_4"
                    name="Win a Rank 4 5v5 Crystal League Match"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x5)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_CRYSTAL_LEAGUE_5V5_WIN_5"
                    name="Win a Rank 5 5v5 Crystal League Match"
                    id="T1_KILL_EMOTE_FLAG_CHARGES_NONTRADABLE"
                    title="Guild Banner Victory Emote Charge (x50)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_CRYSTAL_LEAGUE_5V5_WIN_6"
                    name="Win a Rank 6 5v5 Crystal League Match"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x15)"
                  />
                  <Entry
                    entryID="SA_PVP_CRYSTAL_LEAGUE_RANK_02"
                    name="Win a Rank 7 5v5 Crystal League Match"
                    id="UNIQUE_UNLOCK_CAPE_VANITY_GLADIATOR_CRYSTAL"
                    title="Wardrobe Skin: Crystal Gladiator Cape"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_CRYSTAL_LEAGUE_5V5_WIN_8"
                    name="Win a Rank 8 5v5 Crystal League Match"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x40)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_CRYSTAL_LEAGUE_5V5_WIN_9"
                    name="Win a Rank 9 5v5 Crystal League Match"
                    id="UNIQUE_UNLOCK_HEAD_VANITY_GLADIATOR_CRYSTAL"
                    title="Wardrobe Skin: Crystal Gladiator Helm"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_CRYSTAL_LEAGUE_20V20_WIN_2"
                    name="Win a Rank 2 20v20 Crystal League Match"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x5)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_CRYSTAL_LEAGUE_20V20_WIN_3"
                    name="Win a Rank 3 20v20 Crystal League Match"
                    id="UNIQUE_UNLOCK_SHOES_VANITY_GLADIATOR_CRYSTAL"
                    title="Wardrobe Skin: Crystal Gladiator Boots"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_CRYSTAL_LEAGUE_20V20_WIN_4"
                    name="Win a Rank 4 20v20 Crystal League Match"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x10)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_CRYSTAL_LEAGUE_20V20_WIN_5"
                    name="Win a Rank 5 20v20 Crystal League Match"
                    id="T1_KILL_EMOTE_FLAG_CHARGES_NONTRADABLE"
                    title="Guild Banner Victory Emote Charge (x500)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_CRYSTAL_LEAGUE_20V20_WIN_6"
                    name="Win a Rank 6 20v20 Crystal League Match"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x40)"
                  />
                  <Entry
                    entryID="JOURNAL_PVP_CRYSTAL_LEAGUE_20V20_WIN_7"
                    name="Win a Rank 7 20v20 Crystal League Match"
                    id="UNIQUE_UNLOCK_ARMOR_VANITY_GLADIATOR_CRYSTAL"
                    title="Wardrobe Skin: Crystal Gladiator Armor"
                  />
                </tbody>
              </Table>
            </AccordionBody>
          </AccordionItem>
        </UncontrolledAccordion>
      </Section>

      {/* Social & Guild */}
      <Section>
        <UncontrolledAccordion id="guild">
          <AccordionItem>
            <AccordionHeader targetId="guild">
              Social & Guild (196)
            </AccordionHeader>
            <AccordionBody accordionId="guild">
              <h4>Player Interactions (20)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="JOURNAL_GUILD_CHAT_SAY"
                    name="Start saying something by typing /s in the chat"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_COLLECTION_USE_INSPECT_01"
                    name="Inspect another player"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_PLAYER_DUEL"
                    name="Duel another player"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_CHAT_WHISPER"
                    name="Whisper another player by typing /w"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_PLAYER_TRADE_01"
                    name="Trade with another player"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_PLAYER_DUEL_WIN_01"
                    name="Win a duel"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_COLLECTION_USE_INSPECT_02"
                    name="Inspect 10 players"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_PLAYER_DUEL_WIN_02"
                    name="Win 5 duels"
                    id="T1_KILL_EMOTE_HAMMER_CHARGES_NONTRADABLE"
                    title="Hammer Victory Emote Charge (x3)"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_PLAYER_TRADE_02"
                    name="Trade 10 times with another player"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_COLLECTION_USE_INSPECT_03"
                    name="Inspect 30 players"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="SA_COLLECTION_EMOTES"
                    name="Use every emote in the game"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x5)"
                  />
                  <Entry
                    entryID="SA_COLLECTION_USE_INSPECT"
                    name="Inspect 100 players"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x10)"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_PLAYER_TRADE_03"
                    name="Trade 100 times with another player"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_PLAYER_KILLTROPHY_MISTS"
                    name="Obtain a Kill Trophy by killing a player in the Mists"
                    id="T1_KILL_EMOTE_GHOST_CHARGES_NONTRADABLE"
                    title="Ghost Victory Emote Charge (x20)"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_PLAYER_DUEL_WIN_03"
                    name="Win 20 duels"
                    id="T1_KILL_EMOTE_GHOST_CHARGES_NONTRADABLE"
                    title="Ghost Victory Emote Charge (x5)"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_PLAYER_KILLTROPHY_HELL"
                    name="Obtain a Kill Trophy by killing a player in a Corrupted Dungeon or Hellgate"
                    id="T1_KILL_EMOTE_HELLGATE_CHARGES_NONTRADABLE"
                    title="Hellgate Victory Emote Charge (x20)"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_PLAYER_DUEL_WIN_04"
                    name="Win 100 duels"
                    id="T1_KILL_EMOTE_TOMBSTONE_CHARGES_NONTRADABLE"
                    title="Tombstone Victory Emote Charge (x20)"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_PLAYER_KILLTROPHY_BLACK"
                    name="Obtain a Kill Trophy by killing a player in the Outlands or Roads of Avalon"
                    id="T1_KILL_EMOTE_TOMBSTONE_CHARGES_NONTRADABLE"
                    title="Tombstone Victory Emote Charge (x20)"
                  />
                  <Entry
                    entryID="SA_EXPLORATION_CABBAGE_MERCHANT_ANY"
                    name="Sell a cabbage to another player in a Black Zone."
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x20)"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_SELFTALK"
                    name="Talk to yourself..."
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                </tbody>
              </Table>

              <h4>Parties & Friends (23)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="JOURNAL_GUILD_PARTY_FAME_01"
                    name="Gain 10,000 Fame in a party"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_PARTY_FAME_02"
                    name="Gain 50,000 Fame while in a party"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="SA_SOCIAL_FRIEND_01"
                    name="Add a friend to your friend list"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_PARTY_FAME_03"
                    name="Gain 100,000 Fame while in a party"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_CHAT_LFG"
                    name="Look for a group by typing /lfg in the chat"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_SOCIAL_FRIEND_02"
                    name="Add 3 friends to your friend list"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_PARTY_FAME_04"
                    name="Gain 300,000 Fame while in a party"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_SOCIAL_FRIEND_03"
                    name="Add 5 friends to your friend list"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_BIG_PARTY_FAME_01"
                    name="Gain 50,000 Fame while in a party of 5 or more players"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_PARTY_FAME_05"
                    name="Gain a million Fame while in a party"
                    id="T5_FOCUSPOTION_NONTRADABLE"
                    title="Expert's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_READY_CHECK_01"
                    name="Initiate a Party Ready Check"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_SOCIAL_FRIEND_04"
                    name="Add 10 friends to your friend list"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_VISIT_PLAYERISLAND"
                    name="Visit another player's Personal Island"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_VERY_BIG_PARTY_FAME_01"
                    name="Gain 100,000 Fame while in a party of 7 or more players"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_READY_CHECK_02"
                    name="Initiate 5 Party Ready Checks"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_PARTY_FAME_06"
                    name="Gain 3 million Fame while in a party"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_PARTY_FAME_07"
                    name="Gain 10 million Fame while in a party"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x30)"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_PARTY_FAME_08"
                    name="Gain 30 million Fame while in a party"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_PARTY_FAME_09"
                    name="Gain 100 million Fame while in a party"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_BIG_PARTY_FAME_02"
                    name="Gain 30 million Fame while in a party of 5 or more players"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_BIG_PARTY_FAME_03"
                    name="Gain 100 million Fame while in a party of 5 or more players"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x75)"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_RAID_PARTY_FAME_01"
                    name="Gain 10 million Fame while in a party of 20 players"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_RAID_PARTY_FAME_02"
                    name="Gain 100 million Fame while in a party of 20 players"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                </tbody>
              </Table>

              <h4>Guilds (22)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="JOURNAL_GUILD_OPEN_GUILD_FINDER"
                    name="Open the Guild Finder"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="SA_SOCIAL_GUILD"
                    name="Create or join a guild"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_CHAT_GUILD"
                    name="Write in the guild chat by typing /g"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_GUILD_CHALLENGE_POINTS_01"
                    name="Contribute 10,000 Challenge Points to the Guild Challenge"
                    id="T4_SILVERBAG_NONTRADABLE"
                    title="Adept's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_GUILD_CHALLENGE_LEVEL_01"
                    name="Reach Guild Challenge Level 2 with your Guild"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_GUILD_CHALLENGE_POINTS_02"
                    name="Contribute 40,000 Challenge Points to the Guild Challenge"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_GUILD_CHALLENGE_LEVEL_02"
                    name="Reach Guild Challenge Level 5 with your Guild"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_GUILD_CHALLENGE_POINTS_03"
                    name="Contribute 90,000 Challenge Points to the Guild Challenge"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_GUILD_CHALLENGE_LEVEL_03"
                    name="Reach Guild Challenge Level 15 with your Guild"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_SOCIAL_ALLIANCE"
                    name="Join or create an Alliance"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_GUILD_CHALLENGE_POINTS_04"
                    name="Contribute 160,000 Challenge Points to the Guild Challenge"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_GUILD_CHALLENGE_POINTS_05"
                    name="Contribute 250,000 Challenge Points to the Guild Challenge"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_GUILD_CHALLENGE_POINTS_06"
                    name="Contribute 400,000 Challenge Points to the Guild Challenge"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_GUILD_CHALLENGE_POINTS_07"
                    name="Contribute 700,000 Challenge Points to the Guild Challenge"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_GUILD_CHALLENGE_POINTS_08"
                    name="Contribute 1,200,000 Challenge Points to the Guild Challenge"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_GUILD_CHALLENGE_POINTS_09"
                    name="Contribute 2 million Challenge Points to the Guild Challenge"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_GUILD_CHALLENGE_POINTS_10"
                    name="Contribute 5 million Challenge Points to the Guild Challenge"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x5)"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_GUILD_CHALLENGE_POINTS_11"
                    name="Contribute 10 million Challenge Points to the Guild Challenge"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x10)"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_GUILD_CHALLENGE_LEVEL_04"
                    name="Reach Guild Challenge Level 30 with your Guild"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_GUILD_CHALLENGE_LEVEL_05"
                    name="Reach Guild Challenge Level 50 with your Guild"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_GUILD_CHALLENGE_LEVEL_06"
                    name="Reach Guild Challenge Level 75 with your Guild"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_GUILD_CHALLENGE_LEVEL_07"
                    name="Reach Guild Challenge Level 99 with your Guild"
                    id="T5_LEARNINGPOINTS_NONTRADABLE"
                    title="Expert's Tome of Learning"
                  />
                </tbody>
              </Table>

              <h4>Crystal Creatures (17)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="JOURNAL_GUILD_CRYSTAL_CREATURES_KILL_ANY_01"
                    name="Defeat a Crystal Creature"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_CRYSTAL_CREATURES_KILL_ALL"
                    name="Defeat every type of Crystal Creature"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_CRYSTAL_CREATURES_KILL_ANY_02"
                    name="Defeat 5 Crystal Creatures"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_CRYSTAL_CREATURES_KILL_Q2"
                    name="Defeat 2 Crystal Creatures in Quality Level 2 Regions"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_CRYSTAL_CREATURES_KILL_ANY_03"
                    name="Defeat 10 Crystal Creatures"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_CRYSTAL_CREATURES_KILL_Q3"
                    name="Defeat 4 Crystal Creatures in Quality Level 3 Regions"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_CRYSTAL_CREATURES_KILL_ANY_04"
                    name="Defeat 20 Crystal Creatures"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_CRYSTAL_CREATURES_KILL_Q4"
                    name="Defeat 7 Crystal Creatures in Quality Level 4 Regions"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_CRYSTAL_CREATURES_KILL_ANY_05"
                    name="Defeat 40 Crystal Creatures"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_CRYSTAL_CREATURES_KILL_Q5"
                    name="Defeat 10 Crystal Creatures in Quality Level 5 Regions"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_CRYSTAL_CREATURES_KILL_ANY_06"
                    name="Defeat 65 Crystal Creatures"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_CRYSTAL_CREATURES_KILL_Q6"
                    name="Defeat 15 Crystal Creatures in Quality Level 6 Regions"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_CRYSTAL_CREATURES_KILL_ANY_07"
                    name="Defeat 100 Crystal Creatures"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_CRYSTAL_CREATURES_KILL_T8_Q6"
                    name="Defeat 20 Tier 8 Crystal Creatures in Quality Level 6 Regions"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_CRYSTAL_CREATURES_KILL_ANY_08"
                    name="Defeat 150 Crystal Creatures"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x5)"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_CRYSTAL_CREATURES_KILL_ANY_09"
                    name="Defeat 220 Crystal Creatures"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight (x5)"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_CRYSTAL_CREATURES_KILL_ANY_10"
                    name="Defeat 300 Crystal Creatures"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x10)"
                  />
                </tbody>
              </Table>

              <h4>Castles & Castle Outposts (22)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="SA_PVP_CASTLE_OUTPOST_CAPTURE"
                    name="Help loot a Castle Outpost Chest"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_PVP_CASTLE_OUTPOST_CAPTURE_02"
                    name="Help loot 3 Castle Outpost Chests"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_PVP_CASTLE_OUTPOST_CAPTURE_03"
                    name="Help loot a Castle Outpost Uncommon Chest"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_PVP_CASTLE_OUTPOST_CAPTURE_04"
                    name="Help loot 6 Castle Outpost Chests"
                    id="T1_KILL_EMOTE_HELLGATE_CHARGES_NONTRADABLE"
                    title="Hellgate Victory Emote Charge (x20)"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_PVP_CASTLE_OUTPOST_CAPTURE_05"
                    name="Help loot 10 Castle Outpost Chests"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_PVP_CASTLE_OUTPOST_CAPTURE_06"
                    name="Help loot a Castle Outpost Rare Chest"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_PVP_CASTLE_OUTPOST_CAPTURE_07"
                    name="Help loot 25 Castle Outpost Chests"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_PVP_CASTLE_OUTPOST_CAPTURE_08"
                    name="Help loot a Castle Outpost Legendary Chest"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    entryID="SA_PVP_CASTLE_CAPTURE_01"
                    name="Help loot a Castle Chest"
                    id="T5_LEARNINGPOINTS_NONTRADABLE"
                    title="Expert's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_PVP_CASTLE_CAPTURE_02"
                    name="Help loot 5 Castle Chests"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_PVP_CASTLE_CAPTURE_03"
                    name="Help loot a Castle Uncommon Chest"
                    id="UNIQUE_FURNITUREITEM_KNIGHT_ROUNDTABLE_A"
                    title="Round Table"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_PVP_CASTLE_DAMAGE_GATE_01"
                    name="Deal 20,000 damage to a Castle Gate"
                    id="T1_KILL_EMOTE_HAMMER_CHARGES_NONTRADABLE"
                    title="Hammer Victory Emote Charge (x40)"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_PVP_CASTLE_CAPTURE_04"
                    name="Help loot 10 Castle Chests"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_PVP_CASTLE_CAPTURE_05"
                    name="Help loot a Castle Rare Chest"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_PVP_CASTLE_DAMAGE_GATE_02"
                    name="Deal 100,000 damage to a Castle Gate"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_PVP_CASTLE_CAPTURE_06"
                    name="Help loot a Castle Legendary Chest"
                    id="T1_KILL_EMOTE_GHOST_CHARGES_NONTRADABLE"
                    title="Ghost Victory Emote Charge (x100)"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_PVP_CASTLE_OUTPOST_CAPTURE_09"
                    name="Help loot 50 Castle Outpost Chests"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x2)"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_PVP_CASTLE_OUTPOST_CAPTURE_10"
                    name="Help loot 100 Castle Outpost Chests"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x5)"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_PVP_CASTLE_OUTPOST_CAPTURE_11"
                    name="Help loot 300 Castle Outpost Chests"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x300)"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_PVP_CASTLE_CAPTURE_07"
                    name="Help loot 50 Castle Chests"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x10)"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_PVP_CASTLE_CAPTURE_08"
                    name="Help loot 100 Castle Chests"
                    id="T1_KILL_EMOTE_TOMBSTONE_CHARGES_NONTRADABLE"
                    title="Tombstone Victory Emote Charge (x700)"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_PVP_CASTLE_CAPTURE_09"
                    name="Help loot 100 Legendary Castle Chests"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x15)"
                  />
                </tbody>
              </Table>

              <h4>Hideouts (16)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="SA_COLLECTION_HIDEOUT_HOME"
                    name="Set a Hideout as your Home"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="SA_COLLECTION_HIDEOUT_POWER"
                    name="Successfully transport a Power Core to a Hideout"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_ENTER_GUILD_HIDEOUT_LVL2"
                    name="Enter a Level 2 Hideout owned by your Guild"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_HIDEOUT_POWER_01"
                    name="Transport a Blue Power Core to a Hideout"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_HIDEOUT_POWER_02"
                    name="Transport 5 Power Cores to a Hideout"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_HIDEOUT_POWER_03"
                    name="Transport a Purple Power Core to a Hideout"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_ENTER_GUILD_HIDEOUT_LVL3"
                    name="Enter a Level 3 Hideout owned by your Guild"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_HIDEOUT_POWER_04"
                    name="Transport 20 Power Cores to a Hideout"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_HIDEOUT_POWER_05"
                    name="Transport 10 Blue Power Cores to a Hideout"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_HIDEOUT_POWER_06"
                    name="Transport 5 Purple Power Cores to a Hideout"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_HIDEOUT_POWER_07"
                    name="Transport a Golden Power Core to a Hideout"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_HIDEOUT_POWER_08"
                    name="Transport 100 Power Cores to a Hideout"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_HIDEOUT_POWER_09"
                    name="Transport 5 Golden Power Cores to a Hideout"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_HIDEOUT_POWER_10"
                    name="Transport 300 Power Cores to a Hideout"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x5)"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_HIDEOUT_POWER_11"
                    name="Transport 100 Purple or Golden Power Cores to a Hideout"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x5)"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_ENTER_GUILD_HEADQUARTER"
                    name="Enter your Guild's Headquarter Hideout"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                </tbody>
              </Table>

              <h4>Large-Scale Battles (28)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="JOURNAL_GUILD_ZERGKILL_01"
                    name="Be part of a player kill with 10 or more assists"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_RESILIENCE_01"
                    name="Gain a Resilience buff by having 7 players attack you"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_DISSARRAY_01"
                    name="Get a Disarray debuff"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_PLAYERBATTLE_01"
                    name="Be part of a battle with at least 15 player deaths"
                    id="T1_KILL_EMOTE_SWORD_CHARGES_NONTRADABLE"
                    title="Sword Victory Emote Charge (x20)"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_ZERGKILL_02"
                    name="Be part of a player kill with 15 or more assists"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_RESILIENCE_02"
                    name="Gain a Resilience buff by having 10 players attack you"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_PLAYER_KILLSPREE_01"
                    name="Kill or assist in killing 12 players within one minute"
                    id="T1_KILL_EMOTE_GHOST_CHARGES_NONTRADABLE"
                    title="Ghost Victory Emote Charge (x40)"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_KILLFAME_LARGE_BATTLE_01"
                    name="Gain 100,000 Kill Fame from kills with 10 or more assists"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_PLAYERBATTLE_02"
                    name="Be part of a battle with at least 25 player deaths"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_DISSARRAY_02"
                    name="Get a Level 10 Disarray debuff"
                    id="UNIQUE_UNLOCK_SKIN_ARMORED_HORSE_T5_GUILD_NON_TRADABLE"
                    title="Armored Horse Skin: Expert's Guild Warhorse"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_ZERGKILL_03"
                    name="Be part of a player kill with 19 or more assists"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_PLAYERBATTLE_03"
                    name="Be part of a battle with at least 40 player deaths"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_PLAYER_KILLSPREE_02"
                    name="Kill or assist in killing 20 players within one minute"
                    id="T1_KILL_EMOTE_FLAG_CHARGES_NONTRADABLE"
                    title="Guild Banner Victory Emote Charge (x40)"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_KILLFAME_LARGE_BATTLE_02"
                    name="Gain 300,000 Kill Fame from kills with 10 or more assists"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_DISSARRAY_03"
                    name="Get a Level 20 Disarray debuff"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_PLAYERBATTLE_04"
                    name="Be part of a battle with at least 60 player deaths"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_PLAYER_KILLSPREE_03"
                    name="Kill or assist in killing 30 players within one minute"
                    id="T1_KILL_EMOTE_HELLGATE_CHARGES_NONTRADABLE"
                    title="Hellgate Victory Emote Charge (x100)"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_DISSARRAY_04"
                    name="Get a Level 30 Disarray debuff"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_KILLFAME_LARGE_BATTLE_03"
                    name="Gain a million Kill Fame from kills with 10 or more assists"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_PLAYERBATTLE_05"
                    name="Be part of a battle with at least 85 player deaths"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_DISSARRAY_05"
                    name="Get a Level 40 Disarray debuff"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_PLAYERBATTLE_06"
                    name="Be part of a battle with at least 120 player deaths"
                    id="T1_KILL_EMOTE_TOMBSTONE_CHARGES_NONTRADABLE"
                    title="Tombstone Victory Emote Charge (x100)"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_PLAYER_KILLSPREE_04"
                    name="Kill or assist in killing 50 players within one minute"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_KILLFAME_LARGE_BATTLE_04"
                    name="Gain 3 million Kill Fame from kills with 10 or more assists"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_PLAYERBATTLE_07"
                    name="Be part of a battle with at least 150 player deaths"
                    id="T1_KILL_EMOTE_SWORD_CHARGES_NONTRADABLE"
                    title="Sword Victory Emote Charge (x700)"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_KILLFAME_LARGE_BATTLE_05"
                    name="Gain 10 million Kill Fame from kills with 10 or more assists"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_KILLFAME_LARGE_BATTLE_06"
                    name="Gain 30 million Kill Fame from kills with 10 or more assists"
                    id="T1_KILL_EMOTE_GHOST_CHARGES_NONTRADABLE"
                    title="Ghost Victory Emote Charge (x700)"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_KILLFAME_LARGE_BATTLE_07"
                    name="Gain 100 million Kill Fame from kills with 10 or more assists"
                    id="T5_LEARNINGPOINTS_NONTRADABLE"
                    title="Expert's Tome of Learning"
                  />
                </tbody>
              </Table>

              <h4>Territories (31)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="JOURNAL_GUILD_CLAIM_TERRITORY"
                    name="Claim a Territory with your Guild"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="SA_COLLECTION_TERRITORY_ENERGY"
                    name="Successfully transport a Power Crystal to a Territory"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="SA_PVP_TERRITORY_DEFEAT_COMMANDER"
                    name="Defeat the Sentry Mage in an enemy territory"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_DAMAGE_FORTIFICATION_01"
                    name="Deal 5,000 damage to enemy Fortifications"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_PVP_TERRITORY_DEFEAT_SIPHONINGMAGE_01"
                    name="Defeat 4 Siphoning Mages"
                    id="T1_KILL_EMOTE_OVERGROWN_CHARGES_NONTRADABLE"
                    title="Overgrown Victory Emote Charge (x20)"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_COLLECTION_TERRITORY_ENERGY_02"
                    name="Transport a Substantial Power Crystal to a Territory"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_RAW_ENERGY_01"
                    name="Deliver 300 Raw Energy to a Territory"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_FORTIFICATIONS_UPGRADED_01"
                    name="Have every Fortification on your Territory upgraded to Tier 4"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_DAMAGE_FORTIFICATION_02"
                    name="Deal 3,000 damage to Fortification Gates"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_RAW_ENERGY_02"
                    name="Deliver 2,000 Raw Energy to a Territory"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    entryID="SA_PVP_GVG_WIN_01"
                    name="Participate in a successful attack on a territory"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_TERRITORY_RAID_01"
                    name="Participate in 10 Raids"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_FORTIFICATIONS_UPGRADED_02"
                    name="Have every Fortification on your Territory upgraded to Tier 6"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="SA_PVP_GVG_OPEN_ENEMY_GATE"
                    name="Help open the gate of an enemy territory from within"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_COLLECTION_TERRITORY_ENERGY_03"
                    name="Transport an Extraordinary Power Crystal to a Territory"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_PVP_TERRITORY_DEFEAT_SIPHONINGMAGE_02"
                    name="Defeat 30 Siphoning Mages"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_USE_BANNER"
                    name="Use a Siege Banner on an enemy Territory"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_TERRITORY_RAID_02"
                    name="Participate in 30 Raids"
                    id="T1_KILL_EMOTE_TOMBSTONE_CHARGES_NONTRADABLE"
                    title="Tombstone Victory Emote Charge (x40)"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_COLLECTION_TERRITORY_ENERGY_04"
                    name="Transport an Overwhelming Power Crystal to a Territory"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_RAW_ENERGY_03"
                    name="Deliver 10,000 Raw Energy to a Territory"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_TERRITORY_ATTACK_01"
                    name="Participate in 10 successful attacks on a Territory"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="SA_PVP_GVG_MAX_UPGRADES"
                    name="Enter a fully upgraded territory that's owned by your guild"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_DAMAGE_FORTIFICATION_03"
                    name="Deal 20,000 damage to Tier 6 or higher Fortifications"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_PVP_TERRITORY_DEFEAT_SIPHONINGMAGE_03"
                    name="Defeat 100 Siphoning Mages"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_TERRITORY_RAID_03"
                    name="Participate in 100 Raids"
                    id="T1_KILL_EMOTE_SWORD_CHARGES_NONTRADABLE"
                    title="Sword Victory Emote Charge (x100)"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_DAMAGE_FORTIFICATION_04"
                    name="Deal 50,000 damage to Tier 8 Fortifications"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_TERRITORY_ATTACK_02"
                    name="Participate in 30 successful attacks on a Territory"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight (x2)"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_DAMAGE_FORTIFICATION_05"
                    name="Deal 20000 damage to Tier 8 Fortification Gates"
                    id="T1_KILL_EMOTE_FLAG_CHARGES_NONTRADABLE"
                    title="Guild Banner Victory Emote Charge (x700)"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_COLLECTION_TERRITORY_ENERGY_05"
                    name="Deliver 30 Overwhelming Territory Power Crystals"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x100)"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_TERRITORY_ATTACK_03"
                    name="Participate in 100 successful attacks on a Territory"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight (x5)"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_COLLECTION_TERRITORY_ENERGY_06"
                    name="Deliver 100 Overwhelming Territory Power Crystals"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x15)"
                  />
                </tbody>
              </Table>

              <h4>Guild Season (17)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="JOURNAL_GUILD_GUILD_SEASON_POINTS_01"
                    name="Earn 100 Season Points with your Guild"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_GUILD_SEASON_POINTS_02"
                    name="Earn 300 Season Points with your Guild"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_GUILD_SEASON_POINTS_03"
                    name="Earn 1,000 Season Points with your Guild"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_GUILD_SEASON_POINTS_04"
                    name="Earn 2,500 Season Points with your Guild"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_GUILD_SEASON_POINTS_05"
                    name="Earn 5,000 Season Points with your Guild"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_GUILD_SEASON_POINTS_06"
                    name="Earn 10,000 Season Points with your Guild"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_GUILD_SEASON_POINTS_07"
                    name="Earn 20,000 Season Points with your Guild"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_GUILD_SEASON_POINTS_08"
                    name="Earn 40,000 Season Points with your Guild"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_GUILD_SEASON_POINTS_09"
                    name="Earn 65,000 Season Points with your Guild"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_GUILD_SEASON_POINTS_10"
                    name="Earn 100,000 Season Points with your Guild"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_GUILD_SEASON_POINTS_11"
                    name="Earn 140,000 Season Points with your Guild"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_GUILD_SEASON_POINTS_12"
                    name="Earn 200,000 Season Points with your Guild"
                    id="T5_LEARNINGPOINTS_NONTRADABLE"
                    title="Expert's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_GUILD_SEASON_IRON_BRACKET"
                    name="Earn the Iron Bracket Guild Season Reward or higher"
                    id="T4_SHARD_CRYSTAL"
                    title="Adept's Crystal Shard (x10)"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_GUILD_SEASON_BRONZE_BRACKET"
                    name="Earn the Bronze Bracket Guild Season Reward or higher"
                    id="T4_SHARD_CRYSTAL"
                    title="Adept's Crystal Shard (x20)"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_GUILD_SEASON_SILVER_BRACKET"
                    name="Earn the Silver Bracket Guild Season Reward or higher"
                    id="T5_SHARD_CRYSTAL"
                    title="Expert's Crystal Shard (x20)"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_GUILD_SEASON_GOLD_BRACKET"
                    name="Earn the Gold Bracket Guild Season Reward or higher"
                    id="T5_SHARD_CRYSTAL"
                    title="Expert's Crystal Shard (x30)"
                  />
                  <Entry
                    entryID="JOURNAL_GUILD_GUILD_SEASON_CRYSTAL_BRACKET"
                    name="Earn the Crystal Bracket Guild Season Reward or higher"
                    id="T6_SHARD_CRYSTAL"
                    title="Master's Crystal Shard (x50)"
                  />
                </tbody>
              </Table>
            </AccordionBody>
          </AccordionItem>
        </UncontrolledAccordion>
      </Section>

      {/* Islands */}
      <Section>
        <UncontrolledAccordion id="island">
          <AccordionItem>
            <AccordionHeader targetId="island">Islands (193)</AccordionHeader>
            <AccordionBody accordionId="island">
              <h4>Personal Islands (20)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="SA_PLAYERISLAND"
                    name="Get your very own island"
                    id="PLAYERISLAND_FURNITUREITEM_STONE_WELL_A"
                    title="Stone well"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_PERSONALISLAND_LEVEL_01"
                    name="Upgrade your Personal Island to level 2"
                    id="T5_FOCUSPOTION_NONTRADABLE"
                    title="Expert's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_PERSONALISLAND_OUTDOOR_FURNITURE_01"
                    name="Place 3 decoration items on one of your islands"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_PERSONALISLAND_LEVEL_02"
                    name="Upgrade your Personal Island to level 3"
                    id="T6_FOCUSPOTION_NONTRADABLE"
                    title="Master's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_PERSONALISLAND_OUTDOOR_FURNITURE_02"
                    name="Place 10 decoration items on one of your islands"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_PERSONALISLAND_LEVEL_03"
                    name="Upgrade your Personal Island to level 4"
                    id="T4_SKILLBOOK_GATHER_ORE_NONTRADABLE"
                    title="Adept Ore Miner Tome"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_PERSONALISLAND_VISITORS_01"
                    name="Be on your Player Island with another player"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_PERSONALISLAND_LEVEL_04"
                    name="Upgrade your Personal Island to level 5"
                    id="UNIQUE_FOCUSPOTION_ADC_NONTRADABLE_01"
                    title="Grandmaster's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_PERSONALISLAND_VISITORS_02"
                    name="Be on a Player Island with 2 other players"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x10)"
                  />
                  <Entry
                    entryID="SA_PLAYERISLAND_MAX"
                    name="Upgrade your island to the maximum of 6/6"
                    id="T5_SKILLBOOK_GATHER_ORE_NONTRADABLE"
                    title="Expert Ore Miner Tome"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_PERSONALISLAND_OUTDOOR_FURNITURE_03"
                    name="Place 30 decoration items on one of your islands"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_PERSONALISLAND_MORGANA_WEAPONCRATE"
                    name="Place an Army Crate on your island"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_PERSONALISLAND_BIOMES_01"
                    name="Visit Personal Islands in 3 different Biomes"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x10)"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_PERSONALISLAND_VISITORS_03"
                    name="Be on a Player Island with 4 other players"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_PERSONALISLAND_MULTIPLE_ISLANDS_01"
                    name="Own 2 Personal Islands simultaneously"
                    id="T6_SKILLBOOK_GATHER_ORE_NONTRADABLE"
                    title="Master Ore Miner Tome"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_PERSONALISLAND_BIOMES_02"
                    name="Visit Personal Islands in 5 different Biomes"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_PERSONALISLAND_BIOMES_03"
                    name="Visit islands in every biome"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x20)"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_PERSONALISLAND_MULTIPLE_ISLANDS_02"
                    name="Own 3 Personal Islands at level 3 or higher"
                    id="T7_SKILLBOOK_GATHER_ORE_NONTRADABLE"
                    title="Grandmaster Ore Miner Tome"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_PERSONALISLAND_MULTIPLE_ISLANDS_03"
                    name="Own 5 Personal Islands at level 4 or higher"
                    id="T8_SKILLBOOK_GATHER_ORE_NONTRADABLE"
                    title="Elder Ore Miner Tome"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_PERSONALISLAND_MULTIPLE_ISLANDS_04"
                    name="Own 7 Personal Islands at level 6"
                    id="T8_FOCUSPOTION_NONTRADABLE"
                    title="Elder's Focus Restoration Potion"
                  />
                </tbody>
              </Table>

              <h4>Buildings (32)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="SA_PLAYERISLAND_BUILD_01"
                    name="Build a house on your island"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_BUILDINGS_HOUSE_FURNITURE_01"
                    name="Place a Tier 2 Chest in your House"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_BUILDINGS_BUILD_HOUSE_02"
                    name="Upgrade your House to Tier 3"
                    id="T4_FOCUSPOTION_NONTRADABLE"
                    title="Adept's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_BUILDINGS_HOUSE_FURNITURE_02"
                    name="Place 3 furniture items in your House"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="SA_PLAYERISLAND_LABORER_01"
                    name="Employ any kind of Laborer"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_BUILDINGS_INVEST_RESOURCES_01"
                    name="Invest a total of 3,500 Item Value worth of resources into buildings"
                    id="T4_SKILLBOOK_GATHER_ROCK_NONTRADABLE"
                    title="Adept Quarrier Tome"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_BUILDINGS_BUILD_HOUSE_03"
                    name="Upgrade your House to Tier 4"
                    id="T5_FOCUSPOTION_NONTRADABLE"
                    title="Expert's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_BUILDINGS_BUILD_FARM_01"
                    name="Build or upgrade a Farming Building to Tier 3"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_BUILDINGS_BUILD_FARM_02"
                    name="Upgrade 2 different Farm Buildings to Tier 3"
                    id="T4_SKILLBOOK_GATHER_WOOD_NONTRADABLE"
                    title="Adept Lumberjack Tome"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_BUILDINGS_INVEST_RESOURCES_02"
                    name="Invest a total of 15,000 Item Value worth of resources into buildings"
                    id="PLAYERISLAND_FURNITUREITEM_WOOD_LANTERN_A"
                    title="Simple lantern"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_BUILDINGS_BUILD_HOUSE_04"
                    name="Upgrade your House to Tier 5"
                    id="T5_FOCUSPOTION_NONTRADABLE"
                    title="Expert's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="SA_PLAYERISLAND_LABORER_03"
                    name="Send a Laborer on a mission with 100% Yield from Happiness"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x15)"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_BUILDINGS_BUILD_ECONOMY_01"
                    name="Upgrade an Economy Building to Tier 4"
                    id="T5_SKILLBOOK_GATHER_ROCK_NONTRADABLE"
                    title="Expert Quarrier Tome"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_BUILDINGS_INVEST_RESOURCES_03"
                    name="Invest a total of 30,000 Item Value worth of resources into buildings"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_BUILDINGS_BUILD_HOUSE_05"
                    name="Upgrade your House to Tier 6"
                    id="T6_FOCUSPOTION_NONTRADABLE"
                    title="Master's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_BUILDINGS_BUILD_FARM_03"
                    name="Upgrade a Farming Building to Tier 5"
                    id="T5_SKILLBOOK_GATHER_WOOD_NONTRADABLE"
                    title="Expert Lumberjack Tome"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_BUILDINGS_BUILD_HOUSE_06"
                    name="Upgrade your House to Tier 7"
                    id="T6_FOCUSPOTION_NONTRADABLE"
                    title="Master's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_BUILDINGS_BUILD_ECONOMY_02"
                    name="Upgrade an Economy Building to Tier 6"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_BUILDINGS_INVEST_RESOURCES_04"
                    name="Invest a total of 140,000 Item Value worth of resources into Buildings"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="SA_PLAYERISLAND_BUILD_02"
                    name="Upgrade a house on your island to Tier 8"
                    id="T6_SKILLBOOK_GATHER_ROCK_NONTRADABLE"
                    title="Master Quarrier Tome"
                  />
                  <Entry
                    entryID="SA_PLAYERISLAND_LABORER_02"
                    name="Have a Tier 8 Laborer and send them on a mission"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_BUILDINGS_BUILD_MILITARY_01"
                    name="Upgrade a Military Building to Tier 6"
                    id="T6_SKILLBOOK_GATHER_WOOD_NONTRADABLE"
                    title="Master Lumberjack Tome"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_BUILDINGS_BUILD_ECONOMY_03"
                    name="Upgrade an Economy Building to Tier 8"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_BUILDINGS_BUILD_FARM_04"
                    name="Upgrade a Farming Building to Tier 8"
                    id="T7_SKILLBOOK_GATHER_WOOD_NONTRADABLE"
                    title="Grandmaster Lumberjack Tome"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_BUILDINGS_BUILD_MILITARY_02"
                    name="Upgrade a Military Building to Tier 8"
                    id="T7_SKILLBOOK_GATHER_ROCK_NONTRADABLE"
                    title="Grandmaster Quarrier Tome"
                  />
                  <Entry
                    entryID="JOURNAL_ISLANDS_BUILDINGS_LABORER_04"
                    name="Send a Tier 8 Laborer with maxed Happiness on a mission"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_BUILDINGS_BUILD_FARM_05"
                    name="Upgrade every Farming Building to Tier 8 at least once"
                    id="T8_SKILLBOOK_GATHER_WOOD_NONTRADABLE"
                    title="Elder Lumberjack Tome"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_BUILDINGS_BUILD_ECONOMY_04"
                    name="Upgrade every Economy Building to Tier 8 at least once"
                    id="UNIQUE_FOCUSPOTION_ADC_NONTRADABLE_01"
                    title="Grandmaster's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_BUILDINGS_BUILD_MILITARY_03"
                    name="Upgrade every Military Building to Tier 8 at least once"
                    id="T8_SKILLBOOK_GATHER_ROCK_NONTRADABLE"
                    title="Elder Quarrier Tome"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_BUILDINGS_INVEST_RESOURCES_05"
                    name="Invest a total of 500,000 Item Value worth of resources into buildings"
                    id="T8_FOCUSPOTION_NONTRADABLE"
                    title="Elder's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_BUILDINGS_INVEST_RESOURCES_06"
                    name="Invest a total of 1 million Item Value worth of resources into buildings"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_BUILDINGS_INVEST_RESOURCES_07"
                    name="Invest a total of 3 million Item Value worth of resources into buildings"
                    id="T8_FOCUSPOTION_NONTRADABLE"
                    title="Elder's Focus Restoration Potion"
                  />
                </tbody>
              </Table>

              <h4>Farming (32)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="JOURNAL_ISLAND_FARMING_FARM_01"
                    name="Build a Farm on your island"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="SA_FARMING_FAME_01"
                    name="Farm your first crop"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_FARMING_CROP_TYPE_01"
                    name="Harvest 70 Wheat"
                    id="T3_FOCUSPOTION_NONTRADABLE"
                    title="Journeyman's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_FARMING_WATERCROPS_01"
                    name="Water 20 Crops or Herbs"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_FARMING_FAME_02"
                    name="Farm Crops worth 5,000 Fame"
                    id="T4_SKILLBOOK_GATHER_FIBER_NONTRADABLE"
                    title="Adept Fiber Harvester Tome"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_FARMING_CROP_TYPE_02"
                    name="Harvest 140 Cabbages"
                    id="T3_FOCUSPOTION_NONTRADABLE"
                    title="Journeyman's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_FARMING_FAME_03"
                    name="Farm Crops worth 12,000 Fame"
                    id="T4_FOCUSPOTION_NONTRADABLE"
                    title="Adept's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_FARMING_HERBGARDEN_01"
                    name="Build a Herb Garden"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_FARMING_CROP_TYPE_03"
                    name="Harvest 70 Herbs"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_FARMING_CROP_TYPE_04"
                    name="Harvest 150 Crops or Herbs with a local Yield Bonus"
                    id="T4_FOCUSPOTION_NONTRADABLE"
                    title="Adept's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_FARMING_CROP_TYPE_05"
                    name="Harvest 100 of each of 8 different types of Crops or Herbs"
                    id="T5_SKILLBOOK_GATHER_FIBER_NONTRADABLE"
                    title="Expert Fiber Harvester Tome"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_FARMING_FAME_04"
                    name="Farm Crops and Herbs worth 36,000 Fame"
                    id="T5_FOCUSPOTION_NONTRADABLE"
                    title="Expert's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_FARMING_CROP_FAST_01"
                    name="Harvest 150 Crops or Herbs in 10 minutes on a single island"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_FARMING_CROP_TYPE_06"
                    name="Harvest 3,000 Crops or Herbs"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_FARMING_CROP_TYPE_07"
                    name="Harvest 160 Elusive Foxgloves"
                    id="T5_FOCUSPOTION_NONTRADABLE"
                    title="Expert's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_FARMING_CROP_FAST_02"
                    name="Harvest 450 Crops or Herbs in 10 minutes on a single island"
                    id="T6_SKILLBOOK_GATHER_FIBER_NONTRADABLE"
                    title="Master Fiber Harvester Tome"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_FARMING_CROP_TYPE_08"
                    name="Harvest 4,500 Crops or Herbs"
                    id="T5_FOCUSPOTION_NONTRADABLE"
                    title="Expert's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_FARMING_CROP_TYPE_09"
                    name="Harvest 200 Tier 7 Crops or Herbs"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x10)"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_FARMING_CROP_FAST_03"
                    name="Harvest 700 Crops or Herbs in 10 minutes on a single island"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_FARMING_CROP_TYPE_10"
                    name="Harvest 400 of each of 12 different types of Crops or Herbs"
                    id="T5_FOCUSPOTION_NONTRADABLE"
                    title="Expert's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_FARMING_CROP_FAST_04"
                    name="Harvest 1,000 Crops or Herbs in 10 minutes on a single island"
                    id="T7_SKILLBOOK_GATHER_FIBER_NONTRADABLE"
                    title="Grandmaster Fiber Harvester Tome"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_FARMING_CROP_FAST_05"
                    name="Harvest 1,200 Crops or Herbs in 10 minutes on a single island"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_FARMING_CROP_FAST_06"
                    name="Harvest 1,400 Crops in 10 minutes on a single island"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x25)"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_FARMING_CROP_FAST_07"
                    name="Harvest 1,400 Herbs in 10 minutes on a single island"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x25)"
                  />
                  <Entry
                    entryID="SA_FARMING_FAME_02"
                    name="Farm crops worth 100,000 Fame"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_FARMING_FAME_06"
                    name="Farm Crops worth 300,000 Fame"
                    id="T5_FOCUSPOTION_NONTRADABLE"
                    title="Expert's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_FARMING_CROP_TYPE_11"
                    name="Harvest 500 of each of every different type of Crop and Herb"
                    id="T6_FOCUSPOTION_NONTRADABLE"
                    title="Master's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="SA_FARMING_FAME_03"
                    name="Farm crops worth 1,000,000 Fame"
                    id="T8_SKILLBOOK_GATHER_FIBER_NONTRADABLE"
                    title="Elder Fiber Harvester Tome"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_FARMING_FAME_08"
                    name="Farm Crops worth 3,000,000 Fame"
                    id="T6_FOCUSPOTION_NONTRADABLE"
                    title="Master's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_FARMING_CROP_TYPE_12"
                    name="Harvest 1,000 Crops on an Outlands Farming Territory"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_FARMING_CROP_TYPE_13"
                    name="Harvest 3,000 Crops on an Outlands Farming Territory"
                    id="T5_FOCUSPOTION_NONTRADABLE"
                    title="Expert's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_FARMING_CROP_TYPE_14"
                    name="Harvest 10,000 Crops on an Outlands Farming Territory"
                    id="T6_FOCUSPOTION_NONTRADABLE"
                    title="Master's Focus Restoration Potion"
                  />
                </tbody>
              </Table>

              <h4>Animal Breeding (32)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="SA_FARMING_HORSE"
                    name="Raise a horse"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_ANIMALBREEDING_SADDLE_MOUNT_01"
                    name="Saddle a Horse"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_ANIMALBREEDING_RAISE_ANIMALS_01"
                    name="Raise 10 animals"
                    id="T3_FOCUSPOTION_NONTRADABLE"
                    title="Journeyman's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_ANIMALBREEDING_ANIMAL_REWARDS_01"
                    name="Collect 30 Eggs from Chickens"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_ANIMALBREEDING_ANIMAL_PROCESSING_01"
                    name="Produce 100 Meat at the Butcher"
                    id="UNIQUE_FURNITUREITEM_ADC_RUG_WOLF"
                    title="Wolf Rug"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_ANIMALBREEDING_RAISE_ANIMALS_02"
                    name="Raise 3 different types of animals"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x10)"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_ANIMALBREEDING_SADDLE_MOUNT_02"
                    name="Saddle 5 Mounts"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_ANIMALBREEDING_RAISE_ANIMALS_03"
                    name="Raise 6 different types of animals"
                    id="T4_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                    title="Adept Animal Skinner Tome"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_ANIMALBREEDING_RAISE_SPECIFIC_ANIMALS_01"
                    name="Raise a Fawn into a Giant Stag"
                    id="T4_FOCUSPOTION_NONTRADABLE"
                    title="Adept's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_ANIMALBREEDING_BUILD_KENNEL_01"
                    name="Build a Kennel on your island"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_ANIMALBREEDING_RAISE_SPECIFIC_ANIMALS_02"
                    name="Raise a Swiftclaw"
                    id="T5_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                    title="Expert Animal Skinner Tome"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_ANIMALBREEDING_RAISE_ANIMALS_04"
                    name="Raise a Faction Warfare Mount"
                    id="T4_FOCUSPOTION_NONTRADABLE"
                    title="Adept's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_ANIMALBREEDING_RAISE_ANIMALS_05"
                    name="Raise 10 different types of animals"
                    id="T5_FOCUSPOTION_NONTRADABLE"
                    title="Expert's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_ANIMALBREEDING_ANIMAL_REWARDS_02"
                    name="Collect milk from farm animals 100 times"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_ANIMALBREEDING_RAISE_ANIMALS_06"
                    name="Raise 15 different types of animals"
                    id="T6_FOCUSPOTION_NONTRADABLE"
                    title="Master's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_ANIMALBREEDING_RAISE_SPECIFIC_ANIMALS_03"
                    name="Raise a Direwolf"
                    id="UNIQUE_FURNITUREITEM_ADC_STATUE_MOUNTED_DIREWOLF_A"
                    title="Wolf Rider Statue (L)"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_ANIMALBREEDING_COLLECT_OFFSPRING_01"
                    name="Have offspring from 10 different types of animals"
                    id="T6_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                    title="Master Animal Skinner Tome"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_ANIMALBREEDING_RAISE_ANIMALS_07"
                    name="Raise 21 different types of animals"
                    id="T6_FOCUSPOTION_NONTRADABLE"
                    title="Master's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_ANIMALBREEDING_ANIMAL_REWARDS_03"
                    name="Collect 350 Eggs in 10 minutes on a single island"
                    id="UNIQUE_UNLOCK_OFF_VANITY_PIRATE_RED_NON_TRADABLE"
                    title="Wardrobe Skin: Navigator's Red Parrot Cage"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_ANIMALBREEDING_COLLECT_OFFSPRING_02"
                    name="Have offspring from 16 different types of animals"
                    id="T6_FOCUSPOTION_NONTRADABLE"
                    title="Master's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_ANIMALBREEDING_COLLECT_OFFSPRING_03"
                    name="Have 2 offspring from a single horse"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_ANIMALBREEDING_ANIMAL_REWARDS_04"
                    name="Produce 2,000 Meat at the Butcher"
                    id="T7_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                    title="Grandmaster Animal Skinner Tome"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_ANIMALBREEDING_ANIMAL_REWARDS_05"
                    name="Collect 900 Eggs in 10 minutes on a single island"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x20)"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_ANIMALBREEDING_RAISE_ANIMALS_08"
                    name="Raise a Tier 7 Mount"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_ANIMALBREEDING_RAISE_ANIMALS_09"
                    name="Raise 28 different types of animals"
                    id="UNIQUE_FOCUSPOTION_ADC_NONTRADABLE_01"
                    title="Grandmaster's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_ANIMALBREEDING_COLLECT_OFFSPRING_04"
                    name="Have Offspring from 21 different types of animals"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_ANIMALBREEDING_RAISE_ANIMALS_10"
                    name="Raise a Faction Warfare Elite Mount"
                    id="T8_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                    title="Elder Animal Skinner Tome"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_ANIMALBREEDING_RAISE_ANIMALS_11"
                    name="Raise 35 different types of animals"
                    id="UNIQUE_FOCUSPOTION_ADC_NONTRADABLE_01"
                    title="Grandmaster's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_ANIMALBREEDING_RAISE_SPECIFIC_ANIMALS_04"
                    name="Raise a Mammoth"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x30)"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_ANIMALBREEDING_RAISE_ANIMALS_12"
                    name="Raise all different types of animals"
                    id="T8_FOCUSPOTION_NONTRADABLE"
                    title="Elder's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_ANIMALBREEDING_COLLECT_OFFSPRING_05"
                    name="Collect the offspring of a Mammoth"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_ANIMALBREEDING_COLLECT_OFFSPRING_06"
                    name="Have the offspring of every type of animal"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x75)"
                  />
                </tbody>
              </Table>

              <h4>Create Food (32)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_FOOD_COOK_SPECIFIC_01"
                    name="Create 20 Carrot Soups"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_FOOD_FISH_BAIT_01"
                    name="Create 5 Simple Fish Baits"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_FOOD_COOK_SPECIFIC_02"
                    name="Create 10 Bean Salads"
                    id="T3_FOCUSPOTION_NONTRADABLE"
                    title="Journeyman's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_FOOD_CHOP_FISH_01"
                    name="Create 30 Chopped Fish at the Butcher building"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_FOOD_COOK_SPECIFIC_03"
                    name="Create 5 Clam Soups"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_FOOD_COOK_SPECIFIC_04"
                    name="Create 30 Omelettes"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x10)"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_FOOD_COOK_SPECIFIC_05"
                    name="Create 40 Roast Chicken"
                    id="T4_FOCUSPOTION_NONTRADABLE"
                    title="Adept's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_FOOD_CHOP_FISH_02"
                    name="Create 150 Chopped Fish at the Butcher building"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_FOOD_COOK_SPECIFIC_06"
                    name="Create 10 Goat Butter at a Mill building"
                    id="T4_SKILLBOOK_GATHER_WOOD_NONTRADABLE"
                    title="Adept Lumberjack Tome"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_FOOD_COOK_SPECIFIC_07"
                    name="Create 50 Sandwiches"
                    id="T4_FOCUSPOTION_NONTRADABLE"
                    title="Adept's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_FOOD_COOK_SPECIFIC_08"
                    name="Create 9 Basic Fish Sauces"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_FOOD_COOK_ENCHANTED_01"
                    name="Create a Food item with Enchantment Level 1"
                    id="T4_SKILLBOOK_GATHER_ROCK_NONTRADABLE"
                    title="Adept Quarrier Tome"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_FOOD_COOK_SPECIFIC_09"
                    name="Create 40 Goose Omelettes"
                    id="T5_FOCUSPOTION_NONTRADABLE"
                    title="Expert's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_FOOD_COOK_SPECIFIC_10"
                    name="Create an Avalonian Goat Stew"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x10)"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_FOOD_COOK_GENERAL_01"
                    name="Create every Tier 4 Food item"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_FOOD_COOK_ENCHANTED_02"
                    name="Create 20 Food items with Enchantment Level 2"
                    id="T5_SKILLBOOK_GATHER_ORE_NONTRADABLE"
                    title="Expert Ore Miner Tome"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_FOOD_COOK_GENERAL_02"
                    name="Create every Tier 5 Food item"
                    id="T5_FOCUSPOTION_NONTRADABLE"
                    title="Expert's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_FOOD_COOK_SPECIFIC_11"
                    name="Create 50 Potato Salads"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x20)"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_FOOD_COOK_GENERAL_03"
                    name="Create every Tier 6 Food item"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_FOOD_COOK_ENCHANTED_03"
                    name="Create 40 Food items with Enchantment Level 3"
                    id="T5_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                    title="Expert Animal Skinner Tome"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_FOOD_COOK_GENERAL_04"
                    name="Create 100 Food items using the Local Production Bonus"
                    id="UNIQUE_UNLOCK_ARMOR_VANITY_INNKEEPER_NON_TRADABLE"
                    title="Wardrobe Skin: Innkeeper's Shirt"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_FOOD_COOK_GENERAL_05"
                    name="Create 250 Tier 7 Food items"
                    id="T5_SKILLBOOK_GATHER_FIBER_NONTRADABLE"
                    title="Expert Fiber Harvester Tome"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_FOOD_COOK_GENERAL_06"
                    name="Create every Tier 7 Food item"
                    id="T5_FOCUSPOTION_NONTRADABLE"
                    title="Expert's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_FOOD_COOK_ENCHANTED_04"
                    name="Create 250 Tier 7.3 Food items"
                    id="UNIQUE_FURNITUREITEM_XMAS_FILL_CITY_TREE_A"
                    title="Decorated Pine Tree"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_FOOD_COOK_GENERAL_07"
                    name="Create 250 Tier 7 Food items with Fish"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_FOOD_COOK_GENERAL_08"
                    name="Create every type of Food item"
                    id="T6_FOCUSPOTION_NONTRADABLE"
                    title="Master's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_FOOD_COOK_ENCHANTED_05"
                    name="Create 100 Tier 7.3 or Tier 8.3 Avalonian Food items"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_FOOD_COOK_GENERAL_09"
                    name="Create 1,000 Tier 8 Food items using the Local Production Bonus"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x25)"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_FOOD_COOK_ENCHANTED_06"
                    name="Create 1,000 Tier 7.3 or Tier 8.3 Food items"
                    id="T6_FOCUSPOTION_NONTRADABLE"
                    title="Master's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_FOOD_COOK_GENERAL_10"
                    name="Create 10,000 Tier 7 or Tier 8 Fish Food items"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x60)"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_FOOD_COOK_ENCHANTED_07"
                    name="Create 10,000 Tier 7.3 or Tier 8.3 Food items"
                    id="UNIQUE_FOCUSPOTION_ADC_NONTRADABLE_01"
                    title="Grandmaster's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_FOOD_COOK_GENERAL_11"
                    name="Create 100,000 Tier 7 or Tier 8 Food items"
                    id="T8_FOCUSPOTION_NONTRADABLE"
                    title="Elder's Focus Restoration Potion"
                  />
                </tbody>
              </Table>

              <h4>Create Potions (28)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_POTIONS_BREW_SPECIFIC_01"
                    name="Create 10 Healing Potions"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_POTIONS_BREW_SPECIFIC_02"
                    name="Create 15 Gigantify Potions"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_POTIONS_BREW_GENERAL_01"
                    name="Create 25 Tier 2 Potions"
                    id="T3_FOCUSPOTION_NONTRADABLE"
                    title="Journeyman's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_POTIONS_BREW_SPECIFIC_03"
                    name="Create 10 Minor Cleansing Potions"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_POTIONS_BREW_GENERAL_02"
                    name="Create 75 Potions"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_POTIONS_BREW_GENERAL_03"
                    name="Create every Tier 3 Potion"
                    id="T4_SKILLBOOK_GATHER_FIBER_NONTRADABLE"
                    title="Adept Fiber Harvester Tome"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_POTIONS_BREW_SPECIFIC_04"
                    name="Create 20 Poison Potions"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_POTIONS_BREW_SPECIFIC_05"
                    name="Create 10 Gathering Potions"
                    id="T4_FOCUSPOTION_NONTRADABLE"
                    title="Adept's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_POTIONS_BREW_SPECIFIC_06"
                    name="Create 20 Tier 4 Healing Potions"
                    id="T4_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                    title="Adept Animal Skinner Tome"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_POTIONS_BREW_SPECIFIC_07"
                    name="Create 10 Hellfire Potions"
                    id="UNIQUE_FURNITUREITEM_MORGANA_CAMPFIRE_D@2"
                    title="Cauldron (Disciples of Morgana)"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_POTIONS_ARCANE_EXTRACT_01"
                    name="Create 15 Basic Arcane Extracts"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_POTIONS_BREW_ENCHANTED_01"
                    name="Create 10 Potions with Enchantment Level 1"
                    id="T4_SKILLBOOK_GATHER_ORE_NONTRADABLE"
                    title="Adept Ore Miner Tome"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_POTIONS_BREW_GENERAL_04"
                    name="Create every Tier 4 Potion"
                    id="T4_FOCUSPOTION_NONTRADABLE"
                    title="Adept's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_POTIONS_BREW_GENERAL_05"
                    name="Create 40 Tier 5 Potions"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x15)"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_POTIONS_BREW_ENCHANTED_02"
                    name="Create 50 Potions with Enchantment Level 2"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_POTIONS_BREW_SPECIFIC_08"
                    name="Create 80 Potato Schnapps"
                    id="T5_FOCUSPOTION_NONTRADABLE"
                    title="Expert's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_POTIONS_BREW_SPECIFIC_09"
                    name="Create 20 Major Energy Potions"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_POTIONS_BREW_ENCHANTED_03"
                    name="Create 100 Potions with Enchantment Level 3"
                    id="T5_SKILLBOOK_GATHER_ROCK_NONTRADABLE"
                    title="Expert Quarrier Tome"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_POTIONS_BREW_GENERAL_06"
                    name="Create every Tier 5 and Tier 6 Potion"
                    id="T5_FOCUSPOTION_NONTRADABLE"
                    title="Expert's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_POTIONS_BREW_GENERAL_07"
                    name="Create 500 Potions"
                    id="T5_SKILLBOOK_GATHER_WOOD_NONTRADABLE"
                    title="Expert Lumberjack Tome"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_POTIONS_BREW_GENERAL_08"
                    name="Create 100 Potions using the Local Production Bonus"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_POTIONS_BREW_GENERAL_09"
                    name="Create 1,000 Potions"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_POTIONS_BREW_GENERAL_10"
                    name="Create every type of Potion at least once"
                    id="T6_FOCUSPOTION_NONTRADABLE"
                    title="Master's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_POTIONS_BREW_ENCHANTED_04"
                    name="Create 100 Tier 7.3 or Tier 8.3 Potions"
                    id="T6_FOCUSPOTION_NONTRADABLE"
                    title="Master's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_POTIONS_BREW_ENCHANTED_05"
                    name="Create 1,000 Potions with Enchantment Level 3"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_POTIONS_BREW_GENERAL_11"
                    name="Create 3,000 Major Potions"
                    id="T6_FOCUSPOTION_NONTRADABLE"
                    title="Master's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_POTIONS_BREW_GENERAL_12"
                    name="Create 10,000 Major Potions"
                    id="T6_FOCUSPOTION_NONTRADABLE"
                    title="Master's Focus Restoration Potion"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_CREATE_POTIONS_BREW_GENERAL_13"
                    name="Create 100,000 Major Potions"
                    id="UNIQUE_FOCUSPOTION_ADC_NONTRADABLE_01"
                    title="Grandmaster's Focus Restoration Potion"
                  />
                </tbody>
              </Table>

              <h4>Guild Islands (17)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="JOURNAL_ISLAND_GUILDISLAND_GUILDISLAND_01"
                    name="Visit a Guild Island"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_GUILDISLAND_FEATURES_01"
                    name="Have a Guild Hall on your Guild's Island"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_GUILDISLAND_GUILDISLAND_02"
                    name="Visit a Level 3 Guild Island"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_GUILDISLAND_FEATURES_02"
                    name="Have a Guild Hall on your Guild's Island upgraded to Tier 4"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_GUILDISLAND_GUILDISLAND_03"
                    name="Visit a Level 6 Guild Island"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_GUILDISLAND_FEATURES_03"
                    name="Have a Guild Hall on your Guild's Island upgraded to Tier 8"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_GUILDISLAND_FEATURES_04"
                    name="Place 100 decorations on one of your Guild's Islands"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x5)"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_GUILDISLAND_GUILDMARKET_SELLING_01"
                    name="Earn 100,000 Silver on the Guild Marketplace"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_GUILDISLAND_GUILDMARKET_SELLING_02"
                    name="Earn a million Silver on the Guild Marketplace"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_GUILDISLAND_GUILDMARKET_BUYING_01"
                    name="Spend 100,000 silver on the Guild Marketplace"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_GUILDISLAND_GUILDMARKET_BUYING_02"
                    name="Spend a million Silver on the Guild Marketplace"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_GUILDISLAND_VISITORS_01"
                    name="Be on a Guild Island with 5 players at the same time"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_GUILDISLAND_VISITORS_02"
                    name="Be on a Guild Island with 10 players at the same time"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_GUILDISLAND_VISITORS_03"
                    name="Be on a Guild Island with 20 players at the same time"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_GUILDISLAND_BIOMES_01"
                    name="Visit Guild Islands in every biome"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x15)"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_GUILDISLAND_VISITORS_04"
                    name="Be on a Guild Island with 50 players at the same time"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x40)"
                  />
                  <Entry
                    entryID="JOURNAL_ISLAND_GUILDISLAND_VISITORS_05"
                    name="Be on a Guild Island with 150 players at the same time"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                </tbody>
              </Table>
            </AccordionBody>
          </AccordionItem>
        </UncontrolledAccordion>
      </Section>

      {/* Creatures */}
      <Section>
        <UncontrolledAccordion id="creatures">
          <AccordionItem>
            <AccordionHeader targetId="creatures">
              Creatures (186)
            </AccordionHeader>
            <AccordionBody accordionId="creatures">
              <h4>Heretics (33)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="JOURNAL_CREATURES_HERETICS_BESTIARY_MINER"
                    name="Defeat 25 Miners"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_HERETICS_BESTIARY_SCAVENGER"
                    name="Defeat 25 Scavengers"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_HERETICS_BESTIARY_WOODGATHERER"
                    name="Defeat 25 Gatherers"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_HERETICS_BESTIARY_WOODGATHERER_BOSS"
                    name="Defeat any Lumberjack or Chopper"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_HERETICS_BESTIARY_RATS"
                    name="Defeat 500 Foul Rats"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_HERETICS_BESTIARY_ALARMTRAP"
                    name="Defeat 15 Screamers"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_HERETICS_BESTIARY_FOREMAN_MINIBOSS"
                    name="Defeat any Foreman"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_HERETICS_BESTIARY_OVERSEER_BOSS"
                    name="Defeat 3 Overseers"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_HERETICS_BESTIARY_THIEF"
                    name="Defeat 50 Thieves or Cutthroats"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_HERETICS_BESTIARY_THIEF_MINIBOSS"
                    name="Defeat any Thug or Rouser"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_HERETICS_BESTIARY_POACHER"
                    name="Defeat 50 Poachers"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_HERETICS_BESTIARY_POACHER_MINIBOSS"
                    name="Defeat any Trapper"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_HERETICS_BESTIARY_DUALCROSSBOW"
                    name="Defeat 50 Shooters"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_HERETICS_BESTIARY_FIREMAGE"
                    name="Defeat 50 Firestarters or Arsonists"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_HERETICS_BESTIARY_FIREMAGE_MINIBOSS"
                    name="Defeat any Pyromaniac"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_HERETICS_BESTIARY_TANK"
                    name="Defeat 25 Bouncers or Goons"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_HERETICS_BESTIARY_TANK_MINIBOSS"
                    name="Defeat any Muscle or Bruiser"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_HERETICS_BESTIARY_BRAWLER"
                    name="Defeat 50 Brawlers"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_HERETICS_BESTIARY_BRAWLER_MINIBOSS"
                    name="Defeat any Spencer"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_HERETICS_BESTIARY_BRAWLER_BOSS"
                    name="Defeat any Roughneck or Chops"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_HERETICS_BESTIARY_MORTAR"
                    name="Defeat 25 Mortars"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_HERETICS_BESTIARY_BALLISTA"
                    name="Defeat 5 Cannoneers"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_HERETICS_BESTIARY_BALLISTA_BOSS"
                    name="Defeat any Trapmaster or Weaponsmaster"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_HERETICS_BESTIARY_HEALER"
                    name="Defeat 50 Hermits, Quacks, Healers, or Wisemen"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_HERETICS_BESTIARY_HEALER_BOSS"
                    name="Defeat any Fishy"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_HERETICS_BESTIARY_BOMBTHROWER_BOSS"
                    name="Defeat any Mad Fuzzy or Chief Blaster"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_HERETICS_BESTIARY_SHADOWMASK_BOSS"
                    name="Defeat any Shadowmask"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_HERETICS_KILL_100"
                    name="Defeat 100 Heretics"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_HERETICS_KILL_300"
                    name="Defeat 300 Heretics"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="SA_PVE_KILL_HERETIC"
                    name="Defeat 1,000 Heretics"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_HERETICS_KILL_3000"
                    name="Defeat 3,000 Heretics"
                    id="T4_CAPEITEM_HERETIC_BP"
                    title="Adept's Heretic Crest"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_HERETICS_KILL_10000"
                    name="Defeat 10,000 Heretics"
                    id="T6_CAPEITEM_HERETIC_BP"
                    title="Master's Heretic Crest"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_HERETICS_KILL_50000"
                    name="Defeat 50,000 Heretics"
                    id="T8_CAPEITEM_HERETIC_BP"
                    title="Elder's Heretic Crest"
                  />
                </tbody>
              </Table>

              <h4>Undead (31)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="JOURNAL_CREATURES_UNDEAD_BESTIARY_FRAIL_SKELETON"
                    name="Defeat 150 Frail or Brittle Skeletons"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_UNDEAD_BESTIARY_CURSED_SKELETON"
                    name="Defeat 25 Fragmenters"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_UNDEAD_BESTIARY_SCORPION"
                    name="Defeat 5 Scorpions"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_UNDEAD_BESTIARY_SWORDSMAN"
                    name="Defeat 100 Swordsmen or Revenants"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_UNDEAD_BESTIARY_SWORDSMAN_MINIBOSS"
                    name="Defeat any Swordmaster or Paragon"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_UNDEAD_BESTIARY_MAGE"
                    name="Defeat 100 Frostweavers or Deathmongers"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_UNDEAD_BESTIARY_MAGE_MINIBOSS"
                    name="Defeat any Deathmaster"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_UNDEAD_BESTIARY_MAGE_BOSS"
                    name="Defeat any Deathlord"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_UNDEAD_BESTIARY_NECROMANCER_BOSS"
                    name="Defeat any Necromancer or Cryomancer"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_UNDEAD_BESTIARY_ARCHER"
                    name="Defeat 75 Archers"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_UNDEAD_BESTIARY_ARCHER_MINIBOSS"
                    name="Defeat any Marksman or Sharpshooter"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_UNDEAD_BESTIARY_ARCHER_BOSS"
                    name="Defeat any Forgotten Champion"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_UNDEAD_BESTIARY_GHOUL"
                    name="Defeat 75 Ghouls"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_UNDEAD_BESTIARY_GHOUL_BOSS"
                    name="Defeat any Lacedon or Ghast"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_UNDEAD_BESTIARY_STATUE"
                    name="Defeat 25 Possessed Sculptures"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_UNDEAD_BESTIARY_SHADE"
                    name="Defeat 15 Shades"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_UNDEAD_BESTIARY_GHOST_RAT"
                    name="Defeat 250 Rats"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_UNDEAD_BESTIARY_GHOST_BAT"
                    name="Defeat 100 Bats"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_UNDEAD_BESTIARY_GHOST"
                    name="Defeat 100 Ghosts"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_UNDEAD_BESTIARY_GHOST_BOSS"
                    name="Defeat any Banshee"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_UNDEAD_BESTIARY_KNIGHT"
                    name="Defeat 50 Knights, Dreadknights, or Animated Armors"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_UNDEAD_BESTIARY_KNIGHT_MINIBOSS"
                    name="Defeat any Marshal"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_UNDEAD_BESTIARY_KNIGHT_BOSS"
                    name="Defeat any General"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_UNDEAD_BESTIARY_HERO_BOSS"
                    name="Defeat any Hero"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_UNDEAD_BESTIARY_HARVESTER"
                    name="Defeat any Reaper or Harvester"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_UNDEAD_KILL_100"
                    name="Defeat 100 Undead"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_UNDEAD_KILL_300"
                    name="Defeat 300 Undead"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="SA_PVE_KILL_UNDEAD"
                    name="Defeat 1,000 Undead"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_UNDEAD_KILL_3000"
                    name="Defeat 3,000 Undead"
                    id="T4_CAPEITEM_UNDEAD_BP"
                    title="Adept's Undead Crest"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_UNDEAD_KILL_10000"
                    name="Defeat 10,000 Undead"
                    id="T6_CAPEITEM_UNDEAD_BP"
                    title="Master's Undead Crest"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_UNDEAD_KILL_50000"
                    name="Defeat 50,000 Undead"
                    id="T8_CAPEITEM_UNDEAD_BP"
                    title="Elder's Undead Crest"
                  />
                </tbody>
              </Table>

              <h4>Keepers (26)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="JOURNAL_CREATURES_KEEPER_BESTIARY_ROCK_ELEMENTAL"
                    name="Defeat 10 Rock Elementals"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_KEEPER_BESTIARY_TREE_STUMP"
                    name="Defeat 10 Living Roots"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_KEEPER_BESTIARY_BERSERKER"
                    name="Defeat 50 Berserkers or Wildlings"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_KEEPER_BESTIARY_BERSERKER_MINIBOSS"
                    name="Defeat any Warrior or Brave"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_KEEPER_BESTIARY_BERSERKER_BOSS"
                    name="Defeat any Patriarch or Chieftain"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_KEEPER_BESTIARY_HUNTRESS"
                    name="Defeat 50 Huntress, Knifelings, or Axe-Throwers"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_KEEPER_BESTIARY_HUNTRESS_MINIBOSS"
                    name="Defeat any Pack Leader or Axe-Maiden"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_KEEPER_BESTIARY_HUNTRESS_BOSS"
                    name="Defeat any Axe-Maiden"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_KEEPER_BESTIARY_GIANT"
                    name="Defeat 75 Giants"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_KEEPER_BESTIARY_GIANT_MINIBOSS"
                    name="Defeat any Athos, Graybeard, or Hulk"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_KEEPER_BESTIARY_GIANT_BOSS"
                    name="Defeat any Ancient Athos, Ancient, or Mountain"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_KEEPER_BESTIARY_DRUID"
                    name="Defeat 75 Druids, Sharpeyes, Stormbringers, or Adepts"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_KEEPER_BESTIARY_DRUID_MINIBOSS"
                    name="Defeat any Elder or Sage"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_KEEPER_BESTIARY_DRUID_BOSS"
                    name="Defeat any Elder, Evoker, Savant, or Archdruid"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_KEEPER_BESTIARY_BEAR"
                    name="Defeat 150 Keeper Bears"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_KEEPER_BESTIARY_MUSHROOM_CULTIVATOR"
                    name="Defeat 50 Cultivators"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_KEEPER_BESTIARY_WITCH"
                    name="Defeat any Shaman"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_KEEPER_BESTIARY_EARTHCHILD"
                    name="Defeat 50 Earthchilds or Shamans"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_KEEPER_KILL_EARTHDAUGHTER"
                    name="Defeat any Earthdaughter"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_KEEPER_KILL_EARTHMOTHER"
                    name="Defeat any Earthmother, Earth Aspirant, or Great Mother"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_KEEPER_KILL_100"
                    name="Defeat 100 Keepers"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_KEEPER_KILL_300"
                    name="Defeat 300 Keepers"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="SA_PVE_KILL_KEEPER"
                    name="Defeat 1,000 Keepers"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_KEEPER_KILL_3000"
                    name="Defeat 3,000 Keepers"
                    id="T4_CAPEITEM_KEEPER_BP"
                    title="Adept's Keeper Crest"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_KEEPER_KILL_10000"
                    name="Defeat 10,000 Keepers"
                    id="T6_CAPEITEM_KEEPER_BP"
                    title="Master's Keeper Crest"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_KEEPER_KILL_50000"
                    name="Defeat 50,000 Keepers"
                    id="T8_CAPEITEM_KEEPER_BP"
                    title="Elder's Keeper Crest"
                  />
                </tbody>
              </Table>

              <h4>Disciples of Morgana (28)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="JOURNAL_CREATURES_MORGANA_BESTIARY_BAT"
                    name="Defeat 100 Bats"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_MORGANA_BESTIARY_BLOODHOUND"
                    name="Defeat 150 Guard Dogs or White Hounds"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_MORGANA_BESTIARY_TOME"
                    name="Defeat 125 Tomes"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_MORGANA_BESTIARY_SOLDIER"
                    name="Defeat 50 Pikemen or Footmen"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_MORGANA_BESTIARY_SOLDIER_MINIBOSS"
                    name="Defeat any Lieutenants or Enforcers"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_MORGANA_BESTIARY_SOLDIER_BOSS"
                    name="Defeat any Commander of the Guard"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_MORGANA_BESTIARY_CROSSBOWMAN"
                    name="Defeat 100 Squires or Suppressors"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_MORGANA_BESTIARY_CROSSBOWMAN_MINIBOSS"
                    name="Defeat any Marksman or Suppression Squad Leader"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_MORGANA_BESTIARY_CROSSBOWMAN_BOSS"
                    name="Defeat any Master of Suppression"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_MORGANA_BESTIARY_CULTIST"
                    name="Defeat 100 Acolytes or Occultists"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_MORGANA_BESTIARY_CULTIST_MINIBOSS"
                    name="Defeat any Ritual Leader or Aspirant"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_MORGANA_BESTIARY_CULTIST_BOSS"
                    name="Defeat any Magistra, Raven, Fang, Prioress, or Mistress of Demons"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_MORGANA_BESTIARY_KNIGHT"
                    name="Defeat 50 Knights, Paladins, or Champions"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_MORGANA_BESTIARY_KNIGHT_BOSS"
                    name="Defeat any Honoured, Chosen, or Archfiend"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_MORGANA_BESTIARY_BOMBADIER"
                    name="Defeat 75 Conjurers"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_MORGANA_BESTIARY_INFESTOR"
                    name="Defeat 75 Sorceresses or Infestors"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_MORGANA_BESTIARY_INFESTOR_MINIBOSS"
                    name="Defeat any Favored Sorceress"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_MORGANA_BESTIARY_INFESTOR_BOSS"
                    name="Defeat any Mistress of Magic"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_MORGANA_BESTIARY_RAVEN"
                    name="Defeat 30 Ravens"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_MORGANA_BESTIARY_DEMONS"
                    name="Defeat 50 Molten Demons or Spiked Demons"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_MORGANA_BESTIARY_TORTURER_BOSS"
                    name="Defeat any Tormentor or Jailer"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_MORGANA_KILL_DEMON_PRINCE"
                    name="Defeat any Demon Prince, Prince of Morgana, or Demon General"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_MORGANA_KILL_100"
                    name="Defeat 100 Disciples of Morgana"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_MORGANA_KILL_300"
                    name="Defeat 300 Disciples of Morgana"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="SA_PVE_KILL_MORGANA"
                    name="Defeat 1,000 Disciples of Morgana"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_MORGANA_KILL_3000"
                    name="Defeatl 3,000 Disciples of Morgana"
                    id="T4_CAPEITEM_MORGANA_BP"
                    title="Adept's Morgana Crest"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_MORGANA_KILL_10000"
                    name="Defeat 10,000 Disciples of Morgana"
                    id="T6_CAPEITEM_MORGANA_BP"
                    title="Master's Morgana Crest"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_MORGANA_KILL_50000"
                    name="Defeat 50,000 Disciples of Morgana"
                    id="T8_CAPEITEM_MORGANA_BP"
                    title="Elder's Morgana Crest"
                  />
                </tbody>
              </Table>

              <h4>Demons (20)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="JOURNAL_CREATURES_DEMON_BESTIARY_IMP"
                    name="Defeat 50 Imps"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_DEMON_BESTIARY_SPIKED_DEMON"
                    name="Defeat 25 Spiked Demons"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_DEMON_BESTIARY_HOOK"
                    name="Defeat 10 Slavers"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_DEMON_BESTIARY_MAULER"
                    name="Defeat 50 Maulers"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_DEMON_BESTIARY_SORCERER"
                    name="Defeat 25 Sorcerers"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_DEMON_BESTIARY_SORCERER_BOSS"
                    name="Defeat any Warlock"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_DEMON_BESTIARY_BRUTE"
                    name="Defeat 25 Berserkers"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_DEMON_BESTIARY_BRUTE_BOSS"
                    name="Defeat any Harbinger"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_DEMON_BESTIARY_CHAINED_MINIBOSS"
                    name="Defeat any Horror or Trapped Demon"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_DEMON_BESTIARY_UNDERLORD_MINIBOSS"
                    name="Defeat any Underlord"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_DEMON_BESTIARY_DEMONIC_HER_THIEF"
                    name="Defeat 75 Demented Heretic Thieves"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_DEMON_BESTIARY_DEMONIC_HER_MAGE"
                    name="Defeat 100 Enthralled Heretic Mages"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_DEMON_BESTIARY_DEMONIC_HER_DUALXBOW"
                    name="Defeat 125 Deranged Heretic Arbalists"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_DEMON_BESTIARY_DEMONIC_HER_BRAWLER"
                    name="Defeat 150 Bewildered Heretic Brawlers"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="SA_PVE_CORRUPTED_DUNGEONS_02"
                    name="Defeat 100 Demons"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_DEMON_KILL_300"
                    name="Defeat 300 Demons"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="SA_PVE_CORRUPTED_DUNGEONS_03"
                    name="Defeat 1,000 Demons"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_DEMON_KILL_3000"
                    name="Defeat 3,000 Demons"
                    id="T4_CAPEITEM_DEMON_BP"
                    title="Adept's Demon Crest"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_DEMON_KILL_10000"
                    name="Defeat 10,000 Demons"
                    id="T6_CAPEITEM_DEMON_BP"
                    title="Master's Demon Crest"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_DEMON_KILL_50000"
                    name="Defeat 50,000 Demons"
                    id="T8_CAPEITEM_DEMON_BP"
                    title="Elder's Demon Crest"
                  />
                </tbody>
              </Table>

              <h4>Avalonians (28)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="JOURNAL_CREATURES_AVALON_BESTIARY_DRONES"
                    name="Defeat 250 Drones"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_AVALON_BESTIARY_STATUE"
                    name="Defeat 15 Assemblers"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_AVALON_BESTIARY_MORTAR"
                    name="Defeat 15 Foci"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_AVALON_BESTIARY_WINGED_GUARD"
                    name="Defeat 15 Winged Guards"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_AVALON_BESTIARY_PIKEMAN"
                    name="Defeat 100 Lancers or Spearmen"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_AVALON_BESTIARY_MONK"
                    name="Defeat 50 Initiates or Monks"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_AVALON_BESTIARY_ARCHER"
                    name="Defeat 20 Hunters or Rangers"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_AVALON_BESTIARY_ARCHER_BOSS"
                    name="Defeat any Archer"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_AVALON_BESTIARY_WIZARD"
                    name="Defeat 50 Wizards or Magi"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_AVALON_BESTIARY_CLERIC"
                    name="Defeat 50 Acolytes"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_AVALON_BESTIARY_PRIESTESS"
                    name="Defeat 15 Priestess"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_AVALON_BESTIARY_PRIESTESS_BOSS"
                    name="Defeat any High Priestess"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_AVALON_BESTIARY_MAGE"
                    name="Defeat 50 Mages, Keen Mages, or Spellweavers"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_AVALON_BESTIARY_MAGE_MINIBOSS"
                    name="Defeat any Great Mage or Spellweaver"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_AVALON_BESTIARY_MAGE_BOSS"
                    name="Defeat any Great Mage or Archmage"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_AVALON_BESTIARY_BERSERKER"
                    name="Defeat 25 Warriors"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_AVALON_BESTIARY_KNIGHT"
                    name="Defeat 15 Knights"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_AVALON_BESTIARY_CONSTRUCT_BOSS"
                    name="Defeat any Construct"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_AVALON_BESTIARY_BASILISK_BOSS"
                    name="Defeat any Crystal Basilisk"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_AVALON_BESTIARY_CAPTAIN_BOSS"
                    name="Defeat any Knight Captain"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    entryID="SA_PVE_KILL_RD_ELITE_02"
                    name="Defeat Sir Bedivere"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_AVALON_KILL_TREASURE_DRONE"
                    name="Defeat any Treasure Drone"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_AVALONIAN_KILL_100"
                    name="Defeat 100 Avalonians"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    entryID="SA_PVE_ROADS_AVALON"
                    name="Defeat 250 Avalonians"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_AVALONIAN_KILL_1000"
                    name="Defeat 1,000 Avalonians"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_AVALONIAN_KILL_2500"
                    name="Defeat 2,500 Avalonians"
                    id="T4_CAPEITEM_AVALON_BP"
                    title="Adept's Avalonian Crest"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_AVALONIAN_KILL_10000"
                    name="Defeat 10,000 Avalonians"
                    id="T6_CAPEITEM_AVALON_BP"
                    title="Master's Avalonian Crest"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_AVALONIAN_KILL_50000"
                    name="Defeat 50,000 Avalonians"
                    id="T8_CAPEITEM_AVALON_BP"
                    title="Elder's Avalonian Crest"
                  />
                </tbody>
              </Table>

              <h4>Rare Encounters (20)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    entryID="JOURNAL_CREATURES_RARE_CREATURES_BESTIARY_PANTHER"
                    name="Defeat any Shadow Panther"
                    id="T3_ALCHEMY_RARE_PANTHER"
                    title="Rugged Shadow Claws (x2)"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_RARE_CREATURES_BESTIARY_ENT"
                    name="Defeat any Sylvian"
                    id="T3_ALCHEMY_RARE_ENT"
                    title="Rugged Sylvian Root (x2)"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_RARE_CREATURES_BESTIARY_BEAR"
                    name="Defeat any Spirit Bear"
                    id="T3_ALCHEMY_RARE_DIREBEAR"
                    title="Rugged Spirit Paws (x2)"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_RARE_CREATURES_BESTIARY_WEREWOLF"
                    name="Defeat any Werewolf"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_RARE_CREATURES_BESTIARY_IMP"
                    name="Defeat any Hellfire Imp"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_RARE_CREATURES_BESTIARY_GOLEM"
                    name="Defeat any Runestone Golem"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_RARE_CREATURES_BESTIARY_EAGLE"
                    name="Defeat any Dawnbird"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_RARE_CREATURES_BESTIARY_CRYSTAL_SPIDER"
                    name="Defeat any Crystal Spider"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_RARE_CREATURES_BESTIARY_CRYSTAL_BEETLE"
                    name="Defeat any Crystal Beetle"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_RARE_CREATURES_BESTIARY_CRYSTAL_COBRA"
                    name="Defeat any Crystal Cobra"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_RARE_CREATURES_BESTIARY_MIST_SPIDERLING"
                    name="Defeat 5 Arcane Spiderlings"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_RARE_CREATURES_BESTIARY_MIST_SPIDER"
                    name="Defeat any Veilweaver"
                    id="T4_ARTEFACT_ARMOR_PLATE_FEY"
                    title="Adept's Veilweaver Carapace"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_RARE_CREATURES_BESTIARY_MIST_GRIFFIN"
                    name="Defeat any Griffin"
                    id="T4_ARTEFACT_ARMOR_LEATHER_FEY"
                    title="Adept's Untarnished Griffin Feathers"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_RARE_CREATURES_BESTIARY_MIST_FAIRYDRAGON"
                    name="Defeat any Fey Dragon"
                    id="T4_ARTEFACT_ARMOR_CLOTH_FEY"
                    title="Adept's Fey Dorsal Wing"
                  />
                  <Entry
                    entryID="SA_PVE_RD_STATUES_SOLO"
                    name="Kill any Colossus in a Randomized Dungeon"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    entryID="SA_PVE_RD_STATUES_GROUP"
                    name="Kill any Titan in a Randomized Dungeon"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_RARE_CREATURES_BESTIARY_ARCANE_ELEMENTAL"
                    name="Defeat 10 Vengeful Guardians"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_RARE_CREATURES_BESTIARY_ARCANE_ELEMENTAL_BOSS"
                    name="Defeat any Vengeful Guardian Lord"
                    id="T5_LEARNINGPOINTS_NONTRADABLE"
                    title="Expert's Tome of Learning"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_RARE_CREATURES_BESTIARY_EVENT_UNCLE_FROST"
                    name="Defeat Uncle Frost"
                    id="UNIQUE_FURNITUREITEM_XMAS_PRESENT"
                    title="Present Box"
                  />
                  <Entry
                    entryID="JOURNAL_CREATURES_RARE_CREATURES_BESTIARY_EVENT_BOB"
                    name="Defeat Bob"
                    id="T3_VANITY_CONSUMABLE_FIREWORKS_RED_NONTRADABLE"
                    title="Royal Red Fireworks (x10)"
                  />
                </tbody>
              </Table>
            </AccordionBody>
          </AccordionItem>
        </UncontrolledAccordion>
      </Section>
    </JournalProvider>
  );
};
```
