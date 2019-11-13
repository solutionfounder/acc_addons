# -*- coding: utf-8 -*-

from odoo import api, models, _
# from odoo.addons.report_xlsx.report.report_xlsx import ReportXlsx


class AccountReports(models.AbstractModel):
    _name = 'report.dynamic_reports_pdf.report_financial'


    @api.model
    def _get_report_values(self, docids, data=None):
        return {
            'doc_ids': [],
            'doc_model': 'report.dynamic_reports_pdf.report_financial',
            'datas': data,
            'docs': None
        }


class AccountReportsExcel(models.AbstractModel):
    _name = 'report.dynamic_reports_pdf.report_financial.xlsx'
    _inherit = 'report.report_xlsx.abstract'

    @api.model
    def _get_report_values(self, docids, data=None):
        return {
            'doc_ids': [],
            'doc_model': 'report.dynamic_reports_pdf.report_financial',
            'data': data,
            'docs': None
        }

    def generate_xlsx_report(self, workbook, data, obj):
        sheet = workbook.add_worksheet('Dynamic Report XLSX')
        header = workbook.add_format({'font_size': 12, 'align': 'center', 'bold': True})
        px=[]
        if data['report_type'] == 'vertical':

            for d in data['data']:
                if d['style'] not in px:
                    px.append(d['style'])
            px.sort()
            for d in px:
                sheet.set_column(1, px.index(d), 15)

            i = 1
            dat = data['data']
            level = len(px) - 1
            if data['debit_credit']:
                sheet.write(0, level + 2, 'Credit', header)
                sheet.write(0, level + 1, 'Debit', header)
            else:
                sheet.write(0, level + 1, 'Amount', header)
            for d in dat:
                k = 0
                if d['style'] in px:
                    k = px.index(d['style'])
                sheet.write(i, k, d['child_col_name'].strip())
                sheet.write(i, level+1, d['child_col_bal_1'].replace(' ', '').replace('\n', ''))
                sheet.write(i, (level+2) if data['debit_credit'] else (level + 1), d['child_col_bal_2'].replace(' ', '').replace('\n', ''))
                i += 1
        elif data['report_type'] == 'horizontal':
            left = data['t_body_left']
            right = data['t_body_right']
            i = 1
            level1 = 0
            if left:
                for d in left:
                    if d['style'] not in px:
                        px.append(d['style'])
                px.sort()
                level1 = len(px) - 1
                for d in px:
                    sheet.set_column(1, px.index(d), 15)

                if data['debit_credit']:
                    sheet.write(0, level1 + 2, 'Credit', header)
                    sheet.write(0, level1 + 1, 'Debit', header)
                else:
                    sheet.write(0, level1 + 1, 'Amount', header)
                for d in left:
                    k = 0
                    if d['style'] in px:
                        k = px.index(d['style'])
                    sheet.write(i, k, d['child_col_name'].strip().replace('\n', ''))
                    sheet.write(i, level1 + 1, d['child_col_bal_1'].replace(' ', '').replace('\n', ''))
                    sheet.write(i, (level1 + 2) if data['debit_credit'] else (level1 + 1), d['child_col_bal_2'])
                    i += 1
            i = 1
            w = level1 +(2 if data['debit_credit'] else 1)

            if right:
                level2 = 0
                for d in right:
                    if d['style'] not in px:
                        px.append(d['style'])
                px.sort()
                level2 = len(px) - 1
                for d in px:
                    sheet.set_column(1, px.index(d), 15)
                if data['debit_credit']:
                    sheet.write(0, w + level2 + 3, 'Credit', header)
                    sheet.write(0, w + level2 + 2, 'Debit', header)
                else:
                    sheet.write(0, w + level2 + 2, 'Amount', header)
                for d in right:
                    k = 1
                    if d['style'] in px:
                        k = px.index(d['style']) + 1
                    sheet.write(i, w + k , d['child_col_name'].strip().replace('\n', ''))
                    sheet.write(i, w + level2 + 2, d['child_col_bal_1'])
                    sheet.write(i, w + ((level2 + 3) if data['debit_credit'] else (level2 + 2)),
                                d['child_col_bal_2'])
                    i += 1
