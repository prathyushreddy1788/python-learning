# SQL Assignment Tasks

## Basic SQL Queries

1. Retrieve the names of all the countries in Asia.

Solution:

            SELECT Name
            FROM Country
            WHERE Continent = 'Asia';


2. Display the names of cities in the United Kingdom.

            SELECT Name
            FROM City
            WHERE CountryCode = 'GBR';


3. List the official languages of each country along with their names.

# Without names of country

            SELECT CountryCode, Language
            FROM CountryLanguage 
            WHERE IsOfficial = 'T';

# Withnames of country needs a join - can be discussed in 27Aug Session

4. Show the populations of cities in Brazil with a population over 1 million.

            SELECT Name, Population
            FROM City
            WHERE CountryCode = 'BRA' AND Population > 1000000;


5. Find the names of countries with an area larger than 2 million square kilometers.

            SELECT Name
            FROM Country
            WHERE SurfaceArea > 2000000;
