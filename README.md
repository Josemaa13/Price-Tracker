# 🛒 Eco-Stock Monitor & Price Tracker

Este proyecto nace como una herramienta personal para monitorizar el **stock**, la **variación de precios** y el **impacto sostenible** de productos en diferentes e-commerce. 

Desarrollado como proyecto de ingeniería de software para profundizar en el manejo de datos en tiempo real y automatización.

---

## Objetivos del MVP
- [ ] **Scraping Base:** Extraer nombre, precio y stock de una tienda específica.
- [ ] **Persistencia:** Guardar el histórico de precios en una base de datos local (SQLite).
- [ ] **Sistema de Alertas:** Notificación automática vía GMAIL cuando el precio baje o haya reposición de stock.
- [ ] **Score de Sostenibilidad:** Algoritmo básico que puntúe el producto según sus materiales.

## Stack Tecnológico
* **Lenguaje:** Python 3.13
* **Librerías de Extracción:** Playwright
* **Base de Datos:** SQLite
* **Notificaciones:** API GMAIL
* **Control de Versiones:** Git & GitHub

---

## 🚀 Estructura del Proyecto
* `/src`: Código fuente del scraper y lógica de negocio.
* `/data`: Almacenamiento de la base de datos local (sqlite).
* `/docs`: Documentación del diseño y algoritmos de scoring.
* `requirements.txt`: Dependencias del proyecto.

---

## 📝 Próximos Pasos (Roadmap)
1. Configuración del entorno virtual y primer script de extracción.
2. Diseño del esquema de la base de datos para el histórico.
3. Integración con la API de Telegram.
4. Extensión de navegador (Chrome/Firefox) para visualización rápida.

---
**Autor:** Jose Maria - Estudiante de Ingeniería de Software