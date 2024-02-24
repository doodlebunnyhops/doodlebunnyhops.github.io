---
title: "Abandoned House"
weight: 1
date: 2024-01-02
description: "Brookhaven Abandoned House location and related details"
image: map/abandoned_house.jpg
images: 
- map/abandoned_house.jpg
Categories: ["point of interest","map"]
Tags: ["abandoned house"]
draft: false
--- 

<script>
function markExternalLinks() {
    let links = elems('a');
    if(links) {
      try {
        Array.from(links).forEach(function(link){
  
          let target, rel, blank, noopener, attr1, attr2, url, is_external;
          if(link.href instanceof SVGAnimatedString){
            console.log("Link HREF type animalVal:");
            console.log(link.href);
            url = new URL(link.href.animVal);
          } else {
            console.log("Link HREF:");
            console.log(link.href);
            url = new URL(link.href);
          }
  
          // definition of same origin: RFC 6454, section 4 (https://tools.ietf.org/html/rfc6454#section-4)
          is_external = url.host !== location.host || url.protocol !== location.protocol || url.port !== location.port;
          if(is_external) {
            target = 'target';
            rel = 'rel';
            blank = '_blank';
            noopener = 'noopener';
            attr1 = elemAttribute(link, target);
            attr2 = elemAttribute(link, noopener);
    
            attr1 ? false : elemAttribute(link, target, blank);
            attr2 ? false : elemAttribute(link, rel, noopener);
          }
        });
        } catch (err) {
        console.log("ERROR");
        console.log(err);
  
      }
      
    }
  }
</script>

![Abandoned House](/images/maps/abandoned_house.jpg)

{{< svg "static/images/maps/abandoned-house.svg" >}}

<hr style="background-color: #28b44c" size=8>

### CaseBook Items

- [Movie Code](/casebook/movie_codes/#abandoned-house-code)
- Agency Light Panel [A19](/casebook/light_panel/#a19)
- Agency Light Panel [A20](/casebook/light_panel/#a20)
- [Monolith Locations 1 and 10](/casebook/monoliths/locations/)
- Note to [Madison](/casebook/notes/madison/#abandoned-house)

<hr style="background-color: #28b44c" size=8>

### Quests

- [Find 7 Crystals](/lore/quests/#find-7-crystals)
- [Glowing Chair](/lore/quests/#glowing-chair)