const toggle = document.getElementById('toggle_header');
toggle.onclick = function () {
  const header = document.querySelector('header');
  console.log(header.classList);
  if (header.classList.contains('green')) {
    header.classList.replace('green', 'red');
  } else if (header.classList.contains('red')) {
    header.classList.replace('red', 'green');
  }
};
