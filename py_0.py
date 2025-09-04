import os
from string import ascii_lowercase
from typing import Any, Iterable, Iterator, Generator
from math import sin,cos, pi
from getpass import getpass
from numbers import Number

class py:
    @staticmethod
    def isPrime(number: int):
        if number % 2 == 0:
            return False
        dividers: int = 3
        while dividers * dividers <= number:
            if number % dividers == 0:
                return False
            dividers += 2
        return True

    @staticmethod
    def range(start: int, end: int = 0, step: int = 1) -> range:
        if not end:
            return range(1,start+1)
        return range(start, end+1, step) if step > 0 else range(start, end-1, step) 

    @staticmethod
    def input(msg: str, clear: bool = True) -> str:
        if clear:
            ui.clear()
        print(f"{fmat.bold}{msg}")
        return input(f"> {fmat.end}")

    @staticmethod
    def int_input(msg: str, mt: int = None, lt: int = None, eq: bool = False) -> int:
        err: str = ""
        while True:
            ui.clear()
            if err:
                print(err)
                err = ""
            try:
                try:
                    if mt != None and lt != None and mt == lt: return mt
                    sel_int: int = int(py.input(msg, clear = False))
                except:
                    raise TypeError
                if mt != None:
                    if eq and sel_int < mt:
                        raise ValueError(f"ERROR: Ingrese un Número MAYOR o IGUAL a {mt}.")
                    elif sel_int < mt:
                        raise ValueError(f"ERROR: Ingrese un Número MAYOR a {mt}.")
                if lt != None:
                    if eq and sel_int > lt:
                        raise ValueError(f"ERROR: Ingrese un Número MENOR o IGUAL a {lt}.")
                    elif sel_int > lt:
                        raise ValueError(f"ERROR: Ingrese un Número MENOR a {lt}.")
                return sel_int
            except TypeError:
                err: str = f"{fmat.error}ERROR: Ingrese un Número ENTERO válido.{fmat.end}"
            except ValueError as e:
                err: str = f"{fmat.error}{e}{fmat.end}"

    @staticmethod
    def float_input(msg: str) -> int:
        err = ""
        while True:
            ui.clear()
            if err:
                print(err)
                err = ""
            try:
                sel_int: float = float(py.input(msg))
                return sel_int
            except ValueError:
                err: str = f"{fmat.error}ERROR: Ingrese un Número REAL válido.{fmat.end}"

    @staticmethod
    def getPassword(msg: str) -> str:
        print(msg)
        return getpass("> ")

    @staticmethod
    def print(*args: Any, sep: str = " ", end: str = "\n", raw: bool = False, indent: int = 0) -> None:
        #?/ ================================================ /?#
        validIter: bool = lambda iterable: (
                        hasattr(iterable, '__iter__') 
                        and not isinstance(iterable, str))

        #?/ ================================================ /?#

        def print_collection(opening, closing, collection):
            if all(not validIter(item) for item in collection):
                # Flat collections: print on one line
                for i, item in enumerate(collection):
                    if i < len(collection) - 1:  # Add separator if not the last item
                        print(f"{fmat.tab * indent}{opening}{sep.join(map(str, collection))}{closing}{end}")
                    else:
                        print(f"{fmat.tab * indent}{opening}{sep.join(map(str, collection))}{closing}")
            else:
                # Nested collections: print with indentation
                print(f"{fmat.tab * indent}{opening}")
                for i, item in enumerate(collection):
                    if i < len(collection) - 1:  # Add separator if not the last item
                        py.print(item, sep=sep, end=',', raw=raw, indent=indent + 1)
                    else:
                        py.print(item, sep=sep, end=end, raw=raw, indent=indent + 1)
                if end == ',':
                    print(f"{fmat.tab * indent}{closing}{end}")
                else:
                    print(f"{fmat.tab * indent}{closing}")

        def print_dict(collection, opening='{', closing='}'):
            print(f"{fmat.tab * indent}{opening}")
            ind = indent + 1
            max_key_length = max((len(str(key)) for key in collection), default=0)
            for i, (key, value) in enumerate(collection.items()):
                key_str = str(key).ljust(max_key_length + 1)
                if (validIter(value) and all(not validIter(item) for item in value)) or not validIter(value):
                    if i < len(collection) - 1:  # Add separator if not the last item
                        print(f"{fmat.tab * ind}{fmat.bold}{key_str}:{fmat.end} {value},")
                    else:
                        print(f"{fmat.tab * ind}{fmat.bold}{key_str}:{fmat.end} {value}")
                else:
                    print(f"{fmat.tab * ind}{fmat.bold}{key_str}:{fmat.end}")
                    if i < len(collection) - 1:  # Add separator if not the last item
                        py.print(value, sep=sep, end=',', raw=raw, indent=ind + 1)
                    else:
                        py.print(value, sep=sep, end=end, raw=raw, indent=ind + 1)
            if end == ',':
                print(f"{fmat.tab * indent}{closing}{end}")
            else:
                print(f"{fmat.tab * indent}{closing}")

        #?/ ================================================ /?#

        filtered: list = list(filter(validIter, args))

        if not filtered or raw:
                print(f"{fmat.tab * indent}", end="")
                print(*args, sep=sep, end=end)
                return None

        #?/ ================================================ /?#

        for arg in args:
            if isinstance(arg, dict):
                print_dict(arg)
            elif isinstance(arg, list):
                print_collection("[", "]", arg)
            elif isinstance(arg, tuple):
                print_collection("(", ")", arg)
            elif isinstance(arg, set):
                print_collection("{-", "-}", arg)
            elif isinstance(arg, (Iterator, Generator)):
                for value in arg:
                    print(value,end=' ')
            else:
                print(f'{fmat.tab * indent}{arg}', sep=sep, end=end)

    @staticmethod
    def sin(value) -> float:
        return sin((value*pi)/180)

    @staticmethod
    def sen(value) -> float:
        return py.sin(value)

    @staticmethod
    def cos(value) -> float:
        return cos((value*pi)/180)

