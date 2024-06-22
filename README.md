Outfit generator and wardrobe management tool. Keeps track of the number of wears of each item, with two goals: not wearing the same item more than once every two months, on average, and wearing every item in a category an equal number of times. 

What this program does:

-- Stores data on number of wears for each item, grouped into 56 categories (e.g., dresses, tops)

-- Assembles combinations of 3-20 items to generate an outfit, based on which items have been worn the least. 

-- Prioritizes which categories to shop for by calculating: the frequency each item category is worn measured against a target frequency, the surplus number of items versus the minimum requirement to not exceed the target frequency, and the surplus as a percentage of the minimum requirement, then ranks the surpluses in ascending order. When there is a surplus, the user does not need to buy any more items. When there is a deficit, the user would need to buy more items to not exceed the target frequency. 

What this program entails:

-- Coded in Python

-- Wears data stored in alphabetical order within categories to facilitate easy daily updates following each wear

-- num_of_days function: keeps track of how many days have elapsed since the wears data began

-- get_items function: retrieves the item(s) from a category that has/have been worn the least

-- simple_sort function: sorts the items in a category in order from least worn to most worn

-- get_stats function: for a given category, calculates: the total wears, average wears, minimum number of items required to not exceed the target frequency, item surplus (or deficit; the deficit is expressed as a negative surplus), and the surplus or deficit as a proportion of the minimum requirement

-- outfit_generator function: from a group of user-selected categories, pulls the items that have been worn the least. If the items that have been worn the least do not make a good outfit together, the user can try a different index (e.g., the second-least worn item from each category).

-- what_to_buy function: ranks all categories in ascending order by proportional surplus to identify which categories need additional items the most

Further applications:

-- More outfit generation data to calculate the probability of generating an outfit the user likes, and of needing a second try, third try, and so on

-- Using object-oriented programming, or creating a dictionary for each individual item, to keep track of additional values like: date last worn, place/event/occasion last worn, need for repairs, good for work, and so on

Sample output (outfit generator):

Outfit 1
(‘Xhilaration (maroon)’, 2) [dress, worn twice]
(‘INC’, 12) [jacket, worn 12 times]
(‘LifeStride (gold)’, 14) [heels, worn 14 times]
(‘Silver drop’, 11) [earrings, worn 11 times]
(‘dime’, 5) [necklace, worn 5 times]
(‘Forever 21 (white)’, 10) [bracelet, worn 10 times]
(‘A New Day’, 10) [watch, worn 10 times]
(‘Forever 21 (pixelated)’, 15) [ring, worn 15 times]
(‘Wego’, 2) [hair brooch, worn twice]
(‘Foster Grant (brown)’, 29) [sunglasses, worn 29 times]
(‘Style Paris’, 28) [tote bag, worn 28 times]
[Example user (me) would replace the jacket and remove the bracelet and watch, then wear it on a fall day.]

Outfit 2
(‘Kim and Cami’, 6) [top]
(‘Desigual’, 14) [skirt]
(‘Forever 21 (cape)’, 15) [light coat]
(‘Circus by Sam Edelman’, 19) [flats]
(‘Ethel & Myrtle’, 12) [earrings]
(“Claire’s (white)”, 4) [spring scarf]
(‘Foster Grant Sun Luv’, 29) [sunglasses]
(‘Wild Fable’, 35) [backpack]
[Example user (me) would replace the backpack with a tote bag and wear this outfit on a spring day.]

Outfit 3
(‘Uniqlo (black)’, 12) [sweater]
(‘Rachel Zoe’, 18) [pants]
(‘Style & Co.’, 27) [heavy coat]
(‘Coach (Poppy)’, 19) [boots]
(‘Ulla Thomsen (butterfly)’, 12) [earrings]
(‘Divided by H&M’, 3) [winter scarf]
(‘INC’, 8) [winter hat]
(‘Malaysia’, 28) [sunglasses]
(‘Gap’, 21) [gloves]
(‘Shed Rain (daisies)’, 16) [umbrella]
(‘French Connection’, 27) [tote]
[Example user (me) likes this entire outfit! I would wear this on a rainy day.]

Outfit 4
(‘Gildan (white/red)’, 4) [top]
(‘Universal Thread (pinstriped)’, 7) [jeans]
(‘A New Day’, 26) [heavy coat]
(‘Vintage Havana — Babe’, 17) [sneakers]
(‘Hot Topic’, 12) [earrings]
(‘red ribbon’, 3) [ponytail]
(‘A New Day (boxy)’, 11) [sunglasses]
(‘panther’, 11) [handbag]
[Example user (me) likes this entire outfit! I would wear this on a winter day.]
Outfit 5

