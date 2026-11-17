#!/usr/bin/env python3
"""Static site generator for optimizediv.com.

Run:  python3 _build/build.py
Writes every page into the site root (one folder per URL, each with index.html),
plus sitemap.xml, robots.txt, llms.txt and netlify.toml.
Edit the content dictionaries below and re-run to update the whole site.
"""
import json, os, html
from urllib.parse import quote

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://optimizediv.com"
UPDATED = "2026-11-17"
UPDATED_H = "November 2026"

NAME = "Optimized Performance & Wellness"
PHONE1, PHONE1_T = "+1 (561) 503-0046", "+15615030046"
PHONE2, PHONE2_T = "+1 (561) 312-6570", "+15613126570"
EMAIL = "optiperfwell@gmail.com"
IG = "https://instagram.com/OptimizedPerformanceWellness"

e = html.escape

def sms(body=None, num=PHONE1_T):
    return f"sms:{num}" + (f"?&body={quote(body)}" if body else "")

# ---------------------------------------------------------------- icons
ICONS = {
 "chat": '<path d="M4 5.5A2.5 2.5 0 0 1 6.5 3h11A2.5 2.5 0 0 1 20 5.5v8a2.5 2.5 0 0 1-2.5 2.5H10l-4.5 4v-4h0A1.5 1.5 0 0 1 4 14.5z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/>',
 "phone": '<path d="M5 3.5h3l1.6 4.3-2 1.3a11 11 0 0 0 5.3 5.3l1.3-2 4.3 1.6v3a2 2 0 0 1-2.2 2A16.5 16.5 0 0 1 3 5.7a2 2 0 0 1 2-2.2z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/>',
 "nurse": '<circle cx="12" cy="7.5" r="3.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="M5 20.5c.8-4 3.6-6 7-6s6.2 2 7 6M12 16.5v3M10.5 18h3" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>',
 "home": '<path d="M3.5 11 12 4l8.5 7M6 9.5V20h12V9.5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M10 20v-5h4v5" fill="none" stroke="currentColor" stroke-width="2"/>',
 "shield": '<path d="M12 3 5 6v5.5c0 4.4 3 8 7 9.5 4-1.5 7-5.1 7-9.5V6z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/><path d="m9 12 2.2 2.2L15.5 10" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>',
 "clock": '<circle cx="12" cy="12" r="8.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="M12 7.5V12l3 2" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>',
 "drop": '<path d="M12 3.5s6 6.6 6 11a6 6 0 0 1-12 0c0-4.4 6-11 6-11z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/>',
 "users": '<circle cx="9" cy="8" r="3.2" fill="none" stroke="currentColor" stroke-width="2"/><path d="M3 19.5c.6-3.3 3-5 6-5s5.4 1.7 6 5M16 5a3 3 0 0 1 0 6M17.5 14.5c2 .6 3.2 2.3 3.5 5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>',
 "pin": '<path d="M12 21s-6.5-6-6.5-11a6.5 6.5 0 0 1 13 0c0 5-6.5 11-6.5 11z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/><circle cx="12" cy="10" r="2.4" fill="none" stroke="currentColor" stroke-width="2"/>',
 "steth": '<path d="M6 3.5v5a4 4 0 0 0 8 0v-5M10 12.5v2a5 5 0 0 0 10 0v-1.5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><circle cx="20" cy="11" r="2" fill="none" stroke="currentColor" stroke-width="2"/>',
 "alert": '<path d="M12 3.5 2.5 20h19z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/><path d="M12 10v4.5M12 17.2v.3" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>',
 "spark": '<path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5 18 18M18 6l-2.5 2.5M8.5 15.5 6 18" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>',
}
def ic(n, s=22):
    return f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" aria-hidden="true">{ICONS[n]}</svg>'

# ---------------------------------------------------------------- content: drips
FLUID = ("1L Lactated Ringer's or Normal Saline", "lactated-ringers-normal-saline")
DRIPS = [
 dict(slug="foundational-meyers", name="Foundational Meyers", price=245, tag="Recharge and replenish", popular=True, goals="sick well",
  short="Our signature drip. Immune support and hydration for when you're coming down with something.",
  ings=[(FLUID,"Restores hydration"),(("Vitamin C","vitamin-c"),"Supports immunity"),(("Glutathione","glutathione"),"Powerful antioxidant"),(("B12","vitamin-b12"),"Boosts energy"),(("B-Complex","b-complex"),"Supports metabolism"),(("Zinc","zinc"),"Fights off germs"),(("Magnesium","magnesium"),"Eases muscle tension")],
  best=["You feel a cold or \"something\" coming on","You're run-down, depleted or not sleeping well","It's your first IV and you want a well-rounded place to start"],
  body="""<p>Foundational Meyers is our take on the classic Myers'-style vitamin infusion and the drip most clients start with. One liter of IV fluids rehydrates you, and a balanced blend of vitamin C, glutathione, B12, B-complex, zinc and magnesium gives your body a broad base of support.</p>
<p>It's the drip we suggest when you can tell you're getting run-down but you're not flat-out sick yet, or when you simply want to feel more like yourself. If you need more, step up to <a href="/iv-menu/optimized-meyers/">Optimized Meyers</a>, which uses higher doses of the same core ingredients.</p>""",
  faqs=[("What is a Meyers drip?","A Meyers (often spelled Myers') drip is a vitamin and mineral IV infusion built around vitamin C, B vitamins and magnesium. Our Foundational Meyers adds glutathione and zinc and is given with 1 liter of IV fluids by a licensed nurse at your home."),
        ("What's the difference between Foundational and Optimized Meyers?","Both share the same core ingredients. Optimized Meyers ($350) uses higher, \"optimized\" doses of vitamin C and glutathione for a deeper reset. Foundational Meyers ($245) is the everyday version and a great first IV.")]),
 dict(slug="travel-defense", name="Travel Defense", price=250, tag="Travel + flu season", popular=False, goals="well sick",
  short="Before or after a trip, or when everyone around you is coughing. Stay one step ahead.",
  ings=[(FLUID,"Flushes and rehydrates"),(("Extra Vitamin C, boosted dose","vitamin-c"),"Fights viruses + infection"),(("Glutathione","glutathione"),"Strengthens immune cells"),(("Zinc","zinc"),"Shortens sick days"),(("Vitamin D or basic add-in of choice","vitamin-d"),"Bolsters immune defense")],
  best=["Before a flight, cruise or big trip","Right after you land, to rehydrate from travel","Flu season, or when your household or office is passing something around"],
  body="""<p>Airports, flights and long travel days are dehydrating, and they put you around a lot of people. Travel Defense pairs a full liter of IV fluids with a boosted dose of vitamin C, glutathione, zinc and vitamin D (or a basic add-in of your choice).</p>
<p>Many clients book it the day before they leave or the day they get home. Visitors staying in Jupiter and Palm Beach County rentals and hotels also book it on arrival. We'll come to wherever you're staying.</p>""",
  faqs=[("When should I get an IV before travel?","Most people book Travel Defense within a day or two before departure, or right after they get home. Text us your dates and we'll find a time that works."),
        ("Can you come to my hotel or vacation rental?","Yes. Our nurses visit homes, offices, hotels and rentals across northern Palm Beach County and the Treasure Coast.")]),
 dict(slug="recover", name="Recover", price=235, tag="Bouncing back", popular=False, goals="recover",
  short="After an illness, a tough week or a hard workout. Rehydrate and replenish so your body can recover.",
  ings=[(FLUID,"Rehydrates tired muscles"),(("Amino Blend","amino-blend"),"Rebuilds muscle tissue"),(("L-Carnitine","l-carnitine"),"Fuels muscle energy"),(("Taurine","taurine"),"Reduces muscle fatigue")],
  best=["After a race, tournament, long ride or heavy training block","When you're over an illness but still dragging","After a long, draining week"],
  body="""<p>Recover is built for muscles and energy. Alongside 1 liter of IV fluids, it combines an amino acid blend, L-carnitine and taurine, nutrients involved in muscle repair and energy production.</p>
<p>It's popular with athletes, golfers, boaters and anyone who has pushed hard in the South Florida heat. It's also a good fit when you're past the worst of an illness but still feel wiped out.</p>""",
  faqs=[("Is IV therapy good for athletic recovery?","IV fluids rehydrate you quickly after heavy sweating, and our Recover drip adds amino acids, L-carnitine and taurine for muscle support. Many athletes book it after races, tournaments or hard training days."),
        ("How soon after a workout can I get the Recover drip?","Any time after you finish. Text us when you're done and we'll schedule the soonest available visit.")]),
 dict(slug="glow", name="Glow", price=300, tag="Brighter skin for your big day", popular=False, goals="glow",
  short="Named for the brighter, more radiant-looking skin it supports. A favorite before weddings, photo shoots, galas and any day you want to look and feel your best.",
  ings=[(FLUID,"Dewy, hydrated skin"),(("Glutathione, boosted dose","glutathione"),"Brighter-looking complexion"),(("Vitamin C, boosted dose","vitamin-c"),"Radiant, even glow"),(("Biotin","biotin"),"Healthy hair + nails")],
  best=["A few days before a wedding, event or photo shoot","Bridal parties and groups getting ready together","Anyone who wants hydrated, rested-looking skin"],
  body="""<p>Glow is our beauty-from-within drip. Full hydration plus boosted doses of glutathione and vitamin C (two antioxidants associated with brighter-looking skin) and biotin for hair and nails.</p>
<p>It's a favorite before weddings, galas and photo shoots, and for bridal parties who want to get ready together. We can treat the whole group in one visit. See <a href="/group-iv-therapy/">group and event IVs</a>.</p>""",
  faqs=[("How far before an event should I get the Glow drip?","Many clients book Glow one to three days before a wedding, photo shoot or event. Text us your date and we'll plan around it."),
        ("Can you do Glow drips for a bridal party?","Yes. We can treat multiple people in one visit at your home, rental or hotel. Let us know how many people when you text so your nurse brings enough for everyone.")]),
 dict(slug="optimized-meyers", name="Optimized Meyers", price=350, tag="Running on empty", popular=False, goals="recover well",
  short="A deeper reset with extra support for energy and recovery on top of the essentials.",
  ings=[(FLUID,"Deep rehydration"),(("Vitamin C, optimized dose","vitamin-c"),"Boosts immune defense"),(("Glutathione, optimized dose","glutathione"),"Detoxes and protects"),(("B12","vitamin-b12"),"Fights fatigue"),(("B-Complex","b-complex"),"Supports metabolism"),(("Magnesium","magnesium"),"Relaxes tight muscles"),(("Zinc","zinc"),"Strengthens immunity")],
  best=["You feel completely drained","Busy seasons, long work weeks or burnout","When Foundational Meyers isn't quite enough"],
  body="""<p>Optimized Meyers is the full-strength version of our signature drip. It has the same well-rounded formula, but with optimized doses of vitamin C and glutathione for a deeper reset when you're running on empty.</p>
<p>Choose it when you've been burning the candle at both ends, are coming off a demanding stretch, or want the most complete version of our everyday wellness drip.</p>""",
  faqs=[("Who is Optimized Meyers best for?","People who feel completely run-down and want a deeper reset. It has the same core ingredients as Foundational Meyers with higher doses of vitamin C and glutathione.")]),
 dict(slug="your-call", name="Your Call", price=150, tag="Build your own", popular=False, goals="sick recover well glow",
  short="IV fluids plus any 3 add-ins you choose from the list below, and many other options are available. Not sure? Your nurse will help you pick.",
  ings=[(FLUID,"Restores hydration"),(("Glutathione","glutathione"),"Powerful antioxidant"),(("Vitamin C","vitamin-c"),"Supports immunity"),(("B-Complex","b-complex"),"Supports metabolism"),(("B12","vitamin-b12"),"Boosts energy"),(("Zinc","zinc"),"Strengthens immunity"),(("Taurine","taurine"),"Reduces muscle fatigue"),(("Biotin","biotin"),"Healthy hair + nails"),(("L-Carnitine","l-carnitine"),"Fuels muscle energy"),(("Amino Blend","amino-blend"),"Rebuilds muscle tissue"),(("NAD+","nad-plus"),"Cellular energy + focus"),(("Magnesium","magnesium"),"Eases muscle tension")],
  best=["You know exactly what you like","Simple hydration with a few extras","Headaches, mild illness or symptoms your nurse can tailor treatment to"],
  body="""<p>Your Call is our build-your-own IV and our most affordable starting price. You get 1 liter of IV fluids plus <b>any three add-ins</b> from the list. Many more options are available, so just ask.</p>
<p>Not sure what to choose? Tell your nurse how you're feeling and they'll help you pick. Often, IV fluids plus the right add-ins (or, when appropriate, medication for aches, fever or nausea) is all it takes to help you start feeling better.</p>""",
  faqs=[("What's the cheapest IV you offer?","Your Call starts at $150. It includes 1 liter of IV fluids plus any three add-ins."),
        ("Can I add more than three add-ins?","Yes. Many other options are available. Text us what you're looking for and we'll quote it.")]),
 dict(slug="get-right", name="Get Right", price=435, tag="Flu, stomach bug, rough night", popular=False, goals="sick",
  short="Our everything bag for the worst days. Fluids, vitamins and antioxidants to get you back on your feet.",
  ings=[(FLUID,"Deep rehydration"),(("Vitamin C, optimized dose","vitamin-c"),"Boosts immune defense"),(("Glutathione, optimized dose","glutathione"),"Detoxes and protects"),(("B12","vitamin-b12"),"Fights fatigue"),(("B-Complex","b-complex"),"Supports metabolism"),(("Magnesium","magnesium"),"Relaxes tight muscles"),(("Zinc","zinc"),"Strengthens immunity")],
  meds=[("Toradol","toradol","Eases pain + aches"),("Zofran","zofran","Stops nausea"),("Pepcid","pepcid","Calms upset stomach"),("Benadryl","benadryl","Settles allergic reactions")],
  best=["Flu, body aches and chills","A stomach bug when nothing will stay down","A rough night out, when you're dehydrated and miserable"],
  body="""<p>Get Right is our everything bag for the days you can barely get off the couch. It starts with a full liter of fluids and optimized doses of vitamin C and glutathione, plus B12, B-complex, magnesium and zinc.</p>
<p>When appropriate, and only after your nurse's assessment, optional medications can be added for pain and aches, nausea, an upset stomach or allergic reactions. You don't have to drive anywhere sick. We come to you.</p>""",
  faqs=[("Are the Get Right medications required?","No. They're optional and only given when appropriate after your nurse's assessment."),
        ("Can IV therapy help with a hangover?","A rough night often leaves you dehydrated and nauseated. IV fluids rehydrate you faster than drinking water, and anti-nausea medication can be added when appropriate. Get Right is the drip most people choose for these days."),
        ("Can I get an IV for a stomach bug?","Yes, as long as your nurse's screening shows it's appropriate. When vomiting or diarrhea makes it hard to keep fluids down, IV fluids rehydrate you directly. Seek emergency care for severe dehydration, especially in children.")]),
]
DRIP = {d["slug"]: d for d in DRIPS}
NAD_NOTE = 'Add <a href="/ingredients/#nad-plus">NAD+</a> to any drip for $50.'

