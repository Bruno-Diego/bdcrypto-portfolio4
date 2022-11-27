document.addEventListener('DOMContentLoaded', function () {
  //modal init
  let modal = document.querySelectorAll('.modal');
  M.Modal.init(modal);
  // sidenav initialization
  let sidenav = document.querySelectorAll('.sidenav');
  M.Sidenav.init(sidenav);
  // select elements initialization
  let select = document.querySelectorAll('select');
  M.FormSelect.init(select);
  //toast function
  function dismiss() {
    let toastElement = document.querySelector('.toast');
    if (toastElement) {
      toastElement.parentNode.removeChild(toastElement)
    }
  }
  setTimeout(dismiss, 10000);

});