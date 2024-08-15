SHOW TABLES;
SELECT * FROM alembic_version;
DROP TABLE alembic_version;
CREATE TABLE message (
	message_id bigint primary key auto_increment,
    user_id bigint not null,
    question varchar(1000) not null,
    reply varchar(1000) not null,
	regdate Datetime not null default now()
);

DROP TABLE message;

INSERT INTO message (
	user_id,
    question,
    reply
)VALUES (
	1,
    '너의 이름은?',
    '수희'
);

SELECT * FROM message;

CREATE TABLE user (
	user_id bigint primary key auto_increment,
	username varchar(100) not null,
    connect_ip varchar(20) not null,
	regdate Datetime not null default now()
);


SELECT * FROM message LIMIT 5;

