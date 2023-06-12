var myHeaders = new Headers();

new URLSearchParams({
    postId: 1
})
var queryParams = {
  "userId": 1
};

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://mcqapi.onrender.com/api/dashboard?" + new URLSearchParams(queryParams), requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));