// ==UserScript==
// @name         Starship Save Button
// @namespace    Save Shortcut
// @version      0.1
// @description  Save button shortcut for the modifier page press F2
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