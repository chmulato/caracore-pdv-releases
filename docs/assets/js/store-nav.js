(function () {
  var button = document.getElementById('mobile-menu-button');
  var menu = document.getElementById('mobile-menu');
  if (button && menu) {
    button.addEventListener('click', function () {
      menu.classList.toggle('hidden');
    });
  }
})();
