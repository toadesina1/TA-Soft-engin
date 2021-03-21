
INSERT INTO post  (
            "id": "integer primary key autoincrement",
            "title": "text not null",
            "url": "text not null",
            "notes": "text",
            "date_added": "text not null",
        )
VALUES ('01', 'test' || x'www.go.com' || 'di we get it in', '2021-03-18 00:00:00');