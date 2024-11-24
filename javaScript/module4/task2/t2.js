
document.getElementById("searchForm").addEventListener("submit", async function(event){
  event.preventDefault();

  const query =document.getElementById("query").value;
  console.log("Search query", query);

  const response =await fetch(`https://api.tvmaze.com/search/shows?q=${query}`)
  const data = await response.json();

  console.log("search results", data);


  document.getElementById("results").textContent = JSON.stringify(data,null,2);

});
