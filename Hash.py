import hashlib
class Hash_Function():
    def __init__(self,valor):
        self.valor = valor

    def Hashing(self,valor):
        hash_object = hashlib.md5(valor.encode())
        hex_dig = hash_object.hexdigest()
        return hex_dig

    #Insertar un nuevo elemento
    def insertar(self, valor):
        hash = self.hash_function(valor)
        if self.tabla[hash] is None:
            return None
        else:
            return hex(id(self.tabla[hash]))
    
    #Eliminar un elemento
    def eliminar(self, valor):
        hash = self.hash_function(valor)
        if self.tabla[hash] is None:
            print("No hay elementos con ese valor", valor)
        else:
            print("Elemento con valor", valor, "eliminado")
            self.tabala[hash] is None;
        
