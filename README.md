# Cash Hunter - Proyecto de Inteligencia Artificial

# Introducción

Cash Hunter es una aplicación desarrollada como parte de un proyecto de Inteligencia Artificial de talento tech enfocado en innovación tecnológica en el sector financiero. El objetivo principal es diseñar una solución inteligente capaz de detectar transacciones potencialmente asociadas al lavado de activos, empleando técnicas de machine learning y visualización interactiva. El proyecto busca superar las limitaciones de los sistemas tradicionales, que generan un elevado número de alertas falsas, mediante una herramienta automatizada y precisa que prioriza los casos de mayor riesgo.

## Descripción del Problema

En el sector financiero, la detección de operaciones sospechosas de lavado de activos representa un desafío técnico y regulatorio. Las entidades están obligadas a reportar actividades inusuales a autoridades como la UIAF (en Colombia), bajo pena de sanciones multimillonarias. Sin embargo, los métodos tradicionales, basados en reglas rígidas, resultan ineficaces frente a las estrategias sofisticadas empleadas por los delincuentes, quienes fragmentan transacciones, utilizan terceros o mueven fondos entre jurisdicciones con menor supervisión.
Los sistemas actuales generan un volumen masivo de alertas, muchas de ellas infundadas, lo cual satura a los equipos de cumplimiento y encarece los procesos. En este contexto, existe una necesidad crítica de soluciones más inteligentes que puedan filtrar las verdaderas señales de alerta de manera automatizada y eficiente. El uso de modelos de IA permitiría identificar patrones ocultos o emergentes, optimizando los recursos humanos y tecnológicos, y mejorando la respuesta institucional ante este delito.

## Justificación
Importancia de los datos limpios:
La precisión de los modelos de IA depende directamente de la calidad de los datos. Transacciones con errores de digitación, formatos inconsistentes, registros duplicados o valores extremos pueden sesgar el entrenamiento y producir resultados ineficaces. Por ello, se enfatiza un proceso riguroso de limpieza y preprocesamiento de datos como paso fundamental para asegurar la fiabilidad del modelo.

Impacto potencial en la lucha contra el lavado:
Una herramienta basada en IA tiene el potencial de transformar la forma en que las instituciones identifican actividades ilícitas. Puede descubrir relaciones entre cuentas, detectar patrones inusuales de comportamiento financiero, y emitir alertas basadas en probabilidades reales de riesgo. Esto no solo mejora la efectividad de los reportes enviados a los entes reguladores, sino que también reduce drásticamente las falsas alarmas, permitiendo que los analistas se enfoquen en los casos que realmente lo ameritan.

Eficiencia regulatoria y tecnológica:
El sistema propuesto representa un avance en las tecnologías aplicadas a la regulación (RegTech), integrando IA, interfaces web y contenedores Docker para ofrecer una solución escalable, replicable y fácil de desplegar. Facilita el cumplimiento normativo, reduce la carga operativa del personal de cumplimiento y permite a las instituciones anticiparse a nuevos esquemas de lavado de activos, protegiendo así tanto su reputación como la integridad del sistema financiero.



## Solución Propuesta

Desarrollamos un prototipo funcional utilizando:

- **Plataforma:** Streamlit
- **Lenguaje:** Python
- **Frameworks y Librerías:** Scikit-learn, Pandas, SQLAlchemy, Docker
- **Base de Datos:** PostgreSQL

## 🏗️ Arquitectura del Sistema

- **Entrada de Datos:** CSV o archivos locales / API
- **Preprocesamiento:** Limpieza, transformación y preparación de los datos
- **Modelo IA:** Clasificador entrenado con datos históricos
- **Interfaz:** Panel interactivo en Streamlit
- **Contenedores:** Docker para encapsular base de datos y frontend

![Arquitectura](ruta/a/imagen_diagrama.png)

## 💻 Prototipo en Streamlit

### Estructura del Código

Bash
├── api/
│   ├── main.py
│   ├── model.pkl
│   └── database.py
├── Dockerfile
├── docker-compose.yml
└── requirements.txt

## Como ejecutarlo:
1. Se clona el repositorio:
 git clone https://github.com/tu_usuario/CashHunter.git
 cd CashHunter
2. Se ejecuta el docker compose:
docker-compose up --build
3. Acceder a la app en: http://localhost:8501

## Resultados Esperados
El prototipo permite visualizar resultados de predicciones y explorar registros sospechosos mediante una interfaz simple e intuitiva.

## Mejoras Futuras
Entrenamiento con más datos reales.

Integración con servicios en la nube.

Autenticación de usuarios.

Dashboard administrativo.

## Licencia
Este proyecto se distribuye bajo la licencia MIT.


