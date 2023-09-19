#Cart Class

- At first, Cart has items, so we create a class item that contains item data, and it can be modified in the future and add more features (we could make it as a dictionary and pass, but when we want to add features, that will prevent us).
   - Item class have members (price, name , id).
   - method show that shows the data of the item
- In cart class, we have a dictionary with id as a key and item as a value. , id counter starts by 1 That will help us in ( remove, search methods), itemIds that contain all the ids of of inserted items, and total sum that calculate the sum of the items in the cart.
- Add method : take item and add its id to items ids and assign its ids to item in items dictionary and increase total sum and increase id counter
- Search method : for this we have 2 approaches 1 - to make a common loop with complexity O (Number of the items in the cart) we can reduce it how ?? 
  We are storing ids in ascending order, which means the data is sorted, so I can use binary search algorithm which have complexity O(log(Number of the items in the cart)).
- Remove method : it takes only the id of the item, and at first I have to check if the item id is in the list, so we use the search method to check, and after that, we remove the item.
  I also reduced the complexity of the function to calculate the total price how ??
  Because when i add or remove item i add or remove its price to the total Sum member so it is done in O(1) instead using loop every time i call this function which its complexity is O(number of items in cart)
- Finally ShowProducts method : that shows all items in the cart using a for loop because I have to loop over all items.
