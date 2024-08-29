CREATE TABLE message (
	message_id bigint primary key auto_increment,
    user_id bigint not null,
    question varchar(1000) not null,
    reply varchar(1000) not null,
    emotion varchar(30) not null default '보통',
	regdate Datetime not null default now()
);
CREATE TABLE user (
	user_id bigint primary key auto_increment,
	username varchar(100) not null,
    connect_ip varchar(100) not null,
	regdate Datetime not null default now()
);
