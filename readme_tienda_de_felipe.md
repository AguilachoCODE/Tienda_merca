# Tienda de Felipe 🛒

Un script interactivo en Python simple para simular un sistema de facturación e inventario básico en consola.

## 📋 Descripción

Este programa solicita los datos de compra al usuario (nombre del cliente, nombre del producto, precio unitario y cantidad), calcula el subtotal y aplica un **10% de descuento** si el total supera los $100. Al finalizar, genera un resumen detallado de la transacción con el total final a pagar.

## ✨ Características

* Entrada dinámica de datos por consola.
* Cálculo automático del subtotal.
* Aplicación de lógica condicional para descuentos (10% si el total es mayor a $100).
* Desglose claro y formateado de la compra.

## 🚀 Requisitos e Instalación

Para ejecutar este código solo necesitas contar con **Python 3.x** instalado en tu sistema.

1. Clona o descarga este repositorio en tu equipo.
2. Abre una terminal o consola de comandos en la carpeta del proyecto.

## 🛠️ Uso

Ejecuta el script desde la consola con el siguiente comando:

```bash
python main.py
```

*(Asegúrate de reemplazar `main.py` por el nombre con el que guardaste el archivo).*

### Ejemplo de Ejecución

```text
================================
       TIENDA DE FELIPE
================================
Ingrese su nombre: Juan Pérez
Ingrese el nombre del producto: Camiseta
Ingrese el precio del producto: 30
Ingrese la cantidad: 4

--- RESUMEN DE COMPRA ---
Cliente:  Juan Pérez
Producto:  Camiseta
Precio:  30
Cantidad:  4
Total:  120
Descuento:  12.0
Total a pagar:  108.0

Gracias por su compra,  Juan Pérez !
```

## 📄 Licencia

Este proyecto está bajo la Licencia MIT.