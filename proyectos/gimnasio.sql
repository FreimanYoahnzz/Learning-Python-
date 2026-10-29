DROP TABLE IF EXISTS SOCIOS;
DROP TABLE IF EXISTS PLANES;


CREATE TABLE PLANES (
ID INTEGER PRIMARY KEY,
NOMBRE TEXT UNIQUE NOT NULL,
PRECIO REAL NOT NULL,
DURACION_DIAS INT
);

CREATE TABLE SOCIOS (
ID INTEGER PRIMARY KEY,
NOMBRE TEXT NOT NULL,
TELEFONO TEXT,
PLAN_ID INTEGER REFERENCES PLANES(ID),
FECHA_INICIO TEXT,
FECHA_VENCIMIENTO TEXT,
ACTIVO INT DEFAULT 1
--plan_id se podria expresar de esta forma también: 
--FOREIGN KEY (PLAN_ID) REFERENCES PLANES(ID)
);


INSERT INTO PLANES (NOMBRE, PRECIO, DURACION_DIAS)
VALUES ('MENSUAL', 100000, 31),
		('TRIMESTRAL', 278999, 95),
		('ANUAL', 999999, 365);
		
INSERT INTO SOCIOS (NOMBRE, TELEFONO, PLAN_ID, FECHA_INICIO, FECHA_VENCIMIENTO, ACTIVO)
VALUES ('FREIMAN', '+57 3207549772', 1, '2026-10-28', '2026-11-29', 1),
		('MARINELA', NULL, 3, '2026-09-01', '2027-09-01', 1),
		('JIMENA', '+57 3138897543', 3, '2026-06-26', '2027-06-26', 1),
		('JULIO', '+57 3004337659', 2, '2026-09-15', '2026-12-15', 1),
		('JOSÉ', '+67 4572298', 1, '2026-09-28', '2026-10-28', 0),
		('JOSEFINA', '+1 276459234', 1, '2025-01-01', '2026-01-01', 1),
		('CARLOS', NULL, 3, '2026-09-01', '2027-09-01', 1),
		('DANIELA', '+57 3048270345', 2, '2026-08-07', '2026-11-07', 1);
		
		
--consultas
-- muestra todos los socios que tengan su plan ACTIVO, y los ordena por NOMBRE 
SELECT NOMBRE FROM SOCIOS WHERE ACTIVO = 1 ORDER BY NOMBRE;

-- muestra el NOMBRE de los 3 socios a quienes están más proxímos a vencer su plan, y que tienen su plan activo
SELECT NOMBRE FROM SOCIOS WHERE ACTIVO = 1 ORDER BY FECHA_VENCIMIENTO ASC LIMIT 3; 

-- muestra el NOMBRE de los socios que empiecen con la letra F
SELECT NOMBRE FROM SOCIOS WHERE NOMBRE LIKE 'F%';

-- muestra el NOMBRE de los socios que no registraron numero de TELEFONO
SELECT NOMBRE FROM SOCIOS WHERE TELEFONO IS NULL;

-- muestra el NOMBRE de los socios quienes tienen el plan mensual, se encuentra activo y vencen antes del 2026-11-30
SELECT NOMBRE FROM SOCIOS WHERE PLAN_ID = 1 AND ACTIVO = 1 AND FECHA_VENCIMIENTO < '2026-11-30';

-- cambia el plan, asigna la fecha de inicio y la fecha de vencimiento del plan, para el socio que tiene asignado el ID 8
UPDATE SOCIOS SET PLAN_ID = 1, FECHA_INICIO = '2026-10-26', FECHA_VENCIMIENTO = '2026-11-26' WHERE ID = 8;

-- cambia el estado de activo para los socios a quienes ya se les venció el plan y lo tenían activo
 UPDATE SOCIOS SET ACTIVO = 0 WHERE ACTIVO = 1 AND FECHA_VENCIMIENTO < '2026-10-28';

-- elimina al socio cuyo ID es 6 y su plan esta desactivado
DELETE FROM SOCIOS WHERE ACTIVO = 0 AND ID = 6;
	