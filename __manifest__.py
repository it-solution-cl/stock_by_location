# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    'name': ' Product Stocks By locations report in odoo',
    'version': '14.0.0.1',
    'category': 'Warehouse',
    'sequence': 14,
    'price': 15,
    'currency': "EUR",
    'summary': 'Apps for product stock by location product by location Stock Balance by Location report product stock location Stock quantity by location wise product stock location report warehouse stock by location stock inventory by location product by location report',
    'description': """
    warehouse Stock Balance by Location product stock location product inventory location product 
    warehouse Stock Quantity by location multiple location stock management inventory for products/variations per location
    Location based stock Product Stocks By Location report in odoo stock location report product inventory location report 
    Display Product Quantity based on stock inventory multiple location show multiple location
    stock balance by location stock location by product location of warehouse by product
    Warehouse stock based on location Stock Quantity based on location
    Stock by location Stock qty by location Stock locations
    odoo warehouse stock by location warehouse product stock by location
    odoo inventory by location inventory stock by location inventory product stock by location
    stock inventory by locations  stocks by locations 
    stocks by locations stocks inventory by locations locations of stocks inventory 
    reports Stocks By Location reports

    warehouse Stock Balance by Location report product stock location product inventory report location product report
    warehouse Stock Quantity by location reports multiple location stock management inventory reports for products variations per location reports
    Location based stock Product report Stocks By Location report in odoo stock location report product inventory location report 
    Display Product Quantity based on stock inventory multiple location show multiple location reports
    report stock balance by location stock location by product location of warehouse by product
    report Warehouse stock based on location Stock Quantity based on location reports
    Stock by location Stock qty by location Stock locations reports
    odoo warehouse stock by location report warehouse product stock by location reports
    odoo inventory by location report inventory stock by location report inventory product stock by location report
    reports stock inventory by locations report  stocks by locations reports
    report stocks by locations stocks inventory by locations locations of stocks inventory report
    Stock Balance por ubicaciónStock de cantidad por ubicación -Ubicación basada en la ubicación -Display Cantidad de producto en stock. - Stock de almacén basado en la ubicación - Cantidad de material basado en la ubicación -Stock por ubicación - Cantidad de material por ubicación - Ubicación de stock
    Stock Balance par Lieu -Stock Quantité par lieu - Stock basé sur l'emplacement -Afficher la quantité du produit en fonction du stock. - Stock d'entrepôt basé sur l'emplacement -Stock Quantité basée sur le lieu -Stock par emplacement -Stock quantité par emplacement -Stock emplacement
""",
    'author': 'BrowseInfo',
    'website': 'https://www.browseinfo.in',
    'depends': ['base','sale','sale_management','stock'],
    'data': [
        'views/product.xml',
        'security/ir.model.access.csv',
        'report/stock_by_location_report.xml',
        'report/stock_by_location_report_view.xml',
        'report/stock_by_location_temp_report.xml',
    ],
    'installable': True,
    'auto_install': False,
    'live_test_url' : 'https://www.youtube.com/watch?v=QfN8iSDmUyo&feature=youtu.be',
    "images":['static/description/Banner.png'],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
