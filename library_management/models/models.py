# -*- coding: utf-8 -*-


from odoo import models, fields, api

from odoo import _


class BookTags(models.Model):
    _name = "library_management.tags"

    name = fields.Char(string="Tag Name")
    color = fields.Integer(string="Color Index")
    #fun things


class Authors(models.Model):
    _name = "library_management.authors"

    name = fields.Char(string="Author Name", required=True)
    hometown = fields.Char(string="Author's Hometown")
    birth_date = fields.Float(string="Author's Birth Year", digits=(4, 0))


class Book(models.Model):
    _name = "library_management.book"

    image = fields.Binary(string="Cover Image")
    value = fields.Float(string="Value", digits=(5, 3))
    name = fields.Char(string="Book Name", required=True)
    authors = fields.Many2many(
        string="Authors", comodel_name="library_management.authors")
    editors = fields.Char(string="Editors")
    date = fields.Date(string="Date of Publication")
    isbn = fields.Float(string="ISBN")
    status = fields.Selection(
        selection=[('available', 'Available'), ('rented', 'Rented')])
    user_id = fields.Many2one(comodel_name="res.users", string="User Owner")
    tag_id = fields.Many2many(comodel_name="library_management.tags",
                              relation="rel_book_tag_m2m", column1="book_id", column2="tag_id", string="Tags")
    log_id = fields.One2many(
        comodel_name="library_management.log", inverse_name="book_id", string="Logs")
    log_count = fields.Integer(compute="_log_count", string="#Nbr Logs")

    @api.multi
    @api.depends("log_id")
    def _log_count(self):
        for record in self:
            record.log_count = len(record.log_id.ids)


class Customer(models.Model):
    _name = "library_management.customer"
    _order = "sequence, id"

    name = fields.Char(string="Customer Name", required=True)
    sequence = fields.Integer(string="Sequence", default=10)
    code = fields.Char(string="Code")
    books_loaned = fields.Many2many(
        string="Books loaned to customer", comodel_name="library_management.book")
    address1 = fields.Char(string="Address Line 1")
    address2 = fields.Char(string="Address Line 2")
    city = fields.Char(string="City")
    state = fields.Selection(selection=[('AL', 'Alabama'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), (
        'MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')])
    zipcode = fields.Float(string="Zip Code")
    emails = fields.Char(string="Emails")

    @api.model
    def create(self, vals):
        vals.update({
            "code": self.env["ir.sequence"].next_by_code("library_management.customer")
        })
        res = super(Customer, self).create(vals)
        return res


class RentalLog(models.Model):
    _name = "library_management.log"

    checked_out = fields.Date(string="Date Loaned")
    checked_in = fields.Date(string="Date Returned")
    cust_id = fields.Many2one(
        comodel_name="library_management.customer", string="Loanee")
    book_id = fields.Many2one(
        comodel_name="library_management.book", string="Book name")


# class /home/darren/library_management(models.Model):
#     _name = '/home/darren/library_management./home/darren/library_management'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
