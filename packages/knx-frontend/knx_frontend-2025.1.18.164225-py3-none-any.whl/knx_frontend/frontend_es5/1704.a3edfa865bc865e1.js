"use strict";(self.webpackChunkknx_frontend=self.webpackChunkknx_frontend||[]).push([["1704"],{71942:function(e,o,a){a.a(e,(async function(e,o){try{var t=a(73577),i=(a(71695),a(61893),a(40251),a(39527),a(99790),a(47021),a(57243)),s=a(50778),n=a(49672),d=a(11297),r=a(32770),l=a(46999),u=(a(17949),a(69484)),c=(a(74064),e([u]));u=(c.then?(await c)():c)[0];let h,v,k,p,y=e=>e;const f=e=>(0,i.dy)(h||(h=y`<ha-list-item twoline graphic="icon">
    <span>${0}</span>
    <span slot="secondary">${0}</span>
    ${0}
  </ha-list-item>`),e.name,e.slug,e.icon?(0,i.dy)(v||(v=y`<img
          alt=""
          slot="graphic"
          .src="/api/hassio/addons/${0}/icon"
        />`),e.slug):"");(0,t.Z)([(0,s.Mo)("ha-addon-picker")],(function(e,o){return{F:class extends o{constructor(...o){super(...o),e(this)}},d:[{kind:"field",key:"hass",value:void 0},{kind:"field",decorators:[(0,s.Cb)()],key:"label",value:void 0},{kind:"field",decorators:[(0,s.Cb)()],key:"value",value(){return""}},{kind:"field",decorators:[(0,s.Cb)()],key:"helper",value:void 0},{kind:"field",decorators:[(0,s.SB)()],key:"_addons",value:void 0},{kind:"field",decorators:[(0,s.Cb)({type:Boolean})],key:"disabled",value(){return!1}},{kind:"field",decorators:[(0,s.Cb)({type:Boolean})],key:"required",value(){return!1}},{kind:"field",decorators:[(0,s.IO)("ha-combo-box")],key:"_comboBox",value:void 0},{kind:"field",decorators:[(0,s.SB)()],key:"_error",value:void 0},{kind:"method",key:"open",value:function(){var e;null===(e=this._comboBox)||void 0===e||e.open()}},{kind:"method",key:"focus",value:function(){var e;null===(e=this._comboBox)||void 0===e||e.focus()}},{kind:"method",key:"firstUpdated",value:function(){this._getAddons()}},{kind:"method",key:"render",value:function(){return this._error?(0,i.dy)(k||(k=y`<ha-alert alert-type="error">${0}</ha-alert>`),this._error):this._addons?(0,i.dy)(p||(p=y`
      <ha-combo-box
        .hass=${0}
        .label=${0}
        .value=${0}
        .required=${0}
        .disabled=${0}
        .helper=${0}
        .renderer=${0}
        .items=${0}
        item-value-path="slug"
        item-id-path="slug"
        item-label-path="name"
        @value-changed=${0}
      ></ha-combo-box>
    `),this.hass,void 0===this.label&&this.hass?this.hass.localize("ui.components.addon-picker.addon"):this.label,this._value,this.required,this.disabled,this.helper,f,this._addons,this._addonChanged):i.Ld}},{kind:"method",key:"_getAddons",value:async function(){try{if((0,n.p)(this.hass,"hassio")){const e=await(0,l.yt)(this.hass);this._addons=e.addons.filter((e=>e.version)).sort(((e,o)=>(0,r.$)(e.name,o.name,this.hass.locale.language)))}else this._error=this.hass.localize("ui.components.addon-picker.error.no_supervisor")}catch(e){this._error=this.hass.localize("ui.components.addon-picker.error.fetch_addons")}}},{kind:"get",key:"_value",value:function(){return this.value||""}},{kind:"method",key:"_addonChanged",value:function(e){e.stopPropagation();const o=e.detail.value;o!==this._value&&this._setValue(o)}},{kind:"method",key:"_setValue",value:function(e){this.value=e,setTimeout((()=>{(0,d.B)(this,"value-changed",{value:e}),(0,d.B)(this,"change")}),0)}}]}}),i.oi);o()}catch(h){o(h)}}))},4608:function(e,o,a){a.a(e,(async function(e,t){try{a.r(o),a.d(o,{HaAddonSelector:function(){return h}});var i=a(73577),s=(a(71695),a(47021),a(57243)),n=a(50778),d=a(71942),r=e([d]);d=(r.then?(await r)():r)[0];let l,u,c=e=>e,h=(0,i.Z)([(0,n.Mo)("ha-selector-addon")],(function(e,o){return{F:class extends o{constructor(...o){super(...o),e(this)}},d:[{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"selector",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"value",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"label",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"helper",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Boolean})],key:"disabled",value(){return!1}},{kind:"field",decorators:[(0,n.Cb)({type:Boolean})],key:"required",value(){return!0}},{kind:"method",key:"render",value:function(){return(0,s.dy)(l||(l=c`<ha-addon-picker
      .hass=${0}
      .value=${0}
      .label=${0}
      .helper=${0}
      .disabled=${0}
      .required=${0}
      allow-custom-entity
    ></ha-addon-picker>`),this.hass,this.value,this.label,this.helper,this.disabled,this.required)}},{kind:"field",static:!0,key:"styles",value(){return(0,s.iv)(u||(u=c`
    ha-addon-picker {
      width: 100%;
    }
  `))}}]}}),s.oi);t()}catch(l){t(l)}}))},46999:function(e,o,a){a.d(o,{yt:()=>s,fU:()=>d,kP:()=>n});a("52247"),a("40251"),a("39527"),a("67670");var t=a("99642"),i=a("81054");const s=async e=>(0,t.I)(e.config.version,2021,2,4)?e.callWS({type:"supervisor/api",endpoint:"/addons",method:"get"}):(0,i.rY)(await e.callApi("GET","hassio/addons")),n=async(e,o)=>(0,t.I)(e.config.version,2021,2,4)?e.callWS({type:"supervisor/api",endpoint:`/addons/${o}/start`,method:"post",timeout:null}):e.callApi("POST",`hassio/addons/${o}/start`),d=async(e,o)=>{(0,t.I)(e.config.version,2021,2,4)?await e.callWS({type:"supervisor/api",endpoint:`/addons/${o}/install`,method:"post",timeout:null}):await e.callApi("POST",`hassio/addons/${o}/install`)}},81054:function(e,o,a){a.d(o,{js:function(){return i},rY:function(){return t}});a(19083),a(71695),a(40251),a(92519),a(42179),a(89256),a(24931),a(88463),a(57449),a(19814),a(61006),a(47021),a(99642);const t=e=>e.data,i=e=>"object"==typeof e?"object"==typeof e.body?e.body.message||"Unknown error, see supervisor logs":e.body||e.message||"Unknown error, see supervisor logs":e;new Set([502,503,504])}}]);
//# sourceMappingURL=1704.a3edfa865bc865e1.js.map