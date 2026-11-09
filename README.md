# primero descarga el proyecto
git clone "url-proyecto"

# segundo instala las librerias necesarias
pip o pipenv install -r requirements.txt

# luego hacer migraciones
py manage.py migrate

# si da error hacer makemigrations

# NO SE OLVIDEN DE SU RAMA 

# HISTORIAS DE USUARIOS A TRABJAR EN MGOMEZ
HU03 - Consulta centralizada de horarios: Como usuario, quiero visualizar la parrilla horaria general de forma rápida y centralizada.   
HU06 - Detalle de asignaturas electivas y talleres: Como estudiante/apoderado, quiero ver el detalle y la oferta de asignaturas electivas y talleres.   
HU07 - Reserva digital de espacios comunes: Como docente o administrativo, quiero solicitar la reserva de recintos o salas comunes del liceo.   
HU08 - Validación de cruces en reservas: Como sistema, quiero validar automáticamente que no existan choques de horarios en las reservas de espacios.   
HU09 - Mapa de orientación digital (Wayfinding): Como visitante o estudiante, quiero ver un mapa visual para orientarme y ubicar salas/pabellones en el establecimiento.   
HU11 - Consulta de horarios de salida diarios: Como apoderado/alumno, quiero revisar los horarios de salida programados para la jornada diaria.   
HU12 - Registro de suspensiones y avisos de jornada: Como usuario, quiero estar informado sobre suspensiones de clases o cambios imprevistos en la jornada.   HU13 - Identificación visual de profesores volantes: Como inspectoría/docente, quiero identificar qué profesores se encuentran volantes o disponibles.   
HU14 - Coordinación horaria y articulación PIE: Como equipo docente, quiero visualizar la coordinación del programa PIE dentro de la parrilla horaria.   
HU16 - Exportación de horario semanal a PDF: Como usuario, quiero exportar la información del horario en formato PDF para descarga o impresión. 

estoy a cargo de la Intranet Principal (la cara visible / landing institucional que ven los usuarios al ingresar)