# TRABAJO FINAL CURSO 2020

### Enunciado del Problema a Resolver

Una clínica de Optometría necesita un sistema web en Django que le permita gestionar el diagnóstico de sus pacientes y la venta de los productos Ópticos para los mismos. Para ello se requiere:

<ol>
    <li>Un sistema con un login de usuario con los siguientes roles:</li>
    <ol type="a">
        <li>Secretaría</li>
        <li>Profesional médico</li>
        <li>Ventas</li>
        <li>Taller</li>
        <li>Gerencia</li>
    </ol>
    <li>El sistema gestionará tres Modelos esenciales:</li>
    <ol type="a">
        <li>Turnos</li>
        <li>Pedidos</li>
        <li>Pacientes</li>
    </ol>
    <li>El rol de Secretaría permite agregar, modificar o eliminar los turnos de los Pacientes.</li>
    <li>Cada Paciente tiene su historial médico (solo el Profesional médico puede agregar Observaciones al historial médico).</li>
    <li>Cada Profesional médico puede ver el listado de Pacientes filtrando por día, mes o año.</li>
    <li>El Profesional médico solo puede ver los Pacientes asignados a él.</li>
    <li>El rol de Ventas puede generar un pedido para el Paciente, donde detalla el Producto que quiere adquirir, el precio (pueden ser más de un producto), un  subtotal, tipo de pago (tarjeta de crédito, debido, billetera virtual o efectivo).</li>
    <ol type="a">
        <li>El producto tiene nombre, si está clasificado como Lente tendrá la opción de Lejos/Cerca, Izquierda/Derecha, si incluye Armazón o no.</li>
        <li>Una vez que se genera el pedido queda en estado “Pendiente”.</li>
        <li>Luego el rol de Ventas puede cambiar el estado a “Pedido” o mandarlo a “Taller”.</li>
    </ol>
    <li>El rol de Taller solo visualiza la lista de pedidos (con todos los detalles del producto sin los precios). El Taller puede confirmar cambiando el estado del pedido a “Finalizado”.</li>
    <li>Gerencia puede visualizar todos los datos y necesita los siguientes reportes:</li>
    <ol type="a">
        <li>Pacientes que asistieron a los turnos en la semana/mes.</li>
        <li>Pacientes que no asistieron a los turnos en la semana/mes.</li>
        <li>Pacientes que hicieron por lo menos un Pedido en la semana/mes.</li>
        <li>Productos más vendidos en el mes.</li>
        <li>Ventas totales por mes clasificadas por Vendedores.</li>
    </ol>
</ol>



### Requisitos Obligatorios

<ol>
    <li>Se deben cumplir cada uno de los puntos definidos en el enunciado para la aprobación del trabajo.</li>
    <li>El sistema debe estar implementado en Django.</li>
    <li>El sistema debe implementar Bootstrap.</li>
    <li>El frontend se deja a libre albedrio, pero debe poder visualizarse correctamente en dispositivos móviles (responsivo).</li>
    <li>Se pueden agregar todos los Modelos adicionales que se necesiten.</li>
    <li>Se debe implementar sobre base de datos SQLite.</li>
    <li>Se debe publicar un video de YouTube que demuestre el funcionamiento de todo el sistema.</li>
    <ol type="a">
        <li>El video debe tener en el titulo el nombre del curso completo.</li>
        <li>En la descripción del video debe estar el nombre del curso, el nombre de la persona que presenta y su número de documento con el que se registró al curso.</li>
        <li>En la descripción del video tiene que estar anotado el tiempo (minuto y segundo) de cada uno de los (9) puntos resueltos en el enunciado, mostrando su funcionalidad y la cumplimentación de los requerido.</li>
    </ol>
    <li>Se debe publicar un enlace con el código fuente publicado en GitHub con el usuario de la persona registrada en el curso.
    <li>Se debe adjuntar el código fuente comprimido en .zip Cualquier falla en cumplimentar uno de los requisitos o puntos del enunciado ___derivará en la desaprobación___ del Trabajo Final sin posibilidad a recuperación. Es condición necesaria para la certificación de Desarrollador Full Stack con Python y JavaScript la aprobación del presente trabajo.</li>
</ol>

### Enlace del Formulario de Presentación

Todos los inscriptos, sin distinción, deberán presentar el Trabajo Final 2020 por medio del siguiente formulario [https://forms.gle/yaBkU1RtDTzCpS1u8](https://forms.gle/yaBkU1RtDTzCpS1u8)


