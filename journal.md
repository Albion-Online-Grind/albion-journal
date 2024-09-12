```tsx
const Journal = () => {
  return (
    <div>
      {/* PvE Activities */}
      <Section>
        <UncontrolledAccordion id="pve">
          <AccordionItem>
            <AccordionHeader targetId="pve">
              PvE Activities (190)
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
                  <tr>
                    <td>Finish a T3 Solo Expedition</td>
                    <Reward
                      id="T3_SILVERBAG_NONTRADABLE"
                      title="Journeyman's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Finish a Tier 4 Solo Expedition</td>
                    <Reward
                      id="T4_SILVERBAG_NONTRADABLE"
                      title="Adept's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Finish a Tier 4 Group Expedition</td>
                    <Reward
                      id="T5_SILVERBAG_NONTRADABLE"
                      title="Expert's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Finish a Tier 5 Solo Expedition</td>
                    <Reward
                      id="T5_SILVERBAG_NONTRADABLE"
                      title="Expert's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Finish a Tier 5 Group Expedition</td>
                    <Reward
                      id="T3_LEARNINGPOINTS_NONTRADABLE"
                      title="Journeyman's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Finish a Tier 6 Group Expedition</td>
                    <Reward
                      id="T5_SILVERBAG_NONTRADABLE"
                      title="Expert's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>
                      Finish every non-hardcore Expedition
                      <br />
                      <span className="text-muted">
                        Curious Excavation, Preaching to the Dead, Fishy
                        Business, Stone Wars, Lumber Lunacy, Lurking Underneath,
                        Fungicide, Three Sisters, Fistful of Silver, Eternal
                        Battle, In the Raven&apos;s Claws
                      </span>
                    </td>
                    <Reward
                      id="QUESTITEM_EXP_TOKEN_D1_T6_EXP_HRD_HERETIC_LUMBERCAMP"
                      title="Map (Lvl. 1) - Lumber Lunacy"
                    />
                  </tr>
                  <tr>
                    <td>Finish a T5 Solo Expedition within 7 minutes</td>
                    <Reward
                      id="T4_SKILLBOOK_NONTRADABLE"
                      title="Adept's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Finish a T6 Group Expedition within 10 minutes</td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Finish a T5 Solo Expedition within 5 minutes</td>
                    <Reward
                      id="T6_SKILLBOOK_NONTRADABLE"
                      title="Master's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Finish any Hardcore Expedition</td>
                    <Reward
                      id="T4_LEARNINGPOINTS_NONTRADABLE"
                      title="Adept's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Finish a Level 4 Hardcore Expedition</td>
                    <Reward
                      id="T7_SKILLBOOK_NONTRADABLE"
                      title="Grandmaster's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Finish a Level 8 Hardcore Expedition</td>
                    <Reward
                      id="T8_SKILLBOOK_NONTRADABLE"
                      title="Elder's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Finish a Level 12 Hardcore Expedition</td>
                    <Reward
                      id="UNIQUE_REPAIRPOWDER_ADC_GENERAL_01_NONTRADEABLE"
                      title="Scroll of Repair"
                    />
                  </tr>
                  <tr>
                    <td>Finish a Level 18 Hardcore Expedition</td>
                    <Reward
                      id="UNIQUE_REPAIRPOWDER_ADC_GENERAL_01_NONTRADEABLE"
                      title="Scroll of Repair"
                    />
                  </tr>
                  <tr>
                    <td>
                      Finish a Level 18 Hardcore Expedition within 10 minutes
                    </td>
                    <Reward
                      id="UNIQUE_REPAIRPOWDER_ADC_GENERAL_01_NONTRADEABLE"
                      title="Scroll of Repair (x2)"
                    />
                  </tr>
                  <tr>
                    <td>Finish 5 different Level 18 Hardcore Expeditions</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x5)"
                    />
                  </tr>
                  <tr>
                    <td>
                      Finish every Hardcore Expedition on Level 18
                      <br />
                      <span className="text-muted">
                        Preaching to the Dead, Fishy Business, Stone Wars,
                        Lumber Lunacy, Lurking Underneath, Fungicide, Three
                        Sisters, Fistful of Silver, Eternal Battle, In the
                        Raven&apos;s Claws
                      </span>
                    </td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x10)"
                    />
                  </tr>
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
                  <tr>
                    <td>Finish a T3 Solo Dungeon</td>
                    <Reward id="T1_MEAL_SOUP" title="Carrot Soup" />
                  </tr>
                  <tr>
                    <td>Finish a Tier 4 Solo Dungeon</td>
                    <Reward
                      id="T4_SKILLBOOK_NONTRADABLE"
                      title="Adept's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Finish a Solo Dungeon of every Faction</td>
                    <Reward
                      id="T5_SILVERBAG_NONTRADABLE"
                      title="Expert's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Unlock 10 chests in Solo Dungeons</td>
                    <Reward
                      id="T5_RANDOM_DUNGEON_SOLO_TOKEN_1"
                      title="Expert's Dungeon Map (Solo)"
                    />
                  </tr>
                  <tr>
                    <td>Finish a Tier 5 Solo Dungeon</td>
                    <Reward
                      id="T3_LEARNINGPOINTS_NONTRADABLE"
                      title="Journeyman's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Finish 3 Solo Dungeons with a Map</td>
                    <Reward
                      id="T6_SILVERBAG_NONTRADABLE"
                      title="Master's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>
                      Finish an enchanted Solo Dungeon without using a map
                    </td>
                    <Reward
                      id="T6_SILVERBAG_NONTRADABLE"
                      title="Master's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Unlock 30 chests in Solo Dungeons</td>
                    <Reward
                      id="T4_RANDOM_DUNGEON_TOKEN_1"
                      title="Adept's Dungeon Map (Group)"
                    />
                  </tr>
                  <tr>
                    <td>Finish an Enchantment Level 2 Solo Dungeon</td>
                    <Reward
                      id="T5_SILVERBAG_NONTRADABLE"
                      title="Expert's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Finish an Enchantment Level 3 Solo Dungeon</td>
                    <Reward
                      id="T5_SILVERBAG_NONTRADABLE"
                      title="Expert's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Finish a Tier 6 Solo Dungeon</td>
                    <Reward
                      id="T3_LEARNINGPOINTS_NONTRADABLE"
                      title="Journeyman's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Defeat a T5 boss with T3 equipment on your own</td>
                    <Reward
                      id="T3_LEARNINGPOINTS_NONTRADABLE"
                      title="Journeyman's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Finish an Enchantment Level 4 Solo Dungeon</td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Use 30 combat buff shrines in Solo Dungeons</td>
                    <Reward
                      id="T6_SKILLBOOK_NONTRADABLE"
                      title="Master's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Finish a Tier 7 Solo Dungeon</td>
                    <Reward
                      id="T6_SKILLBOOK_NONTRADABLE"
                      title="Master's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Finish a Tier 8 Solo Dungeon</td>
                    <Reward
                      id="T4_LEARNINGPOINTS_NONTRADABLE"
                      title="Adept's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Finish a Tier 8.4 Solo Dungeon</td>
                    <Reward
                      id="T4_LEARNINGPOINTS_NONTRADABLE"
                      title="Adept's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Unlock 100 chests in Solo Dungeons</td>
                    <Reward
                      id="T7_SILVERBAG_NONTRADABLE"
                      title="Grandmaster's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Defeat a T6 boss with T3 equipment on your own</td>
                    <Reward
                      id="T6_SKILLBOOK_NONTRADABLE"
                      title="Master's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Defeat a T7 boss with T3 equipment on your own</td>
                    <Reward
                      id="T4_LEARNINGPOINTS_NONTRADABLE"
                      title="Adept's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Defeat a T8 boss with T3 equipment on your own</td>
                    <Reward
                      id="T5_LEARNINGPOINTS_NONTRADABLE"
                      title="Expert's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Finish 30 Solo Dungeons</td>
                    <Reward
                      id="T7_SILVERBAG_NONTRADABLE"
                      title="Grandmaster's Bag of Silver (x4)"
                    />
                  </tr>
                  <tr>
                    <td>Finish 100 Solo Dungeons</td>
                    <Reward
                      id="T7_SILVERBAG_NONTRADABLE"
                      title="Grandmaster's Bag of Silver (x7)"
                    />
                  </tr>
                  <tr>
                    <td>Finish 300 Solo Dungeons</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x9)"
                    />
                  </tr>
                  <tr>
                    <td>Finish 600 Solo Dungeons</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x12)"
                    />
                  </tr>
                  <tr>
                    <td>Finish 1,000 Solo Dungeons</td>
                    <Reward
                      id="T5_LEARNINGPOINTS_NONTRADABLE"
                      title="Expert's Tome of Learning"
                    />
                  </tr>
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
                  <tr>
                    <td>Defeat 12 T3 Roaming Mobs</td>
                    <Reward
                      id="T3_SILVERBAG_NONTRADABLE"
                      title="Journeyman's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 50 T4 Roaming Mobs</td>
                    <Reward
                      id="T2_LEARNINGPOINTS_NONTRADABLE"
                      title="Novice's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 3 mobs with your mount standing next to you</td>
                    <Reward
                      id="T3_SKILLBOOK_NONTRADABLE"
                      title="Journeyman's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 4 Roaming Mobs within 10 seconds</td>
                    <Reward
                      id="T4_SKILLBOOK_NONTRADABLE"
                      title="Adept's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Defeat a Roaming Mob with any armor slot ability</td>
                    <Reward
                      id="T4_SKILLBOOK_NONTRADABLE"
                      title="Adept's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 80 T5 Roaming Mobs</td>
                    <Reward
                      id="T3_LEARNINGPOINTS_NONTRADABLE"
                      title="Journeyman's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 10 Roaming Mobs within 30 seconds</td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 50 mobs while flagged for Faction Warfare</td>
                    <Reward
                      id="T3_LEARNINGPOINTS_NONTRADABLE"
                      title="Journeyman's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 8 Roaming Mobs within 10 seconds</td>
                    <Reward
                      id="T4_LEARNINGPOINTS_NONTRADABLE"
                      title="Adept's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 5 Roaming Mobs in a Red Zone</td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 120 T6 Roaming Mobs</td>
                    <Reward
                      id="T5_SILVERBAG_NONTRADABLE"
                      title="Expert's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 200 T7 Roaming Mobs</td>
                    <Reward
                      id="T6_SKILLBOOK_NONTRADABLE"
                      title="Master's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 1,000 Roaming Mobs in a Black Zone</td>
                    <Reward
                      id="T5_LEARNINGPOINTS_NONTRADABLE"
                      title="Expert's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 300 T8 Roaming Mobs</td>
                    <Reward
                      id="T7_SKILLBOOK_NONTRADABLE"
                      title="Grandmaster's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 30 Roaming Mob Champions</td>
                    <Reward
                      id="T3_LEARNINGPOINTS_NONTRADABLE"
                      title="Journeyman's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 100 Roaming Mob Champions</td>
                    <Reward
                      id="T6_SILVERBAG_NONTRADABLE"
                      title="Master's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 300 Roaming Mob Champions</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 1,000 Roaming Mob Champions</td>
                    <Reward
                      id="T7_SKILLBOOK_NONTRADABLE"
                      title="Grandmaster's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 3,000 Roaming Mob Champions</td>
                    <Reward
                      id="T4_LEARNINGPOINTS_NONTRADABLE"
                      title="Adept's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 10 Roaming Mob Mini Bosses</td>
                    <Reward
                      id="UNIQUE_FURNITUREITEM_ADC_ICESCULPTURE_C"
                      title="Ice Sculpture: Obsessed Cultist"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 30 Roaming Mob Mini Bosses</td>
                    <Reward
                      id="T6_SKILLBOOK_NONTRADABLE"
                      title="Master's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 100 Roaming Mob Mini Bosses</td>
                    <Reward
                      id="T7_SKILLBOOK_NONTRADABLE"
                      title="Grandmaster's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 300 Roaming Mob Mini Bosses</td>
                    <Reward
                      id="T4_LEARNINGPOINTS_NONTRADABLE"
                      title="Adept's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 3 Roaming Mob Bosses</td>
                    <Reward
                      id="T6_SKILLBOOK_NONTRADABLE"
                      title="Master's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 10 Roaming Mob Bosses</td>
                    <Reward
                      id="T7_SKILLBOOK_NONTRADABLE"
                      title="Grandmaster's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 30 Roaming Mob Bosses</td>
                    <Reward
                      id="T4_LEARNINGPOINTS_NONTRADABLE"
                      title="Adept's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 100 Roaming Mob Bosses</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x10)"
                    />
                  </tr>
                  <tr>
                    <td>Gain 100,000 Fame from Roaming Mobs</td>
                    <Reward
                      id="T3_LEARNINGPOINTS_NONTRADABLE"
                      title="Journeyman's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Gain 300,000 Fame from Roaming Mobs</td>
                    <Reward
                      id="T6_SKILLBOOK_NONTRADABLE"
                      title="Master's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Gain a million Fame from Roaming Mobs</td>
                    <Reward
                      id="T5_LEARNINGPOINTS_NONTRADABLE"
                      title="Expert's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Gain 3 million Fame from Roaming Mobs</td>
                    <Reward
                      id="T7_SKILLBOOK_NONTRADABLE"
                      title="Grandmaster's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Gain 10 million Fame from Roaming Mobs</td>
                    <Reward
                      id="T8_SKILLBOOK_NONTRADABLE"
                      title="Elder's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Gain 30 million Fame from Roaming Mobs</td>
                    <Reward
                      id="UNIQUE_TOKEN_COMMUNITY"
                      title="Community Token (x50)"
                    />
                  </tr>
                  <tr>
                    <td>Gain 100 million Fame from Roaming Mobs</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x15)"
                    />
                  </tr>
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
                  <tr>
                    <td>Defeat 20 mobs in a T3 Static Dungeon</td>
                    <Reward
                      id="T4_SKILLBOOK_NONTRADABLE"
                      title="Adept's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 50 mobs in a T4 Static Dungeon</td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 100 mobs in a T5 Static Dungeon</td>
                    <Reward
                      id="T4_LEARNINGPOINTS_NONTRADABLE"
                      title="Adept's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 150 mobs in a T6 Static Dungeon</td>
                    <Reward
                      id="T3_POTION_MOB_RESET"
                      title="Minor Calming Potion"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 200 mobs in a T7 Static Dungeon</td>
                    <Reward
                      id="T7_SILVERBAG_NONTRADABLE"
                      title="Grandmaster's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 300 mobs in a T8 Static Dungeon</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Participate in a Static Dungeon Event</td>
                    <Reward
                      id="T2_LEARNINGPOINTS_NONTRADABLE"
                      title="Novice's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Gain 100,000 Fame during a Static Dungeon rally</td>
                    <Reward
                      id="T3_LEARNINGPOINTS_NONTRADABLE"
                      title="Journeyman's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Gain 10,000 Fame in Static Dungeons</td>
                    <Reward
                      id="T3_SKILLBOOK_NONTRADABLE"
                      title="Journeyman's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Gain 100,000 Fame in Static Dungeons</td>
                    <Reward
                      id="UNIQUE_UNLOCK_SKIN_HORSE_BROWN_NON_TRADABLE"
                      title="Riding Horse Skin: Brown Mare"
                    />
                  </tr>
                  <tr>
                    <td>Gain a million Fame in Static Dungeons</td>
                    <Reward
                      id="T7_SKILLBOOK_NONTRADABLE"
                      title="Grandmaster's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Gain 10 million Fame in Static Dungeons</td>
                    <Reward
                      id="T4_LEARNINGPOINTS_NONTRADABLE"
                      title="Adept's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Gain 30 million Fame in Static Dungeons</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x10)"
                    />
                  </tr>
                  <tr>
                    <td>Gain 100 million Fame in Static Dungeons</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x15)"
                    />
                  </tr>
                  <tr>
                    <td>Kill 100 Champions in Static Dungeons</td>
                    <Reward
                      id="UNIQUE_FURNITUREITEM_ADC_ICESCULPTURE_B"
                      title="Ice Sculpture: Cursed Archer"
                    />
                  </tr>
                  <tr>
                    <td>Kill 300 Champions in Static Dungeons</td>
                    <Reward
                      id="T4_LEARNINGPOINTS_NONTRADABLE"
                      title="Adept's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Kill 1,000 Champions in Static Dungeons</td>
                    <Reward
                      id="T8_SKILLBOOK_NONTRADABLE"
                      title="Elder's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Kill 30 Mini Bosses in Static Dungeons</td>
                    <Reward
                      id="T7_SKILLBOOK_NONTRADABLE"
                      title="Grandmaster's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Kill 100 Mini Bosses in Static Dungeons</td>
                    <Reward
                      id="T4_LEARNINGPOINTS_NONTRADABLE"
                      title="Adept's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Kill 300 Mini Bosses in Static Dungeons</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x10)"
                    />
                  </tr>
                  <tr>
                    <td>Kill 10 Bosses in Static Dungeons</td>
                    <Reward
                      id="T7_SKILLBOOK_NONTRADABLE"
                      title="Grandmaster's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Kill 30 Bosses in Static Dungeons</td>
                    <Reward
                      id="T5_LEARNINGPOINTS_NONTRADABLE"
                      title="Expert's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Kill 100 Bosses in Static Dungeons</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x15)"
                    />
                  </tr>
                </tbody>
              </Table>

              <h4>Group Random Dungeons (19)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Finish a Tier 4 Group Dungeon</td>
                    <Reward
                      id="T3_LEARNINGPOINTS_NONTRADABLE"
                      title="Journeyman's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Finish a Tier 5 Group Dungeon</td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Finish 2 Enchantment Level 1 Group Dungeons</td>
                    <Reward
                      id="T6_SILVERBAG_NONTRADABLE"
                      title="Master's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Finish 3 Enchantment Level 2 Group Dungeons</td>
                    <Reward
                      id="T4_LEARNINGPOINTS_NONTRADABLE"
                      title="Adept's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Finish 5 Enchantment Level 3 Group Dungeons</td>
                    <Reward
                      id="T7_SILVERBAG_NONTRADABLE"
                      title="Grandmaster's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Finish a Tier 6 Group Dungeon</td>
                    <Reward
                      id="UNIQUE_UNLOCK_HEAD_VANITY_BARD_NON_TRADABLE"
                      title="Wardrobe Skin: Bard's Hat"
                    />
                  </tr>
                  <tr>
                    <td>Finish a Tier 7 Group Dungeon</td>
                    <Reward
                      id="T6_SKILLBOOK_NONTRADABLE"
                      title="Master's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Finish a Tier 8 Group Dungeon</td>
                    <Reward
                      id="T7_SKILLBOOK_NONTRADABLE"
                      title="Grandmaster's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Finish a Tier 8.4 Group Dungeon</td>
                    <Reward
                      id="T4_LEARNINGPOINTS_NONTRADABLE"
                      title="Adept's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Unlock 10 chests in Group Dungeons</td>
                    <Reward
                      id="T5_SILVERBAG_NONTRADABLE"
                      title="Expert's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Unlock 30 chests in Group Dungeons</td>
                    <Reward
                      id="T6_RANDOM_DUNGEON_ELITE_TOKEN_1"
                      title="Master's Dungeon Map (Large Group)"
                    />
                  </tr>
                  <tr>
                    <td>Unlock 100 chests in Group Dungeons</td>
                    <Reward
                      id="T7_SILVERBAG_NONTRADABLE"
                      title="Grandmaster's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Unlock 500 chests in Group Dungeons</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Finish 10 Group Dungeons</td>
                    <Reward
                      id="T6_SKILLBOOK_NONTRADABLE"
                      title="Master's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Finish 30 Group Dungeons</td>
                    <Reward
                      id="T5_LEARNINGPOINTS_NONTRADABLE"
                      title="Expert's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Finish 80 Group Dungeons</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x5)"
                    />
                  </tr>
                  <tr>
                    <td>Finish 150 Group Dungeons</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x15)"
                    />
                  </tr>
                  <tr>
                    <td>Finish 300 Group Dungeons</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x20)"
                    />
                  </tr>
                  <tr>
                    <td>Finish 500 Group Dungeons</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x25)"
                    />
                  </tr>
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
                  <tr>
                    <td>Track down a solo Rare Creature</td>
                    <Reward
                      id="T3_LEARNINGPOINTS_NONTRADABLE"
                      title="Journeyman's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Track down a T4 solo Rare Quarry</td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Track down 3 types of solo Rare Creature</td>
                    <Reward
                      id="UNIQUE_FURNITUREITEM_KEEPER_SYMBOL_OF_POWER_A"
                      title="Keeper Symbol of Power"
                    />
                  </tr>
                  <tr>
                    <td>Track down a T5 solo Rare Quarry</td>
                    <Reward
                      id="T5_SILVERBAG_NONTRADABLE"
                      title="Expert's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Track down 4 types of solo Rare Creature</td>
                    <Reward
                      id="T4_ARTEFACT_2H_SHAPESHIFTER_MORGANA"
                      title="Adept's Werewolf Remnant"
                    />
                  </tr>
                  <tr>
                    <td>Track down a T6 solo Rare Quarry</td>
                    <Reward
                      id="T6_SILVERBAG_NONTRADABLE"
                      title="Master's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Track down 5 types of solo Rare Creature</td>
                    <Reward
                      id="T4_ARTEFACT_2H_SHAPESHIFTER_HELL"
                      title="Adept's Hellfire Imp Remnant"
                    />
                  </tr>
                  <tr>
                    <td>Finish a hunt at the first encounter</td>
                    <Reward
                      id="T6_SKILLBOOK_NONTRADABLE"
                      title="Master's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Track down 6 types of solo Rare Creature</td>
                    <Reward
                      id="T4_ARTEFACT_2H_SHAPESHIFTER_KEEPER"
                      title="Adept's Runestone Golem Remnant"
                    />
                  </tr>
                  <tr>
                    <td>Track down a T7 solo Rare Quarry</td>
                    <Reward
                      id="T3_LEARNINGPOINTS_NONTRADABLE"
                      title="Journeyman's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>
                      Track down 7 different solo Rare Creatures
                      <br />
                      <span className="text-muted">
                        Shadow Panther, Sylvian, Spirit Bear, Werewolf, Hellfire
                        Imp, Runestone Golem, Dawnbird
                      </span>
                    </td>
                    <Reward
                      id="T4_ARTEFACT_2H_SHAPESHIFTER_AVALON"
                      title="Adept's Dawnbird Remnant"
                    />
                  </tr>
                  <tr>
                    <td>Track down a T8 solo Rare Quarry</td>
                    <Reward
                      id="T7_SKILLBOOK_NONTRADABLE"
                      title="Grandmaster's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Track down a group Rare Creature</td>
                    <Reward
                      id="T3_LEARNINGPOINTS_NONTRADABLE"
                      title="Journeyman's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Track down 3 types of group Rare Creature</td>
                    <Reward
                      id="T7_SILVERBAG_NONTRADABLE"
                      title="Grandmaster's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Track down 5 types of group Rare Creature</td>
                    <Reward
                      id="T4_LEARNINGPOINTS_NONTRADABLE"
                      title="Adept's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>
                      Track down 7 types of group Rare Creature
                      <br />
                      <span className="text-muted">
                        Shadow Panther, Sylvian, Spirit Bear, Werewolf, Hellfire
                        Imp, Runestone Golem, Dawnbird
                      </span>
                    </td>
                    <Reward
                      id="T7_SILVERBAG_NONTRADABLE"
                      title="Grandmaster's Bag of Silver (x5)"
                    />
                  </tr>
                  <tr>
                    <td>Track down a T8 group Rare Quarry</td>
                    <Reward
                      id="T6_SKILLBOOK_NONTRADABLE"
                      title="Master's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Finish a solo Rare Creature hunt in 4 minutes</td>
                    <Reward
                      id="T6_SKILLBOOK_NONTRADABLE"
                      title="Master's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Finish a solo Dawnbird hunt in 10 minutes</td>
                    <Reward
                      id="T7_SKILLBOOK_NONTRADABLE"
                      title="Grandmaster's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Finish a group Rare Creature hunt in 4 minutes</td>
                    <Reward
                      id="T6_SKILLBOOK_NONTRADABLE"
                      title="Master's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Finish a group Dawnbird hunt in 10 minutes</td>
                    <Reward
                      id="T7_SKILLBOOK_NONTRADABLE"
                      title="Grandmaster's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Finish 10 hunts</td>
                    <Reward
                      id="T7_SILVERBAG_NONTRADABLE"
                      title="Grandmaster's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Finish 20 hunts</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Finish 40 hunts</td>
                    <Reward
                      id="T5_LEARNINGPOINTS_NONTRADABLE"
                      title="Expert's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Finish 80 hunts</td>
                    <Reward
                      id="UNIQUE_UNLOCK_ARMOR_VANITY_PIRATE_GREEN_NON_TRADABLE"
                      title="Wardrobe Skin: Green Navigator's Coat"
                    />
                  </tr>
                  <tr>
                    <td>Finish 200 hunts</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x8)"
                    />
                  </tr>
                  <tr>
                    <td>Finish 500 hunts</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x15)"
                    />
                  </tr>
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
                  <tr>
                    <td>Defeat 10 Elite mobs in a World Boss Area</td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 50 Elite mobs in a World Boss Area</td>
                    <Reward
                      id="T7_SILVERBAG_NONTRADABLE"
                      title="Grandmaster's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Defeat a Mini Boss in a World Boss Area</td>
                    <Reward
                      id="UNIQUE_FURNITUREITEM_MORGANA_STATUE_A"
                      title="Morgana Cultist Statue"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 5 Mini Bosses in a World Boss Area</td>
                    <Reward
                      id="T4_LEARNINGPOINTS_NONTRADABLE"
                      title="Adept's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Defeat a Boss in a World Boss Area</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Defeat the Earth Mother</td>
                    <Reward
                      id="T5_LEARNINGPOINTS_NONTRADABLE"
                      title="Expert's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 20 Mini Bosses in a World Boss Area</td>
                    <Reward
                      id="T6_SKILLBOOK_NONTRADABLE"
                      title="Master's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 5 Bosses in World Boss Areas</td>
                    <Reward
                      id="T6_SKILLBOOK_NONTRADABLE"
                      title="Master's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Defeat the Harvester</td>
                    <Reward
                      id="T5_LEARNINGPOINTS_NONTRADABLE"
                      title="Expert's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 50 Mini Bosses in World Boss Areas</td>
                    <Reward
                      id="T7_SKILLBOOK_NONTRADABLE"
                      title="Grandmaster's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 20 Bosses in World Boss Areas</td>
                    <Reward
                      id="T7_SKILLBOOK_NONTRADABLE"
                      title="Grandmaster's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Defeat the Demon Prince</td>
                    <Reward
                      id="T5_LEARNINGPOINTS_NONTRADABLE"
                      title="Expert's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 1,000 Elite mobs in a World Boss Area</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x5)"
                    />
                  </tr>
                  <tr>
                    <td>Defeat a T8 World Boss</td>
                    <Reward
                      id="T8_SKILLBOOK_NONTRADABLE"
                      title="Elder's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>
                      Defeat every T8 World Boss
                      <br />
                      <span className="text-muted">
                        Harvester of Souls, Great Mother of the Earthkeeper,
                        Prince of Morgana
                      </span>
                    </td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x15)"
                    />
                  </tr>
                  <tr>
                    <td>
                      Defeat a World Boss in every possible area
                      <br />
                      <span className="text-muted">
                        Camlann, Astolat, Inis Mon, Citadel of Ash, Eye of the
                        Forest, Eldersleep, Unhallowed Cloister, Deathreach
                        Priory, Black Monastery, Wailing Bulwark, Daemonium Keep
                      </span>
                    </td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x25)"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 200 Mini Bosses in World Boss Areas</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x10)"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 50 Bosses in World Boss Areas</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x5)"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 10 World Bosses</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x10)"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 30 World Bosses</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x20)"
                    />
                  </tr>
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
                  <tr>
                    <td>Finish a T6 Avalonian Dungeon</td>
                    <Reward
                      id="T3_LEARNINGPOINTS_NONTRADABLE"
                      title="Journeyman's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>
                      Receive the Ascension buff at the end of an Avalonian
                      Dungeon
                    </td>
                    <Reward
                      id="T6_SKILLBOOK_NONTRADABLE"
                      title="Master's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>
                      Defeat every Avalonian Dungeon boss type
                      <br />
                      <span className="text-muted">
                        Avalonian Knight Captain, Avalonian Construct, Avalonian
                        Crystal Basilisk, Avalonian High Priestess, Avalonian
                        Archmage
                      </span>
                    </td>
                    <Reward
                      id="T7_SKILLBOOK_NONTRADABLE"
                      title="Grandmaster's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Finish a T7 Avalonian Dungeon</td>
                    <Reward
                      id="T4_LEARNINGPOINTS_NONTRADABLE"
                      title="Adept's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Defeat Sir Bedivere with the Ascension buff active</td>
                    <Reward
                      id="T7_SKILLBOOK_NONTRADABLE"
                      title="Grandmaster's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Finish a T8 Avalonian Dungeon</td>
                    <Reward
                      id="T8_SKILLBOOK_NONTRADABLE"
                      title="Elder's Tome of Insight (x6)"
                    />
                  </tr>
                  <tr>
                    <td>Finish a T8.1 Avalonian Dungeon</td>
                    <Reward
                      id="T8_SKILLBOOK_NONTRADABLE"
                      title="Elder's Tome of Insight (x7)"
                    />
                  </tr>
                  <tr>
                    <td>Finish a T8.2 Avalonian Dungeon</td>
                    <Reward
                      id="T8_SKILLBOOK_NONTRADABLE"
                      title="Elder's Tome of Insight (x8)"
                    />
                  </tr>
                  <tr>
                    <td>Finish a T8.3 Avalonian Dungeon</td>
                    <Reward
                      id="T8_SKILLBOOK_NONTRADABLE"
                      title="Elder's Tome of Insight (x9)"
                    />
                  </tr>
                  <tr>
                    <td>Finish a T8.4 Avalonian Dungeon</td>
                    <Reward
                      id="T8_SKILLBOOK_NONTRADABLE"
                      title="Elder's Tome of Insight (x10)"
                    />
                  </tr>
                  <tr>
                    <td>Finish 5 Avalonian Dungeons</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x10)"
                    />
                  </tr>
                  <tr>
                    <td>Finish 10 Avalonian Dungeons</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x12)"
                    />
                  </tr>
                  <tr>
                    <td>Finish 20 Avalonian Dungeons</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x15)"
                    />
                  </tr>
                  <tr>
                    <td>Finish 40 Avalonian Dungeons</td>
                    <Reward
                      id="T5_LEARNINGPOINTS_NONTRADABLE"
                      title="Expert's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Finish 60 Avalonian Dungeons</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x20)"
                    />
                  </tr>
                  <tr>
                    <td>Finish 100 Avalonian Dungeons</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x30)"
                    />
                  </tr>
                  <tr>
                    <td>Unlock 10 chests in Avalonian Dungeons</td>
                    <Reward
                      id="T7_SKILLBOOK_NONTRADABLE"
                      title="Grandmaster's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Unlock 20 chests in Avalonian Dungeons</td>
                    <Reward
                      id="T5_LEARNINGPOINTS_NONTRADABLE"
                      title="Expert's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Unlock 40 chests in Avalonian Dungeons</td>
                    <Reward
                      id="UNIQUE_UNLOCK_HEAD_VANITY_BARD_BLUE_NON_TRADABLE"
                      title="Wardrobe Skin: Blue Bard's Hat"
                    />
                  </tr>
                  <tr>
                    <td>Unlock 100 chests in Avalonian Dungeons</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x10)"
                    />
                  </tr>
                  <tr>
                    <td>Unlock a Legendary Chest in an Avalonian Dungeon</td>
                    <Reward
                      id="T8_SKILLBOOK_NONTRADABLE"
                      title="Elder's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Unlock 160 chests in Avalonian Dungeons</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x15)"
                    />
                  </tr>
                  <tr>
                    <td>Unlock 300 chests in Avalonian Dungeons</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x20)"
                    />
                  </tr>
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
              Gathering (115)
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
                  <tr>
                    <td>Gather 50 Tier 2 resources</td>
                    <Reward
                      id="T3_SILVERBAG_NONTRADABLE"
                      title="Journeyman's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Gather 75 Tier 3 resources</td>
                    <Reward
                      id="T4_SILVERBAG_NONTRADABLE"
                      title="Adept's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Gather resources worth 500 Fame</td>
                    <Reward
                      id="T2_LEARNINGPOINTS_NONTRADABLE"
                      title="Novice's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Gather 100 Tier 4 resources</td>
                    <Reward
                      id="T3_LEARNINGPOINTS_NONTRADABLE"
                      title="Journeyman's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Gather 10 resources with Enchantment Level 1</td>
                    <Reward
                      id="T4_SKILLBOOK_GATHER_FIBER_NONTRADABLE"
                      title="Adept Fiber Harvester Tome"
                    />
                  </tr>
                  <tr>
                    <td>Gather 150 Tier 5 resources</td>
                    <Reward
                      id="T4_SKILLBOOK_GATHER_ROCK_NONTRADABLE"
                      title="Adept Quarrier Tome"
                    />
                  </tr>
                  <tr>
                    <td>Gather 10 resources with Enchantment Level 2</td>
                    <Reward
                      id="T4_SKILLBOOK_GATHER_WOOD_NONTRADABLE"
                      title="Adept Lumberjack Tome"
                    />
                  </tr>
                  <tr>
                    <td>Gather a resource from a Plentiful Resource Node</td>
                    <Reward
                      id="T4_LEARNINGPOINTS_NONTRADABLE"
                      title="Adept's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Gather 10 resources with Enchantment Level 3</td>
                    <Reward
                      id="T5_SKILLBOOK_GATHER_ORE_NONTRADABLE"
                      title="Expert Ore Miner Tome"
                    />
                  </tr>
                  <tr>
                    <td>Gather 200 Tier 6 resources</td>
                    <Reward
                      id="T5_SKILLBOOK_GATHER_WOOD_NONTRADABLE"
                      title="Expert Lumberjack Tome"
                    />
                  </tr>
                  <tr>
                    <td>Gather 100 resources from Plentiful Resource Nodes</td>
                    <Reward
                      id="T5_SKILLBOOK_GATHER_ROCK_NONTRADABLE"
                      title="Expert Quarrier Tome"
                    />
                  </tr>
                  <tr>
                    <td>Gather 300 enchanted resources</td>
                    <Reward
                      id="UNIQUE_UNLOCK_ARMOR_VANITY_PRIEST_NON_TRADABLE"
                      title="Wardrobe Skin: Monk's Robe"
                    />
                  </tr>
                  <tr>
                    <td>Gather 500 resources from Plentiful Resource Nodes</td>
                    <Reward
                      id="T6_SKILLBOOK_GATHER_WOOD_NONTRADABLE"
                      title="Master Lumberjack Tome"
                    />
                  </tr>
                  <tr>
                    <td>Gather any resource at an enemy Territory</td>
                    <Reward
                      id="T6_SKILLBOOK_GATHER_ORE_NONTRADABLE"
                      title="Master Ore Miner Tome"
                    />
                  </tr>
                  <tr>
                    <td>Gather 750 enchanted resources</td>
                    <Reward
                      id="T6_SKILLBOOK_GATHER_FIBER_NONTRADABLE"
                      title="Master Fiber Harvester Tome"
                    />
                  </tr>
                  <tr>
                    <td>Gather 200 Tier 7 resources</td>
                    <Reward
                      id="T4_LEARNINGPOINTS_NONTRADABLE"
                      title="Adept's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>
                      Gather 1,000 resources from Plentiful Resource Nodes
                    </td>
                    <Reward
                      id="T7_SKILLBOOK_GATHER_ROCK_NONTRADABLE"
                      title="Grandmaster Quarrier Tome"
                    />
                  </tr>
                  <tr>
                    <td>Gather 50 resources at an enemy Territory</td>
                    <Reward
                      id="T7_SKILLBOOK_GATHER_FIBER_NONTRADABLE"
                      title="Grandmaster Fiber Harvester Tome"
                    />
                  </tr>
                  <tr>
                    <td>Gather 1,500 enchanted resources</td>
                    <Reward
                      id="T7_SKILLBOOK_GATHER_ORE_NONTRADABLE"
                      title="Grandmaster Ore Miner Tome"
                    />
                  </tr>
                  <tr>
                    <td>Gather any Tier 8 resource</td>
                    <Reward
                      id="T5_LEARNINGPOINTS_NONTRADABLE"
                      title="Expert's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Gather a resource with maximum Gather Bonus</td>
                    <Reward
                      id="T8_SKILLBOOK_GATHER_ORE_NONTRADABLE"
                      title="Elder Ore Miner Tome"
                    />
                  </tr>
                  <tr>
                    <td>Gather 200 Tier 8 resources</td>
                    <Reward
                      id="T8_SKILLBOOK_GATHER_WOOD_NONTRADABLE"
                      title="Elder Lumberjack Tome"
                    />
                  </tr>
                  <tr>
                    <td>Gather 30 resources with Enchantment Level 4</td>
                    <Reward
                      id="T8_SKILLBOOK_GATHER_ROCK_NONTRADABLE"
                      title="Elder Quarrier Tome"
                    />
                  </tr>
                  <tr>
                    <td>Gather resources worth 10,000 Fame</td>
                    <Reward
                      id="T4_SKILLBOOK_GATHER_ORE_NONTRADABLE"
                      title="Adept Ore Miner Tome"
                    />
                  </tr>
                  <tr>
                    <td>Gather resources worth 25,000 Fame</td>
                    <Reward
                      id="T5_SKILLBOOK_GATHER_FIBER_NONTRADABLE"
                      title="Expert Fiber Harvester Tome"
                    />
                  </tr>
                  <tr>
                    <td>Gather resources worth 50,000 Fame</td>
                    <Reward
                      id="T6_SKILLBOOK_GATHER_ROCK_NONTRADABLE"
                      title="Master Quarrier Tome"
                    />
                  </tr>
                  <tr>
                    <td>Gather resources worth 100,000 Fame</td>
                    <Reward
                      id="T7_SKILLBOOK_GATHER_WOOD_NONTRADABLE"
                      title="Grandmaster Lumberjack Tome"
                    />
                  </tr>
                  <tr>
                    <td>Gather resources worth 250,000 Fame</td>
                    <Reward
                      id="T8_SKILLBOOK_GATHER_FIBER_NONTRADABLE"
                      title="Elder Fiber Harvester Tome"
                    />
                  </tr>
                  <tr>
                    <td>Gather resources worth 500,000 Fame</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Gather resources worth a million Fame</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x2)"
                    />
                  </tr>
                  <tr>
                    <td>Gather resources worth 3 million Fame</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x3)"
                    />
                  </tr>
                  <tr>
                    <td>Gather resources worth 10 million Fame</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x5)"
                    />
                  </tr>
                  <tr>
                    <td>Gather a T8 resource at an enemy territory</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver"
                    />
                  </tr>
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
                  <tr>
                    <td>Skin 3 types of Hide Animal</td>
                    <Reward
                      id="T3_SKILLBOOK_NONTRADABLE"
                      title="Journeyman's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Skin 6 types of Hide Animal</td>
                    <Reward
                      id="T4_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                      title="Adept Animal Skinner Tome"
                    />
                  </tr>
                  <tr>
                    <td>Skin 10 types of Hide Animal</td>
                    <Reward
                      id="T5_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                      title="Expert Animal Skinner Tome"
                    />
                  </tr>
                  <tr>
                    <td>Skin 15 types of Hide Animal</td>
                    <Reward
                      id="UNIQUE_UNLOCK_HEAD_VANITY_INNKEEPER_NON_TRADABLE"
                      title="Wardrobe Skin: Innkeeper's Hat"
                    />
                  </tr>
                  <tr>
                    <td>Skin 22 types of Hide Animal</td>
                    <Reward
                      id="T6_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                      title="Master Animal Skinner Tome"
                    />
                  </tr>
                  <tr>
                    <td>Skin 30 types of Hide Animal</td>
                    <Reward
                      id="T7_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                      title="Grandmaster Animal Skinner Tome"
                    />
                  </tr>
                  <tr>
                    <td>Skin 40 types of Hide Animal</td>
                    <Reward
                      id="T8_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                      title="Elder Animal Skinner Tome"
                    />
                  </tr>
                  <tr>
                    <td>Skin 52 types of Hide Animal</td>
                    <Reward
                      id="T4_LEARNINGPOINTS_NONTRADABLE"
                      title="Adept's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Skin 65 types of Hide Animal</td>
                    <Reward
                      id="UNIQUE_FOCUSPOTION_ADC_NONTRADABLE_01"
                      title="Grandmaster's Focus Restoration Potion"
                    />
                  </tr>
                  <tr>
                    <td>
                      Skin every type of Hide Animal
                      <br />
                      <span className="text-muted">
                        Bear, Boar, Direwolf, Fox, Rabbit, Wolf, Hill Marmot,
                        Wolpertinger, Snow Rabbit, Marmot, Toad, Fey Fox,
                        Impala, Snake, Cougar, Foglands Doe, Moabird, Giant
                        Toad, Mistcougar Runt, Old Mistcougar Runt, Foglands
                        Hart, Giant Stag, Monitor Lizard, Rare Boar, Rare Giant
                        Stag, Rare Monitor Lizard, Grand Foglands Hart,
                        Sabretooth Tiger, Small Mistcougar, Ancient Small
                        Mistcougar, Old Small Mistcougar, Great Mystic Owl,
                        Terrorbird, Giant Snake, Rare Bear, Rare Giant Snake,
                        Majestic Mystic Owl, Rare Terrorbird, Mistcougar,
                        Ancient Mistcougar, Old Mistcougar, Ancient Basilisk,
                        Old White, Moose, Feral Wolfhound, Hyena, Swamp Dragon,
                        Old Basilisk Aspect, Old White&apos;s Aspect, Rare
                        Hyena, Rare Direwolf, Rare Swamp Dragon, Insatiable
                        Wolfhound, Mature Sabretooth Tiger, Large Mistcougar,
                        Ancient Large Mistcougar, Old Large Mistcougar, Feral
                        Boar, Misthide Mauler, Rhino, Rare Direboar, Ferocious
                        Misthide Mauler, Rare Rhino, Alpha Mistcougar, Ancient
                        Alpha Mistcougar, Old Alpha Mistcougar, Ancient Giant
                        Basilisk, Feral Bear, Dragonhawk, Mammoth, Old Giant
                        Basilisk Aspect, Rare Ancient Mammoth, Rare Direbear,
                        Regal Dragonhawk
                      </span>
                    </td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x5)"
                    />
                  </tr>
                  <tr>
                    <td>Loot a wild Baby Animal</td>
                    <Reward
                      id="UNIQUE_FURNITUREITEM_ADC_RUG_DIREBEAR"
                      title="Direbear Rug"
                    />
                  </tr>
                  <tr>
                    <td>Loot 3 wild Baby Animals</td>
                    <Reward
                      id="T4_LEARNINGPOINTS_NONTRADABLE"
                      title="Adept's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Loot 5 different Baby Animals</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x5)"
                    />
                  </tr>
                  <tr>
                    <td>
                      Loot all wild Baby Animals
                      <br />
                      <span className="text-muted">
                        Adept&apos;s Fawn, Swiftclaw Cub, Direwolf Pup, Moose
                        Calf, Direboar Piglet, Swamp Dragon Pup, Direbear Cub,
                        Mammoth Calf
                      </span>
                    </td>
                    <Reward
                      id="T5_LEARNINGPOINTS_NONTRADABLE"
                      title="Expert's Tome of Learning"
                    />
                  </tr>
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
                  <tr>
                    <td>Catch your first fish</td>
                    <Reward
                      id="T3_SKILLBOOK_NONTRADABLE"
                      title="Journeyman's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Eat 5 fish</td>
                    <Reward
                      id="T3_SKILLBOOK_NONTRADABLE"
                      title="Journeyman's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Catch 3 types of fish</td>
                    <Reward
                      id="T4_SKILLBOOK_NONTRADABLE"
                      title="Adept's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Eat 30 fish</td>
                    <Reward
                      id="T3_SILVERBAG_NONTRADABLE"
                      title="Journeyman's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Catch a saltwater fish</td>
                    <Reward
                      id="T2_LEARNINGPOINTS_NONTRADABLE"
                      title="Novice's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Catch 6 types of fish</td>
                    <Reward
                      id="T5_FOCUSPOTION_NONTRADABLE"
                      title="Expert's Focus Restoration Potion"
                    />
                  </tr>
                  <tr>
                    <td>Catch a fish with Fish Bait</td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Catch 10 types of fish</td>
                    <Reward
                      id="T3_LEARNINGPOINTS_NONTRADABLE"
                      title="Journeyman's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Catch 15 types of fish</td>
                    <Reward
                      id="UNIQUE_UNLOCK_SHOES_VANITY_BARD_BLUE_NON_TRADABLE"
                      title="Wardrobe Skin: Blue Bard's Shoes"
                    />
                  </tr>
                  <tr>
                    <td>Catch 21 types of fish</td>
                    <Reward
                      id="T4_LEARNINGPOINTS_NONTRADABLE"
                      title="Adept's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Catch 28 types of fish</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x10)"
                    />
                  </tr>
                  <tr>
                    <td>Catch a Shark</td>
                    <Reward
                      id="T8_SKILLBOOK_NONTRADABLE"
                      title="Elder's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>
                      Catch all types of fish
                      <br />
                      <span className="text-muted">
                        Common Rudd, Striped Carp, Albion Perch, Bluescale Pike,
                        Spotted Trout, Brightscale Zander, Danglemouth Catfish,
                        River Sturgeon, Common Herring, Striped Mackerel,
                        Flatshore Plaice, Bluescale Cod, Spotted Wolffish,
                        Strongfin Salmon, Bluefin Tuna, Steelscale Swordfish,
                        Greenriver Eel, Redspring Eel, Deadwater Eel, Upland
                        Coldeye, Mountain Blindeye, Frostpeak Deadeye,
                        Stonestream Lurcher, Rushwater Lurcher, Thunderfall
                        Lurcher, Lowriver Crab, Drybrook Crab, Dusthole Crab,
                        Greenmoor Clam, Murkwater Clam, Blackbog Clam, Whitefog
                        Snapper, Clearhaze Snapper, Puremist Snapper,
                        Shallowshore Squid, Midwater Octopus, Deepwater Kraken,
                        Shark
                      </span>
                    </td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x15)"
                    />
                  </tr>
                  <tr>
                    <td>Catch fish worth 3,000 Fame</td>
                    <Reward
                      id="T3_SKILLBOOK_NONTRADABLE"
                      title="Journeyman's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Catch fish worth 10,000 Fame</td>
                    <Reward
                      id="UNIQUE_FURNITUREITEM_KEEPER_CAULDRON"
                      title="Keeper Cauldron"
                    />
                  </tr>
                  <tr>
                    <td>Catch fish worth 30,000 Fame</td>
                    <Reward
                      id="T4_SKILLBOOK_NONTRADABLE"
                      title="Adept's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Catch fish worth 100,000 Fame</td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Catch fish worth 300,000 Fame</td>
                    <Reward
                      id="T3_LEARNINGPOINTS_NONTRADABLE"
                      title="Journeyman's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Catch fish worth a million Fame</td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Catch fish worth 3 million Fame</td>
                    <Reward
                      id="T6_SKILLBOOK_NONTRADABLE"
                      title="Master's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Catch fish worth 10 million Fame</td>
                    <Reward
                      id="T3_VANITY_CONSUMABLE_FIREWORKS_BLUE_NONTRADABLE"
                      title="Royal Blue Fireworks (x99)"
                    />
                  </tr>
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
                  <tr>
                    <td>Harvest 30 resources from Resource Mobs</td>
                    <Reward
                      id="T3_SKILLBOOK_NONTRADABLE"
                      title="Journeyman's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Harvest resources from 3 Resource Mob types</td>
                    <Reward id="T3_MEAL_PIE" title="Chicken Pie" />
                  </tr>
                  <tr>
                    <td>Harvest resources from 7 Resource Mob types</td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Harvest resources from 12 Resource Mob types</td>
                    <Reward
                      id="T5_FOCUSPOTION_NONTRADABLE"
                      title="Expert's Focus Restoration Potion"
                    />
                  </tr>
                  <tr>
                    <td>Harvest a resource from an Aspect</td>
                    <Reward
                      id="T4_LEARNINGPOINTS_NONTRADABLE"
                      title="Adept's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Harvest resources from 18 Resource Mob types</td>
                    <Reward
                      id="T7_SKILLBOOK_GATHER_FIBER_NONTRADABLE"
                      title="Grandmaster Fiber Harvester Tome"
                    />
                  </tr>
                  <tr>
                    <td>
                      Harvest resources from Aspects in every biome
                      <br />
                      <span className="text-muted">
                        Steppe, Swamp, Mountain, Forest, Highland, Roads of
                        Avalon
                      </span>
                    </td>
                    <Reward
                      id="T4_LEARNINGPOINTS_NONTRADABLE"
                      title="Adept's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Harvest resources from 25 Resource Mob types</td>
                    <Reward
                      id="T7_SKILLBOOK_GATHER_WOOD_NONTRADABLE"
                      title="Grandmaster Lumberjack Tome"
                    />
                  </tr>
                  <tr>
                    <td>
                      Harvest resources from a Guardian in the Roads of Avalon
                    </td>
                    <Reward
                      id="T6_FOCUSPOTION_NONTRADABLE"
                      title="Master's Focus Restoration Potion"
                    />
                  </tr>
                  <tr>
                    <td>Harvest resources from 34 Resource Mob types</td>
                    <Reward
                      id="T7_SKILLBOOK_GATHER_ORE_NONTRADABLE"
                      title="Grandmaster Ore Miner Tome"
                    />
                  </tr>
                  <tr>
                    <td>Harvest 3,000 resources from Aspects</td>
                    <Reward
                      id="T6_FOCUSPOTION_NONTRADABLE"
                      title="Master's Focus Restoration Potion"
                    />
                  </tr>
                  <tr>
                    <td>Harvest resources from 46 Resource Mob types</td>
                    <Reward
                      id="T7_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                      title="Grandmaster Animal Skinner Tome"
                    />
                  </tr>
                  <tr>
                    <td>Harvest 3,000 resources from Ancient Resource Mobs</td>
                    <Reward
                      id="T7_SKILLBOOK_GATHER_ROCK_NONTRADABLE"
                      title="Grandmaster Quarrier Tome"
                    />
                  </tr>
                  <tr>
                    <td>
                      Harvest resources from all Resource Mob types
                      <br />
                      <span className="text-muted">
                        Swamp Spirit, Ore Elemental, Rock Elemental, Forest
                        Spirit, Hemp Dryad, Ancient Hemp Dryad, Old Hemp Dryad,
                        Iron Elemental, Ancient Iron Elemental, Old Iron
                        Elemental, Travertine Elemental, Ancient Travertine
                        Elemental, Old Travertine Elemental, Pine Spirit,
                        Ancient Pine Spirit, Old Pine Spirit, Skyflower Dryad,
                        Ancient Skyflower Dryad, Old Skyflower Dryad, Mature Ore
                        Elemental, Ancient Titanium Elemental, Old Titanium
                        Elemental, Mature Rock Elemental, Ancient Granite
                        Elemental, Old Granite Elemental, Mature Forest Spirit,
                        Ancient Cedar Spirit, Old Cedar Spirit, Amberleaf Dryad,
                        Ancient Amberleaf Dryad, Old Amberleaf Dryad, Runite
                        Elemental, Ancient Runite Elemental, Old Runite
                        Elemental, Slate Elemental, Ancient Slate Elemental, Old
                        Slate Elemental, Bloodoak Spirit, Ancient Bloodoak
                        Spirit, Old Bloodoak Spirit, Elder Swamp Spirit, Sunflax
                        Dryad, Ancient Sunflax Dryad, Old Sunflax Dryad, Elder
                        Ore Elemental, Ancient Meteorite Elemental, Old
                        Meteorite Elemental, Elder Rock Elemental, Ancient
                        Basalt Elemental, Old Basalt Elemental, Elder Forest
                        Spirit, Ancient Ashenbark Spirit, Old Ashenbark Spirit,
                        Ghost Hemp Dryad, Ancient Ghost Hemp Dryad, Old Ghost
                        Hemp Dryad, Adamantium Elemental, Ancient Adamantium
                        Elemental, Old Adamantium Elemental, Marble Elemental,
                        Ancient Marble Elemental, Old Marble Elemental,
                        Whitewood Spirit, Ancient Whitewood Spirit, Old
                        Whitewood Spirit
                      </span>
                    </td>
                    <Reward
                      id="UNIQUE_TOKEN_COMMUNITY"
                      title="Community Token (x200)"
                    />
                  </tr>
                  <tr>
                    <td>Harvest 100 resources from Resource Mobs</td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Harvest 300 resources from Resource Mobs</td>
                    <Reward
                      id="T6_SKILLBOOK_NONTRADABLE"
                      title="Master's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Harvest 1,000 resources from Resource Mobs</td>
                    <Reward
                      id="T3_LEARNINGPOINTS_NONTRADABLE"
                      title="Journeyman's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Harvest 10,000 resources from Resource Mobs</td>
                    <Reward
                      id="T4_LEARNINGPOINTS_NONTRADABLE"
                      title="Adept's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Harvest 10,000 resources from Aspects</td>
                    <Reward
                      id="T8_SKILLBOOK_NONTRADABLE"
                      title="Elder's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Harvest 10,000 resources from Ancient Resource Mobs</td>
                    <Reward
                      id="T4_LEARNINGPOINTS_NONTRADABLE"
                      title="Adept's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Harvest 30,000 resources from Ancient Resource Mobs</td>
                    <Reward
                      id="UNIQUE_FOCUSPOTION_ADC_NONTRADABLE_01"
                      title="Grandmaster's Focus Restoration Potion"
                    />
                  </tr>
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
                  <tr>
                    <td>Gather 250 resources in a yellow zone</td>
                    <Reward
                      id="UNIQUE_FURNITUREITEM_HERETICS_TOOL_BOARD_A"
                      title="Heretic Toolboard"
                    />
                  </tr>
                  <tr>
                    <td>
                      Gather 250 resources in a yellow zone while faction
                      flagged
                    </td>
                    <Reward
                      id="T3_LEARNINGPOINTS_NONTRADABLE"
                      title="Journeyman's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Gather 250 resources in the yellow Mists</td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Gather 250 resources in a red zone</td>
                    <Reward
                      id="T5_SKILLBOOK_GATHER_WOOD_NONTRADABLE"
                      title="Expert Lumberjack Tome"
                    />
                  </tr>
                  <tr>
                    <td>
                      Gather 250 resources in a red zone while faction flagged
                    </td>
                    <Reward
                      id="T5_SKILLBOOK_GATHER_ROCK_NONTRADABLE"
                      title="Expert Quarrier Tome"
                    />
                  </tr>
                  <tr>
                    <td>Gather 250 resources in a black zone</td>
                    <Reward
                      id="T5_SKILLBOOK_GATHER_ORE_NONTRADABLE"
                      title="Expert Ore Miner Tome"
                    />
                  </tr>
                  <tr>
                    <td>Gather 250 resources in the black Mists</td>
                    <Reward
                      id="T5_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                      title="Expert Animal Skinner Tome"
                    />
                  </tr>
                  <tr>
                    <td>Gather 250 resources in the Roads of Avalon</td>
                    <Reward
                      id="T5_SKILLBOOK_GATHER_FIBER_NONTRADABLE"
                      title="Expert Fiber Harvester Tome"
                    />
                  </tr>
                  <tr>
                    <td>Gather 250 resources in Mountain regions</td>
                    <Reward
                      id="T4_SKILLBOOK_GATHER_ORE_NONTRADABLE"
                      title="Adept Ore Miner Tome"
                    />
                  </tr>
                  <tr>
                    <td>Gather 250 resources in Forest regions</td>
                    <Reward
                      id="T4_SKILLBOOK_GATHER_WOOD_NONTRADABLE"
                      title="Adept Lumberjack Tome"
                    />
                  </tr>
                  <tr>
                    <td>Gather 250 resources in Steppe regions</td>
                    <Reward
                      id="T4_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                      title="Adept Animal Skinner Tome"
                    />
                  </tr>
                  <tr>
                    <td>Gather 250 resources in Highland regions</td>
                    <Reward
                      id="T4_SKILLBOOK_GATHER_ROCK_NONTRADABLE"
                      title="Adept Quarrier Tome"
                    />
                  </tr>
                  <tr>
                    <td>Gather 250 resources in Swamp regions</td>
                    <Reward
                      id="T4_SKILLBOOK_GATHER_FIBER_NONTRADABLE"
                      title="Adept Fiber Harvester Tome"
                    />
                  </tr>
                  <tr>
                    <td>Gather 1,000 resources in Mountain regions</td>
                    <Reward
                      id="T6_SKILLBOOK_GATHER_ORE_NONTRADABLE"
                      title="Master Ore Miner Tome"
                    />
                  </tr>
                  <tr>
                    <td>Gather 1,000 resources in Forest regions</td>
                    <Reward
                      id="T6_SKILLBOOK_GATHER_WOOD_NONTRADABLE"
                      title="Master Lumberjack Tome"
                    />
                  </tr>
                  <tr>
                    <td>Gather 1,000 resources in Steppe regions</td>
                    <Reward
                      id="T6_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                      title="Master Animal Skinner Tome"
                    />
                  </tr>
                  <tr>
                    <td>Gather 1,000 resources in Highland regions</td>
                    <Reward
                      id="T6_SKILLBOOK_GATHER_ROCK_NONTRADABLE"
                      title="Master Quarrier Tome"
                    />
                  </tr>
                  <tr>
                    <td>Gather 1,000 resources in Swamp regions</td>
                    <Reward
                      id="T6_SKILLBOOK_GATHER_FIBER_NONTRADABLE"
                      title="Master Fiber Harvester Tome"
                    />
                  </tr>
                  <tr>
                    <td>Gather 1,000 resources in Black Zones</td>
                    <Reward
                      id="T4_LEARNINGPOINTS_NONTRADABLE"
                      title="Adept's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Gather 10,000 resources in Mountain regions</td>
                    <Reward
                      id="T8_SKILLBOOK_GATHER_ORE_NONTRADABLE"
                      title="Elder Ore Miner Tome"
                    />
                  </tr>
                  <tr>
                    <td>Gather 10,000 resources in Forest regions</td>
                    <Reward
                      id="T8_SKILLBOOK_GATHER_WOOD_NONTRADABLE"
                      title="Elder Lumberjack Tome"
                    />
                  </tr>
                  <tr>
                    <td>Gather 10,000 resources in Steppe regions</td>
                    <Reward
                      id="T8_SKILLBOOK_GATHER_HIDE_NONTRADABLE"
                      title="Elder Animal Skinner Tome"
                    />
                  </tr>
                  <tr>
                    <td>Gather 10,000 resources in Highland regions</td>
                    <Reward
                      id="T8_SKILLBOOK_GATHER_ROCK_NONTRADABLE"
                      title="Elder Quarrier Tome"
                    />
                  </tr>
                  <tr>
                    <td>Gather 10,000 resources in Swamp regions</td>
                    <Reward
                      id="T8_SKILLBOOK_GATHER_FIBER_NONTRADABLE"
                      title="Elder Fiber Harvester Tome"
                    />
                  </tr>
                  <tr>
                    <td>Gather 10,000 resources in Black Zones</td>
                    <Reward
                      id="T6_FOCUSPOTION_NONTRADABLE"
                      title="Master's Focus Restoration Potion"
                    />
                  </tr>
                  <tr>
                    <td>Gather 50,000 resources in Black Zones</td>
                    <Reward
                      id="T5_LEARNINGPOINTS_NONTRADABLE"
                      title="Expert's Tome of Learning"
                    />
                  </tr>
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
                  <tr>
                    <td>Buy a weapon at the Marketplace</td>
                    <Reward
                      id="T2_SKILLBOOK_NONTRADABLE"
                      title="Novice's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Buy 5 Equipment Items at the Marketplace</td>
                    <Reward
                      id="T3_SKILLBOOK_NONTRADABLE"
                      title="Journeyman's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Spend 10,000 Silver on items at the Marketplace</td>
                    <Reward
                      id="T2_LEARNINGPOINTS_NONTRADABLE"
                      title="Novice's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Spend 100,000 Silver on items at the Marketplace</td>
                    <Reward
                      id="T4_SKILLBOOK_NONTRADABLE"
                      title="Adept's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Buy 10 Equipment Items from the Marketplace</td>
                    <Reward
                      id="T4_SKILLBOOK_NONTRADABLE"
                      title="Adept's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Spend a million Silver on items at the Marketplace</td>
                    <Reward
                      id="UNIQUE_TOKEN_COMMUNITY"
                      title="Community Token (x10)"
                    />
                  </tr>
                  <tr>
                    <td>Create a Buy Order</td>
                    <Reward
                      id="T3_VANITY_CONSUMABLE_FIREWORKS_GREEN_NONTRADABLE"
                      title="Royal Green Fireworks (x3)"
                    />
                  </tr>
                  <tr>
                    <td>Spend 10 million Silver on items at the Marketplace</td>
                    <Reward
                      id="UNIQUE_UNLOCK_SHOES_VANITY_INNKEEPER_NON_TRADABLE"
                      title="Wardrobe Skin: Innkeeper's Shoes"
                    />
                  </tr>
                  <tr>
                    <td>
                      Spend 100 million Silver on items at the Marketplace
                    </td>
                    <Reward
                      id="UNIQUE_TOKEN_COMMUNITY"
                      title="Community Token (x20)"
                    />
                  </tr>
                  <tr>
                    <td>Spend a billion Silver on items at the Marketplace</td>
                    <Reward
                      id="UNIQUE_TOKEN_COMMUNITY"
                      title="Community Token (x30)"
                    />
                  </tr>
                  <tr>
                    <td>Buy 30 Equipment Items at the Marketplace</td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Buy 100 Equipment Items at the Marketplace</td>
                    <Reward
                      id="T3_VANITY_CONSUMABLE_FIREWORKS_RED_NONTRADABLE"
                      title="Royal Red Fireworks (x3)"
                    />
                  </tr>
                  <tr>
                    <td>Buy 1,000 Equipment Items at the Marketplace</td>
                    <Reward
                      id="UNIQUE_TOKEN_COMMUNITY"
                      title="Community Token (x10)"
                    />
                  </tr>
                  <tr>
                    <td>Buy 10,000 Equipment Items at the Marketplace</td>
                    <Reward
                      id="T3_LEARNINGPOINTS_NONTRADABLE"
                      title="Journeyman's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Buy 100,000 Equipment Items at the Marketplace</td>
                    <Reward
                      id="T3_LEARNINGPOINTS_NONTRADABLE"
                      title="Journeyman's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Buy 100 Items at the Marketplace</td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Buy 1,000 Items at the Marketplace</td>
                    <Reward
                      id="T3_VANITY_CONSUMABLE_FIREWORKS_YELLOW_NONTRADABLE"
                      title="Royal Yellow Fireworks (x3)"
                    />
                  </tr>
                  <tr>
                    <td>Buy 10,000 Items at the Marketplace</td>
                    <Reward
                      id="UNIQUE_TOKEN_COMMUNITY"
                      title="Community Token (x10)"
                    />
                  </tr>
                  <tr>
                    <td>Buy 100,000 Items at the Marketplace</td>
                    <Reward
                      id="T3_LEARNINGPOINTS_NONTRADABLE"
                      title="Journeyman's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Buy a million Items at the Marketplace</td>
                    <Reward
                      id="T7_SKILLBOOK_NONTRADABLE"
                      title="Grandmaster's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Buy 10 million Items at the Marketplace</td>
                    <Reward
                      id="UNIQUE_UNLOCK_OFF_VANITY_INNKEEPER_NON_TRADABLE"
                      title="Wardrobe Skin: Innkeeper's Beer Mug"
                    />
                  </tr>
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
                  <tr>
                    <td>Sell any item through the Marketplace</td>
                    <Reward
                      id="T2_SKILLBOOK_NONTRADABLE"
                      title="Novice's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Sell items for 10,000 Silver at the Marketplace</td>
                    <Reward
                      id="T3_SKILLBOOK_NONTRADABLE"
                      title="Journeyman's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Sell items worth 100,000 Silver at the Marketplace</td>
                    <Reward
                      id="T3_VANITY_CONSUMABLE_FIREWORKS_GREEN_NONTRADABLE"
                      title="Royal Green Fireworks (x3)"
                    />
                  </tr>
                  <tr>
                    <td>
                      Sell 10 Luxury Goods directly to their preferred city
                    </td>
                    <Reward
                      id="T4_SKILLBOOK_NONTRADABLE"
                      title="Adept's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Create a Sell Order</td>
                    <Reward
                      id="T3_VANITY_CONSUMABLE_FIREWORKS_BLUE_NONTRADABLE"
                      title="Royal Blue Fireworks (x3)"
                    />
                  </tr>
                  <tr>
                    <td>
                      Sell 1000 Luxury Goods directly to their preferred city
                    </td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Create 20 Sell Orders</td>
                    <Reward
                      id="T3_VANITY_CONSUMABLE_FIREWORKS_RED_NONTRADABLE"
                      title="Royal Red Fireworks (x3)"
                    />
                  </tr>
                  <tr>
                    <td>
                      Sell 9999 Luxury Goods directly to their preferred city
                    </td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Sell any item on the Black Market in Caerleon</td>
                    <Reward
                      id="T3_LEARNINGPOINTS_NONTRADABLE"
                      title="Journeyman's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Create a Sell Order on the Black Market</td>
                    <Reward
                      id="T3_VANITY_CONSUMABLE_FIREWORKS_YELLOW_NONTRADABLE"
                      title="Royal Yellow Fireworks (x3)"
                    />
                  </tr>
                  <tr>
                    <td>
                      Earn a total of 1,000,000 Silver through the Marketplace
                    </td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>
                      Earn a total of 10,000,000 Silver through the Marketplace
                    </td>
                    <Reward
                      id="T6_SKILLBOOK_NONTRADABLE"
                      title="Master's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>
                      Sell items for 100 million Silver at the Marketplace
                    </td>
                    <Reward
                      id="UNIQUE_UNLOCK_HEAD_VANITY_RICH_NOBLE_PURPLE_NON_TRADABLE"
                      title="Wardrobe Skin: Purple Rich Noble's Hat"
                    />
                  </tr>
                  <tr>
                    <td>Sell items for a billion Silver at the Marketplace</td>
                    <Reward
                      id="T7_SKILLBOOK_NONTRADABLE"
                      title="Grandmaster's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Earn a million Silver through the Black Market</td>
                    <Reward
                      id="UNIQUE_FURNITUREITEM_KNIGHT_CARPET_A"
                      title="Regal Carpet"
                    />
                  </tr>
                  <tr>
                    <td>Earn 10 million Silver through the Black Market</td>
                    <Reward
                      id="UNIQUE_UNLOCK_SKIN_OX_BLACKMARKET_NON_TRADABLE"
                      title="Transport Ox Skin: Black Market Ox"
                    />
                  </tr>
                  <tr>
                    <td>Earn 100 million Silver through the Black Market</td>
                    <Reward
                      id="T7_SKILLBOOK_NONTRADABLE"
                      title="Grandmaster's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Earn a billion Silver through the Black Market</td>
                    <Reward
                      id="UNIQUE_TOKEN_COMMUNITY"
                      title="Community Token (x100)"
                    />
                  </tr>
                  <tr>
                    <td>
                      Directly sell 9999 preferred luxury goods to Fort Sterling
                    </td>
                    <Reward
                      id="UNIQUE_TOKEN_COMMUNITY"
                      title="Community Token (x15)"
                    />
                  </tr>
                  <tr>
                    <td>
                      Directly sell 9999 preferred luxury goods to Lymhurst
                    </td>
                    <Reward
                      id="UNIQUE_TOKEN_COMMUNITY"
                      title="Community Token (x15)"
                    />
                  </tr>
                  <tr>
                    <td>
                      Directly sell 9999 preferred luxury goods to Bridgewatch
                    </td>
                    <Reward
                      id="UNIQUE_TOKEN_COMMUNITY"
                      title="Community Token (x15)"
                    />
                  </tr>
                  <tr>
                    <td>
                      Directly sell 9999 preferred luxury goods to Martlock
                    </td>
                    <Reward
                      id="UNIQUE_TOKEN_COMMUNITY"
                      title="Community Token (x15)"
                    />
                  </tr>
                  <tr>
                    <td>
                      Directly sell 9999 preferred luxury goods to Thetford
                    </td>
                    <Reward
                      id="UNIQUE_TOKEN_COMMUNITY"
                      title="Community Token (x15)"
                    />
                  </tr>
                  <tr>
                    <td>
                      Directly sell 9999 preferred luxury goods to Caerleon
                    </td>
                    <Reward
                      id="UNIQUE_TOKEN_COMMUNITY"
                      title="Community Token (x15)"
                    />
                  </tr>
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
                  <tr>
                    <td>Refine 30 T2 resources</td>
                    <Reward
                      id="T3_SKILLBOOK_NONTRADABLE"
                      title="Journeyman's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Refine 60 T3 resources</td>
                    <Reward
                      id="T3_FOCUSPOTION_NONTRADABLE"
                      title="Journeyman's Focus Restoration Potion"
                    />
                  </tr>
                  <tr>
                    <td>Refine 100 T4 resources</td>
                    <Reward
                      id="T4_FOCUSPOTION_NONTRADABLE"
                      title="Adept's Focus Restoration Potion"
                    />
                  </tr>
                  <tr>
                    <td>Transmute 10 resources to Uncommon</td>
                    <Reward
                      id="T4_SKILLBOOK_NONTRADABLE"
                      title="Adept's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Refine 200 T5 resources</td>
                    <Reward
                      id="T5_FOCUSPOTION_NONTRADABLE"
                      title="Expert's Focus Restoration Potion"
                    />
                  </tr>
                  <tr>
                    <td>Transmute 20 resources to a higher tier</td>
                    <Reward
                      id="T4_SKILLBOOK_NONTRADABLE"
                      title="Adept's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Refine 400 T6 resources</td>
                    <Reward
                      id="T6_FOCUSPOTION_NONTRADABLE"
                      title="Master's Focus Restoration Potion"
                    />
                  </tr>
                  <tr>
                    <td>Transmute 25 resources to Rare</td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Refine 400 T7 resources</td>
                    <Reward
                      id="UNIQUE_FOCUSPOTION_ADC_NONTRADABLE_01"
                      title="Grandmaster's Focus Restoration Potion"
                    />
                  </tr>
                  <tr>
                    <td>Transmute 30 resources to Exceptional</td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Refine 400 T8 resources</td>
                    <Reward
                      id="T8_FOCUSPOTION_NONTRADABLE"
                      title="Elder's Focus Restoration Potion"
                    />
                  </tr>
                  <tr>
                    <td>Transmute 50 resources to Pristine</td>
                    <Reward
                      id="T6_SKILLBOOK_NONTRADABLE"
                      title="Master's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Use the Fort Sterling refining bonus</td>
                    <Reward
                      id="T4_FOCUSPOTION_NONTRADABLE"
                      title="Adept's Focus Restoration Potion"
                    />
                  </tr>
                  <tr>
                    <td>Use the Lymhurst refining bonus</td>
                    <Reward
                      id="T4_FOCUSPOTION_NONTRADABLE"
                      title="Adept's Focus Restoration Potion"
                    />
                  </tr>
                  <tr>
                    <td>Use the Bridgewatch refining bonus</td>
                    <Reward
                      id="T4_FOCUSPOTION_NONTRADABLE"
                      title="Adept's Focus Restoration Potion"
                    />
                  </tr>
                  <tr>
                    <td>Use the Martlock refining bonus</td>
                    <Reward
                      id="T4_FOCUSPOTION_NONTRADABLE"
                      title="Adept's Focus Restoration Potion"
                    />
                  </tr>
                  <tr>
                    <td>Use the Thetford refining bonus</td>
                    <Reward
                      id="T4_FOCUSPOTION_NONTRADABLE"
                      title="Adept's Focus Restoration Potion"
                    />
                  </tr>
                  <tr>
                    <td>Refine 1,000 Resources</td>
                    <Reward
                      id="T4_SKILLBOOK_NONTRADABLE"
                      title="Adept's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Refine 5,000 Resources</td>
                    <Reward
                      id="T3_FOCUSPOTION_NONTRADABLE"
                      title="Journeyman's Focus Restoration Potion"
                    />
                  </tr>
                  <tr>
                    <td>Refine 10,000 Resources</td>
                    <Reward
                      id="T4_FOCUSPOTION_NONTRADABLE"
                      title="Adept's Focus Restoration Potion"
                    />
                  </tr>
                  <tr>
                    <td>Refine 50,000 Resources</td>
                    <Reward
                      id="T5_FOCUSPOTION_NONTRADABLE"
                      title="Expert's Focus Restoration Potion"
                    />
                  </tr>
                  <tr>
                    <td>Refine 100,000 Resources</td>
                    <Reward
                      id="UNIQUE_FOCUSPOTION_ADC_NONTRADABLE_01"
                      title="Grandmaster's Focus Restoration Potion"
                    />
                  </tr>
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
                  <tr>
                    <td>Craft 3 T2 Equipment Items</td>
                    <Reward
                      id="T3_SKILLBOOK_NONTRADABLE"
                      title="Journeyman's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Craft 10 T3 Equipment Items</td>
                    <Reward
                      id="T3_FOCUSPOTION_NONTRADABLE"
                      title="Journeyman's Focus Restoration Potion"
                    />
                  </tr>
                  <tr>
                    <td>Craft an item in a Royal City</td>
                    <Reward
                      id="T4_SKILLBOOK_NONTRADABLE"
                      title="Adept's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Eat a salad that improves your crafting</td>
                    <Reward
                      id="T3_SKILLBOOK_NONTRADABLE"
                      title="Journeyman's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Craft 40 T4 Equipment Items</td>
                    <Reward
                      id="T4_FOCUSPOTION_NONTRADABLE"
                      title="Adept's Focus Restoration Potion"
                    />
                  </tr>
                  <tr>
                    <td>Use a city&apos;s crafting bonus</td>
                    <Reward
                      id="T3_SKILLBOOK_NONTRADABLE"
                      title="Journeyman's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Craft an Outstanding quality Equipment Item</td>
                    <Reward
                      id="UNIQUE_TOKEN_COMMUNITY"
                      title="Community Token (x10)"
                    />
                  </tr>
                  <tr>
                    <td>Craft 60 T5 Equipment Items</td>
                    <Reward
                      id="T5_FOCUSPOTION_NONTRADABLE"
                      title="Expert's Focus Restoration Potion"
                    />
                  </tr>
                  <tr>
                    <td>Craft 20 Uncommon items</td>
                    <Reward
                      id="UNIQUE_FURNITUREITEM_HERETIC_STOVE_A"
                      title="Heretic Stove"
                    />
                  </tr>
                  <tr>
                    <td>Craft an Excellent quality Equipment Item</td>
                    <Reward
                      id="T3_LEARNINGPOINTS_NONTRADABLE"
                      title="Journeyman's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Craft 80 T6 Equipment Items</td>
                    <Reward
                      id="T6_FOCUSPOTION_NONTRADABLE"
                      title="Master's Focus Restoration Potion"
                    />
                  </tr>
                  <tr>
                    <td>Craft 30 Rare items</td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Craft a Masterpiece quality Equipment Item</td>
                    <Reward
                      id="T7_SKILLBOOK_NONTRADABLE"
                      title="Grandmaster's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Craft 100 T7 Equipment Items</td>
                    <Reward
                      id="UNIQUE_FOCUSPOTION_ADC_NONTRADABLE_01"
                      title="Grandmaster's Focus Restoration Potion"
                    />
                  </tr>
                  <tr>
                    <td>Craft 50 Epic items</td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Use a crafting bonus in a Hideout</td>
                    <Reward
                      id="UNIQUE_TOKEN_COMMUNITY"
                      title="Community Token (x50)"
                    />
                  </tr>
                  <tr>
                    <td>Craft 100 T8 Equipment Items</td>
                    <Reward
                      id="T8_FOCUSPOTION_NONTRADABLE"
                      title="Elder's Focus Restoration Potion"
                    />
                  </tr>
                  <tr>
                    <td>Craft 50 Pristine items</td>
                    <Reward
                      id="T6_SKILLBOOK_NONTRADABLE"
                      title="Master's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Craft a Pristine T8 item</td>
                    <Reward
                      id="T4_LEARNINGPOINTS_NONTRADABLE"
                      title="Adept's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Craft a Pristine T8 Masterpiece</td>
                    <Reward
                      id="UNIQUE_TOKEN_COMMUNITY"
                      title="Community Token (x500)"
                    />
                  </tr>
                  <tr>
                    <td>Craft Items worth 10,000 Fame</td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Craft Items worth 100,000 Fame</td>
                    <Reward
                      id="T5_FOCUSPOTION_NONTRADABLE"
                      title="Expert's Focus Restoration Potion"
                    />
                  </tr>
                  <tr>
                    <td>Craft items worth a million Fame</td>
                    <Reward
                      id="UNIQUE_FOCUSPOTION_ADC_NONTRADABLE_01"
                      title="Grandmaster's Focus Restoration Potion"
                    />
                  </tr>
                  <tr>
                    <td>Craft items worth 10 million Fame</td>
                    <Reward
                      id="T6_FOCUSPOTION_NONTRADABLE"
                      title="Master's Focus Restoration Potion (x2)"
                    />
                  </tr>
                  <tr>
                    <td>Craft items worth 100 million Fame</td>
                    <Reward
                      id="UNIQUE_FOCUSPOTION_ADC_NONTRADABLE_01"
                      title="Grandmaster's Focus Restoration Potion (x3)"
                    />
                  </tr>
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
                  <tr>
                    <td>Study an item</td>
                    <Reward
                      id="T2_SKILLBOOK_NONTRADABLE"
                      title="Novice's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Salvage an item</td>
                    <Reward
                      id="T2_SKILLBOOK_NONTRADABLE"
                      title="Novice's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Reroll an item at a Repair Station</td>
                    <Reward
                      id="T2_SKILLBOOK_NONTRADABLE"
                      title="Novice's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>
                      Meld resources into an Artifact at the Artifact Foundry
                    </td>
                    <Reward
                      id="T4_SKILLBOOK_NONTRADABLE"
                      title="Adept's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Meld 10 Soul Artifacts</td>
                    <Reward
                      id="UNIQUE_FURNITUREITEM_ADC_GLASS_SPHERE_A"
                      title="Glass Sphere"
                    />
                  </tr>
                  <tr>
                    <td>Meld 30 T5 Artifacts</td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Meld 100 T6 Hunter Artifacts</td>
                    <Reward
                      id="T6_SKILLBOOK_NONTRADABLE"
                      title="Master's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Meld 100 T8 Avalonian Artifacts</td>
                    <Reward
                      id="UNIQUE_TOKEN_COMMUNITY"
                      title="Community Token (x30)"
                    />
                  </tr>
                  <tr>
                    <td>Create 50 Souls with Transmutation</td>
                    <Reward
                      id="T4_FOCUSPOTION_NONTRADABLE"
                      title="Adept's Focus Restoration Potion"
                    />
                  </tr>
                  <tr>
                    <td>Create a T8 Dungeon Map with Transmutation</td>
                    <Reward
                      id="T6_SKILLBOOK_NONTRADABLE"
                      title="Master's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>
                      Create a Masterpiece item by rerolling it at a Repair
                      Station
                    </td>
                    <Reward
                      id="T4_FOCUSPOTION_NONTRADABLE"
                      title="Adept's Focus Restoration Potion"
                    />
                  </tr>
                  <tr>
                    <td>
                      Reroll a full stack of 999 items at a Repair Station
                    </td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Salvage 100 items</td>
                    <Reward
                      id="T4_SKILLBOOK_NONTRADABLE"
                      title="Adept's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Salvage 1,000 items</td>
                    <Reward
                      id="UNIQUE_FURNITUREITEM_ADC_CARNIVAL_ARCHWAY_A"
                      title="Carnival Arch"
                    />
                  </tr>
                  <tr>
                    <td>Salvage 10,000 items</td>
                    <Reward
                      id="T6_SKILLBOOK_NONTRADABLE"
                      title="Master's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Study 100 items</td>
                    <Reward
                      id="T2_LEARNINGPOINTS_NONTRADABLE"
                      title="Novice's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Study 1,000 items</td>
                    <Reward
                      id="T4_FOCUSPOTION_NONTRADABLE"
                      title="Adept's Focus Restoration Potion"
                    />
                  </tr>
                  <tr>
                    <td>Study 10,000 items</td>
                    <Reward
                      id="T3_LEARNINGPOINTS_NONTRADABLE"
                      title="Journeyman's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Reroll 100 items</td>
                    <Reward
                      id="T4_SKILLBOOK_NONTRADABLE"
                      title="Adept's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Reroll 1,000 items</td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Reroll 10,000 items</td>
                    <Reward
                      id="T6_SKILLBOOK_NONTRADABLE"
                      title="Master's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Reroll 100,000 items</td>
                    <Reward
                      id="T7_SKILLBOOK_NONTRADABLE"
                      title="Grandmaster's Tome of Insight"
                    />
                  </tr>
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
                  <tr>
                    <td>Own 100,000 Silver</td>
                    <Reward
                      id="T4_SKILLBOOK_NONTRADABLE"
                      title="Adept's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Own 500,000 Silver</td>
                    <Reward
                      id="UNIQUE_TOKEN_COMMUNITY"
                      title="Community Token (x10)"
                    />
                  </tr>
                  <tr>
                    <td>Own 5 Gold</td>
                    <Reward
                      id="T3_VANITY_CONSUMABLE_FIREWORKS_YELLOW_NONTRADABLE"
                      title="Royal Yellow Fireworks (x3)"
                    />
                  </tr>
                  <tr>
                    <td>Own 1 million Silver</td>
                    <Reward
                      id="T6_SKILLBOOK_NONTRADABLE"
                      title="Master's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Own 5 million Silver</td>
                    <Reward
                      id="T6_SKILLBOOK_NONTRADABLE"
                      title="Master's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Own 10 million Silver</td>
                    <Reward
                      id="UNIQUE_UNLOCK_HEAD_VANITY_DRESS_BLUE_NON_TRADABLE"
                      title="Wardrobe Skin: Blue Princess Hat"
                    />
                  </tr>
                  <tr>
                    <td>Own 50 million Silver</td>
                    <Reward
                      id="T6_SKILLBOOK_NONTRADABLE"
                      title="Master's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Own 100 million Silver</td>
                    <Reward
                      id="UNIQUE_UNLOCK_ARMOR_VANITY_DRESS_BLUE_NON_TRADABLE"
                      title="Wardrobe Skin: Blue Princess Dress"
                    />
                  </tr>
                  <tr>
                    <td>Own 500 million Silver</td>
                    <Reward
                      id="UNIQUE_UNLOCK_SKIN_OX_BISON_AH_NON_TRADABLE"
                      title="Transport Ox Skin: Auction House Ox"
                    />
                  </tr>
                  <tr>
                    <td>Own 1 billion Silver</td>
                    <Reward
                      id="T5_LEARNINGPOINTS_NONTRADABLE"
                      title="Expert's Tome of Learning"
                    />
                  </tr>
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
                  <tr>
                    <td>Bid at least 1 million Silver on a city plot</td>
                    <Reward
                      id="UNIQUE_FURNITUREITEM_MORGANA_CARPET_A"
                      title="Morgana Carpet"
                    />
                  </tr>
                  <tr>
                    <td>Own a city plot</td>
                    <Reward
                      id="T4_LEARNINGPOINTS_NONTRADABLE"
                      title="Adept's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Collect 1 million Silver from city plots</td>
                    <Reward
                      id="T6_SKILLBOOK_NONTRADABLE"
                      title="Master's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Keep a city plot you own in an auction cycle</td>
                    <Reward
                      id="T7_SKILLBOOK_NONTRADABLE"
                      title="Grandmaster's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Collect 3 million Silver from City Plots</td>
                    <Reward
                      id="T7_SKILLBOOK_NONTRADABLE"
                      title="Grandmaster's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Own 3 plots in the same city simultaneously</td>
                    <Reward
                      id="UNIQUE_UNLOCK_CAPE_VANITY_SNOWLEOPARD_NON_TRADABLE"
                      title="Wardrobe Skin: Snow Leopard Cape"
                    />
                  </tr>
                  <tr>
                    <td>Collect 10 million Silver from city plots</td>
                    <Reward
                      id="T8_SKILLBOOK_NONTRADABLE"
                      title="Elder's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Collect 30 million Silver from City Plots</td>
                    <Reward
                      id="T6_FOCUSPOTION_NONTRADABLE"
                      title="Master's Focus Restoration Potion"
                    />
                  </tr>
                  <tr>
                    <td>Own 5 plots in the same city simultaneously</td>
                    <Reward
                      id="T8_SKILLBOOK_NONTRADABLE"
                      title="Elder's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Collect 100 million silver from city plots</td>
                    <Reward
                      id="T5_LEARNINGPOINTS_NONTRADABLE"
                      title="Expert's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Collect 300 million Silver from City Plots</td>
                    <Reward
                      id="UNIQUE_FOCUSPOTION_ADC_NONTRADABLE_01"
                      title="Grandmaster's Focus Restoration Potion"
                    />
                  </tr>
                  <tr>
                    <td>Collect 1 billion silver from city plots</td>
                    <Reward
                      id="UNIQUE_UNLOCK_SKIN_GIANTSTAG_ALPACA_BROWN"
                      title="Stag Skin: Brown Alpaca"
                    />
                  </tr>
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
              Exploration (129)
            </AccordionHeader>
            <AccordionBody accordionId="exploration">
              <h4>Cities (10)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Visit a Royal City</td>
                    <Reward
                      id="T3_SKILLBOOK_NONTRADABLE"
                      title="Journeyman's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Visit three Royal Cities</td>
                    <Reward
                      id="UNIQUE_TOKEN_COMMUNITY"
                      title="Community Token (x10)"
                    />
                  </tr>
                  <tr>
                    <td>Visit Caerleon</td>
                    <Reward
                      id="T4_SKILLBOOK_NONTRADABLE"
                      title="Adept's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Visit a Portal Town</td>
                    <Reward
                      id="T3_VANITY_CONSUMABLE_FIREWORKS_YELLOW_NONTRADABLE"
                      title="Royal Yellow Fireworks (x3)"
                    />
                  </tr>
                  <tr>
                    <td>Use the Invisibility Shrine in a Portal Town</td>
                    <Reward
                      id="T3_SKILLBOOK_NONTRADABLE"
                      title="Journeyman's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Find the lost city of Brecilien</td>
                    <Reward
                      id="T5_SILVERBAG_NONTRADABLE"
                      title="Expert's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Purchase an item from Eralia Wayfarer in Brecilien</td>
                    <Reward
                      id="T3_SKILLBOOK_NONTRADABLE"
                      title="Journeyman's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>
                      Visit all six Royal Cities
                      <br />
                      <span className="text-muted">
                        Martlock, Lymhurst, Thetford, Fort Sterling,
                        Bridgewatch, Caerleon
                      </span>
                    </td>
                    <Reward
                      id="UNIQUE_UNLOCK_SHOES_VANITY_PRIEST_NON_TRADABLE"
                      title="Wardrobe Skin: Monk's Sandals"
                    />
                  </tr>
                  <tr>
                    <td>Visit a Rest in the Outlands</td>
                    <Reward
                      id="T3_LEARNINGPOINTS_NONTRADABLE"
                      title="Journeyman's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>
                      Visit all Rests in the Outlands
                      <br />
                      <span className="text-muted">
                        Arthur&apos;s Rest, Merlyn&apos;s Rest, Morgana&apos;s
                        Rest
                      </span>
                    </td>
                    <Reward
                      id="T4_LEARNINGPOINTS_NONTRADABLE"
                      title="Adept's Tome of Learning"
                    />
                  </tr>
                </tbody>
              </Table>

              <h4>Travel (28)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Ride a Horse</td>
                    <Reward
                      id="T3_SKILLBOOK_NONTRADABLE"
                      title="Journeyman's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Find a Hidden Treasure in the open world</td>
                    <Reward
                      id="T3_SILVERBAG_NONTRADABLE"
                      title="Journeyman's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Ride an Ox</td>
                    <Reward
                      id="T3_SKILLBOOK_NONTRADABLE"
                      title="Journeyman's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Travel 20 kilometers</td>
                    <Reward
                      id="T3_SKILLBOOK_NONTRADABLE"
                      title="Journeyman's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Ride a Direwolf</td>
                    <Reward
                      id="T4_SKILLBOOK_NONTRADABLE"
                      title="Adept's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Find 5 Hidden Treasures in the open world</td>
                    <Reward
                      id="T3_LEARNINGPOINTS_NONTRADABLE"
                      title="Journeyman's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>
                      Ride an Adventurer&apos;s Challenge Mount
                      <br />
                      <span className="text-muted">
                        Frost Ram, Saddled Terrorbird, Grizzly Bear, Black
                        Panther, Morgana Raven, Gallant Horse, Spectral
                        Direboar, Divine Owl, Heretic Combat Mule, Spectral Bat,
                        Pest Lizard, Snow Husky
                      </span>
                    </td>
                    <Reward
                      id="T4_SKILLBOOK_NONTRADABLE"
                      title="Adept's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Find 10 Hidden Treasures in the open world</td>
                    <Reward
                      id="T5_SILVERBAG_NONTRADABLE"
                      title="Expert's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Ride a Faction Warfare mount</td>
                    <Reward
                      id="T3_LEARNINGPOINTS_NONTRADABLE"
                      title="Journeyman's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Find 20 Hidden Treasures in the open world</td>
                    <Reward
                      id="T6_SILVERBAG_NONTRADABLE"
                      title="Master's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Ride a Mystic Owl from Brecilien</td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Find 40 Hidden Treasures in the open world</td>
                    <Reward
                      id="T7_SILVERBAG_NONTRADABLE"
                      title="Grandmaster's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Ride an Elite Faction Warfare mount</td>
                    <Reward
                      id="T6_SKILLBOOK_NONTRADABLE"
                      title="Master's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Find 65 Hidden Treasures in the open world</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Ride a Battle Mount</td>
                    <Reward
                      id="T6_SKILLBOOK_NONTRADABLE"
                      title="Master's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Find 100 Hidden Treasures in the open world</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x5)"
                    />
                  </tr>
                  <tr>
                    <td>
                      Ride all Faction Warfare Mounts
                      <br />
                      <span className="text-muted">
                        Saddled Moabird, Saddled Winter Bear, Saddled Wild Boar,
                        Saddled Bighorn Ram, Saddled Swamp Salamander, Saddled
                        Greywolf, Elite Terrorbird, Elite Winter Bear, Elite
                        Wild Boar, Elite Bighorn Ram, Elite Swamp Salamander,
                        Elite Greywolf
                      </span>
                    </td>
                    <Reward
                      id="T3_LEARNINGPOINTS_NONTRADABLE"
                      title="Journeyman's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Find 200 Hidden Treasures in the open world</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x8)"
                    />
                  </tr>
                  <tr>
                    <td>Ride a Transport Mammoth</td>
                    <Reward
                      id="T7_SKILLBOOK_NONTRADABLE"
                      title="Grandmaster's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Find 500 Hidden Treasures in the open world</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x15)"
                    />
                  </tr>
                  <tr>
                    <td>Ride a Command Mammoth</td>
                    <Reward
                      id="T7_SKILLBOOK_NONTRADABLE"
                      title="Grandmaster's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Travel 50 kilometers</td>
                    <Reward
                      id="T4_SKILLBOOK_NONTRADABLE"
                      title="Adept's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Travel 100 kilometers</td>
                    <Reward
                      id="UNIQUE_UNLOCK_OFF_VANITY_PRIEST_NON_TRADABLE"
                      title="Wardrobe Skin: Monk's Walking Staff"
                    />
                  </tr>
                  <tr>
                    <td>Travel 200 kilometers</td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Travel 500 kilometers</td>
                    <Reward
                      id="UNIQUE_FURNITUREITEM_ADC_CARNIVAL_MASK_CART"
                      title="Carnival Costume Cart"
                    />
                  </tr>
                  <tr>
                    <td>Travel 1,000 kilometers</td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Travel 3,000 Kilometers</td>
                    <Reward
                      id="T6_SKILLBOOK_NONTRADABLE"
                      title="Master's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Travel 10,000 Kilometers</td>
                    <Reward
                      id="UNIQUE_FURNITUREITEM_ADC_STATUE_MOUNTED_DIREWOLF_B"
                      title="Wolf Rider Statue (R)"
                    />
                  </tr>
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
                  <tr>
                    <td>Enter a Yellow Zone</td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Earn 10,000 Fame in Yellow Zones</td>
                    <Reward
                      id="T2_LEARNINGPOINTS_NONTRADABLE"
                      title="Novice's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Enter a Red Zone</td>
                    <Reward
                      id="T3_LEARNINGPOINTS_NONTRADABLE"
                      title="Journeyman's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Earn 20,000 Fame in Red Zones</td>
                    <Reward
                      id="UNIQUE_UNLOCK_SKIN_HORSE_KEEPER_NON_TRADABLE"
                      title="Riding Horse Skin: Keeper Horse"
                    />
                  </tr>
                  <tr>
                    <td>Enter a black zone</td>
                    <Reward
                      id="T6_SKILLBOOK_NONTRADABLE"
                      title="Master's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Use the Journey Back ability in a Black Zone</td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Earn 40,000 Fame in Black Zones</td>
                    <Reward
                      id="T3_LEARNINGPOINTS_NONTRADABLE"
                      title="Journeyman's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Earn 80,000 Fame in Quality Level 2 Black Zones</td>
                    <Reward
                      id="T4_LEARNINGPOINTS_NONTRADABLE"
                      title="Adept's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Earn 120,000 Fame in Quality Level 3 Black Zones</td>
                    <Reward
                      id="T4_LEARNINGPOINTS_NONTRADABLE"
                      title="Adept's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Earn 250,000 Fame in Quality Level 4 Black Zones</td>
                    <Reward
                      id="T4_LEARNINGPOINTS_NONTRADABLE"
                      title="Adept's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Earn 500,000 Fame in Quality Level 5 Black Zones</td>
                    <Reward
                      id="T5_LEARNINGPOINTS_NONTRADABLE"
                      title="Expert's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Earn a million Fame in Quality Level 6 Black Zones</td>
                    <Reward
                      id="T5_LEARNINGPOINTS_NONTRADABLE"
                      title="Expert's Tome of Learning"
                    />
                  </tr>
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
                  <tr>
                    <td>Reach the first positive reputation level</td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Reach the reputation level: Virtuous</td>
                    <Reward
                      id="T6_SILVERBAG_NONTRADABLE"
                      title="Master's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Reach the reputation level: Noble</td>
                    <Reward
                      id="T7_SILVERBAG_NONTRADABLE"
                      title="Grandmaster's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Reach maximum reputation level</td>
                    <Reward
                      id="UNIQUE_REPAIRPOWDER_ADC_GENERAL_01_NONTRADEABLE"
                      title="Scroll of Repair"
                    />
                  </tr>
                  <tr>
                    <td>Reach the first negative reputation level</td>
                    <Reward
                      id="T6_SKILLBOOK_NONTRADABLE"
                      title="Master's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Reach the reputation level: Nefarious</td>
                    <Reward
                      id="T7_SKILLBOOK_NONTRADABLE"
                      title="Grandmaster's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Reach minimum reputation level</td>
                    <Reward
                      id="UNIQUE_UNLOCK_ARMOR_VANITY_ENTERTAINER_NON_TRADABLE"
                      title="Wardrobe Skin: Entertainer's Costume"
                    />
                  </tr>
                </tbody>
              </Table>

              <h4>Mists (32)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 500 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Follow a Will o&apos; Wisp into the Mists</td>
                    <Reward
                      id="T3_SKILLBOOK_NONTRADABLE"
                      title="Journeyman's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Rescue 10 Wisps</td>
                    <Reward
                      id="T5_SILVERBAG_NONTRADABLE"
                      title="Expert's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Open 5 Small Caches</td>
                    <Reward
                      id="T4_SKILLBOOK_NONTRADABLE"
                      title="Adept's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Open 5 Medium Caches</td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Enter Knightfall Abbey</td>
                    <Reward
                      id="T3_SKILLBOOK_NONTRADABLE"
                      title="Journeyman's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Open 3 chests in Knightfall Abbey</td>
                    <Reward
                      id="T4_SKILLBOOK_NONTRADABLE"
                      title="Adept's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Deliver a Weakened Wisp to a Sanctuary</td>
                    <Reward
                      id="T6_SILVERBAG_NONTRADABLE"
                      title="Master's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Gain Accepted status with Brecilien</td>
                    <Reward
                      id="T5_SILVERBAG_NONTRADABLE"
                      title="Expert's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Earn 50,000 Fame in Solo Lethal Mists</td>
                    <Reward
                      id="T3_LEARNINGPOINTS_NONTRADABLE"
                      title="Journeyman's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Rescue 30 Wisps in Solo Lethal Mists</td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Deliver a Weakened Wisp in Lethal Mists</td>
                    <Reward
                      id="T6_SILVERBAG_NONTRADABLE"
                      title="Master's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Open 20 chests in Knightfall Abbey</td>
                    <Reward
                      id="T6_SILVERBAG_NONTRADABLE"
                      title="Master's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Gain 50,000 Fame in Greater Mists</td>
                    <Reward
                      id="T3_LEARNINGPOINTS_NONTRADABLE"
                      title="Journeyman's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Rescue 50 Wisps in Greater Mists</td>
                    <Reward
                      id="T6_SKILLBOOK_NONTRADABLE"
                      title="Master's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Deliver 5 Weakened Wisps in Greater Mists</td>
                    <Reward
                      id="T7_SILVERBAG_NONTRADABLE"
                      title="Grandmaster's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Open 100 chests in Knightfall Abbey</td>
                    <Reward
                      id="T7_SILVERBAG_NONTRADABLE"
                      title="Grandmaster's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Deliver 50 Weakened Wisps in Solo Lethal Mists</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Earn 500,000 fame in Solo Lethal Mists</td>
                    <Reward
                      id="T5_SILVERBAG_NONTRADABLE"
                      title="Expert's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Earn a million Fame in Solo Lethal Mists</td>
                    <Reward
                      id="T6_SILVERBAG_NONTRADABLE"
                      title="Master's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Earn 5 million Fame in Solo Lethal Mists</td>
                    <Reward
                      id="T7_SILVERBAG_NONTRADABLE"
                      title="Grandmaster's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Earn 10 million Fame in Solo Lethal Mists</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Earn 500,000 Fame in Greater Mists</td>
                    <Reward
                      id="T5_SILVERBAG_NONTRADABLE"
                      title="Expert's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Earn a million Fame in Greater Mists</td>
                    <Reward
                      id="T6_SILVERBAG_NONTRADABLE"
                      title="Master's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Earn 5 million Fame in Greater Mists</td>
                    <Reward
                      id="T7_SILVERBAG_NONTRADABLE"
                      title="Grandmaster's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Earn 10 million Fame in Greater Mists</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Open 500 chests in Knightfall Abbey</td>
                    <Reward
                      id="T7_SKILLBOOK_NONTRADABLE"
                      title="Grandmaster's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Open 2,000 chests in Knightfall Abbey</td>
                    <Reward
                      id="T8_SKILLBOOK_NONTRADABLE"
                      title="Elder's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Get &apos;Welcomed&apos; Brecilien standing</td>
                    <Reward
                      id="T5_SILVERBAG_NONTRADABLE"
                      title="Expert's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Get &apos;Favored&apos; Brecilien standing</td>
                    <Reward
                      id="T6_SILVERBAG_NONTRADABLE"
                      title="Master's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Gain &apos;Esteemed&apos; Brecilien standing</td>
                    <Reward
                      id="T7_SILVERBAG_NONTRADABLE"
                      title="Grandmaster's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Gain &apos;Venerated&apos; Brecilien standing</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>
                      Kill a &quot;Mysterious Stranger&quot; that&apos;s your
                      friend or ally
                    </td>
                    <Reward
                      id="UNIQUE_FURNITUREITEM_ADC_GRIM_WEEPINGWOMAN"
                      title="Weeping Woman Statue"
                    />
                  </tr>
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
                  <tr>
                    <td>Earn 100 Might</td>
                    <Reward
                      id="T4_SKILLBOOK_NONTRADABLE"
                      title="Adept's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Earn 50 Favor</td>
                    <Reward
                      id="T4_SKILLBOOK_NONTRADABLE"
                      title="Adept's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>
                      Trade your Favor for an item at the Energy Manipulator
                    </td>
                    <Reward
                      id="T3_SKILLBOOK_NONTRADABLE"
                      title="Journeyman's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Earn 1,000 Might</td>
                    <Reward
                      id="T3_LEARNINGPOINTS_NONTRADABLE"
                      title="Journeyman's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>
                      Trade your Favor for a Conqueror&apos;s Chest at the
                      Energy Manipulator
                    </td>
                    <Reward
                      id="T3_SKILLBOOK_NONTRADABLE"
                      title="Journeyman's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Earn 8,000 Might</td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Earn 5,000 Favor</td>
                    <Reward
                      id="T6_SILVERBAG_NONTRADABLE"
                      title="Master's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Earn 40,000 Might</td>
                    <Reward
                      id="T6_SKILLBOOK_NONTRADABLE"
                      title="Master's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Earn 100,000 Might</td>
                    <Reward
                      id="T7_SILVERBAG_NONTRADABLE"
                      title="Grandmaster's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Earn 200,000 Might</td>
                    <Reward
                      id="T7_SKILLBOOK_NONTRADABLE"
                      title="Grandmaster's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Earn 120,000 Favor</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Earn 1 million Might</td>
                    <Reward
                      id="T8_SKILLBOOK_NONTRADABLE"
                      title="Elder's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Earn 2 million Might</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x5)"
                    />
                  </tr>
                  <tr>
                    <td>Earn 5 million Might</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x25)"
                    />
                  </tr>
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
                  <tr>
                    <td>Enter a Road of Avalon</td>
                    <Reward
                      id="T4_SKILLBOOK_NONTRADABLE"
                      title="Adept's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 50 mobs in the Roads of Avalon</td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Open an Avalonian Chest in the Roads of Avalon</td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Enter a Deep Road of Avalon</td>
                    <Reward
                      id="T2_LEARNINGPOINTS_NONTRADABLE"
                      title="Novice's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 500 mobs in the Roads of Avalon</td>
                    <Reward
                      id="T6_SILVERBAG_NONTRADABLE"
                      title="Master's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Open a Blue Avalonian Chest in the Roads of Avalon</td>
                    <Reward
                      id="UNIQUE_FURNITUREITEM_XMAS_PRESENT"
                      title="Present Box"
                    />
                  </tr>
                  <tr>
                    <td>Open a Rare Avalonian Chest in the Roads of Avalon</td>
                    <Reward
                      id="T6_SKILLBOOK_NONTRADABLE"
                      title="Master's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Open 30 Green Chests in Roads of Avalon</td>
                    <Reward
                      id="T7_SILVERBAG_NONTRADABLE"
                      title="Grandmaster's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 2,000 mobs in the Roads of Avalon</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>
                      Open a Yellow Avalonian Chest in the Roads of Avalon
                    </td>
                    <Reward
                      id="T6_SKILLBOOK_NONTRADABLE"
                      title="Master's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 5,000 mobs in the Roads of Avalon</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x3)"
                    />
                  </tr>
                  <tr>
                    <td>Open 50 Blue Chests in Roads of Avalon</td>
                    <Reward
                      id="T6_SKILLBOOK_NONTRADABLE"
                      title="Master's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Open 100 Green Chests in Roads of Avalon</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x5)"
                    />
                  </tr>
                  <tr>
                    <td>Open a Legendary Chest in the Roads</td>
                    <Reward
                      id="T3_LEARNINGPOINTS_NONTRADABLE"
                      title="Journeyman's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Open 150 Blue Chests in Roads of Avalon</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x23)"
                    />
                  </tr>
                  <tr>
                    <td>
                      Open a Legendary Yellow Chest in the Roads of Avalon
                    </td>
                    <Reward
                      id="T7_SKILLBOOK_NONTRADABLE"
                      title="Grandmaster's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Open 50 Yellow Chests in Roads of Avalon</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x15)"
                    />
                  </tr>
                  <tr>
                    <td>Open 500 Green Chests in Roads of Avalon</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x20)"
                    />
                  </tr>
                  <tr>
                    <td>Open 150 Yellow Chests in Roads of Avalon</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x20)"
                    />
                  </tr>
                  <tr>
                    <td>Open 500 Blue Chests in Roads of Avalon</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x25)"
                    />
                  </tr>
                  <tr>
                    <td>Open 500 Yellow Chests in Roads of Avalon</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x25)"
                    />
                  </tr>
                  <tr>
                    <td>Earn 1 million Fame in the Roads of Avalon</td>
                    <Reward
                      id="T7_SILVERBAG_NONTRADABLE"
                      title="Grandmaster's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Earn 3 million Fame in the Roads of Avalon</td>
                    <Reward
                      id="T7_SKILLBOOK_NONTRADABLE"
                      title="Grandmaster's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Earn 10 million Fame in the Roads of Avalon</td>
                    <Reward
                      id="T8_SKILLBOOK_NONTRADABLE"
                      title="Elder's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Earn 30 million Fame in the Roads of Avalon</td>
                    <Reward
                      id="UNIQUE_TOKEN_COMMUNITY"
                      title="Community Token (x50)"
                    />
                  </tr>
                  <tr>
                    <td>Earn 100 million Fame in the Roads of Avalon</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x15)"
                    />
                  </tr>
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
                  <tr>
                    <td>Win your first Arena match</td>
                    <Reward
                      id="T3_SILVERBAG_NONTRADABLE"
                      title="Journeyman's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Win 5 Arena or Crystal Arena Matches</td>
                    <Reward
                      id="T4_SKILLBOOK_NONTRADABLE"
                      title="Adept's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Win 10 Arena or Crystal Arena Matches</td>
                    <Reward
                      id="T4_SILVERBAG_NONTRADABLE"
                      title="Adept's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>
                      Deal 15,000 damage in a single Arena or Crystal Arena
                      match
                    </td>
                    <Reward
                      id="T4_SKILLBOOK_NONTRADABLE"
                      title="Adept's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Win 20 Arena or Crystal Arena Matches</td>
                    <Reward
                      id="QUESTITEM_TOKEN_ARENA_CRYSTAL"
                      title="Arena Sigil (x20)"
                    />
                  </tr>
                  <tr>
                    <td>
                      Get 5 kills in a single Arena or Crystal Arena match
                    </td>
                    <Reward
                      id="T4_SKILLBOOK_NONTRADABLE"
                      title="Adept's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Win 35 Arena or Crystal Arena Matches</td>
                    <Reward
                      id="T5_SILVERBAG_NONTRADABLE"
                      title="Expert's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>
                      Capture 4 Runestones in a single Arena or Crystal Arena
                      match
                    </td>
                    <Reward
                      id="T4_SKILLBOOK_NONTRADABLE"
                      title="Adept's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Win 50 Arena or Crystal Arena Matches</td>
                    <Reward
                      id="T1_KILL_EMOTE_TOMBSTONE_CHARGES_NONTRADABLE"
                      title="Tombstone Victory Emote Charge (x10)"
                    />
                  </tr>
                  <tr>
                    <td>
                      Deal 22,000 damage in an single Arena or Crystal Arena
                      match
                    </td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Win 75 Arena or Crystal Arena Matches</td>
                    <Reward
                      id="QUESTITEM_TOKEN_ARENA_CRYSTAL"
                      title="Arena Sigil (x30)"
                    />
                  </tr>
                  <tr>
                    <td>
                      Take 20,000 damage without dying in a single Arena or
                      Crystal Arena match
                    </td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Win 100 Arena or Crystal Arena matches</td>
                    <Reward
                      id="T1_KILL_EMOTE_SWORD_CHARGES_NONTRADABLE"
                      title="Sword Victory Emote Charge (x20)"
                    />
                  </tr>
                  <tr>
                    <td>
                      Heal 15,000 health in a single Arena or Crystal Arena
                      match
                    </td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Win 150 Arena or Crystal Arena Matches</td>
                    <Reward
                      id="QUESTITEM_TOKEN_ARENA_CRYSTAL"
                      title="Arena Sigil (x40)"
                    />
                  </tr>
                  <tr>
                    <td>
                      Get 10 kills in a single Arena or Crystal Arena match
                    </td>
                    <Reward
                      id="T6_SKILLBOOK_NONTRADABLE"
                      title="Master's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Win 200 Arena or Crystal Arena Matches</td>
                    <Reward
                      id="T6_SILVERBAG_NONTRADABLE"
                      title="Master's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>
                      Deal 30,000 damage in a single Arena or Crystal Arena
                      match
                    </td>
                    <Reward
                      id="T1_KILL_EMOTE_HAMMER_CHARGES_NONTRADABLE"
                      title="Hammer Victory Emote Charge (x20)"
                    />
                  </tr>
                  <tr>
                    <td>Win 250 Arena or Crystal Arena Matches</td>
                    <Reward
                      id="T7_SILVERBAG_NONTRADABLE"
                      title="Grandmaster's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>
                      Capture 8 Runestones in a single Arena or Crystal Arena
                      match
                    </td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Win 300 Arena or Crystal Arena Matches</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>
                      Deal 40,000 damage in a single Arena or Crystal Arena
                      match
                    </td>
                    <Reward
                      id="T6_SKILLBOOK_NONTRADABLE"
                      title="Master's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>
                      Deal 50,000 damage in a single Arena or Crystal Arena
                      match
                    </td>
                    <Reward
                      id="T7_SKILLBOOK_NONTRADABLE"
                      title="Grandmaster's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>
                      Take 50,000 damage without dying in a single Arena or
                      Crystal Arena match
                    </td>
                    <Reward
                      id="UNIQUE_UNLOCK_ARMOR_VANITY_GLADIATOR_ARENA"
                      title="Wardrobe Skin: Arena Gladiator Armor"
                    />
                  </tr>
                  <tr>
                    <td>
                      Heal 30,000 health in a single Arena or Crystal Arena
                      match
                    </td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>
                      Heal 50,000 health in a single Arena or Crystal Arena
                      match
                    </td>
                    <Reward
                      id="T6_SKILLBOOK_NONTRADABLE"
                      title="Master's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>
                      Heal 75,000 health in a single Arena or Crystal Arena
                      match
                    </td>
                    <Reward
                      id="UNIQUE_FURNITUREITEM_ADC_STATUE_MAGE_A"
                      title="Mage Statue"
                    />
                  </tr>
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
                  <tr>
                    <td>Increase your rank in the Crystal Arena</td>
                    <Reward
                      id="T4_SKILLBOOK_NONTRADABLE"
                      title="Adept's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Reach Iron III Rank in Crystal Arena</td>
                    <Reward
                      id="T4_SILVERBAG_NONTRADABLE"
                      title="Adept's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Reach Iron IV Rank in Crystal Arena</td>
                    <Reward
                      id="T4_SKILLBOOK_NONTRADABLE"
                      title="Adept's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Reach Bronze Rank in Crystal Arena</td>
                    <Reward
                      id="T1_KILL_EMOTE_GHOST_CHARGES_NONTRADABLE"
                      title="Ghost Victory Emote Charge (x10)"
                    />
                  </tr>
                  <tr>
                    <td>Reach Bronze II Rank in Crystal Arena</td>
                    <Reward
                      id="T5_SILVERBAG_NONTRADABLE"
                      title="Expert's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Reach Bronze III Rank in Crystal Arena</td>
                    <Reward
                      id="QUESTITEM_TOKEN_ARENA_CRYSTAL"
                      title="Arena Sigil (x20)"
                    />
                  </tr>
                  <tr>
                    <td>Reach Bronze IV Rank in Crystal Arena</td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Reach Silver Rank in the Crystal Arena</td>
                    <Reward
                      id="UNIQUE_UNLOCK_HEAD_VANITY_PRIEST_NON_TRADABLE"
                      title="Wardrobe Skin: Monk's Hood"
                    />
                  </tr>
                  <tr>
                    <td>Reach Silver II Rank in the Crystal Arena</td>
                    <Reward
                      id="T3_LEARNINGPOINTS_NONTRADABLE"
                      title="Journeyman's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Reach Silver III Rank in Crystal Arena</td>
                    <Reward
                      id="T1_KILL_EMOTE_TOMBSTONE_CHARGES_NONTRADABLE"
                      title="Tombstone Victory Emote Charge (x20)"
                    />
                  </tr>
                  <tr>
                    <td>Reach Silver IV Rank in Crystal Arena</td>
                    <Reward
                      id="T7_SILVERBAG_NONTRADABLE"
                      title="Grandmaster's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Reach Gold Rank in Crystal Arena</td>
                    <Reward
                      id="T4_TOKEN_CRYSTALLEAGUE_NONLETHAL_LVL_01"
                      title="Crystal Token (5v5 Nonlethal - Lvl. 1)"
                    />
                  </tr>
                  <tr>
                    <td>Reach Gold II Rank in Crystal Arena</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Reach Gold III Rank in Crystal Arena</td>
                    <Reward
                      id="UNIQUE_UNLOCK_HEAD_VANITY_GLADIATOR_ARENA"
                      title="Wardrobe Skin: Arena Gladiator Helm"
                    />
                  </tr>
                  <tr>
                    <td>Reach Gold IV Rank in Crystal Arena</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x5)"
                    />
                  </tr>
                  <tr>
                    <td>Reach Crytal Rank in Crystal Arena</td>
                    <Reward
                      id="T4_TOKEN_CRYSTALLEAGUE_CITY_LVL_01"
                      title="Crystal Token (20v20 -  Lvl. 1)"
                    />
                  </tr>
                  <tr>
                    <td>Win a match by a 50 point margin</td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Win a match by a 75 point margin</td>
                    <Reward
                      id="T6_SKILLBOOK_NONTRADABLE"
                      title="Master's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Win a match by a 100 point margin</td>
                    <Reward
                      id="UNIQUE_UNLOCK_CAPE_VANITY_GLADIATOR_ARENA"
                      title="Wardrobe Skin: Arena Gladiator Cape"
                    />
                  </tr>
                  <tr>
                    <td>Win a match by a 125 point margin</td>
                    <Reward
                      id="T7_SKILLBOOK_NONTRADABLE"
                      title="Grandmaster's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Win a match by a 150 point margin</td>
                    <Reward
                      id="T1_KILL_EMOTE_HAMMER_CHARGES_NONTRADABLE"
                      title="Hammer Victory Emote Charge (x50)"
                    />
                  </tr>
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
                  <tr>
                    <td>Defeat the final boss in a Hunter Corrupted Dungeon</td>
                    <Reward
                      id="T4_SKILLBOOK_NONTRADABLE"
                      title="Adept's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Get 666 Infamy in Corrupted Dungeons</td>
                    <Reward
                      id="T4_SILVERBAG_NONTRADABLE"
                      title="Adept's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>
                      Defeat another player after invading their Corrupted
                      Dungeon
                    </td>
                    <Reward
                      id="T5_CORRUPTED_NONLETHAL_MAP"
                      title="Corrupted Dungeon Map (Hunter)"
                    />
                  </tr>
                  <tr>
                    <td>Defeat an invading player in a Corrupted Dungeon</td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Get 2,500 Infamy in Corrupted Dungeons</td>
                    <Reward
                      id="T5_SILVERBAG_NONTRADABLE"
                      title="Expert's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 5 players in a Hunter Corrupted Dungeon</td>
                    <Reward
                      id="T1_KILL_EMOTE_SWORD_CHARGES_NONTRADABLE"
                      title="Sword Victory Emote Charge (x10)"
                    />
                  </tr>
                  <tr>
                    <td>
                      Defeat the final boss in a Stalker Corrupted Dungeon
                    </td>
                    <Reward
                      id="T3_LEARNINGPOINTS_NONTRADABLE"
                      title="Journeyman's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Get 10,000 Infamy in Corrupted Dungeons</td>
                    <Reward
                      id="T6_CORRUPTED_LETHAL_MAP"
                      title="Corrupted Dungeon Map (Stalker/Slayer)"
                    />
                  </tr>
                  <tr>
                    <td>Defeat a player in a Stalker Corrupted Dungeon</td>
                    <Reward
                      id="T1_KILL_EMOTE_HELLGATE_CHARGES_NONTRADABLE"
                      title="Hellgate Victory Emote Charge (x20)"
                    />
                  </tr>
                  <tr>
                    <td>Get 50,000 Infamy in Corrupted Dungeons</td>
                    <Reward
                      id="T6_SILVERBAG_NONTRADABLE"
                      title="Master's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 5 players in a Stalker Corrupted Dungeon</td>
                    <Reward
                      id="UNIQUE_FURNITUREITEM_ADC_HALLOWEEN_SCARECROW_A"
                      title="Halloween Scarecrow"
                    />
                  </tr>
                  <tr>
                    <td>Unlock the Slayer difficulty in Corrupted Dungeons</td>
                    <Reward
                      id="T7_SILVERBAG_NONTRADABLE"
                      title="Grandmaster's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Defeat a player in a Slayer Corrupted Dungeon</td>
                    <Reward
                      id="UNIQUE_UNLOCK_HEAD_VANITY_ENTERTAINER_NON_TRADABLE"
                      title="Wardrobe Skin: Entertainer's Mask"
                    />
                  </tr>
                  <tr>
                    <td>Get 150,000 Infamy in Corrupted Dungeons</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 5 players in a Slayer Corrupted Dungeon</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 100 players in full-loot Corrupted Dungeons</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x2)"
                    />
                  </tr>
                  <tr>
                    <td>Get 300,000 Infamy in Corrupted Dungeons</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x5)"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 300 players in full-loot Corrupted Dungeons</td>
                    <Reward
                      id="T1_KILL_EMOTE_TOMBSTONE_CHARGES_NONTRADABLE"
                      title="Tombstone Victory Emote Charge (x50)"
                    />
                  </tr>
                  <tr>
                    <td>Get 600,000 Infamy in Corrupted Dungeons</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x10)"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 666 players in full-loot Corrupted Dungeons</td>
                    <Reward
                      id="T1_KILL_EMOTE_HAMMER_CHARGES_NONTRADABLE"
                      title="Hammer Victory Emote Charge (x500)"
                    />
                  </tr>
                  <tr>
                    <td>Get 1,000,000 Infamy in Corrupted Dungeons</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x20)"
                    />
                  </tr>
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
                  <tr>
                    <td>Enlist in any of the six City Factions</td>
                    <Reward
                      id="T3_SKILLBOOK_NONTRADABLE"
                      title="Journeyman's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Capture an Outpost</td>
                    <Reward
                      id="T4_SKILLBOOK_NONTRADABLE"
                      title="Adept's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>
                      Assist in completely capturing another city&apos;s zone in
                      Faction Warfare
                    </td>
                    <Reward
                      id="T4_SILVERBAG_NONTRADABLE"
                      title="Adept's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Earn a Faction Warfare Daily Reward</td>
                    <Reward
                      id="T4_SILVERBAG_NONTRADABLE"
                      title="Adept's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>
                      Knock down or assist a knockdown of an enemy faction
                      player
                    </td>
                    <Reward
                      id="T4_SKILLBOOK_NONTRADABLE"
                      title="Adept's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Capture 10 Outposts</td>
                    <Reward
                      id="T5_SILVERBAG_NONTRADABLE"
                      title="Expert's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Reach 15,000 standing with any Faction</td>
                    <Reward
                      id="T5_SILVERBAG_NONTRADABLE"
                      title="Expert's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 2 different Faction Champions</td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Reach 30,000 standing with any Faction</td>
                    <Reward
                      id="T6_SILVERBAG_NONTRADABLE"
                      title="Master's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Capture 30 Faction Outposts</td>
                    <Reward
                      id="T1_KILL_EMOTE_FLAG_CHARGES_NONTRADABLE"
                      title="Guild Banner Victory Emote Charge (x10)"
                    />
                  </tr>
                  <tr>
                    <td>Finish a Trade Mission for any city</td>
                    <Reward
                      id="T2_LEARNINGPOINTS_NONTRADABLE"
                      title="Novice's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Reach 60,000 standing with any Faction</td>
                    <Reward
                      id="T6_SILVERBAG_NONTRADABLE"
                      title="Master's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Capture 5 Outposts in Red Zones</td>
                    <Reward
                      id="T3_LEARNINGPOINTS_NONTRADABLE"
                      title="Journeyman's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 3 different Faction Champions</td>
                    <Reward
                      id="T1_KILL_EMOTE_OVERGROWN_CHARGES_NONTRADABLE"
                      title="Overgrown Victory Emote Charge (x20)"
                    />
                  </tr>
                  <tr>
                    <td>
                      Kill or assist a kill of an enemy faction player in a Red
                      Zone
                    </td>
                    <Reward
                      id="T6_SKILLBOOK_NONTRADABLE"
                      title="Master's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Help repel a Bandit Assault</td>
                    <Reward
                      id="T6_SKILLBOOK_NONTRADABLE"
                      title="Master's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Reach 240,000 standing with any Faction</td>
                    <Reward
                      id="T7_SILVERBAG_NONTRADABLE"
                      title="Grandmaster's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Capture 100 Outposts</td>
                    <Reward
                      id="UNIQUE_REPAIRPOWDER_ADC_GENERAL_01_NONTRADEABLE"
                      title="Scroll of Repair"
                    />
                  </tr>
                  <tr>
                    <td>Achieve a standing of 330,000 with any faction</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>
                      Defeat all opposing City Faction Warmasters at least once
                    </td>
                    <Reward
                      id="T7_SKILLBOOK_NONTRADABLE"
                      title="Grandmaster's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Capture 300 Faction Outposts</td>
                    <Reward
                      id="T1_KILL_EMOTE_OVERGROWN_CHARGES_NONTRADABLE"
                      title="Overgrown Victory Emote Charge (x50)"
                    />
                  </tr>
                  <tr>
                    <td>
                      Knock down or assist knockdowns of 30 enemy faction
                      players
                    </td>
                    <Reward
                      id="T5_SILVERBAG_NONTRADABLE"
                      title="Expert's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>
                      Knock down or assist knockdowns of 100 enemy faction
                      players
                    </td>
                    <Reward
                      id="T1_KILL_EMOTE_HAMMER_CHARGES_NONTRADABLE"
                      title="Hammer Victory Emote Charge (x10)"
                    />
                  </tr>
                  <tr>
                    <td>
                      Knock down or assist knockdowns of 300 enemy faction
                      players
                    </td>
                    <Reward
                      id="T6_SILVERBAG_NONTRADABLE"
                      title="Master's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>
                      Knock down or assist knockdowns of 1000 enemy faction
                      players
                    </td>
                    <Reward
                      id="T7_SILVERBAG_NONTRADABLE"
                      title="Grandmaster's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>
                      Kill or assist 10 enemy faction player kills in Red Zones
                    </td>
                    <Reward
                      id="UNIQUE_FURNITUREITEM_ADC_GRAVE_A"
                      title="Tomb of the Unknown"
                    />
                  </tr>
                  <tr>
                    <td>
                      Kill or assist 30 enemy faction player kills in Red Zones
                    </td>
                    <Reward
                      id="T7_SILVERBAG_NONTRADABLE"
                      title="Grandmaster's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>
                      Kill or assist 100 enemy faction player kills in Red Zones
                    </td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>
                      Kill or assist 300 enemy faction player kills in Red Zones
                    </td>
                    <Reward
                      id="T1_KILL_EMOTE_SWORD_CHARGES_NONTRADABLE"
                      title="Sword Victory Emote Charge (x50)"
                    />
                  </tr>
                  <tr>
                    <td>
                      Kill or assist 1,000 enemy faction player kills in Red
                      Zones
                    </td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x5)"
                    />
                  </tr>
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
                  <tr>
                    <td>Open an open-world Treasure Chest</td>
                    <Reward
                      id="T3_LEARNINGPOINTS_NONTRADABLE"
                      title="Journeyman's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Knock down another player in a Yellow Zone</td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Open 10 open-world Treasure Chests</td>
                    <Reward
                      id="T1_KILL_EMOTE_OVERGROWN_CHARGES_NONTRADABLE"
                      title="Overgrown Victory Emote Charge (x10)"
                    />
                  </tr>
                  <tr>
                    <td>Kill or assist a kill in PvP</td>
                    <Reward
                      id="UNIQUE_FURNITUREITEM_ADC_GRAVE_B"
                      title="Memorial of the Fallen"
                    />
                  </tr>
                  <tr>
                    <td>
                      Loot any armor, foot gear and a mount from a killed player
                      at the same time
                    </td>
                    <Reward
                      id="T4_SKILLBOOK_NONTRADABLE"
                      title="Adept's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Get 200,000 Kill Fame</td>
                    <Reward
                      id="T5_SILVERBAG_NONTRADABLE"
                      title="Expert's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Kill 10 players in full-loot regions</td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Kill 3 players in the Roads of Avalon</td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Kill 25 players in full-loot regions</td>
                    <Reward
                      id="T1_KILL_EMOTE_FLAG_CHARGES_NONTRADABLE"
                      title="Guild Banner Victory Emote Charge (x20)"
                    />
                  </tr>
                  <tr>
                    <td>Kill 10 players in Static Dungeons</td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Get 2 million Kill Fame in the Open World</td>
                    <Reward
                      id="T6_SILVERBAG_NONTRADABLE"
                      title="Master's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Kill 6 players within one minute</td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Kill 100 players in full-loot regions</td>
                    <Reward
                      id="T6_SKILLBOOK_NONTRADABLE"
                      title="Master's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Get 2 million Kill Fame in the Roads of Avalon</td>
                    <Reward
                      id="T6_SILVERBAG_NONTRADABLE"
                      title="Master's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Get 5 million Kill Fame in Static Dungeons</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>
                      Kill 6 players within one minute (not including assists)
                    </td>
                    <Reward
                      id="T6_SKILLBOOK_NONTRADABLE"
                      title="Master's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Kill 300 players in the open world</td>
                    <Reward
                      id="T7_SKILLBOOK_NONTRADABLE"
                      title="Grandmaster's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Get 10 million Kill Fame in Black Zones</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x5)"
                    />
                  </tr>
                  <tr>
                    <td>Get 10 million Kill Fame in Static Dungeons</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x5)"
                    />
                  </tr>
                  <tr>
                    <td>Get 10 million Kill Fame in the Roads of Avalon</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x5)"
                    />
                  </tr>
                  <tr>
                    <td>Get 50 million Kill Fame in Black Zones</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x15)"
                    />
                  </tr>
                  <tr>
                    <td>Get 100 million Kill Fame in Black Zones</td>
                    <Reward
                      id="T1_KILL_EMOTE_GHOST_CHARGES_NONTRADABLE"
                      title="Ghost Victory Emote Charge (x50)"
                    />
                  </tr>
                  <tr>
                    <td>Get 500 million Kill Fame in Black Zones</td>
                    <Reward
                      id="T1_KILL_EMOTE_TOMBSTONE_CHARGES_NONTRADABLE"
                      title="Tombstone Victory Emote Charge (x500)"
                    />
                  </tr>
                  <tr>
                    <td>
                      Open 30 open-world Treasure Chests in full-loot regions
                    </td>
                    <Reward
                      id="T7_SILVERBAG_NONTRADABLE"
                      title="Grandmaster's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Open 100 open-world Treasure Chests</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Open 30 Medium Treasure Chests</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Open 10 Large Treasure Chests</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Open 500 open-world Treasure Chests</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x5)"
                    />
                  </tr>
                  <tr>
                    <td>Open 300 Medium Treasure Chests</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x5)"
                    />
                  </tr>
                  <tr>
                    <td>Open 100 Large Treasure Chests</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x5)"
                    />
                  </tr>
                  <tr>
                    <td>Open a Legendary Large Treasure Chest</td>
                    <Reward
                      id="T7_SKILLBOOK_NONTRADABLE"
                      title="Grandmaster's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Get killed by another player</td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
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
                  <tr>
                    <td>Enter a Hellgate</td>
                    <Reward
                      id="T4_SKILLBOOK_NONTRADABLE"
                      title="Adept's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Defeat a Mini Boss in a Hellgate</td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>
                      Defeat a team of enemy players in any type of Hellgate
                    </td>
                    <Reward
                      id="T5_HELLGATE_2V2_NON_LETHAL_1_MAP"
                      title="Expert's Hellgate Ritual (2v2 - Nonlethal)"
                    />
                  </tr>
                  <tr>
                    <td>Chain 2 Hellgates without returning to the surface</td>
                    <Reward
                      id="T5_SKILLBOOK_NONTRADABLE"
                      title="Expert's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Gain 10,000 Infamy in 2v2 Hellgates</td>
                    <Reward
                      id="T1_KILL_EMOTE_HELLGATE_CHARGES_NONTRADABLE"
                      title="Hellgate Victory Emote Charge (x10)"
                    />
                  </tr>
                  <tr>
                    <td>Knock down 10 players in Hellgates</td>
                    <Reward
                      id="T5_SILVERBAG_NONTRADABLE"
                      title="Expert's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Defeat 5 Mini Bosses in Hellgates</td>
                    <Reward
                      id="UNIQUE_FURNITUREITEM_ADC_HALLOWEEN_PUMPKIN_LANTERN_B"
                      title="Friendly Pumpkin Lantern"
                    />
                  </tr>
                  <tr>
                    <td>Defeat a Boss in a Hellgate</td>
                    <Reward
                      id="T6_SILVERBAG_NONTRADABLE"
                      title="Master's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Gain 20,000 Infamy in 2v2 Hellgates</td>
                    <Reward
                      id="T1_KILL_EMOTE_GHOST_CHARGES_NONTRADABLE"
                      title="Ghost Victory Emote Charge (x20)"
                    />
                  </tr>
                  <tr>
                    <td>Chain 5 Hellgates without returning to the surface</td>
                    <Reward
                      id="T7_SKILLBOOK_NONTRADABLE"
                      title="Grandmaster's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Knock down 50 players in Hellgates</td>
                    <Reward
                      id="T6_HELLGATE_2V2_LETHAL_1_MAP"
                      title="Master's Hellgate Ritual (2v2 - Lethal)"
                    />
                  </tr>
                  <tr>
                    <td>Kill a player in a full-loot Hellgate</td>
                    <Reward
                      id="T6_SKILLBOOK_NONTRADABLE"
                      title="Master's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Gain 50,000 Infamy in 2v2 Hellgates</td>
                    <Reward
                      id="T7_HELLGATE_5V5_LETHAL_1_MAP"
                      title="Grandmaster's Hellgate Ritual (5v5 - Lethal)"
                    />
                  </tr>
                  <tr>
                    <td>Defeat a Mini Boss in a 5v5 Hellgate</td>
                    <Reward
                      id="T6_SKILLBOOK_NONTRADABLE"
                      title="Master's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Defeat an enemy team in a 5v5 Hellgate</td>
                    <Reward
                      id="T4_LEARNINGPOINTS_NONTRADABLE"
                      title="Adept's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Gain 20,000 Infamy in 5v5 Hellgates</td>
                    <Reward
                      id="T7_SILVERBAG_NONTRADABLE"
                      title="Grandmaster's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Knock down 200 players in Hellgates</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Gain 50,000 Infamy in 5v5 Hellgates</td>
                    <Reward
                      id="T8_HELLGATE_10V10_LETHAL_1_MAP"
                      title="Elder's Hellgate Ritual (10v10 - Lethal)"
                    />
                  </tr>
                  <tr>
                    <td>Kill 20 players in full-loot Hellgates</td>
                    <Reward
                      id="T7_SILVERBAG_NONTRADABLE"
                      title="Grandmaster's Bag of Silver (x5)"
                    />
                  </tr>
                  <tr>
                    <td>Chain 10 Hellgates without returning to the surface</td>
                    <Reward
                      id="T5_LEARNINGPOINTS_NONTRADABLE"
                      title="Expert's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Kill 50 players in full-loot Hellgates</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x5)"
                    />
                  </tr>
                  <tr>
                    <td>Defeat a Mini Boss in a 10v10 Hellgate</td>
                    <Reward
                      id="T7_SKILLBOOK_NONTRADABLE"
                      title="Grandmaster's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Defeat an enemy team in a 10v10 Hellgate</td>
                    <Reward
                      id="T4_LEARNINGPOINTS_NONTRADABLE"
                      title="Adept's Tome of Learning"
                    />
                  </tr>
                  <tr>
                    <td>Kill 200 players in full-loot Hellgates</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x10)"
                    />
                  </tr>
                  <tr>
                    <td>Kill 500 players in full-loot Hellgates</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x20)"
                    />
                  </tr>
                  <tr>
                    <td>Kill 1,000 players in full-loot Helgates</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x40)"
                    />
                  </tr>
                  <tr>
                    <td>Gain 100,000 Infamy in 2v2 Hellgates</td>
                    <Reward
                      id="T1_KILL_EMOTE_GHOST_CHARGES_NONTRADABLE"
                      title="Ghost Victory Emote Charge (x500)"
                    />
                  </tr>
                  <tr>
                    <td>Gain 250,000 Infamy in 2v2 Hellgates</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x20)"
                    />
                  </tr>
                  <tr>
                    <td>Gain 100,000 Infamy in 5v5 Hellgates</td>
                    <Reward
                      id="T1_KILL_EMOTE_SWORD_CHARGES_NONTRADABLE"
                      title="Sword Victory Emote Charge (x500)"
                    />
                  </tr>
                  <tr>
                    <td>Gain 250,000 Infamy in 5v5 Hellgates</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x25)"
                    />
                  </tr>
                  <tr>
                    <td>Gain 50,000 Infamy in 10v10 Hellgates</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x8)"
                    />
                  </tr>
                  <tr>
                    <td>Gain 100,000 Infamy in 10v10 Hellgates</td>
                    <Reward
                      id="T1_KILL_EMOTE_HELLGATE_CHARGES_NONTRADABLE"
                      title="Hellgate Victory Emote Charge (x500)"
                    />
                  </tr>
                  <tr>
                    <td>Gain 250,000 Infamy in 10v10 Hellgates</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x30)"
                    />
                  </tr>
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
                  <tr>
                    <td>Participate in a Crystal League Battle</td>
                    <Reward
                      id="T6_SKILLBOOK_NONTRADABLE"
                      title="Master's Tome of Insight"
                    />
                  </tr>
                  <tr>
                    <td>Win a 5v5 Crystal League Match</td>
                    <Reward
                      id="T7_SILVERBAG_NONTRADABLE"
                      title="Grandmaster's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Win a Rank 2 5v5 Crystal League Match</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Win a Rank 3 5v5 Crystal League Match</td>
                    <Reward
                      id="UNIQUE_TOKEN_COMMUNITY"
                      title="Community Token (x50)"
                    />
                  </tr>
                  <tr>
                    <td>Win a 20v20 Crystal League Match</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver"
                    />
                  </tr>
                  <tr>
                    <td>Win a Rank 4 5v5 Crystal League Match</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x5)"
                    />
                  </tr>
                  <tr>
                    <td>Win a Rank 5 5v5 Crystal League Match</td>
                    <Reward
                      id="T1_KILL_EMOTE_FLAG_CHARGES_NONTRADABLE"
                      title="Guild Banner Victory Emote Charge (x50)"
                    />
                  </tr>
                  <tr>
                    <td>Win a Rank 6 5v5 Crystal League Match</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x15)"
                    />
                  </tr>
                  <tr>
                    <td>Win a Rank 7 5v5 Crystal League Match</td>
                    <Reward
                      id="UNIQUE_UNLOCK_CAPE_VANITY_GLADIATOR_CRYSTAL"
                      title="Wardrobe Skin: Crystal Gladiator Cape"
                    />
                  </tr>
                  <tr>
                    <td>Win a Rank 8 5v5 Crystal League Match</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x40)"
                    />
                  </tr>
                  <tr>
                    <td>Win a Rank 9 5v5 Crystal League Match</td>
                    <Reward
                      id="UNIQUE_UNLOCK_HEAD_VANITY_GLADIATOR_CRYSTAL"
                      title="Wardrobe Skin: Crystal Gladiator Helm"
                    />
                  </tr>
                  <tr>
                    <td>Win a Rank 2 20v20 Crystal League Match</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x5)"
                    />
                  </tr>
                  <tr>
                    <td>Win a Rank 3 20v20 Crystal League Match</td>
                    <Reward
                      id="UNIQUE_UNLOCK_SHOES_VANITY_GLADIATOR_CRYSTAL"
                      title="Wardrobe Skin: Crystal Gladiator Boots"
                    />
                  </tr>
                  <tr>
                    <td>Win a Rank 4 20v20 Crystal League Match</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x10)"
                    />
                  </tr>
                  <tr>
                    <td>Win a Rank 5 20v20 Crystal League Match</td>
                    <Reward
                      id="T1_KILL_EMOTE_FLAG_CHARGES_NONTRADABLE"
                      title="Guild Banner Victory Emote Charge (x500)"
                    />
                  </tr>
                  <tr>
                    <td>Win a Rank 6 20v20 Crystal League Match</td>
                    <Reward
                      id="T8_SILVERBAG_NONTRADABLE"
                      title="Elder's Bag of Silver (x40)"
                    />
                  </tr>
                  <tr>
                    <td>Win a Rank 7 20v20 Crystal League Match</td>
                    <Reward
                      id="UNIQUE_UNLOCK_ARMOR_VANITY_GLADIATOR_CRYSTAL"
                      title="Wardrobe Skin: Crystal Gladiator Armor"
                    />
                  </tr>
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
