USE group_buy; 


-- INSERT INTO user VALUES("yehudit", "y@gmail", "yyy");
-- INSERT INTO user VALUES("sara", "sa@gmail", "sss");
-- INSERT INTO user VALUES("chaviva", "c@gmail", "ccc");
-- INSERT INTO user VALUES("sari", "s@gmail", "sss");
-- INSERT INTO user VALUES("shraga", "sss@", "ghj");


-- INSERT INTO category (name) VALUES("furniture");
-- INSERT INTO category (name) VALUES("electronics");
-- INSERT INTO category (name) VALUES("Games");
-- INSERT INTO category (name) VALUES("Bags");

-- select  * From user;

--  INSERT INTO `groups`(group_name, item_name, max_price, category_id, manager, end_date, end_time) 
--      VALUES("tables", "table", 3000, 1, "shraga", '2021-12-02', '18:00');

--  INSERT INTO `groups`(group_name, item_name, max_price, category_id, manager, end_date, end_time) 
--      VALUES("microwaves", "microwave", 200, 2, "sara", '2021-12-03', '18:00');
--  INSERT INTO `groups`(group_name, item_name, max_price, category_id, manager, end_date, end_time) 
--       VALUES( "box", "Katan", 130, 3, "yehudit", '2021-12-04', '17:00');
--  INSERT INTO `groups`(group_name, item_name, max_price, category_id, manager, end_date, end_time) 
--      VALUES( "Backpacks", "color",  100, 4, "chaviva", '2021-12-02', '18:00');

--  INSERT INTO `groups`(group_name, item_name, max_price, category_id, manager, end_date, end_time) 
--      VALUES("tables", "chair", 250, 1, "sari", '2021-12-02', '18:00');


-- select  * From category;
-- select  category_id From groups;
select count(*) from user;