class ui:
    name: str = os.name

    @staticmethod
    def opt_menu(opts: list, title: str) -> str:

        # Se aplica .lower() a las opciones, para mejor manejo de input
        for i in range(0, len(opts)):
            opts[i] = opts[i].lower()

        # Se crea la lista de opciones alternas (numeraciones), y se inicia el mensaje de error en falso
        alt_opts: list = []
        err: bool = False

        # Revisa si hay al menos una opción que tenga un dígito de primer caracter
        has_digit: bool = any([opt[0].isdigit() for opt in opts])

        # Si hay al menos una opción que cumpla la condición, se enumera con letras
        if has_digit:
            for i in range(len(opts)):
                alt_opts.append(select.abckey[i])

        # En cambio, si no se cumple la condición, se enumera con números
        else:
            for i in range(1, len(opts)+1):
                alt_opts.append(str(i))

        # Ciclo Principal del Menú (Para Manejo de Errores y Limpieza de pantalla)
        while True:
            ui.clear()
            print(f"{fmat.bold}{title}{endl}{fmat.end}")
            if err:
                print(f"{fmat.error}{err}{fmat.end}{endl}")
                err = None
            opt_ind: int = 0

            # Imprimir Opciones (Y opciones elegidas en caso de que sea selección múltiple)
            for opt in opts: 
                print(fmat.bold + alt_opts[opt_ind] + ".", opt.capitalize())
                opt_ind += 1
            
            # Manejo de ingreso del usuario, si el input está dentro de las numeraciones (1,2,3... | a,b,c...), se reemplazará por su valor dentro de las opciones.
            
            print()
            sel = input("> "+fmat.end).lower()
            print()
            
            if sel in alt_opts:
                sel = opts[alt_opts.index(sel)]
            
            # Retornar en caso de que exista la opción elegida.
            if sel in opts:
                return sel

            # Error en caso de que no exista la opción elegida.
            else:
                err = f"{fmat.bold}{fmat.red}ERROR: Elija un valor válido."


    @staticmethod
    def clear() -> None:
        os.system('cls' if ui.name == 'nt' else 'clear')
        print()

    @staticmethod
    def pause() -> None:
        ui.sep()
        os.system('pause' if ui.name == 'nt'
                  else "/bin/bash -c 'read -s -n 1 -p \"Presione una tecla para continuar . . .\"'")
        ui.clear()

    @staticmethod
    def menu(title: str, error: str = None) -> None:
        ui.clear()
        print(fmat.bold+title+endl+fmat.end)
        if error:
            print(fmat.bold + fmat.red + error + fmat.end + endl)

    @staticmethod
    def sep(msg: str = "",sep: int = 30) -> None:
        if not msg:
            msg = "="*sep
        else:
            msg = f"{f'| {msg} |':=^{sep}}"
        print(endl+msg+endl)

    @staticmethod
    def title(msg: str, sep: int = None, ret: bool = False,sep_char = "=", indent = 0) -> Any:
        if not sep:
            sep = len(msg)
        newStr: str = f"{fmat.tab * indent}{fmat.bold}{sep_char*(sep + 4)}\n{fmat.tab * indent}{msg.center(sep+4)}\n{fmat.tab * indent}{sep_char*(sep + 4)}{fmat.end}"
        if not ret:
            print(newStr)
        else:
            return newStr


