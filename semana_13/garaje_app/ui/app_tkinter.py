import tkinter as tk
from tkinter import ttk
from servicios.garaje_servicio import GarajeServicio

class GarajeApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión de Garaje")

        self.servicio = GarajeServicio()

        # Titulo
        titulo = tk.Label(root, text="Registro de Vehículos", font=("Arial", 16))
        titulo.pack(pady=10)

        # Frame formulario
        frame_form = tk.Frame(root)
        frame_form.pack(pady=10)

        # Placa
        tk.Label(frame_form, text="Placa").grid(row=0, column=0)
        self.entry_placa = tk.Entry(frame_form)
        self.entry_placa.grid(row=0, column=1)

        # Marca
        tk.Label(frame_form, text="Marca").grid(row=1, column=0)
        self.entry_marca = tk.Entry(frame_form)
        self.entry_marca.grid(row=1, column=1)

        # Propietario
        tk.Label(frame_form, text="Propietario").grid(row=2, column=0)
        self.entry_propietario = tk.Entry(frame_form)
        self.entry_propietario.grid(row=2, column=1)

        # Botones
        frame_botones = tk.Frame(root)
        frame_botones.pack(pady=10)

        btn_agregar = tk.Button(
            frame_botones,
            text="Agregar Vehículo",
            command=self.agregar_vehiculo
        )
        btn_agregar.grid(row=0, column=0, padx=10)

        btn_limpiar = tk.Button(
            frame_botones,
            text="Limpiar",
            command=self.limpiar_campos
        )
        btn_limpiar.grid(row=0, column=1, padx=10)

        # Tabla
        self.tabla = ttk.Treeview(root, columns=("Placa", "Marca", "Propietario"), show="headings")
        self.tabla.heading("Placa", text="Placa")
        self.tabla.heading("Marca", text="Marca")
        self.tabla.heading("Propietario", text="Propietario")

        self.tabla.pack(pady=10)

    # FUNCIONES

    def agregar_vehiculo(self):
        placa = self.entry_placa.get()
        marca = self.entry_marca.get()
        propietario = self.entry_propietario.get()

        if placa and marca and propietario:
            self.servicio.agregar_vehiculo(placa, marca, propietario)
            self.actualizar_tabla()
            self.limpiar_campos()

    def actualizar_tabla(self):

        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        for vehiculo in self.servicio.obtener_vehiculos():
            self.tabla.insert("", "end",
                              values=(vehiculo.placa,
                                      vehiculo.marca,
                                      vehiculo.propietario))

    def limpiar_campos(self):
        self.entry_placa.delete(0, tk.END)
        self.entry_marca.delete(0, tk.END)
        self.entry_propietario.delete(0, tk.END)