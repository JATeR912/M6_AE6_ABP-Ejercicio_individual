# 🛠️ Proyecto Django - Gestión de Productos

Este proyecto implementa una aplicación web en Django para la gestión de productos, con control de acceso mediante usuarios, grupos y permisos personalizados. A continuación, se detallan los requerimientos cumplidos y configuraciones implementadas.

---
## ✅🔒 Funcionalidades principales: Control de usuarios, grupos y permisos.
Manejo de usuarios, grupos y permisos en el sitio administrativo de Django

### 1. Creación de un Superusuario

Se ha creado un **superusuario** utilizando el comando:
  ```bash
  python manage.py createsuperuser
  ```
Este superusuario tiene acceso completo al sitio administrativo de Django.

### 2. Acceso al Sitio Administrativo
Se inicia el servidor de desarrollo con:

```bash
python manage.py runserver
```
El panel de administración está disponible en:
👉 http://127.0.0.1:8000/admin/


El superusuario puede iniciar sesión y administrar todos los modelos y configuraciones.

### 3. Creación de un Modelo de Producto
Se ha creado un modelo Producto con los siguientes campos:

```bash
nombre (CharField)

descripcion (TextField)

precio (DecimalField)

stock (PositiveIntegerField)

fecha_creacion (DateTimeField, auto_now_add)
```

El modelo ha sido registrado en admin.py para su gestión desde el panel de administración.

### 4. Manejo de Usuarios
Se han creado varios usuarios con distintos niveles de permisos.

Se asegura que:

 - Solo los administradores pueden eliminar productos.

 - Otros usuarios tienen accesos según su grupo asignado.

### 5. Grupos de Autorización Configurados
Se han definido los siguientes grupos con permisos específicos:
| Rol                      | Permisos | Acciones permitidas           |
| ------------------------ | -------- | ----------------------------- |
| **Administrador**            | **CRUD** | Crear, Leer, Editar, Eliminar |
| **Gestor de productos**      | **CRU**  | Crear, Leer, Editar           |
| **Colaborador de productos** | **CR**   | Crear, Leer                   |
| **Visualizador**             | **R**    | Solo Leer                     |


Los usuarios asignados a estos grupos tienen acceso controlado y limitado según los permisos correspondientes.

### 6. Configuración de Permisos para Usuarios
Los permisos se gestionan desde la interfaz administrativa, asignando acciones específicas a cada grupo y usuario.

Se ha probado que los permisos aplican correctamente:

 - Los usuarios sin permisos no pueden acceder a funciones restringidas.

 - Las acciones no autorizadas redirigen a una página personalizada de error 403 (Prohibido).

### 7. Página de Error 403 Personalizada
Cuando un usuario intenta acceder a una funcionalidad no permitida:

 - Es redirigido a una página de error 403 - Acceso Denegado.

La página incluye:

 - Mensaje explicativo.

 - Opción para cerrar sesión.

 - Enlace para volver al inicio del sitio.

Esto asegura una experiencia clara y segura para el usuario.

### 8. Limitación de Acceso al Sitio Administrativo
El acceso a /admin/ está restringido exclusivamente a usuarios autenticados.

Los usuarios no registrados son redirigidos automáticamente a la página de inicio de sesión.

### 9. Manejo de Errores en el Modelo Auth
Se manejan correctamente errores de autenticación, tales como:

 - Contraseñas incorrectas.

 - Intentos de acceso con usuarios no autorizados.

 - Se muestran mensajes claros y amigables al usuario.

### 10. Pruebas de Roles y Permisos
Se ha verificado que cada tipo de usuario accede únicamente a las funcionalidades habilitadas por su grupo.

Acciones no permitidas muestran el error 403, sin comprometer la seguridad del sistema.



