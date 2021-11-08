// ==UserScript==
// @name         Starship Panel Shortcuts
// @namespace    Panel Shortcuts
// @version      0.4
// @description  Shortcut for the modifier or item page press Alt + 2, Alt + 1 to access item modifiers from an item's page, ALT + Q = Items, ALT + W = Item Categories
// @author       Justin Soon
// @match        https://panel.starship.xyz/marketplace/serviceassignments/*
// @icon         data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
// @grant        none
// ==/UserScript==

    var ctrlDown = false,
        altKey = 18,
        cmdKey = 91,
        qKey = 81,
        wKey = 87,
        eKey = 69,
        oneKey = 49,
        twoKey = 50;


if (/\bmodifiers\b/.test (location.pathname) ) {
    window.addEventListener('keyup', function (e) {
        if (e.keyCode == twoKey) {
            var button = document.evaluate("//*[@id='modifiers']/div/div[2]/div/button", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
            button.click();
            alert("Saved!");
        }
    }, false);
} else {
    window.addEventListener('keyup', function (e) {
        if (e.keyCode == altKey || e.keyCode == twoKey) {
            var button = document.evaluate("/html/body/div[1]/main/div/form/div/div[1]/div/div/div[19]/div/button", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
            button.click();
            alert("Saved!");
        }
    }, false);
}

window.addEventListener('keyup', function (e) {
  if (e.keyCode == altKey || e.keyCode == oneKey) {
     var button = document.evaluate("/html/body/div[1]/main/div/form/div/div[1]/div/div/fieldset[1]/div[3]/div/p/a", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
     button.click();
  }
}, false)

window.addEventListener('keyup', function (e) {
  if (e.keyCode == altKey || e.keyCode == qKey) {
     var button = document.evaluate("/html/body/div[1]/main/div/ul/li[2]/a", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
     button.click();
  }
}, false)

window.addEventListener('keyup', function (e) {
  if (e.keyCode == altKey || e.keyCode == wKey) {
     var button = document.evaluate("/html/body/div[1]/main/div/ul/li[3]/a", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
     button.click();
  }
}, false)