endl: str = '\n'
na  : str = 'n/a' 


class fmat:
    red         : str =   '\033[31m'
    green       : str =   '\033[32m'
    yellow      : str =   '\033[33m'
    blue        : str =   '\033[34m'
    purple      : str =   '\033[35m'
    cyan        : str =   '\033[36m'
    bold        : str =   '\033[1m'
    pale        : str =   '\033[2m'
    italic      : str =   '\033[3m'
    underline   : str =   '\033[4m'
    end         : str =   '\033[0m'
    tab         : str =   '  '
    debug       : str =   f'{green+pale+italic}'
    error       : str =   f'{red+bold}'
    warn        : str =   f'{yellow+bold}'


class select:
    abckey: str      = ascii_lowercase
    num_check: str    = "0123456789"
    true_check: list  = ["true", "v", "verdadero", "si", "yes", "y"]
    false_check: list = ["false", "f", "falso", "no"]

    @staticmethod
    def option(opts: list, title: str, multi: bool = False, v_f: bool = False, err: str = None) -> str or list:  # type: ignore

        for i in range(0, len(opts)):
            opts[i] = opts[i].lower()

        # Inicialización Variables
        alt_opts = []
        if multi:
            selected: list[str] = []

        # Verificar si hay al menos una opción que sea un dígito
        has_digit = any([opt[0].isdigit() for opt in opts])

        # Si hay al menos una opción que es un dígito, enumerarlas con letras

        if has_digit:
            for i in range(len(opts)):
                alt_opts.append(select.abckey[i])

        # Si todas las opciones son texto, enumerarlas con números
        else:
            for i in range(1, len(opts)+1):
                alt_opts.append(str(i))
        # for num in enumerate(opts):

        while True:
            ui.menu(title, err)
            opt_n = 1
            err = None

            # Imprimir Opciones (Y opciones elegidas en caso de que sea selección múltiple)
            for opt in opts: 
                if multi and opt in selected:
                    print(fmat.bold + fmat.yellow + alt_opts[opt_n-1] + ".", opt.capitalize() + fmat.end)
                else:
                    print(fmat.bold + alt_opts[opt_n-1] + ".", opt.capitalize())
                opt_n += 1
            
            # Imprimir "0. Terminar" como opción para finalizar la selección múltiple.
            if multi:
                print(endl + fmat.bold + "0. Terminar" + fmat.end + endl)
            
            # Manejo del input. Si input está dentro de las numeraciones (1,2,3... | a,b,c...), se reemplazará
            # por su valor dentro de las opciones.
            
            print()
            sel = input("> "+fmat.end).lower()
            print()
            if sel in alt_opts:
                sel = opts[alt_opts.index(sel)]

            # Si es opción de "sí" o "no", entonces verifica todas las opciones posibles de true_check y false_check
            if v_f:
                if sel in select.true_check:
                    return "si"
                elif sel in select.false_check:
                    return "no"
            # Si es opción múltiple, actualiza la lista de opciones seleccionadas, y retornar la lista
            # en caso de terminar. 
            elif multi:
                if sel in ["terminar", "0"]:
                    return selected
                if sel in opts:
                    if sel not in selected:
                        selected.append(sel)
                    else:
                        selected.remove(sel)
                else:
                    # Manejo de error en caso de que no exista la opción elegida.
                    err = f"{fmat.error}ERROR: Elija un valor válido."
            
            # Retornar en caso de que exista la opción elegida.
            elif sel in opts:
                return sel

            # Manejo de error en caso de que no exista la opción elegida.
            else:
                err = f"{fmat.bold}{fmat.red}ERROR: Elija un valor válido."
    
    @staticmethod
    def op_int(title: str = "", err: str = None) -> int:
        while True:
            ui.menu(title, err)
            try:
                sel_int: int = round(float(input("> ")))
                return sel_int
            except ValueError:
                err = f"{fmat.error}ERROR: Ingrese un Número ENTERO válido.{fmat.end}"
    
    @staticmethod
    def op_float(title: str = "", err: str = None) -> float:
        while True:
            ui.menu(title, err)
            try:
                sel_int: float = float(input("> "))
                return sel_int
            except ValueError:
                err = f"{fmat.error}ERROR: Ingrese un Número REAL válido.{fmat.end}"
        
    @staticmethod
    def option_vf(title: str) -> bool:
        sel = select.option(["si", "no"], title, v_f = True)
        print()
        if sel == "si":
            return True
        else:
            return False


