import numpy as np

dt = np.dtype([('codigo', 'U10'), ('nombre', 'U50'), ('promedio_acumulado', float), ('carrera', 'U20'), ('fecha_ingreso', 'U10')])

estudiantes = np.array([], dtype=dt)

num_estudiantes = 6500
for i in range(num_estudiantes):
    codigo = f"UIS{i + 1:04d}"  
    nombre = np.random.choice(['Juan', 'Maria', 'Luis', 'Ana', 'Pedro', 'Andrea', 'David', 'Sandra', 'German', 'Heyner', 'Victoria', 'Nicolas'])
    promedio_acumulado = np.random.uniform(2.0, 5.0)  
    carrera = np.random.choice(['Ing. Sistemas', 'Ing. Industrial', 'Matematicas', 'Ing. Metalurgica', 'Ing. Mecanica', 'Musica', 'Ing. Electronica', 'Derecho', 'Lenguas'])
    fecha_ingreso = f"{np.random.randint(1982, 2023):04d}-18-01"  
    
    estudiante = np.array([(codigo, nombre, promedio_acumulado, carrera, fecha_ingreso)], dtype=dt)
    estudiantes = np.append(estudiantes, estudiante)

carrera_a_buscar = np.random.choice(['Ing. Sistemas', 'Ing. Industrial', 'Matematicas', 'Ing. Metalurgica', 'Ing. Mecanica', 'Musica', 'Ing. Electronica', 'Derecho', 'Lenguas'])
estudiantes_carrera_x = estudiantes[(estudiantes['carrera'] == carrera_a_buscar) & (estudiantes['promedio_acumulado'] >= 4)]

print("Estudiantes de la carrera {} con promedio acumulado >= 4.0:".format(carrera_a_buscar))
for estudiante in estudiantes_carrera_x:
    promedio_redondeado = round(estudiante['promedio_acumulado'], 3)  
    print("Código: {}, Nombre: {}, Promedio: {:.3f}".format(estudiante['codigo'], estudiante['nombre'], promedio_redondeado))
print("Total: {}".format(len(estudiantes_carrera_x)))

estudiantes_condicionales = estudiantes[(estudiantes['fecha_ingreso'] < '1990-01-01') & (estudiantes['promedio_acumulado'] < 3.2)]

print("Estudiantes que ingresaron antes de 1990 y están condicionales:")
for estudiante in estudiantes_condicionales:
    promedio_redondeado = round(estudiante['promedio_acumulado'], 3)  
    print("Código: {}, Nombre: {}, Fecha de Ingreso: {}, Promedio: {:.3f}".format(estudiante['codigo'], estudiante['nombre'], estudiante['fecha_ingreso'], promedio_redondeado))

promedio_general = np.mean(estudiantes['promedio_acumulado'])
print("Promedio de todos los estudiantes: {:.3f}".format(promedio_general))

carreras = np.unique(estudiantes['carrera'])
for carrera in carreras:
    estudiantes_carrera = estudiantes[estudiantes['carrera'] == carrera]
    estudiantes_con_4_o_mas = estudiantes_carrera[estudiantes_carrera['promedio_acumulado'] >= 4.0]
    print("Carrera {}: {} estudiantes con 4.0 o más".format(carrera, len(estudiantes_con_4_o_mas)))
