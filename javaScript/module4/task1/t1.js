

document.getElementById("searchForm").addEventListener("submit", async function(event){
  event.preventDefault();

  const query =document.getElementById("query").value;
  const response =await fetch(`https://api.tvmaze.com/search/shows?q=${query}`)
  const data = await response.json();

  console.log(data);
  document.getElementById("results").textContent = JSON.stringify(data,null,2);

});
