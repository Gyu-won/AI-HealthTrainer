const icon = document.getElementById("icon");
const iconCheck = document.getElementById("iconCheck");
const passwordInput = document.getElementById("password");
const checkpasswordInput = document.getElementById("checkpassword");

icon.addEventListener("click", function() {
  if (passwordInput.type === "password") {
    passwordInput.type = "text";
    icon.textContent = "visibility"; // Ubah ikon menjadi "visibility"
  } else {
    passwordInput.type = "password";
    icon.textContent = "visibility_off"; // Ubah ikon menjadi "visibility_off"
  }
});

iconCheck.addEventListener("click", function() {
    if (checkpasswordInput.type === "password") {
      checkpasswordInput.type = "text";
      iconCheck.textContent = "visibility"; // Ubah ikon menjadi "visibility"
    } else {
      checkpasswordInput.type = "password";
      iconCheck.textContent = "visibility_off"; // Ubah ikon menjadi "visibility_off"
    }
  });