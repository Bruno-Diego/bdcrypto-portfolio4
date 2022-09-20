document.addEventListener('DOMContentLoaded', function () {
  // sidenav initialization
  let sidenav = document.querySelectorAll('.sidenav');
  M.Sidenav.init(sidenav);

  function dismiss() {
    let toastElement = document.querySelector('.toast');
    if (toastElement) {
      toastElement.parentNode.removeChild(toastElement)
    }
  }
  setTimeout(dismiss, 10000);

});