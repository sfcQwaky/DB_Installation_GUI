-------     PROJECT OVERVIEW    -------

- GUI project of installation of PostgreSQL or SQLite database


---     DESIGN PROCESS    ---

- INITIAL IDEAS

    - GUI elements
        - next button is the key, it will be on every screen
        - welcome screen, just a little description
        - type of DB
        - name of db
        - while db is being creating can I have some meter or percentage of done???

    - general details and other
        - I need font and two sizes declared as global variables, so it is standardized and neat
        -

----    2nd step updates     ----

    - DB creation
        - create db class in separate .py file
            - maybe that class should be used for all db types
        - do I need to select location where PostgreSQL is installed
        - probably some aspects like library or something else will be based on selected db type value

    - Other details
        - initial load to db, based on added csv file
            - it should be optional, basically step after db is installed
        - finish step on GUI

----    3nd step updates     ----

    - I'll need to figure out how to pack this in standalone installation exe file