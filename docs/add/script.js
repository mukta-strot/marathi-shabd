const HOST = "https://mr-shabd-backend.herokuapp.com"

async function addHandle() {
  const enwr = document.getElementById('eng').value
  const mrwr = document.getElementById('mr').value
  const enex = document.getElementById('enex').value
  const mrex = document.getElementById('mrex').value
  const tags = document.getElementById('tags').value

  const postdata = {
    "en": enwr,
    "mr": mrwr,
    "en_ex": enex,
    "mr_ex": mrex,
    "tags": tags
  }

  const resp = await fetch(`${HOST}/word`, {
    method: 'POST',
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(postdata)
  })

  const data = await resp.json()
  if(data.hasOwnProperty('err')) {
    alert(data.err)
    return
  }
  alert({data})
}
