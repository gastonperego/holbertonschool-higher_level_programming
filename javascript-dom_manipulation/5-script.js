const update = document.getElementById('update_header')
update.onclick = function() {
    const header = document.querySelector('header')
    header.innerText = 'New header!!!'
}