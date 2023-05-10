
INSERT INTO offers_pizza (name, img) VALUES ('Seweroni Pizza', '/static/img/SeweroniPizza.png');
INSERT INTO offers_pizza (name, img) VALUES ('Hawaian Sewer', '/static/img/Hawaian%20Sewer.png');
INSERT INTO offers_pizza (name, img) VALUES ('Spicy Sewage', '/static/img/SpicySewage.png');
INSERT INTO offers_pizza (name, img) VALUES ('Sewage Saucy', '/static/img/SewageSaucy.png');
INSERT INTO offers_pizza (name, img) VALUES ('Cheesy Manhole', '/static/img/CheesyManhole.png');
INSERT INTO offers_pizza (name, img) VALUES ('Shroomy Sewage Magic Sewshrooms', '/static/img/ShroomySewage.png');

INSERT INTO offers_topping_type (name) VALUES ('meat');
INSERT INTO offers_topping_type (name) VALUES ('greens');
INSERT INTO offers_topping_type (name) VALUES ('cheese');
INSERT INTO offers_topping_type (name) VALUES ('sauce');
--meat
INSERT INTO offers_topping (name, topping_type_id) VALUES ('Bacon', 1);         --1
INSERT INTO offers_topping (name, topping_type_id) VALUES ('Chicken', 1);       --2
INSERT INTO offers_topping (name, topping_type_id) VALUES ('Ham', 1);           --3
INSERT INTO offers_topping (name, topping_type_id) VALUES ('Pepperoni', 1);     --4
--greens
INSERT INTO offers_topping (name, topping_type_id) VALUES ('Jalapeno', 2);      --5
INSERT INTO offers_topping (name, topping_type_id) VALUES ('Mushrooms', 2);     --6
INSERT INTO offers_topping (name, topping_type_id) VALUES ('Onion', 2);         --7
INSERT INTO offers_topping (name, topping_type_id) VALUES ('Paprika', 2);       --8
INSERT INTO offers_topping (name, topping_type_id) VALUES ('Pineapple', 2);     --9
--cheese
INSERT INTO offers_topping (name, topping_type_id) VALUES ('Cheese', 3);        --10
INSERT INTO offers_topping (name, topping_type_id) VALUES ('Mozzarella', 3);    --11
INSERT INTO offers_topping (name, topping_type_id) VALUES ('Pepper Cheese', 3); --12
INSERT INTO offers_topping (name, topping_type_id) VALUES ('Yellow Cheese', 3); --13
--sauce
INSERT INTO offers_topping (name, topping_type_id) VALUES ('Pizza Sauce', 4);   --14

--topping on pizza relations
INSERT INTO offers_on_pizza(pizza_id, topping_id) VALUES (1, 4);
INSERT INTO offers_on_pizza(pizza_id, topping_id) VALUES (1, 10);
INSERT INTO offers_on_pizza(pizza_id, topping_id) VALUES (1, 14);

INSERT INTO offers_on_pizza(pizza_id, topping_id) VALUES (2, 3);
INSERT INTO offers_on_pizza(pizza_id, topping_id) VALUES (2, 9);
INSERT INTO offers_on_pizza(pizza_id, topping_id) VALUES (2, 1);
INSERT INTO offers_on_pizza(pizza_id, topping_id) VALUES (2, 10);
INSERT INTO offers_on_pizza(pizza_id, topping_id) VALUES (2, 14);

INSERT INTO offers_on_pizza(pizza_id, topping_id) VALUES (3, 5);
INSERT INTO offers_on_pizza(pizza_id, topping_id) VALUES (3, 6);
INSERT INTO offers_on_pizza(pizza_id, topping_id) VALUES (3, 7);
INSERT INTO offers_on_pizza(pizza_id, topping_id) VALUES (3, 8);
INSERT INTO offers_on_pizza(pizza_id, topping_id) VALUES (3, 10);
INSERT INTO offers_on_pizza(pizza_id, topping_id) VALUES (3, 14);

INSERT INTO offers_on_pizza(pizza_id, topping_id) VALUES (4, 10);
INSERT INTO offers_on_pizza(pizza_id, topping_id) VALUES (4, 14);

INSERT INTO offers_on_pizza(pizza_id, topping_id) VALUES (5, 11);
INSERT INTO offers_on_pizza(pizza_id, topping_id) VALUES (5, 12);
INSERT INTO offers_on_pizza(pizza_id, topping_id) VALUES (5, 13);
INSERT INTO offers_on_pizza(pizza_id, topping_id) VALUES (5, 14);

INSERT INTO offers_on_pizza(pizza_id, topping_id) VALUES (6, 2);
INSERT INTO offers_on_pizza(pizza_id, topping_id) VALUES (6, 6);
INSERT INTO offers_on_pizza(pizza_id, topping_id) VALUES (6, 12);
INSERT INTO offers_on_pizza(pizza_id, topping_id) VALUES (6, 13);
INSERT INTO offers_on_pizza(pizza_id, topping_id) VALUES (6, 14);