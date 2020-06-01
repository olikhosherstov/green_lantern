CREATE TABLE Dish (
    DishID SERIAL PRIMARY KEY NOT NULL,
    DishName VARCHAR(50) NOT NULL,
    Ingredients TEXT,
    Recipe TEXT,
    Weight INT CHECK(Weight > 0) NOT NULL
    );