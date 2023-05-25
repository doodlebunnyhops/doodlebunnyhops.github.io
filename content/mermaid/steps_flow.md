---
title: "Lore Steps Visual"
---

Want to see a better view of this diagram, check it out [here](/images/bh/mermaid-diagram-2023-05-24-083839.svg)

{{< mermaid >}}
flowchart LR
%% Short Steps
    A24[A24: Power Coupler on/off]
    A25[A25: PSU inf. +/-]
    click A24 href "https://www.github.com" "This is a link"
	
	binoculars --> H08
    coffin --> A23
    plant_book --> H06
	blue_keycard --> A02
	A15 --> green_keycard
    A22 --> energy_pyramid
%% End short steps
    bakery_button --> H07
	
	%% frat house
    laptop --> sit
    sit --> H02
    H02 --> H03
	

    A02 --> A03
    H04 --> A04
    A04 --> A05
    A05 --> laptop_connected
    energy_pyramid --> A07
    A17 --> A14
    A20 --> A17



    red_book --> A18
    tslvl1 --> A19
    A19 --> A20

    A09 --> A21
    A01 -->|On| A21
    A06 -->|Off| A21
    A06 -->|On| A17
	A01 -->|Off| A17
    V08 --> A21
    A03 --> A21



    tslvl1 --> scalpel
    scalpel --> hospital_button --> sit_hospital
    sit_hospital --> mall_lever
    mall_lever --> A27

    A08 --> A26
	
%% Glowing Chair
    H07 --> glowing_chair
	
%% rod under arch
    energy_pyramid --> H07
%%    bakery_button --> H07
	
%% chair room
    energy_pyramid --> password
    password --> A26
    H03 --> A26

%% The Red Book
    burn_file --> X01
    X01 --> red_book

%% Build Portal
    red_book --> book_undertable
    book_undertable --> frame
    frame --> hotel_button
    hotel_button --> X02
    X02 --> A16

    red_book --> ghost
	
	A02[A02: Access to Secondary Program Granted]
    A03[A03: Brookhaven Electric main power on]
    A04[A04: Energy Relay Charged]
    A05[A05: Arch Main Power Inverted /Connection Acquired]
    A06[A06: Power Relay on/off - High Voltage Switch]
    A01[A01: Power Relay on/off - Danger Switch]
    A07[A07: Insignia Unlocked]
    A08[A08: Signal Array Online/Disruption]
    A09[A09: SQL Injection Complete]
    A14["A14: Coordinates approved, A(x1,y1) and B(x2,y2)"]
    A15[A15: Apparition of the Crow]
    A16[A16: Hydrogen beam accelerator complete]
    A17[A17: Power configured to crystals]
    A18[A18: Carbon ingot articulation Arch forcefield :NO ERRORS:]
    A19[A19: Energy Crystals released]
    A20[A20: Awaiting Power]
    A21[A21: No Text]
    A22[A22: Enemy Signal Detected]
    A23["A23: Asystole Reversal  (Error)"]
    A26[A26: Inferential delusion mechanism available]
    A27[A27: In Darkness]
    H02[H02: Hidden Dorm Unlocked]
    H03[H03: Unlocked Bunker Control Screen]
    H04[H04: Crystal Found]
    H06[H06: Plant Quantum saved]
    H07[H07: Town Signal ready]
    H08[H08: Counter intelligence detected]
    V08[V08: E-Thermal control online]
    X01["X01: Agency knowledge released [Caution]"]
    X02["X02: The Book power unveiled [Follow]"]
    energy_pyramid[Item: Energy Pyramid]
    red_book[Item: Red Book]
    tslvl1[Unlock: TS Level 1]
    binoculars[Click/Item: binoculars]
    blue_keycard[Item: Blue Key Card]
	green_keycard[Item: Green Key Card]
	laptop_connected[Item: Laptop Connected]
    book_undertable[Click: Book Under Table - Hotel]
    frame[Click: Frame - Hotel]
    hotel_button[Click: Hotel Button]
    laptop[Item: Laptop, connected or not]
    sit[Action: Sit in chair]
    sit_hospital[Action: Sit in chair - Hospital]
    hospital_button[Click: Hospital Button]
    password[Password]
    bakery_button[Click: Bakery Button]
    plant_book[Click: Green Plant Book]
    ghost[Unlock: Ghostly Sighting]
    glowing_chair[Unlock: Glowing Chair]
    coffin[Click: Coffin]
    burn_file[Click: Burn Agency File]
    scalpel[Click: Scalpel]
    mall_lever[Action: Flip left lever behind TV Station]
{{< /mermaid >}}

{{< button "../../lore/" "Back to Lore" "mb-1" >}}