class pyHex(Number):
    value: str
    data: type = None

    def __init__(self, value: Any) -> None:
        if not isinstance(value,(str,int,float)):
            raise TypeError(f"Cannot convert object of type {type(value)} to type <class 'hex'>.")
        self.__init_helper(value)

    def __init_helper(self, value: Any) -> None:
        
        if isinstance(value, str):
            try:
                value = hex(int(value, 16)).value
                self.value = value
            except ValueError:
                raise ValueError(f"Can't convert string object '{value}' to hex. Invalid input.")
            
            self.data = str
        elif isinstance(value, int):
            self.value = self.__inthex(value)
            self.data = int
        else:
            self.value = self.__flthex(value)
            self.data = float

    @staticmethod
    def decode(value: str) -> str:
        value = str(value)
        return bytes.fromhex(value).decode()

    @staticmethod
    def encode(text: str) -> list:
        return [hex(char.encode().hex()) for char in text]
       
    def __inthex(self, value: int) -> str:
        return '%02x' % value
    
    def __flthex(self, value: float) -> str:
        def calc_float(number: float) -> list:
            number *= 16
            number_list: list = str(number).split('.')
            return number_list

        value_list: list = str(value).split('.')
        value_int: int = int(value_list[0])
        value_float: float = float(f'0.{value_list[1]}')
        value_hex: str = f"{'%0x' % value_int}."

        new_value: float = value_float
        for _ in py.range(2):
            number_list: list = calc_float(new_value)
            number_int, number_float = number_list
            value_hex += '%0x' % int(number_int)
            if number_float == '0':
                break
            new_value = float(f"0.{str(int(number_float))}")
        return value_hex

    def __float__(self) -> float:
        value_list: list = str(self).split('.')
        value_int: int = int(f'0x{value_list[0]}', base = 16)
        value_str: str = value_list[1]
        value_float: float = round(sum([(int(f'0x{number}', base = 16)/(16**ind)) for ind, number in enumerate(value_str, start=1)]),2)
        value_int += value_float
        return value_int

    def __int__(self) -> int:
        if self.data == float:
            return int(float(self))
        if '-' in self.value:
            return - int(f'0x{self.value[1::]}', base = 16)
        return int(f'0x{self}', base = 16) 

    def __str__(self) -> str:
        if self.data == str:
            return ' '.join([self.value[ind:ind+2] for ind in range(0,len(self.value),2)])
        else:
            return self.value
    
    def __bool__(self) -> bool:
        return self != 0

    def __convert_to_type(self, value: Any, target_type: type) -> Any:
        if target_type == int:
            return int(value)
        elif target_type == float:
            return float(value)
        elif target_type == str:
            return str(value)
        return value

    def __perform_operation(self, other: object, operation: str) -> object:
        
        if not isinstance(other, Number):
            raise TypeError(f"Invalid operand between {type(self)} and {type(other)}")

        if self.data == str:
            self_value = self.__convert_to_type(self, int)
        else:
            self_value = self.__convert_to_type(self, self.data)

        if isinstance(other, pyHex):
            if other.data == str:
                other_value = self.__convert_to_type(other, int)
            else:
                other_value = self.__convert_to_type(other, other.data)
        else:
            other_value = other
        
        if operation == 'add':
            result = self_value + other_value
        elif operation == 'sub':
            result = self_value - other_value
        elif operation == 'mul':
            result = self_value * other_value
        elif operation == 'tdiv':
            result = self_value / other_value
        elif operation == 'fdiv':
            result = self_value // other_value
        elif operation == 'mod':
            result = self_value % other_value
        else:
            raise ValueError("Unsupported operation")

        new: pyHex = pyHex(result)
        
        return new
    
    def __comp(self, other: object) -> tuple:

        self_value = float(self) if self.data == float else int(self)
        if isinstance(other, pyHex):
            other_value = float(other) if other.data == float else int(other)
        else:
            other_value = other
        return self_value, other_value

    def __eq__(self, other: object) -> bool:
        self_value, other_value = self.__comp(other)
        return self_value == other_value

    def __lt__(self, other: object) -> bool:
        self_value, other_value = self.__comp(other)
        return self_value < other_value

    def __le__(self, other: object) -> bool:
        self_value, other_value = self.__comp(other)
        return self_value <= other_value

    def __gt__(self, other: object) -> bool:
        self_value, other_value = self.__comp(other)
        return self_value > other_value

    def __ge__(self, other: object) -> bool:
        self_value, other_value = self.__comp(other)
        return self_value >= other_value

    def __round__(self, roundValue: int = None) -> object:
        if self.data == str:
            self_value = self.__convert_to_type(self, int)
        else:
            self_value = self.__convert_to_type(self, self.data)
        return hex(round(self_value, roundValue))

    def __add__(self, other: object) -> object:
        return self.__perform_operation(other, 'add')

    def __radd__(self, other: Number) -> object:
        return self.__perform_operation(other, 'add')

    def __sub__(self, other: object) -> object:
        return self.__perform_operation(other, 'sub')

    def __rsub__(self, other: Number) -> object:
        return self.__perform_operation(other, 'sub')

    def __mul__(self, other: object) -> object:
        return self.__perform_operation(other, 'mul')

    def __rmul__(self, other: Number) -> object:
        return self.__perform_operation(other, 'mul')

    def __truediv__(self, other: object) -> object:
        return self.__perform_operation(other, 'tdiv')

    def __rtruediv__(self, other: Number) -> object:
        return self.__perform_operation(other, 'tdiv')

    def __floordiv__(self, other: object) -> object:
        return self.__perform_operation(other, 'fdiv')

    def __rfloordiv__(self, other: Number) -> object:
        return self.__perform_operation(other, 'fdiv')

    def __mod__(self, other: object) -> object:
        return self.__perform_operation(other, 'mod')
    
    def __rmod__(self, other: Number) -> object:
        return self.__perform_operation(other, 'mod')


