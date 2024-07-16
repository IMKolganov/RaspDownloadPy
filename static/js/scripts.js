function validatePassword() {
    var password = document.getElementsByName("password")[0].value;
    // Replace 'hashed_password' with the actual hashed password from Python code
    var hashed_password = 'hashed_password'; // Replace with your hashed password
    var input_password_hash = CryptoJS.MD5(password).toString();

    if (input_password_hash !== hashed_password) {
        alert("Invalid password!");
        return false;
    }
    return true;
}