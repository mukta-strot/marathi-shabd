const csvData = []

// Fetching the HTML DOM elements
const results = document.querySelector('#results-data')
const wordInput = document.querySelector('#query_english')
const resultsTable = document.querySelector('#results-table')

// Handler function for search button
function searchHandler() {
  let searchKeyword = document.querySelector('#query_english').value
  
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
    results.innerHTML +=  matchedRow.en + " : "
    results.innerHTML +=  matchedRow.mr + "<br>"
    if(!matchedRow.en_ex) {
      results.innerHTML += "English example: " + matchedRow.en_ex + "<br>"
    } else {
      results.innerHTML += "English example currently not available for this word"
    }
    if(!matchedRow.mr_ex) {
      results.innerHTML += "Marathi example: " + matchedRow.mr_ex + "<br>"
    } else {
      results.innerHTML += "Marathi example currently not available for this word"
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

    })
    .catch(err => console.log(err))
}

fetchDataCSV()
