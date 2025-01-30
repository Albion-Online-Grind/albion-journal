```tsx
const Journal = ({ reward }: { reward: string }) => {
  return (
    <div>
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
                    reward={reward}
                    name="Finish a T3 Solo Expedition"
                    id="T3_SILVERBAG_NONTRADABLE"
                    title="Journeyman's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Finish a Tier 4 Solo Expedition"
                    id="T4_SILVERBAG_NONTRADABLE"
                    title="Adept's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Finish a Tier 4 Group Expedition"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Finish a Tier 5 Solo Expedition"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Finish a Tier 5 Group Expedition"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Finish a Tier 6 Group Expedition"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Finish a T5 Solo Expedition within 7 minutes"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Finish a T6 Group Expedition within 10 minutes"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Finish a T5 Solo Expedition within 5 minutes"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Finish any Hardcore Expedition"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Finish a Level 4 Hardcore Expedition"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Finish a Level 8 Hardcore Expedition"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Finish a Level 12 Hardcore Expedition"
                    id="UNIQUE_REPAIRPOWDER_ADC_GENERAL_01_NONTRADEABLE"
                    title="Scroll of Repair"
                  />
                  <Entry
                    reward={reward}
                    name="Finish a Level 18 Hardcore Expedition"
                    id="UNIQUE_REPAIRPOWDER_ADC_GENERAL_01_NONTRADEABLE"
                    title="Scroll of Repair"
                  />
                  <Entry
                    reward={reward}
                    name="Finish a Level 18 Hardcore Expedition within 10 minutes"
                    id="UNIQUE_REPAIRPOWDER_ADC_GENERAL_01_NONTRADEABLE"
                    title="Scroll of Repair (x2)"
                  />
                  <Entry
                    reward={reward}
                    name="Finish 5 different Level 18 Hardcore Expeditions"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x5)"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Finish a T3 Solo Dungeon"
                    id="T1_MEAL_SOUP"
                    title="Carrot Soup"
                  />
                  <Entry
                    reward={reward}
                    name="Finish a Tier 4 Solo Dungeon"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Finish a Solo Dungeon of every Faction"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Unlock 10 chests in Solo Dungeons"
                    id="T5_RANDOM_DUNGEON_SOLO_TOKEN_1"
                    title="Expert's Dungeon Map (Solo)"
                  />
                  <Entry
                    reward={reward}
                    name="Finish a Tier 5 Solo Dungeon"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Finish 3 Solo Dungeons with a Map"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Finish an enchanted Solo Dungeon without using a map"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Unlock 30 chests in Solo Dungeons"
                    id="T4_RANDOM_DUNGEON_TOKEN_1"
                    title="Adept's Dungeon Map (Group)"
                  />
                  <Entry
                    reward={reward}
                    name="Finish an Enchantment Level 2 Solo Dungeon"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Finish an Enchantment Level 3 Solo Dungeon"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Finish a Tier 6 Solo Dungeon"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat a T5 boss with T3 equipment on your own"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Finish an Enchantment Level 4 Solo Dungeon"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Use 30 combat buff shrines in Solo Dungeons"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Finish a Tier 7 Solo Dungeon"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Finish a Tier 8 Solo Dungeon"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Finish a Tier 8.4 Solo Dungeon"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Unlock 100 chests in Solo Dungeons"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat a T6 boss with T3 equipment on your own"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat a T7 boss with T3 equipment on your own"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat a T8 boss with T3 equipment on your own"
                    id="T5_LEARNINGPOINTS_NONTRADABLE"
                    title="Expert's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Finish 30 Solo Dungeons"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver (x4)"
                  />
                  <Entry
                    reward={reward}
                    name="Finish 100 Solo Dungeons"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver (x7)"
                  />
                  <Entry
                    reward={reward}
                    name="Finish 300 Solo Dungeons"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x9)"
                  />
                  <Entry
                    reward={reward}
                    name="Finish 600 Solo Dungeons"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x12)"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Defeat 12 T3 Roaming Mobs"
                    id="T3_SILVERBAG_NONTRADABLE"
                    title="Journeyman's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 50 T4 Roaming Mobs"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 3 mobs with your mount standing next to you"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 4 Roaming Mobs within 10 seconds"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat a Roaming Mob with any armor slot ability"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 80 T5 Roaming Mobs"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 10 Roaming Mobs within 30 seconds"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 50 mobs while flagged for Faction Warfare"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 8 Roaming Mobs within 10 seconds"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 5 Roaming Mobs in a Red Zone"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 120 T6 Roaming Mobs"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 200 T7 Roaming Mobs"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 1,000 Roaming Mobs in a Black Zone"
                    id="T5_LEARNINGPOINTS_NONTRADABLE"
                    title="Expert's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 300 T8 Roaming Mobs"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 30 Roaming Mob Champions"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 100 Roaming Mob Champions"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 300 Roaming Mob Champions"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 1,000 Roaming Mob Champions"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 3,000 Roaming Mob Champions"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 10 Roaming Mob Mini Bosses"
                    id="UNIQUE_FURNITUREITEM_ADC_ICESCULPTURE_C"
                    title="Ice Sculpture: Obsessed Cultist"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 30 Roaming Mob Mini Bosses"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 100 Roaming Mob Mini Bosses"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 300 Roaming Mob Mini Bosses"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 3 Roaming Mob Bosses"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 10 Roaming Mob Bosses"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 30 Roaming Mob Bosses"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 100 Roaming Mob Bosses"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x10)"
                  />
                  <Entry
                    reward={reward}
                    name="Gain 100,000 Fame from Roaming Mobs"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Gain 300,000 Fame from Roaming Mobs"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Gain a million Fame from Roaming Mobs"
                    id="T5_LEARNINGPOINTS_NONTRADABLE"
                    title="Expert's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Gain 3 million Fame from Roaming Mobs"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Gain 10 million Fame from Roaming Mobs"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Gain 30 million Fame from Roaming Mobs"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x50)"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Defeat 20 mobs in a T3 Static Dungeon"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 50 mobs in a T4 Static Dungeon"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 100 mobs in a T5 Static Dungeon"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 150 mobs in a T6 Static Dungeon"
                    id="T3_POTION_MOB_RESET"
                    title="Minor Calming Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 200 mobs in a T7 Static Dungeon"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 300 mobs in a T8 Static Dungeon"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Participate in a Static Dungeon Event"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Gain 100,000 Fame during a Static Dungeon rally"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Gain 10,000 Fame in Static Dungeons"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Gain 100,000 Fame in Static Dungeons"
                    id="UNIQUE_UNLOCK_SKIN_HORSE_BROWN_NON_TRADABLE"
                    title="Riding Horse Skin: Brown Mare"
                  />
                  <Entry
                    reward={reward}
                    name="Gain a million Fame in Static Dungeons"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Gain 10 million Fame in Static Dungeons"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Gain 30 million Fame in Static Dungeons"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x10)"
                  />
                  <Entry
                    reward={reward}
                    name="Gain 100 million Fame in Static Dungeons"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x15)"
                  />
                  <Entry
                    reward={reward}
                    name="Kill 100 Champions in Static Dungeons"
                    id="UNIQUE_FURNITUREITEM_ADC_ICESCULPTURE_B"
                    title="Ice Sculpture: Cursed Archer"
                  />
                  <Entry
                    reward={reward}
                    name="Kill 300 Champions in Static Dungeons"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Kill 1,000 Champions in Static Dungeons"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Kill 30 Mini Bosses in Static Dungeons"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Kill 100 Mini Bosses in Static Dungeons"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Kill 300 Mini Bosses in Static Dungeons"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x10)"
                  />
                  <Entry
                    reward={reward}
                    name="Kill 10 Bosses in Static Dungeons"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Kill 30 Bosses in Static Dungeons"
                    id="T5_LEARNINGPOINTS_NONTRADABLE"
                    title="Expert's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Unlock an open world Small Camp Cache in a Yellow Zone"
                    id="T4_SILVERBAG_NONTRADABLE"
                    title="Adept's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Interact with a Lair Map in an Encampment"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Finish a Boss Lair"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Unlock 10 open world Small Camp Caches in a Yellow Zone"
                    id="T4_SILVERBAG_NONTRADABLE"
                    title="Adept's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Finish 3 Boss Lairs"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Unlock 25 open world Small Camp Caches"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Unlock an open world Group Camp Cache in a Yellow Zone"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Finish a Group Boss Lair"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Unlock 10 open world Group Camp Caches"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Unlock an open world Small Camp Cache from 3 different Factions"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Unlock 50 open world Small Camp Caches"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Finish 15 Boss Lairs"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Unlock a Legendary open world Small Camp Cache"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Unlock 15 open world Group Camp Caches"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Finish 5 Group Boss Lairs"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Unlock an open world Group Camp Cache from 3 different Factions"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Unlock an open world Small Camp Cache in the Outlands"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Finish a Boss Lair in the Outlands"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Unlock 5 open world Small Camp Caches in the Outlands"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Finish a Tier 8 Boss Lair"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Unlock an open world Group Camp Cache in the Outlands"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Finish a Group Boss Lair in the Outlands"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Unlock 5 open world Group Camp Caches in the Outlands"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Clear a Tier 8 Group Boss Lair"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight (x3)"
                  />
                  <Entry
                    reward={reward}
                    name="Unlock 300 open world Small Camp Caches"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Unlock 600 open world Small Camp Caches"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Unlock 1000 open world Small Camp Caches"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight (x2)"
                  />
                  <Entry
                    reward={reward}
                    name="Finish 100 Boss Lairs"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Finish 300 Boss Lairs"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x3)"
                  />
                  <Entry
                    reward={reward}
                    name="Unlock 50 open world Group Camp Caches"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight (x5)"
                  />
                  <Entry
                    reward={reward}
                    name="Unlock 100 open world Group Camp Caches"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x5)"
                  />
                  <Entry
                    reward={reward}
                    name="Unlock 300 open world Group Camp Caches"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight (x10)"
                  />
                  <Entry
                    reward={reward}
                    name="Finish 30 Group Boss Lairs"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Finish a Tier 4 Group Dungeon"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Finish a Tier 5 Group Dungeon"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Finish 2 Enchantment Level 1 Group Dungeons"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Finish 3 Enchantment Level 2 Group Dungeons"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Finish 5 Enchantment Level 3 Group Dungeons"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Finish a Tier 6 Group Dungeon"
                    id="UNIQUE_UNLOCK_HEAD_VANITY_BARD_NON_TRADABLE"
                    title="Wardrobe Skin: Bard's Hat"
                  />
                  <Entry
                    reward={reward}
                    name="Finish a Tier 7 Group Dungeon"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Finish a Tier 8 Group Dungeon"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Finish a Tier 8.4 Group Dungeon"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Kill the legendary Morgana Demon General, Keeper Earth Aspirant, Undead Reaper, and Heretic Shadowmask"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight (x5)"
                  />
                  <Entry
                    reward={reward}
                    name="Unlock 10 chests in Group Dungeons"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Unlock 30 chests in Group Dungeons"
                    id="T6_RANDOM_DUNGEON_ELITE_TOKEN_1"
                    title="Master's Dungeon Map (Large Group)"
                  />
                  <Entry
                    reward={reward}
                    name="Unlock 100 chests in Group Dungeons"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Unlock 500 chests in Group Dungeons"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Finish 10 Group Dungeons"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Finish 30 Group Dungeons"
                    id="T5_LEARNINGPOINTS_NONTRADABLE"
                    title="Expert's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Finish 80 Group Dungeons"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x5)"
                  />
                  <Entry
                    reward={reward}
                    name="Finish 150 Group Dungeons"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x15)"
                  />
                  <Entry
                    reward={reward}
                    name="Finish 300 Group Dungeons"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x20)"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Track down a solo Rare Creature"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Track down a T4 solo Rare Quarry"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Track down 3 types of solo Rare Creature"
                    id="UNIQUE_FURNITUREITEM_KEEPER_SYMBOL_OF_POWER_A"
                    title="Keeper Symbol of Power"
                  />
                  <Entry
                    reward={reward}
                    name="Track down a T5 solo Rare Quarry"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Track down 4 types of solo Rare Creature"
                    id="T4_ARTEFACT_2H_SHAPESHIFTER_MORGANA"
                    title="Adept's Werewolf Remnant"
                  />
                  <Entry
                    reward={reward}
                    name="Track down a T6 solo Rare Quarry"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Track down 5 types of solo Rare Creature"
                    id="T4_ARTEFACT_2H_SHAPESHIFTER_HELL"
                    title="Adept's Hellfire Imp Remnant"
                  />
                  <Entry
                    reward={reward}
                    name="Finish a hunt at the first encounter"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Track down 6 types of solo Rare Creature"
                    id="T4_ARTEFACT_2H_SHAPESHIFTER_KEEPER"
                    title="Adept's Runestone Golem Remnant"
                  />
                  <Entry
                    reward={reward}
                    name="Track down a T7 solo Rare Quarry"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Track down a T8 solo Rare Quarry"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Track down a group Rare Creature"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Track down 3 types of group Rare Creature"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Track down 5 types of group Rare Creature"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Track down a T8 group Rare Quarry"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Finish a solo Rare Creature hunt in 4 minutes"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Finish a solo Dawnbird hunt in 10 minutes"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Finish a group Rare Creature hunt in 4 minutes"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Finish a group Dawnbird hunt in 10 minutes"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Finish 10 hunts"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Finish 20 hunts"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Finish 40 hunts"
                    id="T5_LEARNINGPOINTS_NONTRADABLE"
                    title="Expert's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Finish 80 hunts"
                    id="UNIQUE_UNLOCK_ARMOR_VANITY_PIRATE_GREEN_NON_TRADABLE"
                    title="Wardrobe Skin: Green Navigator's Coat"
                  />
                  <Entry
                    reward={reward}
                    name="Finish 200 hunts"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x8)"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Defeat 10 Elite mobs in a World Boss Area"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 50 Elite mobs in a World Boss Area"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat a Mini Boss in a World Boss Area"
                    id="UNIQUE_FURNITUREITEM_MORGANA_STATUE_A"
                    title="Morgana Cultist Statue"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 5 Mini Bosses in a World Boss Area"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat a Boss in a World Boss Area"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat the Earth Mother"
                    id="T5_LEARNINGPOINTS_NONTRADABLE"
                    title="Expert's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 20 Mini Bosses in a World Boss Area"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 5 Bosses in World Boss Areas"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat the Harvester"
                    id="T5_LEARNINGPOINTS_NONTRADABLE"
                    title="Expert's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 50 Mini Bosses in World Boss Areas"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 20 Bosses in World Boss Areas"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat the Demon Prince"
                    id="T5_LEARNINGPOINTS_NONTRADABLE"
                    title="Expert's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 1,000 Elite mobs in a World Boss Area"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x5)"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat a T8 World Boss"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
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
                    reward={reward}
                    name="Defeat 200 Mini Bosses in World Boss Areas"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x10)"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 50 Bosses in World Boss Areas"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x5)"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 10 World Bosses"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x10)"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Finish a T6 Avalonian Dungeon"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Receive the Ascension buff at the end of an Avalonian Dungeon"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Finish a T7 Avalonian Dungeon"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat Sir Bedivere with the Ascension buff active"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Finish a T8 Avalonian Dungeon"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight (x6)"
                  />
                  <Entry
                    reward={reward}
                    name="Finish a T8.1 Avalonian Dungeon"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight (x7)"
                  />
                  <Entry
                    reward={reward}
                    name="Finish a T8.2 Avalonian Dungeon"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight (x8)"
                  />
                  <Entry
                    reward={reward}
                    name="Finish a T8.3 Avalonian Dungeon"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight (x9)"
                  />
                  <Entry
                    reward={reward}
                    name="Finish a T8.4 Avalonian Dungeon"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight (x10)"
                  />
                  <Entry
                    reward={reward}
                    name="Finish 5 Avalonian Dungeons"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x10)"
                  />
                  <Entry
                    reward={reward}
                    name="Finish 10 Avalonian Dungeons"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x12)"
                  />
                  <Entry
                    reward={reward}
                    name="Finish 20 Avalonian Dungeons"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x15)"
                  />
                  <Entry
                    reward={reward}
                    name="Finish 40 Avalonian Dungeons"
                    id="T5_LEARNINGPOINTS_NONTRADABLE"
                    title="Expert's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Finish 60 Avalonian Dungeons"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x20)"
                  />
                  <Entry
                    reward={reward}
                    name="Finish 100 Avalonian Dungeons"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x30)"
                  />
                  <Entry
                    reward={reward}
                    name="Unlock 10 chests in Avalonian Dungeons"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Unlock 20 chests in Avalonian Dungeons"
                    id="T5_LEARNINGPOINTS_NONTRADABLE"
                    title="Expert's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Unlock 40 chests in Avalonian Dungeons"
                    id="UNIQUE_UNLOCK_HEAD_VANITY_BARD_BLUE_NON_TRADABLE"
                    title="Wardrobe Skin: Blue Bard's Hat"
                  />
                  <Entry
                    reward={reward}
                    name="Unlock 100 chests in Avalonian Dungeons"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x10)"
                  />
                  <Entry
                    reward={reward}
                    name="Unlock a Legendary Chest in an Avalonian Dungeon"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Unlock 160 chests in Avalonian Dungeons"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x15)"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Buy a weapon at the Marketplace"
                    id="T2_SKILLBOOK_NONTRADABLE"
                    title="Novice's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Buy 5 Equipment Items at the Marketplace"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Spend 10,000 Silver on items at the Marketplace"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Spend 100,000 Silver on items at the Marketplace"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Buy 10 Equipment Items from the Marketplace"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Spend a million Silver on items at the Marketplace"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x10)"
                  />
                  <Entry
                    reward={reward}
                    name="Create a Buy Order"
                    id="T3_VANITY_CONSUMABLE_FIREWORKS_GREEN_NONTRADABLE"
                    title="Royal Green Fireworks (x3)"
                  />
                  <Entry
                    reward={reward}
                    name="Spend 10 million Silver on items at the Marketplace"
                    id="UNIQUE_UNLOCK_SHOES_VANITY_INNKEEPER_NON_TRADABLE"
                    title="Wardrobe Skin: Innkeeper's Shoes"
                  />
                  <Entry
                    reward={reward}
                    name="Spend 100 million Silver on items at the Marketplace"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x20)"
                  />
                  <Entry
                    reward={reward}
                    name="Spend a billion Silver on items at the Marketplace"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x30)"
                  />
                  <Entry
                    reward={reward}
                    name="Buy 30 Equipment Items at the Marketplace"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Buy 100 Equipment Items at the Marketplace"
                    id="T3_VANITY_CONSUMABLE_FIREWORKS_RED_NONTRADABLE"
                    title="Royal Red Fireworks (x3)"
                  />
                  <Entry
                    reward={reward}
                    name="Buy 1,000 Equipment Items at the Marketplace"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x10)"
                  />
                  <Entry
                    reward={reward}
                    name="Buy 10,000 Equipment Items at the Marketplace"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Buy 100,000 Equipment Items at the Marketplace"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Buy 100 Items at the Marketplace"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Buy 1,000 Items at the Marketplace"
                    id="T3_VANITY_CONSUMABLE_FIREWORKS_YELLOW_NONTRADABLE"
                    title="Royal Yellow Fireworks (x3)"
                  />
                  <Entry
                    reward={reward}
                    name="Buy 10,000 Items at the Marketplace"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x10)"
                  />
                  <Entry
                    reward={reward}
                    name="Buy 100,000 Items at the Marketplace"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Buy a million Items at the Marketplace"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Sell any item through the Marketplace"
                    id="T2_SKILLBOOK_NONTRADABLE"
                    title="Novice's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Sell items for 10,000 Silver at the Marketplace"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Sell items worth 100,000 Silver at the Marketplace"
                    id="T3_VANITY_CONSUMABLE_FIREWORKS_GREEN_NONTRADABLE"
                    title="Royal Green Fireworks (x3)"
                  />
                  <Entry
                    reward={reward}
                    name="Sell 10 Luxury Goods directly to their preferred city"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Create a Sell Order"
                    id="T3_VANITY_CONSUMABLE_FIREWORKS_BLUE_NONTRADABLE"
                    title="Royal Blue Fireworks (x3)"
                  />
                  <Entry
                    reward={reward}
                    name="Sell items worth 1,000,000 Silver at the Marketplace"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Create 20 Sell Orders"
                    id="T3_VANITY_CONSUMABLE_FIREWORKS_RED_NONTRADABLE"
                    title="Royal Red Fireworks (x3)"
                  />
                  <Entry
                    reward={reward}
                    name="Sell 1000 Luxury Goods directly to their preferred city"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Sell any item on the Black Market in Caerleon"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Sell items worth 10,000,000 Silver at the Marketplace"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Sell 9999 Luxury Goods directly to their preferred city"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Create a Sell Order on the Black Market"
                    id="T3_VANITY_CONSUMABLE_FIREWORKS_YELLOW_NONTRADABLE"
                    title="Royal Yellow Fireworks (x3)"
                  />
                  <Entry
                    reward={reward}
                    name="Sell items for 100 million Silver at the Marketplace"
                    id="UNIQUE_UNLOCK_HEAD_VANITY_RICH_NOBLE_PURPLE_NON_TRADABLE"
                    title="Wardrobe Skin: Purple Rich Noble's Hat"
                  />
                  <Entry
                    reward={reward}
                    name="Sell items for a billion Silver at the Marketplace"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Earn a million Silver through the Black Market"
                    id="UNIQUE_FURNITUREITEM_KNIGHT_CARPET_A"
                    title="Regal Carpet"
                  />
                  <Entry
                    reward={reward}
                    name="Earn 10 million Silver through the Black Market"
                    id="UNIQUE_UNLOCK_SKIN_OX_BLACKMARKET_NON_TRADABLE"
                    title="Transport Ox Skin: Black Market Ox"
                  />
                  <Entry
                    reward={reward}
                    name="Earn 100 million Silver through the Black Market"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Earn a billion Silver through the Black Market"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x100)"
                  />
                  <Entry
                    reward={reward}
                    name="Directly sell 9999 preferred luxury goods to Fort Sterling"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x15)"
                  />
                  <Entry
                    reward={reward}
                    name="Directly sell 9999 preferred luxury goods to Lymhurst"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x15)"
                  />
                  <Entry
                    reward={reward}
                    name="Directly sell 9999 preferred luxury goods to Bridgewatch"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x15)"
                  />
                  <Entry
                    reward={reward}
                    name="Directly sell 9999 preferred luxury goods to Martlock"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x15)"
                  />
                  <Entry
                    reward={reward}
                    name="Directly sell 9999 preferred luxury goods to Thetford"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x15)"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Refine 30 T2 resources"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Refine 60 T3 resources"
                    id="T3_FOCUSPOTION_NONTRADABLE"
                    title="Journeyman's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Refine 100 T4 resources"
                    id="T4_FOCUSPOTION_NONTRADABLE"
                    title="Adept's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Transmute 10 resources to Uncommon"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Refine 200 T5 resources"
                    id="T5_FOCUSPOTION_NONTRADABLE"
                    title="Expert's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Transmute 20 resources to a higher tier"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Refine 400 T6 resources"
                    id="T6_FOCUSPOTION_NONTRADABLE"
                    title="Master's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Transmute 25 resources to Rare"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Refine 400 T7 resources"
                    id="UNIQUE_FOCUSPOTION_ADC_NONTRADABLE_01"
                    title="Grandmaster's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Transmute 30 resources to Exceptional"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Refine 400 T8 resources"
                    id="T8_FOCUSPOTION_NONTRADABLE"
                    title="Elder's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Transmute 50 resources to Pristine"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Use the Fort Sterling refining bonus"
                    id="T4_FOCUSPOTION_NONTRADABLE"
                    title="Adept's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Use the Lymhurst refining bonus"
                    id="T4_FOCUSPOTION_NONTRADABLE"
                    title="Adept's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Use the Bridgewatch refining bonus"
                    id="T4_FOCUSPOTION_NONTRADABLE"
                    title="Adept's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Use the Martlock refining bonus"
                    id="T4_FOCUSPOTION_NONTRADABLE"
                    title="Adept's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Use the Thetford refining bonus"
                    id="T4_FOCUSPOTION_NONTRADABLE"
                    title="Adept's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Refine 1,000 Resources"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Refine 5,000 Resources"
                    id="T3_FOCUSPOTION_NONTRADABLE"
                    title="Journeyman's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Refine 10,000 Resources"
                    id="T4_FOCUSPOTION_NONTRADABLE"
                    title="Adept's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Refine 50,000 Resources"
                    id="T5_FOCUSPOTION_NONTRADABLE"
                    title="Expert's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Craft 3 T2 Equipment Items"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Craft 10 T3 Equipment Items"
                    id="T3_FOCUSPOTION_NONTRADABLE"
                    title="Journeyman's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Craft an item in a Royal City"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Eat a salad that improves your crafting"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Craft 40 T4 Equipment Items"
                    id="T4_FOCUSPOTION_NONTRADABLE"
                    title="Adept's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Use a city's crafting bonus"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Craft an Outstanding quality Equipment Item"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x10)"
                  />
                  <Entry
                    reward={reward}
                    name="Craft 60 T5 Equipment Items"
                    id="T5_FOCUSPOTION_NONTRADABLE"
                    title="Expert's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Craft 20 Uncommon items"
                    id="UNIQUE_FURNITUREITEM_HERETIC_STOVE_A"
                    title="Heretic Stove"
                  />
                  <Entry
                    reward={reward}
                    name="Craft an Excellent quality Equipment Item"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Craft 80 T6 Equipment Items"
                    id="T6_FOCUSPOTION_NONTRADABLE"
                    title="Master's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Craft 30 Rare items"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Craft a Masterpiece quality Equipment Item"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Craft 100 T7 Equipment Items"
                    id="UNIQUE_FOCUSPOTION_ADC_NONTRADABLE_01"
                    title="Grandmaster's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Craft 50 Epic items"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Use a crafting bonus in a Hideout"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x50)"
                  />
                  <Entry
                    reward={reward}
                    name="Craft 100 T8 Equipment Items"
                    id="T8_FOCUSPOTION_NONTRADABLE"
                    title="Elder's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Craft 50 Pristine items"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Craft a Pristine T8 item"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Craft a Pristine T8 Masterpiece"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x200)"
                  />
                  <Entry
                    reward={reward}
                    name="Craft Items worth 10,000 Fame"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Craft Items worth 100,000 Fame"
                    id="T5_FOCUSPOTION_NONTRADABLE"
                    title="Expert's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Craft items worth a million Fame"
                    id="UNIQUE_FOCUSPOTION_ADC_NONTRADABLE_01"
                    title="Grandmaster's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Craft items worth 10 million Fame"
                    id="UNIQUE_FOCUSPOTION_ADC_NONTRADABLE_01"
                    title="Grandmaster's Focus Restoration Potion (x2)"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Study an item"
                    id="T2_SKILLBOOK_NONTRADABLE"
                    title="Novice's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Salvage an item"
                    id="T2_SKILLBOOK_NONTRADABLE"
                    title="Novice's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Reroll an item at a Repair Station"
                    id="T2_SKILLBOOK_NONTRADABLE"
                    title="Novice's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Meld resources into an Artifact at the Artifact Foundry"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Meld 10 Soul Artifacts"
                    id="UNIQUE_FURNITUREITEM_ADC_GLASS_SPHERE_A"
                    title="Glass Sphere"
                  />
                  <Entry
                    reward={reward}
                    name="Meld 30 T5 Artifacts"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Meld 100 T6 Hunter Artifacts"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Meld 100 T8 Avalonian Artifacts"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x30)"
                  />
                  <Entry
                    reward={reward}
                    name="Create 50 Souls with Transmutation"
                    id="T4_FOCUSPOTION_NONTRADABLE"
                    title="Adept's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Create a T8 Dungeon Map with Transmutation"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Create a Masterpiece item by rerolling it at a Repair Station"
                    id="T4_FOCUSPOTION_NONTRADABLE"
                    title="Adept's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Reroll a full stack of 999 items at a Repair Station"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Salvage 100 items"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Salvage 1,000 items"
                    id="UNIQUE_FURNITUREITEM_ADC_CARNIVAL_ARCHWAY_A"
                    title="Carnival Arch"
                  />
                  <Entry
                    reward={reward}
                    name="Salvage 10,000 items"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Study 100 items"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Study 1,000 items"
                    id="T4_FOCUSPOTION_NONTRADABLE"
                    title="Adept's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Study 10,000 items"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Reroll 100 items"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Reroll 1,000 items"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Reroll 10,000 items"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Own 100,000 Silver"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Own 500,000 Silver"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x10)"
                  />
                  <Entry
                    reward={reward}
                    name="Own 5 Gold"
                    id="T3_VANITY_CONSUMABLE_FIREWORKS_YELLOW_NONTRADABLE"
                    title="Royal Yellow Fireworks (x3)"
                  />
                  <Entry
                    reward={reward}
                    name="Own 1 million Silver"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Own 5 million Silver"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Own 10 million Silver"
                    id="UNIQUE_UNLOCK_HEAD_VANITY_DRESS_BLUE_NON_TRADABLE"
                    title="Wardrobe Skin: Blue Princess Hat"
                  />
                  <Entry
                    reward={reward}
                    name="Own 50 million Silver"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Own 100 million Silver"
                    id="UNIQUE_UNLOCK_ARMOR_VANITY_DRESS_BLUE_NON_TRADABLE"
                    title="Wardrobe Skin: Blue Princess Dress"
                  />
                  <Entry
                    reward={reward}
                    name="Own 500 million Silver"
                    id="UNIQUE_UNLOCK_SKIN_OX_BISON_AH_NON_TRADABLE"
                    title="Transport Ox Skin: Auction House Ox"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Bid at least 1 million Silver on a city plot"
                    id="UNIQUE_FURNITUREITEM_MORGANA_CARPET_A"
                    title="Morgana Carpet"
                  />
                  <Entry
                    reward={reward}
                    name="Own a city plot"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Collect 1 million Silver from city plots"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Bid 5 million Silver on a city plot you currently own"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Collect 3 million Silver from City Plots"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Own 3 plots in the same city simultaneously"
                    id="UNIQUE_UNLOCK_CAPE_VANITY_SNOWLEOPARD_NON_TRADABLE"
                    title="Wardrobe Skin: Snow Leopard Cape"
                  />
                  <Entry
                    reward={reward}
                    name="Collect 10 million Silver from city plots"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Collect 30 million Silver from City Plots"
                    id="T6_FOCUSPOTION_NONTRADABLE"
                    title="Master's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Own 5 plots in the same city simultaneously"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Collect 100 million Silver from city plots"
                    id="T5_LEARNINGPOINTS_NONTRADABLE"
                    title="Expert's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Collect 300 million Silver from City Plots"
                    id="UNIQUE_FOCUSPOTION_ADC_NONTRADABLE_01"
                    title="Grandmaster's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Gather 80 Tier 2 resources"
                    id="T3_SILVERBAG_NONTRADABLE"
                    title="Journeyman's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Gather 120 Tier 3 resources"
                    id="T4_SILVERBAG_NONTRADABLE"
                    title="Adept's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Gather resources worth 1500 Fame"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Gather 100 Tier 4 resources"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Gather 10 resources with Enchantment Level 1"
                    id="T4_SKILLBOOK_GATHER_FIBER_NONTRADABLE"
                    title="Adept Fiber Harvester Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Gather 150 Tier 5 resources"
                    id="T4_SKILLBOOK_GATHER_ROCK_NONTRADABLE"
                    title="Adept Quarrier Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Gather 10 resources with Enchantment Level 2"
                    id="T4_SKILLBOOK_GATHER_WOOD_NONTRADABLE"
                    title="Adept Lumberjack Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Gather a resource from a Plentiful Resource Node"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Gather 10 resources with Enchantment Level 3"
                    id="T5_SKILLBOOK_GATHER_ORE_NONTRADABLE"
                    title="Expert Ore Miner Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Gather 200 Tier 6 resources"
                    id="T5_SKILLBOOK_GATHER_WOOD_NONTRADABLE"
                    title="Expert Lumberjack Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Gather 100 resources from Plentiful Resource Nodes"
                    id="T5_SKILLBOOK_GATHER_ROCK_NONTRADABLE"
                    title="Expert Quarrier Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Gather 300 enchanted resources"
                    id="UNIQUE_UNLOCK_ARMOR_VANITY_PRIEST_NON_TRADABLE"
                    title="Wardrobe Skin: Monk's Robe"
                  />
                  <Entry
                    reward={reward}
                    name="Gather 500 resources from Plentiful Resource Nodes"
                    id="T6_SKILLBOOK_GATHER_WOOD_NONTRADABLE"
                    title="Master Lumberjack Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Gather any resource at an enemy Territory"
                    id="T6_SKILLBOOK_GATHER_ORE_NONTRADABLE"
                    title="Master Ore Miner Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Gather 750 enchanted resources"
                    id="T6_SKILLBOOK_GATHER_FIBER_NONTRADABLE"
                    title="Master Fiber Harvester Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Gather 200 Tier 7 resources"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Gather 1,000 resources from Plentiful Resource Nodes"
                    id="T7_SKILLBOOK_GATHER_ROCK_NONTRADABLE"
                    title="Grandmaster Quarrier Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Gather 50 resources at an enemy Territory"
                    id="T7_SKILLBOOK_GATHER_FIBER_NONTRADABLE"
                    title="Grandmaster Fiber Harvester Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Gather 1,500 enchanted resources"
                    id="T7_SKILLBOOK_GATHER_ORE_NONTRADABLE"
                    title="Grandmaster Ore Miner Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Gather any Tier 8 resource"
                    id="T5_LEARNINGPOINTS_NONTRADABLE"
                    title="Expert's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Gather a resource with maximum Gather Bonus"
                    id="T8_SKILLBOOK_GATHER_ORE_NONTRADABLE"
                    title="Elder Ore Miner Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Gather 200 Tier 8 resources"
                    id="T8_SKILLBOOK_GATHER_WOOD_NONTRADABLE"
                    title="Elder Lumberjack Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Gather 30 resources with Enchantment Level 4"
                    id="T8_SKILLBOOK_GATHER_ROCK_NONTRADABLE"
                    title="Elder Quarrier Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Gather resources worth 10,000 Fame"
                    id="T4_SKILLBOOK_GATHER_ORE_NONTRADABLE"
                    title="Adept Ore Miner Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Gather resources worth 25,000 Fame"
                    id="T5_SKILLBOOK_GATHER_FIBER_NONTRADABLE"
                    title="Expert Fiber Harvester Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Gather resources worth 50,000 Fame"
                    id="T6_SKILLBOOK_GATHER_ROCK_NONTRADABLE"
                    title="Master Quarrier Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Gather resources worth 100,000 Fame"
                    id="T7_SKILLBOOK_GATHER_WOOD_NONTRADABLE"
                    title="Grandmaster Lumberjack Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Gather resources worth 250,000 Fame"
                    id="T8_SKILLBOOK_GATHER_FIBER_NONTRADABLE"
                    title="Elder Fiber Harvester Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Gather resources worth 500,000 Fame"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Gather resources worth a million Fame"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x2)"
                  />
                  <Entry
                    reward={reward}
                    name="Gather resources worth 3 million Fame"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x3)"
                  />
                  <Entry
                    reward={reward}
                    name="Gather resources worth 10 million Fame"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x5)"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Skin 3 types of Hide Animal"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Skin 6 types of Hide Animal"
                    id="T4_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                    title="Adept Animal Skinner Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Skin 10 types of Hide Animal"
                    id="T5_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                    title="Expert Animal Skinner Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Skin 15 types of Hide Animal"
                    id="UNIQUE_UNLOCK_HEAD_VANITY_INNKEEPER_NON_TRADABLE"
                    title="Wardrobe Skin: Innkeeper's Hat"
                  />
                  <Entry
                    reward={reward}
                    name="Skin 22 types of Hide Animal"
                    id="T6_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                    title="Master Animal Skinner Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Skin 30 types of Hide Animal"
                    id="T7_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                    title="Grandmaster Animal Skinner Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Skin 40 types of Hide Animal"
                    id="T8_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                    title="Elder Animal Skinner Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Skin 52 types of Hide Animal"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Skin 65 types of Hide Animal"
                    id="UNIQUE_FOCUSPOTION_ADC_NONTRADABLE_01"
                    title="Grandmaster's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name={
                      <>
                        Skin every type of Hide Animal
                        <br />
                        <span className="text-muted">
                          Bear, Boar, Wolf, Direwolf, Fox, Rabbit, Hill Marmot,
                          Wolpertinger, Snow Rabbit, Marmot, Toad, Fey Fox,
                          Impala, Snake, Cougar, Foglands Doe, Moabird, Giant
                          Toad, Mistcougar Runt, Old Mistcougar Runt, Foglands
                          Hart, Giant Stag, Monitor Lizard, Rare Boar, Rare
                          Giant Stag, Rare Monitor Lizard, Grand Foglands Hart,
                          Sabretooth Tiger, Small Mistcougar, Ancient Small
                          Mistcougar, Old Small Mistcougar, Great Mystic Owl,
                          Terrorbird, Giant Snake, Rare Bear, Rare Giant Snake,
                          Majestic Mystic Owl, Rare Terrorbird, Mistcougar,
                          Ancient Mistcougar, Old Mistcougar, Ancient Basilisk,
                          Old White, Moose, Feral Wolfhound, Hyena, Swamp
                          Dragon, Old Basilisk Aspect, Old White&apos;s Aspect,
                          Rare Hyena, Rare Direwolf, Rare Swamp Dragon,
                          Insatiable Wolfhound, Mature Sabretooth Tiger, Large
                          Mistcougar, Ancient Large Mistcougar, Old Large
                          Mistcougar, Feral Boar, Misthide Mauler, Rhino, Rare
                          Direboar, Ferocious Misthide Mauler, Rare Rhino, Alpha
                          Mistcougar, Ancient Alpha Mistcougar, Old Alpha
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
                    reward={reward}
                    name="Loot a wild Baby Animal"
                    id="UNIQUE_FURNITUREITEM_ADC_RUG_DIREBEAR"
                    title="Direbear Rug"
                  />
                  <Entry
                    reward={reward}
                    name="Loot 3 wild Baby Animals"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Loot 5 different Baby Animals"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Catch your first fish"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Catch 3 types of fish"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Eat 10 fish"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Catch 6 types of fish"
                    id="T5_FOCUSPOTION_NONTRADABLE"
                    title="Expert's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Eat 30 fish"
                    id="T3_SILVERBAG_NONTRADABLE"
                    title="Journeyman's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Catch a saltwater fish"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Catch a fish with Fish Bait"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Catch 10 types of fish"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Catch fish worth 3,000 Fame"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Catch 15 types of fish"
                    id="UNIQUE_UNLOCK_SHOES_VANITY_BARD_BLUE_NON_TRADABLE"
                    title="Wardrobe Skin: Blue Bard's Shoes"
                  />
                  <Entry
                    reward={reward}
                    name="Catch fish worth 10,000 Fame"
                    id="UNIQUE_FURNITUREITEM_KEEPER_CAULDRON"
                    title="Keeper Cauldron"
                  />
                  <Entry
                    reward={reward}
                    name="Catch 21 types of fish"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Catch fish worth 30,000 Fame"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Catch 28 types of fish"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x10)"
                  />
                  <Entry
                    reward={reward}
                    name="Catch a Shark"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Catch fish worth 100,000 Fame"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Catch fish worth 300,000 Fame"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Catch fish worth a million Fame"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Catch fish worth 3 million Fame"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Harvest 30 resources from Resource Mobs"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Harvest resources from 3 Resource Mob types"
                    id="T3_MEAL_PIE"
                    title="Chicken Pie"
                  />
                  <Entry
                    reward={reward}
                    name="Harvest resources from 7 Resource Mob types"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Harvest resources from 12 Resource Mob types"
                    id="T5_FOCUSPOTION_NONTRADABLE"
                    title="Expert's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Harvest a resource from an Aspect"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Harvest resources from 18 Resource Mob types"
                    id="T7_SKILLBOOK_GATHER_FIBER_NONTRADABLE"
                    title="Grandmaster Fiber Harvester Tome"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Harvest resources from 25 Resource Mob types"
                    id="T7_SKILLBOOK_GATHER_WOOD_NONTRADABLE"
                    title="Grandmaster Lumberjack Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Harvest resources from a Guardian in the Roads of Avalon"
                    id="T6_FOCUSPOTION_NONTRADABLE"
                    title="Master's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Harvest resources from 34 Resource Mob types"
                    id="T7_SKILLBOOK_GATHER_ORE_NONTRADABLE"
                    title="Grandmaster Ore Miner Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Harvest 3,000 resources from Aspects"
                    id="T6_FOCUSPOTION_NONTRADABLE"
                    title="Master's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Harvest resources from 46 Resource Mob types"
                    id="T7_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                    title="Grandmaster Animal Skinner Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Harvest 3,000 resources from Ancient Resource Mobs"
                    id="T7_SKILLBOOK_GATHER_ROCK_NONTRADABLE"
                    title="Grandmaster Quarrier Tome"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Harvest 100 resources from Resource Mobs"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Harvest 300 resources from Resource Mobs"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Harvest 1,000 resources from Resource Mobs"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Harvest 10,000 resources from Resource Mobs"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Harvest 10,000 resources from Aspects"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Harvest 10,000 resources from Ancient Resource Mobs"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Gather a resource from a Dynamic Resource Hotspot"
                    id="T4_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                    title="Adept Animal Skinner Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Gather 500 resources from Dynamic Resource Hotspots"
                    id="T5_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                    title="Expert Animal Skinner Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Enter a Resource Mist from a Dynamic Resource Hotspot in the Outlands"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Gather 100 resources inside Resource Mists"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Gather 1,000 resources from Dynamic Resource Hotspots"
                    id="T6_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                    title="Master Animal Skinner Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Gather 500 resources inside Resource Mists"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Gather 10,000 resources from a Dynamic Resource Hotspot"
                    id="T7_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                    title="Grandmaster Animal Skinner Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Gather 1,000 resources inside Resource Mists"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Gather 50,000 resources from a Dynamic Resource Hotspot"
                    id="T8_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                    title="Elder Animal Skinner Tome"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Gather 250 resources in a yellow zone"
                    id="UNIQUE_FURNITUREITEM_HERETICS_TOOL_BOARD_A"
                    title="Heretic Toolboard"
                  />
                  <Entry
                    reward={reward}
                    name="Gather 250 resources in the yellow Mists"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Gather 250 resources in a yellow zone while faction flagged"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Gather 250 resources in a red zone"
                    id="T5_SKILLBOOK_GATHER_WOOD_NONTRADABLE"
                    title="Expert Lumberjack Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Gather 250 resources in a red zone while faction flagged"
                    id="T5_SKILLBOOK_GATHER_ROCK_NONTRADABLE"
                    title="Expert Quarrier Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Gather 250 resources in a black zone"
                    id="T5_SKILLBOOK_GATHER_ORE_NONTRADABLE"
                    title="Expert Ore Miner Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Gather 250 resources in the black Mists"
                    id="T5_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                    title="Expert Animal Skinner Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Gather 250 resources in the Roads of Avalon"
                    id="T5_SKILLBOOK_GATHER_FIBER_NONTRADABLE"
                    title="Expert Fiber Harvester Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Gather 250 resources in Mountain regions"
                    id="T4_SKILLBOOK_GATHER_ORE_NONTRADABLE"
                    title="Adept Ore Miner Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Gather 250 resources in Forest regions"
                    id="T4_SKILLBOOK_GATHER_WOOD_NONTRADABLE"
                    title="Adept Lumberjack Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Gather 250 resources in Steppe regions"
                    id="T4_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                    title="Adept Animal Skinner Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Gather 250 resources in Highland regions"
                    id="T4_SKILLBOOK_GATHER_ROCK_NONTRADABLE"
                    title="Adept Quarrier Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Gather 250 resources in Swamp regions"
                    id="T4_SKILLBOOK_GATHER_FIBER_NONTRADABLE"
                    title="Adept Fiber Harvester Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Gather 1,000 resources in Mountain regions"
                    id="T6_SKILLBOOK_GATHER_ORE_NONTRADABLE"
                    title="Master Ore Miner Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Gather 1,000 resources in Forest regions"
                    id="T6_SKILLBOOK_GATHER_WOOD_NONTRADABLE"
                    title="Master Lumberjack Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Gather 1,000 resources in Steppe regions"
                    id="T6_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                    title="Master Animal Skinner Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Gather 1,000 resources in Highland regions"
                    id="T6_SKILLBOOK_GATHER_ROCK_NONTRADABLE"
                    title="Master Quarrier Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Gather 1,000 resources in Swamp regions"
                    id="T6_SKILLBOOK_GATHER_FIBER_NONTRADABLE"
                    title="Master Fiber Harvester Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Gather 1,000 resources in Black Zones"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Gather 10,000 resources in Mountain regions"
                    id="T8_SKILLBOOK_GATHER_ORE_NONTRADABLE"
                    title="Elder Ore Miner Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Gather 10,000 resources in Forest regions"
                    id="T8_SKILLBOOK_GATHER_WOOD_NONTRADABLE"
                    title="Elder Lumberjack Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Gather 10,000 resources in Steppe regions"
                    id="T8_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                    title="Elder Animal Skinner Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Gather 10,000 resources in Highland regions"
                    id="T8_SKILLBOOK_GATHER_ROCK_NONTRADABLE"
                    title="Elder Quarrier Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Gather 10,000 resources in Swamp regions"
                    id="T8_SKILLBOOK_GATHER_FIBER_NONTRADABLE"
                    title="Elder Fiber Harvester Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Gather 10,000 resources in Black Zones"
                    id="T6_FOCUSPOTION_NONTRADABLE"
                    title="Master's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Visit a Royal City"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Visit two Royal Cities"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x10)"
                  />
                  <Entry
                    reward={reward}
                    name="Visit Caerleon"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Visit a Portal Town"
                    id="T3_VANITY_CONSUMABLE_FIREWORKS_YELLOW_NONTRADABLE"
                    title="Royal Yellow Fireworks (x3)"
                  />
                  <Entry
                    reward={reward}
                    name="Use the Invisibility Shrine in a Portal Town"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Use the S.A.F.E. Portal in a Portal Town"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Use the S.A.F.E. Portal to return to a Portal Town"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Find the lost city of Brecilien"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Purchase an item from Eralia Wayfarer in Brecilien"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Visit a Rest in the Outlands"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Ride a Horse"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Find a Hidden Treasure in the open world"
                    id="T3_SILVERBAG_NONTRADABLE"
                    title="Journeyman's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Ride an Ox"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Travel 20 kilometers"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Ride a Direwolf"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Find a Coffer Chest in the open world"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Find 5 Hidden Treasures in the open world"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Find 5 Coffer Chests in the open world"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Find 10 Hidden Treasures in the open world"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Ride a Faction Warfare mount"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Find 10 Coffer Chests in the open world"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Find 20 Hidden Treasures in the open world"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Ride a Mystic Owl from Brecilien"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Find 20 Coffer Chests in the open world"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Find 40 Hidden Treasures in the open world"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Ride an Elite Faction Warfare mount"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Find 40 Coffer Chests in the open world"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Find 65 Hidden Treasures in the open world"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Ride a Battle Mount"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Find 65 Coffer Chests in the open world"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x2)"
                  />
                  <Entry
                    reward={reward}
                    name="Find 100 Hidden Treasures in the open world"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x5)"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Find 100 Coffer Chests in the open world"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Find 200 Hidden Treasures in the open world"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x8)"
                  />
                  <Entry
                    reward={reward}
                    name="Ride a Transport Mammoth"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Find 200 Coffer Chests in the open world"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Find 500 Hidden Treasures in the open world"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x15)"
                  />
                  <Entry
                    reward={reward}
                    name="Ride a Command Mammoth"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Travel 50 kilometers"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Travel 100 kilometers"
                    id="UNIQUE_UNLOCK_OFF_VANITY_PRIEST_NON_TRADABLE"
                    title="Wardrobe Skin: Monk's Walking Staff"
                  />
                  <Entry
                    reward={reward}
                    name="Travel 200 kilometers"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Travel 500 kilometers"
                    id="UNIQUE_FURNITUREITEM_ADC_CARNIVAL_MASK_CART"
                    title="Carnival Costume Cart"
                  />
                  <Entry
                    reward={reward}
                    name="Travel 1,000 kilometers"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Travel 3,000 Kilometers"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Enter a Yellow Zone"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Earn 10,000 Fame in Yellow Zones"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Enter a Red Zone"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Earn 40,000 Fame in Red Zones"
                    id="UNIQUE_UNLOCK_SKIN_HORSE_KEEPER_NON_TRADABLE"
                    title="Riding Horse Skin: Keeper Horse"
                  />
                  <Entry
                    reward={reward}
                    name="Enter a black zone"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Use the Journey Back ability in a Black Zone"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Earn 100,000 Fame in Black Zones"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Earn 100,000 Fame in Quality Level 2 Black Zones"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Earn 120,000 Fame in Quality Level 3 Black Zones"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Earn 250,000 Fame in Quality Level 4 Black Zones"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Earn 500,000 Fame in Quality Level 5 Black Zones"
                    id="T5_LEARNINGPOINTS_NONTRADABLE"
                    title="Expert's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Reach the first positive reputation level"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Reach the reputation level: Virtuous"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Reach the reputation level: Noble"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Reach maximum reputation level"
                    id="UNIQUE_REPAIRPOWDER_ADC_GENERAL_01_NONTRADEABLE"
                    title="Scroll of Repair"
                  />
                  <Entry
                    reward={reward}
                    name="Reach the first negative reputation level"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Reach the reputation level: Nefarious"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Follow a Will o' Wisp into the Mists"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Rescue 10 Wisps"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Open 3 Small Caches"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Open 3 Medium Caches"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Enter Knightfall Abbey"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Open 3 chests in Knightfall Abbey"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Deliver a Weakened Wisp to a Sanctuary"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Gain Accepted status with Brecilien"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Earn 50,000 Fame in Solo Lethal Mists"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Rescue 30 Wisps in Solo Lethal Mists"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Deliver a Weakened Wisp in Lethal Mists"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Open 20 chests in Knightfall Abbey"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Gain 50,000 Fame in Greater Mists"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Rescue 50 Wisps in Greater Mists"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Deliver 5 Weakened Wisps in Greater Mists"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Open 100 chests in Knightfall Abbey"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Deliver 50 Weakened Wisps in Solo Lethal Mists"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Earn 500,000 fame in Solo Lethal Mists"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Earn a million Fame in Solo Lethal Mists"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Earn 5 million Fame in Solo Lethal Mists"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Earn 10 million Fame in Solo Lethal Mists"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Earn 500,000 Fame in Greater Mists"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Earn a million Fame in Greater Mists"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Earn 5 million Fame in Greater Mists"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Earn 10 million Fame in Greater Mists"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Open 500 chests in Knightfall Abbey"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Open 2,000 chests in Knightfall Abbey"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Get 'Welcomed' Brecilien standing"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Get 'Favored' Brecilien standing"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Gain 'Esteemed' Brecilien standing"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Gain 'Venerated' Brecilien standing"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="...and how to kill them"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight (x5)"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Earn 100 Might"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Earn 90 Favor"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Trade your Favor for an item at the Energy Manipulator"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Earn 1,000 Might"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Trade your Favor for a Conqueror's Chest at the Energy Manipulator"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Earn 8,000 Might"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Earn 5,000 Favor"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Earn 40,000 Might"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Earn 100,000 Might"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Earn 200,000 Might"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Earn 120,000 Favor"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Earn 1 million Might"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Earn 2 million Might"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x5)"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Enter a Road of Avalon"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 50 mobs in the Roads of Avalon"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Open an Avalonian Chest in the Roads of Avalon"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Enter a Deep Road of Avalon"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 500 mobs in the Roads of Avalon"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Open a Blue Avalonian Chest in the Roads of Avalon"
                    id="UNIQUE_FURNITUREITEM_XMAS_PRESENT"
                    title="Present Box"
                  />
                  <Entry
                    reward={reward}
                    name="Open a Rare Avalonian Chest in the Roads of Avalon"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Open 30 Green Chests in Roads of Avalon"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 2,000 mobs in the Roads of Avalon"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Open a Yellow Avalonian Chest in the Roads of Avalon"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 5,000 mobs in the Roads of Avalon"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x3)"
                  />
                  <Entry
                    reward={reward}
                    name="Open 50 Blue Chests in Roads of Avalon"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Open 100 Green Chests in Roads of Avalon"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x5)"
                  />
                  <Entry
                    reward={reward}
                    name="Open a Legendary Chest in the Roads"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Open 150 Blue Chests in Roads of Avalon"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x10)"
                  />
                  <Entry
                    reward={reward}
                    name="Open a Legendary Yellow Chest in the Roads of Avalon"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Open 50 Yellow Chests in Roads of Avalon"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x15)"
                  />
                  <Entry
                    reward={reward}
                    name="Open 500 Green Chests in Roads of Avalon"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x20)"
                  />
                  <Entry
                    reward={reward}
                    name="Open 150 Yellow Chests in Roads of Avalon"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x20)"
                  />
                  <Entry
                    reward={reward}
                    name="Open 500 Blue Chests in Roads of Avalon"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x25)"
                  />
                  <Entry
                    reward={reward}
                    name="Open 500 Yellow Chests in Roads of Avalon"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x25)"
                  />
                  <Entry
                    reward={reward}
                    name="Earn 1 million Fame in the Roads of Avalon"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Earn 3 million Fame in the Roads of Avalon"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Earn 10 million Fame in the Roads of Avalon"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Earn 30 million Fame in the Roads of Avalon"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x50)"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Enter a Smuggler's Den"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Free a Captured Smuggler"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Buy a Round for the Smugglers"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Visit 3 Smuggler's Dens"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Free 4 Captured Smugglers"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Buy 5 Rounds for the Smugglers"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Help deliver a Smuggler Crate"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Gain Accepted Standing with the Smugglers"
                    id="QUESTITEM_TOKEN_SMUGGLER"
                    title="Smuggler's Coin"
                  />
                  <Entry
                    reward={reward}
                    name="Visit 6 Smuggler's Dens"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Free 10 Captured Smugglers"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Buy 15 Rounds for the Smugglers"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Help deliver 4 Smuggler Crates"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Visit 10 Smuggler's Dens"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Free 25 Captured Smugglers"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Visit 15 Smuggler's Dens"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Buy 50 Rounds for the Smugglers"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Help deliver 12 Smuggler Crates"
                    id="QUESTITEM_TOKEN_SMUGGLER"
                    title="Smuggler's Coin (x5)"
                  />
                  <Entry
                    reward={reward}
                    name="Gain Respected Standing with the Smugglers"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Visit 21 Smuggler's Dens"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Help deliver a Rare Smuggler Crate"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Free 65 Captured Smugglers"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Help deliver 40 Smuggler Crates"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Buy 180 Rounds for the Smugglers"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Help deliver a Legendary Smuggler Crate"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Gain Esteemed Standing with the Smugglers"
                    id="QUESTITEM_TOKEN_SMUGGLER"
                    title="Smuggler's Coin (x10)"
                  />
                  <Entry
                    reward={reward}
                    name="Visit 28 Smuggler's Dens"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight (x5)"
                  />
                  <Entry
                    reward={reward}
                    name="Free 150 Captured Smugglers"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x3)"
                  />
                  <Entry
                    reward={reward}
                    name="Buy 500 Rounds for the Smugglers"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x2)"
                  />
                  <Entry
                    reward={reward}
                    name="Help deliver 120 Smuggler Crates"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight (x5)"
                  />
                  <Entry
                    reward={reward}
                    name="Visit 35 Smuggler's Dens"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight (x5)"
                  />
                  <Entry
                    reward={reward}
                    name="Help deliver 300 Smuggler Crates"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x3)"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Win your first Arena match"
                    id="T3_SILVERBAG_NONTRADABLE"
                    title="Journeyman's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Win 5 Arena or Crystal Arena Matches"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Win 10 Arena or Crystal Arena Matches"
                    id="T4_SILVERBAG_NONTRADABLE"
                    title="Adept's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Deal 15,000 damage in a single Arena or Crystal Arena match"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Win 20 Arena or Crystal Arena Matches"
                    id="QUESTITEM_TOKEN_ARENA_CRYSTAL"
                    title="Arena Sigil (x20)"
                  />
                  <Entry
                    reward={reward}
                    name="Get 5 kills in a single Arena or Crystal Arena match"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Win 35 Arena or Crystal Arena Matches"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Capture 4 Runestones in a single Arena or Crystal Arena match"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Win 50 Arena or Crystal Arena Matches"
                    id="T1_KILL_EMOTE_TOMBSTONE_CHARGES_NONTRADABLE"
                    title="Tombstone Victory Emote Charge (x10)"
                  />
                  <Entry
                    reward={reward}
                    name="Deal 22,000 damage in an single Arena or Crystal Arena match"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Win 75 Arena or Crystal Arena Matches"
                    id="QUESTITEM_TOKEN_ARENA_CRYSTAL"
                    title="Arena Sigil (x30)"
                  />
                  <Entry
                    reward={reward}
                    name="Take 20,000 damage without dying in a single Arena or Crystal Arena match"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Win 100 Arena or Crystal Arena matches"
                    id="T1_KILL_EMOTE_SWORD_CHARGES_NONTRADABLE"
                    title="Sword Victory Emote Charge (x20)"
                  />
                  <Entry
                    reward={reward}
                    name="Heal 15,000 health in a single Arena or Crystal Arena match"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Win 150 Arena or Crystal Arena Matches"
                    id="QUESTITEM_TOKEN_ARENA_CRYSTAL"
                    title="Arena Sigil (x40)"
                  />
                  <Entry
                    reward={reward}
                    name="Get 10 kills in a single Arena or Crystal Arena match"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Win 200 Arena or Crystal Arena Matches"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Deal 30,000 damage in a single Arena or Crystal Arena match"
                    id="T1_KILL_EMOTE_HAMMER_CHARGES_NONTRADABLE"
                    title="Hammer Victory Emote Charge (x20)"
                  />
                  <Entry
                    reward={reward}
                    name="Win 250 Arena or Crystal Arena Matches"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Capture 8 Runestones in a single Arena or Crystal Arena match"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Win 300 Arena or Crystal Arena Matches"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Deal 40,000 damage in a single Arena or Crystal Arena match"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Deal 50,000 damage in a single Arena or Crystal Arena match"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Take 50,000 damage without dying in a single Arena or Crystal Arena match"
                    id="UNIQUE_UNLOCK_ARMOR_VANITY_GLADIATOR_ARENA"
                    title="Wardrobe Skin: Arena Gladiator Armor"
                  />
                  <Entry
                    reward={reward}
                    name="Heal 30,000 health in a single Arena or Crystal Arena match"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Heal 50,000 health in a single Arena or Crystal Arena match"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Increase your rank in the Crystal Arena"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Reach Iron III Rank in Crystal Arena"
                    id="T4_SILVERBAG_NONTRADABLE"
                    title="Adept's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Reach Iron IV Rank in Crystal Arena"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Reach Bronze Rank in Crystal Arena"
                    id="T1_KILL_EMOTE_GHOST_CHARGES_NONTRADABLE"
                    title="Ghost Victory Emote Charge (x10)"
                  />
                  <Entry
                    reward={reward}
                    name="Reach Bronze II Rank in Crystal Arena"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Reach Bronze III Rank in Crystal Arena"
                    id="QUESTITEM_TOKEN_ARENA_CRYSTAL"
                    title="Arena Sigil (x20)"
                  />
                  <Entry
                    reward={reward}
                    name="Reach Bronze IV Rank in Crystal Arena"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Reach Silver Rank in the Crystal Arena"
                    id="UNIQUE_UNLOCK_HEAD_VANITY_PRIEST_NON_TRADABLE"
                    title="Wardrobe Skin: Monk's Hood"
                  />
                  <Entry
                    reward={reward}
                    name="Reach Silver II Rank in the Crystal Arena"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Reach Silver III Rank in Crystal Arena"
                    id="T1_KILL_EMOTE_TOMBSTONE_CHARGES_NONTRADABLE"
                    title="Tombstone Victory Emote Charge (x20)"
                  />
                  <Entry
                    reward={reward}
                    name="Reach Silver IV Rank in Crystal Arena"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Reach Gold Rank in Crystal Arena"
                    id="T4_TOKEN_CRYSTALLEAGUE_NONLETHAL_LVL_01"
                    title="Crystal Token (5v5 Nonlethal - Lvl. 1)"
                  />
                  <Entry
                    reward={reward}
                    name="Reach Gold II Rank in Crystal Arena"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Reach Gold III Rank in Crystal Arena"
                    id="UNIQUE_UNLOCK_HEAD_VANITY_GLADIATOR_ARENA"
                    title="Wardrobe Skin: Arena Gladiator Helm"
                  />
                  <Entry
                    reward={reward}
                    name="Reach Gold IV Rank in Crystal Arena"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x5)"
                  />
                  <Entry
                    reward={reward}
                    name="Reach Crytal Rank in Crystal Arena"
                    id="T4_TOKEN_CRYSTALLEAGUE_CITY_LVL_01"
                    title="Crystal Token (20v20 -  Lvl. 1)"
                  />
                  <Entry
                    reward={reward}
                    name="Win a match by a 50 point margin"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Win a match by a 75 point margin"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Win a match by a 100 point margin"
                    id="UNIQUE_UNLOCK_CAPE_VANITY_GLADIATOR_ARENA"
                    title="Wardrobe Skin: Arena Gladiator Cape"
                  />
                  <Entry
                    reward={reward}
                    name="Win a match by a 125 point margin"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Defeat the final boss in a Hunter Corrupted Dungeon"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Get 666 Infamy in Corrupted Dungeons"
                    id="T4_SILVERBAG_NONTRADABLE"
                    title="Adept's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat another player after invading their Corrupted Dungeon"
                    id="T5_CORRUPTED_NONLETHAL_MAP"
                    title="Corrupted Dungeon Map (Hunter)"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat an invading player in a Corrupted Dungeon"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Get 2,500 Infamy in Corrupted Dungeons"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 5 players in a Hunter Corrupted Dungeon"
                    id="T1_KILL_EMOTE_SWORD_CHARGES_NONTRADABLE"
                    title="Sword Victory Emote Charge (x10)"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat the final boss in a Stalker Corrupted Dungeon"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Get 10,000 Infamy in Corrupted Dungeons"
                    id="T6_CORRUPTED_LETHAL_MAP"
                    title="Corrupted Dungeon Map (Stalker/Slayer)"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat a player in a Stalker Corrupted Dungeon"
                    id="T1_KILL_EMOTE_HELLGATE_CHARGES_NONTRADABLE"
                    title="Hellgate Victory Emote Charge (x20)"
                  />
                  <Entry
                    reward={reward}
                    name="Get 50,000 Infamy in Corrupted Dungeons"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 5 players in a Stalker Corrupted Dungeon"
                    id="UNIQUE_FURNITUREITEM_ADC_HALLOWEEN_SCARECROW_A"
                    title="Halloween Scarecrow"
                  />
                  <Entry
                    reward={reward}
                    name="Unlock the Slayer difficulty in Corrupted Dungeons"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat a player in a Slayer Corrupted Dungeon"
                    id="UNIQUE_UNLOCK_HEAD_VANITY_ENTERTAINER_NON_TRADABLE"
                    title="Wardrobe Skin: Entertainer's Mask"
                  />
                  <Entry
                    reward={reward}
                    name="Get 150,000 Infamy in Corrupted Dungeons"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 5 players in a Slayer Corrupted Dungeon"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 100 players in full-loot Corrupted Dungeons"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x2)"
                  />
                  <Entry
                    reward={reward}
                    name="Get 300,000 Infamy in Corrupted Dungeons"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x5)"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 300 players in full-loot Corrupted Dungeons"
                    id="T1_KILL_EMOTE_TOMBSTONE_CHARGES_NONTRADABLE"
                    title="Tombstone Victory Emote Charge (x50)"
                  />
                  <Entry
                    reward={reward}
                    name="Get 600,000 Infamy in Corrupted Dungeons"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x10)"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 666 players in full-loot Corrupted Dungeons"
                    id="T1_KILL_EMOTE_HAMMER_CHARGES_NONTRADABLE"
                    title="Hammer Victory Emote Charge (x500)"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Enlist in any of the six City Factions"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Capture an Outpost"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Assist in completely capturing another city's zone in Faction Warfare"
                    id="T4_SILVERBAG_NONTRADABLE"
                    title="Adept's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Capture 10 Outposts"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Earn a Faction Warfare Daily Reward"
                    id="T4_SILVERBAG_NONTRADABLE"
                    title="Adept's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Knock down or assist a knockdown of an enemy faction player"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Reach 15,000 standing with any Faction"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 2 different Faction Champions"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Reach 30,000 standing with any Faction"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Capture 30 Faction Outposts"
                    id="T1_KILL_EMOTE_FLAG_CHARGES_NONTRADABLE"
                    title="Guild Banner Victory Emote Charge (x10)"
                  />
                  <Entry
                    reward={reward}
                    name="Finish a Trade Mission for any city"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Reach 60,000 standing with any Faction"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Capture 5 Outposts in Red Zones"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 3 different Faction Champions"
                    id="T1_KILL_EMOTE_OVERGROWN_CHARGES_NONTRADABLE"
                    title="Overgrown Victory Emote Charge (x20)"
                  />
                  <Entry
                    reward={reward}
                    name="Kill or assist a kill of an enemy faction player in a Red Zone"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Help repel a Bandit Assault"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Reach 240,000 standing with any Faction"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Capture 100 Outposts"
                    id="UNIQUE_REPAIRPOWDER_ADC_GENERAL_01_NONTRADEABLE"
                    title="Scroll of Repair"
                  />
                  <Entry
                    reward={reward}
                    name="Achieve a standing of 330,000 with any faction"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat all opposing City Faction Warmasters at least once"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Capture 300 Faction Outposts"
                    id="T1_KILL_EMOTE_OVERGROWN_CHARGES_NONTRADABLE"
                    title="Overgrown Victory Emote Charge (x50)"
                  />
                  <Entry
                    reward={reward}
                    name="Knock down or assist knockdowns of 30 enemy faction players"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Knock down or assist knockdowns of 100 enemy faction players"
                    id="T1_KILL_EMOTE_HAMMER_CHARGES_NONTRADABLE"
                    title="Hammer Victory Emote Charge (x10)"
                  />
                  <Entry
                    reward={reward}
                    name="Knock down or assist knockdowns of 300 enemy faction players"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Knock down or assist knockdowns of 1000 enemy faction players"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Kill or assist 10 enemy faction player kills in Red Zones"
                    id="UNIQUE_FURNITUREITEM_ADC_GRAVE_A"
                    title="Tomb of the Unknown"
                  />
                  <Entry
                    reward={reward}
                    name="Kill or assist 30 enemy faction player kills in Red Zones"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Kill or assist 100 enemy faction player kills in Red Zones"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Kill or assist 300 enemy faction player kills in Red Zones"
                    id="T1_KILL_EMOTE_SWORD_CHARGES_NONTRADABLE"
                    title="Sword Victory Emote Charge (x50)"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Open an open-world Treasure Chest"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Knock down another player in a Yellow Zone"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Open 10 open-world Treasure Chests"
                    id="T1_KILL_EMOTE_OVERGROWN_CHARGES_NONTRADABLE"
                    title="Overgrown Victory Emote Charge (x10)"
                  />
                  <Entry
                    reward={reward}
                    name="Kill or assist a kill in PvP"
                    id="UNIQUE_FURNITUREITEM_ADC_GRAVE_B"
                    title="Memorial of the Fallen"
                  />
                  <Entry
                    reward={reward}
                    name="Loot any armor, foot gear and a mount from a killed player at the same time"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Get 200,000 Kill Fame"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Kill 10 players in full-loot regions"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Kill 3 players in the Roads of Avalon"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Kill 25 players in full-loot regions"
                    id="T1_KILL_EMOTE_FLAG_CHARGES_NONTRADABLE"
                    title="Guild Banner Victory Emote Charge (x20)"
                  />
                  <Entry
                    reward={reward}
                    name="Kill 10 players in Static Dungeons"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Get 2 million Kill Fame in the Open World"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Kill 6 players within one minute"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Kill 100 players in full-loot regions"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Get 2 million Kill Fame in the Roads of Avalon"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Get 5 million Kill Fame in Static Dungeons"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Kill 6 players within one minute (not including assists)"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Kill 300 players in the open world"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Get 10 million Kill Fame in Black Zones"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x5)"
                  />
                  <Entry
                    reward={reward}
                    name="Get 10 million Kill Fame in Static Dungeons"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x5)"
                  />
                  <Entry
                    reward={reward}
                    name="Get 10 million Kill Fame in the Roads of Avalon"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x5)"
                  />
                  <Entry
                    reward={reward}
                    name="Get 50 million Kill Fame in Black Zones"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x15)"
                  />
                  <Entry
                    reward={reward}
                    name="Get 100 million Kill Fame in Black Zones"
                    id="T1_KILL_EMOTE_GHOST_CHARGES_NONTRADABLE"
                    title="Ghost Victory Emote Charge (x50)"
                  />
                  <Entry
                    reward={reward}
                    name="Get 500 million Kill Fame in Black Zones"
                    id="T1_KILL_EMOTE_TOMBSTONE_CHARGES_NONTRADABLE"
                    title="Tombstone Victory Emote Charge (x500)"
                  />
                  <Entry
                    reward={reward}
                    name="Open 30 open-world Treasure Chests in full-loot regions"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Open 100 open-world Treasure Chests"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Open 30 Medium Treasure Chests"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Open 10 Large Treasure Chests"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Open 500 open-world Treasure Chests"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x5)"
                  />
                  <Entry
                    reward={reward}
                    name="Open 300 Medium Treasure Chests"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x5)"
                  />
                  <Entry
                    reward={reward}
                    name="Open 100 Large Treasure Chests"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x5)"
                  />
                  <Entry
                    reward={reward}
                    name="Open a Legendary Large Treasure Chest"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Enter a Hellgate"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat a Mini Boss in a Hellgate"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat a team of enemy players in any type of Hellgate"
                    id="T5_HELLGATE_2V2_NON_LETHAL_1_MAP"
                    title="Expert's Hellgate Ritual (2v2 - Nonlethal)"
                  />
                  <Entry
                    reward={reward}
                    name="Chain 2 Hellgates without returning to the surface"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Gain 10,000 Infamy in 2v2 Hellgates"
                    id="T1_KILL_EMOTE_HELLGATE_CHARGES_NONTRADABLE"
                    title="Hellgate Victory Emote Charge (x10)"
                  />
                  <Entry
                    reward={reward}
                    name="Knock down 10 players in Hellgates"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 5 Mini Bosses in Hellgates"
                    id="UNIQUE_FURNITUREITEM_ADC_HALLOWEEN_PUMPKIN_LANTERN_B"
                    title="Friendly Pumpkin Lantern"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat a Boss in a Hellgate"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Gain 20,000 Infamy in 2v2 Hellgates"
                    id="T1_KILL_EMOTE_GHOST_CHARGES_NONTRADABLE"
                    title="Ghost Victory Emote Charge (x20)"
                  />
                  <Entry
                    reward={reward}
                    name="Chain 5 Hellgates without returning to the surface"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Knock down 50 players in Hellgates"
                    id="T6_HELLGATE_2V2_LETHAL_1_MAP"
                    title="Master's Hellgate Ritual (2v2 - Lethal)"
                  />
                  <Entry
                    reward={reward}
                    name="Kill a player in a full-loot Hellgate"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Gain 50,000 Infamy in 2v2 Hellgates"
                    id="T7_HELLGATE_5V5_LETHAL_1_MAP"
                    title="Grandmaster's Hellgate Ritual (5v5 - Lethal)"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat a Mini Boss in a 5v5 Hellgate"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat an enemy team in a 5v5 Hellgate"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Gain 20,000 Infamy in 5v5 Hellgates"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Knock down 200 players in Hellgates"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Gain 50,000 Infamy in 5v5 Hellgates"
                    id="T8_HELLGATE_10V10_LETHAL_1_MAP"
                    title="Elder's Hellgate Ritual (10v10 - Lethal)"
                  />
                  <Entry
                    reward={reward}
                    name="Kill 20 players in full-loot Hellgates"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver (x5)"
                  />
                  <Entry
                    reward={reward}
                    name="Chain 10 Hellgates without returning to the surface"
                    id="T5_LEARNINGPOINTS_NONTRADABLE"
                    title="Expert's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Kill 50 players in full-loot Hellgates"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x5)"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat a Mini Boss in a 10v10 Hellgate"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat an enemy team in a 10v10 Hellgate"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Kill 200 players in full-loot Hellgates"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x10)"
                  />
                  <Entry
                    reward={reward}
                    name="Kill 500 players in full-loot Hellgates"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x20)"
                  />
                  <Entry
                    reward={reward}
                    name="Kill 1,000 players in full-loot Helgates"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x40)"
                  />
                  <Entry
                    reward={reward}
                    name="Gain 100,000 Infamy in 2v2 Hellgates"
                    id="T1_KILL_EMOTE_GHOST_CHARGES_NONTRADABLE"
                    title="Ghost Victory Emote Charge (x500)"
                  />
                  <Entry
                    reward={reward}
                    name="Gain 250,000 Infamy in 2v2 Hellgates"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x20)"
                  />
                  <Entry
                    reward={reward}
                    name="Gain 100,000 Infamy in 5v5 Hellgates"
                    id="T1_KILL_EMOTE_SWORD_CHARGES_NONTRADABLE"
                    title="Sword Victory Emote Charge (x500)"
                  />
                  <Entry
                    reward={reward}
                    name="Gain 250,000 Infamy in 5v5 Hellgates"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x25)"
                  />
                  <Entry
                    reward={reward}
                    name="Gain 50,000 Infamy in 10v10 Hellgates"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x8)"
                  />
                  <Entry
                    reward={reward}
                    name="Gain 100,000 Infamy in 10v10 Hellgates"
                    id="T1_KILL_EMOTE_HELLGATE_CHARGES_NONTRADABLE"
                    title="Hellgate Victory Emote Charge (x500)"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Participate in a Crystal League Battle"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Win a 5v5 Crystal League Match"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Win a Rank 2 5v5 Crystal League Match"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Win a Rank 3 5v5 Crystal League Match"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x50)"
                  />
                  <Entry
                    reward={reward}
                    name="Win a 20v20 Crystal League Match"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Win a Rank 4 5v5 Crystal League Match"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x5)"
                  />
                  <Entry
                    reward={reward}
                    name="Win a Rank 5 5v5 Crystal League Match"
                    id="T1_KILL_EMOTE_FLAG_CHARGES_NONTRADABLE"
                    title="Guild Banner Victory Emote Charge (x50)"
                  />
                  <Entry
                    reward={reward}
                    name="Win a Rank 6 5v5 Crystal League Match"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x15)"
                  />
                  <Entry
                    reward={reward}
                    name="Win a Rank 7 5v5 Crystal League Match"
                    id="UNIQUE_UNLOCK_CAPE_VANITY_GLADIATOR_CRYSTAL"
                    title="Wardrobe Skin: Crystal Gladiator Cape"
                  />
                  <Entry
                    reward={reward}
                    name="Win a Rank 8 5v5 Crystal League Match"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x40)"
                  />
                  <Entry
                    reward={reward}
                    name="Win a Rank 9 5v5 Crystal League Match"
                    id="UNIQUE_UNLOCK_HEAD_VANITY_GLADIATOR_CRYSTAL"
                    title="Wardrobe Skin: Crystal Gladiator Helm"
                  />
                  <Entry
                    reward={reward}
                    name="Win a Rank 2 20v20 Crystal League Match"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x5)"
                  />
                  <Entry
                    reward={reward}
                    name="Win a Rank 3 20v20 Crystal League Match"
                    id="UNIQUE_UNLOCK_SHOES_VANITY_GLADIATOR_CRYSTAL"
                    title="Wardrobe Skin: Crystal Gladiator Boots"
                  />
                  <Entry
                    reward={reward}
                    name="Win a Rank 4 20v20 Crystal League Match"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x10)"
                  />
                  <Entry
                    reward={reward}
                    name="Win a Rank 5 20v20 Crystal League Match"
                    id="T1_KILL_EMOTE_FLAG_CHARGES_NONTRADABLE"
                    title="Guild Banner Victory Emote Charge (x500)"
                  />
                  <Entry
                    reward={reward}
                    name="Win a Rank 6 20v20 Crystal League Match"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x40)"
                  />
                  <Entry
                    reward={reward}
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
              Social & Guild (193)
            </AccordionHeader>
            <AccordionBody accordionId="guild">
              <h4>Player Interactions (17)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <Entry
                    reward={reward}
                    name="Start saying something by typing /s in the chat"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Inspect another player"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Duel another player"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Whisper another player by typing /w"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Trade with another player"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Win a duel"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Inspect 10 players"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Win 5 duels"
                    id="T1_KILL_EMOTE_HAMMER_CHARGES_NONTRADABLE"
                    title="Hammer Victory Emote Charge (x3)"
                  />
                  <Entry
                    reward={reward}
                    name="Trade 10 times with another player"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Inspect 30 players"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Use every emote in the game"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x5)"
                  />
                  <Entry
                    reward={reward}
                    name="Inspect 100 players"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x10)"
                  />
                  <Entry
                    reward={reward}
                    name="Trade 100 times with another player"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Win 20 duels"
                    id="T1_KILL_EMOTE_GHOST_CHARGES_NONTRADABLE"
                    title="Ghost Victory Emote Charge (x5)"
                  />
                  <Entry
                    reward={reward}
                    name="Win 100 duels"
                    id="T1_KILL_EMOTE_TOMBSTONE_CHARGES_NONTRADABLE"
                    title="Tombstone Victory Emote Charge (x20)"
                  />
                  <Entry
                    reward={reward}
                    name="Sell a cabbage to another player in a Black Zone."
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x20)"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Gain 10,000 Fame in a party"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Gain 50,000 Fame while in a party"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Add a friend to your friend list"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Gain 100,000 Fame while in a party"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Look for a group by typing /lfg in the chat"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Add 3 friends to your friend list"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Gain 300,000 Fame while in a party"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Add 5 friends to your friend list"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Gain 50,000 Fame while in a party of 5 or more players"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Gain a million Fame while in a party"
                    id="T5_FOCUSPOTION_NONTRADABLE"
                    title="Expert's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Initiate a Party Ready Check"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Add 10 friends to your friend list"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Visit another player's Personal Island"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Gain 100,000 Fame while in a party of 7 or more players"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Initiate 5 Party Ready Checks"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Gain 3 million Fame while in a party"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Gain 10 million Fame while in a party"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x30)"
                  />
                  <Entry
                    reward={reward}
                    name="Gain 30 million Fame while in a party"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Gain 100 million Fame while in a party"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Gain 30 million Fame while in a party of 5 or more players"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Gain 100 million Fame while in a party of 5 or more players"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x75)"
                  />
                  <Entry
                    reward={reward}
                    name="Gain 10 million Fame while in a party of 20 players"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Open the Guild Finder"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Create or join a guild"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Write in the guild chat by typing /g"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Contribute 10,000 Challenge Points to the Guild Challenge"
                    id="T4_SILVERBAG_NONTRADABLE"
                    title="Adept's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Reach Guild Challenge Level 2 with your Guild"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Contribute 40,000 Challenge Points to the Guild Challenge"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Reach Guild Challenge Level 5 with your Guild"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Contribute 90,000 Challenge Points to the Guild Challenge"
                    id="T5_SILVERBAG_NONTRADABLE"
                    title="Expert's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Reach Guild Challenge Level 15 with your Guild"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Join or create an Alliance"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Contribute 160,000 Challenge Points to the Guild Challenge"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Contribute 250,000 Challenge Points to the Guild Challenge"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Contribute 400,000 Challenge Points to the Guild Challenge"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Contribute 700,000 Challenge Points to the Guild Challenge"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Contribute 1,200,000 Challenge Points to the Guild Challenge"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Contribute 2 million Challenge Points to the Guild Challenge"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Contribute 5 million Challenge Points to the Guild Challenge"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x5)"
                  />
                  <Entry
                    reward={reward}
                    name="Contribute 10 million Challenge Points to the Guild Challenge"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x10)"
                  />
                  <Entry
                    reward={reward}
                    name="Reach Guild Challenge Level 30 with your Guild"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Reach Guild Challenge Level 50 with your Guild"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Reach Guild Challenge Level 75 with your Guild"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Defeat a Crystal Creature"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat every type of Crystal Creature"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 5 Crystal Creatures"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 2 Crystal Creatures in Quality Level 2 Regions"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 10 Crystal Creatures"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 4 Crystal Creatures in Quality Level 3 Regions"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 20 Crystal Creatures"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 7 Crystal Creatures in Quality Level 4 Regions"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 40 Crystal Creatures"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 10 Crystal Creatures in Quality Level 5 Regions"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 65 Crystal Creatures"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 15 Crystal Creatures in Quality Level 6 Regions"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 100 Crystal Creatures"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 20 Tier 8 Crystal Creatures in Quality Level 6 Regions"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 150 Crystal Creatures"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x5)"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 220 Crystal Creatures"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight (x5)"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Help loot a Castle Outpost Chest"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Help loot 3 Castle Outpost Chests"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Help loot a Castle Outpost Uncommon Chest"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Help loot 6 Castle Outpost Chests"
                    id="T1_KILL_EMOTE_HELLGATE_CHARGES_NONTRADABLE"
                    title="Hellgate Victory Emote Charge (x20)"
                  />
                  <Entry
                    reward={reward}
                    name="Help loot 10 Castle Outpost Chests"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Help loot a Castle Outpost Rare Chest"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Help loot 25 Castle Outpost Chests"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Help loot a Castle Outpost Legendary Chest"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Help loot a Castle Chest"
                    id="T5_LEARNINGPOINTS_NONTRADABLE"
                    title="Expert's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Help loot 5 Castle Chests"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Help loot a Castle Uncommon Chest"
                    id="UNIQUE_FURNITUREITEM_KNIGHT_ROUNDTABLE_A"
                    title="Round Table"
                  />
                  <Entry
                    reward={reward}
                    name="Deal 20,000 damage to a Castle Gate"
                    id="T1_KILL_EMOTE_HAMMER_CHARGES_NONTRADABLE"
                    title="Hammer Victory Emote Charge (x40)"
                  />
                  <Entry
                    reward={reward}
                    name="Help loot 10 Castle Chests"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Help loot a Castle Rare Chest"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Deal 100,000 damage to a Castle Gate"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Help loot a Castle Legendary Chest"
                    id="T1_KILL_EMOTE_GHOST_CHARGES_NONTRADABLE"
                    title="Ghost Victory Emote Charge (x100)"
                  />
                  <Entry
                    reward={reward}
                    name="Help loot 50 Castle Outpost Chests"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x2)"
                  />
                  <Entry
                    reward={reward}
                    name="Help loot 100 Castle Outpost Chests"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x5)"
                  />
                  <Entry
                    reward={reward}
                    name="Help loot 300 Castle Outpost Chests"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x300)"
                  />
                  <Entry
                    reward={reward}
                    name="Help loot 50 Castle Chests"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x10)"
                  />
                  <Entry
                    reward={reward}
                    name="Help loot 100 Castle Chests"
                    id="T1_KILL_EMOTE_TOMBSTONE_CHARGES_NONTRADABLE"
                    title="Tombstone Victory Emote Charge (x700)"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Set a Hideout as your Home"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Successfully transport a Power Core to a Hideout"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Enter a Level 2 Hideout owned by your Guild"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Transport a Blue Power Core to a Hideout"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Transport 5 Power Cores to a Hideout"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Transport a Purple Power Core to a Hideout"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Enter a Level 3 Hideout owned by your Guild"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Transport 20 Power Cores to a Hideout"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Transport 10 Blue Power Cores to a Hideout"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Transport 5 Purple Power Cores to a Hideout"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Transport a Golden Power Core to a Hideout"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Transport 100 Power Cores to a Hideout"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Transport 5 Golden Power Cores to a Hideout"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Transport 300 Power Cores to a Hideout"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x5)"
                  />
                  <Entry
                    reward={reward}
                    name="Transport 100 Purple or Golden Power Cores to a Hideout"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver (x5)"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Be part of a player kill with 10 or more assists"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Gain a Resilience buff by having 7 players attack you"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Get a Disarray debuff"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Be part of a battle with at least 15 player deaths"
                    id="T1_KILL_EMOTE_SWORD_CHARGES_NONTRADABLE"
                    title="Sword Victory Emote Charge (x20)"
                  />
                  <Entry
                    reward={reward}
                    name="Be part of a player kill with 15 or more assists"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Gain a Resilience buff by having 10 players attack you"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Kill or assist in killing 12 players within one minute"
                    id="T1_KILL_EMOTE_GHOST_CHARGES_NONTRADABLE"
                    title="Ghost Victory Emote Charge (x40)"
                  />
                  <Entry
                    reward={reward}
                    name="Gain 100,000 Kill Fame from kills with 10 or more assists"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Be part of a battle with at least 25 player deaths"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Get a Level 10 Disarray debuff"
                    id="UNIQUE_UNLOCK_SKIN_ARMORED_HORSE_T5_GUILD_NON_TRADABLE"
                    title="Armored Horse Skin: Expert's Guild Warhorse"
                  />
                  <Entry
                    reward={reward}
                    name="Be part of a player kill with 19 or more assists"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Be part of a battle with at least 40 player deaths"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Kill or assist in killing 20 players within one minute"
                    id="T1_KILL_EMOTE_FLAG_CHARGES_NONTRADABLE"
                    title="Guild Banner Victory Emote Charge (x40)"
                  />
                  <Entry
                    reward={reward}
                    name="Gain 300,000 Kill Fame from kills with 10 or more assists"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Get a Level 20 Disarray debuff"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Be part of a battle with at least 60 player deaths"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Kill or assist in killing 30 players within one minute"
                    id="T1_KILL_EMOTE_HELLGATE_CHARGES_NONTRADABLE"
                    title="Hellgate Victory Emote Charge (x100)"
                  />
                  <Entry
                    reward={reward}
                    name="Get a Level 30 Disarray debuff"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Gain a million Kill Fame from kills with 10 or more assists"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Be part of a battle with at least 85 player deaths"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Get a Level 40 Disarray debuff"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Be part of a battle with at least 120 player deaths"
                    id="T1_KILL_EMOTE_TOMBSTONE_CHARGES_NONTRADABLE"
                    title="Tombstone Victory Emote Charge (x100)"
                  />
                  <Entry
                    reward={reward}
                    name="Kill or assist in killing 50 players within one minute"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Gain 3 million Kill Fame from kills with 10 or more assists"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Be part of a battle with at least 150 player deaths"
                    id="T1_KILL_EMOTE_SWORD_CHARGES_NONTRADABLE"
                    title="Sword Victory Emote Charge (x700)"
                  />
                  <Entry
                    reward={reward}
                    name="Gain 10 million Kill Fame from kills with 10 or more assists"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Gain 30 million Kill Fame from kills with 10 or more assists"
                    id="T1_KILL_EMOTE_GHOST_CHARGES_NONTRADABLE"
                    title="Ghost Victory Emote Charge (x700)"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Claim a Territory with your Guild"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Successfully transport a Power Crystal to a Territory"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat the Sentry Mage in an enemy territory"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Deal 5,000 damage to enemy Fortifications"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 4 Siphoning Mages"
                    id="T1_KILL_EMOTE_OVERGROWN_CHARGES_NONTRADABLE"
                    title="Overgrown Victory Emote Charge (x20)"
                  />
                  <Entry
                    reward={reward}
                    name="Transport a Substantial Power Crystal to a Territory"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Deliver 300 Raw Energy to a Territory"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Have every Fortification on your Territory upgraded to Tier 4"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Deal 3,000 damage to Fortification Gates"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Deliver 2,000 Raw Energy to a Territory"
                    id="T6_SILVERBAG_NONTRADABLE"
                    title="Master's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Participate in a successful attack on a territory"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Participate in 10 Raids"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Have every Fortification on your Territory upgraded to Tier 6"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Help open the gate of an enemy territory from within"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Transport an Extraordinary Power Crystal to a Territory"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 30 Siphoning Mages"
                    id="T7_SILVERBAG_NONTRADABLE"
                    title="Grandmaster's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Use a Siege Banner on an enemy Territory"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Participate in 30 Raids"
                    id="T1_KILL_EMOTE_TOMBSTONE_CHARGES_NONTRADABLE"
                    title="Tombstone Victory Emote Charge (x40)"
                  />
                  <Entry
                    reward={reward}
                    name="Transport an Overwhelming Power Crystal to a Territory"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Deliver 10,000 Raw Energy to a Territory"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Participate in 10 successful attacks on a Territory"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Enter a fully upgraded territory that's owned by your guild"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Deal 20,000 damage to Tier 6 or higher Fortifications"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 100 Siphoning Mages"
                    id="T8_SILVERBAG_NONTRADABLE"
                    title="Elder's Bag of Silver"
                  />
                  <Entry
                    reward={reward}
                    name="Participate in 100 Raids"
                    id="T1_KILL_EMOTE_SWORD_CHARGES_NONTRADABLE"
                    title="Sword Victory Emote Charge (x100)"
                  />
                  <Entry
                    reward={reward}
                    name="Deal 50,000 damage to Tier 8 Fortifications"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Participate in 30 successful attacks on a Territory"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight (x2)"
                  />
                  <Entry
                    reward={reward}
                    name="Deal 20000 damage to Tier 8 Fortification Gates"
                    id="T1_KILL_EMOTE_FLAG_CHARGES_NONTRADABLE"
                    title="Guild Banner Victory Emote Charge (x700)"
                  />
                  <Entry
                    reward={reward}
                    name="Deliver 30 Overwhelming Territory Power Crystals"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x100)"
                  />
                  <Entry
                    reward={reward}
                    name="Participate in 100 successful attacks on a Territory"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight (x5)"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Earn 100 Season Points with your Guild"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Earn 300 Season Points with your Guild"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Earn 1,000 Season Points with your Guild"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Earn 2,500 Season Points with your Guild"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Earn 5,000 Season Points with your Guild"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Earn 10,000 Season Points with your Guild"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Earn 20,000 Season Points with your Guild"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Earn 40,000 Season Points with your Guild"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Earn 65,000 Season Points with your Guild"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Earn 100,000 Season Points with your Guild"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Earn 140,000 Season Points with your Guild"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Earn 200,000 Season Points with your Guild"
                    id="T5_LEARNINGPOINTS_NONTRADABLE"
                    title="Expert's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Earn the Iron Bracket Guild Season Reward or higher"
                    id="T4_SHARD_CRYSTAL"
                    title="Adept's Crystal Shard (x10)"
                  />
                  <Entry
                    reward={reward}
                    name="Earn the Bronze Bracket Guild Season Reward or higher"
                    id="T4_SHARD_CRYSTAL"
                    title="Adept's Crystal Shard (x20)"
                  />
                  <Entry
                    reward={reward}
                    name="Earn the Silver Bracket Guild Season Reward or higher"
                    id="T5_SHARD_CRYSTAL"
                    title="Expert's Crystal Shard (x20)"
                  />
                  <Entry
                    reward={reward}
                    name="Earn the Gold Bracket Guild Season Reward or higher"
                    id="T5_SHARD_CRYSTAL"
                    title="Expert's Crystal Shard (x30)"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Get your very own island"
                    id="PLAYERISLAND_FURNITUREITEM_STONE_WELL_A"
                    title="Stone well"
                  />
                  <Entry
                    reward={reward}
                    name="Upgrade your Personal Island to level 2"
                    id="T5_FOCUSPOTION_NONTRADABLE"
                    title="Expert's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Place 3 decoration items on one of your islands"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Upgrade your Personal Island to level 3"
                    id="T6_FOCUSPOTION_NONTRADABLE"
                    title="Master's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Place 10 decoration items on one of your islands"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Upgrade your Personal Island to level 4"
                    id="T4_SKILLBOOK_GATHER_ORE_NONTRADABLE"
                    title="Adept Ore Miner Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Be on your Player Island with another player"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Upgrade your Personal Island to level 5"
                    id="UNIQUE_FOCUSPOTION_ADC_NONTRADABLE_01"
                    title="Grandmaster's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Be on a Player Island with 2 other players"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x10)"
                  />
                  <Entry
                    reward={reward}
                    name="Upgrade your island to the maximum of 6/6"
                    id="T5_SKILLBOOK_GATHER_ORE_NONTRADABLE"
                    title="Expert Ore Miner Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Place 30 decoration items on one of your islands"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Place an Army Crate on your island"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Visit Personal Islands in 3 different Biomes"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x10)"
                  />
                  <Entry
                    reward={reward}
                    name="Be on a Player Island with 4 other players"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Own 2 Personal Islands simultaneously"
                    id="T6_SKILLBOOK_GATHER_ORE_NONTRADABLE"
                    title="Master Ore Miner Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Visit Personal Islands in 5 different Biomes"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Visit islands in every biome"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x20)"
                  />
                  <Entry
                    reward={reward}
                    name="Own 3 Personal Islands at level 3 or higher"
                    id="T7_SKILLBOOK_GATHER_ORE_NONTRADABLE"
                    title="Grandmaster Ore Miner Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Own 5 Personal Islands at level 4 or higher"
                    id="T8_SKILLBOOK_GATHER_ORE_NONTRADABLE"
                    title="Elder Ore Miner Tome"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Build a house on your island"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Place a Tier 2 Chest in your House"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Upgrade your House to Tier 3"
                    id="T4_FOCUSPOTION_NONTRADABLE"
                    title="Adept's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Place 3 furniture items in your House"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Employ any kind of Laborer"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Invest a total of 3,500 Item Value worth of resources into buildings"
                    id="T4_SKILLBOOK_GATHER_ROCK_NONTRADABLE"
                    title="Adept Quarrier Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Upgrade your House to Tier 4"
                    id="T5_FOCUSPOTION_NONTRADABLE"
                    title="Expert's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Build or upgrade a Farming Building to Tier 3"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Upgrade 2 different Farm Buildings to Tier 3"
                    id="T4_SKILLBOOK_GATHER_WOOD_NONTRADABLE"
                    title="Adept Lumberjack Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Invest a total of 15,000 Item Value worth of resources into buildings"
                    id="PLAYERISLAND_FURNITUREITEM_WOOD_LANTERN_A"
                    title="Simple lantern"
                  />
                  <Entry
                    reward={reward}
                    name="Upgrade your House to Tier 5"
                    id="T5_FOCUSPOTION_NONTRADABLE"
                    title="Expert's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Send a Laborer on a mission with 100% Yield from Happiness"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x15)"
                  />
                  <Entry
                    reward={reward}
                    name="Upgrade an Economy Building to Tier 4"
                    id="T5_SKILLBOOK_GATHER_ROCK_NONTRADABLE"
                    title="Expert Quarrier Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Invest a total of 30,000 Item Value worth of resources into buildings"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Upgrade your House to Tier 6"
                    id="T6_FOCUSPOTION_NONTRADABLE"
                    title="Master's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Upgrade a Farming Building to Tier 5"
                    id="T5_SKILLBOOK_GATHER_WOOD_NONTRADABLE"
                    title="Expert Lumberjack Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Upgrade your House to Tier 7"
                    id="T6_FOCUSPOTION_NONTRADABLE"
                    title="Master's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Upgrade an Economy Building to Tier 6"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Invest a total of 140,000 Item Value worth of resources into Buildings"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Upgrade a house on your island to Tier 8"
                    id="T6_SKILLBOOK_GATHER_ROCK_NONTRADABLE"
                    title="Master Quarrier Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Have a Tier 8 Laborer and send them on a mission"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Upgrade a Military Building to Tier 6"
                    id="T6_SKILLBOOK_GATHER_WOOD_NONTRADABLE"
                    title="Master Lumberjack Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Upgrade an Economy Building to Tier 8"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Upgrade a Farming Building to Tier 8"
                    id="T7_SKILLBOOK_GATHER_WOOD_NONTRADABLE"
                    title="Grandmaster Lumberjack Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Upgrade a Military Building to Tier 8"
                    id="T7_SKILLBOOK_GATHER_ROCK_NONTRADABLE"
                    title="Grandmaster Quarrier Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Send a Tier 8 Laborer with maxed Happiness on a mission"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Upgrade every Farming Building to Tier 8 at least once"
                    id="T8_SKILLBOOK_GATHER_WOOD_NONTRADABLE"
                    title="Elder Lumberjack Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Upgrade every Economy Building to Tier 8 at least once"
                    id="UNIQUE_FOCUSPOTION_ADC_NONTRADABLE_01"
                    title="Grandmaster's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Upgrade every Military Building to Tier 8 at least once"
                    id="T8_SKILLBOOK_GATHER_ROCK_NONTRADABLE"
                    title="Elder Quarrier Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Invest a total of 500,000 Item Value worth of resources into buildings"
                    id="T8_FOCUSPOTION_NONTRADABLE"
                    title="Elder's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Invest a total of 1 million Item Value worth of resources into buildings"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Build a Farm on your island"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Farm your first crop"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Harvest 70 Wheat"
                    id="T3_FOCUSPOTION_NONTRADABLE"
                    title="Journeyman's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Water 20 Crops or Herbs"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Farm Crops worth 5,000 Fame"
                    id="T4_SKILLBOOK_GATHER_FIBER_NONTRADABLE"
                    title="Adept Fiber Harvester Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Harvest 140 Cabbages"
                    id="T3_FOCUSPOTION_NONTRADABLE"
                    title="Journeyman's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Farm Crops worth 12,000 Fame"
                    id="T4_FOCUSPOTION_NONTRADABLE"
                    title="Adept's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Build a Herb Garden"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Harvest 70 Herbs"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Harvest 150 Crops or Herbs with a local Yield Bonus"
                    id="T4_FOCUSPOTION_NONTRADABLE"
                    title="Adept's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Harvest 100 of each of 8 different types of Crops or Herbs"
                    id="T5_SKILLBOOK_GATHER_FIBER_NONTRADABLE"
                    title="Expert Fiber Harvester Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Farm Crops and Herbs worth 36,000 Fame"
                    id="T5_FOCUSPOTION_NONTRADABLE"
                    title="Expert's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Harvest 150 Crops or Herbs in 10 minutes on a single island"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Harvest 3,000 Crops or Herbs"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Harvest 160 Elusive Foxgloves"
                    id="T5_FOCUSPOTION_NONTRADABLE"
                    title="Expert's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Harvest 450 Crops or Herbs in 10 minutes on a single island"
                    id="T6_SKILLBOOK_GATHER_FIBER_NONTRADABLE"
                    title="Master Fiber Harvester Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Harvest 4,500 Crops or Herbs"
                    id="T5_FOCUSPOTION_NONTRADABLE"
                    title="Expert's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Harvest 200 Tier 7 Crops or Herbs"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x10)"
                  />
                  <Entry
                    reward={reward}
                    name="Harvest 700 Crops or Herbs in 10 minutes on a single island"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Harvest 400 of each of 12 different types of Crops or Herbs"
                    id="T5_FOCUSPOTION_NONTRADABLE"
                    title="Expert's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Harvest 1,000 Crops or Herbs in 10 minutes on a single island"
                    id="T7_SKILLBOOK_GATHER_FIBER_NONTRADABLE"
                    title="Grandmaster Fiber Harvester Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Harvest 1,200 Crops or Herbs in 10 minutes on a single island"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Harvest 1,400 Crops in 10 minutes on a single island"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x25)"
                  />
                  <Entry
                    reward={reward}
                    name="Harvest 1,400 Herbs in 10 minutes on a single island"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x25)"
                  />
                  <Entry
                    reward={reward}
                    name="Farm crops worth 100,000 Fame"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Farm Crops worth 300,000 Fame"
                    id="T5_FOCUSPOTION_NONTRADABLE"
                    title="Expert's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Harvest 500 of each of every different type of Crop and Herb"
                    id="T6_FOCUSPOTION_NONTRADABLE"
                    title="Master's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Farm crops worth 1,000,000 Fame"
                    id="T8_SKILLBOOK_GATHER_FIBER_NONTRADABLE"
                    title="Elder Fiber Harvester Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Farm Crops worth 3,000,000 Fame"
                    id="T6_FOCUSPOTION_NONTRADABLE"
                    title="Master's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Harvest 1,000 Crops on an Outlands Farming Territory"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Harvest 3,000 Crops on an Outlands Farming Territory"
                    id="T5_FOCUSPOTION_NONTRADABLE"
                    title="Expert's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Raise a horse"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Saddle a Horse"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Raise 10 animals"
                    id="T3_FOCUSPOTION_NONTRADABLE"
                    title="Journeyman's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Collect 30 Eggs from Chickens"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Produce 100 Meat at the Butcher"
                    id="UNIQUE_FURNITUREITEM_ADC_RUG_WOLF"
                    title="Wolf Rug"
                  />
                  <Entry
                    reward={reward}
                    name="Raise 3 different types of animals"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x10)"
                  />
                  <Entry
                    reward={reward}
                    name="Saddle 5 Mounts"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Raise 6 different types of animals"
                    id="T4_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                    title="Adept Animal Skinner Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Raise a Fawn into a Giant Stag"
                    id="T4_FOCUSPOTION_NONTRADABLE"
                    title="Adept's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Build a Kennel on your island"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Raise a Swiftclaw"
                    id="T5_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                    title="Expert Animal Skinner Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Raise a Faction Warfare Mount"
                    id="T4_FOCUSPOTION_NONTRADABLE"
                    title="Adept's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Raise 10 different types of animals"
                    id="T5_FOCUSPOTION_NONTRADABLE"
                    title="Expert's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Collect milk from farm animals 100 times"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Raise 15 different types of animals"
                    id="T6_FOCUSPOTION_NONTRADABLE"
                    title="Master's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Raise a Direwolf"
                    id="UNIQUE_FURNITUREITEM_ADC_STATUE_MOUNTED_DIREWOLF_A"
                    title="Wolf Rider Statue (L)"
                  />
                  <Entry
                    reward={reward}
                    name="Have offspring from 10 different types of animals"
                    id="T6_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                    title="Master Animal Skinner Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Raise 21 different types of animals"
                    id="T6_FOCUSPOTION_NONTRADABLE"
                    title="Master's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Collect 350 Eggs in 10 minutes on a single island"
                    id="UNIQUE_UNLOCK_OFF_VANITY_PIRATE_RED_NON_TRADABLE"
                    title="Wardrobe Skin: Navigator's Red Parrot Cage"
                  />
                  <Entry
                    reward={reward}
                    name="Have offspring from 16 different types of animals"
                    id="T6_FOCUSPOTION_NONTRADABLE"
                    title="Master's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Have 2 offspring from a single horse"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Produce 2,000 Meat at the Butcher"
                    id="T7_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                    title="Grandmaster Animal Skinner Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Collect 900 Eggs in 10 minutes on a single island"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x20)"
                  />
                  <Entry
                    reward={reward}
                    name="Raise a Tier 7 Mount"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Raise 28 different types of animals"
                    id="UNIQUE_FOCUSPOTION_ADC_NONTRADABLE_01"
                    title="Grandmaster's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Have Offspring from 21 different types of animals"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Raise a Faction Warfare Elite Mount"
                    id="T8_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                    title="Elder Animal Skinner Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Raise 35 different types of animals"
                    id="UNIQUE_FOCUSPOTION_ADC_NONTRADABLE_01"
                    title="Grandmaster's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Raise a Mammoth"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x30)"
                  />
                  <Entry
                    reward={reward}
                    name="Raise all different types of animals"
                    id="T8_FOCUSPOTION_NONTRADABLE"
                    title="Elder's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Collect the offspring of a Mammoth"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Create 20 Carrot Soups"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Create 5 Simple Fish Baits"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Create 10 Bean Salads"
                    id="T3_FOCUSPOTION_NONTRADABLE"
                    title="Journeyman's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Create 30 Chopped Fish at the Butcher building"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Create 5 Clam Soups"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Create 30 Omelettes"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x10)"
                  />
                  <Entry
                    reward={reward}
                    name="Create 40 Roast Chicken"
                    id="T4_FOCUSPOTION_NONTRADABLE"
                    title="Adept's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Create 150 Chopped Fish at the Butcher building"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Create 10 Goat Butter at a Mill building"
                    id="T4_SKILLBOOK_GATHER_WOOD_NONTRADABLE"
                    title="Adept Lumberjack Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Create 50 Sandwiches"
                    id="T4_FOCUSPOTION_NONTRADABLE"
                    title="Adept's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Create 9 Basic Fish Sauces"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Create a Food item with Enchantment Level 1"
                    id="T4_SKILLBOOK_GATHER_ROCK_NONTRADABLE"
                    title="Adept Quarrier Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Create 40 Goose Omelettes"
                    id="T5_FOCUSPOTION_NONTRADABLE"
                    title="Expert's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Create an Avalonian Goat Stew"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x10)"
                  />
                  <Entry
                    reward={reward}
                    name="Create every Tier 4 Food item"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Create 20 Food items with Enchantment Level 2"
                    id="T5_SKILLBOOK_GATHER_ORE_NONTRADABLE"
                    title="Expert Ore Miner Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Create every Tier 5 Food item"
                    id="T5_FOCUSPOTION_NONTRADABLE"
                    title="Expert's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Create 50 Potato Salads"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x20)"
                  />
                  <Entry
                    reward={reward}
                    name="Create every Tier 6 Food item"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Create 40 Food items with Enchantment Level 3"
                    id="T5_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                    title="Expert Animal Skinner Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Create 100 Food items using the Local Production Bonus"
                    id="UNIQUE_UNLOCK_ARMOR_VANITY_INNKEEPER_NON_TRADABLE"
                    title="Wardrobe Skin: Innkeeper's Shirt"
                  />
                  <Entry
                    reward={reward}
                    name="Create 250 Tier 7 Food items"
                    id="T5_SKILLBOOK_GATHER_FIBER_NONTRADABLE"
                    title="Expert Fiber Harvester Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Create every Tier 7 Food item"
                    id="T5_FOCUSPOTION_NONTRADABLE"
                    title="Expert's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Create 250 Tier 7.3 Food items"
                    id="UNIQUE_FURNITUREITEM_XMAS_FILL_CITY_TREE_A"
                    title="Decorated Pine Tree"
                  />
                  <Entry
                    reward={reward}
                    name="Create 250 Tier 7 Food items with Fish"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Create every type of Food item"
                    id="T6_FOCUSPOTION_NONTRADABLE"
                    title="Master's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Create 100 Tier 7.3 or Tier 8.3 Avalonian Food items"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Create 1,000 Tier 8 Food items using the Local Production Bonus"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x25)"
                  />
                  <Entry
                    reward={reward}
                    name="Create 1,000 Tier 7.3 or Tier 8.3 Food items"
                    id="T6_FOCUSPOTION_NONTRADABLE"
                    title="Master's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Create 10,000 Tier 7 or Tier 8 Fish Food items"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x60)"
                  />
                  <Entry
                    reward={reward}
                    name="Create 10,000 Tier 7.3 or Tier 8.3 Food items"
                    id="UNIQUE_FOCUSPOTION_ADC_NONTRADABLE_01"
                    title="Grandmaster's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Create 10 Healing Potions"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Create 15 Gigantify Potions"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Create 25 Tier 2 Potions"
                    id="T3_FOCUSPOTION_NONTRADABLE"
                    title="Journeyman's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Create 10 Minor Cleansing Potions"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Create 75 Potions"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Create every Tier 3 Potion"
                    id="T4_SKILLBOOK_GATHER_FIBER_NONTRADABLE"
                    title="Adept Fiber Harvester Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Create 20 Poison Potions"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Create 10 Gathering Potions"
                    id="T4_FOCUSPOTION_NONTRADABLE"
                    title="Adept's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Create 20 Tier 4 Healing Potions"
                    id="T4_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                    title="Adept Animal Skinner Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Create 10 Hellfire Potions"
                    id="UNIQUE_FURNITUREITEM_MORGANA_CAMPFIRE_D@2"
                    title="Cauldron (Disciples of Morgana)"
                  />
                  <Entry
                    reward={reward}
                    name="Create 15 Basic Arcane Extracts"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Create 10 Potions with Enchantment Level 1"
                    id="T4_SKILLBOOK_GATHER_ORE_NONTRADABLE"
                    title="Adept Ore Miner Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Create every Tier 4 Potion"
                    id="T4_FOCUSPOTION_NONTRADABLE"
                    title="Adept's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Create 40 Tier 5 Potions"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x15)"
                  />
                  <Entry
                    reward={reward}
                    name="Create 50 Potions with Enchantment Level 2"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Create 80 Potato Schnapps"
                    id="T5_FOCUSPOTION_NONTRADABLE"
                    title="Expert's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Create 20 Major Energy Potions"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Create 100 Potions with Enchantment Level 3"
                    id="T5_SKILLBOOK_GATHER_ROCK_NONTRADABLE"
                    title="Expert Quarrier Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Create every Tier 5 and Tier 6 Potion"
                    id="T5_FOCUSPOTION_NONTRADABLE"
                    title="Expert's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Create 500 Potions"
                    id="T5_SKILLBOOK_GATHER_WOOD_NONTRADABLE"
                    title="Expert Lumberjack Tome"
                  />
                  <Entry
                    reward={reward}
                    name="Create 100 Potions using the Local Production Bonus"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Create 1,000 Potions"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Create every type of Potion at least once"
                    id="T6_FOCUSPOTION_NONTRADABLE"
                    title="Master's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Create 100 Tier 7.3 or Tier 8.3 Potions"
                    id="T6_FOCUSPOTION_NONTRADABLE"
                    title="Master's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Create 1,000 Potions with Enchantment Level 3"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Create 3,000 Major Potions"
                    id="T6_FOCUSPOTION_NONTRADABLE"
                    title="Master's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
                    name="Create 10,000 Major Potions"
                    id="T6_FOCUSPOTION_NONTRADABLE"
                    title="Master's Focus Restoration Potion"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Visit a Guild Island"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Have a Guild Hall on your Guild's Island"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Visit a Level 3 Guild Island"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Have a Guild Hall on your Guild's Island upgraded to Tier 4"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Visit a Level 6 Guild Island"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Have a Guild Hall on your Guild's Island upgraded to Tier 8"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Place 100 decorations on one of your Guild's Islands"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x5)"
                  />
                  <Entry
                    reward={reward}
                    name="Earn 100,000 Silver on the Guild Marketplace"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Earn a million Silver on the Guild Marketplace"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Spend 100,000 silver on the Guild Marketplace"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Spend a million Silver on the Guild Marketplace"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Be on a Guild Island with 5 players at the same time"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Be on a Guild Island with 10 players at the same time"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Be on a Guild Island with 20 players at the same time"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Visit Guild Islands in every biome"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x15)"
                  />
                  <Entry
                    reward={reward}
                    name="Be on a Guild Island with 50 players at the same time"
                    id="UNIQUE_TOKEN_COMMUNITY"
                    title="Community Token (x40)"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Defeat 25 Miners"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 25 Scavengers"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 25 Gatherers"
                    id="T4_SKILLBOOK_NONTRADABLE"
                    title="Adept's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Lumberjack or Chopper"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 500 Foul Rats"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 15 Screamers"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Foreman"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 3 Overseers"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 50 Thieves or Cutthroats"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Thug or Rouser"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 50 Poachers"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Trapper"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 50 Shooters"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 50 Firestarters or Arsonists"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Pyromaniac"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 25 Bouncers or Goons"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Muscle or Bruiser"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 50 Brawlers"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Spencer"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Roughneck or Chops"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 25 Mortars"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 5 Cannoneers"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Trapmaster or Weaponsmaster"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 50 Hermits, Quacks, Healers, or Wisemen"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Fishy"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Mad Fuzzy or Chief Blaster"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Shadowmask"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 100 Heretics"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 300 Heretics"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 1,000 Heretics"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 3,000 Heretics"
                    id="T4_CAPEITEM_HERETIC_BP"
                    title="Adept's Heretic Crest"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 10,000 Heretics"
                    id="T6_CAPEITEM_HERETIC_BP"
                    title="Master's Heretic Crest"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Defeat 150 Frail or Brittle Skeletons"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 25 Fragmenters"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 5 Scorpions"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 100 Swordsmen or Revenants"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Swordmaster or Paragon"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 100 Frostweavers or Deathmongers"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Deathmaster"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Deathlord"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Necromancer or Cryomancer"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 75 Archers"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Marksman or Sharpshooter"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Forgotten Champion"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 75 Ghouls"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Lacedon or Ghast"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 25 Possessed Sculptures"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 15 Shades"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 250 Rats"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 100 Bats"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 100 Ghosts"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Banshee"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 50 Knights, Dreadknights, or Animated Armors"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Marshal"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any General"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Hero"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Reaper or Harvester"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 100 Undead"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 300 Undead"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 1,000 Undead"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 3,000 Undead"
                    id="T4_CAPEITEM_UNDEAD_BP"
                    title="Adept's Undead Crest"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 10,000 Undead"
                    id="T6_CAPEITEM_UNDEAD_BP"
                    title="Master's Undead Crest"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Defeat 10 Rock Elementals"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 10 Living Roots"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 50 Berserkers or Wildlings"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Warrior or Brave"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Patriarch or Chieftain"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 50 Huntress, Knifelings, or Axe-Throwers"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Pack Leader or Axe-Maiden"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Axe-Maiden"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 75 Giants"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Athos, Graybeard, or Hulk"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Ancient Athos, Ancient, or Mountain"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 75 Druids, Sharpeyes, Stormbringers, or Adepts"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Elder or Sage"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Elder, Evoker, Savant, or Archdruid"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 150 Keeper Bears"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 50 Cultivators"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Shaman"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 50 Earthchilds or Shamans"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Earthdaughter"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Earthmother, Earth Aspirant, or Great Mother"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 100 Keepers"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 300 Keepers"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 1,000 Keepers"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 3,000 Keepers"
                    id="T4_CAPEITEM_KEEPER_BP"
                    title="Adept's Keeper Crest"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 10,000 Keepers"
                    id="T6_CAPEITEM_KEEPER_BP"
                    title="Master's Keeper Crest"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Defeat 100 Bats"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 150 Guard Dogs or White Hounds"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 125 Tomes"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 50 Pikemen or Footmen"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Lieutenants or Enforcers"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Commander of the Guard"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 100 Squires or Suppressors"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Marksman or Suppression Squad Leader"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Master of Suppression"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 100 Acolytes or Occultists"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Ritual Leader or Aspirant"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Magistra, Raven, Fang, Prioress, or Mistress of Demons"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 50 Knights, Paladins, or Champions"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Honoured, Chosen, or Archfiend"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 75 Conjurers"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 75 Sorceresses or Infestors"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Favored Sorceress"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Mistress of Magic"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 30 Ravens"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 50 Molten Demons or Spiked Demons"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Tormentor or Jailer"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Demon Prince, Prince of Morgana, or Demon General"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 100 Disciples of Morgana"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 300 Disciples of Morgana"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 1,000 Disciples of Morgana"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeatl 3,000 Disciples of Morgana"
                    id="T4_CAPEITEM_MORGANA_BP"
                    title="Adept's Morgana Crest"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 10,000 Disciples of Morgana"
                    id="T6_CAPEITEM_MORGANA_BP"
                    title="Master's Morgana Crest"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Defeat 50 Imps"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 25 Spiked Demons"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 10 Slavers"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 50 Maulers"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 25 Sorcerers"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Warlock"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 25 Berserkers"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Harbinger"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Horror or Trapped Demon"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Underlord"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 75 Demented Heretic Thieves"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 100 Enthralled Heretic Mages"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 125 Deranged Heretic Arbalists"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 150 Bewildered Heretic Brawlers"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 100 Demons"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 300 Demons"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 1,000 Demons"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 3,000 Demons"
                    id="T4_CAPEITEM_DEMON_BP"
                    title="Adept's Demon Crest"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 10,000 Demons"
                    id="T6_CAPEITEM_DEMON_BP"
                    title="Master's Demon Crest"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Defeat 250 Drones"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 15 Assemblers"
                    id="T5_SKILLBOOK_NONTRADABLE"
                    title="Expert's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 15 Foci"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 15 Winged Guards"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 100 Lancers or Spearmen"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 50 Initiates or Monks"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 20 Hunters or Rangers"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Archer"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 50 Wizards or Magi"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 50 Acolytes"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 15 Priestess"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any High Priestess"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 50 Mages, Keen Mages, or Spellweavers"
                    id="T6_SKILLBOOK_NONTRADABLE"
                    title="Master's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Great Mage or Spellweaver"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Great Mage or Archmage"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 25 Warriors"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 15 Knights"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Construct"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Crystal Basilisk"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Knight Captain"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat Sir Bedivere"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Treasure Drone"
                    id="T3_SKILLBOOK_NONTRADABLE"
                    title="Journeyman's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 100 Avalonians"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 250 Avalonians"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 1,000 Avalonians"
                    id="T4_LEARNINGPOINTS_NONTRADABLE"
                    title="Adept's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 2,500 Avalonians"
                    id="T4_CAPEITEM_AVALON_BP"
                    title="Adept's Avalonian Crest"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 10,000 Avalonians"
                    id="T6_CAPEITEM_AVALON_BP"
                    title="Master's Avalonian Crest"
                  />
                  <Entry
                    reward={reward}
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
                    reward={reward}
                    name="Defeat any Shadow Panther"
                    id="T3_ALCHEMY_RARE_PANTHER"
                    title="Rugged Shadow Claws (x2)"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Sylvian"
                    id="T3_ALCHEMY_RARE_ENT"
                    title="Rugged Sylvian Root (x2)"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Spirit Bear"
                    id="T3_ALCHEMY_RARE_DIREBEAR"
                    title="Rugged Spirit Paws (x2)"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Werewolf"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Hellfire Imp"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Runestone Golem"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Dawnbird"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Crystal Spider"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Crystal Beetle"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Crystal Cobra"
                    id="T8_SKILLBOOK_NONTRADABLE"
                    title="Elder's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 5 Arcane Spiderlings"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Veilweaver"
                    id="T4_ARTEFACT_ARMOR_PLATE_FEY"
                    title="Adept's Veilweaver Carapace"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Griffin"
                    id="T4_ARTEFACT_ARMOR_LEATHER_FEY"
                    title="Adept's Untarnished Griffin Feathers"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Fey Dragon"
                    id="T4_ARTEFACT_ARMOR_CLOTH_FEY"
                    title="Adept's Fey Dorsal Wing"
                  />
                  <Entry
                    reward={reward}
                    name="Kill any Colossus in a Randomized Dungeon"
                    id="T2_LEARNINGPOINTS_NONTRADABLE"
                    title="Novice's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Kill any Titan in a Randomized Dungeon"
                    id="T3_LEARNINGPOINTS_NONTRADABLE"
                    title="Journeyman's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat 10 Vengeful Guardians"
                    id="T7_SKILLBOOK_NONTRADABLE"
                    title="Grandmaster's Tome of Insight"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat any Vengeful Guardian Lord"
                    id="T5_LEARNINGPOINTS_NONTRADABLE"
                    title="Expert's Tome of Learning"
                  />
                  <Entry
                    reward={reward}
                    name="Defeat Uncle Frost"
                    id="UNIQUE_FURNITUREITEM_XMAS_PRESENT"
                    title="Present Box"
                  />
                  <Entry
                    reward={reward}
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
    </div>
  );
};
```
