#Año con mas carreras
select *, count(*) as conteo FROM RACES
group by year
order by conteo desc;


#Piloto con mayor cantidad de primeros puestos
select driverid, COUNT(*) as conteo FROM results
where position = 1
GROUP BY (driverid)
order by conteo desc;


#Nombre del circuito más corrido
select *, COUNT(circuits.circuitid) as conteo
FROM races
INNER JOIN circuits
ON races.circuitid = circuits.circuitid
GROUP BY (circuits.name)
order by conteo desc;


#Piloto con mayor cantidad de puntos en total, cuyo constructor sea de nacionalidad sea American o British
select *, sum(points) as conteo FROM results 
inner join drivers
on results.driverid = drivers.driverid
inner join constructors
on constructors.constructorid = results.constructorid
group by drivers.driverid;
