# DobleTau Quant

**DobleTau Quant** es una API diseñada para los participantes de la competencia de trading algoritmico. Proporciona funcionalidades clave como la ejecución de órdenes, la consulta de balances, el historial de operaciones y los activos actuales.

---

## Instalación

Para instalar la librería, ejecuta el siguiente comando en tu terminal:

```bash
pip install dobletau-quant
```

---

## Uso Básico

### Inicialización

Antes de usar las funciones, debes inicializar la clase `BotConnector` con el **token único** que identifica a tu bot. Este token te es proporcionado por los organizadores de la competencia.

```python
from dobletau_quant import BotConnector

# Inicializa el cliente con tu token único
bot = BotConnector(token="TU_TOKEN")
```

---

## Funciones Disponibles

### 1. Enviar una Operación (`send_order`)

Envía una operación de compra o venta de un activo. La autenticación del bot se maneja a través del token, y no es necesario pasarlo en cada solicitud.

#### Parámetros:
- **activo**: El ticker del activo, como `AAPL`, `TSLA`, etc.
- **cantidad**: Número entero que representa la cantidad a comprar (positivo) o vender (negativo).

#### Ejemplo:
```python
bot.send_order(activo="AAPL", cantidad=10)
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

### 2. Consultar el Historial de Operaciones (`get_history`)

Obtiene el historial de todas las operaciones realizadas por tu bot. El resultado será un `DataFrame` con los detalles de cada operación, incluyendo el nombre del bot, el activo operado, la cantidad, el precio y la hora.

#### Ejemplo:
```python
historial = bot.get_history()
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

### 3. Consultar los Activos Actuales (`get_positions`)

Obtiene un listado de los activos que tu bot tiene en su portafolio en tiempo real. El resultado también es un `DataFrame` con los activos y las cantidades actuales de cada uno.

#### Ejemplo:
```python
activos = bot.get_positions()
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
1     BotX     TSLA        -3
```

#### Posibles errores:
- `"Error al obtener activos actuales: [detalle del error]"`

---

### 4. Consultar Información de Equity (`get_balance`)

Obtiene información clave sobre el equity (valor total de las inversiones) y el capital disponible del bot. Devuelve un `diccionario` con estos datos.

#### Ejemplo:
```python
info = bot.get_balance()
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
    "equity": 105402.51,
    "disponible": 25121.47
}

```

#### Posibles errores:
- `"Error al obtener información de la cuenta: [detalle del error]"`

---

## Flujo de Trabajo Sugerido

1. **Configura tu cliente**: Inicializa el cliente con el token único de tu bot.
2. **Envía operaciones**: Usa `send_order` para enviar operaciones de compra y venta de activos.
3. **Analiza resultados**: Utiliza `get_history` para revisar el rendimiento de tu bot en la competencia.
4. **Consulta posiciones actuales**: Usa `get_positions` para ver qué activos están actualmente en el portafolio de tu bot.
5. **Monitorea tu balance**: Usa `get_balance` para consultar el estado financiero actual del bot.

---

## Validaciones Automáticas

La API incluye varias validaciones para asegurar que los parámetros sean correctos antes de ejecutar las operaciones:

1. **Cantidad**:
   - Debe ser un número entero distinto de cero.
   - Ejemplo válido: `10` o `-5`.
   - Ejemplo inválido: `0` o `5.5`.
2. **Activos**:
   - Solo se pueden operar activos que estén registrados en la tabla `Activos válidos` (revisar bases del concurso).
3. **Bots**:
   - Cada operación está vinculada al bot identificado por el token proporcionado durante la inicialización.

---

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

---

## Contacto

¿Tienes preguntas o sugerencias?  
Escríbenos a **percy.guerra1@unmsm.edu.pe**.
