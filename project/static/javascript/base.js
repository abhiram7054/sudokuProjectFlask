
// const darkmode = JSON.parse(localStorage.getItem('darkmode'));
// document.body.classList.add(darkmode ? 'dark' : 'light');
// document.querySelector('meta[name="theme-color"').setAttribute('content', darkmode ? '#1a1a2e' : '#fff');


const menuIcon = document.getElementsByClassName("menuIcon")[0]
const topbar = document.getElementsByClassName("topbar")[0]

// Here, we have created a function where it toggles the active class we mentioned in the css file.
// If active is on, then it will toggle that to original and viceversa.

menuIcon.addEventListener("click", () => {
    topbar.classList.toggle("active");
});

window.onscroll = function () {
    topbar.classList.remove("active");
};

const darkmode = JSON.parse(localStorage.getItem('darkmode'));
document.body.classList.add(darkmode ? 'dark' : 'light');
document.querySelector('meta[name="theme-color"').setAttribute('content', darkmode ? '#1a1a2e' : '#fff');

// Here, we are changing the theme of the page from dark to light mode or viceversa.


const mode = document.getElementById("mode");

mode.onclick = function () {
    document.body.classList.toggle("theme");
    if (document.body.classList.contains("theme")) {
        mode.src = "../static/assets/moon.png"
    }
    else {
        mode.src = "../static/assets/sun.png"
    }
};
