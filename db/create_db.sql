-- CREATE database group_buy;
USE group_buy; 

-- drop table purchaser;
-- drop table groups;

-- drop table purchaser;
-- drop table `groups`;



-- CREATE database group_buy;

--  CREATE TABLE user(
--     user_name varchar(50) NOT NULL PRIMARY KEY,
--     user_mail varchar(50),
--     user_password varchar(50)
--     );


-- CREATE TABLE category(
-- id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
-- name varchar(50) NOT NULL
-- );



-- CREATE TABLE groups(
--     id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
--     group_name varchar(50),
--     item_name varchar(50) NOT NULL,
--     max_price int NOT NULL,

--     category_id int NOT NULL,
--     manager varchar(50) NOT NULL,
--     end_date DATE,
--     end_time TIME,
--     description_group varchar(1000),


--     FOREIGN KEY(category_id) REFERENCES category(id),
--     FOREIGN KEY(manager) REFERENCES user(user_name)

-- );


-- CREATE TABLE purchaser(
--     user_name varchar(50) NOT NULL,
--     group_id int NOT NULL,

--     PRIMARY KEY (user_name, group_id),
--     FOREIGN KEY(group_id) REFERENCES groups(id),
--     FOREIGN KEY(user_name) REFERENCES user(user_name)

--     );


CREATE TABLE forums(
    group_id int NOT NULL,
    user_name varchar(50) NOT NULL,
    message_ varchar(1000) NOT NULL,
    count_like int NOT NULL,

    end_date DATE,
    end_time TIME,

    FOREIGN KEY(group_id) REFERENCES groups(id),
    FOREIGN KEY(user_name) REFERENCES user(user_name)

);








