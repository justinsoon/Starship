# Useful tools and tips to efficiently edit the menu

## Panel Shortcuts (PanelShortcuts.js)
### Keybinds
- press **F2** to save on mod page / item page
- press **TAB** to go to item modifier page from item setting page
- press **LEFT ALT + Q** to go to item page from merchant setting page
- press **LEFT ALT + W** to go to item categories page from merchant setting page
- press **LEFT ALT + ONE** to access action modal from items page 
### Q&A
* saves do apply just don't use back and forward button on browser to update, because it takes last cache data
* how to use?
  - install tampermonkey extension https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo?hl=en
  - install userscript from link https://raw.githubusercontent.com/justinsoon/Starship/main/Menu%20Tools/savebutton.js?token=AEHZQVCXRMLLN4PSE6D5HZTBRCX6I
  - customize key used by change the keycode. get val from https://keycode.info/

## Macros
* When getting an item instead of clicking the modifier button make a macro [OLD METHOD - By Script press **TAB**]
  - Ctrl + L -> End -> '/modifiers' -> Enter
  - make sure to open the item page
* When opening a merchant and checking all categories [OLD METHOD - By Script press **LEFT ALT + W**]
  - Ctrl + L -> End -> '/item_categories' -> Enter
  - make sure to be on the merchant setting page
* When opening a merchant and checking all items [OLD METHOD - By Script press **LEFT ALT + Q**]
  - Ctrl + L -> End -> '/items' -> Enter
  - make sure to be on the merchant setting page
* Fastest way to save changes on main item page [OLD METHOD - By Script press **F2**]
  - press enter in the edit name box
  - Can make a bind on the mouse that presses enter so it all mouse movement and is faster
* editing a lot of prices from mods
  - Mouse 1 -> Ctrl + A -> '0'
  - change the number to what is needed
  - **warning** for this macro - you need to have really good aim for this method

## Multiple item with the same mod names
* Using this extension as a text replacement
  - https://chrome.google.com/webstore/detail/magical-text-expander/iibninhmiggehlcdolcilmhacighjamp
  - Type in ur shortcut phrase and it'll autocomplete the name
  - Phrase: s1 -> 12oz Hot | s2 -> 16oz Hot | s3 -> 16oz Cold
  - ![iamge](https://github.com/justinsoon/Starship/blob/main/images/textreplacement.jpg)
## Saving stock images
* Using this extension you'll always get the JPG
  - The panel will only take jpg so instead of renaming them if you get an image from your search engine it will automatically save it as a jpg
  - https://chrome.google.com/webstore/detail/save-image-as-type/gabfmnliflodkdafenbcpjdlppllnemd
