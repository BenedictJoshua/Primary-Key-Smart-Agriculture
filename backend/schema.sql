create database if not exists smart_agriculture;
use smart_agriculture;

create table users (
    user_id int auto_increment primary key,
    name varchar(100) not null,
    email varchar(100) unique,
    phone varchar(15),
    created_at timestamp default current_timestamp
);

create table farms (
    farm_id int auto_increment primary key,
    user_id int not null,
    farm_name varchar(100) not null,
    location varchar(100),
    area_acres decimal(10,2),
    foreign key (user_id) references users(user_id)
);

create table soil_data (
    soil_id int auto_increment primary key,
    farm_id int not null,
    soil_type varchar(50) not null,
    ph_level decimal(4,2),
    nitrogen decimal(8,2),
    phosphorus decimal(8,2),
    potassium decimal(8,2),
    foreign key (farm_id) references farms(farm_id)
);

create table crops (
    crop_id int auto_increment primary key,
    crop_name varchar(100) not null,
    suitable_soil varchar(100),
    min_ph decimal(4,2),
    max_ph decimal(4,2),
    description varchar(500)
);

create table crop_recommendations (
    recommendation_id int auto_increment primary key,
    farm_id int not null,
    crop_id int not null,
    recommendation_date timestamp default current_timestamp,
    confidence_score decimal(5,2),
    reason varchar(500),
    foreign key (farm_id) references farms(farm_id),
    foreign key (crop_id) references crops(crop_id)
);

insert into users (name, email, phone)
values ('Demo Farmer', 'farmer@example.com', '9876543210');

insert into farms (user_id, farm_name, location, area_acres)
values (1, 'Demo Farm', 'Tamil Nadu', 5.00);

insert into soil_data
(farm_id, soil_type, ph_level, nitrogen, phosphorus, potassium)
values (1, 'Loamy', 6.5, 90, 45, 40);

insert into crops
(crop_name, suitable_soil, min_ph, max_ph, description)
values
('Rice', 'Loamy', 5.5, 7.0,
 'Suitable for warm and water-rich agricultural conditions.');

insert into crops
(crop_name, suitable_soil, min_ph, max_ph, description)
values
('Maize', 'Loamy', 5.8, 7.0,
 'Suitable for well-drained fertile soil.');

insert into crops
(crop_name, suitable_soil, min_ph, max_ph, description)
values
('Groundnut', 'Sandy', 6.0, 7.5,
 'Performs well in light and well-drained soil.');