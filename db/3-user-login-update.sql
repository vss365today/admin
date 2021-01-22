UPDATE users
SET date_last_login = current_timestamp
WHERE username = :username;
