var dates = document.body.getElementsByClassName("bite-day-menu")
day = 0
var textOut = ""
for (let i = 0; i < dates[day].getElementsByClassName("col-xs-9").length; i ++){
    var foods = dates[day].getElementsByClassName("col-xs-9")[i].innerText.trim()
    textOut += foods + '\n'
} 

console.log(textOut)