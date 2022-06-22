from datetime import date

def num_of_days(date1, date2):
    days_elapsed = (date2 - date1).days
    return days_elapsed
    print("Days Elapsed: ", days_elapsed)

def get_items(dict): # Displays items from a given category that have been worn the least
  minimum = min(dict.values())
  print("Minimum Number of Wears: ", minimum)
  for key, value in dict.items():
    if value == minimum:
      print(key)
  return "****"  
      
def simple_sort(dict): # Lists in order of wears for one item category
  simple_sort = sorted(dict.items(), key = lambda x: x[1], reverse = False)
  return simple_sort
  
def get_stats(dict, max_wears):
  vals = [v for _, v in dict.items()]
  total_wears = sum(vals)
  average = total_wears / len(dict)
  minimum_requirement = round(total_wears / max_wears, 2) # Minimum number of items from a category required to not wear the same item twice per two-month period (or other length of time chosen by the user)
  # Setting floating-point number precision to 2 decimal places for readability
  surplus = round(len(dict) - minimum_requirement, 2) # How many more items the user has versus what they need. A deficit would be displayed as a negative surplus.
  proportional_surplus = round(surplus / minimum_requirement, 2) # The surplus as a proportion of the minimum items required is a standardized approach that weighs, for example, having two pairs of gloves when you only need one differently from having 10 dresses when you only need nine, despite the surpluses in each example being the same number of items
  print(get_items(dict))
  print("Total Wears: ", total_wears)
  print("Average Wears: ", average)
  print("Minimum Requirement: ", minimum_requirement)
  print("Surplus: ", surplus)
  print("Proportional Surplus: ", proportional_surplus, "\n")
  print(simple_sort(dict), "\n")
  return proportional_surplus

def outfit_generator(index, *args): 
  # If index is 0, returns the least-worn item from each of your categories of choice, thereby generating an outfit
    # If the user doesn't like the generated outfit from the category minima, they can edit the index to 1, 2, etc. 
  for arg in args:
    if index >= len(arg): # Avoids selecting an index that is out of range (e.g., the user tries to pull the 25th sweater when there are only 20 sweaters)
      print("Not enough items")
    else: 
      print(arg[index]) 
    
def what_to_buy(dict):
  sort = sorted(dict.items(), key = lambda x: x[1], reverse = False)
  print("What to Buy Next: ", sort)

