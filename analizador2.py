
import ply.yacc as yacc
from tarealex import tokens, lexico  # 'lexico' es la función de análisis léxico

# Reglas para PLY
def p_statement_for(p):
    '''statement : PR'''
    p[0] = ('bucle_for', p[1], 'Correcto')

def p_statement_id(p):
    '''statement : ID'''
    p[0] = ('identificador', p[1], 'Incorrecto')

def p_syntax_error(p):
    print(f"Error de sintaxis encontrado en: '{p.value}'")
    p[0] = ('error_sintaxis', p.value, 'Error de sintaxis')

# Crear el parser
parser = yacc.yacc()

# Función principal para análisis sintáctico
def analizar_sintaxis(entrada):
    resultado = []
    try:
        # Usamos el análisis léxico de 'lexico'
        tokens = lexico(entrada)
        parser.parse(entrada)  # Aquí se realiza el análisis sintáctico

        for token in tokens:
            if token['valor'] == 'for':
                resultado.append({'linea': token['linea'], 'tipo': 'for', 'escritura': 'Correcto'})
            else:
                resultado.append({'linea': token['linea'], 'tipo': token['valor'], 'escritura': 'Incorrecto'})
    except Exception as e:
        print(f"Error de sintaxis: {e}")
        resultado.append({'linea': '-', 'tipo': '-', 'escritura': 'Error de sintaxis'})
    
    return resultado













