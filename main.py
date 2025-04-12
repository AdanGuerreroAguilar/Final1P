from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI(
    title="Final 1er Parcial ",
    description= "S-196 Adan Guerrero Aguilar",
    version="1.0.0"
)

libros=[ 
    {"id": 1, "titulo": "El Quijote", "año": 1615,  "autor": "Miguel de Cervantes"},
    {"id": 2, "titulo": "Cien años de soledad", "año": 1967, "autor": "Gabriel García Márquez"},
    {"id": 3, "titulo": "El amor en los tiempos del cólera", "año": 1985, "autor": "Gabriel García Márquez"},
    {"id": 4, "titulo": "La casa de los espíritus", "año": 1982, "autor": "Isabel Allende"},
    {"id": 5, "titulo": "Crónica de una muerte anunciada", "año": 1981, "autor": "Gabriel García Márquez"},
    {"id": 6, "titulo": "La sombra del viento", "año": 2001, "autor": "Carlos Ruiz Zafón"},
    {"id": 7, "titulo": "Los ojos de mi princesa", "año": 2004, "autor": "Carlos Cuauhtémoc Sánchez"},
    {"id": 8, "titulo": "La tregua", "año": 1960, "autor": "Mario Benedetti"},
    {"id": 9, "titulo": "Rayuela", "año": 1963, "autor": "Julio Cortázar"},
    {"id": 10, "titulo": "El túnel", "año": 1948, "autor": "Ernesto Sabato"}
]

@app.get("/",tags=["Inicio"])
def main():
    return {"Bienvenida": "Bienvenido a la API de libros"}

#endpoint para ver todos
@app.get("/libros",tags=["Libros"])
def TodosLibros():
    return {"Libros Registrados": libros}

#endpoint para ver uno
@app.get("/libros/{id}",tags=["Libros"])
def Libro(id: int):
    for libro in libros:
        if libro["id"] == id:
            return {"Libro": libro}
    raise HTTPException(status_code=404, detail="Libro no encontrado")

#endpoint para agregar
@app.post("/libros/",tags=["Libros"])
def AgregarLibro(LibroNuevo: dict):
    if "id" not in LibroNuevo or "titulo" not in LibroNuevo or "año" not in LibroNuevo or "autor" not in LibroNuevo:
        raise HTTPException(status_code=400, detail="Faltan datos")
    for libro in libros:
        if libro["id"] == LibroNuevo["id"]:
            raise HTTPException(status_code=400, detail="ID ya existe")
    libros.append(LibroNuevo)
    return {"Libro Agregado": LibroNuevo}

#endpoint para actualizar
@app.put("/libros/{id}",tags=["Libros"])
def ActualizarLibro(id: int, libro_actualizado: dict):
    for libro in libros:
        if libro["id"] == id:
            libro.update(libro_actualizado)
            return libro
    raise HTTPException(status_code=404, detail="Libro no encontrado")

#endpoint para eliminar
@app.delete("/libros/{id}",tags=["Libros"])
def EliminarLibro(id: int):
    for libro in libros:
        if libro["id"] == id:
            libros.remove(libro)
            return {"Mensaje": "Libro eliminado"}
    raise HTTPException(status_code=404, detail="Libro no encontrado")