DROP TABLE items;
DROP TABLE characters;

CREATE TABLE characters (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  health INT,
  damage INT,
  armor INT,
  -- item_id INT REFERENCES items(id)

);

CREATE TABLE items (
  id SERIAL PRIMARY KEY,  
  name VARCHAR(255),
  attribute VARCHAR(255),
  value INT,
  description VARCHAR(255)
);


