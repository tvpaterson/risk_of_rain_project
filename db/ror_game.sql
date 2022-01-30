DROP TABLE items;
DROP TABLE characters;

CREATE TABLE characters (
  id SERIAL PRIMARY KEY,  
  name VARCHAR(255),
  health INT,
  damage INT,
  armor INT
);

CREATE TABLE items (
  id SERIAL PRIMARY KEY,  
  name VARCHAR(255),
  attribute VARCHAR(255),
  value INT,
  description VARCHAR(255)
);

INSERT INTO characters (id, name, health, damage, armor) VALUES (1, 'COMMANDO', 110, 12, 0);
INSERT INTO characters (id, name, health, damage, armor) VALUES (2, 'ENGINEER', 130, 14, 0);
INSERT INTO characters (id, name, health, damage, armor) VALUES (3, 'BANDIT', 110, 12, 0);
INSERT INTO characters (id, name, health, damage, armor) VALUES (4, 'CAPTIAN', 110, 12, 0);
INSERT INTO characters (id, name, health, damage, armor) VALUES (5, 'ACRID', 160, 15, 20);
INSERT INTO characters (id, name, health, damage, armor) VALUES (6, 'ARTIFICER', 110, 12, 0);
INSERT INTO characters (id, name, health, damage, armor) VALUES (7, 'HERETIC', 440, 18, 0);
INSERT INTO characters (id, name, health, damage, armor) VALUES (8, 'HUNTRESS', 90, 12, 0);
INSERT INTO characters (id, name, health, damage, armor) VALUES (9, 'LOADER', 160, 12, 20);
INSERT INTO characters (id, name, health, damage, armor) VALUES (10, 'MARCENARY', 110, 12, 20);
INSERT INTO characters (id, name, health, damage, armor) VALUES (11, 'MUL-T', 200, 11, 12);
INSERT INTO characters (id, name, health, damage, armor) VALUES (12, 'REX', 130, 12, 20);


INSERT INTO items (id, name, attribute, value, description) VALUES (1, 'Sticky Bomb', 'DMG', 10, 'Chance to throw sticky bomb');
INSERT INTO items (id, name, attribute, value, description) VALUES (2, 'Topaz Brooch', 'ARM', 20, 'Gain temporary armor');
INSERT INTO items (id, name, attribute, value, description) VALUES (3, 'Medkit', 'HP', 20, 'Gain 20 health');
INSERT INTO items (id, name, attribute, value, description) VALUES (4, 'Bison Steak', 'HP', 25, 'Increase health by 25');
INSERT INTO items (id, name, attribute, value, description) VALUES (5, 'Ukulele', 'DMG', 100, 'Permanently increase damage by 100');


SELECT * FROM characters;
SELECT * FROM items;