(‘Zara’, 4) [jumpsuit]
(‘Calvin Klein’, 14) [ankle boots]
(‘Silver hearts’, 11) [earrings]
(‘silver lizard’, 4) [brooch]
(‘Wild Fable’, 6) [glasses]
(‘Christian Siriano for Payless’, 10) [clutch]
[Example user (me) would replace the ankle boots with heels and the brooch with a necklace, then would wear this to work.]

Outfit 6
(‘Kaileigh — Kaela’, 13) [dress]
(‘black crocheted (Mommy)’, 8) [tights]
(‘Circus by Sam Edelman’, 19) [flats]
(‘Napel (gold tree)’, 12) [earrings]
(‘gold interlocking’, 9) [belt]
(‘Goody (navy)’, 1) [headband]
(‘Retro Pop (oxblood)’, 28) [sunglasses]
(‘Jennifer Moore (black)’, 10) [handbag]
[Example user (me) would remove the tights, belt, and headband and replace the flats, then wear this outfit on a summer day.]

[Outfit 7 not needed]

Outfit 8
(‘Xhilaration (pink)’, 3) [swim top]
(‘Anne Cole’, 1) [swim bottom]
(‘Beach Mania’, 4) [flip-flops]
(‘Paradise Craft (navy)’, 6) [summer hat]
(‘GirlProps’, 28) [sunglasses]
(‘Ikea (white/black)’, 13) [beach tote]
[Example user (me) would replace the swim bottom and wear this outfit to the beach.]

Outfit 9
(‘DVF for Target’, 2) [dress]
(‘Jenny’, 14) [flip-flops]
(‘Karen Hanna’, 12) [earrings]
(‘Foster Grant Sun Luv’, 29) [sunglasses]
(‘Baufooer’, 11) [handbag]
[Example user (me) would replace the flip-flops with heels and wear this outfit for a night out.]

[Outfits 10 and 11 not needed]

Outfit 12
(‘Jax (white)’, 3) [evening jumpsuit]
(‘Mossimo (lace-up)’, 9) [evening shoes]
(‘panther’, 8) [evening bag]
[Example user (me) would like this entire outfit and wear it out in the evening.]

Sample output (select analytics):
Categories sorted by minimum item requirement (I need one pair of shorts and 26 pairs of sunglasses)
[(‘shorts’, 1), (‘socks’, 1), (‘ties’, 1), (‘winter scarves’, 1), (‘belts’, 1), (‘hair brooches’, 1), (‘summer hats’, 1), (‘glasses’, 1), (‘eyeglasses’, 1), (‘coin purses’, 1), (‘club dresses’, 1), (‘evening dresses’, 1), (‘evening jumpsuits’, 1), (‘evening tops’, 1), (‘evening skirts’, 1), (‘evening jackets’, 1), (‘evening accessories’, 1), (‘swim tops’, 1), (‘swim bottoms’, 1), (‘beach shoes’, 1), (‘festival’, 1), (“St. Patrick’s Day”, 1), (‘Easter’, 1), (‘Halloween’, 1), (“New Year’s”, 1), (‘jumpsuits’, 2), (‘hosiery’, 2), (‘watches’, 2), (‘clips’, 2), (‘ponies’, 2), (‘headbands’, 2), (‘evening shoes’, 2), (‘evening bags’, 2), (‘workout’, 2), (‘Christmas’, 2), (‘boots’, 3), (‘sandals’, 3), (‘sneakers’, 3), (‘brooches’, 3), (‘spring scarves’, 3), (‘umbrellas’, 3), (‘cosmetics bags’, 3), (‘winter hats’, 4), (‘ankle boots’, 5), (‘gloves’, 6), (‘skirts’, 7), (‘bracelets’, 7), (‘sweaters’, 8), (‘jeans’, 8), (‘masks’, 8), (‘phone cases’, 8), (‘wallets’, 8), (‘pants’, 9), (‘jackets’, 10), (‘light coats’, 10), (‘flats’, 10), (‘dresses’, 11), (‘heavy coats’, 12), (‘heels’, 12), (‘necklaces’, 12), (‘rings’, 13), (‘shopping totes’, 13), (‘handbags’, 16), (‘totes’, 17), (‘earrings’, 19), (‘tops’, 21), (‘sunglasses’, 26)]
