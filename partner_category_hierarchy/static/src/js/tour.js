odoo.define('partner_category_hierarchy.tour', function(require) {
    "use strict";

    var core = require('web.core');
    var tour = require('web_tour.tour');

    var _t = core._t;

    tour.register('advitus_Partners Hierarchy', {
        url: "/web",
    }, [{
        trigger: '.o_menu_apps > .dropdown > a',
        content: _t("Ready to try setting up <b>Partners Hierarchy</b>? Configuration can be found here, under the <b>Settings</b> menu."),
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
        trigger: '.o_form_button_save',
        content: _t("Click here to <b>save new category</b>."),
        position: "bottom",
    }, {
        trigger: 'a[data-menu-xmlid="partner_category_hierarchy.menu_action_res_partners"]',
        content: _t("Click here to open <b>Partners</b> list."),
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
        trigger: '.o_res_partner_kanban .o_kanban_record:nth-child(1)',
        content: _t("Click here to <b>open partner</b>."),
        position: "bottom",
    }, {
        trigger: '.o_form_button_edit',
        content: _t("Click here to <b>edit partner</b>."),
        position: "bottom",
    }, {
        trigger: '.partner_category_hierarchy_hcategory_id',
        content: _t("Select <b>partner category</b>."),
        position: "bottom",
    }, {
        trigger: '.partner_category_hierarchy_hcategory_id',
        extra_trigger: '.o_form_view.o_form_editable',
        content: _t("Select <b>partner category</b>."),
        position: "bottom",
        run: function(actions) {
            actions.text('', this.$anchor.find("input"));
            actions.text('Basic', this.$anchor.find("input"));
        },
    }, {
        trigger: ".ui-autocomplete > li > a",
        extra_trigger: ".ui-autocomplete > li:nth-child(1) > a:contains('Basic')",
        auto: true,
    }, {
        trigger: '.o_form_button_save',
        content: _t("Click here to <b>save partner</b>."),
        position: "bottom",
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
        content: _t("Click here to <b>create another category</b>."),
        position: "bottom",
    }, {
        trigger: '.partner_category_hierarchy_name',
        content: _t("Enter <b>partner category name</b> (e.g. VIP)."),
        position: "top",
        run: function(actions) {
            actions.text("VIP", this.$anchor);
        },
    }, {
        trigger: '.o_form_button_save',
        content: _t("Click here to <b>save new category</b>."),
        position: "bottom",
    }, {
        trigger: 'a[data-menu-xmlid="partner_category_hierarchy.menu_action_res_partners"]',
        content: _t("Click here to open <b>Partners</b> list."),
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
        trigger: '.o_res_partner_kanban .o_kanban_record:nth-child(2)',
        content: _t("Click here to <b>open another partner</b>."),
        position: "bottom",
    }, {
        trigger: '.o_form_button_edit',
        content: _t("Click here to <b>edit partner</b>."),
        position: "bottom",
    }, {
        trigger: '.partner_category_hierarchy_hcategory_id',
        content: _t("Select <b>partner category</b>."),
        position: "bottom",
    }, {
        trigger: '.partner_category_hierarchy_hcategory_id',
        extra_trigger: '.o_form_view.o_form_editable',
        content: _t("Select another <b>partner category</b>."),
        position: "bottom",
        run: function(actions) {
            actions.text('', this.$anchor.find("input"));
            actions.text('VIP', this.$anchor.find("input"));
        },
    }, {
        trigger: ".ui-autocomplete > li > a",
        extra_trigger: ".ui-autocomplete > li:nth-child(1) > a:contains('VIP')",
        auto: true,
    }, {
        trigger: '.o_form_button_save',
        content: _t("Click here to <b>save partner</b>."),
        position: "bottom",
    }, {
        trigger: 'a[data-menu-xmlid="partner_category_hierarchy.menu_action_res_partners"]',
        content: _t("Click here to open <b>Partners</b> list."),
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
        trigger: '.o_search_options button:contains(' + _t('Group By') + ')',
        content: _t("Click here to <b>open grouping options</b>."),
        position: "bottom",
    }, {
        trigger: '.o_search_options button:contains(' + _t('Group By') + ') + .dropdown-menu .dropdown-item:contains(' + _t('Category') + ')',
        content: _t("Click here to <b>group by partner category</b>."),
        position: "bottom",
    }]);

});