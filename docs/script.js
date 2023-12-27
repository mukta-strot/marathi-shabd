const csvData = []
const uniqueTags = new Set()

// Fetching the HTML DOM elements
const results = document.querySelector('#results-data')
const wordInput = document.querySelector('#query_english')
const tagInput = document.querySelector("#search-box-tag")

// Handler function for search button
function searchHandler() {
  let searchKeyword = wordInput.value

  // Convert to lower so as to match lower case word in db.csv
  searchKeyword = searchKeyword.toLowerCase()

  // Remove leading and trailing whitespaces 
  searchKeyword = searchKeyword.trim()

  // Search for the keyword from the array
  let matchedResults = csvData.filter(row => {
    return row.en == searchKeyword
  })

  if(matchedResults.length === 0) {
    results.innerHTML = "The word is currently not in the Thesaurus"
    return
  }

  // Display the result in result section
  results.innerHTML = "<span>"
  for (let matchedRow of matchedResults) {
    results.innerHTML +=  "<b>" + matchedRow.en.toUpperCase() + "</b> : "
    results.innerHTML +=  matchedRow.mr + "<br>"
    if(matchedRow.en_ex) {
      results.innerHTML += "<b>English example: </b>" + matchedRow.en_ex 
    } else {
      results.innerHTML += "<b>English example currently not available for this word</b>"
    }

    results.innerHTML += "<br>"

    if(matchedRow.mr_ex) {
      results.innerHTML += "<b>Marathi example: </b>" + matchedRow.mr_ex
    } else {
      results.innerHTML += "<b>Marathi example currently not available for this word</b>"
    }

  }
  results.innerHTML += "</span>"
  return
}

// Preload - load all the csv data into an array
async function fetchDataCSV() {

  // fetch db.csv 
  fetch('../database/db.csv', {mode: 'no-cors'})
    .then(resp => resp.text())
    .then(data => {

      // Split the lines along newline characters
      let lines = data.split(/\r\n|\n/)

      for(let line of lines) {
        // The individual values of Comma-separeted 'values'
        let values = line.split(',')

        // Push values as an object into global array
        csvData.push({
          en: values[0],
          mr: values[1],
          tags: values[2],
          en_ex: values[3],
          mr_ex: values[4],
        })
      }

      getUniqueTags();    // get all unique tags in the data
      populateSearch();   // populate the searchlist using above tags
    })
    .catch(err => console.log(err))
}

fetchDataCSV()

// get all unique tags from the data
function getUniqueTags() {
  for (let entry of csvData) {
    if (typeof (entry['tags']) !== 'undefined') {
      entry['tags'].split(';').forEach(tag => {
        uniqueTags.add(tag);
      });
    }
  }
  uniqueTags.delete(''); // remove empty tags
  uniqueTags.delete('tags'); // remove the header from csv
}


// populate the search box dropdown with tags
function populateSearch() {
  const searchItems = document.getElementById("search-items");
  for (const tag of uniqueTags) {
    // create a list-element for every tag found
    const item = document.createElement("option");
    item.setAttribute("value", tag);
    searchItems.appendChild(item);
  }
}

// search handler for searching via tags
function searchByTag() {
  tagInput.blur();    // remove focus from input
  const searchQuery = tagInput.value;

  // if search query is not a tag then return
  if (!uniqueTags.has(searchQuery)) {
    results.innerHTML = "Select an appropriate tag to filter words"
    return
  }

  // FIlter the words with matching tags in the data
  let matchedResults = csvData.filter(row => {
    let t = row.tags;
    return typeof (t) === 'string' && t.includes(searchQuery);
  })

  if (matchedResults.length === 0) {
    results.innerHTML = "Currently no words are assigned to this tag"
    return
  }

  // display results in results section
  // create a list to wrap all the results
  results.innerHTML = '<ul type="none" style="padding: 0;"></ul>';

  for (const item of matchedResults) {
    // create a list item for every matched result
    const resultItem = document.createElement("li");
    resultItem.innerHTML = "<span>";
    resultItem.innerHTML += "<b>" + item.en.toUpperCase() + "</b> : ";
    resultItem.innerHTML += item.mr + "<br>";

    if (item.en_ex)
      resultItem.innerHTML += "<b>English example: </b>" + item.en_ex + "<br>";
    else
      resultItem.innerHTML += "English example currently not available for this word<br>";

    if (item.mr_ex)
      resultItem.innerHTML += "<b>Marathi example: </b>" + item.mr_ex + "<br>";
    else
      resultItem.innerHTML += "Marathi example currently not available for this word<br>"

    resultItem.innerHTML += "</span><br>";

    // append the resultItem to result list
    document.querySelector("#results-data > ul").appendChild(resultItem);
  }
  return
}