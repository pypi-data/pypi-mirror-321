from arrendatools.modelo303.datos import Modelo303Datos, Periodo
from arrendatools.modelo303.generador import Modelo303Generador


class GeneradorEjercicio2023(Modelo303Generador):
    """
    Implementación para generar el modelo 303 trimestral para arrendadores con IVA para el ejercicio 2023.
    """

    _LONGITUD_NIF = 9
    # _MAX_LONGITUD_IBAN = 34 -> Los 34 son para cuentas en el extranjero que no está soportado por el módulo
    _MAX_LONGITUD_IBAN = 24
    _MAX_LONGITUD_VERSION = 4
    _MAX_LONGITUD_NOMBRE_FISCAL_CONTRIBUYENTE = 80

    _INICIO_APERTURA = "<T"
    _INICIO_CIERRE = "</T"
    _MODELO = "303"
    _DISCRIMINANTE = "0"
    _CIERRE = ">"
    _TIPO_Y_CIERRE = "0000" + _CIERRE
    _AUX_APERTURA = "<AUX>"
    _AUX_CIERRE = "</AUX>"
    _RESERVADO_ADMON_4_ESPACIOS = "".ljust(4, " ")  # 4 espacios
    _RESERVADO_ADMON_13_ESPACIOS = "".ljust(13, " ")  # 13 espacios
    _RESERVADO_ADMON_35_ESPACIOS = "".ljust(35, " ")  # 35 espacios
    _RESERVADO_ADMON_70_ESPACIOS = "".ljust(70, " ")  # 70 espacios
    _RESERVADO_ADMON_86_ESPACIOS = "".ljust(86, " ")  # 86 espacios
    _RESERVADO_ADMON_200_ESPACIOS = "".ljust(200, " ")  # 200 espacios
    _RESERVADO_ADMON_213_ESPACIOS = "".ljust(213, " ")  # 213 espacios
    _RESERVADO_ADMON_479_ESPACIOS = "".ljust(479, " ")  # 479 espacios
    _RESERVADO_ADMON_600_ESPACIOS = "".ljust(600, " ")  # 600 espacios
    _RESERVADO_ADMON_617_ESPACIOS = "".ljust(617, " ")  # 617 espacios
    _RESERVADO_ADMON_672_ESPACIOS = "".ljust(672, " ")  # 672 espacios
    _DP30301 = "01000"
    _DP30302 = "02000"
    _DP30303 = "03000"
    _DP30304 = "04000"
    _DP30305 = "05000"
    _DP303DID = "DID00"
    _DP30301_APERTURA = _INICIO_APERTURA + _MODELO + _DP30301 + _CIERRE
    _DP30301_CIERRE = _INICIO_CIERRE + _MODELO + _DP30301 + _CIERRE
    # _DP30302_APERTURA = _INICIO_APERTURA + _MODELO + _DP30302 + _CIERRE
    # _DP30302_CIERRE = _INICIO_CIERRE + _MODELO + _DP30302 + _CIERRE
    _DP30303_APERTURA = _INICIO_APERTURA + _MODELO + _DP30303 + _CIERRE
    _DP30303_CIERRE = _INICIO_CIERRE + _MODELO + _DP30303 + _CIERRE
    _DP30304_APERTURA = _INICIO_APERTURA + _MODELO + _DP30304 + _CIERRE
    _DP30304_CIERRE = _INICIO_CIERRE + _MODELO + _DP30304 + _CIERRE
    _DP30305_APERTURA = _INICIO_APERTURA + _MODELO + _DP30305 + _CIERRE
    _DP30305_CIERRE = _INICIO_CIERRE + _MODELO + _DP30305 + _CIERRE
    _DP303DID_APERTURA = _INICIO_APERTURA + _MODELO + _DP303DID + _CIERRE
    _DP303DID_CIERRE = _INICIO_CIERRE + _MODELO + _DP303DID + _CIERRE
    _PAGINA_COMPLEMENTARIA_ESPACIO = " "
    _NO_ES_4T = "0"
    _SI = "1"
    _NO = "2"
    _NO_SOLO_RG = "3"
    _CODIGO_ACTIVIDAD = "A01"
    _EPIGRAFE_IAE = "8612"

    def generar(self, datos: Modelo303Datos) -> str:
        REGISTRO_GENERAL_APERTURA = (
            self._INICIO_APERTURA
            + self._MODELO
            + self._DISCRIMINANTE
            + self.ejercicio
            + datos.periodo
            + self._TIPO_Y_CIERRE
        )
        REGISTRO_GENERAL_CIERRE = (
            self._INICIO_CIERRE
            + self._MODELO
            + self._DISCRIMINANTE
            + self.ejercicio
            + datos.periodo
            + self._TIPO_Y_CIERRE
        )
        modelo = REGISTRO_GENERAL_APERTURA
        modelo += self._generar_dp303_00(datos)
        modelo += self._generar_dp303_01(datos)
        modelo += self._generar_dp303_02(datos)
        modelo += self._generar_dp303_03(datos)
        if datos.periodo == Periodo.CUARTO_TRIMESTRE:
            modelo += self._generar_dp303_04(datos)
            modelo += self._generar_dp303_05(datos)
        modelo += self._generar_dp303_did(datos)
        modelo += REGISTRO_GENERAL_CIERRE
        return modelo

    def _generar_dp303_00(self, datos: Modelo303Datos) -> str:
        """
        Genera los datos de la seccion DP30300 del modelo 303.
        """

        modelo = self._AUX_APERTURA
        modelo += self._RESERVADO_ADMON_70_ESPACIOS
        modelo += datos.version
        modelo += self._RESERVADO_ADMON_4_ESPACIOS
        modelo += datos.nif_empresa_desarrollo
        modelo += self._RESERVADO_ADMON_213_ESPACIOS
        modelo += self._AUX_CIERRE
        return modelo

    def _generar_dp303_01(self, datos: Modelo303Datos) -> str:
        """
        Genera los datos de la seccion DP30301 del modelo 303.
        """

        iva_devengado = round(datos.base_imponible * 0.21, 2)
        total_iva_deducible = round(
            datos.iva_gastos_bienes_servicios
            + datos.iva_adquisiciones_bienes_inversion,
            2,
        )
        cuota = self._calcula_cuota(datos)

        # Indicador de inicio de registro página 1
        modelo = self._DP30301_APERTURA
        # Indicador de página complementaria.
        modelo += self._PAGINA_COMPLEMENTARIA_ESPACIO
        # Tipo Declaración
        modelo += self._tipo_declaracion(datos)
        # Identificación (1) - NIF
        modelo += datos.nif_contribuyente
        # Identificación (1) - Apellidos y nombre o Razón social
        modelo += datos.nombre_fiscal_contribuyente.ljust(80, " ")
        # Ejercicio
        modelo += self.ejercicio
        # Devengo
        modelo += datos.periodo
        # Identificación (1) - Tributación exclusivamente foral. Sujeto pasivo que tributa exclusivamente a una Administración tributaria Foral
        # con IVA a la importación liquidado por la Aduana pendiente de ingreso
        modelo += self._NO
        # Identificación (1) - Sujeto pasivo inscrito en el Registro de devolución mensual (art. 30 RIVA)
        modelo += self._NO
        # Identificación (1) - Sujeto pasivo que tributa exclusivamente en régimen simplificado -> "1" SI (sólo RS), "2" NO (RG + RS), "3" NO (sólo RG).
        modelo += self._NO_SOLO_RG
        # Identificación (1) - Autoliquidación conjunta
        modelo += self._NO
        # Identificación (1) - Sujeto pasivo acogido al régimen especial del criterio de Caja (art. 163 undecies LIVA)
        modelo += self._NO
        # Identificación (1) - Sujeto pasivo destinatario de operaciones acogidas al régimen especial del criterio de caja
        modelo += self._NO
        # Identificación (1) - Opción por la aplicación de la prorrata especial (art. 103.Dos.1º LIVA)
        modelo += self._NO
        # Identificación (1) - Revocación de la opción por la aplicación de la prorrata especial
        modelo += self._NO
        # Identificación (1) - Sujeto pasivo declarado en concurso de acreedores en el presente período de liquidación
        modelo += self._NO
        # Identificación (1) - Fecha en que se dictó el auto de declaración de concurso
        modelo += "".ljust(8, "0")
        # Identificación (1) - Tipo de autoliquidación si se ha dictado auto de declaración de concurso en este período:
        # "1" SI Preconcursal, "2" SI postconcursal, blanco NO.
        modelo += "".ljust(1, " ")
        # Identificación (1) - Sujeto pasivo acogido voluntariamente al SII
        modelo += self._NO
        # Identificación (1) - Sujeto pasivo exonerado de la Declaración-resumen anual del IVA, modelo 390
        modelo += self._exoneracion_modelo_390(datos.periodo)
        # Identificación (1) - Sujeto pasivo con volumen anual de operaciones distinto de cero (art. 121 LIVA)
        modelo += self._operaciones_distinto_0(datos.periodo)
        # IVA Devengado - Régimen general 0%. Casillas: [150], [151], [152]
        modelo += self._base_tipo_cuota_str(0.0, 0.0, 0.0)
        # IVA Devengado - Régimen general 4%. Casillas: [1], [2], [3]
        modelo += self._base_tipo_cuota_str(0.0, 4.0, 0.0)
        # IVA Devengado - Régimen general 5%. Casillas: [153], [154], [155]
        modelo += self._base_tipo_cuota_str(0.0, 5.0, 0.0)
        # IVA Devengado - Regimen general 10%. Casillas: [4], [5], [6]
        modelo += self._base_tipo_cuota_str(0.0, 10.0, 0.0)
        # IVA Devengado - Regimen general 21%. Casillas: [7], [8], [9]
        modelo += self._base_tipo_cuota_str(
            datos.base_imponible, 21.0, iva_devengado
        )
        # IVA Devengado - Adquisiciones intracomunitarias de bienes y servicios. Casillas: [10], [11]
        modelo += self._base_cuota_str(0.0, 0.0)
        # IVA Devengado - Otras operaciones con inversión del sujeto pasivo (excepto. adq. intracom). Casillas: [12], [13]
        modelo += self._base_cuota_str(0.0, 0.0)
        # IVA Devengado - Modificacion bases y cuotas. Casillas: [14], [15]
        modelo += self._base_cuota_str(0.0, 0.0)
        # IVA Devengado - Recargo equivalencia 1,75%. Casillas: [156], [157], [158]
        modelo += self._base_tipo_cuota_str(0.0, 1.75, 0.0)
        # IVA Devengado - Recargo equivalencia 0%, 0,5% o 0,62%. Casillas: [16], [17], [18]
        modelo += self._base_tipo_cuota_str(0.0, 0.0, 0.0)
        # IVA Devengado - Recargo equivalencia 1,40%. Casillas: [19], [20], [21]
        modelo += self._base_tipo_cuota_str(0.0, 1.4, 0.0)
        # IVA Devengado - Recargo equivalencia 5,20%. Casillas: [22], [23], [24]
        modelo += self._base_tipo_cuota_str(0.0, 5.2, 0.0)
        # IVA Devengado - Modificaciones bases y cuotas del recargo de equivalencia. Casillas: [25], [26]
        modelo += self._base_cuota_str(0.0, 0.0)
        # IVA Devengado - Total cuota devengada.
        # Casillas: ( [152] + [03] + [155] + [06] + [09] + [11] + [13] + [15] + [158] + [18] + [21] + [24] + [26] ) [27]
        modelo += self._convertir_a_centimos_str(iva_devengado)
        # IVA Deducible - Por cuotas soportadas en operaciones interiores corrientes. Casillas: [28], [29]
        modelo += self._base_cuota_str(
            datos.gastos_bienes_servicios,
            datos.iva_gastos_bienes_servicios,
        )
        # IVA Deducible - Por cuotas soportadas en operaciones interiores con bienes de inversión. Casillas: [30], [31]
        modelo += self._base_cuota_str(
            datos.adquisiciones_bienes_inversion,
            datos.iva_adquisiciones_bienes_inversion,
        )
        # IVA Deducible - Por cuotas soportadas en las importaciones de bienes corrientes. Casillas: [32], [33]
        modelo += self._base_cuota_str(0.0, 0.0)
        # IVA Deducible - Por cuotas soportadas en las importaciones de bienes de inversión. Casillas: [34], [35]
        modelo += self._base_cuota_str(0.0, 0.0)
        # IVA Deducible - En adquisiciones intracomunitarias de bienes y servicios corrientes. Casillas: [36], [37]
        modelo += self._base_cuota_str(0.0, 0.0)
        # IVA Deducible - En adquisiciones intracomunitarias de bienes de inversión. Casillas: [38], [39]
        modelo += self._base_cuota_str(0.0, 0.0)
        # IVA Deducible - Rectificación de deducciones. Casillas: [40], [41]
        modelo += self._base_cuota_str(0.0, 0.0)
        # IVA Deducible - Compensaciones Régimen Especial A.G. y P. Casillas: [42]
        modelo += self._convertir_a_centimos_str(0.0)
        # IVA Deducible - Regularización inversiones. Casillas: [43]
        modelo += self._convertir_a_centimos_str(0.0)
        # IVA Deducible - Regularización por aplicación del porcentaje definitivo de prorrata. Casillas: [44]
        modelo += self._convertir_a_centimos_str(0.0)
        # IVA Deducible - Total a deducir. Casillas: ( [29] + [31] + [33] + [35] + [37] + [39] + [41] + [42] + [43] + [44] ) -> Cuota [45]
        modelo += self._convertir_a_centimos_str(total_iva_deducible)
        # IVA Deducible - Resultado régimen general. Casillas: ( [27] - [45] ) -> Cuota [46]
        modelo += self._convertir_a_centimos_str(cuota)
        # Reservado para la AEAT
        modelo += self._RESERVADO_ADMON_600_ESPACIOS
        # Reservado para la AEAT - Sello electrónico reservado para la AEAT
        modelo += self._RESERVADO_ADMON_13_ESPACIOS
        # Indicador de fin de registro página 1
        modelo += self._DP30301_CIERRE
        return modelo

    def _generar_dp303_02(self, datos: Modelo303Datos) -> str:
        """
        Genera los datos de la seccion DP30302 del modelo 303. En el caso de arrendadores con IVA esta sección no se tiene que rellenar.
        """
        # Actualización 14/12/2023
        # Para el periodo 4T se añaden campos para la información de "Días" correspondiente al módulo "Superficie del horno"
        # de los siguientes epígrafes: 419.1, 419.2, 644.1, 644.2 y 644.3.
        # Para facilitar la compatibilidad con los ficheros generados/presentados anteriormente se permitirá que dichos campos
        # vengan cumplimentados a blancos sin dar error por ello.

        return ""

    def _generar_dp303_03(self, datos: Modelo303Datos) -> str:
        """
        Genera los datos de la seccion DP30303 del modelo 303.
        """

        cuota = self._calcula_cuota(datos)

        resultado = cuota
        resultado_estado = cuota
        resultado_autoliquidacion = cuota
        resultado_final = cuota

        modelo = self._DP30303_APERTURA
        # Información adicional - Entregas intracomunitarias de bienes y servicios. Casillas: [59]
        modelo += self._convertir_a_centimos_str(0.0)
        # Información adicional - Exportaciones y operaciones asimiladas. Casillas: [60]
        modelo += self._convertir_a_centimos_str(0.0)
        # Información adicional - Operaciones no sujetas por reglas de localización (excepto las incluidas en la casilla 123). Casillas: [120]
        modelo += self._convertir_a_centimos_str(0.0)
        # Información adicional - Operaciones sujetas con inversión del sujeto pasivo. Casillas: [122]
        modelo += self._convertir_a_centimos_str(0.0)
        # Información adicional - Operaciones no sujetas por reglas de localización acogidas a los regímenes especiales de ventanilla única.
        # Casillas: [123]
        modelo += self._convertir_a_centimos_str(0.0)
        # Información adicional - Operaciones sujetas y acogidas a los regímenes especiales de ventanilla única. Casillas: [124]
        modelo += self._convertir_a_centimos_str(0.0)
        # Información adicional - Importes de las entregas de bienes y prestaciones de servicios a las que habiéndoles sido aplicado el
        # régimen especial del criterio de caja hubieran resultado devengadas conforme a la regla general de devengo contenida en el art. 75 LIVA.
        # Casillas: [62], [63]
        modelo += self._base_cuota_str(0.0, 0.0)
        # Información adicional - Importes de las adquisiciones de bienes y servicios a las que sea de aplicación o afecte el régimen especial
        # del criterio de caja. Casillas: [74], [75]
        modelo += self._base_cuota_str(0.0, 0.0)
        # Resultado - Regularización cuotas art. 80.cinco.5ª LIVA. Casillas: [76]
        modelo += self._convertir_a_centimos_str(0.0)
        # Resultado - Suma de resultados. Casillas: ( [46] + [58] + [76] ) [64]
        modelo += self._convertir_a_centimos_str(resultado)
        # Resultado - % Atribuible a la Administración del Estado. Casillas: [65]
        modelo += self._porcentaje_str(100)
        # Resultado - Atribuible a la Administración del Estado. Casillas: [66]
        modelo += self._convertir_a_centimos_str(resultado_estado)
        # Resultado - IVA a la importación liquidado por la Aduana pendiente de ingreso. Casillas: [77]
        modelo += self._convertir_a_centimos_str(0.0)
        # Resultado - Cuotas a compensar pendientes de periodos anteriores. Casillas: [110]
        modelo += self._convertir_a_centimos_str(0.0)
        # Resultado - Cuotas a compensar de periodos anteriores aplicadas en este periodo. Casillas: [78]
        modelo += self._convertir_a_centimos_str(0.0)
        # Resultado - Cuotas a compensar de periodos previos pendientes para periodos posteriores. Casillas: ([110] - [78]) [87]
        modelo += self._convertir_a_centimos_str(0.0)
        # Resultado - Exclusivamente para sujetos pasivos que tributan conjuntamente a la Administración del Estado y a las Haciendas
        # Forales Resultado de la regularización anual. Casillas: [68]
        modelo += self._convertir_a_centimos_str(0.0)
        # Resultado - Resultado de la autoliquidación. Casillas: ( [66] + [77] - [78] + [68] ) [69]
        modelo += self._convertir_a_centimos_str(resultado_autoliquidacion)
        # Resultado - Resultados a ingresar de anteriores autoliquidaciones o liquidaciones administrativas correspondientes al e
        # jercicio y período objeto de la autoliquidación. Casillas: [70]
        modelo += self._convertir_a_centimos_str(0.0)
        # Resultado - Devoluciones acordadas por la Agencia Tributaria como consecuencia de la tramitación de anteriores autoliquidaciones
        # correspondientes al ejercicio y período objeto de la autoliquidación [109]
        modelo += self._convertir_a_centimos_str(0.0)
        # Resultado - Resultado. Casillas: ( [69] - [70] + [109] ) [71]
        modelo += self._convertir_a_centimos_str(resultado_final)
        # Declaración Sin actividad (X o blanco)
        modelo += "".ljust(1, " ")
        # Declaración complementaria (X o blanco)
        modelo += "".ljust(1, " ")
        # Número justificante declaración anterior
        modelo += self._RESERVADO_ADMON_13_ESPACIOS
        # Reservado para la AEAT
        modelo += self._RESERVADO_ADMON_35_ESPACIOS
        # Reservado para la AEAT
        modelo += self._RESERVADO_ADMON_86_ESPACIOS
        # Reservado para la AEAT
        modelo += self._RESERVADO_ADMON_479_ESPACIOS
        # Indicador de fin de registro página 3
        modelo += self._DP30303_CIERRE
        return modelo

    def _generar_dp303_04(self, datos: Modelo303Datos) -> str:
        """
        Genera los datos de la seccion DP30304 del modelo 303.
        """

        modelo = self._DP30304_APERTURA
        # Indicador de página complementaria.
        modelo += "".ljust(1, " ")
        # Código de actividad - Principal
        modelo += self._CODIGO_ACTIVIDAD
        # Epígrafe IAE - Principal
        modelo += self._EPIGRAFE_IAE
        # Código de actividad - Otras - 1ª
        modelo += "".ljust(3, " ")
        # Epígrafe IAE - Otras - 1ª
        modelo += "".ljust(4, " ")
        # Código de actividad - Otras - 2ª
        modelo += "".ljust(3, " ")
        # Epígrafe IAE - Otras - 2ª
        modelo += "".ljust(4, " ")
        # Código de actividad - Otras - 3ª
        modelo += "".ljust(3, " ")
        # Epígrafe IAE - Otras - 3ª
        modelo += "".ljust(4, " ")
        # Código de actividad - Otras - 4ª
        modelo += "".ljust(3, " ")
        # Epígrafe IAE - Otras - 4ª
        modelo += "".ljust(4, " ")
        # Código de actividad - Otras - 5ª
        modelo += "".ljust(3, " ")
        # Epígrafe IAE - Otras - 5ª
        modelo += "".ljust(4, " ")
        # Marque si ha efectuado operaciones por las que tenga obligación de presentar la declaración anual de operaciones con terceras personas.
        # (X o blanco)
        modelo += "".ljust(1, " ")
        # Información de la tributación por razón de territorio: Álava [89]
        modelo += self._porcentaje_str(0.0)
        # Información de la tributación por razón de territorio: Guipuzcoa [90]
        modelo += self._porcentaje_str(0.0)
        # Información de la tributación por razón de territorio: Vizcaya [91]
        modelo += self._porcentaje_str(0.0)
        # Información de la tributación por razón de territorio: Navarra [92]
        modelo += self._porcentaje_str(0.0)
        # Información de la tributación por razón de territorio: Territorio común [107]
        modelo += self._porcentaje_str(0.0)
        # Operaciones realizadas en el ejercicio - Operaciones en régimen general [80]
        modelo += self._convertir_a_centimos_str(
            datos.volumen_anual_operaciones
        )
        # Operaciones realizadas en el ejercicio - Operaciones en régimen especial del criterio de caja conforme art. 75 LIVA [81]
        modelo += self._convertir_a_centimos_str(0.0)
        # Operaciones realizadas en el ejercicio - Entregas intracomunitarias de bienes y servicios [93]
        modelo += self._convertir_a_centimos_str(0.0)
        # Operaciones realizadas en el ejercicio - Exportaciones y otras operaciones exentas con derecho a deducción [94]
        modelo += self._convertir_a_centimos_str(0.0)
        # Operaciones realizadas en el ejercicio - Operaciones exentas sin derecho a deducción [83]
        modelo += self._convertir_a_centimos_str(0.0)
        # Operaciones realizadas en el ejercicio - Operaciones no sujetas por reglas de localización (excepto las incluidas en la casilla 126) [84]
        modelo += self._convertir_a_centimos_str(0.0)
        # Operaciones sujetas con inversión del sujeto pasivo [125]
        modelo += self._convertir_a_centimos_str(0.0)
        # Operaciones no sujetas por reglas de localización acogidas a los regímenes especiales de ventanilla única [126]
        modelo += self._convertir_a_centimos_str(0.0)
        # OSS. Operaciones sujetas y acogidas a los regímenes especiales de ventanilla única [127]
        modelo += self._convertir_a_centimos_str(0.0)
        # Operaciones intragrupo valoradas conforme a lo dispuesto en los arts. 78 y 79 LIVA [128]
        modelo += self._convertir_a_centimos_str(0.0)
        # Operaciones realizadas en el ejercicio - Operaciones en régimen simplificado [86]
        modelo += self._convertir_a_centimos_str(0.0)
        # Operaciones realizadas en el ejercicio - Operaciones en régimen especial de la agricultura, ganadería y pesca [95]
        modelo += self._convertir_a_centimos_str(0.0)
        # Operaciones realizadas en el ejercicio - Operaciones realizadas por sujetos pasivos acogidos al régimen especial del recargo
        # de equivalencia [96]
        modelo += self._convertir_a_centimos_str(0.0)
        # Operaciones realizadas en el ejercicio - Operaciones en Régimen especial de bienes usados, objetos de arte, antigüedades y
        # objetos de colección [97]
        modelo += self._convertir_a_centimos_str(0.0)
        # Operaciones realizadas en el ejercicio - Operaciones en régimen especial de Agencias de Viajes [98]
        modelo += self._convertir_a_centimos_str(0.0)
        # Operaciones realizadas en el ejercicio - Entregas de bienes inmuebles, operaciones financieras y relativas al oro de
        # inversión no habituales [79]
        modelo += self._convertir_a_centimos_str(0.0)
        # Operaciones realizadas en el ejercicio - Entregas de bienes de inversión [99]
        modelo += self._convertir_a_centimos_str(0.0)
        # Operaciones realizadas en el ejercicio.
        # Total volumen de operaciones ([80]+[81]+[93]+[94]+[83]+[84]+[125]+[126]+[127]+[128]+[86]+[95]+[96]+[97]+[98]-[79]-[99]) [88]
        modelo += self._convertir_a_centimos_str(
            datos.volumen_anual_operaciones
        )
        # Reservado para la AEAT
        modelo += self._RESERVADO_ADMON_600_ESPACIOS
        modelo += self._DP30304_CIERRE
        return modelo

    def _generar_dp303_05(self, datos: Modelo303Datos) -> str:
        """
        Genera los datos de la seccion DP30305 del modelo 303.
        """

        modelo = self._DP30305_APERTURA
        # Indicador de página complementaria.
        modelo += "".ljust(1, " ")
        # Prorratas - 1 - Código CNAE [500]
        modelo += "".ljust(3, " ")
        # Prorratas - 1 - Importe de operaciones [501]
        modelo += self._convertir_a_centimos_str(0.0)
        # Prorratas - 1 - Importe de operaciones con derecho a deducción [502]
        modelo += self._convertir_a_centimos_str(0.0)
        # Prorratas - 1 - Tipo de prorrata ("G", "E" o blanco). [503]
        modelo += "".ljust(1, " ")
        # Prorratas - 1 - % de prorrata [504]
        modelo += self._porcentaje_str(0.0)
        # Prorratas - 2 - Código CNAE [505]
        modelo += "".ljust(3, " ")
        # Prorratas - 2 - Importe de operaciones [506]
        modelo += self._convertir_a_centimos_str(0.0)
        # Prorratas - 2 - Importe de operaciones con derecho a deducción [507]
        modelo += self._convertir_a_centimos_str(0.0)
        # Prorratas - 2 - Tipo de prorrata ("G", "E" o blanco). [508]
        modelo += "".ljust(1, " ")
        # Prorratas - 2 - % de prorrata [509]
        modelo += self._porcentaje_str(0.0)
        # Prorratas - 3 - Código CNAE [510]
        modelo += "".ljust(3, " ")
        # Prorratas - 3 - Importe de operaciones [511]
        modelo += self._convertir_a_centimos_str(0.0)
        # Prorratas - 3 - Importe de operaciones con derecho a deducción [512]
        modelo += self._convertir_a_centimos_str(0.0)
        # Prorratas - 3 - Tipo de prorrata ("G", "E" o blanco). [513]
        modelo += "".ljust(1, " ")
        # Prorratas - 3 - % de prorrata [514]
        modelo += self._porcentaje_str(0.0)
        # Prorratas - 4 - Código CNAE [515]
        modelo += "".ljust(3, " ")
        # Prorratas - 4 - Importe de operaciones [516]
        modelo += self._convertir_a_centimos_str(0.0)
        # Prorratas - 4 - Importe de operaciones con derecho a deducción [517]
        modelo += self._convertir_a_centimos_str(0.0)
        # Prorratas - 4 - Tipo de prorrata ("G", "E" o blanco). [518]
        modelo += "".ljust(1, " ")
        # Prorratas - 4 - % de prorrata [519]
        modelo += self._porcentaje_str(0.0)
        # Prorratas - 5 - Código CNAE [520]
        modelo += "".ljust(3, " ")
        # Prorratas - 5 - Importe de operaciones [521]
        modelo += self._convertir_a_centimos_str(0.0)
        # Prorratas - 5 - Importe de operaciones con derecho a deducción [522]
        modelo += self._convertir_a_centimos_str(0.0)
        # Prorratas - 5 - Tipo de prorrata ("G", "E" o blanco). [523]
        modelo += "".ljust(1, " ")
        # Prorratas - 5 - % de prorrata [524]
        modelo += self._porcentaje_str(0.0)
        # 13. Reg. Deducc. Diferenc.- 1 - IVA ded. Operac. Interiores - Bienes y servicios corrientes - Base imponible [700]
        modelo += self._convertir_a_centimos_str(0.0)
        # 13. Reg. Deducc. Diferenc.- 1 - IVA ded. Operac. Interiores - Bienes y servicios corrientes - Cuota deducible [701]
        modelo += self._convertir_a_centimos_str(0.0)
        # 13. Reg. Deducc. Diferenc.- 1 - IVA ded. Operac. Interiores - Bienes inversión - Base imponible [702]
        modelo += self._convertir_a_centimos_str(0.0)
        # 13. Reg. Deducc. Diferenc.- 1 - IVA ded. Operac. Interiores - Bienes inversión - Cuota deducible [703]
        modelo += self._convertir_a_centimos_str(0.0)
        # 13. Reg. Deducc. Diferenc.- 1 - IVA ded. Importaciones - Bienes corrientes - Base imponible [704]
        modelo += self._convertir_a_centimos_str(0.0)
        # 13. Reg. Deducc. Diferenc.- 1 - IVA ded. Importaciones - Bienes corrientes - Cuota deducible [705]
        modelo += self._convertir_a_centimos_str(0.0)
        # 13. Reg. Deducc. Diferenc.- 1 - IVA ded. Importaciones - Bienes inversión - Base imponible [706]
        modelo += self._convertir_a_centimos_str(0.0)
        # 13. Reg. Deducc. Diferenc.- 1 - IVA ded. Importaciones - Bienes inversión - Cuota deducible [707]
        modelo += self._convertir_a_centimos_str(0.0)
        # 13. Reg. Deducc. Diferenc.- 1 - IVA ded. Adquisic. intracomun. - Bienes corrientes y servicios - Base imponible [708]
        modelo += self._convertir_a_centimos_str(0.0)
        # 13. Reg. Deducc. Diferenc.- 1 - IVA ded. Adquisic. intracomun. - Bienes corrientes y servicios - Cuota deducible [709]
        modelo += self._convertir_a_centimos_str(0.0)
        # 13. Reg. Deducc. Diferenc.- 1 - IVA ded. Adquisic. intracomun. - Bienes inversión - Base imponible [710]
        modelo += self._convertir_a_centimos_str(0.0)
        # 13. Reg. Deducc. Diferenc.- 1 - IVA ded. Adquisic. intracomun. - Bienes inversión - Cuota deducible [711]
        modelo += self._convertir_a_centimos_str(0.0)
        # 13. Reg. Deducc. Diferenc.- 1 - Compensac. rég. especial agric./ganad./pesca - Base impon. [712]
        modelo += self._convertir_a_centimos_str(0.0)
        # 13. Reg. Deducc. Diferenc.- 1 - Compensac. rég. especial agric./ganad./pesca - Cuota deduc. [713]
        modelo += self._convertir_a_centimos_str(0.0)
        # 13. Reg. Deducc. Diferenc.- 1 - Rectificación de deducciones - Base impon.  [714]
        modelo += self._convertir_a_centimos_str(0.0)
        # 13. Reg. Deducc. Diferenc.- 1 - Rectificación de deducciones - Cuota deduc. [715]
        modelo += self._convertir_a_centimos_str(0.0)
        # 13. Reg. Deducc. Diferenc.- 1 - Regularización de bienes de inversión [716]
        modelo += self._convertir_a_centimos_str(0.0)
        # 13. Reg. Deducc. Diferenc.- 1 - Suma de deducciones [717]
        modelo += self._convertir_a_centimos_str(0.0)
        # 13. Reg. Deducc. Diferenc.- 2 - IVA ded. Operac. Interiores - Bienes y servicios corrientes - Base imponible [718]
        modelo += self._convertir_a_centimos_str(0.0)
        # 13. Reg. Deducc. Diferenc.- 2 - IVA ded. Operac. Interiores - Bienes y servicios corrientes - Cuota deducible [719]
        modelo += self._convertir_a_centimos_str(0.0)
        # 13. Reg. Deducc. Diferenc.- 2 - IVA ded. Operac. Interiores - Bienes inversión - Base imponible [720]
        modelo += self._convertir_a_centimos_str(0.0)
        # 13. Reg. Deducc. Diferenc.- 2 - IVA ded. Operac. Interiores - Bienes inversión - Cuota deducible [721]
        modelo += self._convertir_a_centimos_str(0.0)
        # 13. Reg. Deducc. Diferenc.- 2 - IVA ded. Importaciones - Bienes corrientes - Base imponible [722]
        modelo += self._convertir_a_centimos_str(0.0)
        # 13. Reg. Deducc. Diferenc.- 2 - IVA ded. Importaciones - Bienes corrientes - Cuota deducible [723]
        modelo += self._convertir_a_centimos_str(0.0)
        # 13. Reg. Deducc. Diferenc.- 2 - IVA ded. Importaciones - Bienes inversión - Base imponible [724]
        modelo += self._convertir_a_centimos_str(0.0)
        # 13. Reg. Deducc. Diferenc.- 2 - IVA ded. Importaciones - Bienes inversión - Cuota deducible [725]
        modelo += self._convertir_a_centimos_str(0.0)
        # 13. Reg. Deducc. Diferenc.- 2 - IVA ded. Adquisic. intracomun. - Bienes corrientes y servicios - Base imponible [726]
        modelo += self._convertir_a_centimos_str(0.0)
        # 13. Reg. Deducc. Diferenc.- 2 - IVA ded. Adquisic. intracomun. - Bienes corrientes y servicios - Cuota deducible [727]
        modelo += self._convertir_a_centimos_str(0.0)
        # 13. Reg. Deducc. Diferenc.- 2 - IVA ded. Adquisic. intracomun. - Bienes inversión - Base imponible [728]
        modelo += self._convertir_a_centimos_str(0.0)
        # 13. Reg. Deducc. Diferenc.- 2 - IVA ded. Adquisic. intracomun. - Bienes inversión - Cuota deducible [729]
        modelo += self._convertir_a_centimos_str(0.0)
        # 13. Reg. Deducc. Diferenc.- 2 - Compensac. rég. especial agric./ganad./pesca - Base impon. [730]
        modelo += self._convertir_a_centimos_str(0.0)
        # 13. Reg. Deducc. Diferenc.- 2 - Compensac. rég. especial agric./ganad./pesca - Cuota deduc. [731]
        modelo += self._convertir_a_centimos_str(0.0)
        # 13. Reg. Deducc. Diferenc.- 2 - Rectificación de deducciones - Base impon.  [732]
        modelo += self._convertir_a_centimos_str(0.0)
        # 13. Reg. Deducc. Diferenc.- 2 - Rectificación de deducciones - Cuota deduc. [733]
        modelo += self._convertir_a_centimos_str(0.0)
        # 13. Reg. Deducc. Diferenc.- 2 - Regularización de bienes de inversión [734]
        modelo += self._convertir_a_centimos_str(0.0)
        # 13. Reg. Deducc. Diferenc.- 2 - Suma de deducciones [735]
        modelo += self._convertir_a_centimos_str(0.0)
        modelo += self._RESERVADO_ADMON_672_ESPACIOS
        modelo += self._DP30305_CIERRE
        return modelo

    def _generar_dp303_did(self, datos: Modelo303Datos) -> str:
        """
        Genera los datos de la seccion DP303DID del modelo 303.
        """

        modelo = self._DP303DID_APERTURA
        # Devolución. SWIFT-BIC
        modelo += "".ljust(11, " ")
        if self._calcula_cuota(datos) < 0:
            # Si la cuota es negativa no se incluye el IBAN
            # Domiciliación/Devolución - IBAN
            modelo += "".ljust(34, " ")
        else:
            # Si la cuota es positiva se incluye el IBAN
            # Domiciliación/Devolución - IBAN
            modelo += datos.iban.ljust(34, " ")
        # Devolución - Banco/Bank name
        modelo += "".ljust(70, " ")
        # Devolución - Dirección del Banco/ Bank address
        modelo += "".ljust(35, " ")
        # Devolución - Ciudad/City
        modelo += "".ljust(30, " ")
        # Devolución - Código País/Country code
        modelo += "".ljust(2, " ")
        # Devolución - Marca SEPA (0 - Vacía, 1 - Cuenta España, 2 - Unión Europea SEPA, 3 - Resto Países)
        modelo += self._marca_sepa(datos.iban)
        modelo += self._RESERVADO_ADMON_617_ESPACIOS
        modelo += self._DP303DID_CIERRE
        return modelo

    def _calcula_cuota(self, datos: Modelo303Datos) -> str:
        iva_devengado = round(datos.base_imponible * 0.21, 2)
        total_iva_deducible = round(
            datos.iva_gastos_bienes_servicios
            + datos.iva_adquisiciones_bienes_inversion,
            2,
        )
        return round(iva_devengado - total_iva_deducible, 2)

    def _tipo_declaracion(self, datos: Modelo303Datos) -> str:
        """
        Obtiene el tipo de declaración en base al IVA devengado y el IBAN.
        Sólo tiene en cuenta los tipos N, C, D, U e I. El resto de tipos no están soportados.
        El tipo de declaración puede ser:
        C (solicitud de compensación)
        D (devolución)
        G (cuenta corriente tributaria-ingreso)
        I (ingreso)
        N (sin actividad/resultado cero)
        V (cuenta corriente tributaria -devolución)
        U (domiciliacion del ingreso en CCC)
        X (Devolución por transferencia al extranjero)
        """
        cuota = self._calcula_cuota(datos)

        if cuota == 0:
            return "N"
        if cuota < 0 and not datos.periodo == Periodo.CUARTO_TRIMESTRE:
            return "C"
        if cuota < 0 and datos.periodo == Periodo.CUARTO_TRIMESTRE:
            return "D"
        if cuota > 0 and datos.iban is not None and datos.iban != "":
            return "U"
        return "I"

    def _exoneracion_modelo_390(self, periodo):
        """
        Obtiene el valor a añadir para la exoneración del Modelo 390 dependiendo del periodo.

        :param periodo: Periodo para el cual se generan los datos.
        :type string: Periodo
        :return: String con valor a añadir para la exoneración del Modelo 390 dependiendo del periodo.
        :rtype: String.
        """
        if periodo != Periodo.CUARTO_TRIMESTRE:
            return self._NO_ES_4T
        return self._SI

    def _operaciones_distinto_0(self, periodo):
        if periodo != Periodo.CUARTO_TRIMESTRE:
            return self._NO_ES_4T
        return self._SI

    def _marca_sepa(self, iban):
        return "0"

    def _convertir_a_centimos(self, valor):
        return int(round(valor * 100, 2))

    def _convertir_a_centimos_zfill(self, valor, length):
        resultado = str(self._convertir_a_centimos(abs(valor))).zfill(length)
        if valor < 0:
            return "N" + resultado[1:]
        else:
            return resultado

    def _convertir_a_centimos_str(self, valor):
        return self._convertir_a_centimos_zfill(valor, 17)

    def _porcentaje_str(self, valor):
        return self._convertir_a_centimos_zfill(valor, 5)

    def _base_cuota_str(self, base, cuota):
        return self._convertir_a_centimos_str(
            base
        ) + self._convertir_a_centimos_str(cuota)

    def _base_tipo_cuota_str(self, base, tipo, cuota):
        return (
            self._convertir_a_centimos_str(base)
            + self._porcentaje_str(tipo)
            + self._convertir_a_centimos_str(cuota)
        )
