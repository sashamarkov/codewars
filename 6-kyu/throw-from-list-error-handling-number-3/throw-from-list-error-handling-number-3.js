  if (invalidChars.length > 0) {
    throw ERRORS.usernameInvalidCharacters(username, ...invalidChars);
  }
}
​
function validatePasswordLength(password) {
  if (password.length > 24) throw ERRORS.passwordTooLong(password);
  if (password.length < 8) throw ERRORS.passwordTooShort(password);
}
​
function validatePasswordCharacters(password) {
  const invalidChars = password.split('').filter(char =>
    !ALLOWED_NORMAL_CHARS.includes(char) && !ALLOWED_SPECIAL_CHARS.includes(char)
  );
  
  if (invalidChars.length > 0) {
    throw ERRORS.passwordInvalidCharacters(password, ...invalidChars);
  }
}
​
function validatePasswordCapital(password) {
  if (!/[A-Z]/.test(password)) {
    throw ERRORS.passwordNoCapital(password);
  }
}
​
function validatePasswordNumber(password) {
  if (!/\d/.test(password)) {
    throw ERRORS.passwordNoNumber(password);
  }
}
​
function validatePasswordUsername(password, username) {