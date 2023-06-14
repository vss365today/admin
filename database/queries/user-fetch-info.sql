SELECT api_token, is_superuser, date_last_login
FROM users
WHERE username = :username;
