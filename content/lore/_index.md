---
title: "Lore"
noindex: false
weight: 1
description: "Walkthrough guide to unlocking all the currently known secrets and mysteries found in Brookhaven RP."

images: 
- images/bh/collage.png
- images/bh/agency_greed_desk_1_button.jpg
aliases:
- /mermaid/steps_flow
---



### What is the Lore of Brookhaven RP?

We started out with a few hints around the Town of Brookhaven. A movie clip, some notes, a strange experimentation room above the hospital. But what does it all mean?

We're on a mystery hunt to find clues and solve the mystery of Brookhaven!


{{% button href="./quests/" hint="Click Me"  style="green" %}}Get Started!{{% /button %}}

<hr style="background-color: #28b44c" size=8>

### Where to get started

If  you're new to Secrets and Mysteries of Brookhaven, it's suggested starting out getting the [Connected Laptop](/lore/tools/connect_laptop) in the [Tools](/lore/tools) section and then following the [Quests](/lore/quests/). They are laid out in a way here to keep from jumping around too much, but they don't have to be done in any particular order.

If you're pretty familiar or want to look at a specific thing, each tool, special tool, and quest will list requirements they have so you can easily decide where you would like to start!
{{% notice style="tip" %}}
Keep in mind, maybe there are steps we shouldn't do, though commonly the community feels all steps and lights in the [Agency Light Panel](../../casebook/light_panel/) should be done to solve the mystery.
{{% /notice %}}









<hr style="background-color: #28b44c" size=8>

### Why are some things a quest, and others not?

The flow of investigating can be... chaotic. But I have identified there are tools, special tools, and quests to help guide you through your journey on what has been discovered.



{{% button href="./tools/" style="green" %}}Tools{{% /button %}}: These are items that give us hints along the way of our investigation.

{{% button href="./special_tools/" style="green" %}}Special Tools{{% /button %}}: These are items not available in inventory and are needed for other quests.

{{% button href="./quests/" style="green" %}}Quests{{% /button %}}: These are considered main story line quests, they may unlock, build, or show us new hints. Since this is an ever updating game, we don't know if a quest is ever really complete. 

---

To get a sense of what the flow looks like, checkout the diagram below.

>You can also zoom in to make it easier to see each step, don't worry zooming in doesn't lose quality... there's a lot here!


>Some of the boxes are clickable to take you to the appropriate page for more details, actively working on making it more apparent which ones are clickable :hear:

{{< mermaid align="center" zoom="true" >}}
graph LR
%% Short Steps
    A24[A24: Power Coupler on/off]
    A25[A25: PSU inf. +/-]
	
	binoculars --> H08
    coffin --> A23
    plant_book --> H06
	A15 --> green_keycard
%% End short steps
%% rod under arch
%% A22 has to be clicked again before collecting rod
    bakery_button --> A22a --> rod_under_arch --> H07
%% Glowing Chair
    H07 --> use_rod[Use Rod in Museum] --> glowing_chair

    
    A22 --> energy_pyramid




	
	%% frat house
    laptop --> sit
    sit --> H02
    H02 --> H03
	

    A02 --> A03
    H04 --> A04
    A04 --> A05
    A05 --> laptop_connected
    

    A08 --> A26
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
    



    hospital_paper --> message_sent --> barn_button --> tslvl1
    barn_button --> tslvl1_msg
    tslvl1 --> scalpel
    scalpel --> hospital_button --> sit_hospital
    sit_hospital --> mall_lever
    mall_lever --> A27
    
    blue_keycard --> A02
    A03 --> A21
	

	

	
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
    frame --> motel_button
    motel_button --> X02
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
    A22a[A22: Enemy Signal Detected]
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
    tslvl1>Unlocked: TS Level 1 Authorized]
    tslvl1_msg[["TS [LVL 1] Permissable"]]
    binoculars[Click/Item: binoculars]
    blue_keycard[Item: Blue Key Card]
	green_keycard[Item: Green Key Card]
	laptop_connected[Item: Laptop Connected]
    book_undertable[Click: Book Under Table - Motel]
    frame[Click: Frame - Motel]
    motel_button[Click: Motel Button]
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
    hospital_paper[Click: Paper Stack Hidden X-Ray Room]
    barn_button[Click: Barn Button second floor] 
    message_sent[[Message Sent]]
    rod_under_arch[Item: Rod under arch]
    click A01 href "../../casebook/light_panel/#a01" "A01 Details"
    click A02 href "../../casebook/light_panel/#a02" "A02 Details"
    click A03 href "../../casebook/light_panel/#a03" "A03 Details"
    click A04 href "../../casebook/light_panel/#a04" "A04 Details"
    click A05 href "../../casebook/light_panel/#a05" "A05 Details"
    click A06 href "../../casebook/light_panel/#a06" "A06 Details"
    click A07 href "../../casebook/light_panel/#a07" "A07 Details"
    click A08 href "../../casebook/light_panel/#a08" "A08 Details"
    click A09 href "../../casebook/light_panel/#a09" "A09 Details"
    click A10 href "../../casebook/light_panel/#a10" "A10 Details"
    click A11 href "../../casebook/light_panel/#a11" "A11 Details"
    click A12 href "../../casebook/light_panel/#a12" "A12 Details"
    click A13 href "../../casebook/light_panel/#a13" "A13 Details"
    click A14 href "../../casebook/light_panel/#a14" "A14 Details"
    click A15 href "../../casebook/light_panel/#a15" "A15 Details"
    click A16 href "../../casebook/light_panel/#a16" "A16 Details"
    click A17 href "../../casebook/light_panel/#a17" "A17 Details"
    click A18 href "../../casebook/light_panel/#a18" "A18 Details"
    click A19 href "../../casebook/light_panel/#a19" "A19 Details"
    click A20 href "../../casebook/light_panel/#a20" "A20 Details"
    click A21 href "../../casebook/light_panel/#a21" "A21 Details"
    click A22 href "../../casebook/light_panel/#a22" "A22 Details"
    click A23 href "../../casebook/light_panel/#a23" "A23 Details"
    click A24 href "../../casebook/light_panel/#a24" "A24 Details"
    click A25 href "../../casebook/light_panel/#a25" "A25 Details"
    click A26 href "../../casebook/light_panel/#a26" "A26 Details"
    click A27 href "../../casebook/light_panel/#a27" "A27 Details"
{{< /mermaid >}}