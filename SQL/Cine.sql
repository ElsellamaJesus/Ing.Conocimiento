--Creacion de Base de Datos
create database Cine
use Cine

--Creacion de Tablas
create table Peliculas(
id int primary key,
Pelicula varchar(50),
Genero varchar(50),
idYear int
)

create table Estreno(
idYear int primary key,
Year_ int
)

--Consultas
Select * from Peliculas

Select * from Estreno

Select Pelicula, Year_ from (Peliculas as p
inner join Estreno as e on
p.idYear = e.idYear) where id = 10

Select COUNT(Genero) as [Total Peliculas de Drama]
from Peliculas where Genero = 'Drama'

Select * From Peliculas
Order by id Desc;