# ---------------------------------------------------------------- content: ingredients
INGREDIENTS = [
 ("lactated-ringers-normal-saline","Lactated Ringer's & Normal Saline","IV fluids · base of every drip",
  "Every drip starts with 1 liter of sterile IV fluid. Normal saline is a salt-and-water solution. Lactated Ringer's is a balanced electrolyte solution containing sodium, potassium, calcium and lactate. Both rehydrate you directly through the bloodstream, which is faster than drinking water when you're sick, nauseated or very dehydrated."),
 ("vitamin-c","Vitamin C","Antioxidant · immune support",
  "An essential vitamin and antioxidant that the body uses to support normal immune function and collagen production. It's a core ingredient in our Meyers, Travel Defense, Glow and Get Right drips, at standard, boosted or optimized doses depending on the drip."),
 ("glutathione","Glutathione","Antioxidant",
  "A naturally occurring antioxidant made of three amino acids. It plays a role in protecting cells from oxidative stress and is popular in wellness and beauty drips for its association with a brighter-looking complexion."),
 ("vitamin-b12","Vitamin B12","Energy",
  "A B vitamin the body needs to make red blood cells and support normal nerve function and energy metabolism. People low in B12 often feel tired. It's included in our Meyers and Get Right drips."),
 ("b-complex","B-Complex","Metabolism",
  "A group of B vitamins (such as B1, B2, B3, B5 and B6) that help your body turn food into energy. It's included in our Meyers and Get Right drips."),
 ("zinc","Zinc","Immune support",
  "An essential mineral involved in normal immune function and wound healing. It's commonly used during cold and flu season."),
 ("magnesium","Magnesium","Muscles · relaxation",
  "A mineral involved in hundreds of processes in the body, including muscle and nerve function. Many people associate it with relaxed muscles and easing tension."),
 ("vitamin-d","Vitamin D","Immune support",
  "A vitamin that supports immune function and bone health. It's an option in Travel Defense, or you can choose another basic add-in instead."),
 ("amino-blend","Amino Blend","Muscle recovery",
  "A blend of amino acids, the building blocks of protein, which your muscles use to repair and rebuild. It's a key part of the Recover drip."),
 ("l-carnitine","L-Carnitine","Muscle energy",
  "A nutrient that helps your body move fatty acids into cells to be used for energy. It's included in Recover for active clients."),
 ("taurine","Taurine","Muscle fatigue",
  "An amino acid found in muscle, heart and brain tissue that's often used to support exercise performance and reduce muscle fatigue."),
 ("biotin","Biotin","Hair · nails",
  "Vitamin B7, a B vitamin associated with healthy hair, skin and nails. It's included in the Glow drip."),
 ("nad-plus","NAD+","Add-on · $50",
  "Nicotinamide adenine dinucleotide, a coenzyme found in every cell that's involved in energy production. Clients add it for energy and focus. You can add NAD+ to any drip for $50."),
 ("toradol","Toradol (ketorolac)","Optional medication · pain",
  "A non-steroidal anti-inflammatory (NSAID) pain reliever. It's optional in Get Right and only given when appropriate after your nurse's assessment, because it isn't right for everyone (for example, some kidney, stomach or bleeding conditions)."),
 ("zofran","Zofran (ondansetron)","Optional medication · nausea",
  "An anti-nausea medication. It's optional and only given when appropriate after your nurse's assessment."),
 ("pepcid","Pepcid (famotidine)","Optional medication · stomach",
  "Reduces stomach acid to help calm an upset stomach. It's optional and only given when appropriate after your nurse's assessment."),
 ("benadryl","Benadryl (diphenhydramine)","Optional medication · allergy",
  "An antihistamine used to settle allergic reactions. It can cause drowsiness. It's optional and only given when appropriate after your nurse's assessment."),
]

# ---------------------------------------------------------------- content: service areas
AREAS = [
 dict(slug="jupiter-fl", city="Jupiter", county="Palm Beach County",
  intro="Jupiter is our home base, so it's where we can usually get to you fastest. Our nurses make house calls all over town, from neighborhoods off Indiantown Road and Donald Ross Road to homes along the Intracoastal and beachside condos.",
  local="<p>We see Jupiter clients for everything from flu and stomach bugs to post-workout recovery, boat-day dehydration and pre-event Glow drips. Because we're based here, same-day visits are often possible. Text us and we'll give you the soonest time.</p>",
  places="Homes, condos, offices, hotels and vacation rentals throughout Jupiter, including Abacoa, Jupiter Farms and the Jupiter Inlet area",
  near=["tequesta-fl","juno-beach-fl","palm-beach-gardens-fl"]),
 dict(slug="tequesta-fl", city="Tequesta", county="Palm Beach County",
  intro="Tequesta sits right next door to our Jupiter home base, so a licensed nurse can usually reach you quickly. We bring IV hydration and vitamin drips to homes, condos and offices across the village.",
  local="<p>Whether you're down with something and don't want to drive, recovering after a long day on the water, or getting a household of family visitors through flu season, we can treat everyone in one visit right at home.</p>",
  places="Homes, condos, offices and rentals throughout Tequesta and the surrounding Jupiter Island and Loxahatchee River area",
  near=["jupiter-fl","hobe-sound-fl","juno-beach-fl"]),
 dict(slug="juno-beach-fl", city="Juno Beach", county="Palm Beach County",
  intro="We bring mobile IV therapy to Juno Beach homes, oceanfront condos and vacation rentals. You don't have to give up a beach day to drive to a clinic.",
  local="<p>Juno Beach visitors often book Travel Defense on arrival or Recover after a long day in the sun. Residents call us when flu or a stomach bug hits the house. Your nurse sets up wherever you're comfortable, and the drip takes about 45 to 60 minutes.</p>",
  places="Homes, beachfront condos, hotels and short-term rentals throughout Juno Beach",
  near=["jupiter-fl","north-palm-beach-fl","palm-beach-gardens-fl"]),
 dict(slug="palm-beach-gardens-fl", city="Palm Beach Gardens", county="Palm Beach County",
  intro="We make house calls across Palm Beach Gardens with IV hydration and vitamin drips, delivered by a licensed nurse to your home, office or hotel.",
  local="<p>Gardens clients book us for busy-season burnout (Optimized Meyers), recovery after golf, tennis or training (Recover), and Glow before galas and events. Getting the IV at your office or home means no time lost in a waiting room.</p>",
  places="Homes, gated communities, offices, hotels and resorts throughout Palm Beach Gardens",
  near=["jupiter-fl","north-palm-beach-fl","juno-beach-fl"]),
 dict(slug="north-palm-beach-fl", city="North Palm Beach", county="Palm Beach County",
  intro="Mobile IV therapy in North Palm Beach, delivered. A licensed nurse brings IV hydration and vitamin drips to your home, condo, boat-side residence or office.",
  local="<p>North Palm Beach clients often call us when illness hits and the last thing they want is an urgent care waiting room. We can also treat the whole household in a single visit, so everyone gets care without anyone driving sick.</p>",
  places="Homes, condos, offices and rentals throughout North Palm Beach and Lost Tree area neighborhoods",
  near=["palm-beach-gardens-fl","juno-beach-fl","west-palm-beach-fl"]),
 dict(slug="hobe-sound-fl", city="Hobe Sound", county="Martin County",
  intro="We extend our house calls north into Hobe Sound on the Treasure Coast, bringing IV hydration and vitamin drips to your home, so you don't have to drive to Jupiter or Stuart when you're feeling awful.",
  local="<p>Hobe Sound is a short drive from our Jupiter base. Text us your address and preferred time, and we'll confirm the soonest visit we can offer.</p>",
  places="Homes, condos and rentals throughout Hobe Sound and nearby Jupiter Island",
  near=["tequesta-fl","stuart-fl","jupiter-fl"]),
 dict(slug="stuart-fl", city="Stuart", county="Martin County",
  intro="Optimized Performance & Wellness brings mobile IV therapy to Stuart and the Treasure Coast. A licensed nurse comes to your home, office or hotel with IV hydration and vitamin drips.",
  local="<p>Stuart is at the northern edge of our regular service area. Text us your address and we'll confirm availability and the soonest time we can be there. Scheduling a bit ahead is the best way to lock in the time you want.</p>",
  places="Homes, condos, offices, hotels and rentals in Stuart and nearby Treasure Coast communities",
  near=["hobe-sound-fl","tequesta-fl","jupiter-fl"]),
 dict(slug="west-palm-beach-fl", city="West Palm Beach", county="Palm Beach County",
  intro="We bring mobile IV therapy to West Palm Beach homes, offices and hotels. A licensed nurse delivers IV hydration and vitamin drips wherever you are.",
  local="<p>West Palm Beach is the southern end of our regular service area. Business travelers and visitors often book Travel Defense or Get Right at their hotel, and residents book us when they're too sick to sit in a waiting room. Text your address and we'll confirm the soonest time.</p>",
  places="Homes, condos, offices and hotels across West Palm Beach",
  near=["north-palm-beach-fl","palm-beach-gardens-fl","juno-beach-fl"]),
]
AREA = {a["slug"]: a for a in AREAS}

