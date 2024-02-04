fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')

  .then((res) => {
    return res.json();
  })

  .then((data) => {
    const element = document.getElementById('hello');
    element.innerText = data.hello;
  });
