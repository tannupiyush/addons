from openerp.osv import fields, osv
from openerp.tools.safe_eval import safe_eval as eval
from openerp.addons.base.res.res_partner import format_address
from openerp.tools.translate import _

class crm_lead(format_address, osv.osv):
    _inherit = "crm.lead"

    _columns = {
        'c_fli_sector': fields.char('Sector'),
        'c_fli_prefer_airline': fields.char('Preferred Airlines'),
        'c_fli_departure_Date': fields.date('Departure Date'),
        'c_fli_return_date': fields.date('Return Date'),
        'c_fli_departure_Date2': fields.date('Departure Date2'),
        'c_fli_return_date2': fields.date('Return Date2'),
        'c_fli_departure_Date3': fields.date('Departure Date3'),
        'c_fli_return_date3': fields.date('Return Date3'),
        'c_fli_class_travel': fields.char('Class of Travel'),
        'c_fli_no_pax': fields.char('No. of Pax'),
        'c_fli_remarks': fields.text('Remarks'),
        'c_fli_date2_check': fields.boolean('Date2 check'),
        'c_fli_date3_check': fields.boolean('Date3 check'),
        'c_fli_remove_date':fields.boolean('Date2 remove'),
        'c_fli_remove_date3': fields.boolean('Date3 remove'),

        'c_ho_destinat': fields.char('Destination'),
        'c_ho_name': fields.char('Hotel Name'),
        'c_ho_check_in_date': fields.date('Check in Date'),
        'c_ho_check_out_date': fields.date('Check out Date'),
        'c_ho_check_in_date2': fields.date('Check in Date2'),
        'c_ho_check_out_date2': fields.date('Check out Date2'),
        'c_ho_check_in_date3': fields.date('Check in Date3'),
        'c_ho_check_out_date3': fields.date('Check out Date3'),
        'c_ho_no_rooms': fields.char('No. of Rooms'),
        'c_ho_no_pax': fields.char('No. of Pax'),
        'c_ho_meal_plan': fields.char('Meal Plan'),
        'c_ho_remarks': fields.text('Remarks'),
        'c_ho_date2_check': fields.boolean('Date2 check'),
        'c_ho_date3_check': fields.boolean('Date3 check'),
        'c_ho_remove_date': fields.boolean('Date2 remove'),
        'c_ho_remove_date3': fields.boolean('Date3 remove'),

        'c_tax_pick_up_loc': fields.char('Pick Up Location'),
        'c_tax_drop_loc': fields.char('Drop Location'),
        'c_tax_pick_up_date': fields.date('Pick Up date'),
        'c_tax_drop_date': fields.date('Drop Date'),
        'c_tax_pick_up_date2': fields.date('Pick Up date2'),
        'c_tax_drop_date2': fields.date('Drop Date2'),
        'c_tax_pick_up_date3': fields.date('Pick Up date3'),
        'c_tax_drop_date3': fields.date('Drop Date3'),
        'c_tax_vech_type': fields.char('Vehicle Type'),
        'c_tax_no_pax': fields.char('No. of Pax'),
        'c_tax_remarks': fields.text('Remarks'),
        'c_tax_date2_check': fields.boolean('Date2 check'),
        'c_tax_date3_check': fields.boolean('Date3 check'),
        'c_tax_remove_date': fields.boolean('Date2 remove'),
        'c_tax_remove_date3': fields.boolean('Date3 remove'),

        'c_vi_country': fields.char('Country'),
        'c_vis_category': fields.selection([('Business','Business'),('Tourist','Tourist'),('Transit','Transit')],string='Visa Category'),
        'c_vi_departure_date': fields.date('Departure Date'),
        'c_vi_arrival_date': fields.date('Arrival Date'),
        'c_vi_departure_date2': fields.date('Departure Date2'),
        'c_vi_arrival_date2': fields.date('Arrival Date2'),
        'c_vi_departure_date3': fields.date('Departure Date3'),
        'c_vi_arrival_date3': fields.date('Arrival Date3'),
        'c_vi_no_pax': fields.char('No. of Pax'),
        'c_vi_date_sub': fields.date('Date of Submission'),
        'c_vi_exp_date': fields.date('Expected Date of Collection'),
        'c_vi_remarks': fields.text('Remarks'),
        'c_vi_date2_check': fields.boolean('Date2 check'),
        'c_vi_date3_check': fields.boolean('Date3 check'),
        'c_vi_remove_date': fields.boolean('Date2 remove'),
        'c_vi_remove_date3': fields.boolean('Date3 remove'),

    }
    _defaults = {
        'c_fli_date2_check':False,
        'c_fli_date3_check': False,
        'c_ho_date2_check': False,
        'c_ho_date3_check': False,
        'c_tax_date2_check': False,
        'c_tax_date3_check': False,
        'c_vi_date2_check':False,
        'c_vi_date3_check': False,
        'c_fli_remove_date':False,
        'c_ho_remove_date':False,
        'c_tax_remove_date':False,
        'c_vi_remove_date':False,
        'c_fli_remove_date3':False,
        'c_ho_remove_date3': False,
        'c_tax_remove_date3': False,
        'c_vi_remove_date3': False,
    }

    def date2_view(self, cr, uid, ids, context=None):
        for lead in self.browse(cr, uid, ids, context=context):
            lead.c_fli_date2_check = True
            lead.c_fli_remove_date = False

    def date3_view(self, cr, uid, ids, context=None):
        for lead in self.browse(cr, uid, ids, context=context):
            lead.c_fli_date3_check = True
            lead.c_fli_remove_date3 = False

    def fli_remove_date2(self, cr, uid, ids, context=None):
        for lead in self.browse(cr, uid, ids, context=context):
            lead.c_fli_remove_date = True
            lead.c_fli_date2_check = False

    def fli_remove_date3(self, cr, uid, ids, context=None):
        for lead in self.browse(cr, uid, ids, context=context):
            lead.c_fli_remove_date3 = True
            lead.c_fli_date3_check = False

    def hotel_date2_view(self, cr, uid, ids, context=None):
        for lead in self.browse(cr, uid, ids, context=context):
            lead.c_ho_date2_check = True
            lead.c_ho_remove_date = False

    def hotel_date3_view(self, cr, uid, ids, context=None):
        for lead in self.browse(cr, uid, ids, context=context):
            lead.c_ho_date3_check = True
            lead.c_ho_remove_date3 = False

    def hotel_remove_date2(self, cr, uid, ids, context=None):
        for lead in self.browse(cr, uid, ids, context=context):
            lead.c_ho_remove_date = True
            lead.c_ho_date2_check = False

    def hotel_remove_date3(self, cr, uid, ids, context=None):
        for lead in self.browse(cr, uid, ids, context=context):
            lead.c_ho_remove_date3 = True
            lead.c_ho_date3_check = False

    def taxi_date2_view(self, cr, uid, ids, context=None):
        for lead in self.browse(cr, uid, ids, context=context):
            lead.c_tax_date2_check = True
            lead.c_tax_remove_date = False

    def taxi_date3_view(self, cr, uid, ids, context=None):
        for lead in self.browse(cr, uid, ids, context=context):
            lead.c_tax_date3_check = True
            lead.c_tax_remove_date3 = False

    def taxi_remove_date2(self, cr, uid, ids, context=None):
        for lead in self.browse(cr, uid, ids, context=context):
            lead.c_tax_remove_date = True
            lead.c_tax_date2_check = False

    def taxi_remove_date3(self, cr, uid, ids, context=None):
        for lead in self.browse(cr, uid, ids, context=context):
            lead.c_tax_remove_date3 = True
            lead.c_tax_date3_check = False

    def visa_date2_view(self, cr, uid, ids, context=None):
        for lead in self.browse(cr, uid, ids, context=context):
            lead.c_vi_date2_check = True
            lead.c_vi_remove_date = False

    def visa_date3_view(self, cr, uid, ids, context=None):
        for lead in self.browse(cr, uid, ids, context=context):
            lead.c_vi_date3_check = True
            lead.c_vi_remove_date3 = False

    def vasi_remove_date2(self, cr, uid, ids, context=None):
        for lead in self.browse(cr, uid, ids, context=context):
            lead.c_vi_remove_date = True
            lead.c_vi_date2_check = False

    def vasi_remove_date3(self, cr, uid, ids, context=None):
        for lead in self.browse(cr, uid, ids, context=context):
            lead.c_vi_remove_date3 = True
            lead.c_vi_date3_check = False

