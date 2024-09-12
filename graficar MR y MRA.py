import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Definir el modelo para el sistema masa-resorte
def solve_system(m, c, k, damping=True):
    def model(y, t, m, c, k):
        x, v = y  # y[0] = x (desplazamiento), y[1] = v (velocidad)
        if damping:
            dydt = [v, (F(t) - c * v - k * x) / m]  # Con amortiguación
        else:
            dydt = [v, (F(t) - k * x) / m]  # Sin amortiguación
        return dydt

    def F(t):
        # Fuerza externa aplicada (puedes modificarla según lo que necesites)
        return 1000 * np.sin(2 * np.pi * t)

    # Estado inicial (desplazamiento inicial y velocidad inicial)
    y0 = [0.0, 0.0]
    
    # Tiempo para la simulación
    t = np.linspace(0, 10, 1000)
    
    # Resolver la ecuación diferencial
    solution = odeint(model, y0, t, args=(m, c, k))
    x = solution[:, 0]  # Desplazamiento
    return t, x

# Función para actualizar la gráfica y la fórmula en tiempo real
def update_graph(*args):
    m = mass_slider.get()
    c = damping_slider.get()
    k = spring_slider.get()
    
    # Actualizar la gráfica
    t, x_damped = solve_system(m, c, k, damping=True)
    t, x_undamped = solve_system(m, c, k, damping=False)
    
    ax.clear()
    
    # Gráfico con amortiguación
    ax.plot(t, x_damped, label=f'Con amortiguación: m={m}, c={c}, k={k}')
    
    # Gráfico sin amortiguación
    ax.plot(t, x_undamped, label=f'Sin amortiguación: m={m}, k={k}')
    
    ax.set_xlabel('Tiempo (s)')
    ax.set_ylabel('Desplazamiento (m)')
    ax.set_title('Respuesta del sistema masa-resorte')
    ax.legend()
    ax.grid(True)
    canvas.draw()

    # Actualizar la fórmula
    equation_text.set(f"{m} * x''(t) + {c} * x'(t) + {k} * x(t) = F(t) (Con amortiguación)\n\n"
                      f"{m} * x''(t) + {k} * x(t) = F(t) (Sin amortiguación)")

# Función para restablecer los valores por defecto
def reset_defaults():
    mass_slider.set(1500)
    damping_slider.set(1200)
    spring_slider.set(50000)

# Configuración de la ventana principal con Tkinter
root = tk.Tk()
root.title("Simulación del Sistema Masa-Resorte")

# Frame para los parámetros, con un tamaño fijo
param_frame = ttk.Frame(root, width=600)  # Ancho fijo para la zona de parámetros
param_frame.pack_propagate(0)  # Impedir que se redimensione con el contenido
param_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

# Barra deslizante para la masa
ttk.Label(param_frame, text="Masa (kg):").pack(padx=5, pady=5)
mass_slider = tk.Scale(param_frame, from_=500, to=3000, orient=tk.HORIZONTAL, command=update_graph)
mass_slider.set(1500)  # Valor inicial
mass_slider.pack(padx=5, pady=5)

# Barra deslizante para la amortiguación
ttk.Label(param_frame, text="Amortiguación (Ns/m):").pack(padx=5, pady=5)
damping_slider = tk.Scale(param_frame, from_=0, to=3000, orient=tk.HORIZONTAL, command=update_graph)
damping_slider.set(1200)  # Valor inicial
damping_slider.pack(padx=5, pady=5)

# Barra deslizante para la constante del resorte
ttk.Label(param_frame, text="Constante del Resorte (N/m):").pack(padx=5, pady=5)
spring_slider = tk.Scale(param_frame, from_=0, to=60000, orient=tk.HORIZONTAL, command=update_graph)
spring_slider.set(50000)  # Valor inicial
spring_slider.pack(padx=5, pady=5)

# Botón para regresar a valores por defecto
reset_button = ttk.Button(param_frame, text="Regresar a valores por defecto", command=reset_defaults)
reset_button.pack(pady=20)

# Etiqueta para mostrar la fórmula
equation_text = tk.StringVar()
equation_label = ttk.Label(param_frame, textvariable=equation_text, font=("Arial", 14))
equation_label.pack(pady=20)

# Frame para el gráfico
graph_frame = ttk.Frame(root)
graph_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Crear la figura y el gráfico
fig, ax = plt.subplots(figsize=(8, 6))
canvas = FigureCanvasTkAgg(fig, master=graph_frame)  # Integrar el gráfico en Tkinter
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Inicializar gráfico y fórmula
update_graph()

# Ejecutar la aplicación
root.mainloop()
