// ==UserScript==
// @name         Starship Panel Shortcuts
// @namespace    Panel Shortcuts
// @version      0.5
// @description  Shortcut for the modifier or item page press F2, Tab to access item modifiers from an item's page, Alt + Q = Items, Alt + W = Item Categories, Alt + 1 = Action Button, Alt + 2 = Download, Alt + 3 = Upload
// @author       Justin Soon
// @match        https://panel.starship.xyz/marketplace/serviceassignments/*
// @icon         data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
// @grant        none
// ==/UserScript==

var ctrlDown = false,
    altKey = 16,
    cmdKey = 91,
    qKey = 81,
    wKey = 87,
    oneKey = 49,
    twoKey = 50,
    threeKey = 51,
    tabKey = 9,
    f2Key = 113;

window.addEventListener('keyup', function (e) {
  if (e.keyCode == tabKey) {
     var button = document.evaluate("/html/body/div[1]/main/div/form/div/div[1]/div/div/fieldset[1]/div[3]/div/p/a", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
     button.click();
  }
}, false)

window.addEventListener('keydown', function (e) {
    if (e.keyCode.altKey || e.keyCode == qKey) {
        var button = document.evaluate("/html/body/div[1]/main/div/ul/li[2]/a", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        button.click();
    }
}, false)
window.addEventListener('keydown', function (e) {
    if (e.keyCode.altKey || e.keyCode == wKey) {
        var button = document.evaluate("/html/body/div[1]/main/div/ul/li[3]/a", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        button.click();
    }
}, false)

if (/\items\b/.test (location.pathname) ) {
    window.addEventListener('keydown', function (e) {
        if (e.keyCode.altKey || e.keyCode == oneKey) {
            var button = document.evaluate("/html/body/div[1]/nav/div/div[2]/button", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
            button.click();
        }
    }, false)
}
if (/\items\b/.test (location.pathname) ) {
    window.addEventListener('keydown', function (e) {
        if (e.keyCode.altKey || e.keyCode == twoKey) {
            var button = document.evaluate("//*[@id='download-items-csv']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
            button.click();
        }
    }, false)
}
if (/\items\b/.test (location.pathname) ) {
    window.addEventListener('keydown', function (e) {
        if (e.keyCode.altKey || e.keyCode == threeKey) {
            var button = document.evaluate("/html/body/div[1]/main/div/div[1]/div/div[1]/div/label[1]", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
            button.click();
        }
    }, false)
}
if (/\bmodifiers\b/.test (location.pathname) ) {
    window.addEventListener('keyup', function (e) {
        if (e.keyCode == f2Key) {
            var button = document.evaluate("//*[@id='modifiers']/div/div[2]/div/button", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
            button.click();
            alert("Saved!");
        }
    }, false);
} else {
    window.addEventListener('keyup', function (e) {
        if (e.keyCode == f2Key) {
            var button = document.evaluate("/html/body/div[1]/main/div/form/div/div[1]/div/div/div[19]/div/button", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
            button.click();
            alert("Saved!");
        }
    }, false);
}
