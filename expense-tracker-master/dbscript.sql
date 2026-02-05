use kbnhzraf_ticketdb;

DROP TABLE IF EXISTS expenses;
DROP TABLE IF EXISTS expense_categories;

CREATE TABLE expense_categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    description VARCHAR(255) NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    date DATE NOT NULL,
    category_id INT,
    CONSTRAINT fk_category
        FOREIGN KEY (category_id) REFERENCES expense_categories(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);

-- Insert categories
INSERT INTO expense_categories (name) VALUES ('Food'), ('Travel'), ('Rent'), ('Utilities'),('Others');

