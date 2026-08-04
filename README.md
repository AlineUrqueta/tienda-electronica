# 🛒 Tienda Electrónica RM

Sistema de gestión por consola para una tienda de artículos electrónicos, desarrollado en **Python**.
Proyecto de la asignatura **Introducción a la Programación** — Universidad Andrés Bello (UNAB).

> **Grupo 4 · Tercera Entrega**

---

## 📋 Descripción

Aplicación de línea de comandos que permite administrar la información de una tienda
electrónica mediante un menú interactivo. Los datos se almacenan en **listas en memoria**
durante la ejecución del programa e incluyen validaciones de entrada para evitar registros
inválidos o duplicados.

## ✨ Funcionalidades

| Opción | Módulo | Descripción |
|:------:|--------|-------------|
| 1 | Registrar Cliente | RUT, nombre, teléfono y correo (con validaciones) |
| 2 | Registrar Producto | Código, nombre, marca y precio |
| 3 | Registrar Proveedor | RUT, nombre y teléfono |
| 4 | Registrar Empleado | RUT, nombre y cargo |
| 5 | Registrar Venta | Folio, cliente y producto (verifica que existan) |
| 6 | Registrar Orden de Compra | N° de orden, producto y proveedor |
| 7 | Consultar Clientes | Lista los clientes registrados y su total |
| 8 | Consultar Productos | Lista los productos y el valor total del inventario |
| 9 | Salir | Cierra el sistema |

### 🔎 Validaciones implementadas
- Campos obligatorios (no se aceptan valores vacíos).
- Nombres solo con letras; teléfonos solo con números.
- Correo electrónico debe contener el símbolo `@`.
- Precios numéricos y mayores que cero.
- Prevención de **duplicados** (RUT, código de producto, folio, N° de orden).
- Las ventas y órdenes de compra exigen que el cliente, producto o proveedor **ya esté registrado**.

## 🚀 Cómo ejecutar

Requisitos: **Python 3.x** instalado.

```bash
python "Proyecto_Tienda_Electronica_RM(v4.0).py"
```

## 📁 Versiones

- **`Proyecto_Tienda_Electronica_RM(v4.0).py`** — Versión actual y completa (rama `main`).
- **`Proyecto_Tienda_Electronica_RM(v3.0).py`** — Versión anterior (disponible en la rama `dev-ruth`).

## 🌿 Ramas del proyecto

| Rama | Contenido |
|------|-----------|
| `main` | Integración final del proyecto (v4.0) |
| `dev-aline` | Desarrollo — v4.0 |
| `dev-cristopher` | Desarrollo — v4.0 |
| `dev-natalia` | Desarrollo — v4.0 |
| `dev-diego` | Desarrollo — v4.0 |
| `dev-ruth` | Desarrollo — v3.0 |

## 👥 Integrantes — Grupo 4

- Aline
- Cristopher
- Ruth
- Natalia
- Diego

---

_Proyecto académico · UNAB · Introducción a la Programación · Segundo Trimestre · Tercera Entrega · 2026._
