const red_header = document.querySelector('#red_header')
red_header.onclick = function() {
    const header = document.querySelector('header')
    header.setAttribute('class', 'red')
}
