import tipo_usuario

class Usuario(tipo_usuario): #HERENCIA
    def __init__(self, idUsuario, nombre, direccion, telefono, correoElectronico, id_tipo_usuario):
        tipo_usuario.Tipo_usuario.__init__(id_tipo_usuario)
        super().__init__(id_tipo_usuario)
        self.idUsuario = idUsuario
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correoElectronico = correoElectronico