# import logging as logger
from sys import _getframe as get_currentcodeframe


class logHandler:
    def __init__(self, name: str = os.path.basename(__file__)) -> None:
        self.name:    str = name
        self.logName: str = f"{fmat.underline}[{name}]{fmat.end}"

    def debug(self, msg: str = "") -> None:
        print(f'{fmat.debug+self.logName+fmat.debug}: line {self.get_codeline(1)}  | [DEBUG]: {msg}{fmat.end}')

    def info(self, msg: str = "")  -> None:
        print(f'{fmat.bold+self.logName+fmat.bold}: line {self.get_codeline(1)}  | [INFO]: {msg}{fmat.end}')

    def warn(self, msg: str = "")  -> None:
        print(f'{fmat.warn+self.logName+fmat.warn}: line {self.get_codeline(1)} | [WARN]: {msg}{fmat.end}')

    def error(self, msg: str = "") -> None:
        print(f'{fmat.error+self.logName+fmat.error}: line {self.get_codeline(1)} | [ERROR]: {msg}{fmat.end}')

    @staticmethod
    def get_codeline(back: int = 0) -> int:
        currentFrame = get_currentcodeframe(back + 1)
        return currentFrame.f_lineno


if __name__ == '__main__':
    ui.clear()
    py0log: logHandler = logHandler()
    py0log.warn(f"Se ha ejecutado {py0log.name}.")
    py0log.info("Esta es una librería/módulo. No tiene código a ejecutar.")
    print()
