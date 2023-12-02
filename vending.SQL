CREATE TABLE items (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    slot TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL
);

CREATE TABLE purchase_history (
    id INTEGER PRIMARY KEY,
    item_id INTEGER,
    quantity INTEGER,
    purchase_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (item_id) REFERENCES items (id)
);

INSERT INTO items (name, slot, quantity, price) VALUES ('Water', 'A1', 8, 1.00);
INSERT INTO items (name, slot, quantity, price) VALUES ('Water', 'A2', 8, 1.00);
INSERT INTO items (name, slot, quantity, price) VALUES ('Water', 'A3', 8, 1.00);
INSERT INTO items (name, slot, quantity, price) VALUES ('Water', 'A4', 8, 1.00);

INSERT INTO items (name, slot, quantity, price) VALUES ('Energy Drink', 'B1', 8, 1.50);
INSERT INTO items (name, slot, quantity, price) VALUES ('Energy Drink', 'B2', 8, 1.50);
INSERT INTO items (name, slot, quantity, price) VALUES ('Energy Drink', 'B3', 8, 1.50);
INSERT INTO items (name, slot, quantity, price) VALUES ('Energy Drink', 'B4', 8, 1.50);

INSERT INTO items (name, slot, quantity, price) VALUES ('Energy Bar', 'C1', 8, 1.25);
INSERT INTO items (name, slot, quantity, price) VALUES ('Energy Bar', 'C2', 8, 1.25);
INSERT INTO items (name, slot, quantity, price) VALUES ('Energy Bar', 'C3', 8, 1.25);
INSERT INTO items (name, slot, quantity, price) VALUES ('Energy Bar', 'C4', 8, 1.25);

INSERT INTO items (name, slot, quantity, price) VALUES ('Chips', 'D1', 8, 0.99);
INSERT INTO items (name, slot, quantity, price) VALUES ('Chips', 'D2', 8, 0.99);
INSERT INTO items (name, slot, quantity, price) VALUES ('Chips', 'D3', 8, 0.99);
INSERT INTO items (name, slot, quantity, price) VALUES ('Chips', 'D4', 8, 0.99);

INSERT INTO items (name, slot, quantity, price) VALUES ('Skittles', 'E1', 8, 0.75);
INSERT INTO items (name, slot, quantity, price) VALUES ('Skittles', 'E2', 8, 0.75);
INSERT INTO items (name, slot, quantity, price) VALUES ('Skittles', 'E3', 8, 0.75);
INSERT INTO items (name, slot, quantity, price) VALUES ('Skittles', 'E4', 8, 0.75);

INSERT INTO items (name, slot, quantity, price) VALUES ('Gummies', 'F1', 8, 1.20);
INSERT INTO items (name, slot, quantity, price) VALUES ('Gummies', 'F2', 8, 1.20);
INSERT INTO items (name, slot, quantity, price) VALUES ('Gummies', 'F3', 8, 1.20);
INSERT INTO items (name, slot, quantity, price) VALUES ('Gummies', 'F4', 8, 1.20);