# ---------------------------------------------------------------- content: FAQ
FAQ = [
 ("About IV therapy", [
  ("What is mobile IV therapy?","Mobile IV therapy means a licensed nurse comes to your home, office or hotel and gives you IV fluids, vitamins and, when appropriate, medications through a small IV in your arm. You get the same kind of IV hydration you'd get in a clinic without driving anywhere or sitting in a waiting room."),
  ("Does an IV actually help when I'm sick?","When you're sick it's easy to get dehydrated, especially with fever, vomiting or not eating. IV fluids rehydrate you faster than sipping water, and many people feel noticeably better after. It supports your recovery, it doesn't cure the illness."),
  ("Is IV hydration better than drinking water?","For everyday hydration, drinking water is usually enough. IV fluids go directly into your bloodstream, so they're helpful when you're too nauseated to keep fluids down, significantly dehydrated or need to rehydrate quickly. <a href=\"/guides/iv-hydration-vs-drinking-water/\">Read our full comparison</a>."),
  ("What's in an IV drip?","Every drip starts with 1 liter of Lactated Ringer's or normal saline. We then add vitamins, minerals, antioxidants or amino acids depending on the drip, such as vitamin C, glutathione, B12, zinc or magnesium. See every ingredient in our <a href=\"/ingredients/\">ingredient guide</a>."),
 ]),
 ("Booking + visits", [
  ("How do I book?",f"Text us at {PHONE1} or {PHONE2} with the drip you want (or how you're feeling) and your address. A real person replies and locks in the soonest time."),
  ("How long does a drip take?","About 45 to 60 minutes from setup to finish."),
  ("Where do you go?","Homes, offices, hotels and rentals across northern Palm Beach County and the Treasure Coast: Jupiter, Tequesta, Juno Beach, Palm Beach Gardens, North Palm Beach, Hobe Sound, Stuart and West Palm Beach. Don't see your town? Text us, we'll likely still come."),
  ("Can you treat the whole family?","Yes, we treat ages 10 and older. Let us know how many people when you text so your nurse brings enough for everyone."),
  ("Does it hurt?","Just a quick pinch when the IV goes in. After that most people barely notice it."),
  ("What should I do before my nurse arrives?","Drink some water if you can, have a comfortable place to sit or lie down, and have a list of your medications and allergies handy. Wear a top with sleeves that roll up easily."),
 ]),
 ("Safety + who we are", [
  ("Who gives the IV?","Every IV is overseen by Barry, our licensed registered nurse. Every visit starts with a health screening to make sure your drip is safe and right for you."),
  ("Who oversees your treatments?","Our licensed nurses are overseen by a medical director. Telehealth visits with our primary care provider are also available to schedule for a fee."),
  ("Is IV therapy safe?","IV therapy is generally well tolerated when it's given by a licensed professional after a health screening. Your nurse reviews your health history, medications and allergies before every drip and won't proceed if an IV isn't right for you. <a href=\"/safety/\">Read about our safety process</a>."),
  ("Are the Get Right meds required?","No. They're optional and only given when appropriate after your nurse's assessment."),
  ("When should I go to a doctor or ER instead?","IV hydration isn't emergency care. For trouble breathing, chest pain, confusion, a fever that won't come down, or severe dehydration in a child, call your doctor or 911."),
 ]),
 ("Pricing", [
  ("How much does mobile IV therapy cost?","Our drips range from $150 (Your Call, build your own) to $435 (Get Right). NAD+ can be added to any drip for $50. Prices are subject to change due to market fluctuations. <a href=\"/guides/mobile-iv-therapy-cost/\">See the full price breakdown</a>."),
  ("Do you take insurance?","Text or email us your question about payment and we'll let you know what's available."),
 ]),
]

# ---------------------------------------------------------------- content: guides
GUIDES = [
 dict(slug="mobile-iv-therapy-cost", title="How Much Does Mobile IV Therapy Cost in Palm Beach County?", short="Every drip on our menu, what's in it, and what affects the price.",
  answer="At Optimized Performance & Wellness, mobile IV therapy costs $150 to $435 per drip, delivered to your home by a licensed nurse. Your Call (build your own) starts at $150, most vitamin drips are $235 to $350, Get Right is $435, and NAD+ can be added to any drip for $50.",
  desc="Mobile IV therapy in Jupiter and Palm Beach County costs $150 to $435 per drip. See every drip's price, what's included, and what affects the cost.",
  body="""<h2>Price list</h2>
<div class="tscroll"><table class="tbl"><thead><tr><th>Drip</th><th>Price</th><th>Best for</th></tr></thead><tbody>
{rows}
</tbody></table></div>
<p class="fine" style="margin-top:12px">Add NAD+ to any drip for $50. Prices subject to change due to market fluctuations.</p>
<h2>What's included in the price</h2>
<ul><li><b>A licensed nurse who comes to you</b> at your home, office, hotel or rental</li><li><b>A health screening</b> before every single drip</li><li><b>1 liter of IV fluids</b> (Lactated Ringer's or normal saline) in every bag</li><li><b>The vitamins, minerals and nutrients</b> listed for your drip</li><li><b>Setup and cleanup.</b> You stay on the couch for 45 to 60 minutes.</li></ul>
<h2>What changes the cost</h2>
<p><b>The drip you choose.</b> Drips with boosted or optimized doses of ingredients like vitamin C and glutathione cost more than our everyday drips.</p>
<p><b>Add-ins.</b> NAD+ is a $50 add-on to any drip. Your Call includes three add-ins of your choice, and many other options are available.</p>
<p><b>Optional medications.</b> In the Get Right drip, medications for pain, nausea, upset stomach or allergic reactions are available when appropriate after your nurse's assessment.</p>
<h2>Is mobile IV therapy worth it compared to a clinic?</h2>
<p>With mobile IV therapy you don't drive while you're sick, sit in a room with other sick people, or wait your turn. You can also treat the whole household in one visit. For many people, that convenience is the main reason they choose an at-home IV.</p>
<h2>How to book</h2>
<p>Text <a href="sms:+15615030046">{p1}</a> with the drip you want and your address. A real person replies and books the soonest time.</p>"""),
 dict(slug="what-to-expect-at-home-iv", title="What to Expect at Your First At-Home IV Therapy Visit", short="From the first text to the last drop, step by step.",
  answer="An at-home IV visit takes about 45 to 60 minutes. You text to book, a licensed nurse arrives and does a quick health screening, places a small IV in your arm, and you relax while the 1-liter drip runs. The nurse then removes the IV and cleans everything up.",
  desc="What happens during an at-home IV therapy visit in Jupiter and Palm Beach County: booking, health screening, how long it takes, and how to prepare.",
  body="""<h2>1. Book by text</h2>
<p>Text <a href="sms:+15615030046">{p1}</a> or <a href="sms:+15613126570">{p2}</a> with the drip you want (or just how you're feeling), how many people, and your address. A real person replies and locks in the soonest time.</p>
<h2>2. Get ready</h2>
<ul><li>Drink some water if you can. Hydrated veins are easier to find.</li><li>Pick a comfortable spot like the couch, bed or a recliner.</li><li>Have a list of your medications and allergies handy.</li><li>Wear a top with sleeves that roll up easily.</li></ul>
<h2>3. Your nurse arrives and screens you</h2>
<p>A licensed nurse asks about your symptoms, health history, medications and allergies, and checks your vital signs. The screening makes sure the drip is safe and right for you. If something doesn't look right, your nurse will tell you, and may recommend you see a doctor instead.</p>
<h2>4. The IV goes in</h2>
<p>You'll feel a quick pinch as a small, flexible catheter is placed in a vein in your arm or hand. After that, most people barely notice it.</p>
<h2>5. Relax for 45 to 60 minutes</h2>
<p>Watch TV, work on your laptop or nap. The drip runs while your nurse monitors how you're doing. If several people are getting drips, everyone can be treated at the same time.</p>
<h2>6. Wrap-up</h2>
<p>Your nurse removes the IV, applies a small bandage and takes everything with them. You get back to your day.</p>
<h2>How will I feel after?</h2>
<p>Many people say they feel noticeably better after rehydrating, especially when they've been sick. It's normal to need to use the bathroom more for a few hours afterward. Contact your doctor if you have redness, swelling or pain at the IV site that gets worse."""),
 dict(slug="iv-therapy-when-sick", title="IV Therapy for Flu, Colds and Stomach Bugs: When It Helps", short="How IV fluids help when you're sick, and when to see a doctor instead.",
  answer="IV therapy can help when you're sick by rehydrating you faster than drinking, which matters most with fever, vomiting, diarrhea or not eating. It supports recovery but doesn't cure illness. For trouble breathing, chest pain, confusion, a fever that won't come down or a severely dehydrated child, call your doctor or 911.",
  desc="Can IV therapy help with the flu, a cold or a stomach bug? How IV fluids support recovery at home, which drip to choose, and when to see a doctor instead.",
  body="""<h2>Why being sick dehydrates you</h2>
<p>Fever makes you lose more fluid through sweat and breathing. Vomiting and diarrhea pull fluid and electrolytes out fast. And when you feel awful, you usually don't eat or drink much. Dehydration can make headaches, fatigue and dizziness worse.</p>
<h2>How IV fluids help</h2>
<p>IV fluids go straight into your bloodstream, so they don't depend on your stomach. That's why they're useful when you can't keep anything down. Many people feel noticeably better after rehydrating. To be clear: an IV supports your recovery, it doesn't cure the flu, a cold or a stomach bug.</p>
<h2>Which drip to choose</h2>
<ul>
<li><b>Flu, aches + chills:</b> we'll individualize it. Often IV fluids plus the right medication for aches or fever is all it takes. For the worst days, <a href="/iv-menu/get-right/">Get Right</a> is our everything bag.</li>
<li><b>Stomach bug or nausea:</b> IV fluids with anti-nausea medication, when appropriate, are often enough to rehydrate you. Your nurse tailors it to you.</li>
<li><b>Cold or sniffles:</b> <a href="/iv-menu/foundational-meyers/">Foundational Meyers</a>, with vitamin C, glutathione, B12 and zinc.</li>
<li><b>Over the worst but still wiped out:</b> <a href="/iv-menu/recover/">Recover</a>.</li>
</ul>
<h2>Why at home is easier when you're sick</h2>
<p>You don't have to drive while you feel awful, sit in a waiting room full of other sick people, or bring sick kids out. We can also treat everyone in the household who's 10 or older in one visit.</p>
<h2>When to see a doctor or call 911 instead</h2>
<div class="warn">{alert}<div><b>IV hydration isn't emergency care.</b> For trouble breathing, chest pain, confusion, a fever that won't come down, or severe dehydration in a child, call your doctor or 911.</div></div>"""),
 dict(slug="iv-hydration-vs-drinking-water", title="IV Hydration vs. Drinking Water: What's the Difference?", short="When drinking is enough, and when an IV makes sense.",
  answer="Drinking water is enough for everyday hydration. IV hydration delivers fluid and electrolytes directly into your bloodstream, bypassing the stomach, so it works faster and helps when you're nauseated, vomiting, significantly dehydrated or need to recover quickly. An IV also lets you add vitamins and medications when appropriate.",
  desc="IV hydration vs. drinking water: how each works, how fast they rehydrate, and when an at-home IV makes sense. From the nurses at Optimized Performance & Wellness.",
  body="""<h2>The short version</h2>
<div class="tscroll"><table class="tbl"><thead><tr><th></th><th>Drinking water</th><th class="us">IV hydration</th></tr></thead><tbody>
<tr><td>How it's absorbed</td><td>Through your digestive system</td><td class="us">Directly into the bloodstream</td></tr>
<tr><td>Works if you're nauseated or vomiting</td><td>Often not</td><td class="us">Yes</td></tr>
<tr><td>Speed</td><td>Gradual</td><td class="us">About 45 to 60 minutes for 1 liter</td></tr>
<tr><td>Can include vitamins + meds</td><td>No</td><td class="us">Yes, when appropriate</td></tr>
<tr><td>Best for</td><td>Everyday hydration</td><td class="us">Illness, heavy sweating, recovery, travel</td></tr>
</tbody></table></div>
<h2>When drinking water is enough</h2>
<p>For most healthy people on a normal day, drinking water and eating normally keeps you well hydrated. You don't need an IV to stay hydrated day to day.</p>
<h2>When IV hydration makes sense</h2>
<ul><li>You're sick and can't keep fluids down</li><li>You've lost a lot of fluid from fever, vomiting, diarrhea or heavy sweating</li><li>You're recovering from a race, tournament or long day in the South Florida heat</li><li>You want to rehydrate before or after travel</li><li>You want vitamins like vitamin C, B12 or glutathione delivered with your fluids</li></ul>
<h2>What's in our IV fluids</h2>
<p>Every drip starts with 1 liter of <a href="/ingredients/#lactated-ringers-normal-saline">Lactated Ringer's or normal saline</a>. These are sterile solutions with electrolytes that closely match your body's own fluids. See our <a href="/ingredients/">ingredient guide</a> for everything else we add."""),
]

# ---------------------------------------------------------------- templating
NAV_DRIPS = "".join(f'<a href="/iv-menu/{d["slug"]}/">{e(d["name"])} <span>${d["price"]}</span></a>' for d in DRIPS)
NAV_AREAS = "".join(f'<a href="/service-areas/{a["slug"]}/">{e(a["city"])}, FL</a>' for a in AREAS)

