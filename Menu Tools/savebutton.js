// ==UserScript==
// @name         Starship Save Button
// @namespace    Save Shortcut
// @version      0.2
// @description  Save button shortcut for the modifier page press F2 and F4 for items page
// @author       Justin Soon
// @match        https://panel.starship.xyz/marketplace/serviceassignments/*
// @icon         data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
// @grant        none
// ==/UserScript==

window.addEventListener('keyup', function (e) {
  if (e.keyCode === 113) {
     var button = document.evaluate("//*[@id='modifiers']/div/div[2]/div/button", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
     button.click();
  }
}, false);

window.addEventListener('keyup', function (e) {
  if (e.keyCode === 115) {
     var button = document.evaluate("/html/body/div[1]/main/div/form/div/div[1]/div/div/div[19]/div/button", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
     button.click();
  }
}, false);
