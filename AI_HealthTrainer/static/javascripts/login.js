const icon = document.getElementById("icon");
const passwordInput = document.getElementById("password");

icon.addEventListener("click", function() {
  if (passwordInput.type === "password") {
    passwordInput.type = "text";
    icon.textContent = "visibility"; // Ubah ikon menjadi "visibility"
  } else {
    passwordInput.type = "password";
    icon.textContent = "visibility_off"; // Ubah ikon menjadi "visibility_off"
  }
});
