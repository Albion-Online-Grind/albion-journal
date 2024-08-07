```tsx
const AlbionJournal = () => {
  return (
    <div>
      {/* PVE Activities */}
      <div>
        <UncontrolledAccordion id="pve-activities">
          <AccordionItem>
            <AccordionHeader targetId="pve-activities">
              PvE Activities (190)
            </AccordionHeader>
            <AccordionBody accordionId="pve-activities">
              <h4>Expeditions (18)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 300 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Finish a Tier 3 Solo Expedition</td>
                    <Reward id="T3_SILVERBAG_NONTRADABLE" title="Journeyman's Bag of Silver" />
                  </tr>
                  <tr>
                    <td>Finish a Tier 4 Solo Expedition</td>
                    <Reward id="T4_SILVERBAG_NONTRADABLE" title="Adept's Bag of Silver" />
                  </tr>
                  <tr>
                    <td>Finish a Tier 4 Group Expedition</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish a Tier 5 Solo Expedition</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish a Tier 5 Group Expedition</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish a Tier 6 Group Expedition</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish every non-hardcore Expedition</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish a Tier 5 Solo Expedition within 7 minutes</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish a Tier 6 Group Expedition within 10 minutes</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish a Tier 5 Solo Expedition within 5 minutes</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish any Hardcore Expedition</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish a Level 4 Hardcore Expedition</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish a Level 8 Hardcore Expedition</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish a Level 12 Hardcore Expedition</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Finish a Level 18 Hardcore Expedition within 10 minutes
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish 5 different level 18 Hardcore Expeditions</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Finish every Hardcore Expedition on Level 18
                      <br />
                      <span className="text-muted">
                        Preaching to the Dead, Fishy Business, Stone Wars,
                        Lumber Lunacy, Lurking Underneath, Fungicide, Three
                        Sisters, Eternal Battle, Fistful of Silver, In the
                        Raven&apos;s Claws
                      </span>
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                </tbody>
              </Table>

              <h4>Solo Random Dungeons (26)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 300 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Finish a Tier 3 Solo Dungeon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish a Tier 4 Solo Dungeon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish a Solo Dungeon of every Faction</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Unlock 10 chests in Solo Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish a Tier 5 Solo Dungeon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish 3 Solo Dungeons with a Map</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Find an enchanted Solo Dungeon without using a map</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Unlock 30 chests in Solo Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish an Enchantment Level 3 Solo Dungeon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish a Tier 6 Solo Dungeon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat a T5 boss with T3 equipment on your own</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish an Enchantment Level 4 Solo Dungeon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Use 30 combat buff shrines in Solo Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish a Tier 7 Solo Dungeon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish a Tier 8 Solo Dungeon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish a Tier 8.4 Solo Dungeon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Unlock 100 chests in Solo Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat a T6 boss with T3 equipment on your own</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat a T7 boss with T3 equipment on your own</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat a T8 boss with T3 equipment on your own</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish 30 Solo Dungeon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish 100 Solo Dungeon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish 300 Solo Dungeon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish 600 Solo Dungeon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish 1,000 Solo Dungeon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                </tbody>
              </Table>

              <h4>Roaming Mobs (34)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 300 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Defeat 25 T3 Roaming Mobs</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat 50 T4 Roaming Mobs</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat 3 mobs with your mount standing next to you</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat 4 Roaming Mobs within 10 seconds</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat a Roaming Mob with any armor slot ability</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat 80 T5 Roaming Mobs</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat 10 Roaming Mobs within 30 seconds</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Defeat 50 Roaming Mobs while flagged for Faction Warfare
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat 8 Roaming Mobs within 10 seconds</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat 5 Roaming Mobs in a Red Zone</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat 120 T6 Roaming Mobs</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat 200 T7 Roaming Mobs</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat 1,000 Roaming Mobs in a Black Zone</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat 300 T8 Roaming Mobs</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat 30 Roaming Mobs Champions</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat 100 Roaming Mobs Champions</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat 300 Roaming Mobs Champions</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat 1,000 Roaming Mobs Champions</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat 3,000 Roaming Mobs Champions</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat 10 Roaming Mob Mini Bosses</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat 30 Roaming Mob Mini Bosses</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat 100 Roaming Mob Mini Bosses</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat 300 Roaming Mob Mini Bosses</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat 3 Roaming Mob Bosses</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat 10 Roaming Mob Bosses</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat 30 Roaming Mob Bosses</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat 100 Roaming Mob Bosses</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gain 100,000 Fame from Roaming Mobs</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gain 300,000 Fame from Roaming Mobs</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gain a million Fame from Roaming Mobs</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gain 3 million Fame from Roaming Mobs</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gain 10 million Fame from Roaming Mobs</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gain 30 million Fame from Roaming Mobs</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gain 100 million Fame from Roaming Mobs</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                </tbody>
              </Table>

              <h4>Static Dungeons (23)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 300 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Defeat 12 mobs in a T3 Static Dungeon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat 50 mobs in a T4 Static Dungeon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat 100 mobs in a T5 Static Dungeon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat 150 mobs in a T6 Static Dungeon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat 200 mobs in a T7 Static Dungeon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat 300 mobs in a T8 Static Dungeon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Participate in a Static Dungeon Event</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gain 100,000 Fame during a Static Dungeon rally</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gain 10,000 Fame in Static Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gain 100,000 Fame in Static Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gain a million Fame in Static Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gain 10 million Fame in Static Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gain 30 million Fame in Static Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gain 100 million Fame in Static Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Kill 100 Champions in Static Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Kill 300 Champions in Static Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Kill 1,000 Champions in Static Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Kill 30 Mini Bosses in Static Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Kill 100 Mini Bosses in Static Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Kill 300 Mini Bosses in Static Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Kill 10 Bosses in Static Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Kill 30 Bosses in Static Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Kill 100 Bosses in Static Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                </tbody>
              </Table>

              <h4>Group Random Dungeons (19)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 300 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Finish a Tier 4 Group Dungeon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish a Tier 5 Group Dungeon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish 2 Enchantment Level 1 Group Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish 3 Enchantment Level 2 Group Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish 5 Enchantment Level 3 Group Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish a Tier 6 Group Dungeon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish a Tier 7 Group Dungeon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish a Tier 8 Group Dungeon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish a Tier 8.4 Group Dungeon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Unlock 10 chests in Group Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Unlock 30 chests in Group Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Unlock 100 chests in Group Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Unlock 500 chests in Group Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish 10 Group Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish 30 Group Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish 80 Group Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish 150 Group Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish 300 Group Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish 500 Group Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                </tbody>
              </Table>

              <h4>Tracking (27)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 300 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Track down a solo Rare Creature</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Track down a T4 solo Rare Quarry</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Track down 3 types of solo Rare Creature</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Track down a T5 solo Rare Quarry</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Track down 4 types of solo Rare Creature</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Track down a T6 solo Rare Quarry</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Track down 5 types of solo Rare Creature</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish a hunt at the first encounter</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Track down 6 types of solo Rare Creature</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Track down a T7 solo Rare Quarry</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Track down 7 different solo Rare Creature <br />
                      <span className="text-muted">
                        Shadow Panter, Spirit Bear, Hellfire Imp, Downbird,
                        Sylvian, Werewolf, Runestone Golem
                      </span>
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Track down a T8 solo Rare Quarry</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Track down a group Rare Creature</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Track down 3 types of group Rare Creature</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Track down 5 types of group Rare Creature</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Track down 7 types of group Rare Creature
                      <br />
                      <span className="text-muted">
                        Shadow Panter, Spirit Bear, Hellfire Imp, Downbird,
                        Sylvian, Werewolf, Runestone Golem
                      </span>
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Track down a T8 group Rare Quarry</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish a solo Rare Creature hunt in 4 minutes</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish a solo Dawnbird hunt in 10 minutes</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish a group Rare Creature hunt in 4 minutes</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish a group Dawnbird hunt in 10 minutes</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish 10 hunts</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish 20 hunts</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish 40 hunts</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish 80 hunts</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish 200 hunts</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish 500 hunts</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                </tbody>
              </Table>

              <h4>World Bosses (20)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 300 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Defeat 10 Elite mobs in a World Boss Area</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat 50 Elite mobs in a World Boss Area</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat a Mini Boss in a World Boss Area</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat 5 Mini Bosses in a World Boss Area</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat a Boss in a World Boss Area</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat the Earth Mother</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat 20 Mini Bosses in a World Boss Area</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat 5 Bosses in a World Boss Area</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat the Harvester</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat 50 Mini Bosses in a World Boss Area</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat 20 Bosses in a World Boss Area</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat the Demon Prince</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat 1,000 Elite mobs in a World Boss Area</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat a T8 World Boss</td>
                    <td className="text-muted">TODO: Add reward</td>
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
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Defeat a World Boss in every possible area
                      <br />
                      <span className="text-muted">
                        Camlann, Ini Mon, Eye of the Forest, Unhallowed
                        Cloister, Black Monastery, Daemonium Keep, Astolat,
                        Citadel of Ash, Eldersleep, Deathreach Priory, Wailin
                        Bulwark
                      </span>
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat 200 Mini Bosses in a World Boss Area</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat 50 Bosses in a World Boss Area</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat 10 World Bosses</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat 30 World Bosses</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                </tbody>
              </Table>

              <h4>Avalonian Dungeons (23)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 300 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Finish a T6 Avalonian Dungeon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Receive the Ascension buff at the end of an Avalonian
                      Dungeon
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Defeat every Avalonian Dungeon boss type
                      <br />
                      <span className="text-muted">
                        Avalonian Knight Captain, Avalonian Constuct, Avalonian
                        Crystal Basilisk, Avalonian Hight Priestess, Avalonian
                        Archmage
                      </span>
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish a T7 Avalonian Dungeon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat Sir Bedivere with the Ascension buff active</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish a T8 Avalonian Dungeon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish a T8.1 Avalonian Dungeon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish a T8.2 Avalonian Dungeon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish a T8.3 Avalonian Dungeon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish a T8.4 Avalonian Dungeon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish 5 Avalonian Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish 20 Avalonian Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish 40 Avalonian Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish 60 Avalonian Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish 100 Avalonian Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Unlock 10 chests in Avalonian Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Unlock 20 chests in Avalonian Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Unlock 40 chests in Avalonian Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Unlock 100 chests in Avalonian Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Unlock a Legendary Chest in an Avalonian Dungeon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Unlock 160 chests in Avalonian Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Unlock 300 chests in Avalonian Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                </tbody>
              </Table>
            </AccordionBody>
          </AccordionItem>
        </UncontrolledAccordion>
      </div>

      {/* Economy */}
      <div>
        <UncontrolledAccordion id="economy">
          <AccordionItem>
            <AccordionHeader targetId="economy">Economy (137)</AccordionHeader>
            <AccordionBody accordionId="economy">
              <h4>Buying Items (21)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 300 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Buy a weapon at the Marketplace</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Buy 5 Equipment Items at the Marketplace</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Spend 10,000 Silver on items at the Marketplace</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Spend 100,000 Silver on items at the Marketplace</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Buy a mount from the Marketplace</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Spend a million Silver on items at the Marketplace</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Create a Buy Order</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Spend 10 million Silver on items at the Marketplace</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Spend 100 million Silver on items at the Marketplace
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Spend a billion Silver on items at the Marketplace</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Buy 30 Equipment Items at the Marketplace</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Buy 100 Equipment Items at the Marketplace</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Buy 1,000 Equipment Items at the Marketplace</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Buy 10,000 Equipment Items at the Marketplace</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Buy 100,000 Equipment Items at the Marketplace</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Buy 100 Items at the Marketplace</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Buy 1,000 Items at the Marketplace</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Buy 10,000 Items at the Marketplace</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Buy 100,000 Items at the Marketplace</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Buy a million Items at the Marketplace</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Buy 10 million Items at the Marketplace</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                </tbody>
              </Table>

              <h4>Selling Items (24)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 300 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Sell any items through the Marketplace</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Sell items for 10,000 Silver at the Marketplace</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Sell items for 100,000 Silver at the Marketplace</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Sell 10 Luxury Goods directly to their preferred city
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Create a Sell Order</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Sell 1000 Luxury Goods directly to their preferred city
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Create 20 Sell Orders</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Sell 9999 Luxury Goods directly to their preferred city
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Sell any item on the Black Market in Caerleon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Create a Sell Order on the Black Market</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Earn a total of 1,000,000 Silver through the Marketplace
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Earn a total of 10,000,000 Silver through the Marketplace
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Sell items for 100 million Silver at the Marketplace
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Sell items for a billion Silver at the Marketplace</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Earn a million Silver through the Black Market</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Earn 10 million Silver through the Black Market</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Earn 100 million Silver through the Black Market</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Earn a billion Silver through the Black Market</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Directly sell 9999 preferred luxury goods to Fort Sterling
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Directly sell 9999 preferred luxury goods to Lymhurst
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Directly sell 9999 preferred luxury goods to Bridgewatch
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Directly sell 9999 preferred luxury goods to Martlock
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Directly sell 9999 preferred luxury goods to Thetford
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Directly sell 9999 preferred luxury goods to Caerleon
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                </tbody>
              </Table>

              <h4>Refining (22)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 300 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Refine 30 T2 resources</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Refine 60 T3 resources</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Refine 100 T4 resources</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Transmute 10 resources to Uncommon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Refine 200 T5 resources</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Transmute 20 resources to a higher tier</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Refine 400 T6 resources</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Transmute 25 resources to Rare</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Refine 400 T7 resources</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Transmute a resource to Exceptional</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Refine 400 T8 resources</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Transmute a resource to Pristine</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Use the Fort Sterling refining bonus</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Use the Lymhurst refining bonus</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Use the Bridgewatch refining bonus</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Use the Martlock refining bonus</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Use the Thetford refining bonus</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Refine 1,000 Resources</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Refine 5,000 Resources</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Refine 10,000 Resources</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Refine 50,000 Resources</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Refine 100,000 Resources</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                </tbody>
              </Table>

              <h4>Crafting (25)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 300 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Craft 3 T2 Equipment Items</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Craft 10 T3 Equipment Items</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Craft an item in a Royal City</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Eat a salad that improves your crafting</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Craft 40 T4 Equipment Items</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Use city&apos;s crafting bonus</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Craft an Outstanding quality Equipment Item</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Craft 60 T5 Equipment Items</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Craft 20 Uncommon items</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Craft an Excellent quality Equipment Item</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Craft 80 T6 Equipment Items</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Craft 30 Rare items</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Craft an Masterpiece quality Equipment Item</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Craft 100 T7 Equipment Items</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Craft 50 Epic items</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Use a crafting bonus in a Hideout</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Craft 100 T8 Equipment Items</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Craft a Pristine T8 item</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Craft a Pristine T8 Masterpiece</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Craft items worth of 10,000 Fame</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Craft items worth of 100,000 Fame</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Craft items worth of a million Fame</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Craft items worth of 10 million Fame</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Craft items worth of 100 million Fame</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                </tbody>
              </Table>

              <h4>Item Conversions (22)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 300 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Study an item</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Salvage an item</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Reroll an item at a Repair Station</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Meld resources into an Artifact at the Artifact Foundry
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Meld 10 Soul Artifacts</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Meld 30 T5 Artifacts</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Meld 100 T6 Hunter Artifacts</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Meld 100 T8 Avalonian Artifacts</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Create 50 Souls with Transmutation</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Create a T8 Dungeon Map with Transmutation</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Create a Masterpiece item by rerolling it at a Repair
                      Station
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Reroll a full stack of 999 items at a Repair Station
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Salvage 100 items</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Salvage 1,000 items</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Salvage 10,000 items</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Study 100 items</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Study 1,000 items</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Study 10,000 items</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Reroll 100 items</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Reroll 1,000 items</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Reroll 10,000 items</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Reroll 100,000 items</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                </tbody>
              </Table>

              <h4>Accumulate Wealth (10)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 300 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Own 100,000 Silver</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Own 500,000 Silver</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Own 5 Gold</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Own 1 million Silver</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Own 5 million Silver</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Own 10 million Silver</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Own 50 million Silver</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Own 100 million Silver</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Own 500 million Silver</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Own 1 billion Silver</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                </tbody>
              </Table>

              <h4>City Plots (12)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 300 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Bid at least 1 million Silver on a city plot</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Own a city plot</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Collect 1 million Silver from city plots</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Keep a city plot you own in an auction cycle</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Collect 3 million Silver from city plots</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Own three city plots simultaneously</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Collect 10 million Silver from city plots</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Collect 30 million Silver from city plots</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Own 5 City Plots simultaneously</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Collect 100 million Silver from city plots</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Collect 300 million Silver from city plots</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Collect 1 billion silver from city plots</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                </tbody>
              </Table>
            </AccordionBody>
          </AccordionItem>
        </UncontrolledAccordion>
      </div>

      {/* Gathering */}
      <div>
        <UncontrolledAccordion id="gathering">
          <AccordionItem>
            <AccordionHeader targetId="gathering">
              Gathering (113)
            </AccordionHeader>
            <AccordionBody accordionId="gathering">
              <h4>Resources (33)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 300 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Gather 50 Tier 2 resources</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gather 75 Tier 3 resources</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gather resources worth 500 Fame</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gather 100 Tier 4 resources</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gather 10 resources with Enchantment Level 1</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gather 150 Tier 5 resources</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gather 10 resources with Enchantment Level 2</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gather a resource from a Plentiful Resource Node</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gather 10 resources with Enchantment Level 3</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gather 200 Tier 6 resources</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Gather 100 resources from a Plentiful Resource Nodes
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gather 300 enchanted resources</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Gather 500 resources from a Plentiful Resource Nodes
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gather any resource at an enemy Territory</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gather 750 enchanted resources</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gather 200 Tier 7 resources</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Gather 1,000 resources from a Plentiful Resource Nodes
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gather 50 resources at an enemy Territory</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gather 1,500 enchanted resources</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gather any Tier 8 resource</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gather a resource with maximum Gather Bonus</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gather 200 Tier 8 resources</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gather 30 resources with Enchantment Level 4</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gather resources worth 10,000 Fame</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gather resources worth 25,000 Fame</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gather resources worth 50,000 Fame</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gather resources worth 100,000 Fame</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gather resources worth 250,000 Fame</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gather resources worth 500,000 Fame</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gather resources worth a million Fame</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gather resources worth 3 million Fame</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gather resources worth 10 million Fame</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gather a T8 resource at an enemy territory</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                </tbody>
              </Table>

              <h4>Hide Animals (12)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 300 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Skin 3 types of Hide Animal</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Skin 6 types of Hide Animal</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Skin 10 types of Hide Animal</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Skin 15 types of Hide Animal</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Skin 22 types of Hide Animal</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Skin 30 types of Hide Animal</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Skin 40 types of Hide Animal</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Skin every type of Hide Animal
                      <br />
                      <span className="text-muted">
                        Bear, Boar, Direbear, Direboar, Direwolf, Fox, Rabbit,
                        Wolf, Hill Marmot, Snow Rabit, Marmot, Toad, Impala,
                        Snake, Cougar, Moabird, Giant Toad, Mistcougar Runt, Old
                        Mistcougar Runt, Ancient Mistcougar Runt, Giant Stag,
                        Monitor Lizard, Sabretooth Tiger, Small Mistcougar,
                        Terrorbird, Giant Snake, Mistcougar, Ancient Mistcougar,
                        Old Mistcougar, Ancient Basilisk, Old White, Moose,
                        Hyena, Swamp Dragon, Old Basilisk Aspect, Old
                        White&apos;s Aspect, Mature Sabretooh Tiger, Large
                        Mistcougar, Ancient Large Mistcougar, Old Large
                        Mistcougar, Ancient Large Basilisk, Feral Boar, Bighorn
                        Rhino, Rhino, Old Large Basilisk Aspect, Alpha
                        Mistcougar, Ancient Alpha Mistcougar, Old Alpha
                        Mistcougar, Ancient Giant Basilisk, Feral Bear, Ancient
                        Mammoth, Mammoth, Old Giant Basilisk Aspect
                      </span>
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Loot a wild Baby Animal</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Loot 3 wild Baby Animals</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Loot 5 different Baby Animals</td>
                    <td className="text-muted">TODO: Add reward</td>
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
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                </tbody>
              </Table>

              <h4>Fishing (21)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 300 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Catch your first fish</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Eat 5 fish</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Catch 3 types of fish</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Eat 20 fish</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Catch a saltwater fish</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Catch 6 types of fish</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Catch a fish with Fish Bait</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Catch 10 types of fish</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Catch 15 types of fish</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Catch 21 types of fish</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Catch 28 types of fish</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Catch a Shark</td>
                    <td className="text-muted">TODO: Add reward</td>
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
                        Shallowshore Squid, Midwater Octopus, Deepwater Kraker,
                        Shark
                      </span>
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Catch fish worth 3,000 Fame</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Catch fish worth 10,000 Fame</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Catch fish worth 30,000 Fame</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Catch fish worth 100,000 Fame</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Catch fish worth a million Fame</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Catch fish worth 3 million Fame</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Catch fish worth 10 million Fame</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                </tbody>
              </Table>

              <h4>Resource Creatures (21)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 300 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Harvest 30 resources from Resource Mobs</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Harvest resources from 3 Resource Mobs</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Harvest resources from 7 Resource Mobs</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Harvest resources from 12 Resource Mobs</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Harvest resources from an Aspect</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Harvest resources from 18 Resource Mobs</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Harvest resources from an Aspects in every biome
                      <br />
                      <span className="text-muted">
                        Steppe, Swamp, Mountain, Forest, Highland, Roads of
                        Avalon
                      </span>
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Harvest resources from 25 Resource Mobs</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Harvest resources from a Guardian in the Roads of Avalon
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Harvest resources from 34 Resource Mobs</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Harvest 3,000 resources from Aspects</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Harvest resources from 46 Resource Mobs</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Harvest 3,000 resources from Ancient Resource Mobs</td>
                    <td className="text-muted">TODO: Add reward</td>
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
                        Baslat Elemental, Old Basalt Elemental, Elder Forest
                        Spirit, Ancient Ashenbark Spirit, Old Ashenbark Spirit,
                        Ghost Hemp Dryad, Ancient Ghost Hemp Dryad, Old Ghost
                        Hemp Dryad, Adamantium Elemental, Ancient Adamantium
                        Elemental, Old Adamantium Elemental, Marble Elemental,
                        Ancient Marble Elemental, Old Marble Elemental,
                        Whitewood Spirit, Ancient Whitewood Spirit, Old
                        Whitewood Spirit
                      </span>
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Harvest 100 resources from Resource Mobs</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Harvest 300 resources from Resource Mobs</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Harvest 1,000 resources from Resource Mobs</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Harvest 10,000 resources from Resource Mobs</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Harvest 30,000 resources from Resource Mobs</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                </tbody>
              </Table>

              <h4>Biomes (26)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 300 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Gather 250 resources in a yellow zone</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Gather 250 resources in a yellow zone while faction
                      flagged
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gather 250 resources in the yellow mists</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gather 250 resources in a red zone</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Gather 250 resources in a red zone while faction flagged
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gather 250 resources in a black zone</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gather 250 resources in the black Mists</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gather 250 resources in a the Roads of Avalon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gather 250 resources in Mountain regions</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gather 250 resources in Forest regions</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gather 250 resources in Steppe regions</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gather 250 resources in Highland regions</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gather 250 resources in Swamp regions</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gather 1,000 resources in Mountain regions</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gather 1,000 resources in Forest regions</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gather 1,000 resources in Steppe regions</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gather 1,000 resources in Highland regions</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gather 1,000 resources in Swamp regions</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gather 1,000 resources in Black Zones</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gather 10,000 resources in Mountain regions</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gather 10,000 resources in Forest regions</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gather 10,000 resources in Steppe regions</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gather 10,000 resources in Highland regions</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gather 10,000 resources in Swamp regions</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gather 10,000 resources in Black Zones</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gather 50,000 resources in Black Zones</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                </tbody>
              </Table>
            </AccordionBody>
          </AccordionItem>
        </UncontrolledAccordion>
      </div>

      {/* Exploration */}
      <div>
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
                    <th style={{ width: 300 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Visit a Royal City</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Visit three Royal Cities</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Visit Caerleon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Visit a Portal Town</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Use the Invisibility Shrine in a Portal Town</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Find the lost city of Brecilien</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Purchase an item from Eralia Wayfarer in Brecilien</td>
                    <td className="text-muted">TODO: Add reward</td>
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
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Visit a Rest in the Outlands</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Visit all Rests in the Outlands</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                </tbody>
              </Table>

              <h4>Travel (28)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 300 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Ride a Horse</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Find a Hidden Treasure in the open world</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Ride an Ox</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Travel 20 kilometers</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Ride a Direwolf</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Find 5 Hidden Treasures in the open world</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Ride an Adventurer`&apos;s Challenge Mount</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Find 10 Hidden Treasures in the open world</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Ride a Faction Mount</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Find 20 Hidden Treasures in the open world</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Ride a Mystic Owl from Brecilien</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Find 40 Hidden Treasures in the open world</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Ride an Elite Faction Warware mount</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Find 65 Hidden Treasures in the open world</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Ride a Battle Mount</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Find 100 Hidden Treasures in the open world</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Find all Faction Warfare Mounts
                      <br />
                      <span className="text-muted">
                        Saddled Moabird, Saddled Winter Bear, Saddled Wild Boar,
                        Saddled Bighorn Ram, Saddled Swamp Salamander, Saddled
                        Greywold, Elite Terrorbird, Elite Winter Bear, Elite
                        Wild Boar, Elite Bighorn Ram, Elite Swamp Salamander,
                        Elite Greywolf
                      </span>
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Find 200 Hidden Treasures in the open world</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Ride a Transport Mammoth</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Find 500 Hidden Treasures in the open world</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Ride a Command Mammoth</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Travel 50 kilometers</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Travel 100 kilometers</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Travel 200 kilometers</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Travel 500 kilometers</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Travel 1,000 kilometers</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Travel 3,000 kilometers</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Travel 10,000 kilometers</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                </tbody>
              </Table>

              <h4>Zone Types (12)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 300 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Enter a Yellow Zone</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Earn 10,000 Fame in Yellow Zones</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Enter a Red Zone</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Earn 20,000 Fame in Red Zones</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Enter a Black Zone</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Use the Journey Back ability in a Black Zone</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Earn 40,000 Fame in Black Zones</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Earn 80,000 Fame in Quality Level 2 Black Zones</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Earn 120,000 Fame in Quality Level 3 Black Zones</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Earn 250,000 Fame in Quality Level 4 Black Zones</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Earn 500,000 Fame in Quality Level 5 Black Zones</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Earn a million Fame in Quality Level 6 Black Zones</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                </tbody>
              </Table>

              <h4>Reputation (7)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 300 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Reach the first positive reputation level</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Reach the reputation level: Virtuous</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Reach the reputation level: Noble</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Reach maximum reputation level</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Reach the first negative reputation level</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Reach the reputation level: Nefarious</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Reach minimum reputation level</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                </tbody>
              </Table>

              <h4>Mists (32)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 300 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Follow a Will o&apos; Wisp into the Mists</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Rescue 10 Wisps</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Open 5 Small Caches</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Open 5 Medium Caches</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Enter Knightfall Abbey</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Open 3 chests in Knightfall Abbey</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Deliver a Weakened Wisp to a Sanctuary</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gain Accepted Status with Brecilien</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Earn 50,000 Fame in Solo Lethal Mists</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Rescue 30 Wisps in Solo Lethal Mists</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Deliver a Weakened Wisp in Lethal Mists</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Open 20 chests in Knightfall Abbey</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gain 50,000 Fame in Greater Mists</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Rescue 50 Wisps in Greater Mists</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Deliver 5 Weakened Wisps in Greater Mists</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Open 100 chests in Knightfall Abbey</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Deliver 50 Weakened Wisps in Solo Lethal Mists</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Earn 500,000 Fame in Solo Lethal Mists</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Earn a million Fame in Solo Lethal Mists</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Earn 5 million Fame in Solo Lethal Mists</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Earn 10 million Fame in Solo Lethal Mists</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Earn 500,000 Fame in Greater Mists</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Earn a million Fame in Greater Mists</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Earn 5 million Fame in Greater Mists</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Earn 10 million Fame in Greater Mists</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Open 500 chests in Knightfall Abbey</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Open 1,000 chests in Knightfall Abbey</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Get &apos;Welcomed&apos; Brecilien standing</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Get &apos;Favored&apos; Brecilien standing</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Get &apos;Esteemed&apos; Brecilien standing</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Get &apos;Venerated&apos; Brecilien standing</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Kill a &apos;Mysterious Stranger&apos; that&apos;s your
                      friend or ally
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                </tbody>
              </Table>

              <h4>Might & Favor (14)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 300 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Earn 100 Might</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Earn 50 Favor</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Trade your Favor for an item at the Energy Manipulator
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Earn 1,000 Might</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Trade your Favor for a Conqueror&apos;s Chest at the
                      Energy Manipulator
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Earn 8,000 Might</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Earn 5,000 Favor</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Earn 40,000 Might</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Earn 100,000 Might</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Earn 200,000 Might</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Earn 120,000 Favor</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Earn 1 million Might</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Earn 2 million Might</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Earn 5 million Might</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                </tbody>
              </Table>

              <h4>Roads of Avalon (26)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 300 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Enter a Road of Avalon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat 50 mobs in the Roads of Avalon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Open an Avalonian Chest in the Roads of Avalon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Enter a Deep Road of Avalon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat 500 mobs in the Roads of Avalon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Open a Blue Avalonian Chest in the Roads of Avalon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Open a Rare Avalonian Chest in the Roads of Avalon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Open 30 Green Chests in Roads of Avalon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat 2,000 mobs in the Roads of Avalon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Open a Yellow Avalonian Chest in the Roads of Avalon
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat 5,000 mobs in the Roads of Avalon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Open 50 Blue Chests in Roads of Avalon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Open 100 Green Chests in Roads of Avalon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Open a Legendary Chest in the Roads</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Open 150 Blue Chests in Roads of Avalon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Open a Legendary Yellow Chest in the Roads of Avalon
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Open 50 Yellow Chests in Roads of Avalon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Open 500 Green Chests in Roads of Avalon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Open 500 Blue Chests in Roads of Avalon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Open 500 Yellow Chests in Roads of Avalon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Earn 1 million Fame in the Roads of Avalon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Earn 3 million Fame in the Roads of Avalon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Earn 10 million Fame in the Roads of Avalon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Earn 30 million Fame in the Roads of Avalon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Earn 100 million Fame in the Roads of Avalon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                </tbody>
              </Table>
            </AccordionBody>
          </AccordionItem>
        </UncontrolledAccordion>
      </div>

      {/* PVP */}
      <div>
        <UncontrolledAccordion id="pvp">
          <AccordionItem>
            <AccordionHeader targetId="pvp">PvP (181)</AccordionHeader>
            <AccordionBody accordionId="pvp">
              <h4>Arena (27)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 300 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Win your first Arena match</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Win 5 Arena or Crystal Arena Matches</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Win 10 Arena or Crystal Arena Matches</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Deal 15,000 damage in an Arena or Crystal Arena Match
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Win 20 Arena or Crystal Arena Matches</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Win 35 Arena or Crystal Arena Matches</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Capture 4 Runestones in an Arena or Crystal Arena Match
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Win 50 Arena or Crystal Arena Matches</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Deal 22,000 damage in an Arena or Crystal Arena Match
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Win 75 Arena or Crystal Arena Matches</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Take 20,000 damage without dying in an Arena or Crystal
                      Arena Match
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Win 100 Arena or Crystal Arena Matches</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Heal 15,000 health in an Arena or Crystal Arena Match
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Win 150 Arena or Crystal Arena Matches</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Get 10 kills in an Arena or Crystal Arena Match</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Win 200 Arena or Crystal Arena Matches</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Deal 30,000 damage in an Arena or Crystal Arena Match
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Win 250 Arena or Crystal Arena Matches</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Capture 8 Runestones in an Arena or Crystal Arena Match
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Win 300 Arena or Crystal Arena Matches</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Deal 40,000 damage in an Arena or Crystal Arena Match
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Deal 50,000 damage in an Arena or Crystal Arena Match
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Take 50,000 damage without dying in an Arena or Crystal
                      Arena Match
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Heal 30,000 health in an Arena or Crystal Arena Match
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Heal 50,000 health in an Arena or Crystal Arena Match
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Heal 75,000 health in an Arena or Crystal Arena Match
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                </tbody>
              </Table>

              <h4>Crystal Arena (21)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 300 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Increase your rank in the Crystal Arena</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Reach Iron III in Crystal Arena</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Reach Iron IV in Crystal Arena</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Reach Bronze Rank in Crystal Arena</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Reach Bronze II Rank in Crystal Arena</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Reach Bronze III Rank in Crystal Arena</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Reach Bronze IV Rank in Crystal Arena</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Reach Silver Rank in Crystal Arena</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Reach Silver II Rank in Crystal Arena</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Reach Silver III Rank in Crystal Arena</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Reach Silver IV Rank in Crystal Arena</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Reach Gold Rank in Crystal Arena</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Reach Gold II Rank in Crystal Arena</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Reach Gold III Rank in Crystal Arena</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Reach Gold IV Rank in Crystal Arena</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Reach Crystal Rank in Crystal Arena</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Win a match by 50 point margin</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Win a match by 75 point margin</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Win a match by 100 point margin</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Win a match by 125 point margin</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Win a match by 150 point margin</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                </tbody>
              </Table>

              <h4>Corrupted Dungeons (21)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 300 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Defeat the final boss in a Hunter Corrupted Dungeon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Get 666 Infamy in Corrupted Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Defeat another player after invading their Corrupted
                      Dungeon
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat an invading player in a Corrupted Dungeon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Get 2,500 Infamy in Corrupted Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat 5 players in a Hunter Corrupted Dungeon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Defeat the final boss in a Stalker Corrupted Dungeon
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Get 10,000 Infamy in Corrupted Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat a player in a Stalker Corrupted Dungeon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Get 50,000 Infamy in Corrupted Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat 5 players in a Stalker Corrupted Dungeon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Unlock the Slayer difficulty in a Corrupted Dungeons
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat a player in a Slayer Corrupted Dungeon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Get 300,000 Infamy in Corrupted Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat 5 players in a Slayer Corrupted Dungeon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat 100 players in full-loot Corrupted Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat 300 players in full-loot Corrupted Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Get 1,000,000 Infamy in Corrupted Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat 666 players in full-loot Corrupted Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Get 6,660,000 Infamy in Corrupted Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                </tbody>
              </Table>

              <h4>Faction Warfare (30)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 300 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Enlist in any of the six City Factions</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Capture an Outpost</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Assist in a complete capturing another city&apos;s zone in
                      Faction Warfare
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Earn a Faction Warfare Daily Reward</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Knock down or assist a knockdown of an enemy faction
                      player
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Capture 10 Outposts</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Reach 15,000 standing with any Faction</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat 2 different Faction Champions</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Reach 30,000 standing with any Faction</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Capture 30 Outposts</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Finish a Trade Mission for any city</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Reach 60,000 standing with any Faction</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Capture 5 Outposts in Red Zones</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat 3 different Faction Champions</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Kill or assist of an enemy faction player in Red Zone
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Help repel a Bandit Assault</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Reach 240,000 standing with any Faction</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Capture 100 Outposts</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Achieve a standing of 330,000 with any Faction</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Defeat all opposing City Faction Warmasters at least once
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Capture 300 Faction Outposts</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Knock down or assist knockdowns of 30 enemy faction
                      players
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Knock down or assist knockdowns of 100 enemy faction
                      players
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Knock down or assist knockdowns of 300 enemy faction
                      players
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Knock down or assist knockdowns of 1000 enemy faction
                      players
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Kill or assist 30 enemy faction player kills in Red Zones
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Kill or assist 100 enemy faction player kills in Red Zones
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Kill or assist 300 enemy faction player kills in Red Zones
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Kill or assist 1,000 enemy faction player kills in Red
                      Zones
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                </tbody>
              </Table>

              <h4>Open World PvP (32)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 300 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Open an open-world Treasury Chest</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Knock down another player in a Yellow Zone</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Open 10 open-world Treasury Chests</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Kill or assist a kill in PvP</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Loot any armor, foot gear and a mount from a killed player
                      at the same time
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Get 200,000 Kill Fame</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Kill 10 players in full-loot regions</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Kill 3 players in the Roads of Avalon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Kill 25 players in full-loot regions</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Kill 10 players in Static Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Get 2 million Kill Fame in the Open World</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Kill 6 players within one minute</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Kill 100 players in full-loot regions</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Get 2 million Kill Fame in the Roads of Avalon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Get 5 million Kill Fame in Static Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Kill 6 players within one minute (not including assists)
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Kill 300 players in the open world</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Get 10 million Kill Fame in Black Zones</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Get 10 million Kill Fame in Static Dungeons</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Get 10 million Kill Fame in the Roads of Avalon</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Get 50 million Kill Fame in Black Zones</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Get 100 million Kill Fame in Black Zones</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Get 500 million Kill Fame in Black Zones</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Open 30 open-world Treasure Chests in full-loot regions
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Open 100 open-world Treasure Chests</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Open 30 Medium Treasure Chests</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Open 10 Large Treasury Chests</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Open 500 open-world Treasure Chests</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Open 300 Medium Treasure Chests</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Open 100 Large Treasury Chests</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Open a Legendary Large Treasury Chest</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Get killed by another player</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                </tbody>
              </Table>

              <h4>Hellgates (33)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 300 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Defeat 5 Mini Bosses in Hellgates</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat a Boss in Hellgates</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gain 50,000 Infamy in 2v2 Hellgates</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Chain 5 lethal Hellgates without returining to the surface
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Knock down 50 players in Hellgates</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Kill a player in a full-loot Hellgate</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Enter a Hellgate</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat a Mini Boss in a Hellgate</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Defeat a team of enemy players in any type of Hellgate
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Chain 2 lethal Hellgates without returining to the surface
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gain 20,000 Infamy in 2v2 Hellgates</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Knock down 10 players in Hellgates</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gain 100,000 Infamy in 2v2 Hellgates</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat a Mini Boss in a 5v5 Hellgate</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat an enemy team in a 5v5 Hellgate</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gain 50,000 Infamy in 5v5 Hellgates</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Knock down 200 players in Hellgates</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gain 100,000 Infamy in 5v5 Hellgates</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Kill 20 players in full-loot Hellgates</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>
                      Chain 10 lethal Hellgates without returining to the
                      surface
                    </td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Kill 50 players in full-loot Hellgates</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat a Mini Boss in a 10v10 Hellgate</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Defeat a team of enemy players in a 10v10 Hellgate</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Kill 200 players in full-loot Hellgates</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Kill 500 players in full-loot Hellgates</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Kill 1,000 players in full-loot Hellgates</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gain 250,000 Infamy in 2v2 Hellgates</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gain 500,000 Infamy in 2v2 Hellgates</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gain 250,000 Infamy in 5v5 Hellgates</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gain 500,000 Infamy in 5v5 Hellgates</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gain 100,000 Infamy in 10v10 Hellgates</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gain 250,000 Infamy in 10v10 Hellgates</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Gain 500,000 Infamy in 10v10 Hellgates</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                </tbody>
              </Table>

              <h4>Crystal League (17)</h4>
              <Table responsive striped borderless hover dark>
                <thead>
                  <tr>
                    <th>Name</th>
                    <th style={{ width: 300 }}>Reward</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Participate in a Crystal League Battle</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Win a 5v5 Crystal League Battle</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Win a Rank 2 5v5 Crystal League Battle</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Win a Rank 3 5v5 Crystal League Battle</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Win a 20v20 Crystal League Battle</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Win a Rank 4 5v5 Crystal League Battle</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Win a Rank 5 5v5 Crystal League Battle</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Win a Rank 6 5v5 Crystal League Battle</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Win a Rank 7 5v5 Crystal League Battle</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Win a Rank 8 5v5 Crystal League Battle</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Win a Rank 9 5v5 Crystal League Battle</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Win a Rank 2 20v20 Crystal League Battle</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Win a Rank 3 20v20 Crystal League Battle</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Win a Rank 4 20v20 Crystal League Battle</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Win a Rank 5 20v20 Crystal League Battle</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Win a Rank 6 20v20 Crystal League Battle</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                  <tr>
                    <td>Win a Rank 7 20v20 Crystal League Battle</td>
                    <td className="text-muted">TODO: Add reward</td>
                  </tr>
                </tbody>
              </Table>
            </AccordionBody>
          </AccordionItem>
        </UncontrolledAccordion>
      </div>
    </div>
  );
};

export default AlbionJournal;
```