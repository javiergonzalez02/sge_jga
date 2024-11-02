## Integración de Google Custom Search API para Imágenes de Productos en Odoo

### Pasos a Seguir

1. **Activar el Módulo de Inventario**

   - Navega al menú de aplicaciones en Odoo.
   - Busca el módulo **Inventario** y haz clic en **Activar**.

2. **Importar Productos desde un Archivo Excel**

   - Ve a **Inventario > Productos > Productos**.
   - Haz clic en **Favoritos > Importar registros**.
   - Selecciona el archivo, en este caso `libros.xls`, y súbelo.
   - Asegúrate de mapear correctamente los campos **Título**, **Precio** y **EAN**. Desmarca la opción de **Imagen**, ya que se cargará desde la API.
   - Haz clic en **Importar**.

3. **Obtener y Configurar la Clave API de Google**

   3.1. **Crear una Clave API**
   
   - Accede a [Google API's y Servicios](https://console.cloud.google.com/apis/credentials).
   - Selecciona o crea un nuevo proyecto.
   - Ve a **Credenciales** y haz clic en **Crear credenciales > Clave de API**.
   - Copia y guarda la clave generada.
   
   3.2. **Habilitar Custom Search API**
   
   - En el panel de **Biblioteca**, busca **Custom Search API**.
   - Haz clic en **Habilitar**.

4. **Crear un Motor de Búsqueda Programable**

   - Accede a [Google Programmable Search Engine](https://programmablesearchengine.google.com).
   - Haz clic en **Añadir**.
   - Configura tu buscador:
     - **Nombre**: Asigna un nombre descriptivo.
     - **Dónde buscar**: Selecciona **Buscar en toda la web**.
     - **Configuración de búsqueda**: Activa **Búsqueda por imágenes** y **Búsqueda segura**.
   - Completa el CAPTCHA y haz clic en **Crear**.
   - Copia el **ID del buscador**.

5. **Configurar Odoo para Usar la API de Google**

   - En Odoo, ve a **Ajustes > Opciones generales > Integraciones**.
   - Activa la opción **Obtener imágenes de Google** y guarda.
   - Introduce la **Clave API** y el **ID del motor de búsqueda** previamente obtenidos.
   - Guarda los cambios.

6. **Asignar Imágenes a los Productos**

   - Regresa a **Inventario > Productos > Productos**.
   - Abre un producto sin imagen.
   - En el desplegable de **Acción**, selecciona **Obtener imagen**.
   - Odoo buscará y asignará automáticamente una imagen basada en el código EAN.

[Ver resultado](./imagenProductos.png)

Así estará configurada la búsqueda de imágenes de Google en Odoo para los productos.
