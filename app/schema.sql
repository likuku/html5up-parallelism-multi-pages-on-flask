drop table if exists setting;
create table setting (
  id integer primary key autoincrement,
  key string not null,
  value string not null
);

drop table if exists contact;
create table contact (
  id integer primary key autoincrement,
  href string not null,
  class_name string not null,
  label string,
  example string,
  display string default 'Yes',
  check (display = 'Yes' or display = 'No' )
);

drop table if exists project;
create table project (
  id integer primary key autoincrement,
  name string not null,uniq,
  display string default 'Yes',
  check (display = 'Yes' or display = 'No' )
);

drop table if exists photo;
create table photo (
  id integer primary key autoincrement,
  href string not null,
  src string not null,
  width integer not null,
  project_id integer,
  show_on_homepage string default 'Yes',
  display string default 'Yes',
  check (show_on_homepage = 'Yes' or show_on_homepage = 'No'),
  check (display = 'Yes' or display = 'No')
);

drop table if exists projects_photos;
create table projects_photos (
  project_id integer not null,
  photo_id integer not null,
  primary key (project_id, photo_id)
);

insert into setting (key, value) values ('logo', 'likuku');
insert into setting (key, value) values ('bg_img', 'https://wx4.sinaimg.cn/large/4d48a5a9gy1fn2e6ivc6oj21kw1fk1kx.jpg');

insert into contact (href, class_name, label, example) values ('#','icon fa-twitter','Twitter','https://twitter.com/someone');
insert into contact (href, class_name, label) values ('#','icon fa-instagram','Instagram');
insert into contact (href, class_name, label) values ('#','icon fa-facebook','Facebook');
insert into contact (href, class_name, label) values ('#','icon fa-dribbble','Dribbble');
insert into contact (href, class_name, label) values ('#','icon fa-pinterest','Pinterest');
insert into contact (href, class_name, label) values ('#','icon fa-weixin','Wechat');
insert into contact (href, class_name, label, example) values ('#','icon fa-envelope','Email','mailto:someone@domain.name');

insert into project (name) values ('Sun');
insert into project (name) values ('Luna');
insert into project (name) values ('Mars');

insert into photo (href, src, width, project_id) values ('https://farm3.staticflickr.com/2839/12237482636_d71fbbda2a_z.jpg','https://farm3.staticflickr.com/2839/12237482636_d71fbbda2a_n.jpg','279','1');
insert into photo (href, src, width, project_id) values ('https://farm3.staticflickr.com/2839/12237482636_d71fbbda2a_z.jpg','https://farm3.staticflickr.com/2839/12237482636_d71fbbda2a_n.jpg','279','1');
insert into photo (href, src, width, project_id) values ('https://farm3.staticflickr.com/2839/12237482636_d71fbbda2a_z.jpg','https://farm3.staticflickr.com/2839/12237482636_d71fbbda2a_n.jpg','279','1');
insert into photo (href, src, width, project_id) values ('https://farm3.staticflickr.com/2839/12237482636_d71fbbda2a_z.jpg','https://farm3.staticflickr.com/2839/12237482636_d71fbbda2a_n.jpg','279','1');
insert into photo (href, src, width, project_id) values ('https://farm3.staticflickr.com/2839/12237482636_d71fbbda2a_z.jpg','https://farm3.staticflickr.com/2839/12237482636_d71fbbda2a_n.jpg','279','2');
insert into photo (href, src, width, project_id) values ('https://farm3.staticflickr.com/2839/12237482636_d71fbbda2a_z.jpg','https://farm3.staticflickr.com/2839/12237482636_d71fbbda2a_n.jpg','279','2');
insert into photo (href, src, width, project_id) values ('https://farm3.staticflickr.com/2839/12237482636_d71fbbda2a_z.jpg','https://farm3.staticflickr.com/2839/12237482636_d71fbbda2a_n.jpg','279','3');
insert into photo (href, src, width, project_id) values ('https://farm3.staticflickr.com/2839/12237482636_d71fbbda2a_z.jpg','https://farm3.staticflickr.com/2839/12237482636_d71fbbda2a_n.jpg','279','3');

insert into projects_photos (project_id, photo_id) values (1,1);
insert into projects_photos (project_id, photo_id) values (1,2);
insert into projects_photos (project_id, photo_id) values (1,3);
insert into projects_photos (project_id, photo_id) values (1,4);
insert into projects_photos (project_id, photo_id) values (2,5);
insert into projects_photos (project_id, photo_id) values (2,6);
insert into projects_photos (project_id, photo_id) values (2,7);
insert into projects_photos (project_id, photo_id) values (2,8);
insert into projects_photos (project_id, photo_id) values (3,3);
insert into projects_photos (project_id, photo_id) values (3,5);
insert into projects_photos (project_id, photo_id) values (3,7);
insert into projects_photos (project_id, photo_id) values (3,1);
