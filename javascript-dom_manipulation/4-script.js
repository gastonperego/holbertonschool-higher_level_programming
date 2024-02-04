const add = document.getElementById('add_item');
add.onclick = function () {
  const list = document.querySelector('.my_list');
  const li = document.createElement('li');
  li.appendChild(document.createTextNode('Item'));
  list.appendChild(li);
};
