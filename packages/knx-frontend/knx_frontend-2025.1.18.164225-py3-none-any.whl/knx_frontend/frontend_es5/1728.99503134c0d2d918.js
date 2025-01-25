"use strict";(self.webpackChunkknx_frontend=self.webpackChunkknx_frontend||[]).push([["1728"],{19082:function(e,t,i){i.r(t),i.d(t,{HaTTSSelector:()=>C});var n=i("73577"),s=(i("71695"),i("47021"),i("57243")),a=i("50778"),d=i("72621"),l=(i("19083"),i("40251"),i("61006"),i("39527"),i("67670"),i("13334"),i("11297")),u=i("81036"),r=i("73525"),o=i("56587"),h=i("421"),c=(i("74064"),i("58130"),i("79575"));let v,g,k,f,p=e=>e;const y="__NONE_OPTION__";(0,n.Z)([(0,a.Mo)("ha-tts-picker")],(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"field",decorators:[(0,a.Cb)()],key:"value",value:void 0},{kind:"field",decorators:[(0,a.Cb)()],key:"label",value:void 0},{kind:"field",decorators:[(0,a.Cb)()],key:"language",value:void 0},{kind:"field",decorators:[(0,a.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,a.Cb)({type:Boolean,reflect:!0})],key:"disabled",value(){return!1}},{kind:"field",decorators:[(0,a.Cb)({type:Boolean})],key:"required",value(){return!1}},{kind:"field",decorators:[(0,a.SB)()],key:"_engines",value:void 0},{kind:"method",key:"render",value:function(){if(!this._engines)return s.Ld;let e=this.value;if(!e&&this.required){for(const t of Object.values(this.hass.entities))if("cloud"===t.platform&&"tts"===(0,c.M)(t.entity_id)){e=t.entity_id;break}if(!e)for(const i of this._engines){var t;if(0!==(null==i||null===(t=i.supported_languages)||void 0===t?void 0:t.length)){e=i.engine_id;break}}}return e||(e=y),(0,s.dy)(v||(v=p`
      <ha-select
        .label=${0}
        .value=${0}
        .required=${0}
        .disabled=${0}
        @selected=${0}
        @closed=${0}
        fixedMenuPosition
        naturalMenuWidth
      >
        ${0}
        ${0}
      </ha-select>
    `),this.label||this.hass.localize("ui.components.tts-picker.tts"),e,this.required,this.disabled,this._changed,u.U,this.required?s.Ld:(0,s.dy)(g||(g=p`<ha-list-item .value=${0}>
              ${0}
            </ha-list-item>`),y,this.hass.localize("ui.components.tts-picker.none")),this._engines.map((t=>{var i;if(t.deprecated&&t.engine_id!==e)return s.Ld;let n;if(t.engine_id.includes(".")){const e=this.hass.states[t.engine_id];n=e?(0,r.C)(e):t.engine_id}else n=t.name||t.engine_id;return(0,s.dy)(k||(k=p`<ha-list-item
            .value=${0}
            .disabled=${0}
          >
            ${0}
          </ha-list-item>`),t.engine_id,0===(null===(i=t.supported_languages)||void 0===i?void 0:i.length),n)})))}},{kind:"method",key:"willUpdate",value:function(e){(0,d.Z)(i,"willUpdate",this,3)([e]),this.hasUpdated?e.has("language")&&this._debouncedUpdateEngines():this._updateEngines()}},{kind:"field",key:"_debouncedUpdateEngines",value(){return(0,o.D)((()=>this._updateEngines()),500)}},{kind:"method",key:"_updateEngines",value:async function(){var e;if(this._engines=(await(0,h.Wg)(this.hass,this.language,this.hass.config.country||void 0)).providers,!this.value)return;const t=this._engines.find((e=>e.engine_id===this.value));(0,l.B)(this,"supported-languages-changed",{value:null==t?void 0:t.supported_languages}),t&&0!==(null===(e=t.supported_languages)||void 0===e?void 0:e.length)||(this.value=void 0,(0,l.B)(this,"value-changed",{value:this.value}))}},{kind:"get",static:!0,key:"styles",value:function(){return(0,s.iv)(f||(f=p`
      ha-select {
        width: 100%;
      }
    `))}},{kind:"method",key:"_changed",value:function(e){var t;const i=e.target;!this.hass||""===i.value||i.value===this.value||void 0===this.value&&i.value===y||(this.value=i.value===y?void 0:i.value,(0,l.B)(this,"value-changed",{value:this.value}),(0,l.B)(this,"supported-languages-changed",{value:null===(t=this._engines.find((e=>e.engine_id===this.value)))||void 0===t?void 0:t.supported_languages}))}}]}}),s.oi);let _,b,$=e=>e,C=(0,n.Z)([(0,a.Mo)("ha-selector-tts")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,a.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,a.Cb)({attribute:!1})],key:"selector",value:void 0},{kind:"field",decorators:[(0,a.Cb)()],key:"value",value:void 0},{kind:"field",decorators:[(0,a.Cb)()],key:"label",value:void 0},{kind:"field",decorators:[(0,a.Cb)()],key:"helper",value:void 0},{kind:"field",decorators:[(0,a.Cb)({type:Boolean})],key:"disabled",value(){return!1}},{kind:"field",decorators:[(0,a.Cb)({type:Boolean})],key:"required",value(){return!0}},{kind:"field",decorators:[(0,a.Cb)({attribute:!1})],key:"context",value:void 0},{kind:"method",key:"render",value:function(){var e,t;return(0,s.dy)(_||(_=$`<ha-tts-picker
      .hass=${0}
      .value=${0}
      .label=${0}
      .helper=${0}
      .language=${0}
      .disabled=${0}
      .required=${0}
    ></ha-tts-picker>`),this.hass,this.value,this.label,this.helper,(null===(e=this.selector.tts)||void 0===e?void 0:e.language)||(null===(t=this.context)||void 0===t?void 0:t.language),this.disabled,this.required)}},{kind:"field",static:!0,key:"styles",value(){return(0,s.iv)(b||(b=$`
    ha-tts-picker {
      width: 100%;
    }
  `))}}]}}),s.oi)},421:function(e,t,i){i.d(t,{MV:function(){return r},Wg:function(){return l},Xk:function(){return d},aT:function(){return n},b_:function(){return a},yP:function(){return u}});i(88044);const n=(e,t)=>e.callApi("POST","tts_get_url",t),s="media-source://tts/",a=e=>e.startsWith(s),d=e=>e.substring(19),l=(e,t,i)=>e.callWS({type:"tts/engine/list",language:t,country:i}),u=(e,t)=>e.callWS({type:"tts/engine/get",engine_id:t}),r=(e,t,i)=>e.callWS({type:"tts/engine/voices",engine_id:t,language:i})}}]);
//# sourceMappingURL=1728.99503134c0d2d918.js.map