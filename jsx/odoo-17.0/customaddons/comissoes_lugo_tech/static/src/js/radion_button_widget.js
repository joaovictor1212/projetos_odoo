odoo.define('comissoes_lugo_tech.field_colorpicker', function (require) {
    "use strict";

    var FieldColorpicker = require('web.field_colorpicker');
    var RadioButton = require('web.radio_button');

    var FieldColorpickerRadioButton = RadioButton.extend({
        template: 'web.field_colorpicker_radiobutton',
        events: {
            'change input': function () {
                this._setValue(this.$('input').val());
            },
        },
        init: function () {
            this._super.apply(this, arguments);

            this.colorpicker = new FieldColorpicker(this, {
                mode: 'palette',
                palette: [
                    '#FF0000', // Vermelho
                    '#808080', // Cinza
                    '#008000', // Verde
                ],
            });

            this.colorpicker.appendTo(this.$('.oe_colorpicker'));
        },
        destroy: function () {
            this.colorpicker.destroy();

            this._super.apply(this, arguments);
        },
    });

    return FieldColorpickerRadioButton;
});
