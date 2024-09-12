# Actividad de Sustentación - Dinámica de Sistemas Físicos

**Autor:** Sebastián Morales

## Introducción

En esta actividad, se aplicarán los principios de la Dinámica desarrollando una simulación en Python que permita visualizar y analizar fenómenos dinámicos en sistemas físicos. El sistema estudiado es el sistema de suspensión de un vehículo, el cual puede ser descrito mediante una ecuación diferencial de segundo orden:

### Ecuación del sistema de suspensión

𝑚𝑥¨ + 𝑐𝑥˙ + 𝑘𝑥 = 𝐹(𝑡)

Donde:

- **m**: masa (kg)
- **c**: constante de amortiguación (N/m)
- **k**: constante del resorte (N/m)
- **x**: desplazamiento
- **F(t)**: fuerza externa aplicada, que puede depender del tiempo

La simulación mostrará cómo el desplazamiento **x** cambia con el tiempo en función de los valores de las variables ajustadas.

## Simulación de un Sistema de Suspensión

En este ejemplo, la fuerza externa **F(t)** es una función sinusoidal. La gráfica generada mostrará el desplazamiento en función del tiempo y cómo este comportamiento varía al ajustar los parámetros del sistema.

### Efectos de Cambiar los Parámetros del Sistema

### Aumento de la Masa

1. El sistema responde más lentamente, ya que una masa mayor implica mayor dificultad para acelerar el sistema.
2. Las oscilaciones son más lentas y pueden aumentar en magnitud en algunos casos.
3. El sistema tarda más en detenerse debido a la mayor inercia.

### Disminución de la Masa

1. El sistema responde más rápidamente, alcanzando el desplazamiento máximo más pronto.
2. Las oscilaciones son más rápidas y el sistema se estabiliza más rápidamente.

### Interpretación Gráfica

- **Aumento de la masa**: la gráfica mostrará oscilaciones más suaves y lentas.
- **Disminución de la masa**: las oscilaciones serán más rápidas y el sistema responderá de manera más ágil.

### Aumento de la Amortiguación

1. El sistema pierde energía rápidamente, estabilizándose antes.
2. Las oscilaciones disminuyen rápidamente, llegando a desaparecer por completo.

### Disminución de la Amortiguación

1. El sistema pierde energía más lentamente, permitiendo que las oscilaciones duren más tiempo.
2. Si no hay amortiguación (c=0), el sistema oscilará indefinidamente.

### Interpretación Gráfica

- **Aumento de la amortiguación**: las oscilaciones disminuirán rápidamente en la gráfica.
- **Disminución de la amortiguación**: las oscilaciones persistirán por más tiempo.

### Aumento de la Constante del Resorte

1. El sistema se vuelve más rígido, lo que genera oscilaciones más rápidas pero de menor amplitud.
2. El desplazamiento máximo disminuye, ya que el sistema regresa más rápido a la posición de equilibrio.

### Disminución de la Constante del Resorte

1. El resorte es más flexible, generando oscilaciones más lentas.
2. El desplazamiento máximo puede ser mayor debido a la menor fuerza restauradora.

### Interpretación Gráfica

- **Aumento de la constante del resorte**: las oscilaciones serán más rápidas y de menor amplitud.
- **Disminución de la constante del resorte**: las oscilaciones serán más amplias y lentas.

## Preguntas Frecuentes

### ¿Por qué la gráfica es oscilante?

La oscilación ocurre porque la masa se desplaza de su posición de equilibrio y es restaurada por la fuerza del resorte. La amortiguación disipa la energía, lo que genera un movimiento oscilante característico de los sistemas de segundo orden.

## Resumen Visual de los Efectos

1. **Masa (m)**: Controla la inercia. Aumentar la masa disminuye la frecuencia de las oscilaciones.
2. **Amortiguación (c)**: Controla la pérdida de energía. Mayor amortiguación disipa las oscilaciones rápidamente.
3. **Constante del resorte (k)**: Controla la rigidez del sistema. Aumentar la rigidez reduce la amplitud de las oscilaciones.

## Ejemplos de Situaciones Físicas

En un coche, la amortiguación se ajusta para absorber impactos. Si la masa del vehículo es grande y la amortiguación es baja, las oscilaciones pueden prolongarse antes de estabilizarse.

### Casos Especiales

1. **Cuando k=0**: No existe fuerza restauradora, el resorte no actúa y el sistema depende solo de la masa y la amortiguación.
2. **Cuando c=0**: El sistema oscilará indefinidamente, ya que no hay resistencia al movimiento.

### ¿Por qué las oscilaciones pueden ser irregulares?

1. **Alta amortiguación**: El sistema disipa mucha energía, lo que puede causar picos irregulares en las primeras oscilaciones.
2. **Constante del resorte baja**: Un resorte débil genera oscilaciones más amplias y lentas, contribuyendo a la irregularidad.

### Conclusión sobre las Oscilaciones Irregulares

El sistema con alta amortiguación y un resorte débil muestra oscilaciones disparejas debido a la combinación de una gran inercia, débil restauración y alta disipación de energía. Los picos irregulares en la gráfica son el resultado de esta dinámica.
