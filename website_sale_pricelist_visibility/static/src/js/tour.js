odoo.define('website_sale_pricelist_visibility.tour', function(require) {
    "use strict";

    var core = require('web.core');
    var tour = require('web_tour.tour');
    var base = require("web_editor.base");

    var _t = core._t;

    tour.register('advitus_Pricelist by Partner Category', {
        url: "/web",
    }, [{
        trigger: '.o_menu_apps > .dropdown > a',
        content: _t("Ready to try setting up <b>Pricelist by Partner Category</b>? Configuration can be found here, under the <b>Settings</b> menu."),
        position: 'bottom',
    }, {
        trigger: '.o_app[data-menu-xmlid="base.menu_administration"]',
        content: _t("Open the <b>Settings</b> menu."),
        position: 'right',
    }, {
        trigger: 'a[data-menu-xmlid="partner_category_hierarchy.menu_partner_category"]',
        content: _t("Click here to open <b>Partner Categories</b> configuration."),
        position: "bottom",
        pre_step_run: function(tip_trigger) {
            if ($(tip_trigger + ':visible:hasVisibility').size() == 0) {
                var trigger = $('a[data-menu-xmlid="partner_category_hierarchy.menu_partners"]:visible:hasVisibility');
                if (trigger.size() == 0) {
                    trigger = $('.o_extra_menu_items > a:visible:hasVisibility');
                }

                if (trigger.size() > 0 && trigger.next('.dropdown-menu.show').size() == 0) {
                    trigger.click();
                }

                return (trigger.size() > 0);
            }
        }
    }, {
        trigger: 'button.o_list_button_add',
        content: _t("Click here to <b>create new category</b>."),
        position: "bottom",
    }, {
        trigger: '.partner_category_hierarchy_name',
        content: _t("Enter <b>partner category name</b> (e.g. Basic)."),
        position: "top",
        run: function(actions) {
            actions.text("Basic", this.$anchor);
        },
    }, {
        trigger: '.o_field_many2many[name="partner_ids"] .o_field_x2many_list_row_add > a',
        content: _t("Add partner to this category."),
        position: "bottom"
    }, {
        trigger: '.modal-body td:contains("YourCompany, Joel Willis")',
        content: _t("Click here to add this partner."),
        position: "bottom"
    }, {
        trigger: '.o_notebook .nav-item a:contains("Pricelist Visibility")',
        content: _t("Click here to <b>open pricelist settings</b> for this partner category."),
        position: "bottom"
    }, {
        trigger: '.o_field_many2many[name="pricelist_ids"] .o_field_x2many_list_row_add > a',
        content: _t("Click here to <b>select allowed pricelists</b> for this partner category."),
        position: "bottom"
    }, {
        trigger: '.modal-body td:contains("Benelux")',
        content: _t("Click here to <b>add this pricelist</b>."),
        position: "bottom"
    }, {
        trigger: '.o_field_many2many[name="pricelist_ids"] .o_field_x2many_list_row_add > a',
        content: _t("Click here to <b>select another allowed pricelists</b> for this partner category."),
        position: "bottom"
    }, {
        trigger: '.modal-body td:contains("Public Pricelist")',
        content: _t("Click here to <b>add this pricelist</b>."),
        position: "bottom"
    }, {
        trigger: '.o_form_button_save',
        content: _t("Click here to <b>save new category</b>."),
        position: "bottom",
    }, {
        trigger: '.o_user_menu a[data-menu="logout"]',
        content: _t("Now we need to login with user we just configured pricelists for. Click here to open <b>logout</b>."),
        position: "bottom",
        pre_step_run: function(tip_trigger) {
            if ($(tip_trigger + ':visible:hasVisibility').size() == 0) {
                var trigger = $('.o_user_menu > a:visible:hasVisibility');

                if (trigger.size() > 0 && trigger.next('.dropdown-menu.show').size() == 0) {
                    trigger.click();
                }
            }
            return "website_sale_pricelist_visibility_frontend";
        }
    }]);

    tour.register('website_sale_pricelist_visibility_frontend', {
        url: "/web/login",
        wait_for: base.ready(),
    }, [{
        trigger: 'input#login',
        content: _t("Now lets login with the \"portal\" user."),
        position: "bottom",
        run: function(actions) {
            actions.text("portal", this.$anchor);
        }
    }, {
        trigger: 'input#password',
        content: _t("The password is \"portal\"."),
        position: "bottom",
        run: function(actions) {
            actions.text("portal", this.$anchor);
        }
    }, {
        trigger: 'button[type="submit"]',
        content: _t("Click here to <b>login</b>."),
        position: "bottom",
        pre_step_run: function() {
            return 'website_sale_pricelist_visibility_frontend2';
        }
    }]);

    tour.register('website_sale_pricelist_visibility_frontend2', {
        url: "/",
        wait_for: base.ready(),
    }, [{
        trigger: 'ul#top_menu a[role="menuitem"][href="/shop"]',
        content: _t("Click here to <b>open shop</b>."),
        position: "bottom",
        pre_step_run: function() {
            return 'website_sale_pricelist_visibility_frontend3';
        }
    }]);

    tour.register('website_sale_pricelist_visibility_frontend3', {
        url: "/shop",
        wait_for: base.ready(),
    }, [{
        trigger: '.products_pager.form-inline.justify-content-center .dropdown.ml-2',
        content: _t("Click here to see <b>available pricelists</b>."),
        position: "bottom"
    }]);

});