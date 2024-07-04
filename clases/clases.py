import json 


#Creacion de la clase
class Producto:

    #Inicializacion de los atributos con uso de un metodo magico
    def __init__(self, codigoproducto, nombreproducto, inventarioproducto, precioproducto):
        self.__codigoproducto = codigoproducto
        self.__nombreproducto = nombreproducto
        self.__inventarioproducto = inventarioproducto
        self.__precioproducto = precioproducto
    
    #Comenzamos a nombrar set's de los atributos
    #def set_(self, value):
    #    self.__ = value
    def set_codigoproducto(self, value):
       self.__codigoproducto = value
    def set_nombreproducto(self, value):
       self.__nombreproducto = value
    def set_inventarioproducto(self, value):
       self.__inventarioproducto = value
    def set_precioproducto(self, value):
       self.__precioproducto = value
    

    #Comenzamos a nombrar get's de los atributos
    #def get_(self):
    #    return self.__ 
    def get_codigoproducto(self):
       return self.__codigoproducto
    def get_nombreproducto(self):
       return self.__nombreproducto
    def get_inventarioproducto(self):
       return self.__inventarioproducto
    def get_precioproducto(self):
       return self.__precioproducto

#Creacion de la segunda clase, no sabemos si es herencia de Producto
class ProductosVenta:
   
   #Inicializamos el unico atributo que es parte de esta clase, siendo una lista
    def __init__(self, listaproductos):
      self.__listaproductos = listaproductos
    
    #Nombramos el set de este unico atributo
    #def set_(self, value):
    #    self.__ = value
    def set_listaproductos(self, value):
       self.__listaproductos = value

    #Continuamos con el get de este unico atributo
    #def get_(self):
    #    return self.__ 
    def get_listaproductos(self):
       return self.__listaproductos
    
    #Aun con un unico atributo, tiene varios metodos, acontinuacion los creamos

    def digitardato(self):
        print('#')
    def cargararchivoproductos(self):
        print('#')
    def cargamanualproductos(self):
        print('#')
    def borrarproductos(self):
        print('#')
    def verificarborrarproductos(self):
        print('#')
    def nuevosproductos(self):
        print('#')
    def verificarcodigoproducto(self):
        print('#')
    def verificarnombreproducto(self):
        print('#')
    def grabararchivoproductos(self):
        print('#')
    def existenciaproductos(self):
        print('#')


class ProductoCarrito:
    def __init__(self, codigoproducto, nombreproducto, cantidadproducto, precioproducto, subtotalproducto):
        self.__codigoproducto = codigoproducto
        self.__nombreproducto = nombreproducto
        self.__cantidadproducto = cantidadproducto
        self.__precioproducto = precioproducto
        self.__subtotalproducto = subtotalproducto
    
    #Nombramos el set de sus atributos
    
    #def set_(self, value):
    #    self.__ = value
    def set_codigoproducto(self, value):
       self.__codigoproducto = value
    def set_nombreproducto(self, value):
       self.__nombreproducto = value
    def set_cantidadproducto(self, value):
       self.__cantidadproducto = value
    def set_precioproducto(self, value):
       self.__precioproducto = value
    def set_subtotalproducto(self, value):
       self.__subtotalproducto = value


    #Continuamos con el get de sus atributos

    #def get_(self):
    #    return self.__ 
    def get_codigoproducto(self):
       return self.__codigoproducto 
    def get_nombreproducto(self):
       return self.__nombreproducto
    def get_cantidadproducto(self):
       return self.__cantidadproducto
    def get_precioproducto(self):
       return self.__precioproducto
    def get_subtotalproducto(self):
       return self.__subtotalproducto

    # Creacion de los metodos
    #def (self):
    #   print('#')  

    # Funcion para la impresion de los productos de la tienda
    def digitardatos(self):
      print('#')
    def verificarcodigoproducto(self):
      print('#')
    def calcularvalor(self):
      print('#')
    def datoscompra(self):
      print('#')
    def datocodigoproducto(self):
      print('#')
    def datocantidadproducto(self):
      print('#')

#Creacion de la ultima clase
class CarritoCompra:
   
    #Creacion de los atributos
    def __init__(self, documentocliente, nombrecliente, direccioncliente, productoscarrito):
      self.__documentocliente = documentocliente
      self.__nombrecliente = nombrecliente
      self.__direccioncliente = direccioncliente
      self.__productoscarrito = productoscarrito
    
    #Nombramos el set de sus atributos
    
    #def set_(self, value):
    #    self.__ = value
    def set_documentocliente(self, value):
       self.__documentocliente = value

    def set_nombrecliente(self, value):
       self.__nombrecliente = value
    def set_direccioncliente(self, value):
       self.__direccioncliente = value
    def set_productoscarrito(self, value):
       self.__productoscarrito = value


    #Continuamos con el get de sus atributos

    #def get_(self):
    #    return self.__ 
    def get_documentocliente(self):
       return self.__documentocliente
    def get_nombrecliente(self):
       return self.__nombrecliente 
    def get_direccioncliente(self):
       return self.__direccioncliente
    def get_productoscarrito(self):
       return self.__productoscarrito


    # Creacion de los metodos
    #def (self):
    #   print('#')  
    def setnumeroproductoscarritocompra(self):
      print('#')  
    def digitardato(self):
      print('#')  
    def documentocliente(self):
      print('#')  
    def nombrecliente(self):
      print('#')     
    def direccioncliente(self):
      print('#')  
    def nuevoproducto(self):
      print('#')  
    def facturacompra(self):
      print('#')  
