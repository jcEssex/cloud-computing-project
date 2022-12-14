SHOW DATABASES;
use group7;
show tables;
create table users (userID VARCHAR(255) NOT NULL, pw VARCHAR(255) NOT NULL, userRole VARCHAR(255) NOT NULL);
select * from users;
insert into users (userID, pw, userRole) values ('ec22339@qmul.ac.uk', 'yhc239qM', 'admin');
insert into users (userID, pw, userRole) values ('ec221255@qmul.ac.uk', 'fcc215xK', 'moderator');
# remove unwanted user after demostration
# https://stackoverflow.com/questions/11448068/mysql-error-code-1175-during-update-in-mysql-workbench
SET SQL_SAFE_UPDATES = 0;
delete from users where userID = 'takana';
SET SQL_SAFE_UPDATES = 1;
