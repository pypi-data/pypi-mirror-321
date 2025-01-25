export const ids=["2999"];export const modules={46784:function(e,a,t){t.a(e,(async function(e,i){try{t.d(a,{u:function(){return u}});var l=t(69440),n=t(27486),s=e([l]);l=(s.then?(await s)():s)[0];const u=(e,a)=>{try{return o(a)?.of(e)??e}catch{return e}},o=(0,n.Z)((e=>new Intl.DisplayNames(e.language,{type:"language",fallback:"code"})));i()}catch(u){i(u)}}))},96980:function(e,a,t){t.a(e,(async function(e,a){try{var i=t(44249),l=t(72621),n=t(69440),s=t(57243),u=t(50778),o=t(27486),r=t(11297),d=t(81036),c=t(46784),h=t(32770),g=t(55534),v=(t(74064),t(58130),e([n,c]));[n,c]=v.then?(await v)():v;(0,i.Z)([(0,u.Mo)("ha-language-picker")],(function(e,a){class t extends a{constructor(...a){super(...a),e(this)}}return{F:t,d:[{kind:"field",decorators:[(0,u.Cb)()],key:"value",value:void 0},{kind:"field",decorators:[(0,u.Cb)()],key:"label",value:void 0},{kind:"field",decorators:[(0,u.Cb)({type:Array})],key:"languages",value:void 0},{kind:"field",decorators:[(0,u.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,u.Cb)({type:Boolean,reflect:!0})],key:"disabled",value(){return!1}},{kind:"field",decorators:[(0,u.Cb)({type:Boolean})],key:"required",value(){return!1}},{kind:"field",decorators:[(0,u.Cb)({attribute:"native-name",type:Boolean})],key:"nativeName",value(){return!1}},{kind:"field",decorators:[(0,u.Cb)({attribute:"no-sort",type:Boolean})],key:"noSort",value(){return!1}},{kind:"field",decorators:[(0,u.Cb)({attribute:"inline-arrow",type:Boolean})],key:"inlineArrow",value(){return!1}},{kind:"field",decorators:[(0,u.SB)()],key:"_defaultLanguages",value(){return[]}},{kind:"field",decorators:[(0,u.IO)("ha-select")],key:"_select",value:void 0},{kind:"method",key:"firstUpdated",value:function(e){(0,l.Z)(t,"firstUpdated",this,3)([e]),this._computeDefaultLanguageOptions()}},{kind:"method",key:"updated",value:function(e){(0,l.Z)(t,"updated",this,3)([e]);const a=e.has("hass")&&this.hass&&e.get("hass")&&e.get("hass").locale.language!==this.hass.locale.language;if(e.has("languages")||e.has("value")||a){if(this._select.layoutOptions(),this._select.value!==this.value&&(0,r.B)(this,"value-changed",{value:this._select.value}),!this.value)return;const e=this._getLanguagesOptions(this.languages??this._defaultLanguages,this.nativeName,this.hass?.locale).findIndex((e=>e.value===this.value));-1===e&&(this.value=void 0),a&&this._select.select(e)}}},{kind:"field",key:"_getLanguagesOptions",value(){return(0,o.Z)(((e,a,t)=>{let i=[];if(a){const a=g.o.translations;i=e.map((e=>{let t=a[e]?.nativeName;if(!t)try{t=new Intl.DisplayNames(e,{type:"language",fallback:"code"}).of(e)}catch(i){t=e}return{value:e,label:t}}))}else t&&(i=e.map((e=>({value:e,label:(0,c.u)(e,t)}))));return!this.noSort&&t&&i.sort(((e,a)=>(0,h.f)(e.label,a.label,t.language))),i}))}},{kind:"method",key:"_computeDefaultLanguageOptions",value:function(){this._defaultLanguages=Object.keys(g.o.translations)}},{kind:"method",key:"render",value:function(){const e=this._getLanguagesOptions(this.languages??this._defaultLanguages,this.nativeName,this.hass?.locale),a=this.value??(this.required?e[0]?.value:this.value);return s.dy`
      <ha-select
        .label=${this.label??(this.hass?.localize("ui.components.language-picker.language")||"Language")}
        .value=${a||""}
        .required=${this.required}
        .disabled=${this.disabled}
        @selected=${this._changed}
        @closed=${d.U}
        fixedMenuPosition
        naturalMenuWidth
        .inlineArrow=${this.inlineArrow}
      >
        ${0===e.length?s.dy`<ha-list-item value=""
              >${this.hass?.localize("ui.components.language-picker.no_languages")||"No languages"}</ha-list-item
            >`:e.map((e=>s.dy`
                <ha-list-item .value=${e.value}
                  >${e.label}</ha-list-item
                >
              `))}
      </ha-select>
    `}},{kind:"get",static:!0,key:"styles",value:function(){return s.iv`
      ha-select {
        width: 100%;
      }
    `}},{kind:"method",key:"_changed",value:function(e){const a=e.target;""!==a.value&&a.value!==this.value&&(this.value=a.value,(0,r.B)(this,"value-changed",{value:this.value}))}}]}}),s.oi);a()}catch(k){a(k)}}))},37270:function(e,a,t){t.a(e,(async function(e,i){try{t.r(a),t.d(a,{HaLanguageSelector:function(){return r}});var l=t(44249),n=t(57243),s=t(50778),u=t(96980),o=e([u]);u=(o.then?(await o)():o)[0];let r=(0,l.Z)([(0,s.Mo)("ha-selector-language")],(function(e,a){return{F:class extends a{constructor(...a){super(...a),e(this)}},d:[{kind:"field",decorators:[(0,s.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,s.Cb)({attribute:!1})],key:"selector",value:void 0},{kind:"field",decorators:[(0,s.Cb)()],key:"value",value:void 0},{kind:"field",decorators:[(0,s.Cb)()],key:"label",value:void 0},{kind:"field",decorators:[(0,s.Cb)()],key:"helper",value:void 0},{kind:"field",decorators:[(0,s.Cb)({type:Boolean})],key:"disabled",value(){return!1}},{kind:"field",decorators:[(0,s.Cb)({type:Boolean})],key:"required",value(){return!0}},{kind:"method",key:"render",value:function(){return n.dy`
      <ha-language-picker
        .hass=${this.hass}
        .value=${this.value}
        .label=${this.label}
        .helper=${this.helper}
        .languages=${this.selector.language?.languages}
        .nativeName=${Boolean(this.selector?.language?.native_name)}
        .noSort=${Boolean(this.selector?.language?.no_sort)}
        .disabled=${this.disabled}
        .required=${this.required}
      ></ha-language-picker>
    `}},{kind:"field",static:!0,key:"styles",value(){return n.iv`
    ha-language-picker {
      width: 100%;
    }
  `}}]}}),n.oi);i()}catch(r){i(r)}}))}};
//# sourceMappingURL=2999.78c9613961aeeff8.js.map