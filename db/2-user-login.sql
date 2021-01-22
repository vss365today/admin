SELECT api_token, is_superuser
FROM users
WHERE username = :username AND password = :password;
