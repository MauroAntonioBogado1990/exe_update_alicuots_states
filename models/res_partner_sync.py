# -*- coding: utf-8 -*-
from odoo import models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    def action_sync_alicuotas_from_padron(self):
        """Buscar en los padróns cargados (Tucumán y Santa Fe) y aplicar las
        alícuotas correspondientes al partner (por `vat`).
        Crea una entrada en los one2many correspondientes según provincia.
        """
        PadronT = self.env['tucuman.padron']
        PadronS = self.env['santafe.padron']

        for partner in self:
            if not partner.vat:
                continue
            norm_vat = ''.join(filter(str.isdigit, partner.vat))

            padrones_t = PadronT.search([('name', '=', norm_vat)])
            padrones_s = PadronS.search([('name', '=', norm_vat)])

            for padron in list(padrones_t) + list(padrones_s):
                # Tucumán
                if padron._name == 'tucuman.padron':
                    if padron.type_alicuot == 'R':
                        activas = partner.alicuot_ret_tucuman_ids.filtered('padron_activo')
                        if activas:
                            activas.write({'padron_activo': False})
                        partner.sudo().write({'alicuot_ret_tucuman_ids': [(0, 0, {
                            'partner_id': partner.id,
                            'publication_date': padron.publication_date,
                            'effective_date_from': padron.effective_date_from,
                            'effective_date_to': padron.effective_date_to,
                            'type_contr_insc': padron.type_contr_insc,
                            'alta_baja': padron.alta_baja,
                            'cambio': padron.cambio,
                            'a_ret': padron.a_ret,
                            'nro_grupo_ret': getattr(padron, 'nro_grupo_ret', False),
                            'padron_activo': True,
                            'coeficiente': getattr(padron, 'coeficiente', False),
                        })]})

                    elif padron.type_alicuot == 'P':
                        activas = partner.alicuot_per_tucuman_ids.filtered('padron_activo')
                        if activas:
                            activas.write({'padron_activo': False})
                        partner.sudo().write({'alicuot_per_tucuman_ids': [(0, 0, {
                            'partner_id': partner.id,
                            'publication_date': padron.publication_date,
                            'effective_date_from': padron.effective_date_from,
                            'effective_date_to': padron.effective_date_to,
                            'type_contr_insc': padron.type_contr_insc,
                            'alta_baja': padron.alta_baja,
                            'cambio': padron.cambio,
                            'a_per': padron.a_per,
                            'nro_grupo_per': getattr(padron, 'nro_grupo_perc', False),
                            'padron_activo': True,
                            'coeficiente': getattr(padron, 'coeficiente', False),
                        })]})

                # Santa Fe
                elif padron._name == 'santafe.padron':
                    if padron.type_alicuot == 'R':
                        activas = partner.alicuot_ret_santafe_ids.filtered('padron_activo')
                        if activas:
                            activas.write({'padron_activo': False})
                        partner.sudo().write({'alicuot_ret_santafe_ids': [(0, 0, {
                            'partner_id': partner.id,
                            'publication_date': padron.publication_date,
                            'effective_date_from': padron.effective_date_from,
                            'effective_date_to': padron.effective_date_to,
                            'type_contr_insc': padron.type_contr_insc,
                            'alta_baja': padron.alta_baja,
                            'cambio': padron.cambio,
                            'a_ret': padron.a_ret,
                            'nro_grupo_ret': getattr(padron, 'nro_grupo_ret', False),
                            'padron_activo': True,
                            'coeficiente': getattr(padron, 'coeficiente', False),
                        })]})

                    elif padron.type_alicuot == 'P':
                        activas = partner.alicuot_per_santafe_ids.filtered('padron_activo')
                        if activas:
                            activas.write({'padron_activo': False})
                        partner.sudo().write({'alicuot_per_santafe_ids': [(0, 0, {
                            'partner_id': partner.id,
                            'publication_date': padron.publication_date,
                            'effective_date_from': padron.effective_date_from,
                            'effective_date_to': padron.effective_date_to,
                            'type_contr_insc': padron.type_contr_insc,
                            'alta_baja': padron.alta_baja,
                            'cambio': padron.cambio,
                            'a_per': padron.a_per,
                            'nro_grupo_per': getattr(padron, 'nro_grupo_perc', False),
                            'padron_activo': True,
                            'coeficiente': getattr(padron, 'coeficiente', False),
                        })]})

        return True
