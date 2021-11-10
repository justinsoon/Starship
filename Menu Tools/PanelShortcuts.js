// ==UserScript==
// @name         Starship Panel Shortcuts
// @namespace    Panel Shortcuts
// @version      0.7
// @description  Shortcut for the modifier or item page press F2, Tab to access item modifiers from an item's page, Alt + Q = Items, Alt + W = Item Categories, Alt + 1 = Action Button, Alt + 2 = Download, Alt + 3 = Upload, ALT + A = Available, Alt + D = Archived
// @author       Justin Soon
// @match        https://panel.starship.xyz/marketplace/serviceassignments/*
// @icon         data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
// @grant        none
// ==/UserScript==

(function() {
var ctrlDown = false,
    altKey = 16,
    cmdKey = 91,
    qKey = 81,
    wKey = 87,
    oneKey = 49,
    twoKey = 50,
    threeKey = 51,
    aKey = 65,
    sKey = 83,
    zKey = 90,
    tabKey = 9,
    f2Key = 113;
function onKeydown(evt) {
    if (evt.altKey && evt.keyCode == qKey) {
        itemPage();
    }
    if (evt.altKey && evt.keyCode == wKey) {
        itemCat();
    }
    if (evt.altKey && evt.keyCode == oneKey) {
        actionModal();
    }
    if (evt.altKey && evt.keyCode == twoKey) {
        dlMenu();
    }
    if (evt.altKey && evt.keyCode == threeKey) {
        upMenu();
    }
    if (evt.altKey && evt.keyCode == aKey) {
        itemAvail();
    }
    if (evt.altKey && evt.keyCode == sKey) {
        itemArch();
    }
    if (evt.altKey && evt.keyCode == zKey) {
        itemSelCat();
    }
    if (evt.keyCode == tabKey) {
        itemMod();
    }
    if (evt.keyCode == f2Key) {
        save();
    }
}
function itemPage() {
        var button = document.evaluate("/html/body/div[1]/main/div/ul/li[2]/a", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        button.click();
    }
function itemCat() {
        var button = document.evaluate("/html/body/div[1]/main/div/ul/li[3]/a", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        button.click();
    }
function actionModal() {
    if (/\items\b/.test (location.pathname) ) {
        var button = document.evaluate("/html/body/div[1]/nav/div/div[2]/button", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        button.click();
    }
}
function dlMenu() {
    if (/\items\b/.test (location.pathname) ) {
        var button = document.evaluate("//*[@id='download-items-csv']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        button.click();
    }
}
function upMenu() {
    if (/\items\b/.test (location.pathname) ) {
        var button = document.evaluate("/html/body/div[1]/main/div/div[1]/div/div[1]/div/label[1]", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        button.click();
    }
}
function itemArch() {
    if (/\items\b/.test (location.pathname) ) {
        var button = document.evaluate("/html/body/div[1]/main/div/form/div/div[1]/div/div/fieldset[1]/div[4]/div/div[3]/label", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        button.click();
    }
}
function itemAvail() {
    if (/\items\b/.test (location.pathname) ) {
        var button = document.evaluate("/html/body/div[1]/main/div/form/div/div[1]/div/div/fieldset[1]/div[4]/div/div[1]/label", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        button.click();
    }
}
function itemSelCat() {
    if (/\items\b/.test (location.pathname) ) {
        var button = document.evaluate("/html/body/div[1]/main/div/form/div/div[1]/div/div/fieldset[1]/div[2]/div[2]/p/a", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        button.click();
    }
}
function save() {
    if (/\bmodifiers\b/.test (location.pathname) ) {
        var button = document.evaluate("//*[@id='modifiers']/div/div[2]/div/button", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        button.click();
        alert("Saved!");
    } else {
        var button2 = document.evaluate("/html/body/div[1]/main/div/form/div/div[1]/div/div/div[19]/div/button", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        button2.click();
        alert("Saved!");
    }
}
function itemMod() {
    if (/\bmodifiers\b/.test (location.pathname) ) {
        var button = document.evaluate("/html/body/div[1]/nav/div/div/ol/li[4]/a", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        button.click();
    } else {
        var button2 = document.evaluate("/html/body/div[1]/main/div/form/div/div[1]/div/div/fieldset[1]/div[3]/div/p/a", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
        button2.click();
    }
}
document.addEventListener('keydown', onKeydown, true);
})();
