CREATE TABLE Restaurant (
    RestaurantID SERIAL PRIMARY KEY,
    RestaurantName VARCHAR(50) NOT NULL,
    CountryID INT REFERENCES Country(CountryID),
    CityID INT REFERENCES City(CityID),
    Address CHAR(50) NOT NULL UNIQUE,
    MenuId INT REFERENCES RestaurantMenu(Id)
    );

