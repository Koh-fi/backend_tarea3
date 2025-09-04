function createAlert(message, type) {
  const alertPlaceholder = document.getElementById('alertPlaceholder')
  const wrapper = document.createElement('div')
  while (alertPlaceholder.firstChild) {
    alertPlaceholder.removeChild(alertPlaceholder.firstChild);
  }
  let icon = ""
  switch (type) {
    case "info":
      icon = "fa fas fa-info-circle"
      break;

    case "success":
      icon = "fa fa-check-circle"
      break;

    default:
      icon = "fa fa-exclamation-triangle"
      break;
  }

  wrapper.innerHTML = [
    `<div class="alert alert-${type} live-alert d-flex align-items-center alert-dismissible" role="alert">`,
    `   <i class="${icon} icn-alert"></i>`,
    `   <div>${message}</div>`,
    '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
    '</div>'
  ].join('')
  
  
  alertPlaceholder.append(wrapper)

  const alert = wrapper.querySelector('.alert');
  alert.classList.add('fade');
  setTimeout(() => {alert.classList.add('show')}, 10);

}