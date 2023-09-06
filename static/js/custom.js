function getCookie(name) {
  let matches = document.cookie.match(new RegExp(
    "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
  ));
  return matches ? decodeURIComponent(matches[1]) : undefined;
}

const logged__cookies = getCookie("logged")

if(logged__cookies === "yes") {
    let link_login = document.querySelector(".login_link")
    link_login.setAttribute("href", "/logout/")
    link_login.innerHTML = "Выйти"
}