const CONSTANTS = {
  USERNAME: { MIN_LEN: 4, MAX_LEN: 15, PATTERN: /^[a-zA-Z0-9_]+$/ },
  PASSWORD: { MIN_LEN: 6, MAX_LEN: 15, PATTERN: /^[a-zA-Z0-9]+$/ },
  RESERVED_NAMES: ["administrator", "admin", "system", "john"],
  ALLOWED_DOMAINS: ["hotmail.com", "facebook.com", "gmail.com", "163.com", "126.com"]
};
​
const ERROR_MESSAGES = {
  USERNAME_TOO_SHORT: "Error: username is too short.",
  USERNAME_TOO_LONG: "Error: username is too long.",
  USERNAME_INVALID_CHARS: "Error: username contains invalid characters.",
  USERNAME_RESERVED: "Error: username has been reserved by system.",
  USERNAME_REGISTERED: "Error: username has been registered by other users.",
  PASSWORD_TOO_SHORT: "Error: password is too short.",
  PASSWORD_TOO_LONG: "Error: password is too long.",
  PASSWORD_INVALID_CHARS: "Error: password contains invalid characters.",
  PASSWORD_WEAK: "Error: password is a weak password.",
  EMAIL_INVALID_CHARS: "Error: email address contains invalid characters.",
  EMAIL_INVALID_FORMAT: "Error: email address format is invalid.",
  EMAIL_NOT_ALLOWED: "Error: email address is not allowed.",
  SUCCESS: "User registration success!"
};