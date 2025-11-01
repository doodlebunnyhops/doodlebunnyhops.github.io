---
linktitle: "Путеводитель"
title: "Brookhaven RP: Прохождение, Секреты, Квесты и Тайны"
noindex: false
weight: 1
description: "Разгадайте тайны Brookhaven RP с этим подробным путеводителем. Выполняйте квесты, раскрывайте загадки и исследуйте инструменты и скрытые локации в игре."

images: 
- images/bh/collage.webp
- images/bh/agency_greed_desk_1_button.webp
aliases:
- /mermaid/steps_flow
collapsibleMenu: true
---

## Добро пожаловать в путеводитель по Brookhaven RP

Начните с квестов, инструментов и пошагового руководства, которое поможет вам раскрыть скрытую историю Brookhaven.

{{% button href="./quests/" hint="Исследовать квесты" style="green" %}}Начать исследование!{{% /button %}}

### Какова история Brookhaven RP?

Brookhaven — это город, окутанный тайнами. Секретные базы, призрачные видения, высокие технологии и зашифрованные послания — каждый уголок скрывает подсказки.  

В центре всего этого стоит Агентство, загадочная организация, чьи эксперименты оставили после себя множество тайн.  

Исследуйте скрытые локации, разгадывайте головоломки и соединяйте фрагменты истории через квесты. Каждое новое открытие раскрывает ещё один слой истории Brookhaven — истории жадности, страха и неизвестности.  

Игра постоянно обновляется, добавляя всё больше загадок для раскрытия.

<hr style="background-color: #28b44c" size=8>

### С чего начать?

Если вы новичок в Тайнах и Загадках Brookhaven, рекомендуется сначала получить [Подключённый ноутбук](/lore/tools/connect_laptop) в разделе [Инструменты](/lore/tools), а затем следовать квестам в разделе [Квесты](/lore/quests/).  

Квесты расположены так, чтобы избежать хаотичного переключения между задачами, но их не обязательно выполнять в определённом порядке.  

Если вы уже знакомы с игрой или ищете что-то конкретное, в каждом разделе (инструменты, специальные инструменты и квесты) указаны все требования. Это поможет вам выбрать, с чего начать!

{{% notice style="tip" %}}
Помните, что, возможно, не все шаги нужно выполнять. Однако в сообществе считается, что все шаги и огни на [Панели огней Агентства](../../casebook/light_panel/) необходимо активировать, чтобы разгадать тайну.
{{% /notice %}}

<hr style="background-color: #28b44c" size=8>

### Предпочитаете видео?  

:heart: O1G сделал полное прохождение со всеми последними секретами дома Агентства RP!

<div class="grid-1 post-vid-dot">
{{< youtube id=Exnr-wQ76Fs loading=lazy >}}
</div>

<hr style="background-color: #28b44c" size=8>

### Почему одни вещи считаются квестами, а другие нет?

Исследование Brookhaven может быть... хаотичным.  

Но я выделила инструменты, специальные инструменты и квесты, чтобы направить вас и помочь разобраться, что уже было обнаружено.

- {{% button href="/ru/lore/tools/" style="green" %}}Инструменты{{% /button %}} — это предметы, которые дают подсказки в ходе расследования.  
- {{% button href="/ru/lore/special_tools/" style="green" %}}Специальные инструменты{{% /button %}} — это предметы, которые не добавляются в инвентарь, но нужны для других квестов.  
- {{% button href="/ru/lore/quests/" style="green" %}}Квесты{{% /button %}} — основная сюжетная линия. Они могут разблокировать, построить или дать новые подсказки.  

Так как игра постоянно обновляется, мы никогда не знаем наверняка, завершён ли квест окончательно.

---

### Как выглядит общий ход расследования?

Посмотрите схему ниже, чтобы увидеть структуру взаимодействий в игре.

> Вы можете увеличить масштаб, чтобы лучше рассмотреть каждый шаг!  

> Некоторые блоки кликабельны и ведут на соответствующие страницы с подробной информацией. Я работаю над тем, чтобы было проще понять, какие из них можно открыть. :hear:


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