def header(cur):
    def cu(p): return ' aria-current="page"' if cur == p else ''
    return f'''<a class="skip" href="#main">Skip to content</a>
<div class="topbar"><div class="w"><span class="tb-l">Mobile IV therapy in Jupiter, Palm Beach County + the Treasure Coast</span><span class="tb-r"><a href="tel:{PHONE1_T}">{ic("phone",14).replace('<svg','<svg style="display:inline;vertical-align:-2px;margin-right:6px"')}{PHONE1}</a></span></div></div>
<nav id="nav" aria-label="Main"><div class="w nv">
  <a href="/" class="logo" aria-label="{e(NAME)} home"><img src="/assets/logo-mark.png" width="40" height="44" alt=""><span><b>OPTIMIZED</b><small>PERFORMANCE &amp; WELLNESS</small></span></a>
  <div class="nl" id="nl">
    <div class="dd"><button type="button" aria-expanded="false">IV Menu</button><div class="ddm">{NAV_DRIPS}<a class="all" href="/iv-menu/">See the full IV menu →</a></div></div>
    <a href="/how-it-works/"{cu("how-it-works/")}>How it works</a>
    <div class="dd"><button type="button" aria-expanded="false">Service areas</button><div class="ddm">{NAV_AREAS}<a class="all" href="/service-areas/">All service areas →</a></div></div>
    <a href="/about/"{cu("about/")}>About</a>
    <a href="/guides/"{cu("guides/")}>Guides</a>
    <a href="/faq/"{cu("faq/")}>FAQ</a>
    <a href="{sms("Hi! I'd like to book an IV.")}" class="btn btn-p">{ic("chat",18)}Text to book</a>
  </div>
  <button class="mb" id="mb" aria-label="Open menu" aria-expanded="false" aria-controls="nl"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M4 8h16M4 16h16"/></svg></button>
</div></nav>'''

def footer():
    drips = "".join(f'<li><a href="/iv-menu/{d["slug"]}/">{e(d["name"])}</a></li>' for d in DRIPS)
    areas = "".join(f'<li><a href="/service-areas/{a["slug"]}/">{e(a["city"])}</a></li>' for a in AREAS)
    return f'''<footer><div class="w">
<div class="ft">
  <div><a href="/" aria-label="{e(NAME)} home"><img src="/assets/logo-white.png" width="220" height="64" alt="{e(NAME)}"></a>
  <p>Mobile IV therapy at home. A licensed nurse brings IV hydration and vitamin drips to your home, office or hotel in Jupiter, Palm Beach County and the Treasure Coast.</p>
  <p><a href="tel:{PHONE1_T}">{PHONE1}</a><br><a href="tel:{PHONE2_T}">{PHONE2}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a><br><a href="{IG}" rel="noopener">Instagram</a></p></div>
  <div><h4>IV Menu</h4><ul>{drips}<li><a href="/iv-menu/">Full menu + prices</a></li></ul></div>
  <div><h4>Service areas</h4><ul>{areas}</ul></div>
  <div><h4>Learn</h4><ul><li><a href="/how-it-works/">How it works</a></li><li><a href="/ingredients/">Ingredient guide</a></li><li><a href="/group-iv-therapy/">Group + event IVs</a></li><li><a href="/safety/">Safety + screening</a></li><li><a href="/guides/">Guides</a></li><li><a href="/about/">About us</a></li><li><a href="/faq/">FAQ</a></li><li><a href="/contact/">Contact + booking</a></li></ul></div>
</div>
<div class="fb">© 2026 {e(NAME)}. IV therapy is not intended to diagnose, treat, cure or prevent any disease and is not a substitute for care from your doctor. All treatments require a health screening. Prices subject to change. In an emergency, call 911.</div>
</div></footer>
<div class="mbar"><a class="btn btn-p" href="{sms("Hi! I'd like to book an IV.")}">{ic("chat",18)}Text us</a><a class="btn btn-o" href="tel:{PHONE1_T}">{ic("phone",18)}Call</a></div>'''

BIZ_ID = BASE + "/#business"
def business():
    return {
     "@type": ["MedicalBusiness", "HealthAndBeautyBusiness"], "@id": BIZ_ID, "name": NAME, "alternateName": "Optimized IV",
     "description": "Mobile IV therapy. A licensed nurse brings IV hydration and vitamin drips to your home, office or hotel in Jupiter, Palm Beach County and the Treasure Coast.",
     "url": BASE + "/", "telephone": ["+1-561-503-0046", "+1-561-312-6570"], "email": EMAIL,
     "image": BASE + "/og-image.jpg", "logo": BASE + "/assets/logo-mark.png", "priceRange": "$150-$435",
     "currenciesAccepted": "USD",
     "address": {"@type": "PostalAddress", "addressLocality": "Jupiter", "addressRegion": "FL", "addressCountry": "US"},
     "areaServed": [{"@type": "City", "name": f'{a["city"]}, FL', "url": f'{BASE}/service-areas/{a["slug"]}/'} for a in AREAS],
     "sameAs": [IG],
     "medicalSpecialty": "Nursing",
     "knowsAbout": ["IV therapy", "IV hydration", "Vitamin infusion", "Myers' cocktail", "NAD+ IV", "Glutathione IV"],
     "hasOfferCatalog": {"@id": BASE + "/iv-menu/#catalog"},
    }

def crumbs_html(cr):
    items = "".join((f'<li><a href="{p}">{e(n)}</a></li>' if i < len(cr)-1 else f'<li aria-current="page">{e(n)}</li>') for i,(n,p) in enumerate(cr))
    return f'<nav class="crumbs" aria-label="Breadcrumb"><ol>{items}</ol></nav>'

