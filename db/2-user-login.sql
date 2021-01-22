SELECT api_token, is_superuser
FROM users
WHERE username = ? AND password = ?;
