document.addEventListener("DOMContentLoaded", function () {
  const hamburger = document.querySelector(".hamburger");
  const closeIcon = document.querySelector(".close-icon");
  const menu = document.querySelector(".menu");

  hamburger.addEventListener("click", () => {
    hamburger.classList.toggle("active");
    closeIcon.classList.toggle("active");
    menu.classList.toggle("active");
  });

  closeIcon.addEventListener("click", () => {
    hamburger.classList.toggle("active");
    closeIcon.classList.toggle("active");
    menu.classList.toggle("active");
  });

  // Tambahkan listener click untuk setiap link menu
  const menuLinks = document.querySelectorAll(".menu a");
  menuLinks.forEach(link => {
    link.addEventListener("click", () => {
      hamburger.classList.remove("active");
      closeIcon.classList.remove("active");
      menu.classList.remove("active");
    });
  });
});
