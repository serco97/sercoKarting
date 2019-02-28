# -*- coding: utf-8 -*-

from odoo import models, fields, api
import re
from odoo.exceptions import ValidationError

class empleado(models.Model):
    _name = 'serco_karting.empleado'
    name = fields.Char(string = "DNI",size=9, required = True)
    nombre = fields.Char(string="Nombre", required = True)
    apellidos = fields.Char(string="Apellidos", required = True)
    edad = fields.Integer(string ="Edad", required = True)
    puesto = fields.Many2one("serco_karting.puesto", string = "Ocupacion del trabajador")

    @api.onchange('name')
    def validate_dni(self):
        if self.name:
            match = re.match('[1-9]{8}[BCDFGHJKLMNPQRSTVXYZ]{1}$', self.name)
            if match == None:
                raise ValidationError('No es un DNI valido')

class puesto(models.Model):
    _name = 'serco_karting.puesto'
    name = fields.Char(string = "Nombre", required = True)
    descripcion = fields.Text(string = "Descripcion de las labores a realizar")


class vehiculos(models.Model):
    _name = 'serco_karting.vehiculos'
    identificador = fields.Integer(string = "Identificador", required = True)
    modelo = fields.Char(string = "Modelo Kart",required = True)
    ruedas = fields.Many2one("serco_karting.estados", string = "Estado de las ruedas",required = True)
    gasolina = fields.Many2one("serco_karting.estados", string = "Estado de la gasolina",required = True)
    aceite = fields.Many2one("serco_karting.estados", string = "Estado del aceite",required = True)
    empleado = fields.Many2one("serco_karting.empleado", string = "Empleado a cargo",required = True)


class estados(models.Model):
    _name = 'serco_karting.estados'
    identificador = fields.Char(string = "Identificador", required = True)
    name = fields.Char(string = "Estado", required = True)

class piezas(models.Model):
    _name = 'serco_karting.piezas'
    name = fields.Char(string = "Nombre", required = True)
    identificador = fields.Integer(string = "Identificador",size = 4, required = True)
    estado = fields.Many2one("serco_karting.estados",string = "Estado de la pieza", required = True)
    cantidad = fields.Integer(string = "Cantidad", required = False)
    proveedor = fields.Many2one("serco_karting.proveedor",string = "Proveedor", required = False)

class proveedor(models.Model):
    _name = 'serco_karting.proveedor'
    name = fields.Char(string = "Nombre", required = True)
    identificador = fields.Integer(string = "Identificador", required = True)
    email = fields.Char(string = "Email", required = True)
    direccion = fields.Char(string = "Direccion", required = True)
    fax = fields.Char(string = "Fax", required = False)

    @api.onchange('email')
    def validate_mail(self):
       if self.email:
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.email)
        if match == None:
            raise ValidationError('No es un email valido')

    @api.onchange('fax')
    def validate_fax(self):
        if self.fax:
            match = re.match('[1-9]{9}',self.fax)
            if match == None:
                raise ValidationError('El numero de fax tiene que contener 9 digitos\n EJEMPLO: 941000000')

class pista(models.Model):
    _name = 'serco_karting.pista'
    empleado = fields.Many2one("serco_karting.empleado", string = "Empleado", required = True)
    fecha = fields.Date(string = "Fecha mantenimiento", required = True)
    estado = fields.Many2one("serco_karting.estados",String = "Estado", required = True)
    descripcion = fields.Char(string = "Pequeña descripcion", required = True)

class tiempo_carreras(models.Model):
    _name = 'serco_karting.tiempo_carreras'
    cliente2 = fields.Many2one("serco_karting.clientes",string = "Cliente", required = True)
    tiempo = fields.Datetime(string = "Tiempo", required = True)

class bar(models.Model):
    _name = 'serco_karting.bar'
    empleado = fields.Many2one("serco_karting.empleado",string = "Empleado", required = True)
    fecha = fields.Char(string = "Revision bar", required = True)
    productosBar = fields.Char(string = "Productos necesarios", required = False)


class productos_bar(models.Model):
    _name = 'serco_karting.productos_bar'
    name = fields.Char(string = "Identificador", required = True)
    nombre = fields.Char(string = "Nombre producto", required = True)
    precio = fields.Char(string = "Precio", required = False)
    proveedor = fields.Many2one("serco_karting.proveedor",string = "Proveedor", required = True)

    @api.onchange('precio')
    def validate_precio(self):
        if self.precio:
            match = re.match('^[0-9]*[€]$',self.precio)
            if match == None:
                raise ValidationError('El precio debe ir indicado asi : 100€')

class competiciones(models.Model):
    _name = 'serco_karting.competiciones'
    nombre = fields.Char(string = "Nombre de la competicion", required = True)
    fecha = fields.Date(string = "Fecha competicion", required = True)
    participantes = fields.One2many("serco_karting.clientes","identificador",string = "participantes", required = True)
    premio = fields.One2many("serco_karting.premios","name",string = "premios",required = True)

class clientes(models.Model):
    _name = 'serco_karting.clientes'
    identificador = fields.Integer(string = "Identificador", required = True)
    nombre = fields.Char(string = "Nombre",required = True)
    telefono = fields.Char(string = "Telefono", required = True)
    email = fields.Char(string = "Email", required = True)
    premios = fields.One2many("serco_karting.premios","name",string = "Premios", required = False)

    @api.onchange('email')
    def validate_mail(self):
       if self.email:
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', self.email)
        if match == None:
            raise ValidationError('No es un email valido')

    @api.onchange('telefono')
    def validate_fax(self):
        if self.telefono:
            match = re.match('[1-9]{9}',self.telefono)
            if match == None:
                raise ValidationError('El numero de telefono tiene que contener 9 digitos\n EJEMPLO: 941000000')

class premios(models.Model):
    _name = 'serco_karting.premios'
    name = fields.Char(string = "Nombre", required = True)
    descripcion = fields.Char(string = "Pequeña descripcion", required = True)
