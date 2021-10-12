### Why?
- Needed to grab all the menu items for the day from [ERAU](http://menus.sodexomyway.com/BiteMenu/Menu?menuId=189&locationId=94144001&whereami=https://eraudining.sodexomyway.com/dining-near-me/refueling-station)

## Instructions
- Define Var
`<var dates = document.body.getElementsByClassName("bite-day-menu")  >`
- Gather food names and format
`<
day = 0
var textOut = ""
for (let i = 0; i < dates[day].getElementsByClassName("col-xs-9").length; i ++){
    var foods = dates[day].getElementsByClassName("col-xs-9")[i].innerText.trim()
    textOut += foods + '\n'
} >`

- Print the formatted list
`<console.log(textOut)>`
