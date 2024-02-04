fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')

  .then((res) => res.json)
  .then((data) => {
    const tag = document.getElementById('character');
    tag.innerText = data.name;
  });
