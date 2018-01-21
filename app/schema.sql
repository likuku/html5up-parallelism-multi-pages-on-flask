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
  name string not null unique,
  display string default 'Yes',
  check (display = 'Yes' or display = 'No' )
);

drop table if exists photo;
create table photo (
  id integer primary key autoincrement,
  href string not null unique,
  src string not null unique,
  width integer not null,
  project_id integer,
  description string,
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

insert into photo (href, src, width, project_id) values ('https://farm3.staticflickr.com/2839/12237482636_d71fbbda2a_b.jpg','https://farm3.staticflickr.com/2839/12237482636_d71fbbda2a.jpg','279','3');
insert into photo (href, src, width, project_id) values ('https://farm6.staticflickr.com/5526/12155438034_d3c6e222be_b.jpg','https://farm6.staticflickr.com/5526/12155438034_d3c6e222be.jpg','279','3');
insert into photo (href, src, width, project_id) values ('https://farm6.staticflickr.com/5474/10271445013_8f279857c3_b.jpg','https://farm6.staticflickr.com/5474/10271445013_8f279857c3.jpg','228','1');
insert into photo (href, src, width, project_id) values ('https://farm6.staticflickr.com/5493/10292646283_f7dc10c7a5_b.jpg','https://farm6.staticflickr.com/5493/10292646283_f7dc10c7a5.jpg','300','1');
insert into photo (href, src, width, project_id) values ('https://farm3.staticflickr.com/2844/10138375634_ded44a78df_b.jpg','https://farm3.staticflickr.com/2844/10138375634_ded44a78df_m.jpg','228','1');
insert into photo (href, src, width, project_id) values ('https://farm8.staticflickr.com/7434/10102294576_fd4ce0e566_b.jpg','https://farm8.staticflickr.com/7434/10102294576_fd4ce0e566_m.jpg','228','3');
insert into photo (href, src, width, project_id) values ('https://farm4.staticflickr.com/3825/9708725741_e239098763_b.jpg','https://farm4.staticflickr.com/3825/9708725741_e239098763_m.jpg','228','3');
insert into photo (href, src, width, project_id) values ('https://farm3.staticflickr.com/2874/9689232803_9dbd0e27a1_b.jpg','https://farm3.staticflickr.com/2874/9689232803_9dbd0e27a1_m.jpg','228','3');
insert into photo (href, src, width, project_id) values ('https://farm9.staticflickr.com/8056/8113187059_901c195d8c_b.jpg','https://farm9.staticflickr.com/8056/8113187059_901c195d8c.jpg','300','2');
insert into photo (href, src, width, project_id) values ('https://farm9.staticflickr.com/8476/8076607041_542851ebca_b.jpg','https://farm9.staticflickr.com/8476/8076607041_542851ebca_n.jpg','300','1');
insert into photo (href, src, width, project_id) values ('https://farm6.staticflickr.com/5498/11710413895_41d1f2359c_b.jpg','https://farm6.staticflickr.com/5498/11710413895_41d1f2359c_n.jpg','300','2');
insert into photo (href, src, width, project_id) values ('https://farm7.staticflickr.com/6122/5997931902_1a621b7356_b.jpg','https://farm7.staticflickr.com/6122/5997931902_1a621b7356_n.jpg','300','2');
insert into photo (href, src, width, project_id) values ('https://farm6.staticflickr.com/5261/5758567895_ded256d52c_b.jpg','https://farm6.staticflickr.com/5261/5758567895_ded256d52c_m.jpg','228','2');
