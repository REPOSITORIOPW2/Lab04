<div align="center">
<table>
    <theader>
        <tr>
            <td><img src="https://github.com/rescobedoq/pw2/blob/main/epis.png?raw=true" alt="EPIS" style="width:50%; height:auto"/></td>
            <th>
                <span style="font-weight:bold;">UNIVERSIDAD NACIONAL DE SAN AGUSTIN</span><br />
                <span style="font-weight:bold;">FACULTAD DE INGENIERÍA DE PRODUCCIÓN Y SERVICIOS</span><br />
                <span style="font-weight:bold;">ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS</span>
            </th>
            <td><img src="https://github.com/rescobedoq/pw2/blob/main/abet.png?raw=true" alt="ABET" style="width:50%; height:auto"/></td>
        </tr>
    </theader>
    <tbody>
        <tr><td colspan="3"><span style="font-weight:bold;">Formato</span>: Guía de Práctica de Laboratorio / Talleres / Centros de Simulación</td></tr>
        <tr><td><span style="font-weight:bold;">Aprobación</span>:  2022/03/01</td><td><span style="font-weight:bold;">Código</span>: GUIA-PRLD-001</td><td><span style="font-weight:bold;">Página</span>: 1</td></tr>
    </tbody>
</table>
</div>

<div align="center">
<span style="font-weight:bold;">INFORME DE LABORATORIO</span><br />
<span>(formato estudiante)</span>
</div>


<table>
<theader>
<tr><th colspan="6">INFORMACIÓN BÁSICA</th></tr>
</theader>
<tbody>
<tr><td>ASIGNATURA:</td><td colspan="5">Programación Web 2</td></tr>
<tr><td>TÍTULO DE LA PRÁCTICA:</td><td colspan="5">Python</td></tr>
<tr>
<td>NÚMERO DE PRÁCTICA:</td><td>04</td><td>AÑO LECTIVO:</td><td>2022 A</td><td>NRO. SEMESTRE:</td><td>III</td>
</tr>
<tr>
<td>FECHA DE PRESENTACION:</td><td>05-Jun-2022</td><td>HORA DE PRESENTACION:</td><td colspan="3">21:00</td>
</tr>
<tr><td colspan="3">Integrantes:
<ul>
<li>Kevin Pedro Yare Chulunquia</li>
<li>Joel Erick Gutierrez Puma</li>
<li>Joaquín Gonzalo Paredes Mescco</li>
</ul>
</td>
<td>NOTA:</td><td colspan="2"></td>
</tr>
<tr><td colspan="6">DOCENTES:
<ul>
<li>Richart Smith Escobedo Quispe (rescobedoq@unsa.edu.pe)</li>
</ul>
</td>
</<tr>
</tdbody>
</table>


# Solución y resultados

## I.		SOLUCIÓN DE EJERCICIOS/PROBLEMAS

-   Para resolver los siguientes ejercicios sólo está permitido usar ciclos, condicionales, definición de listas por comprensión, sublistas, map, join, (+), lambda, zip, append, pop, range.

    1.  Implemente los métodos de la clase Picture. Se recomienda que implemente la clase picture por etapas, probando realizar los dibujos que se muestran en la siguiente preguntas.
    2.  Usando únicamente los métodos de los objetos de la clase Picture dibuje las siguientes figuras (invoque a draw):

           *    (a) ![(a)](Imagenes/ejercicio_02_a.png)

                        from interpreter import draw
                        from chessPictures import *
   
                        negro = knight._invColor(.)
                        blanco=knight.join(knigth._invColor(.))
                        figura=blanco.under(negro.join(knigth))
                        draw(figura)

           *    (b) ![(b)](Imagenes/ejercicio_02_b.png)
                        
                           from interpreter import draw
                           from chessPictures import *

                           negro = knight._invColor(.)
                           vicevernegro=negro.verticalMirror
                           blanco=knight.join(knigth._invColor(.))
                           figura=blanco.under(negro.join(knigth.verticalMirror))
                           draw(figura)

           *    (c) ![(c)](Imagenes/ejercicio_02_c.png)
               usando la función join de Picture.py y Ejercicio02c.py
               
                ```sh
                    from interpreter import draw
                    from chessPictures import *

                    unido = knight.join(king)
                    unido = unido.join(knight)
    
                    draw(unido)                                                                                     
                ```
                
          luego, ejecutar python ejercicio02d.py
           *    (d) ![(d)](Imagenes/ejercicio_02_d.png)

           usando la función join de Picture.py
              
              ```sh
                    def join(self, p):
                    """ Devuelve una nueva figura poniendo la figura del argumento 
                    al lado derecho de la figura actual """
                    arreglo = []
                    for i in range(len(self.img)):
                        arreglo.append(self.img[i] + p.img[i])
                    return Picture(arreglo)                                                                                       
                ```
                
          luego, ejecutar python ejercicio02d.py
            https://github.com/REPOSITORIOPW2/Lab04/blob/ec8c604197dd73643d83ade57096e354f7ca0a5e/Imagenes/pygame%20window%2005_06_2022%2023_16_19.png
          
           *    (e) ![(e)](Imagenes/ejercicio_02_e.png)

            usando la función join de Picture.py
              
              ```sh
                    def join(self, p):
                    """ Devuelve una nueva figura poniendo la figura del argumento 
                    al lado derecho de la figura actual """
                    arreglo = []
                    for i in range(len(self.img)):
                        arreglo.append(self.img[i] + p.img[i])
                    return Picture(arreglo)                                                                                       
                ```
        luego, ejecutar python ejercicio02d.py
        
           *    (f) ![(f)](Imagenes/ejercicio_02_f.png)

           *    (g) ![(g)](Imagenes/ejercicio_02_g.png)

#
    
## II.	SOLUCIÓN DE CUESTIONARIO

-   ¿Qué son los archivos *.pyc?

    Son archivos compilados y entendidos por el lengua de python.
    
-   ¿Para qué sirve el directorio __pycache__?

    __pycache__ es un directorio que contiene archivos de caché de bytecode que son generados automáticamente por python, con extensión .pyc archivos. Esta carpeta con los archivos .pyc son generadas en primera instancia por el interprete. Asi, su función es que los programas se ejecutan más rápido.
    
-   ¿Cuáles son los usos y lo que representa el subguión en Python?

    En python los el subguión es muy utilizado los usos son los siguientes:
    
       - Utilizarlo en Internacionalización (i18n) o Localización (l10n).

       - Almacenar el valor de la última expresión en intérprete.

       - Separar los dígitos de un número.

       - Ignorar valores específicos.

       - Dar significados especiales (y funciones) al nombre de variables o funciones.

#

## III.	CONCLUSIONES

- En conclusión, python es uno de los lenguajes de programación más usados en desarrollo de juegos, sistemas, software en general. 
- Por otro lado, tiene un aprendizaje rápido, sin embargo tiene sus rectricciones y/o políticas. Como por ejemplo, la identación. 

## REFERENCIAS Y BIBLIOGRÁFIA RECOMENDADAS
-   https://www.w3schools.com/python/python_reference.asp
-   https://docs.python.org/3/tutorial/
