import pickle

class arcP1:
    nombre: str
    arc: object
    codif: str

    def __init__(self, nom, cod="utf-8"):
        self.nombre = nom
        self.codif = cod
        self.arc = None

    def crear(self):
        try:
            self.arc = open(self.nombre, "x")
        except (FileExistsError, Exception) as e:
            print(self.nombre, ":", e)
        finally:
            if self.arc:
                self.arc.close()

    def abrir(self, modo, code=""):
        try:
            if code == "":
                self.arc = open(self.nombre, modo)
            else:
                self.arc = open(self.nombre, modo, code)
        except (IOError, IndexError, FileNotFoundError) as e:
            print(self.nombre, ":", e)

    def cerrar(self):
        try:
            if self.arc:
                self.arc.close()
        except Exception as e:
            print(self.nombre, ":", e)

    def grabar(self, datos, code):
        try:
            if code == 'P':
                pickle.dump(datos, self.arc)
            else:
                if code == 'B':
                    datos = datos.encode()
                self.arc.write(datos)
        except (IndexError, FileNotFoundError, IOError) as e:
            print(self.nombre, ":", e)

    def leer(self, code=''):
        try:
            if not self.arc.closed:
                self.arc.seek(0)
                if code == 'P':
                    datos = pickle.load(self.arc)
                else:
                    datos = self.arc.read()
            else:
                with open(self.nombre, "rb") as self.arc:
                    if code == 'P':
                        datos = pickle.load(self.arc)
                    else:
                        datos = self.arc.read()
                    return datos
        except (IOError, IndexError, FileNotFoundError) as e:
            if(code != '' and code != 'P'):
                print(self.nombre, ":", e)
            return b''

    # -----------------------------
    # Agregar texto al archivo
    # -----------------------------
    def agregar(self, texto):
        try:
            with open(self.nombre, "a", encoding=self.codif) as f:
                f.write(texto + "\n")
        except Exception as e:
            print(f"{self.nombre}: Error al agregar -> {e}")

    # -----------------------------
    # Eliminar palabra del archivo
    # -----------------------------
    def eliminar(self, palabra):
        try:
            with open(self.nombre, "r+", encoding=self.codif) as f:
                contenido = f.read()
                nuevo_contenido = ' '.join([w for w in contenido.split() if w != palabra])
                f.seek(0)
                f.write(nuevo_contenido)
                f.truncate()
        except Exception as e:
            print(f"{self.nombre}: Error al eliminar -> {e}")

    # -----------------------------
    # Buscar palabra y devolver posiciones por caracter
    # -----------------------------
    def buscar(self, palabra):
        posiciones = []
        try:
            with open(self.nombre, "r", encoding=self.codif) as f:
                contenido = f.read()
                index = 0
                while True:
                    index = contenido.find(palabra, index)
                    if index == -1:
                        break
                    posiciones.append(index + 1)
                    index += len(palabra)
        except Exception as e:
            print(f"{self.nombre}: Error al buscar -> {e}")
        return posiciones

    # -----------------------------
    # Calcular frecuencia de palabras
    # -----------------------------
    def frecuencia(self):
        frec = {}
        try:
            with open(self.nombre, "r", encoding=self.codif) as f:
                palabras = f.read().split()
                for w in palabras:
                    frec[w] = frec.get(w, 0) + 1
        except Exception as e:
            print(f"{self.nombre}: Error al calcular frecuencia -> {e}")
        return [(palabra, cant) for palabra, cant in frec.items()]

