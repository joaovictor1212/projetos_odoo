odoo.define('comissoes_lugo_tech.custom_radio_color', function (require) {
    "use strict";

    var FieldRadio = require('web.basic_fields').FieldRadio;

    FieldRadio.include({
        _render: function () {
            var self = this;
            this._super.apply(this, arguments);
            if (this.mode !== 'readonly') {
                this.$el.find('input').on('change', function () {
                    self.trigger_up('field_changed', {
                        dataPointID: self.recordData.id,
                        changes: {cor: $(this).val()}
                    });
                });
            }
        }
    });

});
