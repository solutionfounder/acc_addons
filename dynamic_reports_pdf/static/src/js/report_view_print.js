odoo.define('dynamic_reports_pdf.dynamic_reports_pdf', function (require) {
    'use strict';

    var core = require('web.core');
    var _t = core._t;
    var DynamicReport = require('accounting_dynamic_reports.MyReportWidget');
    var DynamicReportHorizontal = require('accounting_dynamic_reports.MyReportHorizontal');

    var rpc = require('web.rpc');

    DynamicReport.include({
        events: _.extend({}, DynamicReport.prototype.events, {
            'click .button_print_xls_rep': 'print_report_excel',
            'click .button_print_rep': 'print_report',
        }),

        print_report: function (ev) {
            console.log(" vertical pdf report")
            var t_body = [], t_row, att_key, self = this;

            $('.vertical_report .categ .child_row').each(function () {
                t_row = {};
                $(this).find('td').each(function (td) {
                    att_key = $(this).attr('class').split(' ')[0];
                    if (att_key == 'child_col_bal') {
                        att_key += '_' + td;
                    }
                    else if (att_key == 'child_col_name') {
                        t_row['style'] = $(this).css('padding-left');
                    }
                    if (att_key != '') {
                        t_row[att_key] = $(this).text();
                    }
                });
                t_body.push(t_row);
            });

            var done = new $.Deferred();
            self.do_action({
                active_model: 'new.accounting.report',
                report_name: 'dynamic_reports_pdf.report_financial',
                type: 'ir.actions.report',
                report_type: 'qweb-pdf',
                data: {
                    data: t_body,
                    debit_credit: self.form.debit_credit,
                    report_type: 'vertical'
                }
            }).done(function () {
                done.resolve();
            });
            return done;
        },

        print_report_excel: function (ev) {
            ev.preventDefault();
            console.log("vertical excel report")
            var t_body = [], t_row, att_key, self = this;

            $('.vertical_report .categ .child_row').each(function () {
                t_row = {};
                $(this).find('td').each(function (td) {
                    att_key = $(this).attr('class').split(' ')[0];
                    if (att_key == 'child_col_bal') {
                        att_key += '_' + td;
                    }
                    else if (att_key == 'child_col_name') {
                        t_row['style'] = $(this).css('padding-left');
                    }
                    if (att_key != '') {
                        t_row[att_key] = $(this).text();
                    }
                });
                t_body.push(t_row);
                console.log("vertical 1 ")
            });

            var done = new $.Deferred();
            self.do_action({
                active_model: 'new.accounting.report',
                report_name: 'dynamic_reports_pdf.report_financial.xlsx',
                type: 'ir.actions.report',
                report_type: 'xlsx',
                data: {
                    data: t_body,
                    debit_credit: self.form.debit_credit,
                    report_type: 'vertical'
                }
            }).done(function () {
                done.resolve();
            });
            console.log("vertical 2")
            return done;
        }
    });

    DynamicReportHorizontal.include({
        events: _.extend({}, DynamicReportHorizontal.prototype.events, {
            'click .button_print_rep': 'print_report',
            'click .button_print_xls_rep': 'print_report_excel'
        }),

        print_report: function (ev) {
            console.log("horizontal pdf report")
            var t_body_left = [], t_body_right = [], t_row, att_key, self = this;

            $('.horizontal_report_left .categ .child_row').each(function () {
                t_row = {};
                $(this).find('td').each(function (td) {
                    att_key = $(this).attr('class').split(' ')[0];
                    if (att_key == 'child_col_bal') {
                        att_key += '_' + td;
                    }
                    else if (att_key == 'child_col_name') {
                        t_row['style'] = $(this).css('padding-left');
                    }
                    if (att_key != '') {
                        t_row[att_key] = $(this).text();
                    }
                });
                t_body_left.push(t_row);
            });

            $('.horizontal_report_right .categ .child_row').each(function () {
                t_row = {};
                $(this).find('td').each(function (td) {
                    att_key = $(this).attr('class').split(' ')[0];
                    if (att_key == 'child_col_bal') {
                        att_key += '_' + td;
                    }
                    else if (att_key == 'child_col_name') {
                        t_row['style'] = $(this).css('padding-left');
                    }
                    if (att_key != '') {
                        t_row[att_key] = $(this).text();
                    }
                });
                t_body_right.push(t_row);
            });

            console.log("----------left----------------..", t_body_left)
            console.log("----------right----------------..", t_body_right)

            var done = new $.Deferred();
            self.do_action({
                active_model: 'new.accounting.report',
                report_name: 'dynamic_reports_pdf.report_financial',
                type: 'ir.actions.report',
                report_type: 'qweb-pdf',
                data: {
                    t_body_left: t_body_left,
                    t_body_right: t_body_right,
                    report_type: 'horizontal',
                    debit_credit: self.form.debit_credit
                }
            }).done(function () {
                done.resolve();
            });
            return done;
        },

        print_report_excel: function (ev) {
            ev.stopPropagation();
            console.log("horizontal excel report")
            var t_body_left = [], t_body_right = [], t_row, att_key, self = this;

            $('.horizontal_report_left .categ .child_row').each(function () {
                t_row = {};
                $(this).find('td').each(function (td) {
                    att_key = $(this).attr('class').split(' ')[0];
                    if (att_key == 'child_col_bal') {
                        att_key += '_' + td;
                    }
                    else if (att_key == 'child_col_name') {
                        t_row['style'] = $(this).css('padding-left');
                    }
                    if (att_key != '') {
                        t_row[att_key] = $(this).text();
                    }
                });
                t_body_left.push(t_row);
            });

            $('.horizontal_report_right .categ .child_row').each(function () {
                t_row = {};
                $(this).find('td').each(function (td) {
                    att_key = $(this).attr('class').split(' ')[0];
                    if (att_key == 'child_col_bal') {
                        att_key += '_' + td;
                    }
                    else if (att_key == 'child_col_name') {
                        t_row['style'] = $(this).css('padding-left');
                    }
                    if (att_key != '') {
                        t_row[att_key] = $(this).text();
                    }
                });
                t_body_right.push(t_row);
            });

            console.log("----------left----------------..", t_body_left)
            console.log("----------right----------------..", t_body_right)

            var done = new $.Deferred();
            self.do_action({
                active_model: 'new.accounting.report',
                report_name: 'dynamic_reports_pdf.report_financial.xlsx',
                type: 'ir.actions.report',
                report_type: 'xlsx',
                data: {
                    t_body_left: t_body_left,
                    t_body_right: t_body_right,
                    report_type: 'horizontal',
                    debit_credit: self.form.debit_credit
                }
            }).done(function () {
                done.resolve();
            });
            return done;
        }
    });

});
