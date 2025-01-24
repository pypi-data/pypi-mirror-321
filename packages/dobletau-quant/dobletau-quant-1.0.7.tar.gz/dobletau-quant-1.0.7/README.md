# DobleTau Quant

**DobleTau Quant** es una API diseñada para los participantes de la competencia de trading algoritmico. La API permite enviar operaciones automatizadas y consultar resultados de manera sencilla y eficiente.

---

## Instalación

Para instalar la librería, ejecuta el siguiente comando en tu terminal:

```bash
pip install dobletau-quant
```

---

## Uso Básico

### Inicialización

Antes de usar las funciones, debes inicializar la clase `BotConnector` con el **token único** que identifica a tu bot. Este token es proporcionado al registrarte en la plataforma.

```python
from dobletau_quant import BotConnector

# Inicializa el cliente con tu token único
bot = BotConnector(token="TU_TOKEN")
```

---

## Funciones Disponibles

### 1. Enviar una Operación (`send_operation`)

Envía una operación de compra o venta de un activo. El token del bot se incluye automáticamente durante la inicialización del cliente.

#### Parámetros:
- **activo**: Símbolo del activo (ticker) como `AAPL`, `TSLA`.
- **cantidad**: Número entero (positivo para compras, negativo para ventas).

#### Ejemplo:
```python
bot.send_operation(activo="AAPL", cantidad=10)
```

#### Resultado esperado (éxito):
```
Operación enviada exitosamente.
```

#### Posibles errores:
- `"La cantidad debe ser un número entero distinto de cero."`
- `"El activo 'AAPL' no existe en la tabla 'Activos'."`
- `"Error al enviar la operación: [detalle del error]"`

---

### 2. Consultar el Historial de Operaciones (`get_historial`)

Devuelve un historial detallado de todas las operaciones realizadas por tu bot. El token del bot se incluye automáticamente.

#### Ejemplo:
```python
historial = bot.get_historial()
print(historial)
```

#### Resultado esperado:
Un `DataFrame` con el historial, con columnas como:
- `bot`: Nombre del bot.
- `ticker`: Activo financiero operado.
- `cantidad`: Cantidad comprada o vendida.
- `precio`: Precio al momento de la operación.
- `hora`: Fecha y hora de la operación.

Ejemplo de salida:
```
        bot   ticker  cantidad  precio                hora
0     BotX     AAPL        10  150.25  2024-12-22 10:30:00
1     BotX     TSLA       -15  400.50  2024-12-21 12:00:00
```

#### Posibles errores:
- `"Error al obtener historial: [detalle del error]"`

---

### 3. Consultar los Activos Actuales (`get_actuales`)

Obtiene un listado de los activos actuales que el bot está manejando en su portafolio.

#### Ejemplo:
```python
activos = bot.get_actuales()
print(activos)
```

#### Resultado esperado:
Un `DataFrame` con los activos actuales, con columnas como:
- `bot`: Nombre del bot.
- `ticker`: Símbolo del activo (ticker).
- `cantidad`: Cantidad de activos actuales.

Ejemplo de salida:
```
        bot   ticker  cantidad
0     BotX     AAPL        8
1     BotX     TSLA        3
```

#### Posibles errores:
- `"Error al obtener activos actuales: [detalle del error]"`

---

### 4. Consultar Información de Equity (`get_info`)

Obtiene información clave sobre el equity y el capital disponible del bot. La información está vinculada al token único del bot.

#### Ejemplo:
```python
info = bot.get_info()
print(info)
```

#### Resultado esperado:
Un `diccionario` con las siguientes claves:
- `bot`: Nombre del bot.
- `equity`: Valor del equity del bot.
- `disponible`: Capital disponible del bot.

Ejemplo de salida:
```
{
    "bot": "BotX",
    "equity": 25000.50,
    "disponible": 5000.00
}

```

#### Posibles errores:
- `"Error al obtener información de la cuenta: [detalle del error]"`

---

## Flujo de Trabajo Sugerido

1. **Configura tu cliente**: Inicializa el cliente con el token único de tu bot.
2. **Envia operaciones**: Usa `send_operation` para enviar operaciones de compra y venta simuladas.
3. **Analiza resultados**: Utiliza `get_historial` para evaluar el rendimiento de tu bot en la competencia.
4. **Consulta los activos actuales**: Usa `get_actuales` para obtener una lista de los activos que tu bot tiene en su portafolio.

---

## Validaciones Automáticas

La API incluye validaciones para:
1. **Cantidad**:
   - Debe ser un número entero distinto de cero.
   - Ejemplo válido: `10` o `-5`.
   - Ejemplo inválido: `0` o `5.5`.
2. **Activos**:
   - Solo se permiten activos registrados en la tabla `Activos`.
3. **Bots**:
   - Cada operación está vinculada al bot identificado por el token proporcionado durante la inicialización.

---

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

## Contacto

¿Tienes preguntas o sugerencias?  
Escríbenos a **percy.guerra1@unmsm.edu.pe**.
