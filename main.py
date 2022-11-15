from dataset import * 
from datetime import date
from math import ceil, floor
from random import choice

def num_of_days(date1, date2):
    days_elapsed = (date2 - date1).days
    return days_elapsed

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

# Option 1 for creating outfits: using the least-worn items
def get_stats(dict1, dict2, max_wears):
  vals1 = [v for _, v in dict1.items()]
  vals2 = [v for _, v in dict2.items()]
  
  total_wears = sum(vals1) + sum(vals2)
  minimum_requirement = ceil(total_wears / max_wears)
  # Minimum number of items from a category required to not wear the same item twice per two-month period (or other length of time chosen by the user). Ceil is a conservative measure of how many items the user needs. For example, if they technically need half an item, to say they need 1 item instead of 0 errs on the side of caution. 
  for key, value in dict1.items():
    if value == "None":
      average = total_wears / len(dict2)
      surplus = floor(-minimum_requirement)
    else:
      average = round(total_wears / (len(dict1) + len(dict2)))
      surplus = floor(len(dict1) - minimum_requirement) # How many more items the user has versus what they need. A deficit would be displayed as a negative surplus. Floor function instead of rounding because fashion items are discrete, and floor is a more conservative measure than ceil (i.e., if you technically need half an item, having a -1 surplus instead of a 0 surplus -- that is, needing 1 item instead of 0 items -- is erring on the side of caution).
    proportional_surplus = round(surplus / minimum_requirement, 2) 
  # Setting floating-point number precision to 2 decimal places for readability
  # The surplus as a proportion of the minimum items required is a standardized approach that weighs, for example, having two pairs of gloves when you only need one differently from having 10 dresses when you only need nine, despite the surpluses in each example being the same number of items.
  print(get_items(dict1))
  for key, value in dict1.items():
    if value == "None":
      print("Total Items: 0")
    else:
      print("Total Items: ", len(dict1))
      break
  print("Total Wears: ", total_wears)
  print("Average Wears: ", average)
  print("Minimum Requirement: ", minimum_requirement)
  print("Surplus: ", surplus)
  print("Proportional Surplus: ", proportional_surplus, "\n")
  print(simple_sort(dict1), "\n")
  return proportional_surplus

# Option 2 for creating outfits: random items
def outfit_generator(max_wears, *args): #which categories to include in the outfit
  for arg in args:
    item = choice(list(arg.items())) #selects a random item from each category
    print(item) 
  print("Max Wears: ", max_wears) #user can compare each item's wears to max_wears and choose not to wear those items that have already been worn the maximum number of times 
    
def what_to_buy(dict):
  sort = sorted(dict.items(), key = lambda x: x[1], reverse = False)
  print("What to Buy Next: ", sort)

