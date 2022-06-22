Outfit generator and wardrobe management tool. Keeps track of the number of wears of each item, with a goal of every item in a category to be worn an equal number of times. 

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
-- Storing the dataset in its own folder while still being able to implement it in main and update it daily
-- More outfit generation data to calculate the probability of generating an outfit the user likes, and of needing a second try, third try, and so on
-- Using object-oriented programming, or creating a dictionary for each individual item, to keep track of additional values like: date last worn, place/event/occasion last worn, need for repairs, no longer available to wear, good for work, and so on

 <img width="275" alt="image" src="https://user-images.githubusercontent.com/79230918/175111448-ad7c7658-d590-4a0e-bd67-ff2a2c414dd3.png">

<img width="274" alt="image" src="https://user-images.githubusercontent.com/79230918/175111475-87ca6c19-1ca0-436f-b010-969008ea07b9.png">

<img width="274" alt="image" src="https://user-images.githubusercontent.com/79230918/175111578-b94ae02b-8435-409a-a736-c5e587fd701f.png">

<img width="274" alt="image" src="https://user-images.githubusercontent.com/79230918/175111696-1106a4ce-4016-4f6d-b62c-de23540e7679.png">

<img width="298" alt="image" src="https://user-images.githubusercontent.com/79230918/175111758-9003a5af-f16e-477c-89c0-7757a342b0d0.png">

<img width="185" alt="image" src="https://user-images.githubusercontent.com/79230918/175111788-a2a3530a-5eb1-44ee-95cf-e8a4235ca053.png">

<img width="186" alt="image" src="https://user-images.githubusercontent.com/79230918/175111832-a76a31e7-752f-4e8e-aa52-7f8bd3b72a49.png">

<img width="184" alt="image" src="https://user-images.githubusercontent.com/79230918/175111874-cec4c1ed-9079-4dd5-a1f5-cb819ddc9c44.png">

<img width="186" alt="image" src="https://user-images.githubusercontent.com/79230918/175111938-42542714-b0ef-4685-9f6c-5922681b2e2b.png">

<img width="185" alt="image" src="https://user-images.githubusercontent.com/79230918/175111971-dd0ee1b1-eb95-42af-8dd1-89bdfa0058ad.png">

<img width="185" alt="image" src="https://user-images.githubusercontent.com/79230918/175112011-08c73fb7-596f-48bc-8fdf-58ffaa2ddc53.png">

<img width="184" alt="image" src="https://user-images.githubusercontent.com/79230918/175112035-cb3f9045-5add-4afa-9446-5f05fd99e129.png">

<img width="184" alt="image" src="https://user-images.githubusercontent.com/79230918/175112074-60ef8614-61b2-4924-9dd9-cdf515a3f99d.png">

<img width="186" alt="image" src="https://user-images.githubusercontent.com/79230918/175112098-61b9a440-64d8-4577-86e8-9476b72e5129.png">

<img width="187" alt="image" src="https://user-images.githubusercontent.com/79230918/175112198-f2a898d0-4090-4b1c-809b-1ecaf972486b.png">

<img width="186" alt="image" src="https://user-images.githubusercontent.com/79230918/175112225-48305dd2-58ad-4554-a9bf-bcea30444034.png">

<img width="184" alt="image" src="https://user-images.githubusercontent.com/79230918/175112271-c320ff89-1aa0-455d-9b57-474c0268e5d1.png">

<img width="186" alt="image" src="https://user-images.githubusercontent.com/79230918/175112306-a8e7710c-cc30-48ca-84c8-9f306488b8ef.png">

<img width="185" alt="image" src="https://user-images.githubusercontent.com/79230918/175112337-eb1dc860-54c5-42fe-a53a-9636896fb453.png">

<img width="331" alt="image" src="https://user-images.githubusercontent.com/79230918/175112352-b846f6e7-bc8c-4526-802e-b005d7628037.png">

<img width="329" alt="image" src="https://user-images.githubusercontent.com/79230918/175112386-bfee0b73-44ad-4b77-878a-08ae55f0692e.png">

<img width="330" alt="image" src="https://user-images.githubusercontent.com/79230918/175112397-537f5ff5-81a2-4bd8-9715-767f72e86370.png">

<img width="331" alt="image" src="https://user-images.githubusercontent.com/79230918/175112451-dec540c6-dcb5-456e-959c-fe343ea8a949.png">

<img width="330" alt="image" src="https://user-images.githubusercontent.com/79230918/175114463-fe5bb7ef-18ec-4aba-97a7-5378845e0836.png">

<img width="329" alt="image" src="https://user-images.githubusercontent.com/79230918/175114496-dd9de912-1630-4bef-8ef1-edc626c7d1a2.png">

<img width="328" alt="image" src="https://user-images.githubusercontent.com/79230918/175114521-4bc7e3ac-7d73-4893-8987-e7c2cc9112e4.png">

<img width="329" alt="image" src="https://user-images.githubusercontent.com/79230918/175114542-3c233449-9728-43e3-bd22-32df664f3a69.png">


