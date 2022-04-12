# Useful tools and tips to efficiently edit the menu

## Panel Shortcuts (PanelShortcuts.js)
### Keybinds
| Shortcuts | Actions | 
| --------------- | --------------- |
| F2 | save changes on mod page / item page / modifier template / click import | 
| F4 | upload image on item page | 
| TAB | item setting page -> mod setting page / mod setting page -> item setting page |
| LEFT ALT + Q | merchant page -> go to items tab | 
| LEFT ALT + W | merchant page -> go to items categories tab | 
| LEFT ALT + 1 | merchant item page -> open action modal | 
| LEFT ALT + 2 | merchant item page -> download | 
| LEFT ALT + 3 | merchant item page -> upload |
| LEFT ALT + A | item page -> make item available | 
| LEFT ALT + S | item page -> make item archived |
| LEFT ALT + Z | item page -> open item categories |
### Q&A
* saves do apply just don't use back and forward button on browser to update, because it takes last cache data
* how to use?
  - install tampermonkey extension https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo?hl=en
  - install userscript from link https://raw.githubusercontent.com/justinsoon/Starship/main/Menu%20Tools/savebutton.js?token=AEHZQVCXRMLLN4PSE6D5HZTBRCX6I
  - customize key used by changing the keycode. Get your input val from https://keycode.info/
## Paste Raw (pasteraw.js)
### Keybinds
| Shortcuts | Actions | 
| --------------- | --------------- |
| F4 | typing clipboard contents | 
### Q&A
* Why?
  * When finding a linked mod, to find the matching item
  * Can't paste in the drop down, but accepts keyboard input
  * Simulates raw input
  * ![image](https://github.com/justinsoon/Starship/blob/main/images/pasteraw.jpg)
* how to use?
  * open terminal to folder
  * type py pasteraw.py 
  * press ***F4*** when needing to type copied contents 
  * Leave terminal on, or close it when not needed
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