def main():
  NONREPEAT_PERIOD = 62 # Goal of not wearing the same item more than once per two-month period, on average. User can set their nonrepeat period of choice.
  days_elapsed = num_of_days(date(2018, 1, 1), date.today()) # Enters the date user started tracking wears and today's date
  print("Days Elapsed: ", days_elapsed)
  print("Nonrepeat Period: ", NONREPEAT_PERIOD, " days")
  max_wears = ceil(days_elapsed / NONREPEAT_PERIOD) # Maximum number of times the same item could be worn during the entire period, if it was worn only an average of once per two-month period
  print(max_wears)

  # Storing the proportional surplus stat as its own variable outside get_stats allows the what_to_buy function to use it later
  # Including items that were worn, but are no longer available to be worn now (damaged, lost, etc.) is important for accuracy of the number of wears in a category and the number of new items needed (i.e., how many unavailable items need to be replaced)
  dress_proportional_surplus = get_stats(dresses, dresses_not_available, max_wears)
  jumpsuit_proportional_surplus = get_stats(jumpsuits, jumpsuits_not_available, max_wears)
  top_proportional_surplus = get_stats(tops, tops_not_available, max_wears)
  sweater_proportional_surplus = get_stats(sweaters, sweaters_not_available, max_wears)
  skirt_proportional_surplus = get_stats(skirts, skirts_not_available, max_wears)
  shorts_proportional_surplus = get_stats(shorts, shorts_not_available, max_wears)
  jeans_proportional_surplus = get_stats(jeans, jeans_not_available, max_wears)
  pants_proportional_surplus = get_stats(pants, pants_not_available, max_wears)
  hosiery_proportional_surplus = get_stats(hosiery, hosiery_not_available, max_wears)
  jacket_proportional_surplus = get_stats(jackets, jackets_not_available, max_wears)
  light_coat_proportional_surplus = get_stats(light_coats, light_coats_not_available, max_wears)
  heavy_coat_proportional_surplus = get_stats(heavy_coats, heavy_coats_not_available, max_wears)
  ankle_boots_proportional_surplus = get_stats(ankle_boots, ankle_boots_not_available, max_wears)
  heels_proportional_surplus = get_stats(heels, heels_not_available, max_wears)
  boots_proportional_surplus = get_stats(boots, boots_not_available, max_wears)
  flats_proportional_surplus = get_stats(flats, flats_not_available, max_wears)
  sandals_proportional_surplus = get_stats(sandals, sandals_not_available, max_wears)
  sneakers_proportional_surplus = get_stats(sneakers, sneakers_not_available, max_wears)
  earrings_proportional_surplus = get_stats(earrings, earrings_not_available, max_wears)
  necklaces_proportional_surplus = get_stats(necklaces, necklaces_not_available, max_wears)
  brooches_proportional_surplus = get_stats(brooches, brooches_not_available, max_wears)
  ties_proportional_surplus = get_stats(ties, ties_not_available, max_wears)
  spring_scarves_proportional_surplus = get_stats(spring_scarves, spring_scarves_not_available, max_wears)
  winter_scarves_proportional_surplus = get_stats(winter_scarves, winter_scarves_not_available, max_wears)
  belts_proportional_surplus = get_stats(belts, belts_not_available, max_wears)
  bracelets_proportional_surplus = get_stats(bracelets, bracelets_not_available, max_wears)
  watches_proportional_surplus = get_stats(watches, watches_not_available, max_wears)
  rings_proportional_surplus = get_stats(rings, rings_not_available, max_wears)
  hair_brooches_proportional_surplus = get_stats(hair_brooches, hair_brooches_not_available, max_wears)
  clips_proportional_surplus = get_stats(clips, clips_not_available, max_wears)
  ponies_proportional_surplus = get_stats(ponies, ponies_not_available, max_wears)
  headbands_proportional_surplus = get_stats(headbands, headbands_not_available, max_wears)
  summer_hats_proportional_surplus = get_stats(summer_hats, summer_hats_not_available, max_wears)
  winter_hats_proportional_surplus = get_stats(winter_hats, winter_hats_not_available, max_wears)
  glasses_proportional_surplus = get_stats(glasses, glasses_not_available, max_wears)
  eyeglasses_proportional_surplus = get_stats(eyeglasses, eyeglasses_not_available, max_wears)
  sunglasses_proportional_surplus = get_stats(sunglasses, sunglasses_not_available, max_wears)
  masks_proportional_surplus = get_stats(masks, masks_not_available, max_wears)
  gloves_proportional_surplus = get_stats(gloves, gloves_not_available, max_wears)
  umbrellas_proportional_surplus = get_stats(umbrellas, umbrellas_not_available, max_wears)
  handbags_proportional_surplus = get_stats(handbags, handbags_not_available, max_wears)
  totes_proportional_surplus = get_stats(totes, totes_not_available, max_wears)
  shopping_totes_proportional_surplus = get_stats(shopping_totes, shopping_totes_not_available, max_wears)
  wallets_proportional_surplus = get_stats (wallets, wallets_not_available, max_wears)
  cosmetics_bags_proportional_surplus = get_stats(cosmetics_bags, cosmetics_bags_not_available, max_wears)
  coin_purses_proportional_surplus = get_stats(coin_purses, coin_purses_not_available, max_wears)
  evening_dresses_proportional_surplus = get_stats(evening_dresses, evening_dresses_not_available, max_wears)
  evening_jumpsuits_proportional_surplus = get_stats(evening_jumpsuits, evening_jumpsuits_not_available, max_wears)
  evening_tops_proportional_surplus = get_stats(evening_tops, evening_tops_not_available, max_wears)
  evening_skirts_proportional_surplus = get_stats(evening_skirts, evening_skirts_not_available, max_wears)
  evening_jackets_proportional_surplus = get_stats(evening_jackets, evening_jackets_not_available, max_wears)
  evening_shoes_proportional_surplus = get_stats(evening_shoes, evening_shoes_not_available, max_wears)
  evening_accessories_proportional_surplus = get_stats(evening_accessories, evening_accessories_not_available, max_wears)
  evening_bags_proportional_surplus = get_stats(evening_bags, evening_bags_not_available, max_wears)
  workout_proportional_surplus = get_stats(workout, workout_not_available, max_wears)
  swim_tops_proportional_surplus = get_stats(swim_tops, swim_tops_not_available, max_wears)
  swim_bottoms_proportional_surplus = get_stats(swim_bottoms, swim_bottoms_not_available, max_wears)
  beach_shoes_proportional_surplus = get_stats(beach_shoes, beach_shoes_not_available, max_wears)
  festival_proportional_surplus = get_stats(festival, festival_not_available, max_wears)
  st_patricks_day_proportional_surplus = get_stats(st_patricks_day, st_patricks_day_not_available, max_wears)
  easter_proportional_surplus = get_stats(easter, easter_not_available, max_wears)
  halloween_proportional_surplus = get_stats(halloween, halloween_not_available, max_wears)
  christmas_proportional_surplus = get_stats(christmas, christmas_not_available, max_wears)
  
  # # Printing get_stats for each category, instead of combining them into one get_stats function that prints all the categories, in order to have a different string as the header for every category
  print("Dresses \n")
  get_stats(dresses, dresses_not_available, max_wears)

  print("Jumpsuits\n")
  get_stats(jumpsuits, jumpsuits_not_available, max_wears)
  
  print("Tops\n")
  get_stats(tops, tops_not_available, max_wears)

  print("Sweaters\n")
  get_stats(sweaters, sweaters_not_available, max_wears)

  print("Skirts\n")
  get_stats(skirts, skirts_not_available, max_wears)

  print("Shorts\n")
  get_stats(shorts, shorts_not_available, max_wears)

  print("Jeans\n")
  get_stats(jeans, jeans_not_available, max_wears)

  print("Pants\n")
  get_stats(pants, pants_not_available, max_wears)

  print("Hosiery\n")
  get_stats(hosiery, hosiery_not_available, max_wears)

  print("Jackets\n")
  get_stats(jackets, jackets_not_available, max_wears)

  print("Light Coats\n")
  get_stats(light_coats, light_coats_not_available, max_wears)

  print("Heavy Coats\n")
  get_stats(heavy_coats, heavy_coats_not_available, max_wears)

  print("Boots\n")
  get_stats(boots, boots_not_available, max_wears)

  print("Ankle Boots\n")
  get_stats(ankle_boots, ankle_boots_not_available, max_wears)

  print("Heels\n")
  get_stats(heels, heels_not_available, max_wears)

  print("Flats\n")
  get_stats(flats, flats_not_available, max_wears)
  
  print("Sandals\n")
  get_stats(sandals, sandals_not_available, max_wears)

  print("Sneakers\n")
  get_stats(sneakers, sneakers_not_available, max_wears)

  print("Earrings\n")
  get_stats(earrings, earrings_not_available, max_wears)

  print("Necklaces\n")
  get_stats(necklaces, necklaces_not_available, max_wears)

  print("Brooches\n")
  get_stats(brooches, brooches_not_available, max_wears)

  print("Ties\n")
  get_stats(ties, ties_not_available, max_wears)

  print("Spring Scarves\n")
  get_stats(spring_scarves, spring_scarves_not_available, max_wears)

  print("Winter Scarves\n")
  get_stats(winter_scarves, winter_scarves, max_wears)

  print("Belts\n")
  get_stats(belts, belts_not_available, max_wears)

  print("Bracelets\n")
  get_stats(bracelets, bracelets_not_available, max_wears)

  print("Watches\n")
  get_stats(watches, watches_not_available, max_wears)

  print("Rings\n")
  get_stats(rings, rings_not_available, max_wears)

  print("Hair Brooches\n")
  get_stats(hair_brooches, hair_brooches_not_available, max_wears)

  print("Clips\n")
  get_stats(clips, clips_not_available, max_wears)

  print("Ponies\n")
  get_stats(ponies, ponies_not_available, max_wears)

  print("Headbands\n")
  get_stats(headbands, headbands_not_available, max_wears)

  print("Summer Hats\n")
  get_stats(summer_hats, summer_hats_not_available, max_wears)

  print("Winter Hats\n")
  get_stats(winter_hats, winter_hats_not_available, max_wears)

  print("Glasses\n")
  get_stats(glasses, glasses_not_available, max_wears)

  print("Eyeglasses\n")
  get_stats(eyeglasses, eyeglasses_not_available, max_wears)

  print("Sunglasses\n")
  get_stats(sunglasses, sunglasses_not_available, max_wears)

  print("Masks\n")
  get_stats(masks, masks_not_available, max_wears)

  print("Gloves\n")
  get_stats(gloves, gloves_not_available, max_wears)

  print("Umbrellas\n")
  get_stats(umbrellas, umbrellas_not_available, max_wears)

  print("Handbags\n")
  get_stats(handbags, handbags_not_available, max_wears)

  print("Totes\n")
  get_stats(totes, totes_not_available, max_wears)

  print("Shopping Totes\n")
  get_stats(shopping_totes, shopping_totes_not_available, max_wears)

  print("Wallets\n")
  get_stats(wallets, wallets_not_available, max_wears)
  
  print("Cosmetics Bags\n")
  get_stats(cosmetics_bags, cosmetics_bags_not_available, max_wears)

  print("Coin Purses\n")
  get_stats(coin_purses, coin_purses_not_available, max_wears)

  print("Evening Dresses\n")
  get_stats(evening_dresses, evening_dresses_not_available, max_wears)

  print("Evening Jumpsuits\n")
  get_stats(evening_jumpsuits, evening_jumpsuits_not_available, max_wears)

  print("Evening Tops\n")
  get_stats(evening_tops, evening_tops_not_available, max_wears)

  print("Evening Skirts\n")
  get_stats(evening_skirts, evening_skirts_not_available, max_wears)

  print("Evening Jackets\n")
  get_stats(evening_jackets, evening_jackets_not_available, max_wears)

  print("Evening Shoes\n")
  get_stats(evening_shoes, evening_shoes_not_available, max_wears)

  print("Evening Accessories\n")
  get_stats(evening_accessories, evening_accessories_not_available, max_wears)

  print("Evening Bags\n")
  get_stats(evening_bags, evening_bags_not_available, max_wears)

  print("Workout\n")
  get_stats(workout, workout_not_available, max_wears)

  print("Swim Tops\n")
  get_stats(swim_tops, swim_tops_not_available, max_wears)

  print("Swim Bottoms\n")
  get_stats(swim_bottoms, swim_bottoms_not_available, max_wears)

  print("Beach Shoes\n")
  get_stats(beach_shoes, beach_shoes_not_available, max_wears)

  print("Festival\n")
  get_stats(festival, festival_not_available, max_wears)

  print("St. Patrick's Day\n")
  get_stats(st_patricks_day, st_patricks_day_not_available, max_wears)

  print("Easter\n")
  get_stats(easter, easter_not_available, max_wears)

  print("Halloween\n")
  get_stats(halloween, halloween_not_available, max_wears)

  print("Christmas\n")
  get_stats(christmas, christmas_not_available, max_wears)
  
  print("Outfit 1\n")
  outfit_generator(max_wears, dresses, jackets, heels, earrings, necklaces, bracelets, watches, rings, hair_brooches, sunglasses, masks, totes)
  print("\n") # Creates space between sample outfits for readability
  
  print("Outfit 2\n")
  outfit_generator(max_wears, tops, skirts, light_coats, flats, earrings, spring_scarves, sunglasses, masks, totes)
  print("\n")
  
  print("Outfit 3\n")
  outfit_generator(max_wears, sweaters, pants, heavy_coats, boots, earrings, winter_scarves, winter_hats, sunglasses, masks, gloves, umbrellas, totes)
  print("\n")

  print("Outfit 4\n")
  outfit_generator(max_wears, tops, jeans, heavy_coats, sneakers, earrings, ponies, sunglasses, masks, handbags, coin_purses)
  print("\n")

  print("Outfit 5\n")
  outfit_generator(max_wears, jumpsuits, ankle_boots, earrings, brooches, eyeglasses, masks, handbags)
  print("\n")

  print("Outfit 6\n")
  outfit_generator(max_wears, dresses, hosiery, flats, earrings, belts, headbands, glasses, sunglasses, masks, handbags)
  print("\n")

  print("Outfit 7\n")
  outfit_generator(max_wears, tops, pants, flats, earrings, ties, sunglasses, masks, totes)
  print("\n")

  print("Outfit 8\n")
  outfit_generator(max_wears, swim_tops, swim_bottoms, beach_shoes, summer_hats, sunglasses, shopping_totes)
  print("\n")

  print("Outfit 9\n")
  outfit_generator(max_wears, dresses, sandals, earrings, sunglasses, masks, handbags)
  print("\n")

  print("Outfit 10\n")
  outfit_generator(max_wears, evening_dresses, evening_jackets, evening_shoes, evening_accessories, evening_bags)
  print("\n")

  print("Outfit 11\n")
  outfit_generator(max_wears, evening_tops, evening_skirts, evening_shoes, evening_bags)
  print("\n")

  print("Outfit 12\n")
  outfit_generator(max_wears, evening_jumpsuits, evening_shoes, evening_bags)
  print("\n")
  
  categories = {"dresses": dress_proportional_surplus, "jumpsuits": jumpsuit_proportional_surplus, "tops": top_proportional_surplus, "sweaters": sweater_proportional_surplus, "skirts": skirt_proportional_surplus, "shorts": shorts_proportional_surplus, "jeans": jeans_proportional_surplus, "pants": pants_proportional_surplus, "hosiery": hosiery_proportional_surplus, "jackets": jacket_proportional_surplus, "light coats": light_coat_proportional_surplus, "heavy coats": heavy_coat_proportional_surplus, "ankle boots": ankle_boots_proportional_surplus, "heels": heels_proportional_surplus, "boots": boots_proportional_surplus, "flats": flats_proportional_surplus, "sandals": sandals_proportional_surplus, "sneakers": sneakers_proportional_surplus, "earrings": earrings_proportional_surplus, "necklaces": necklaces_proportional_surplus, "brooches": brooches_proportional_surplus, "ties": ties_proportional_surplus, "spring scarves": spring_scarves_proportional_surplus, "winter scarves": winter_scarves_proportional_surplus, "belts": belts_proportional_surplus, "bracelets": bracelets_proportional_surplus, "watches": watches_proportional_surplus, "rings": rings_proportional_surplus, "hair brooches": hair_brooches_proportional_surplus, "clips": clips_proportional_surplus, "ponies": ponies_proportional_surplus, "headbands": headbands_proportional_surplus, "summer hats": summer_hats_proportional_surplus, "winter hats": winter_hats_proportional_surplus, "glasses": glasses_proportional_surplus, "eyeglasses": eyeglasses_proportional_surplus, "sunglasses": sunglasses_proportional_surplus, "masks": masks_proportional_surplus, "gloves": gloves_proportional_surplus, "umbrellas": umbrellas_proportional_surplus,"handbags": handbags_proportional_surplus, "totes": totes_proportional_surplus, "shopping totes": shopping_totes_proportional_surplus, "wallets": wallets_proportional_surplus, "cosmetics bags": cosmetics_bags_proportional_surplus, "coin purses": coin_purses_proportional_surplus, "evening dresses": evening_dresses_proportional_surplus, "evening tops": evening_tops_proportional_surplus, "evening skirts": evening_skirts_proportional_surplus, "evening jackets": evening_jackets_proportional_surplus, "evening shoes": evening_shoes_proportional_surplus, "evening accessories": evening_accessories_proportional_surplus, "evening bags": evening_bags_proportional_surplus, "workout": workout_proportional_surplus, "swim tops": swim_tops_proportional_surplus, "swim bottoms": swim_bottoms_proportional_surplus, "beach shoes": beach_shoes_proportional_surplus, "festival": festival_proportional_surplus, "St. Patrick's Day": st_patricks_day_proportional_surplus, "Easter": easter_proportional_surplus, "Halloween": halloween_proportional_surplus, "Christmas": christmas_proportional_surplus}
  
  what_to_buy(categories) # Lists new categories to buy from in order of priority. That said, if there is a surplus and not a deficit (i.e., the "surplus" variable is positive), then the user doesn't need anything new! 

if __name__ == "__main__":
    main()
