var contextMenuItem = {
  "id": "verifyInformation",
  "title": "Verify Information",
  "contexts": ["selection"]
};
chrome.contextMenus.create(contextMenuItem);

// function query(text) { 
//   var body = { 
//     "query": text
//   } 
//   const url = "https://covid-api.arjungandhi.com/"
//   fetch(url,
//     { 
//       method: "POST",
//       headers: { 
//         "Accept": "application/json",
//         "Content-Type": "application/json" 
//     }, 
//     body: JSON.stringify(body)
//   })
//   .then(res => { return res.json() })
//   .then(e => {
//     chrome.storage.sync.set({response: e}, function() {
//       alert('Value is set to ' + value);
//     });
//
//     chrome.runtime.sendMessage(e, (resp) => {
//       alert(resp);
//     });
//
//     chrome.storage.sync.get(['response'], function(result) {
//       alert('Value currently is ' + (JSON.stringify(result.response)));
//     });
//   })
//   .catch(err => { 
//     alert(err);
//   }) 
// } 

chrome.contextMenus.onClicked.addListener(function(clickData){
  if (clickData.menuItemId == "verifyInformation" && clickData.selectionText){
    query(clickData.selectionText)
  }
})