def main():
  NONREPEAT_PERIOD = 62 # Goal of not wearing the same item more than once per two-month period, on average. User can set their nonrepeat period of choice.
  days_elapsed = num_of_days(date(2018, 1, 1), date.today()) # Enters the date user started tracking wears and today's date
  max_wears = days_elapsed / NONREPEAT_PERIOD # Maximum number of times the same item could be worn during the entire period, if it was worn only an average of once per two-month period

  # Data on items in each category, in alphabetical order in main function so user can easily update after each new wear. Data in main allows for easy daily updates. 
    dresses = {"AFRM": 5, "All Saints -- Picolina": 6, "Banana Republic (floral)": 5, "Banana Republic (red)": 7, "Banana Republic (sweater)": 4, "Banana Republic (tweed)": 6, "Banana Republic (white)": 4, "Collectif": 2, "Erin by Erin Fetherston": 6, "Forever 21 (fuchsia)": 6, "Forever 21(navy)": 7, "Forever 21 (tiles)": 6, "Forever 21 Twist": 6, "H&M (black knit)": 7, "Handkerchief hem": 6, "Hell Bunny Vixen": 6, "Juicy Couture": 6, "Kaileigh -- Amandine": 6, "Kaileigh -- Kaela": 7, "Marni": 7, "Melrose and Market": 4, "Metro Style": 6, "Mossimo": 6, "Mystic": 7, "Pantagio": 0, "Rampage": 6, "Rose-Marie Seoir": 6, "See by Chloe": 6, "Vivoli": 4, "Voodoo Vixen": 1, "Xhilaration (black)": 6, "Xhilaration (purple)": 6, "XOXO": 5}

  jumpsuits = {"Banana Republic": 6, "Forever 21 (rose)": 6, "Kaileigh -- Rica": 6, "MSGM": 6, "Red Valentino": 6, "Rules of Etiquette": 6, "Xhilaration (black)": 6, "Xhilaration (red)": 6}

  tops = {"Alice + Olivia -- Hilaria": 6, "Ann Taylor Loft (blue)": 7, "Ann Taylor Loft (purple)": 7, "Aqua Blues": 7, "At Last Classics": 5, "BCX": 5, "Bella + Canvas (We Should All Be Feminists)": 4, "Black lace (short sleeve)": 6, "Burberry Brit": 7, "Cece by Cynthia Steffe": 3, "Chiapanec": 5, "Covington": 7, "Cynthia Rowley": 7, "Edward": 7, "Elodie": 4, "Express(lace)": 7, "Forever 21 (black lace Gothic)": 6, "Forever 21 (black ruffled)": 7, "Forever 21 (blue)": 8, "Forever 21 (crosshatch)": 6, "Forever 21 (marigold)": 9, "Forever 21 (mint)": 6, "Forever 21 (strapless)": 5, "Forever 21 (yellow)": 1, "French Laundry (purple)": 7, "French Laundry (white)": 6, "Gap (plaid)": 3, "Gildan (Don't Tread on Me)": 4, "Gili (gold)": 1, "Gili (light gold)": 5, "H&M (lavender)": 5, "H&M (pink)": 7, "H&M (purple)": 6, "Harve Benard (black)": 7, "Heritage 1981 (Creme de la Creme)": 5, "Hillard & Hanson (buttonup)": 6, "Hillard & Hanson (sleeveless)": 6, "J for Justify": 6, "Love 21": 7, "Lux": 6, "Maje": 8, "Marina": 3, "Marks & Spencer": 5, "Mars": 6, "Merona (pink)": 7, "Merona (striped)": 5, "Modcloth (black)": 1, "Modcloth(white)": 1, "Mossimo (blue)": 7, "Mossimo (gray)": 9, "Mudo Collection": 6, "Next Level": 1, "Old Navy": 5, "Peter Jensen": 6, "Pierre Cardin": 6, "Rachel Rachel Roy": 6, "Rampage": 6, "Style & Co. (white)": 11, "Sylvie & Mado": 7, "T. Tandon NY": 7, "Tanzara": 5,  "Tokidoki": 7, "Vakkorama": 5, "West Kei -- Julianna": 8, "Wild Fable": 9}

  sweaters = {"Banana Republic (caramel)": 4, "Banana Republic (cats)": 9, "Banana Republic (heather)": 6, "Banana Republic (midnight)": 4, "Banana Republic (sleeveless)": 9, "Calypso St. Barth": 1, "En Creme": 8, "Forever 21 (bow)": 7, "Forever 21 (duster)": 7, "Gap (duster)": 8, "Gap (striped)": 3, "H&M (beige)": 6, "H&M (green)": 10, "H&M (silver)": 6, "H&M (shrug)": 6, "Lou & Grey": 11, "REQ": 9, "Uniqlo (black)": 10, "Uniqlo (lavender)": 7, "Uniqlo (mauve)": 7, "Wild Fable (overalls)": 4, "XOXO (gray)": 7}

  skirts = {"Desigual": 7, "Divided by H&M": 8, "Forever 21 (high-low)": 6, "Forever 21 (lips)": 7, "Forever 21 (red pencil)": 9, "French Grey -- Kaylyn": 7, "H&M (pink)": 7, "Jay Godrey": 9, "Luella": 8, "Mod Department": 7, "Mondetta": 7, "Renai Keikaku": 8, "SC & Co.": 6, "Talbots": 4, "Topshop": 4, "Zara": 7, "41 Hawthorn -- Maura": 8}

  jeans = {"Banana Republic (black coated)": 10, "Banana Republic (black flared)": 10, "Banana Republic (light wash)":7 , "Banana Republic (medium wash)": 10, "Calvin Klein (dark wash)": 7}

  pants = {"A New Day": 6, "Alfani": 9, "Amanda & Chelsea": 9, "Banana Republic -- Avery": 9, "Banana Republic -- Sloan": 4, "Banana Republic (periwinkle)": 7, "Banana Republic (tan)": 10, "BCX (black)": 11, "BCX (gray)": 7, "Dictionary Jodi": 11, "Fiona": 7, "Forever 21 (athleisure)": 13, "Forever 21 (black high-waisted": 10, "Forever 21 (midnight)": 8, "H&M (pink)": 6, "INC": 8, "Levi's -- Math Club": 4, "Napel": 11, "Rachel Zoe": 11, "Style & Co.": 12}

  hosiery = {"Art socks (black/jade)": 0, "art socks (black/navy)":0, "art socks (charcoal/orange)": 0, "art socks (ocher/oxblood)" :1, "black crocheted (Mommy)": 3, "black knee socks": 1, "black knee socks (from Mommy": 0, "black pantyhose": 2, "blue knee socks": 1, "Copperfield's Books": 1, "crosshatch": 2, "fishnet knee socks": 0, "fishnet knee socks w/ flowers": 0, "Forever 21": 2, "Gigi K. (fishnets with bow)": 4, "Gigi K. (knee socks)": 1, "Hue": 4, "long black knee socks": 1, "Music Legs": 1, "ribbed black knee socks": 1, "Victoria's Secret": 0, "Wego": 1, "white knee socks": 0}

  jackets = {"A New Day": 12, "Ann Taylor Loft (floral)": 7, "Ann Taylor Loft (pinstriped)": 9, "Anne Klein": 8, "Banana Republic": 6, "BCBG": 8, "BCX": 8, "Charter Club": 7, "CW": 6, "D-Face": 9, "Faith + Passion": 7, "Forever 21 (boucle)": 9, "Forever 21 (cape)": 7, "Forever 21 (floral)": 8, "Grass": 9, "INC": 7, "Jolt": 9, "Jones New York": 8, "Joseph Abboud": 8, "Lauren Ralph Lauren": 8, "Lou & Grey": 11, "Merona": 8, "Old Navy": 10, "Pendleton": 7, "Renai Keikaku": 27, "Studio M": 8, "Style & Co. Jeans": 9, "Tahari": 8, "True Meaning": 7}

  light_coats = {"A New Day": 11, "BCX": 9, "Brette Fitzgibbon": 11, "Carven": 13, "Cello": 13, "Divided by H&M (leopard)": 10, "Divided by H&M (red)": 5, "Dollhouse": 11, "Forever 21 (fur)": 9, "Harris Wallace": 10, "Hillard & Hanson": 11, "I. Magnin": 11, "Koret Francisca": 1, "Sashimi": 12, "St. Patrick's": 11, "Style & Co.": 11}

  heavy_coats = {"A New Day": 15, "Badgley Mischka": 15, "Banana Republic (olive)": 15, "Banana Republic (white)": 14, "Divided by H&M": 14, "Fengzhiyuan": 14, "Hell Bunny": 14, "Marc New York Risor": 16, "Marc New York Yorkshire": 16, "North Face": 19, "Sebby": 14, "Style & Co.": 14, "Uniqlo (midnight)": 15, "Uniqlo (tan)": 14, "Vero Moda Madge": 15}

  ankle_boots = {"Adrianna Papell": 7, "Aerosoles (burgundy)": 8, "Calvin Klein": 8, "Docle Vita (black)": 9, "Dresshead": 7, "Franco Sarto": 7, "Jones New York Chloe": 8, "Lulu Hun": 7, "Nine West": 7, "Old Navy": 7, "Royal Monk": 7, "Sam & Libby": 7}

  heels = {"Aerosoles (perforated)": 9, "Anna Sui": 15, "Banana Republic (white/black)": 9, "Breckelle's": 9, "Daily Shoes -- Wendy": 9, "Dex Flex": 9, "Dolce & Gabbana": 5, "DV Dolce Vita (mules)": 7, "Forever 21 (lace-up)": 9, "Giani Bernini": 9, "Halogen": 9, "Impo": 9, "INC": 10, "Jessica Simpson": 8, "LifeStride (gold)": 9, "LifeStride (wedges)": 9, "Rocket Dog (gray)": 8, "Rocket Dog (burnt red)": 9, "Steve Madden": 9, "Steven by Steve Madden": 11, "Vionic -- Mia": 9, "10 Corso Como": 9}

  boots = {"Casadei": 9, "Coach (black)": 10, "Coach (Poppy)": 9, "Getmorebeauty": 9, "Merona": 9}

  flats = {"A Rider Girl": 10, "Banana Republic": 11, "Bandolino": 10, "Barneys": 9, "Circus by Sam Edelman": 10, "Crocs": 12, "Dukkah": 10, "Franco Sarto": 9, "INC": 10, "Kate Spade": 10, "Marc by Marc Jacobs (kitty)": 12, "Marc by Marc Jacobs (mouse)": 10, "Marc Jacobs": 11, "Marni": 10, "Old Navy (blue)": 11, "Old Navy (yellow)": 10, "Rothy's": 9, "Vionic -- Alice": 12}

  sandals = {"Jenny": 7, "Karen Scott -- Daisy": 10, "Linea Paolo": 6, "Manufactore d'Essai": 7, "New York Transit": 8, "Rialto": 8, "Skechers": 8}

  sneakers = {"Amazon": 8, "Cole Haan -- Zerogrand": 8, "Converse": 9, "Kate Spade": 8, "Nike": 6, "Taylor Swift for Keds": 10, "Vintage Havana -- Babe": 10}

  earrings = {"Barbie": 6, "Black/ocher/fuchsia": 7, "Boomerang": 7, "Bottle caps": 7, "Claire's (chandelier)": 7, "Claire's (silver hearts)": 7, "Claire's (silver leaf)": 6, "Cost Plus": 7, "Elisabeth Zosseder": 7, "Ethel & Myrtle": 7, "Forever 21 (black daisies)": 6, "Forever 21 (gold daisies)": 6, "Forever 21 (gold hoops)": 7, "Forever 21 (studs)": 7, "Forever 21 (white floral)": 7, "Gold": 7, "Gold floral": 7, "Green fish": 7, "Hot Topic": 7, "I Am (black)": 7, "I Am (purple)": 7, "Idle Hands": 7, "Iran": 7, "Jade/teal/rust": 7, "Karen Hanna": 7, "Long's": 7, "Lonna and Lilly": 7, "Loren Olivia (love)": 6, "Loren Olivia (strand)": 7, "Loren Olivia (studs)": 6, "Nach": 8, "Napel (gold)": 7, "Napel (gold tree)": 6, "Pearls": 7, "Pearls w/ gold": 7, "Red fabric flower with coin": 7, "Rhinestone hearts": 7, "Richie": 7, "Silver drop": 7, "Silver fronds": 7, "Silver hearts": 6, "Silver hoops": 7, "Simply Salma": 7, "Styles": 6, "Sugar Fix (bows)": 8, "Sugar Fix (toucans)": 7, "Tilly's": 6, "Ulla Thomsen (butterfly)": 7, "Ulla Thomsen (fish)": 7, "Ulla Thomsen (moonstone)": 7, "Ulla Thomsen (pearls)": 7}

  necklaces = {"A New Day (pearls)": 4, "A New Day (rhinestone chain)": 3, "Banana Republic": 4, "Barbie": 4, "black/gold choker": 4, "black lariat": 2, "blue beads (long)": 4, "blue heart": 5, "bolo": 4, "Claire's (bee)": 4, "Cost Plus": 4, "daisy": 4, "ebony branch": 4, "dime": 4, "Dawn Fitzgibbon": 4, "Eomir": 4, "Forever 21 (black/gold)": 4, "Forever 21 (black rose)": 4, "Forever 21 (cameo)": 4, "Forever 21 (colorful)": 4, "Forever 21 (damask)": 4, "Forever 21 (bow)": 4, "Forever 21 (gold flowerbed)": 4, "Forever 21 (gray pearls)": 4, "Forever 21 (happy)":3, "Forever 21 (multi-strand pearls)": 4, "Forever 21 (pink enamel flowers": 4, "Forever 21 (pink fabric flowers)": 4, "Forever 21 (pink ribbon beads)": 4, "Forever 21 (purple)": 3, "Forever 21 (silver hearts)": 4, "Forever 21 (white/gold": 3, "gold chain": 4, "gold choker": 3, "gold dragonfly": 4, "gold heart locket": 3, "gold rose locket": 4, "Guatemala": 4, "green wooden": 4, "H&M": 3, "Ipanema": 4, "Lucorai": 4, "Macy's": 4, "Meenaz": 4, "needlepoint": 4, "pearl choker (pink)": 4, "pearl with rhinestones": 4, "pearls": 5, "pearls (Fulya)": 4, "pink beaded ribbon": 4, "rhinestone choker": 3, "seashell": 4, "silver butterfly": 4, "silver fronds": 4, "silver heart": 3, "St. Patrick's": 3, "starfish": 4, "shattering glass ceiling": 4, "Tugana Berk": 4, "Turkey (gold)": 4, "Turkey (red and black)": 5, "Ulla Thomsen (crystal)": 4, "Ulla Thomsen (moonstone)": 5, "White House Black Market": 4, "Yony (pink)": 4, "1925": 3, "1928 (black)": 4, "1928 (green)": 5}

  brooches = {"Alex": 2, "ballerina angel": 2, "black/forest rectangle": 0, "black/rectangle": 2, "bronze": 2, "dragon": 2, "E-Klah": 2, "Elmcroft": 2, "Eomir": 2, "Express": 2, "handmade mirror": 1, "Italy": 2, "Japanese postage stamp": 2, "Jos. A. Bank (black)": 2, "Jos. A. Bank (rust)": 2, "Macy's": 1, "martini glass": 0, "Modcloth": 2, "navy/red bow": 6, "Pineapple Crafts": 1, "Sanrio": 1, "sea turtle": 0, "silver bow": 3, "silver lizard": 1, "The Outrage (Feminist as Fuck)": 8, "The Outrage (Women's March)": 6, "The RealReal": 0, "Wego": 5}

  ties = {"Beymen (blue Swiss dot": 0, "Beymen (blue with links)": 0, "Beymen (gold floral)": 0, "Beymen (teal floral)": 0, "Beymen (yellow floral)": 0, "Club Room Gold": 0, "Goodfellow": 1, "Hardy Amies": 0, "Massimo Dutti": 0, "Yves Saint Laurent": 0}

  spring_scarves = {"Broadway floral": 2, "Claire's (red)": 2, "Claire's (turquoise": 2, "Claire's (white)": 2, "Diane von Furstenberg": 2, "Eda": 1, "Georgiou": 2, "Grand Canyon": 1, "H&M": 2, "Minnie Mouse": 3, "Oscr de la Renta": 3, "Project Hope": 1, "rose gold": 0, "square": 1, "Turkey (green)": 2, "Turkey (red)": 2}

  winter_scarves = {"Apt. 9": 2, "Banana Republic": 2, "Ben Berger": 2, "black cable knit": 2, "black short": 1, "Cashmink by V. Fraas": 2, "Divided by H&M": 1, "Forever 21": 1, "Gap": 2, "Old Navy": 2}

  belts = {"Apt. 9 (black)": 1, "Apt. 9 (red)": 2, "black skinny": 2, "Charter Club (red)": 2, "Forever 21 (red bow)": 2, "gold buckle": 2, "mock croc": 2, "painted burgundy": 0}

  bracelets = {"Azadeh": 5, "black rose": 4, "black/gold stretch": 4, "Cara": 4, "Contiki": 7, "Croatia": 5, "Evil Eye (brown)": 4, "Dawn Fitzgibbon": 6, "Forever 21 (black roses)": 4, "Forever 21 (white)": 4, "gold chain": 4, "I Am": 5, "jade beads": 5, "Kate Spade": 5, "Narmi": 5, "Liz Boslar": 4, "pink/purple lanyard": 4, "Richie": 5, "Sequin": 5, "silver cuff": 4, "Turkey (beads)": 4, "Turkey (Evil Eye)": 4, "turquoise/silver": 4, "We Are Pricless": 4, "white/pink/blue lanyard": 4, "Xhilaration": 4, "4Ocean": 5, "17 Jewels": 4}

  watches = {"A New Day": 5, "Adrienne": 5, "Betty Boop": 6, "GaoLo": 4, "Hello Kitty (white)": 9}

  rings = {"Aislinn Byrne": 7, "blue zircon": 7, "Broadway": 7, "Celtic wedding ring": 7, "Claire's (red)": 7, "Claire's (turquoise)": 7, "Eton": 7, "Evil Eye": 7, "Forever 21 (kiss)": 7, "Forever 21 (pearl)": 7, "Forever 21 (pixelated)": 7, "Forever 21 (purple flower)": 7, "Forever 21 (red flower)": 7, "garnet": 7, "gold ring": 7, "green painted": 7, "jet/rhinestone wings": 8, "Pier1 (aqua)": 7, "Pier1 (black)": 7, "Pier1 (pink)": 7, "Pier1 (purple)": 7, "Pier1 (red)": 7, "rhinestone leaf": 7, "Teddy Thotz": 8, "The Market NYC": 7}

  hair_brooches = {"black/white flower": 2, "Express": 4, "navy/red bow": 2, "Pineapple Crafts": 0, "silver bow": 2, "Wego": 1}

  clips = {"E-Klah": 2, "Egyptian": 3, "Gardens by the Bay (blue)": 7, "Gardens by the Bay (silver)": 8, "Goody (bronze)": 1, "Goody (pewter)": 2, "Goody (silver)": 2, "white bow": 3, "Wild Fable (aqua)": 5, "Wild Fable (cobalt)": 4, "Wild Fable (seafoam)": 4, "Yony (pink)": 7}

  ponies = {"Guatemala": 12, "pink floral scrunchie": 11, "red riboon": 2}

  headbands = {"Anna Belen (fuchsia)": 8, "Goody (black)": 2, "Goody (brown)": 0, "Goody (burgundy)": 0, "Goody (gold)": 1, "Goody (navy)": 1, "Goody (tan)": 2, "Topshop": 6}

  summer_hats = {"floral": 7, "Paradise Craft (mint)": 6, "Paradise Craft (navy)": 4, "Target": 5}

  winter_hats = {"August Accessories (black)": 5, "August Accessories (white)": 6, "August Accessories (camel)": 6, "Ben Berger (burgundy)": 5, "Ben Berger (pink)": 5, "Brette Fitzgibbon": 5, "black pom-pom beanie": 1, "Camila's": 5, "Farmers Market": 1, "INC": 5, "Nine West": 5, "Pineapple Crafts (blue)": 3, "Pineapple Crafts (pink)": 4, "pink pom-pom beanie": 1, "Scala": 5, "Toucan Collection": 6, "white beanie": 3}

  glasses = {"Amazon (black)": 1, "Amazon (leopard": 0, "Amazon (purple)": 0, "Amazon (red)": 2}

  eyeglasses = {"Glamourous Elf": 4, "Wild Fable": 2}

  sunglasses = {"A New Day (octagon)": 17, "A New Day (white)": 17, "Banana Republic (pink)": 17, "Banana Republic (white)": 17, "Foster Grant (brown)": 16, "Foster Grant -- Mireya": 17, "Foster Grant (pink)": 17, "Foster Grant (tortoiseshell)": 16, "Gardens by the Bay": 17, "GirlProps": 17, "Kiss": 16, "Locs (black)": 16, "Locs (light brown)": 23, "Locs (silver)": 17, "Malaysia": 17, "Miu Miu": 22, "Rainbow": 17, "Retro Pop (aqua)": 17, "Retro Pop (oxblood)": 16, "Retro Pop (pale blue)": 17, "Revlon": 17, "St. Mark's Place": 17, "steampunk": 17, "Target": 17, "Tod's": 17, "tortoiseshell": 16, "wayfarer": 17, "Zac Posen -- Anna": 16, "7-Eleven": 18}

  masks = {"Amazon (pink)": 7, "Amazon (tie-dye)": 6, "Amazon (white with butterflies": 5, "Amazon (white with flowers)": 6, "black lace": 11, "black sequined": 11, "Etsy": 13, "Fran Bloustein": 11, "Johnny Was (black)": 13, "Johnny Was (butterflies)": 12, "Johnny Was (gray)": 11, "Johnny Was (orchids)": 12, "Johnny Was (red)": 12, "Johnny Was (yellow)": 11, "poppies": 13, "rose gold": 11, "rose gold mesh": 5, "solid black": 12, "Some Bunny Loves You": 11, "Universal Thread (floral)": 14, "Universal Thread (pinstriped)": 14, "Universal Thread (plaid)": 12, "Wild Fable": 12}
  
  gloves = {"Alberta Ferretti": 12, "Banana Republic": 8, "Ben Berger": 12, "black": 13, "Gap": 13, "Jisen": 2, "Moschino": 12, "Sanrio": 18, "St. Patrick's": 6}

  umbrellas = {"Sanrio": 14, "Shed Rain (floral)": 14, "Shed Rain (polka dot)": 14}

  handbags = {"A New Day (basket)": 9, "A New Day (fronds)": 10, "A New Day (ice blue)": 8, "Aldo": 9, "armadillo": 11, "Aurielle": 8, "Baufooer": 8, "beaded clouds": 5, "Becky (tan)": 8, "Brette Fitzgibbon": 4, "brown/white": 8, "Charter Club": 8, "China": 8, "Chinese crossbody (red)": 8, "Christian Siriano for Payless": 8, "DKNY": 14, "Esprit": 8, "Far Nine": 9, "Frenchy": 9, "green brocade": 8, "Jennifer Moore (black)": 8, "Jennifer Moore (pink)": 8, "Juniorsweet": 9, "LC Lauren Conrad": 9, "Lougefly": 9, "Loungefly Loves Hello Kitty": 8, "Market & Spruce -- Staci": 9, "Mary Frances": 7, "MG Collection": 8, "Modcloth": 8, "Nine and Company": 8, "Nine West": 8, "Old Shanghai": 8, "panther": 8, "purple velvet": 8, "Pylones": 9, "Relic (black)": 10, "Relic (burnt red)": 9, "silver brocade": 10, "skirt": 9, "sky patent": 12, "Sonoma Life + Style": 10, "Stupa": 10, "tapestry": 8, "Tignanello (black)": 17, "Vera Bradley": 8, "Victoria's Secret": 8, "W <3 C": 10}

  totes = {"Barnes & Noble (olive)": 15, "Barnes & Noble (red/cream)": 15, "Chateau": 16,  "DKNY (silver)": 14, "DKNY (yellow)": 14, "Forgotten Shanghai": 15, "French Connection": 14, "Kate Spade": 15, "Loungefly Loves Hello Kitty": 14, "Mahi": 23, "Mossimo": 14, "Osumashi": 14, "Sanrio": 25, "Style Paris": 15, "Unicorn Collection": 14, "Urban Expressions": 15, "Urban Expressions (anchor)": 14, "Wellington & Cromwell -- Lady Croft": 16, "Wild Fable": 26}
  
  shopping_totes = {"Athleta": 10, "Bike-to-Work Day": 11, "Buffalo Exchange": 25, "Chic and Co.": 13, "Clean Conscience": 3, "Don't Ask Why": 13, "Forever 21": 13, "GQ": 2, "Hudson River Trading": 14, "Ikea (dresses)": 3, "Ikea (emerald/slate grid)": 3, "Ikea (female)": 3, "Ikea (gunmetal/white)": 3, "Ikea (leaves)": 2, "Ikea (pink/green)": 4, "Ikea (polka dot)": 3, "Ikea (tigers)": 3, "Ikea (white/black)": 3, "Ikea (white/marigold)": 2, "Marin City": 3, "Marin Sustainable Enterprise Conference": 10, "NACA": 8, "New York Coffee Festival": 20, "Pera Muzesi": 14, "Sanrio": 3, "The Market": 5, "The RealReal": 20, "The RealReal (Earth Day)": 10, "Uniqlo": 22, "Vogue": 23, "WWD": 13, "Zero Waste Marin (green)": 10, "Zero Waste Marin (white)": 5}

  cosmetics_bags = {"Lancome": 26, "Modella (filigree floral)": 12, "Modella (leaves)": 2, "Modella (lipstick)": 11, "Modella (zebra)": 16, "Sanrio": 10, "St. Patrick's": 1, "Sephora": 8, "Thrive Causemetics (pink)": 13, "Thrive Causemetics (turquoise)": 2}

  coin_purses = {"A New Day": 1, "Cath Kidston": 1, "Sephora": 1}

  evening_dresses = {"ABS by Allen Schwartz": 1, "Bullocks Wilshire": 1, "Divided by H&M (black sparkly)": 1, "Divided by H&M (purple floral)": 0, "Divided by H&M (tribal)": 3, "Forever 21 (gold cheetah)": 1, "Forever 21 (peplum)": 0, "Forever 21 (red bodycon": 0, "Forever 21 (red ruched)": 1, "Forever 21 (snow leopard)": 0, "Jessica McClintock": 0, "Know One Cares": 2, "Max Studio": 1, "Sense": 1, "Trixie": 2}

  evening_jumpsuits = {"Rules of Etiquette": 5}

  evening_tops = {"ASTR": 1, "Forever 21 (gray": 0, "Gili (gold)": 1, "Gili (light gold)": 5, "Lucca": 3}

  evening_skirts = {"Forever 21 (leopard)": 1, "Forever 21 (polka dot)": 0, "Forever 21 (striped": 0}

  evening_jackets = {"Grass": 9}

  evening_shoes = {"Dolce & Gabbana": 5, "INC (black)": 10, "Jessica Simpson (gold)": 2, "Jessica Simpson (turquoise)": 8, "Journee -- Kalani": 1, "Mossimo (lace-up)": 6, "Nina": 3, "Nuova Mokas": 4, "Willy van Rouey": 3}

  evening_accessories = {"C. Jorgensen": 1, "rose gold mesh": 4}

  evening_bags = {"abalone shell": 8, "Aunt Angela": 6, "beaded clouds": 5, "Cache": 2, "Magid (gold)": 2, "Magid (silver)": 3, "Mariell": 2, "Mary Frances": 7, "panther": 8, "purple velvet": 8, "silver brocade": 10, "Talbots": 1, "Whiting & Davis": 2}

  workout = {"All in Motion (black)": 1, "All in Motion (gray)": 1, "Cheetah": 1, "Forever 21 (black)": 1, "Forever 21 (crop top)": 2, "Forever 21 (leggings)": 2, "Forever 21 (white)": 1}

  swim_tops = {"Mossimo (black)": 4, "Mossimo (red)": 4, "Xhilaration (blue)": 2, "Xhilaration (pink)": 2}

  swim_bottoms = {"Anne Cole": 1, "eBuddy (black)": 1, "eBuddy (white)": 1, "Kona Sol": 1, "Mossimo (black)": 1, "Mossimo (black ruffled)": 3, "Xakalaka": 1, "Xhilaration (blue)": 1, "Xhilaration (pink)": 3, "Xhilaration (white)": 3}

  beach_shoes = {"Beach Mania": 4, "Havaianas": 4}

  festival = {"Amazon (tutus)": 1, "David Dalrymple (bottoms)": 0, "David Dalrymple (top)": 1, "Pride bracelet": 0}

  st_patricks_day = {"Safeway": 4}

  easter = {"Amazon (bunny ears)": 2, "basket": 2, "Peeps": 1, "Target (bunny ears)": 0}

  halloween = {"American Apparel": 0, "bat bracelet": 2, "black zip-front dress": 0, "Celebrate It": 0, "Jack-o-lantern bracelet": 2, "Pleaser": 0, "Target": 1, "Target (bat ears)": 0, "Target (cat ears)": 2, "tiara": 1, "witch hat": 2}

  christmas = {"Accutime": 7, "Born Famous": 4, "Christmas tree necklace": 2, "Claire's (bow clips)": 4, "Claire's (Santa glasses)": 5, "Claire's (snowman)": 8, "Gyothrig (green)": 6, "Gyothrig (red)": 9}

  
  # Storing the proportional surplus stat as its own variable outside get_stats allows the what_to_buy function to use it later
  dress_proportional_surplus = get_stats(dresses, max_wears)
  jumpsuit_proportional_surplus = get_stats(jumpsuits, max_wears)
  top_proportional_surplus = get_stats(tops, max_wears)
  sweater_proportional_surplus = get_stats(sweaters, max_wears)
  skirt_proportional_surplus = get_stats(skirts, max_wears)
  jeans_proportional_surplus = get_stats(jeans, max_wears)
  pants_proportional_surplus = get_stats(pants, max_wears)
  hosiery_proportional_surplus = get_stats(hosiery, max_wears)
  jacket_proportional_surplus = get_stats(jackets, max_wears)
  light_coat_proportional_surplus = get_stats(light_coats, max_wears)
  heavy_coat_proportional_surplus = get_stats(heavy_coats, max_wears)
  ankle_boots_proportional_surplus = get_stats(ankle_boots, max_wears)
  heels_proportional_surplus = get_stats(heels, max_wears)
  boots_proportional_surplus = get_stats(boots, max_wears)
  flats_proportional_surplus = get_stats(flats, max_wears)
  sandals_proportional_surplus = get_stats(sandals, max_wears)
  sneakers_proportional_surplus = get_stats(sneakers, max_wears)
  earrings_proportional_surplus = get_stats(earrings, max_wears)
  necklaces_proportional_surplus = get_stats(necklaces, max_wears)
  brooches_proportional_surplus = get_stats(brooches, max_wears)
  ties_proportional_surplus = get_stats(ties, max_wears)
  spring_scarves_proportional_surplus = get_stats(spring_scarves, max_wears)
  winter_scarves_proportional_surplus = get_stats(winter_scarves, max_wears)
  belts_proportional_surplus = get_stats(belts, max_wears)
  bracelets_proportional_surplus = get_stats(bracelets, max_wears)
  watches_proportional_surplus = get_stats(watches, max_wears)
  rings_proportional_surplus = get_stats(rings, max_wears)
  hair_brooches_proportional_surplus = get_stats(hair_brooches, max_wears)
  clips_proportional_surplus = get_stats(clips, max_wears)
  ponies_proportional_surplus = get_stats(ponies, max_wears)
  headbands_proportional_surplus = get_stats(headbands, max_wears)
  summer_hats_proportional_surplus = get_stats(summer_hats, max_wears)
  winter_hats_proportional_surplus = get_stats(winter_hats, max_wears)
  glasses_proportional_surplus = get_stats(glasses, max_wears)
  eyeglasses_proportional_surplus = get_stats(eyeglasses, max_wears)
  sunglasses_proportional_surplus = get_stats(sunglasses, max_wears)
  masks_proportional_surplus = get_stats(masks, max_wears)
  gloves_proportional_surplus = get_stats(gloves, max_wears)
  umbrellas_proportional_surplus = get_stats(umbrellas, max_wears)
  handbags_proportional_surplus = get_stats(handbags, max_wears)
  totes_proportional_surplus = get_stats(totes, max_wears)
  shopping_totes_proportional_surplus = get_stats(shopping_totes, max_wears)
  cosmetics_bags_proportional_surplus = get_stats(cosmetics_bags, max_wears)
  coin_purses_proportional_surplus = get_stats(coin_purses, max_wears)
  evening_dresses_proportional_surplus = get_stats(evening_dresses, max_wears)
  evening_jumpsuits_proportional_surplus = get_stats(evening_jumpsuits, max_wears)
  evening_tops_proportional_surplus = get_stats(evening_tops, max_wears)
  evening_skirts_proportional_surplus = get_stats(evening_skirts, max_wears)
  evening_jackets_proportional_surplus = get_stats(evening_jackets, max_wears)
  evening_shoes_proportional_surplus = get_stats(evening_shoes, max_wears)
  evening_accessories_proportional_surplus = get_stats(evening_accessories, max_wears)
  evening_bags_proportional_surplus = get_stats(evening_bags, max_wears)
  workout_proportional_surplus = get_stats(workout, max_wears)
  swim_tops_proportional_surplus = get_stats(swim_tops, max_wears)
  swim_bottoms_proportional_surplus = get_stats(swim_bottoms, max_wears)
  beach_shoes_proportional_surplus = get_stats(beach_shoes, max_wears)
  festival_proportional_surplus = get_stats(festival, max_wears)
  st_patricks_day_proportional_surplus = get_stats(st_patricks_day, max_wears)
  easter_proportional_surplus = get_stats(easter, max_wears)
  halloween_proportional_surplus = get_stats(halloween, max_wears)
  christmas_proportional_surplus = get_stats(christmas, max_wears)
  
  # Printing get_stats for each category, instead of combining them into one get_stats function that prints all the categories, in order to have a different string as the header for every category
  print("Dresses \n")
  get_stats(dresses, max_wears)

  print("Jumpsuits\n")
  get_stats(jumpsuits, max_wears)
  
  print("Tops\n")
  get_stats(tops, max_wears)

  print("Sweaters\n")
  get_stats(sweaters, max_wears)

  print("Skirts\n")
  get_stats(skirts, max_wears)

  print("Jeans\n")
  get_stats(jeans, max_wears)

  print("Pants\n")
  get_stats(pants, max_wears)

  print("Hosiery\n")
  get_stats(hosiery, max_wears)

  print("Jackets\n")
  get_stats(jackets, max_wears)

  print("Light Coats\n")
  get_stats(light_coats, max_wears)

  print("Heavy Coats\n")
  get_stats(heavy_coats, max_wears)

  print("Ankle Boots\n")
  get_stats(ankle_boots, max_wears)

  print("Heels\n")
  get_stats(heels, max_wears)

  print("Boots\n")
  get_stats(boots, max_wears)

  print("Flats\n")
  get_stats(flats, max_wears)
  
  print("Sandals\n")
  get_stats(sandals, max_wears)

  print("Sneakers\n")
  get_stats(sneakers, max_wears)

  print("Earrings\n")
  get_stats(earrings, max_wears)

  print("Necklaces\n")
  get_stats(necklaces, max_wears)

  print("Brooches\n")
  get_stats(brooches, max_wears)

  print("Ties\n")
  get_stats(ties, max_wears)

  print("Spring Scarves\n")
  get_stats(spring_scarves, max_wears)

  print("Winter Scarves\n")
  get_stats(winter_scarves, max_wears)

  print("Bracelets\n")
  get_stats(bracelets, max_wears)

  print("Watches\n")
  get_stats(watches, max_wears)

  print("Rings\n")
  get_stats(rings, max_wears)

  print("Hair Brooches\n")
  get_stats(hair_brooches, max_wears)

  print("Clips\n")
  get_stats(clips, max_wears)

  print("Ponies\n")
  get_stats(ponies, max_wears)

  print("Headbands\n")
  get_stats(headbands, max_wears)

  print("Summer Hats\n")
  get_stats(summer_hats, max_wears)

  print("Winter Hats\n")
  get_stats(winter_hats, max_wears)

  print("Glasses\n")
  get_stats(glasses, max_wears)

  print("Eyeglasses\n")
  get_stats(eyeglasses, max_wears)

  print("Sunglasses\n")
  get_stats(sunglasses, max_wears)

  print("Masks\n")
  get_stats(masks, max_wears)

  print("Gloves\n")
  get_stats(gloves, max_wears)

  print("Umbrellas\n")
  get_stats(umbrellas, max_wears)

  print("Handbags\n")
  get_stats(handbags, max_wears)

  print("Totes\n")
  get_stats(totes, max_wears)

  print("Shopping Totes\n")
  get_stats(shopping_totes, max_wears)

  print("Cosmetics Bags\n")
  get_stats(cosmetics_bags, max_wears)

  print("Coin Purses\n")
  get_stats(coin_purses, max_wears)

  print("Evening Dresses\n")
  get_stats(evening_dresses, max_wears)

  print("Evening Jumpsuits\n")
  get_stats(evening_jumpsuits, max_wears)

  print("Evening Tops\n")
  get_stats(evening_tops, max_wears)

  print("Evening Skirts\n")
  get_stats(coin_purses, max_wears)

  print("Evening Jackets\n")
  get_stats(coin_purses, max_wears)

  print("Evening Shoes\n")
  get_stats(coin_purses, max_wears)

  print("Evening Accessories\n")
  get_stats(coin_purses, max_wears)

  print("Evening Bags\n")
  get_stats(coin_purses, max_wears)

  print("Workout\n")
  get_stats(workout, max_wears)

  print("Swim Tops\n")
  get_stats(swim_tops, max_wears)

  print("Swim Bottoms\n")
  get_stats(swim_bottoms, max_wears)

  print("Beach Shoes\n")
  get_stats(beach_shoes, max_wears)

  print("Festival\n")
  get_stats(festival, max_wears)

  print("St. Patrick's Day\n")
  get_stats(st_patricks_day, max_wears)

  print("Easter\n")
  get_stats(easter, max_wears)

  print("Halloween\n")
  get_stats(halloween, max_wears)

  print("Christmas\n")
  get_stats(christmas, max_wears)
  
  # Calls each item of a sample outfit
  print("Outfit 1\n")
  outfit_generator(1, simple_sort(dresses), simple_sort(jackets), simple_sort(heels), simple_sort(earrings), simple_sort(necklaces), simple_sort(bracelets), simple_sort(watches), simple_sort(rings), simple_sort(hair_brooches), simple_sort(sunglasses), simple_sort(masks), simple_sort(handbags), simple_sort(shopping_totes), simple_sort(cosmetics_bags))
  print("\n") # Creates space between sample outfits for readability
  
  # Calls each item of a different sample outfit
  print("Outfit 2\n")
  outfit_generator(1, simple_sort(tops), simple_sort(skirts), simple_sort(light_coats), simple_sort(flats), simple_sort(spring_scarves), simple_sort(masks), simple_sort(totes))
  print("\n")
  
  # Calls each item of a different sample outfit
  print("Outfit 3\n")
  outfit_generator(1, simple_sort(sweaters), simple_sort(pants), simple_sort(heavy_coats), simple_sort(boots), simple_sort(winter_scarves), simple_sort(winter_hats), simple_sort(masks), simple_sort(gloves), simple_sort(umbrellas), simple_sort(totes))
  print("\n")

   # Calls each item of a different sample outfit
  print("Outfit 4\n")
  outfit_generator(1, simple_sort(tops), simple_sort(jeans), simple_sort(heavy_coats), simple_sort(sneakers), simple_sort(ponies), simple_sort(masks), simple_sort(handbags), simple_sort(coin_purses))
  print("\n")

  print("Outfit 5\n")
  outfit_generator(1, simple_sort(jumpsuits), simple_sort(ankle_boots), simple_sort(brooches), simple_sort(eyeglasses), simple_sort(masks), simple_sort(handbags)) 
  print("\n")

  print("Outfit 6\n")
  outfit_generator(1, simple_sort(dresses), simple_sort(hosiery), simple_sort(flats), simple_sort(belts), simple_sort(headbands), simple_sort(glasses), simple_sort(masks), simple_sort(handbags))
  print("\n")

  print("Outfit 7\n")
  outfit_generator(0, simple_sort(tops), simple_sort(pants), simple_sort(flats), simple_sort(ties), simple_sort(masks), simple_sort(totes))
  print("\n")

  print("Outfit 8\n")
  outfit_generator(0, simple_sort(swim_tops), simple_sort(swim_bottoms), simple_sort(beach_shoes), simple_sort(summer_hats), simple_sort(shopping_totes))
  print("\n")

  print("Outfit 9\n")
  outfit_generator(0, simple_sort(dresses), simple_sort(sandals), simple_sort(sunglasses), simple_sort(masks), simple_sort(handbags))
  print("\n")

  print("Outfit 10\n")
  outfit_generator(1, simple_sort(evening_dresses), simple_sort(evening_jackets), simple_sort(evening_shoes), simple_sort(evening_accessories), simple_sort(evening_bags))
  print("\n")

  print("Outfit 11\n")
  outfit_generator(1, simple_sort(evening_tops), simple_sort(evening_skirts), simple_sort(evening_shoes), simple_sort(evening_bags))
  print("\n")

  print("Outfit 12\n")
  outfit_generator(0, simple_sort(evening_jumpsuits), simple_sort(evening_shoes), simple_sort(evening_bags))
  print("\n")
  
  categories = {"dresses": dress_proportional_surplus, "jumpsuits": jumpsuit_proportional_surplus, "tops": top_proportional_surplus, "sweaters": sweater_proportional_surplus, "skirts": skirt_proportional_surplus, "jeans": jeans_proportional_surplus, "pants": pants_proportional_surplus, "hosiery": hosiery_proportional_surplus, "jackets": jacket_proportional_surplus, "light coats": light_coat_proportional_surplus, "heavy coats": heavy_coat_proportional_surplus, "ankle boots": ankle_boots_proportional_surplus, "heels": heels_proportional_surplus, "boots": boots_proportional_surplus, "flats": flats_proportional_surplus, "sandals": sandals_proportional_surplus, "sneakers": sneakers_proportional_surplus, "earrings": earrings_proportional_surplus, "necklaces": necklaces_proportional_surplus, "brooches": brooches_proportional_surplus, "ties": ties_proportional_surplus, "spring scarves": spring_scarves_proportional_surplus, "winter scarves": winter_scarves_proportional_surplus, "belts": belts_proportional_surplus, "bracelets": bracelets_proportional_surplus, "watches": watches_proportional_surplus, "rings": rings_proportional_surplus, "hair brooches": hair_brooches_proportional_surplus, "clips": clips_proportional_surplus, "ponies": ponies_proportional_surplus, "headbands": headbands_proportional_surplus, "summer hats": summer_hats_proportional_surplus, "winter hats": winter_hats_proportional_surplus, "glasses": glasses_proportional_surplus, "eyeglasses": eyeglasses_proportional_surplus, "sunglasses": sunglasses_proportional_surplus, "masks": masks_proportional_surplus, "gloves": gloves_proportional_surplus, "umbrellas": umbrellas_proportional_surplus,"handbags": handbags_proportional_surplus, "totes": totes_proportional_surplus, "shopping totes": shopping_totes_proportional_surplus, "cosmetics bags": cosmetics_bags_proportional_surplus, "coin purses": coin_purses_proportional_surplus, "evening dresses": evening_dresses_proportional_surplus, "evening tops": evening_tops_proportional_surplus, "evening skirts": evening_skirts_proportional_surplus, "evening jackets": evening_jackets_proportional_surplus, "evening shoes": evening_shoes_proportional_surplus, "evening accessories": evening_accessories_proportional_surplus, "evening bags": evening_bags_proportional_surplus, "workout": workout_proportional_surplus, "swim tops": swim_tops_proportional_surplus, "swim bottoms": swim_bottoms_proportional_surplus, "beach shoes": beach_shoes_proportional_surplus, "festival": festival_proportional_surplus, "St. Patrick's Day": st_patricks_day_proportional_surplus, "Easter": easter_proportional_surplus, "Halloween": halloween_proportional_surplus, "Christmas": christmas_proportional_surplus}
  
  what_to_buy(categories) # Lists new categories to buy from in order of priority. That said, if there is a surplus and not a deficit (i.e., the "surplus" variable is positive), then the user doesn't need anything new! 

if __name__ == "__main__":
    main()