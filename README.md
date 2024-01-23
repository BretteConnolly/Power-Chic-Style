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


<img width="328" alt="image" src="https://user-images.githubusercontent.com/79230918/175114521-4bc7e3ac-7d73-4893-8987-e7c2cc9112e4.png">

<img width="329" alt="image" src="https://user-images.githubusercontent.com/79230918/175114542-3c233449-9728-43e3-bd22-32df664f3a69.png">


