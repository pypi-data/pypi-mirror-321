# ArrendaTools Modelo 303
![License](https://img.shields.io/github/license/hokus15/ArrendaToolsModelo303)
[![Build Status](https://github.com/hokus15/ArrendaToolsModelo303/actions/workflows/main.yml/badge.svg)](https://github.com/hokus15/ArrendaToolsModelo303/actions)
![GitHub last commit](https://img.shields.io/github/last-commit/hokus15/ArrendaToolsModelo303?logo=github)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/hokus15/ArrendaToolsModelo303?logo=github)

Módulo de Python que genera un string para la importación de datos en el modelo 303 de la Agencia Tributaria de España a partir del año 2023 (PRE 303 - Servicio ayuda modelo 303). El string generado se puede guardar en un fichero para importarlo en el modelo 303 para la presentación trimestral del IVA.

## Limitaciones

Este módulo está diseñado específicamente para facilitar la presentación del IVA trimestral de arrendadores de locales y viviendas urbanos que no realicen ninguna otra actividad. **No es válido para otros casos**, por lo que se recomienda su uso exclusivamente en el contexto mencionado.

Es importante tener en cuenta que este módulo no es aplicable en los siguientes casos:

- Si durante el trimestre se han realizado:
  - Ventas de inmuebles
  - Arrendamientos con opción de compra
  - Servicios complementarios de hostelería
  - Adquisiciones de bienes o servicios a proveedores extranjeros o establecidos en Canarias, Ceuta o Melilla (a excepción de obras realizadas por extranjeros).
- En declaraciones mensuales.
- En el régimen simplificado.
- En el Régimen Especial del Criterio de Caja.
- Si el % atribuible a la Administración del Estado es distinto de 100%.
- En el IVA a la importación liquidado por la Aduana pendiente de ingreso.
- En autoliquidaciones complementarias (opción y número de justificante).
- En casos en los que el volumen de operaciones anual sea igual a 0.
- Cuando existan cuotas pendientes de compensar de periodos anteriores.
- En la cuenta corriente tributaria - ingreso.
- En la cuenta corriente tributaria - devolución.
- En la devolución por transferencia al extranjero.

Por lo tanto, se recomienda al usuario verificar que se cumplen todas las condiciones necesarias antes de utilizar este módulo para la presentación del IVA trimestral.

## Descargo de responsabilidad

Este módulo proporciona una opción para generar un archivo con la información necesaria para el modelo 303 de la Agencia Tributaria española en un formato legible por su servicio de ayuda. Sin embargo, es importante tener en cuenta que la correcta generación, presentación e introducción de los datos, así como la veracidad del contenido, son responsabilidad exclusiva del usuario. **El usuario es siempre el último responsable de verificar que los datos introducidos son correctos y cumplen con los requisitos de la Agencia Tributaria.**

Es importante destacar que **el autor del módulo está exento de cualquier tipo de responsabilidad derivada del uso de la información generada por este módulo**. La veracidad y exactitud de los datos contenidos generados es responsabilidad exclusiva del usuario, y cualquier sanción que pudiera derivarse de un uso correcto o incorrecto o fraudulento del los datos generados por este módulo será responsabilidad exclusiva del usuario.

Por tanto, se recomienda al usuario **revisar cuidadosamente la información generada antes de presentarla en la web de la Agencia Tributaria y asegurarse de que cumple con los requisitos y está libre de errores**.

## Requisitos

Este módulo requiere Python 3.10 o superior.

## Uso

El primer paso es recopilar la información necesaria para el trimestre fiscal que desees realizar la declaración. Esta información incluye datos del contribuyente, datos financieros y otros detalles específicos del trimestre. Algunos campos son obligatorios, como el periodo, la base imponible y el NIF del contribuyente, mientras que otros son opcionales dependiendo del contexto, como el volumen anual de operaciones (obligatorio solo en el cuarto trimestre).

Usando la clase DatosModelo proporcionada por el módulo, puedes definir los datos requeridos. Cada campo tiene validaciones, como la longitud máxima, el formato y la obligatoriedad.
Por ejemplo:

```python
from modelo_303 import DatosModelo, Periodo

datos = DatosModelo(
    periodo=Periodo.CUARTO_TRIMESTRE,
    version="1.0",
    nif_empresa_desarrollo="12345678X",
    nombre_fiscal_contribuyente="DE LOS PALOTES PERICO",
    nif_contribuyente="12345678X",
    iban="ES0012341234123412341234",
    base_imponible=10000.00,
    gastos_bienes_servicios=500.00,
    iva_gastos_bienes_servicios=105.00,
    adquisiciones_bienes_inversion=3000.00,
    iva_adquisiciones_bienes_inversion=630.00,
    volumen_anual_operaciones=20000.00
)
```

El módulo incluye un factory que facilita la creación del modelo a usar en función del ejercicio.
Por ejemplo:

```python
modelo = Modelo303Factory.obtener_generador_modelo303(2024)
```

Ahora ya puedes generar el fichero utilizando el método correspondiente. Este método convierte los datos proporcionados en un formato compatible con el sistema de la Agencia Tributaria.
Por ejemplo:


```python
datos_fichero = modelo.generar(datos)
```

A continuación se muestra un ejemplo completo de cómo crear un objeto GeneradorModelo303 para el ejercicio 2024 y generar un archivo con los datos del modelo:

```python
from arrendatools.modelo303.modelo303_datos import Modelo303Datos, Periodo
from arrendatools.modelo303.modelo303_factory import Modelo303Factory

periodo = Periodo.TERCER_TRIMESTRE
nif_empresa_desarrollo = "12345678X"
version = "v1.0"
nombre_fiscal_contribuyente = "DE LOS PALOTES PERICO"
nif_contribuyente = "12345678X"
iban = "ES0012341234123412341234"
base_imponible = 2000.00
gastos_bienes_servicios = 2500.0
iva_gastos_bienes_servicios = 525.0
adquisiciones_bienes_inversion = 0.0
iva_adquisiciones_bienes_inversion = 0.0
volumen_anual_operaciones = None

datos_modelo = DatosModelo303(
    periodo=periodo,
    nif_empresa_desarrollo=nif_empresa_desarrollo,
    version=version,
    nombre_fiscal_contribuyente=nombre_fiscal_contribuyente,
    nif_contribuyente=nif_contribuyente,
    iban=iban,
    base_imponible=base_imponible,
    gastos_bienes_servicios=gastos_bienes_servicios,
    iva_gastos_bienes_servicios=iva_gastos_bienes_servicios,
    adquisiciones_bienes_inversion=adquisiciones_bienes_inversion,
    iva_adquisiciones_bienes_inversion=iva_adquisiciones_bienes_inversion,
    volumen_anual_operaciones=volumen_anual_operaciones,
)

modelo = Modelo303Factory.obtener_generador_modelo303(2024)

datos_fichero = modelo.generar(datos_modelo)
print(datos_fichero)

with open(f"{nif_contribuyente}_{ejercicio}_{periodo.value}.303", "w") as archivo:
    archivo.write(datos_fichero)
```

Es importante tener en cuenta que, aunque el ejemplo anterior es funcional, es posible que la importación en la web de la Agencia Tributaria falle en las validaciones adicionales que esta realiza, por lo que se deben proporcionar los datos correctos para poder importar correctamente el modelo en la web de la Agencia Tributaria. 