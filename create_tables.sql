CREATE TABLE employee
(
    employee_id integer primary key not null,
    first_name  varchar(50),
    last_name   varchar(50),
    title       varchar(100),
    birth_date  date,
    notes       text
);

CREATE TABLE customers
(
    customer_id  varchar(50) primary key not null,
    company_name varchar(100),
    contact_name varchar(100)
);

CREATE TABLE orders
(
    order_id    integer primary key not null,
    customer_id varchar(50),
    employee_id integer,
    order_date  date,
    ship_city   varchar(50),
    foreign key (customer_id) references customers (customer_id)
        match simple on update no action on delete no action,
    foreign key (employee_id) references employee (employee_id)
        match simple on update no action on delete no action
);