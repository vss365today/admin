UPDATE users
SET api_token = :api_token
WHERE username = :username;