def crumbs_ld(cr):
    return {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": i+1, "name": n, "item": BASE + p} for i,(n,p) in enumerate(cr)]}

def faq_html(faqs):
    return '<div class="faq">' + "".join(f'<details><summary>{e(q)}</summary><div class="fa"><p>{a}</p></div></details>' for q,a in faqs) + '</div>'

def faq_ld(faqs, url):
    import re
    return {"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}} for q,a in faqs]}

def answer(text, label="Quick answer"):
    return f'<div class="answer"><span class="al">{label}</span><p>{text}</p></div>'

def cta(title="Feel better. Don't get up.", text="Text us how you're feeling and where you are. We'll handle the rest."):
    return f'''<section class="sec tight"><div class="w"><div class="cta rv">
<div><h2>{title}</h2><p>{text}</p><p class="ctainfo"><a href="tel:{PHONE1_T}">{PHONE1}</a> · <a href="tel:{PHONE2_T}">{PHONE2}</a> · <a href="mailto:{EMAIL}">{EMAIL}</a></p></div>
<div class="btns"><a class="btn btn-w" href="{sms("Hi! I'd like to book an IV.")}">{ic("chat",18)}Text us</a><a class="btn btn-g" href="tel:{PHONE1_T}">{ic("phone",18)}Call us</a></div>
</div></div></section>'''

def drip_card(d, h="h3"):
    ings = "".join(f'<li>{e(n.split(",")[0])}</li>' for (n,_),_b in d["ings"][1:6])
    if len(d["ings"]) > 6: ings += f'<li>+{len(d["ings"])-6} more</li>'
    pop = '<span class="pop">Most popular</span>' if d["popular"] else ''
    return f'''<article class="card rv" data-c="{d["goals"]}">{pop}
<div class="top"><span class="tg">{e(d["tag"])}</span><span class="price">${d["price"]}</span></div>
<{h}><a href="/iv-menu/{d["slug"]}/">{e(d["name"])}</a></{h}>
<p>{e(d["short"])}</p>
<ul class="ing" aria-label="Key ingredients">{ings}</ul>
<div class="cf"><span class="tlink">Details</span><a class="btn btn-p btn-sm" href="{sms(f"Hi! I'd like to book {d['name']}.")}">Book</a></div>
</article>'''

def aside_book(extra=""):
    drips = "".join(f'<li><a href="/iv-menu/{d["slug"]}/">{e(d["name"])} <span>${d["price"]}</span></a></li>' for d in DRIPS)
    return f'''<aside class="aside">
<div class="box dark"><h3>Book by text</h3><p style="font-size:15.5px">A real person replies fast. Send your drip and address.</p>
<a class="btn btn-w" href="{sms("Hi! I'd like to book an IV.")}">{ic("chat",18)}Text {PHONE1}</a>
<a class="btn btn-g" href="tel:{PHONE1_T}">{ic("phone",18)}Call</a></div>
{extra}
<div class="box"><h3>IV menu</h3><ul>{drips}</ul></div>
</aside>'''

PAGES = []
def page(path, title, desc, body, ld=None, cr=None, cur=None, og_type="website", noindex=False):
    url = BASE + "/" + path
    graph = [business(), {"@type": "WebSite", "@id": BASE + "/#website", "url": BASE + "/", "name": NAME, "publisher": {"@id": BIZ_ID}},
             {"@type": "WebPage", "@id": url + "#webpage", "url": url, "name": title, "description": desc, "isPartOf": {"@id": BASE + "/#website"},
              "about": {"@id": BIZ_ID}, "dateModified": UPDATED, "inLanguage": "en-US"}]
    if cr: graph.append(crumbs_ld(cr))
    graph += (ld or [])
    if NAME in title or len(title) + 35 > 66:
        full_title = title if (NAME in title or len(title) + 15 > 70) else f"{title} | Optimized IV"
    else:
        full_title = f"{title} | {NAME}"
    doc = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(full_title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="canonical" href="{url}">
{'<meta name="robots" content="noindex">' if noindex else '<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1">'}
<meta name="theme-color" content="#0C2340">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{e(NAME)}">
<meta property="og:title" content="{e(full_title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/og-image.jpg">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{e(NAME)} mobile IV therapy">
<meta property="og:locale" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="geo.region" content="US-FL"><meta name="geo.placename" content="Jupiter">
<link rel="icon" href="/favicon-32.png" sizes="32x32"><link rel="icon" href="/favicon.png" sizes="512x512">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500..800&family=Figtree:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="/assets/site.css">
<script>document.documentElement.classList.add('js')</script>
<script type="application/ld+json">{json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False)}</script>
</head>
<body>
{header(cur)}
<main id="main">
{body}
</main>
{footer()}
<script src="/assets/site.js" defer></script>
</body>
</html>
'''
    out = os.path.join(ROOT, path, "index.html") if not path.endswith(".html") else os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    open(out, "w").write(doc)
    if not noindex: PAGES.append(path)

def phero(cr, h1, lead, extra="", side=""):
    inner = f'{crumbs_html(cr)}<h1>{h1}</h1><p class="lead">{lead}</p>{extra}'
    if side:
        return f'<header class="phero"><div class="w phero-g"><div>{inner}</div>{side}</div></header>'
    return f'<header class="phero"><div class="w">{inner}</div></header>'

BOOK_BTNS = f'<div class="btns"><a class="btn btn-p" href="{sms("Hi! I would like to book an IV.")}">{ic("chat",18)}Text {PHONE1}</a><a class="btn btn-o" href="/iv-menu/">See the IV menu</a></div>'

# ================================================================ HOME
def build_home():
    finder_opts = [
     ("Flu, aches + chills", None, "We individualize your treatment to your symptoms. Often IV saline plus the right medication for aches, fever or nausea is all it takes to help you start feeling better. No package needed.", "flu, aches + chills"),
     ("Stomach bug or nausea", None, "When nothing is staying down, IV saline with anti-nausea medication is often all it takes to rehydrate you and help improve your day. Your nurse tailors it to you.", "a stomach bug or nausea"),
     ("Cold or sniffles", "foundational-meyers", "Vitamin C, glutathione, B12 and zinc with hydration for colds, sniffles and that run-down feeling.", None),
     ("Wiped out, still recovering", "recover", "Fluids, amino acids, L-carnitine and taurine to rehydrate and help your muscles bounce back when you're still dragging.", None),
     ("About to travel", "travel-defense", "Vitamin C, glutathione, zinc and vitamin D before or after a trip so you stay a step ahead.", None),
     ("Want my glow back", "glow", "Boosted glutathione and vitamin C plus biotin to help bring back that bright, rested look.", None),
     ("Migraine or headache", None, "IV saline with medication for pain and nausea is often enough to help take the edge off. Your nurse tailors treatment to your symptoms, no package needed.", "a migraine or headache"),
    ]
    btns = ""
    for i,(lbl,slug,desc,sym) in enumerate(finder_opts):
        if slug:
            d = DRIP[slug]; a = f'data-name="{e(d["name"])}" data-price="${d["price"]}" data-url="/iv-menu/{slug}/" data-sms="{e(sms("Hi! I would like to book " + d["name"] + "."))}"'
        else:
            a = f'data-name="Treatment tailored to you" data-sms="{e(sms("Hi! I am dealing with " + sym + "."))}"'
        btns += f'<button type="button" class="sym" aria-pressed="{"true" if i==0 else "false"}" {a} data-desc="{e(desc)}">{e(lbl)}</button>'
    first = finder_opts[0]
    home_faqs = [q for cat in FAQ for q in cat[1]][:0] + [FAQ[0][1][1], FAQ[1][1][1], FAQ[1][1][3], FAQ[2][1][0], FAQ[1][1][4], FAQ[3][1][0]]
    areas = "".join(f'<a href="/service-areas/{a["slug"]}/">{e(a["city"])}</a>' for a in AREAS)
    guides = "".join(f'<a class="acard rv" href="/guides/{g["slug"]}/"><div class="art"></div><div class="ab"><span class="tg">Guide</span><h3>{e(g["title"])}</h3><p>{e(g["short"])}</p></div></a>' for g in GUIDES[:3])
    body = f'''
<header class="hero"><div class="w hero-g">
 <div>
  <span class="badge"><span class="live"></span>Now booking home visits in Jupiter + Palm Beach County</span>
  <h1>Mobile IV therapy,<br><span class="wv">delivered.<svg viewBox="0 0 300 20" preserveAspectRatio="none" aria-hidden="true"><path d="M4 12c40-10 80 6 120-2s80-8 120 0 40 4 52 2" fill="none" stroke="#E2493B" stroke-width="5" stroke-linecap="round"/></svg></span></h1>
  <p class="lead">Stay home. <b>A licensed nurse comes to you</b> in Jupiter, Palm Beach County and the Treasure Coast with IV hydration and vitamin drips for flu, recovery and feeling like yourself again.</p>
  <div class="btns"><a class="btn btn-p" href="{sms("Hi! I would like to book an IV.")}">{ic("chat",18)}Text {PHONE1}</a><a class="btn btn-o" href="/iv-menu/">See the IV menu</a></div>
  <div class="stats"><div><b>$150+</b><span>drips start at</span></div><div><b>45-60</b><span>minutes, start to finish</span></div><div><b>RN</b><span>every single visit</span></div></div>
 </div>
 <div class="hcard rv">
  <img class="mk" src="/assets/logo-mark.png" width="64" height="71" alt="">
  <h2>What every visit includes</h2>
  <p>No waiting room. No driving sick.</p>
  <ul class="chk"><li><span><b>A licensed RN comes to you</b>: home, office, hotel or rental</span></li><li><span><b>A health screening</b> before every single drip</span></li><li><span><b>1 liter of IV fluids</b> plus the vitamins in your drip</span></li><li><span><b>Overseen by a medical director</b>, with optional telehealth</span></li><li><span><b>Whole household</b> treated in one visit (ages 10+)</span></li></ul>
  <div class="btns"><a class="btn btn-p" href="{sms("Hi! I would like to book an IV.")}">{ic("chat",18)}Text to book</a></div>
 </div>
</div></header>

<section class="trust" aria-label="Why choose us"><div class="w">
 <div>{'<span class="ic">'+ic("nurse")+'</span>'}<p style="margin:0"><b>Licensed nurses</b><span>Overseen by a medical director</span></p></div>
 <div>{'<span class="ic">'+ic("home")+'</span>'}<p style="margin:0"><b>We come to you</b><span>Home, office or hotel</span></p></div>
 <div>{'<span class="ic">'+ic("shield")+'</span>'}<p style="margin:0"><b>Health screen first</b><span>Before every single drip</span></p></div>
 <div>{'<span class="ic">'+ic("chat")+'</span>'}<p style="margin:0"><b>Book by text</b><span>Real person, fast reply</span></p></div>
</div></section>

<section class="sec" id="what"><div class="w g2">
 <div><span class="kick">What is mobile IV therapy?</span><h2>The IV comes to <em class="hl">your couch</em>.</h2></div>
 <div>{answer("Mobile IV therapy is IV hydration and vitamin infusions given by a licensed nurse at your home, office or hotel. Optimized Performance &amp; Wellness serves Jupiter, Palm Beach County and the Treasure Coast. Each visit starts with a health screening, uses 1 liter of IV fluids plus vitamins chosen for your goal, and takes 45 to 60 minutes. Drips start at $150.")}
 <p>Feeling awful is hard enough. Instead of driving to a clinic and waiting with other sick people, you text us, a nurse arrives, and you rest while the drip does its work. Our healthcare team customizes every drip to you and your situation, so you feel your best today and can keep going after your goals.</p>
 <a class="tlink" href="/how-it-works/">See how it works</a></div>
</div></section>

<section class="sec bg-grad" id="menu"><div class="w">
 <div class="head"><span class="kick">The IV menu</span><h2>What's your wellness goal?</h2><p class="sub">Pick a goal to see the drips made for it. Every bag starts with 1 liter of IV fluids, then we add the good stuff.</p></div>
 <div class="goals" role="group" aria-label="Filter drips by goal"><button class="goal" data-f="all" aria-pressed="true">All drips</button><button class="goal" data-f="sick" aria-pressed="false">Feel better when I'm sick</button><button class="goal" data-f="recover" aria-pressed="false">Recover + recharge</button><button class="goal" data-f="well" aria-pressed="false">Stay well</button><button class="goal" data-f="glow" aria-pressed="false">Glow + anti-aging</button></div>
 <div class="cards">{"".join(drip_card(d) for d in DRIPS)}</div>
 <p class="fine" style="margin-top:24px">{NAD_NOTE} Prices subject to change due to market fluctuations. Optional medications are only given when appropriate after your nurse's assessment.</p>
</div></section>

<section class="sec" id="finder"><div class="w"><div class="fbox rv">
 <div class="fl"><span class="kick">Not sure?</span><h2>Tell us what's going on.</h2><p class="sub" style="font-size:17px">Tap what you're dealing with and we'll point you to a drip.</p>
 <div class="syms" role="group" aria-label="What are you dealing with?">{btns}</div>
 <p class="fine">Just a starting point. Your nurse confirms the right drip at your visit. Every IV is given by a licensed RN with 5 years of ER experience, and your visit can be upgraded to a telehealth call with our primary care provider.</p></div>
 <div class="fr" aria-live="polite"><span class="k" id="fK">We'll individualize it</span><h3 id="fN">Treatment tailored to you</h3><span class="pp" id="fP" hidden></span><p id="fD">{e(first[2])}</p>
 <div class="btns" style="position:relative;z-index:1"><a class="btn btn-w" id="fB" href="{sms("Hi! I am dealing with flu, aches + chills.")}">{ic("chat",18)}<span>Text us your symptoms</span></a><a class="btn btn-g" id="fL" href="#" hidden>Drip details</a></div></div>
</div></div></section>

<section class="sec bg-foam" id="how"><div class="w">
 <div class="head center"><span class="kick">How it works</span><h2>Three steps. Zero waiting rooms.</h2></div>
 <div class="steps">
  <div class="step rv"><div class="n"><b>1</b></div><h3>Text us</h3><p>Send <a href="sms:{PHONE1_T}">{PHONE1}</a> or <a href="sms:{PHONE2_T}">{PHONE2}</a> your drip and address. We'll lock in the soonest time.</p></div>
  <div class="step rv"><div class="n"><b>2</b></div><h3>Nurse arrives</h3><p>A licensed nurse does a quick health screening to make sure your drip is right for you.</p></div>
  <div class="step rv"><div class="n"><b>3</b></div><h3>Relax + refuel</h3><p>Stay on the couch for 45 to 60 minutes. We clean up, you get back to your life.</p></div>
 </div>
</div></section>

<section class="sec"><div class="w g2">
 <div><span class="kick">Why at home</span><h2>Skip the waiting room.</h2><p class="sub">Feeling awful is hard enough. Here's what changes when the IV comes to you.</p><a class="tlink" href="/group-iv-therapy/">Treating a group or event?</a></div>
 <div class="tscroll"><table class="tbl"><thead><tr><th></th><th>Clinic or urgent care</th><th class="us">Optimized at home</th></tr></thead><tbody>
 <tr><td>Drive there while you're sick</td><td>Yes</td><td class="us">Nope, we come to you</td></tr>
 <tr><td>Sit in a room full of other sick people</td><td>Usually</td><td class="us">Just you, on your couch</td></tr>
 <tr><td>Treat the whole household in one visit</td><td>One at a time</td><td class="us">Yes, everyone at once</td></tr>
 <tr><td>Book with a quick text</td><td>Call, hold, wait</td><td class="us">One quick text</td></tr>
 <tr><td>Licensed medical professional</td><td>Yes</td><td class="us">Yes, a licensed RN</td></tr>
 </tbody></table></div>
</div></section>

<section class="sec bg-foam" id="areas"><div class="w g2">
 <div><span class="kick">Service area</span><h2>We make house calls.</h2><p class="sub">Homes, offices, hotels and rentals across northern Palm Beach County and the Treasure Coast.</p><p>Don't see your town? <a href="{sms("Hi! Do you come to my area?")}">Text us</a>, we'll likely still come.</p></div>
 <div><div class="areas">{areas}</div><p style="margin-top:22px"><a class="tlink" href="/service-areas/">Explore service areas</a></p></div>
</div></section>

<section class="sec"><div class="w">
 <div class="head"><span class="kick">Guides</span><h2>Know before you drip.</h2></div>
 <div class="g3">{guides}</div>
 <p style="margin-top:24px"><a class="tlink" href="/guides/">All guides</a> &nbsp;·&nbsp; <a class="tlink" href="/ingredients/">Ingredient guide</a></p>
</div></section>

<section class="sec bg-grad" id="faq"><div class="w wn">
 <div class="head center"><span class="kick">FAQ</span><h2>Good questions.</h2><p class="sub">Still wondering? Text or call <a href="tel:{PHONE1_T}">{PHONE1}</a> or <a href="tel:{PHONE2_T}">{PHONE2}</a>, or email <a href="mailto:{EMAIL}">{EMAIL}</a>, and a real person, one of our RNs or healthcare professionals, will get back to you.</p></div>
 {faq_html(home_faqs)}
 <p class="center" style="margin-top:26px"><a class="tlink" href="/faq/">See all FAQs</a></p>
 <div class="warn" style="margin-top:28px">{ic("alert",24).replace('<svg','<svg class="ic"')}<div><b>When to call a doctor instead:</b> IV hydration isn't emergency care. For trouble breathing, chest pain, confusion, a fever that won't come down, or severe dehydration in a child, call your doctor or 911.</div></div>
</div></section>
{cta()}'''
    ld = [faq_ld(home_faqs, BASE + "/")]
    page("", "Mobile IV Therapy in Jupiter, FL | Optimized Performance & Wellness",
         f"Mobile IV therapy at home in Jupiter + Palm Beach County. A licensed nurse brings IV hydration and vitamin drips to you. From $150. Text {PHONE1}.",
         body, ld)

# ================================================================ IV MENU + DRIPS
def build_menu():
    cr = [("Home","/"),("IV Menu","/iv-menu/")]
    rows = "".join(f'<tr><td><a href="/iv-menu/{d["slug"]}/">{e(d["name"])}</a></td><td>${d["price"]}</td><td>{e(d["tag"])}</td><td>{len(d["ings"])-1} add-ins + 1L fluids</td></tr>' for d in DRIPS)
    body = phero(cr, "IV therapy menu + prices", "Seven drips, each starting with 1 liter of IV fluids, delivered to your home by a licensed nurse. We customize every drip to you and your situation.", BOOK_BTNS) + f'''
<section class="sec"><div class="w">
 {answer(f"Our mobile IV drips cost $150 to $435: Your Call $150, Recover $235, Foundational Meyers $245, Travel Defense $250, Glow $300, Optimized Meyers $350 and Get Right $435. Add NAD+ to any drip for $50. Every drip includes 1 liter of IV fluids, a health screening and a licensed nurse visit at your home, office or hotel.", "Prices at a glance")}
 <div class="goals" role="group" aria-label="Filter drips by goal"><button class="goal" data-f="all" aria-pressed="true">All drips</button><button class="goal" data-f="sick" aria-pressed="false">Feel better when I'm sick</button><button class="goal" data-f="recover" aria-pressed="false">Recover + recharge</button><button class="goal" data-f="well" aria-pressed="false">Stay well</button><button class="goal" data-f="glow" aria-pressed="false">Glow + anti-aging</button></div>
 <div class="cards">{"".join(drip_card(d,"h2") for d in DRIPS)}</div>
 <p class="fine" style="margin-top:24px">{NAD_NOTE} Prices subject to change due to market fluctuations. Optional medications are only given when appropriate after your nurse's assessment.</p>
</div></section>
<section class="sec bg-foam"><div class="w">
 <div class="head"><span class="kick">Compare</span><h2>All drips side by side</h2></div>
 <div class="tscroll"><table class="tbl"><thead><tr><th>Drip</th><th>Price</th><th>Made for</th><th>What's in it</th></tr></thead><tbody>{rows}</tbody></table></div>
 <div class="note" style="margin-top:24px"><b>Our approach:</b> Our experienced healthcare team works with you to help you reach your best. Every drip on this menu is a starting point. We customize it to you and your situation, to optimize how you feel today so you can meet your goals and be your best self. See every ingredient in our <a href="/ingredients/">ingredient guide</a>.</div>
</div></section>
{cta("Not sure which drip?","Text us how you're feeling. Your nurse will help you pick, and confirm it at your visit.")}'''
    catalog = {"@type": "OfferCatalog", "@id": BASE + "/iv-menu/#catalog", "name": "IV therapy menu", "itemListElement": [
        {"@type": "Offer", "price": str(d["price"]), "priceCurrency": "USD", "url": f'{BASE}/iv-menu/{d["slug"]}/',
         "itemOffered": {"@type": "Service", "@id": f'{BASE}/iv-menu/{d["slug"]}/#service', "name": f'{d["name"]} IV drip'}} for d in DRIPS]}
    page("iv-menu/", "IV Therapy Menu + Prices ($150–$435)",
         "Mobile IV therapy menu and prices: Your Call $150, Recover $235, Foundational Meyers $245, Travel Defense $250, Glow $300, Optimized Meyers $350, Get Right $435.",
         body, [catalog], cr)

    for d in DRIPS:
        cr = [("Home","/"),("IV Menu","/iv-menu/"),(d["name"], f'/iv-menu/{d["slug"]}/')]
        ings = "".join(f'<li><a href="/ingredients/#{s}">{e(n)}</a><span>{e(b)}</span></li>' for (n,s),b in d["ings"])
        meds = ""
        if d.get("meds"):
            meds = '<h3>Optional medications, when appropriate</h3><ul class="drip-ing">' + "".join(f'<li><a href="/ingredients/#{s}">{e(n)}</a><span>{e(b)}</span></li>' for n,s,b in d["meds"]) + '</ul><p class="fine" style="margin-top:10px">Optional medications are only given when appropriate after your nurse\'s assessment.</p>'
        best = "".join(f"<li>{e(b)}</li>" for b in d["best"])
        others = [x for x in DRIPS if x["slug"] != d["slug"]][:3]
        side = f'''<div class="pricebox"><div class="pr">${d["price"]}<small>per drip</small></div>
<ul class="chk"><li>1 liter of IV fluids + {len(d["ings"])-1} add-ins</li><li>Licensed nurse at your door</li><li>45 to 60 minutes</li><li>Health screening included</li></ul>
<a class="btn btn-p" href="{sms(f"Hi! I'd like to book {d['name']}.")}">{ic("chat",18)}Book {e(d["name"])}</a><a class="btn btn-o" href="tel:{PHONE1_T}">{ic("phone",18)}Call {PHONE1}</a>
<p class="fine" style="margin:12px 0 0">+ Add NAD+ for $50</p></div>'''
        ans = f'{e(d["name"])} is a ${d["price"]} mobile IV drip from {e(NAME)}, given at your home, office or hotel in Jupiter and Palm Beach County by a licensed nurse. It includes 1 liter of IV fluids plus ' + ", ".join(e(n.split(",")[0]) for (n,_),_b in d["ings"][1:]) + f'. {e(d["short"])}'
        body = phero(cr, f'{e(d["name"])} IV drip', e(d["short"]), "", side) + f'''
<section class="sec"><div class="w layout">
<article>
 {answer(ans)}
 <div class="prose">{d["body"]}
 <h2>What's in the {e(d["name"])} drip</h2>
 <ul class="drip-ing">{ings}</ul>
 {meds}
 <h2>Who it's best for</h2><ul>{best}</ul>
 <h2>How the visit works</h2>
 <ol><li><b>Text us</b> "{e(d["name"])}" and your address at <a href="{sms(f"Hi! I'd like to book {d['name']}.")}">{PHONE1}</a>.</li><li><b>Your nurse arrives</b> and does a quick health screening to make sure the drip is right for you.</li><li><b>Relax for 45 to 60 minutes</b> while it runs. We clean up and you get back to your day.</li></ol>
 <h2>{e(d["name"])} FAQ</h2>
 </div>
 {faq_html(d["faqs"])}
 <p class="fine" style="margin-top:24px">Prices subject to change due to market fluctuations. IV therapy is not intended to diagnose, treat, cure or prevent any disease. All treatments require a health screening.</p>
</article>
{aside_book()}
</div></section>
<section class="sec bg-foam"><div class="w"><div class="head"><span class="kick">Also on the menu</span><h2>Other drips you might like</h2></div><div class="cards">{"".join(drip_card(x) for x in others)}</div></div></section>
{cta()}'''
        svc = {"@type": "Service", "@id": f'{BASE}/iv-menu/{d["slug"]}/#service', "name": f'{d["name"]} IV drip', "serviceType": "Mobile IV therapy",
               "description": d["short"], "provider": {"@id": BIZ_ID}, "areaServed": [f'{a["city"]}, FL' for a in AREAS],
               "offers": {"@type": "Offer", "price": str(d["price"]), "priceCurrency": "USD", "url": f'{BASE}/iv-menu/{d["slug"]}/', "availability": "https://schema.org/InStock"}}
        page(f'iv-menu/{d["slug"]}/', f'{d["name"]} IV Drip (${d["price"]}), Jupiter FL',
             f'{d["name"]} IV drip, ${d["price"]}, delivered to your home in Jupiter + Palm Beach County by a licensed nurse. With ' + ", ".join(n.split(",")[0] for (n,_),_b in d["ings"][1:4]) + ' + more.',
             body, [svc, faq_ld(d["faqs"], f'{BASE}/iv-menu/{d["slug"]}/')], cr)

# ================================================================ INGREDIENTS
def build_ingredients():
    cr = [("Home","/"),("Ingredient guide","/ingredients/")]
    used = {}
    for d in DRIPS:
        for (n,s),_b in d["ings"]: used.setdefault(s, []).append(d)
        for n,s,b in d.get("meds", []): used.setdefault(s, []).append(d)
    items = ""
    for s,n,role,txt in INGREDIENTS:
        ds = used.get(s, [])
        inn = ("In: " + ", ".join(f'<a href="/iv-menu/{d["slug"]}/">{e(d["name"])}</a>' for d in ds)) if ds else "Available as an add-in"
        if s == "nad-plus": inn = "Add to any drip for $50 · Available in <a href=\"/iv-menu/your-call/\">Your Call</a>"
        items += f'<div class="ingi" id="{s}"><div><h3>{e(n)}</h3><span class="role">{e(role)}</span></div><div><p>{e(txt)}</p><p class="in">{inn}</p></div></div>'
    toc = "".join(f'<a href="#{s}">{e(n.split(" (")[0])}</a>' for s,n,_r,_t in INGREDIENTS)
    body = phero(cr, "IV ingredient guide", "What's in our IV drips, what each ingredient does, and which drips include it. Plain language, from our nursing team.") + f'''
<section class="sec"><div class="w wn">
 {answer("Every drip starts with 1 liter of Lactated Ringer's or normal saline for hydration. We then add vitamins (C, B12, B-complex, D, biotin), minerals (zinc, magnesium), antioxidants (glutathione) and amino acids (amino blend, L-carnitine, taurine). NAD+ can be added to any drip, and medications for pain, nausea, stomach upset or allergy are optional in Get Right when appropriate.")}
 <div class="areas" style="margin-bottom:36px">{toc}</div>
 <div class="ingl">{items}</div>
 <p class="fine" style="margin-top:28px">This guide is general information, not medical advice. Your nurse reviews your health history, medications and allergies before every drip. IV therapy is not intended to diagnose, treat, cure or prevent any disease.</p>
</div></section>
{cta("Want help choosing?","Text us what you're hoping to feel. Your nurse will help you pick the right ingredients.")}'''
    dterms = {"@type": "DefinedTermSet", "@id": BASE + "/ingredients/#terms", "name": "IV therapy ingredients", "hasDefinedTerm": [
        {"@type": "DefinedTerm", "@id": f"{BASE}/ingredients/#{s}", "name": n, "description": t, "url": f"{BASE}/ingredients/#{s}"} for s,n,_r,t in INGREDIENTS]}
    page("ingredients/", "IV Ingredients: Glutathione, NAD+, Vitamin C",
         "What's in an IV drip? Glutathione, NAD+, vitamin C, B12, zinc, magnesium, amino acids and IV fluids explained in plain language, plus which drips include each one.",
         body, [dterms], cr)

# ================================================================ HOW IT WORKS
def build_how():
    cr = [("Home","/"),("How it works","/how-it-works/")]
    faqs = [FAQ[1][1][0], FAQ[1][1][1], FAQ[1][1][5], FAQ[1][1][4], FAQ[1][1][3]]
    body = phero(cr, "How mobile IV therapy works", "Three steps. Zero waiting rooms. Here's exactly what happens from your first text to the last drop.", BOOK_BTNS) + f'''
<section class="sec"><div class="w">
 {answer(f"Text {PHONE1} with your drip and address. A licensed nurse arrives, does a quick health screening, and starts your IV. You relax for 45 to 60 minutes while 1 liter of fluids and vitamins drips in. Then the nurse removes the IV and cleans everything up.")}
 <div class="steps">
  <div class="step rv"><div class="n"><b>1</b></div><h2 style="font-size:24px">Text us</h2><p>Send <a href="sms:{PHONE1_T}">{PHONE1}</a> or <a href="sms:{PHONE2_T}">{PHONE2}</a> your drip (or how you're feeling), how many people and your address. A real person replies fast and locks in the soonest time.</p></div>
  <div class="step rv"><div class="n"><b>2</b></div><h2 style="font-size:24px">Nurse arrives + screens</h2><p>A licensed nurse checks your symptoms, health history, medications, allergies and vital signs to make sure your drip is safe and right for you.</p></div>
  <div class="step rv"><div class="n"><b>3</b></div><h2 style="font-size:24px">Relax + refuel</h2><p>A quick pinch, then stay on the couch for 45 to 60 minutes. Your nurse monitors you, removes the IV and cleans up. You get back to your life.</p></div>
 </div>
</div></section>
<section class="sec bg-foam"><div class="w g2">
 <div><span class="kick">Where we go</span><h2>Anywhere you're comfortable.</h2><p class="sub">Homes, offices, hotels and rentals across northern Palm Beach County and the Treasure Coast.</p></div>
 <div class="g2" style="gap:16px">
  <div class="tile">{'<div class="ic">'+ic("home")+'</div>'}<h3>Home</h3><p>Stay on your couch or in bed.</p></div>
  <div class="tile">{'<div class="ic">'+ic("users")+'</div>'}<h3>Office</h3><p>Get back to work without losing an afternoon.</p></div>
  <div class="tile">{'<div class="ic">'+ic("pin")+'</div>'}<h3>Hotel + rental</h3><p>Visiting? We'll come to where you're staying.</p></div>
  <div class="tile">{'<div class="ic">'+ic("spark")+'</div>'}<h3>Events</h3><p>Bridal parties, groups and households. <a href="/group-iv-therapy/">Learn more</a>.</p></div>
 </div>
</div></section>
<section class="sec"><div class="w wn"><div class="head"><span class="kick">Questions</span><h2>Booking + visit FAQ</h2></div>{faq_html(faqs)}</div></section>
{cta()}'''
    howto = {"@type": "HowTo", "name": "How to book mobile IV therapy with Optimized Performance & Wellness", "totalTime": "PT60M",
             "step": [{"@type": "HowToStep", "position": 1, "name": "Text us", "text": f"Text {PHONE1} or {PHONE2} with your drip and address."},
                      {"@type": "HowToStep", "position": 2, "name": "Nurse arrives", "text": "A licensed nurse does a quick health screening to make sure your drip is right for you."},
                      {"@type": "HowToStep", "position": 3, "name": "Relax and refuel", "text": "Relax for 45 to 60 minutes while the drip runs. The nurse cleans up afterward."}]}
    page("how-it-works/", "How Mobile IV Therapy Works",
         "How at-home IV therapy works in Jupiter + Palm Beach County: text to book, a licensed nurse screens you, and you relax 45–60 minutes. No waiting room.",
         body, [howto, faq_ld(faqs, BASE + "/how-it-works/")], cr, cur="how-it-works/")

# ================================================================ GROUP
def build_group():
    cr = [("Home","/"),("Group + event IV therapy","/group-iv-therapy/")]
    faqs = [("Can you treat several people in one visit?","Yes, we treat the whole household or group in one visit, ages 10 and older. Let us know how many people when you text so your nurse brings enough for everyone."),
            ("Which drip is best before a wedding?","Glow is a favorite before weddings, photo shoots and galas. It has boosted glutathione and vitamin C plus biotin. Many guests also choose Foundational Meyers or Recover."),
            ("Can everyone pick a different drip?","Yes. Each person can choose their own drip, and every person gets their own health screening first.")]
    body = phero(cr, "Group + event IV therapy", "Bridal parties, family visits, sick households and team recovery days. We treat everyone in one visit, right where you are.", f'<div class="btns"><a class="btn btn-p" href="{sms("Hi! I would like to book IVs for a group.")}">{ic("chat",18)}Text us your group size</a></div>') + f'''
<section class="sec"><div class="w layout"><article>
 {answer("Optimized Performance &amp; Wellness can give IV drips to a whole household or group in one visit at your home, rental or hotel in Jupiter and Palm Beach County. Everyone 10 and older can be treated, each person gets their own health screening, and each can choose their own drip. Text us how many people so your nurse brings enough for everyone.")}
 <div class="prose">
 <h2>Popular reasons to book a group</h2>
 <ul><li><b>Weddings + bridal parties:</b> <a href="/iv-menu/glow/">Glow</a> drips before the big day, at your rental or hotel.</li><li><b>The whole house is sick:</b> one visit instead of multiple urgent care trips. See <a href="/iv-menu/get-right/">Get Right</a>.</li><li><b>Visiting family + friends:</b> <a href="/iv-menu/travel-defense/">Travel Defense</a> on arrival or before everyone flies home.</li><li><b>Teams + training groups:</b> <a href="/iv-menu/recover/">Recover</a> after a race, tournament or hard training day.</li></ul>
 <h2>How group visits work</h2>
 <ol><li>Text us your date, location, number of people and the drips you're interested in.</li><li>We confirm timing and make sure your nurse brings enough for everyone.</li><li>Each person is screened, then drips run at the same time, so the whole group is usually done in about an hour.</li></ol>
 <h2>Group IV FAQ</h2></div>
 {faq_html(faqs)}
</article>{aside_book()}</div></section>
{cta("Planning a group?","Text us the date, location and number of people. We'll take care of the rest.")}'''
    page("group-iv-therapy/", "Group + Bridal Party IV Therapy in Jupiter",
         "Group IV therapy in Jupiter + Palm Beach County: bridal parties, sick households, visiting family and teams treated in one visit at your home, rental or hotel.",
         body, [faq_ld(faqs, BASE + "/group-iv-therapy/")], cr)

# ================================================================ SERVICE AREAS
def build_areas():
    cr = [("Home","/"),("Service areas","/service-areas/")]
    tiles = "".join(f'<a class="tile rv" href="/service-areas/{a["slug"]}/"><div class="ic">{ic("pin")}</div><h3>{e(a["city"])}, FL</h3><p>{e(a["county"])}</p></a>' for a in AREAS)
    body = phero(cr, "Mobile IV therapy service areas", "We make house calls to homes, offices, hotels and rentals across northern Palm Beach County and the Treasure Coast.", BOOK_BTNS) + f'''
<section class="sec"><div class="w">
 {answer("Optimized Performance &amp; Wellness provides mobile IV therapy in Jupiter, Tequesta, Juno Beach, Palm Beach Gardens, North Palm Beach and West Palm Beach in Palm Beach County, and Hobe Sound and Stuart in Martin County. Don't see your town? Text us, we'll likely still come.", "Where we go")}
 <div class="g4">{tiles}</div>
 <div class="note" style="margin-top:28px">Don't see your town? <a href="{sms("Hi! Do you come to my area?")}">Text us your address</a>. We'll likely still come.</div>
</div></section>
{cta()}'''
    page("service-areas/", "IV Therapy Service Areas: Jupiter to Stuart, FL",
         "Mobile IV therapy house calls in Jupiter, Tequesta, Juno Beach, Palm Beach Gardens, North Palm Beach, Hobe Sound, Stuart and West Palm Beach, FL.",
         body, None, cr)

    for a in AREAS:
        cr = [("Home","/"),("Service areas","/service-areas/"),(f'{a["city"]}, FL', f'/service-areas/{a["slug"]}/')]
        c = e(a["city"])
        faqs = [(f"Do you offer mobile IV therapy in {a['city']}, FL?", f"Yes. A licensed nurse from {NAME} comes to homes, offices, hotels and rentals in {a['city']}. Text {PHONE1} with your drip and address to book."),
                (f"How much is an at-home IV in {a['city']}?", "Drips range from $150 (Your Call) to $435 (Get Right), and NAD+ can be added to any drip for $50. Prices subject to change due to market fluctuations."),
                (f"How fast can a nurse get to me in {a['city']}?", "Text us your address and we'll lock in the soonest available time. A drip takes about 45 to 60 minutes once your nurse arrives."),
                ("Can you treat my whole family?", "Yes, we treat ages 10 and older. Let us know how many people when you text so your nurse brings enough for everyone.")]
        near = "".join(f'<a href="/service-areas/{n}/">{e(AREA[n]["city"])}</a>' for n in a["near"])
        picks = [DRIP["get-right"], DRIP["foundational-meyers"], DRIP["recover"]]
        body = phero(cr, f"Mobile IV therapy in {c}, FL", f"A licensed nurse brings IV hydration and vitamin drips to your home, office or hotel in {c}. No waiting room, no driving sick. Drips from $150.", f'<div class="btns"><a class="btn btn-p" href="{sms("Hi! I would like to book an IV in " + a["city"] + ".")}">{ic("chat",18)}Text {PHONE1}</a><a class="btn btn-o" href="/iv-menu/">See the IV menu</a></div>') + f'''
<section class="sec"><div class="w layout"><article>
 {answer(f"{e(NAME)} offers mobile IV therapy in {c}, FL ({e(a['county'])}). A licensed nurse comes to your home, office, hotel or rental, does a health screening, and gives IV hydration and vitamin drips in 45 to 60 minutes. Drips cost $150 to $435. Book by texting {PHONE1}.")}
 <div class="prose">
 <p>{e(a["intro"])}</p>
 {a["local"]}
 <h2>Where we visit in {c}</h2>
 <p>{e(a["places"])}.</p>
 <h2>Popular drips in {c}</h2>
 </div>
 <div class="cards">{"".join(drip_card(d) for d in picks)}</div>
 <p style="margin-top:18px"><a class="tlink" href="/iv-menu/">See all 7 drips + prices</a></p>
 <div class="prose" style="margin-top:36px"><h2>How it works in {c}</h2>
 <ol><li><b>Text us</b> your drip and {c} address at <a href="sms:{PHONE1_T}">{PHONE1}</a> or <a href="sms:{PHONE2_T}">{PHONE2}</a>.</li><li><b>Your nurse arrives</b> and does a quick health screening.</li><li><b>Relax for 45 to 60 minutes.</b> We clean up, you get back to your life.</li></ol>
 <h2>{c} IV therapy FAQ</h2></div>
 {faq_html(faqs)}
 <div class="warn" style="margin-top:28px">{ic("alert",24).replace('<svg','<svg class="ic"')}<div><b>IV hydration isn't emergency care.</b> For trouble breathing, chest pain, confusion, a fever that won't come down, or severe dehydration in a child, call your doctor or 911.</div></div>
</article>{aside_book(f'<div class="box"><h3>Nearby areas</h3><div class="areas">{near}</div></div>')}</div></section>
{cta(f"Feel better in {c}. Don't get up.")}'''
        svc = {"@type": "Service", "@id": f'{BASE}/service-areas/{a["slug"]}/#service', "name": f'Mobile IV therapy in {a["city"]}, FL', "serviceType": "Mobile IV therapy",
               "provider": {"@id": BIZ_ID}, "areaServed": {"@type": "City", "name": f'{a["city"]}, FL', "containedInPlace": {"@type": "AdministrativeArea", "name": f'{a["county"]}, Florida'}},
               "offers": {"@type": "AggregateOffer", "lowPrice": "150", "highPrice": "435", "priceCurrency": "USD", "offerCount": len(DRIPS)}}
        page(f'service-areas/{a["slug"]}/', f'Mobile IV Therapy in {a["city"]}, FL',
             f'At-home IV therapy in {a["city"]}, FL. A licensed nurse brings IV drips to your home, office or hotel. $150–$435. Text {PHONE1}.',
             body, [svc, faq_ld(faqs, f'{BASE}/service-areas/{a["slug"]}/')], cr)

# ================================================================ ABOUT
def build_about():
    cr = [("Home","/"),("About","/about/")]
    body = phero(cr, "About Optimized Performance &amp; Wellness", "A Jupiter-based mobile IV therapy team of licensed nurses who come to you, so you can feel like yourself again without leaving home.") + f'''
<section class="sec"><div class="w layout"><article>
 {answer("Optimized Performance &amp; Wellness is a mobile IV therapy provider based in Jupiter, Florida. Licensed registered nurses, overseen by a medical director, bring IV hydration and vitamin drips to homes, offices and hotels across northern Palm Beach County and the Treasure Coast. Every visit starts with a health screening.", "Who we are")}
 <div class="prose">
 <h2>Our approach</h2>
 <p>Our experienced healthcare team works with you to help you reach your best. Every drip on our menu is a starting point. We customize it to you and your situation, to optimize how you feel today so you can meet your goals and be your best self.</p>
 <p>We started with a simple idea: when you feel awful, the last thing you should have to do is drive to a clinic and sit in a waiting room. So we come to you.</p>
 <h2>Your care team</h2>
 </div>
 <div class="g2" style="gap:18px;margin-bottom:32px">
  <div class="tile"><div class="ic">{ic("nurse")}</div><h3>Barry, RN</h3><p>Every IV is overseen by Barry, our licensed registered nurse, who brings 5 years of emergency room experience to every visit.</p></div>
  <div class="tile"><div class="ic">{ic("steth")}</div><h3>Medical director</h3><p>Our licensed nurses are overseen by a medical director.</p></div>
  <div class="tile"><div class="ic">{ic("chat")}</div><h3>Primary care telehealth</h3><p>Your visit can be upgraded to a telehealth call with our primary care provider. Telehealth visits are available to schedule for a fee.</p></div>
  <div class="tile"><div class="ic">{ic("shield")}</div><h3>Screening first, always</h3><p>Every visit starts with a health screening to make sure your drip is safe and right for you. <a href="/safety/">Our safety process</a>.</p></div>
 </div>
 <div class="prose">
 <h2>What we believe</h2>
 <ul><li><b>Real people, fast replies.</b> When you text, a real person (one of our RNs or healthcare professionals) gets back to you.</li><li><b>Honest about what IVs do.</b> IV hydration supports recovery. It doesn't cure illness, and it isn't emergency care.</li><li><b>Tailored, not upsold.</b> Often IV fluids plus the right medication is all it takes. No package needed.</li></ul>
 </div>
</article>{aside_book()}</div></section>
{cta()}'''
    about = {"@type": "AboutPage", "@id": BASE + "/about/#about", "url": BASE + "/about/", "mainEntity": {"@id": BIZ_ID}}
    page("about/", "About Our RN-Led Mobile IV Team",
         "Meet Optimized Performance & Wellness: Jupiter-based licensed nurses with ER experience, overseen by a medical director, bringing IV therapy to your home.",
         body, [about], cr, cur="about/")

# ================================================================ SAFETY
def build_safety():
    cr = [("Home","/"),("Safety + screening","/safety/")]
    faqs = [FAQ[2][1][2], FAQ[2][1][0], FAQ[2][1][4],
            ("Who might not be a good fit for IV therapy?","Your nurse will ask about conditions that can affect how your body handles fluids or certain ingredients, such as heart or kidney conditions, pregnancy, allergies and your current medications. If an IV isn't right for you, your nurse will tell you and may recommend you see your doctor."),
            ("What are the side effects of IV therapy?","Most people only notice a quick pinch. Some may have minor bruising or tenderness at the IV site, or feel a cool sensation as fluids run. Your nurse monitors you during the drip. Contact your doctor if redness, swelling or pain at the site gets worse.")]
    body = phero(cr, "Safety + health screening", "Every single drip starts with a health screening by a licensed nurse. Here's what we check and why.") + f'''
<section class="sec"><div class="w layout"><article>
 {answer("Every IV from Optimized Performance &amp; Wellness is given by a licensed nurse, overseen by a medical director, after a health screening that reviews your symptoms, health history, medications, allergies and vital signs. If an IV isn't right for you, your nurse won't proceed. IV hydration isn't emergency care.", "How we keep you safe")}
 <div class="prose">
 <h2>What your nurse checks</h2>
 <ul><li>Your symptoms and how long you've had them</li><li>Your health history, including heart, kidney and other conditions</li><li>Medications you take and any allergies</li><li>Vital signs</li><li>Whether you're pregnant or could be</li></ul>
 <h2>Medications are optional and assessed</h2>
 <p>Medications like Toradol, Zofran, Pepcid and Benadryl are never automatic. They're optional and only given when appropriate after your nurse's assessment.</p>
 <h2>Ages we treat</h2><p>We treat ages 10 and older.</p>
 <h2>When to call a doctor or 911 instead</h2></div>
 <div class="warn">{ic("alert",24).replace('<svg','<svg class="ic"')}<div><b>IV hydration isn't emergency care.</b> For trouble breathing, chest pain, confusion, a fever that won't come down, or severe dehydration in a child, call your doctor or 911.</div></div>
 <div class="prose" style="margin-top:36px"><h2>Safety FAQ</h2></div>
 {faq_html(faqs)}
</article>{aside_book()}</div></section>
{cta("Questions before you book?","Text or call us. One of our RNs or healthcare professionals will get back to you.")}'''
    page("safety/", "Is IV Therapy Safe? Our Screening Process",
         "How Optimized Performance & Wellness keeps mobile IV therapy safe: licensed nurses, medical director oversight, and a health screening before every drip.",
         body, [faq_ld(faqs, BASE + "/safety/")], cr)

# ================================================================ FAQ
def build_faq():
    cr = [("Home","/"),("FAQ","/faq/")]
    allf = [q for _c,qs in FAQ for q in qs]
    sections = "".join(f'<h2 class="faqcat" id="{c.split()[0].lower().strip("+")}">{e(c)}</h2>{faq_html(qs)}' for c,qs in FAQ)
    body = phero(cr, "Mobile IV therapy FAQ", f"Good questions, straight answers. Still wondering? Text or call {PHONE1} and a real person will get back to you.") + f'''
<section class="sec"><div class="w wn">
 {sections}
 <div class="warn" style="margin-top:36px">{ic("alert",24).replace('<svg','<svg class="ic"')}<div><b>When to call a doctor instead:</b> IV hydration isn't emergency care. For trouble breathing, chest pain, confusion, a fever that won't come down, or severe dehydration in a child, call your doctor or 911.</div></div>
</div></section>
{cta()}'''
    page("faq/", "Mobile IV Therapy FAQ",
         "Answers about mobile IV therapy in Jupiter + Palm Beach County: what it is, cost, how long a drip takes, safety, who gives the IV, and when to see a doctor.",
         body, [faq_ld(allf, BASE + "/faq/")], cr, cur="faq/")

# ================================================================ CONTACT
def build_contact():
    cr = [("Home","/"),("Contact + booking","/contact/")]
    body = phero(cr, "Book your IV", "Booking is a quick text. Send your drip (or how you're feeling), how many people and your address, and we'll lock in the soonest time.") + f'''
<section class="sec"><div class="w">
 {answer(f"Book mobile IV therapy by texting {PHONE1} or {PHONE2}. You can also call either number or email {EMAIL}. Reach us at either number. If one isn't going through, try the other.", "How to book")}
 <div class="g3">
  <a class="tile" href="{sms("Hi! I would like to book an IV.")}"><div class="ic">{ic("chat")}</div><h3>Text (fastest)</h3><p>{PHONE1}<br>{PHONE2}</p></a>
  <a class="tile" href="tel:{PHONE1_T}"><div class="ic">{ic("phone")}</div><h3>Call</h3><p>{PHONE1}<br>{PHONE2}</p></a>
  <a class="tile" href="mailto:{EMAIL}"><div class="ic">{ic("drop")}</div><h3>Email</h3><p>{EMAIL}</p></a>
 </div>
 <div class="g2" style="margin-top:48px">
  <div class="tile"><h3>What to include in your text</h3><ul class="chk" style="margin-top:14px"><li>The drip you want, or how you're feeling</li><li>How many people</li><li>Your address (home, office, hotel or rental)</li><li>Your preferred time</li></ul></div>
  <div class="tile"><h3>Service area</h3><p style="margin-bottom:14px">Jupiter, Tequesta, Juno Beach, Palm Beach Gardens, North Palm Beach, Hobe Sound, Stuart and West Palm Beach. Don't see your town? Text us, we'll likely still come.</p><a class="tlink" href="/service-areas/">Service areas</a></div>
 </div>
 <p class="fine" style="margin-top:28px">Follow us on <a href="{IG}" rel="noopener">Instagram</a>. In an emergency, call 911.</p>
</div></section>'''
    cp = {"@type": "ContactPage", "@id": BASE + "/contact/#contact", "url": BASE + "/contact/", "mainEntity": {"@id": BIZ_ID}}
    page("contact/", "Book Mobile IV Therapy by Text",
         f"Book at-home IV therapy in Jupiter + Palm Beach County by text: {PHONE1} or {PHONE2}, or email us. A real person replies fast.",
         body, [cp], cr)

# ================================================================ GUIDES
def build_guides():
    cr = [("Home","/"),("Guides","/guides/")]
    cards = "".join(f'<a class="acard rv" href="/guides/{g["slug"]}/"><div class="art"></div><div class="ab"><span class="tg">Guide</span><h2 style="font-size:21px;margin:8px 0">{e(g["title"])}</h2><p>{e(g["short"])}</p></div></a>' for g in GUIDES)
    body = phero(cr, "IV therapy guides", "Plain-language answers to the questions we hear most, from our nursing team.") + f'''
<section class="sec"><div class="w"><div class="g2" style="gap:22px">{cards}</div>
<p style="margin-top:28px"><a class="tlink" href="/ingredients/">IV ingredient guide</a> &nbsp;·&nbsp; <a class="tlink" href="/faq/">FAQ</a></p></div></section>
{cta()}'''
    page("guides/", "IV Therapy Guides",
         "Guides to mobile IV therapy: cost in Palm Beach County, what to expect at an at-home visit, IV fluids when you're sick, and IV hydration vs. drinking water.",
         body, None, cr, cur="guides/")
    rows = "".join(f'<tr><td><a href="/iv-menu/{d["slug"]}/">{e(d["name"])}</a></td><td>${d["price"]}</td><td>{e(d["tag"])}</td></tr>' for d in sorted(DRIPS, key=lambda x: x["price"]))
    for g in GUIDES:
        url = f'/guides/{g["slug"]}/'
        cr = [("Home","/"),("Guides","/guides/"),(g["title"], url)]
        content = g["body"].replace("{rows}", rows).replace("{p1}", PHONE1).replace("{p2}", PHONE2).replace("{alert}", ic("alert",24).replace('<svg','<svg class="ic"'))
        more = "".join(f'<li><a href="/guides/{x["slug"]}/">{e(x["title"])}</a></li>' for x in GUIDES if x["slug"] != g["slug"])
        body = phero(cr, e(g["title"]), e(g["short"])) + f'''
<section class="sec"><div class="w layout"><article>
 <p class="meta">By the {e(NAME)} nursing team · Updated {UPDATED_H}</p>
 {answer(g["answer"])}
 <div class="prose">{content}</div>
 <p class="fine" style="margin-top:32px">This article is general information, not medical advice. IV therapy is not intended to diagnose, treat, cure or prevent any disease and is not a substitute for care from your doctor. In an emergency, call 911.</p>
</article>{aside_book(f'<div class="box"><h3>More guides</h3><ul>{more}</ul></div>')}</div></section>
{cta()}'''
        art = {"@type": "Article", "@id": BASE + url + "#article", "headline": g["title"], "description": g["desc"], "datePublished": UPDATED, "dateModified": UPDATED,
               "author": {"@id": BIZ_ID}, "publisher": {"@id": BIZ_ID}, "mainEntityOfPage": BASE + url, "image": BASE + "/og-image.jpg",
               "speakable": {"@type": "SpeakableSpecification", "cssSelector": [".answer p"]}}
        page(url.strip("/") + "/", g["title"], g["desc"], body, [art], cr, og_type="article")

# ================================================================ 404 + extras
def build_extras():
    body = f'''<header class="phero" style="padding:96px 0"><div class="w center"><h1>Page not found</h1><p class="lead" style="margin:16px auto 28px">That page may have moved. Here's where to go next.</p>
<div class="btns" style="justify-content:center"><a class="btn btn-p" href="/">Home</a><a class="btn btn-o" href="/iv-menu/">IV menu</a><a class="btn btn-o" href="/contact/">Book</a></div></div></header>'''
    page("404.html", "Page not found", "Page not found.", body, noindex=True)

    urls = "\n".join(f'  <url><loc>{BASE}/{p}</loc><lastmod>{UPDATED}</lastmod><priority>{"1.0" if p=="" else "0.8" if p.count("/")==1 else "0.6"}</priority></url>' for p in PAGES)
    open(os.path.join(ROOT, "sitemap.xml"), "w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}\n</urlset>\n')
    open(os.path.join(ROOT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nDisallow: /_build/\n\n# AI answer engines are welcome\nUser-agent: GPTBot\nAllow: /\nUser-agent: OAI-SearchBot\nAllow: /\nUser-agent: ChatGPT-User\nAllow: /\nUser-agent: PerplexityBot\nAllow: /\nUser-agent: ClaudeBot\nAllow: /\nUser-agent: Claude-SearchBot\nAllow: /\nUser-agent: Google-Extended\nAllow: /\nUser-agent: Applebot-Extended\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")
    drips = "\n".join(f'- [{d["name"]} (${d["price"]})]({BASE}/iv-menu/{d["slug"]}/): {d["short"]}' for d in DRIPS)
    areas = "\n".join(f'- [{a["city"]}, FL]({BASE}/service-areas/{a["slug"]}/)' for a in AREAS)
    guides = "\n".join(f'- [{g["title"]}]({BASE}/guides/{g["slug"]}/): {g["short"]}' for g in GUIDES)
    open(os.path.join(ROOT, "llms.txt"), "w").write(f"""# {NAME}

> Mobile IV therapy based in Jupiter, Florida. A licensed registered nurse, overseen by a medical director, brings IV hydration and vitamin drips to homes, offices, hotels and rentals across northern Palm Beach County and the Treasure Coast. Every visit starts with a health screening and takes 45 to 60 minutes. Drips cost $150 to $435. Book by text.

- Phone / text: {PHONE1} or {PHONE2}
- Email: {EMAIL}
- Ages treated: 10 and older; whole households in one visit
- Every drip includes 1 liter of Lactated Ringer's or normal saline
- NAD+ add-on: $50 for any drip
- Not emergency care: for trouble breathing, chest pain, confusion, a fever that won't come down, or severe dehydration in a child, call a doctor or 911.

## IV menu
{drips}

## Service areas
{areas}

## Key pages
- [IV menu + prices]({BASE}/iv-menu/)
- [How it works]({BASE}/how-it-works/)
- [Ingredient guide]({BASE}/ingredients/)
- [Safety + screening]({BASE}/safety/)
- [Group + event IV therapy]({BASE}/group-iv-therapy/)
- [About]({BASE}/about/)
- [FAQ]({BASE}/faq/)
- [Contact + booking]({BASE}/contact/)

## Guides
{guides}
""")
    open(os.path.join(ROOT, "netlify.toml"), "w").write("""[build]
  publish = "."

[[redirects]]
  from = "/_build/*"
  to = "/404.html"
  status = 404

[[headers]]
  for = "/assets/*"
  [headers.values]
    Cache-Control = "public, max-age=604800"

[[headers]]
  for = "/*"
  [headers.values]
    X-Content-Type-Options = "nosniff"
    Referrer-Policy = "strict-origin-when-cross-origin"
""")

if __name__ == "__main__":
    build_home(); build_menu(); build_ingredients(); build_how(); build_group(); build_areas()
    build_about(); build_safety(); build_faq(); build_contact(); build_guides(); build_extras()
    print(f"Built {len(PAGES)} indexable pages + 404")
