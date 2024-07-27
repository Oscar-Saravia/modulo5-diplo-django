## Modulo V - DJANGO

---

**DOCENTE**: Marcelo Arteaga

**PARTICIPANTE**: Oscar Saravia Veizaga

---

## Propósito:

- Demostrar los conocimientos adquiridos en la creación de un proyecto en
Django.

## Requerimientos:

- Cree un Proyecto en Django con al menos una Aplicación
- Su Aplicación debe tener al menos 4 Models (Modelos o Tablas)
- Sus Models deben contener al menos 2 validaciones personalizadas
- Su Administrador de Django debe tener al menos 2 Models registrados
- Utilice Django Rest Framework para crear al menos 3 ModelViewSet o
GenericAPIView
- Utilice Django Rest Framework para crear al menos 1 Custom API
- Debe incluir el archivo requirements.txt en la raíz del repositorio

---

## Descripción:

Este proyecto es un gestor de personajes de “Rick and Morty”, para registrar nuevos personajes de la serie, localizaciones relacionadas con la serie y recompensas por los personajes. Inspirado en el lore de la misma serie, se podrá asignar recompensas y registrar cazarrecompensas.

## Modelos:

1. **CHARACTER**:
    - **Campos**: id, name, status, species, gender, origin, last_location, image.
    - **Descripción**: representa la información de los personajes de Rick y Morty.
2. **LOCATION**:
    - **Campos**: id, name, type_location, dimesion.
    - **Descripción**: representa las diferentes localizaciones en la serie.
3. **LOG_CHARACTER**:
    - **Campos**: id, character_id(FK), location_id(FK), description, date_time.
    - **Descripción**: registra las diferentes localizaciones donde estuvo el personaje.
4. **BOUNTY**:
    - **Campos**: id, title, character_id(FK), search_status, description, amount, currency_type.
    - **Descripción**: registra las recompensas por cada personaje.
5. **HUNTER**:
    - **Campos**: id, name, nickname, image, skill.
    - **Descripción**: representa la información de los cazarrecompensas.
6. **CLAIMBOUNTY**:
    - **Campos**: id, hunter_id(FK), bounty_id(FK), date_time, claimed, claimed_at.
    - **Descripción**: representa el cambio de las recompensas y que usuarios están relacionados.

---

## **Integración con API Pública:**

- **API de Rick and Morty**: Datos de personajes y localizaciones obtenidos a través de la API pública y utilizados para poblar la base de datos del proyecto. (https://rickandmortyapi.com/)

---

## Pasos para Iniciar el Proyecto:

1. Migrar la base de datos y crear un superusuario.
    
    ```powershell
     python .\manage.py makemigrations
     python .\manage.py migrate
     python .\manage.py createsuperuser
    ```
    
2. Ejecutar el servidor de desarrollo de Django.
    
    ```powershell
    python .\manage.py runserver
    ```
    
3. Ejecutar el script de seed para poblar la base de datos.
    
    ```powershell
    python .\seed.py
    ```
    
4. Acceder a las vistas y administradores de Django para verificar la correcta implementación.
    
    > http://127.0.0.1:8000/admin/
    > 

---

## Rutas del Proyecto:

- [http://127.0.0.1:8000/](http://127.0.0.1:8000/admin/)
- http://127.0.0.1:8000/admin/
- [http://127.0.0.1:8000/a](http://127.0.0.1:8000/admin/)pi/
    - "characters": "http://127.0.0.1:8000/api/characters/"
    - "logCharacter": "http://127.0.0.1:8000/api/logCharacter/"
    - "claimBounty": "http://127.0.0.1:8000/api/claimBounty/"
- http://127.0.0.1:8000/swagger/