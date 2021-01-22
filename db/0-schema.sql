CREATE TABLE "users" (
  "_id" INTEGER NOT NULL UNIQUE,
  "username" TEXT NOT NULL UNIQUE,
  "password" TEXT NOT NULL,
  "date_created" TEXT NOT NULL DEFAULT current_timestamp,
  "date_last_login" TEXT DEFAULT current_timestamp,
  "api_token" TEXT NOT NULL,
  "is_superuser"	INTEGER NOT NULL DEFAULT 0,
  PRIMARY KEY("_id" AUTOINCREMENT)
);
