document.addEventListener('DOMContentLoaded', (event) => {
  load()
})

async function searchFunction(e) {
  //stop page reload
  e.preventDefault();
  //get input value
  var inputVal = document.getElementById("query").value
  //show button is loading
  var form = document.getElementById("loading")
  form.classList.add("loading")
  //make api requst
  var res = await postData('https://covid-api.arjungandhi.com/', {
    query: inputVal
  })
  data = JSON.parse(res.body)
  console.log(data)
  //putting data in modal
  var medbar=document.getElementById("medical")
  var value=Math.round(data.medical_credibility * 100).toString()
  medbar.className= "c100 p".concat(value)
  medbar.firstElementChild.innerHTML=value.concat("%")

  var newsbar=document.getElementById("news")
  var value=Math.round(data.news_hotness * 100).toString()
  newsbar.className= "c100 green p".concat(value)
  newsbar.firstElementChild.innerHTML=value.concat("%")

  var toxbar=document.getElementById("toxicity")
  var value=Math.round(data.toxicity * 100).toString()
  toxbar.className= "c100 purple p".concat(value)
  toxbar.firstElementChild.innerHTML=value.concat("%")

  var negbar=document.getElementById("negative")
  var value=Math.round(data.negitive_credibility * 100).toString()
  negbar.className= "c100 red p".concat(value)
  negbar.firstElementChild.innerHTML=value.concat("%")







  //pop modal up
  $('.ui.small.modal')
    .modal('show');
  //remove loading state
  form.classList.remove("loading")
}


function load() {
  const form = document.getElementById('covidsearch');
  form.addEventListener('submit', searchFunction);
}


// Example POST method implementation:
async function postData(url = '', data = {}) {
  // Default options are marked with *
  const response = await fetch(url, {
    method: 'POST', // *GET, POST, PUT, DELETE, etc.
    mode: 'cors', // no-cors, *cors, same-origin
    cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
    credentials: 'same-origin', // include, *same-origin, omit
    headers: {
      'Content-Type': 'application/json'
      // 'Content-Type': 'application/x-www-form-urlencoded',
    },
    redirect: 'follow', // manual, *follow, error
    referrerPolicy: 'no-referrer', // no-referrer, *client
    body: JSON.stringify(data) // body data type must match "Content-Type" header
  });
  return response.json(); // parses JSON response into native JavaScript objects
}
