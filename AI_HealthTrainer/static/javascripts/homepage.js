const hamburger = document.querySelector(".hamburger");
const closeIcon = document.querySelector(".close-icon");
const menu = document.querySelector(".menu");

hamburger.addEventListener("click", () => {
  hamburger.classList.toggle("active");
  closeIcon.classList.toggle("active");
  menu.classList.toggle("active");
});
