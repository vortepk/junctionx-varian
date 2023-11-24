CREATE TABLE "patient" (
  "id" int PRIMARY KEY,
  "name" varchar NOT NULL,
  "family" varchar NOT NULL,
  "email" varchar NOT NULL,
  "weith" int NOT NULL,
  "number_fraction" int NOT NULL,
  "gender" varchar NOT NULL,
  "condition" varchar NOT NULL,
  "priority" varchar NOT NULL,
  "treat_date" timestamp
);

CREATE TABLE "machine" (
  "name" varchar NOT NULL,
  "status" varchar NOT NULL
);

CREATE TABLE "calendar" (
  "id" int PRIMARY KEY,
  "machine_name" varchar NOT NULL,
  "slots" timestamp UNIQUE NOT NULL
);

ALTER TABLE "patient" ADD FOREIGN KEY ("treat_date") REFERENCES "calendar" ("id");