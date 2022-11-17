document.addEventListener('DOMContentLoaded', function () {
  //modal init
  let modal = document.querySelectorAll('.modal');
  M.Modal.init(modal);
  // sidenav initialization
  let sidenav = document.querySelectorAll('.sidenav');
  M.Sidenav.init(sidenav);
  //toast function
  function dismiss() {
    let toastElement = document.querySelector('.toast');
    if (toastElement) {
      toastElement.parentNode.removeChild(toastElement)
    }
  }
  setTimeout(dismiss, 10000);

});