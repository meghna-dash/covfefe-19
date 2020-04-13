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
  var res= await postData('https://covid-api.arjungandhi.com/', { query: inputVal })
  data=JSON.parse(res.body)
  console.log(data)
  //putting data in modal
  
  //
  //pop modal up
  $('.ui.tiny.modal')
    .modal('show')
  ;
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
