net localgroup docker-users %USERDOMAIN%\%USERNAME% /add

docker run -d -e MYSQL_DATABASE=employees -e MYSQL_USER=employees -e MYSQL_PASSWORD=employees -e
MYSQL_ALLOW_EMPTY_PASSWORD=yes -p 3306:3306 --name employees-mariadb mariadb

# belépés a docker containerbe

docker exec -it employess-mariadb bash

# mysql szerverbe beléps

mysql

# db kiválasztása

use employees;

# queryk futatása

select * from employees
