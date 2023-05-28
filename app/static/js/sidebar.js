

function toggleNav() {
    var sidebar = document.getElementById("sidenav")
    var main = document.getElementById("main")
    var sidebar_toggle = document.getElementById("sidebar-toggle")
    var nav_links =  document.getElementsByClassName("nav-item-text");

    if (sidebar.getAttribute('data-is-open') == 'true'){
        sidebar.style.width = "5%";
        main.style.marginLeft = "7%";
        sidebar_toggle.style.marginLeft = "5%";
        sidebar.setAttribute("data-is-open", "false")
        sidebar_toggle.textContent='\u00D7';

        for (var i = 0; i < nav_links.length; i++) {
          var link = nav_links[i];
          link.style.fontSize = "0";
        }
    } else {
        sidebar.style.width = "15%";
        main.style.marginLeft = "15%";
        sidebar_toggle.style.marginLeft = "17%";
        sidebar.setAttribute("data-is-open", "true")
        sidebar_toggle.textContent="\u2630"
        for (var i = 0; i < nav_links.length; i++) {
          var link = nav_links[i];
          link.style.fontSize = "20px";
        }


    }

}