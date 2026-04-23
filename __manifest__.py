{
    'name': 'EXE Update Alicuotas States',
    'version': '16.0.1.0.0',
    'summary': 'Sincroniza alícuotas provinciales desde padróns a partners',
    'category': 'Accounting',
    'author': 'Mauro Bogado, Exemax',
    'depends': [
        'base',
        'contacts',
        'l10n_ar_withholding_sircar_tucuman',
        'l10n_ar_withholding_sircar_santafe',
    ],
    'data': [
        'views/partner_view.xml',
    ],
    'installable': True,
    'application': False,
}
