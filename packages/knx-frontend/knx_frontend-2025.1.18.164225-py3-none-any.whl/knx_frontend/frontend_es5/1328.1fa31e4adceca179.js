"use strict";(self.webpackChunkknx_frontend=self.webpackChunkknx_frontend||[]).push([["1328"],{62304:function(e,a,i){var s=i(73577),t=(i(71695),i(47021),i(57243)),l=i(50778),o=i(11297);i(26375);let r,n=e=>e;(0,s.Z)([(0,l.Mo)("ha-aliases-editor")],(function(e,a){return{F:class extends a{constructor(...a){super(...a),e(this)}},d:[{kind:"field",decorators:[(0,l.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,l.Cb)({type:Array})],key:"aliases",value:void 0},{kind:"field",decorators:[(0,l.Cb)({type:Boolean})],key:"disabled",value(){return!1}},{kind:"method",key:"render",value:function(){return this.aliases?(0,t.dy)(r||(r=n`
      <ha-multi-textfield
        .hass=${0}
        .value=${0}
        .disabled=${0}
        .label=${0}
        .removeLabel=${0}
        .addLabel=${0}
        item-index
        @value-changed=${0}
      >
      </ha-multi-textfield>
    `),this.hass,this.aliases,this.disabled,this.hass.localize("ui.dialogs.aliases.label"),this.hass.localize("ui.dialogs.aliases.remove"),this.hass.localize("ui.dialogs.aliases.add"),this._aliasesChanged):t.Ld}},{kind:"method",key:"_aliasesChanged",value:function(e){(0,o.B)(this,"value-changed",{value:e})}}]}}),t.oi)},40600:function(e,a,i){i.a(e,(async function(e,s){try{i.r(a);var t=i(73577),l=(i(71695),i(40251),i(81804),i(47021),i(31622),i(2060),i(57243)),o=i(50778),r=i(11297),n=(i(17949),i(62304),i(44118)),d=i(10581),h=(i(18805),i(37643)),c=(i(70596),i(35760)),u=i(66193),_=e([d,h,c]);[d,h,c]=_.then?(await _)():_;let p,v,m,k,f=e=>e;const g={round:!1,type:"image/jpeg",quality:.75,aspectRatio:1.78};let y=(0,t.Z)(null,(function(e,a){return{F:class extends a{constructor(...a){super(...a),e(this)}},d:[{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_name",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_aliases",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_labels",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_picture",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_icon",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_floor",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_error",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_params",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_submitting",value:void 0},{kind:"method",key:"showDialog",value:async function(e){var a,i,s;this._params=e,this._error=void 0,this._name=this._params.entry?this._params.entry.name:this._params.suggestedName||"",this._aliases=this._params.entry?this._params.entry.aliases:[],this._labels=this._params.entry?this._params.entry.labels:[],this._picture=(null===(a=this._params.entry)||void 0===a?void 0:a.picture)||null,this._icon=(null===(i=this._params.entry)||void 0===i?void 0:i.icon)||null,this._floor=(null===(s=this._params.entry)||void 0===s?void 0:s.floor_id)||null,await this.updateComplete}},{kind:"method",key:"closeDialog",value:function(){this._error="",this._params=void 0,(0,r.B)(this,"dialog-closed",{dialog:this.localName})}},{kind:"method",key:"render",value:function(){if(!this._params)return l.Ld;const e=this._params.entry,a=!this._isNameValid();return(0,l.dy)(p||(p=f`
      <ha-dialog
        open
        @closed=${0}
        .heading=${0}
      >
        <div>
          ${0}
          <div class="form">
            ${0}

            <ha-textfield
              .value=${0}
              @input=${0}
              .label=${0}
              .validationMessage=${0}
              required
              dialogInitialFocus
            ></ha-textfield>

            <ha-icon-picker
              .hass=${0}
              .value=${0}
              @value-changed=${0}
              .label=${0}
            ></ha-icon-picker>

            <ha-floor-picker
              .hass=${0}
              .value=${0}
              @value-changed=${0}
              .label=${0}
            ></ha-floor-picker>

            <ha-labels-picker
              .hass=${0}
              .value=${0}
              @value-changed=${0}
            ></ha-labels-picker>

            <ha-picture-upload
              .hass=${0}
              .value=${0}
              crop
              select-media
              .cropOptions=${0}
              @change=${0}
            ></ha-picture-upload>

            <h3 class="header">
              ${0}
            </h3>

            <p class="description">
              ${0}
            </p>
            <ha-aliases-editor
              .hass=${0}
              .aliases=${0}
              @value-changed=${0}
            ></ha-aliases-editor>
          </div>
        </div>
        <mwc-button slot="secondaryAction" @click=${0}>
          ${0}
        </mwc-button>
        <mwc-button
          slot="primaryAction"
          @click=${0}
          .disabled=${0}
        >
          ${0}
        </mwc-button>
      </ha-dialog>
    `),this.closeDialog,(0,n.i)(this.hass,e?this.hass.localize("ui.panel.config.areas.editor.update_area"):this.hass.localize("ui.panel.config.areas.editor.create_area")),this._error?(0,l.dy)(v||(v=f`<ha-alert alert-type="error">${0}</ha-alert>`),this._error):"",e?(0,l.dy)(m||(m=f`
                  <ha-settings-row>
                    <span slot="heading">
                      ${0}
                    </span>
                    <span slot="description"> ${0} </span>
                  </ha-settings-row>
                `),this.hass.localize("ui.panel.config.areas.editor.area_id"),e.area_id):l.Ld,this._name,this._nameChanged,this.hass.localize("ui.panel.config.areas.editor.name"),this.hass.localize("ui.panel.config.areas.editor.name_required"),this.hass,this._icon,this._iconChanged,this.hass.localize("ui.panel.config.areas.editor.icon"),this.hass,this._floor,this._floorChanged,this.hass.localize("ui.panel.config.areas.editor.floor"),this.hass,this._labels,this._labelsChanged,this.hass,this._picture,g,this._pictureChanged,this.hass.localize("ui.panel.config.areas.editor.aliases_section"),this.hass.localize("ui.panel.config.areas.editor.aliases_description"),this.hass,this._aliases,this._aliasesChanged,this.closeDialog,this.hass.localize("ui.common.cancel"),this._updateEntry,a||this._submitting,e?this.hass.localize("ui.common.save"):this.hass.localize("ui.common.create"))}},{kind:"method",key:"_isNameValid",value:function(){return""!==this._name.trim()}},{kind:"method",key:"_nameChanged",value:function(e){this._error=void 0,this._name=e.target.value}},{kind:"method",key:"_floorChanged",value:function(e){this._error=void 0,this._floor=e.detail.value}},{kind:"method",key:"_iconChanged",value:function(e){this._error=void 0,this._icon=e.detail.value}},{kind:"method",key:"_labelsChanged",value:function(e){this._error=void 0,this._labels=e.detail.value}},{kind:"method",key:"_pictureChanged",value:function(e){this._error=void 0,this._picture=e.target.value}},{kind:"method",key:"_updateEntry",value:async function(){const e=!this._params.entry;this._submitting=!0;try{const a={name:this._name.trim(),picture:this._picture||(e?void 0:null),icon:this._icon||(e?void 0:null),floor_id:this._floor||(e?void 0:null),labels:this._labels||null,aliases:this._aliases};e?await this._params.createEntry(a):await this._params.updateEntry(a),this.closeDialog()}catch(a){this._error=a.message||this.hass.localize("ui.panel.config.areas.editor.unknown_error")}finally{this._submitting=!1}}},{kind:"method",key:"_aliasesChanged",value:function(e){this._aliases=e.detail.value}},{kind:"get",static:!0,key:"styles",value:function(){return[u.yu,(0,l.iv)(k||(k=f`
        ha-textfield,
        ha-icon-picker,
        ha-floor-picker,
        ha-labels-picker,
        ha-picture-upload {
          display: block;
          margin-bottom: 16px;
        }
      `))]}}]}}),l.oi);customElements.define("dialog-area-registry-detail",y),s()}catch(p){s(p)}}))}}]);
//# sourceMappingURL=1328.1fa31e4adceca179.js.map