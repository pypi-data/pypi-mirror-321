"use strict";(self.webpackChunkknx_frontend=self.webpackChunkknx_frontend||[]).push([["4608"],{68091:function(e,i,t){t.r(i),t.d(i,{HaFormFloat:function(){return u}});var a=t(73577),d=(t(68212),t(63721),t(71695),t(95078),t(19134),t(97499),t(97003),t(47021),t(57243)),l=t(50778),o=t(11297);t(70596);let r,n,s=e=>e,u=(0,a.Z)([(0,l.Mo)("ha-form-float")],(function(e,i){return{F:class extends i{constructor(...i){super(...i),e(this)}},d:[{kind:"field",decorators:[(0,l.Cb)({attribute:!1})],key:"localize",value:void 0},{kind:"field",decorators:[(0,l.Cb)({attribute:!1})],key:"schema",value:void 0},{kind:"field",decorators:[(0,l.Cb)({attribute:!1})],key:"data",value:void 0},{kind:"field",decorators:[(0,l.Cb)()],key:"label",value:void 0},{kind:"field",decorators:[(0,l.Cb)()],key:"helper",value:void 0},{kind:"field",decorators:[(0,l.Cb)({type:Boolean})],key:"disabled",value(){return!1}},{kind:"field",decorators:[(0,l.IO)("ha-textfield")],key:"_input",value:void 0},{kind:"method",key:"focus",value:function(){this._input&&this._input.focus()}},{kind:"method",key:"render",value:function(){var e,i;return(0,d.dy)(r||(r=s`
      <ha-textfield
        type="numeric"
        inputMode="decimal"
        .label=${0}
        .helper=${0}
        helperPersistent
        .value=${0}
        .disabled=${0}
        .required=${0}
        .autoValidate=${0}
        .suffix=${0}
        .validationMessage=${0}
        @input=${0}
      ></ha-textfield>
    `),this.label,this.helper,void 0!==this.data?this.data:"",this.disabled,this.schema.required,this.schema.required,null===(e=this.schema.description)||void 0===e?void 0:e.suffix,this.schema.required?null===(i=this.localize)||void 0===i?void 0:i.call(this,"ui.common.error_required"):void 0,this._valueChanged)}},{kind:"method",key:"updated",value:function(e){e.has("schema")&&this.toggleAttribute("own-margin",!!this.schema.required)}},{kind:"method",key:"_valueChanged",value:function(e){const i=e.target,t=i.value.replace(",",".");let a;if(!t.endsWith(".")&&"-"!==t)if(""!==t&&(a=parseFloat(t),isNaN(a)&&(a=void 0)),this.data!==a)(0,o.B)(this,"value-changed",{value:a});else{const e=void 0===a?"":String(a);i.value!==e&&(i.value=e)}}},{kind:"field",static:!0,key:"styles",value(){return(0,d.iv)(n||(n=s`
    :host([own-margin]) {
      margin-bottom: 5px;
    }
    ha-textfield {
      display: block;
    }
  `))}}]}}),d.oi)}}]);
//# sourceMappingURL=4608.bfb3efa51ecdc1bd.js.map