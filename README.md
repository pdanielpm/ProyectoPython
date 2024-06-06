# Paquete dna_analysis

## Descripción
Este paquete de Python, dna_analysis, proporciona una serie de herramientas para el análisis de secuencias de ADN.

## Funcionalidades Principales
**1. Calculo del contenido de AT**
Este módulo calcula el contenido de AT en una secuencia de ADN.

**2. Análisis de Frecuencia de Codonoes**
Este módulo analiza la frecuencia de codones en una secuencia de ADN.

**3. Identificación de sitios de Restricción**
Este módulo identifica los sitios de restricción en una secuencia de ADN utilizando una enzima de restricción especificada.

**4. Traducción de secuencias de ADN a Aminoácidos**
Este módulo traduce una secuencia de ADN en una secuencia de aminoácidos utilizando la tabla de código genético estándar.

## Uso
El paquete dna_analysis se puede utilizar desde la línea de comandos o importarse como una biblioteca en un script Python. **Aun no se si dejar esto**

## Estructura del proyecto
```
dna_analysis/
│
├── __init__.py
│
├── utils/
│   ├── __init__.py
│   ├── file_io.py
│   ├── validators.py
│   └── amino_acid_validators.py  # Nuevo archivo para validar secuencias de aminoácidos
│
├── operations/
│   ├── __init__.py
│   ├── at_content.py
│   ├── codon_frequency.py
│   ├── restriction_sites.py
│   └── translation.py  # Módulo para traducir secuencias de ADN a aminoácidos
│
├── scripts/
│   ├── __init__.py
│   ├── calculate_at_content.py
│   ├── calculate_codon_frequency.py
│   ├── find_restriction_sites.py
│   └── translate_dna.py  # Script para traducir secuencias de ADN a aminoácidos
│
├── tests/
│   ├── __init__.py
│   ├── test_utils/
│   │   ├── __init__.py
│   │   ├── test_file_io.py
│   │   ├── test_validators.py
│   │   └── test_amino_acid_validators.py  # Pruebas para el validador de secuencias de aminoácidos
│   ├── test_operations/
│   │   ├── __init__.py
│   │   ├── test_at_content.py
│   │   ├── test_codon_frequency.py
│   │   ├── test_restriction_sites.py
│   │   └── test_translation.py  # Pruebas para la traducción de secuencias de ADN a aminoácidos
│   └── test_scripts/
│       ├── __init__.py
│       ├── test_calculate_at_content.py
│       ├── test_calculate_codon_frequency.py
│       ├── test_find_restriction_sites.py
│       └── test_translate_dna.py  # Pruebas para el script de traducción de secuencias de ADN
└── docs/
    ├── user_manual.md
    ├── api_reference.md
    └── developer_guide.md
```
## Contribuyentes
Este paquete fue desarrollado por Palafox Collaodo Dara Jazheel y Pineda Martinez Pedro Daniel.

## Terminos de uso
Este paquete está disponible bajo la Licencia Apache. Consulta el archivo LICENSE para obtener más detalles.

