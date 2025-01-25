"use strict";(self.webpackChunkknx_frontend=self.webpackChunkknx_frontend||[]).push([["6997"],{61239:function(e,t,r){r.d(t,{v:function(){return i}});r(19083);var n=r(36719),a=r(79575);function i(e,t){const r=(0,a.M)(e.entity_id),i=void 0!==t?t:null==e?void 0:e.state;if(["button","event","input_button","scene"].includes(r))return i!==n.nZ;if((0,n.rk)(i))return!1;if(i===n.PX&&"alert"!==r)return!1;switch(r){case"alarm_control_panel":return"disarmed"!==i;case"alert":return"idle"!==i;case"cover":case"valve":return"closed"!==i;case"device_tracker":case"person":return"not_home"!==i;case"lawn_mower":return["mowing","error"].includes(i);case"lock":return"locked"!==i;case"media_player":return"standby"!==i;case"vacuum":return!["idle","docked","paused"].includes(i);case"plant":return"problem"===i;case"group":return["on","home","open","locked","problem"].includes(i);case"timer":return"active"===i;case"camera":return"streaming"===i}return!0}},42877:function(e,t,r){var n=r(73577),a=r(72621),i=(r(71695),r(19423),r(40251),r(39527),r(41360),r(13334),r(47021),r(57243)),o=r(50778),s=r(38653),u=r(11297);r(17949),r(59414);let l,c,d,h,m,p,b,f,k,v=e=>e;const y={boolean:()=>r.e("6461").then(r.bind(r,90918)),constant:()=>r.e("4418").then(r.bind(r,92152)),float:()=>r.e("4608").then(r.bind(r,68091)),grid:()=>r.e("4351").then(r.bind(r,39090)),expandable:()=>r.e("9823").then(r.bind(r,78446)),integer:()=>r.e("9456").then(r.bind(r,93285)),multi_select:()=>Promise.all([r.e("7493"),r.e("5079"),r.e("1808")]).then(r.bind(r,87092)),positive_time_period_dict:()=>Promise.all([r.e("2047"),r.e("5235")]).then(r.bind(r,96636)),select:()=>r.e("1083").then(r.bind(r,6102)),string:()=>r.e("9752").then(r.bind(r,58701))},g=(e,t)=>e?!t.name||t.flatten?e:e[t.name]:null;(0,n.Z)([(0,o.Mo)("ha-form")],(function(e,t){class r extends t{constructor(...t){super(...t),e(this)}}return{F:r,d:[{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"data",value:void 0},{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"schema",value:void 0},{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"error",value:void 0},{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"warning",value:void 0},{kind:"field",decorators:[(0,o.Cb)({type:Boolean})],key:"disabled",value(){return!1}},{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"computeError",value:void 0},{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"computeWarning",value:void 0},{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"computeLabel",value:void 0},{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"computeHelper",value:void 0},{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"localizeValue",value:void 0},{kind:"method",key:"getFormProperties",value:function(){return{}}},{kind:"method",key:"focus",value:async function(){await this.updateComplete;const e=this.renderRoot.querySelector(".root");if(e)for(const t of e.children)if("HA-ALERT"!==t.tagName){t instanceof i.fl&&await t.updateComplete,t.focus();break}}},{kind:"method",key:"willUpdate",value:function(e){e.has("schema")&&this.schema&&this.schema.forEach((e=>{var t;"selector"in e||null===(t=y[e.type])||void 0===t||t.call(y)}))}},{kind:"method",key:"render",value:function(){return(0,i.dy)(l||(l=v`
      <div class="root" part="root">
        ${0}
        ${0}
      </div>
    `),this.error&&this.error.base?(0,i.dy)(c||(c=v`
              <ha-alert alert-type="error">
                ${0}
              </ha-alert>
            `),this._computeError(this.error.base,this.schema)):"",this.schema.map((e=>{var t;const r=((e,t)=>e&&t.name?e[t.name]:null)(this.error,e),n=((e,t)=>e&&t.name?e[t.name]:null)(this.warning,e);return(0,i.dy)(d||(d=v`
            ${0}
            ${0}
          `),r?(0,i.dy)(h||(h=v`
                  <ha-alert own-margin alert-type="error">
                    ${0}
                  </ha-alert>
                `),this._computeError(r,e)):n?(0,i.dy)(m||(m=v`
                    <ha-alert own-margin alert-type="warning">
                      ${0}
                    </ha-alert>
                  `),this._computeWarning(n,e)):"","selector"in e?(0,i.dy)(p||(p=v`<ha-selector
                  .schema=${0}
                  .hass=${0}
                  .name=${0}
                  .selector=${0}
                  .value=${0}
                  .label=${0}
                  .disabled=${0}
                  .placeholder=${0}
                  .helper=${0}
                  .localizeValue=${0}
                  .required=${0}
                  .context=${0}
                ></ha-selector>`),e,this.hass,e.name,e.selector,g(this.data,e),this._computeLabel(e,this.data),e.disabled||this.disabled||!1,e.required?"":e.default,this._computeHelper(e),this.localizeValue,e.required||!1,this._generateContext(e)):(0,s.h)(this.fieldElementName(e.type),Object.assign({schema:e,data:g(this.data,e),label:this._computeLabel(e,this.data),helper:this._computeHelper(e),disabled:this.disabled||e.disabled||!1,hass:this.hass,localize:null===(t=this.hass)||void 0===t?void 0:t.localize,computeLabel:this.computeLabel,computeHelper:this.computeHelper,localizeValue:this.localizeValue,context:this._generateContext(e)},this.getFormProperties())))})))}},{kind:"method",key:"fieldElementName",value:function(e){return`ha-form-${e}`}},{kind:"method",key:"_generateContext",value:function(e){if(!e.context)return;const t={};for(const[r,n]of Object.entries(e.context))t[r]=this.data[n];return t}},{kind:"method",key:"createRenderRoot",value:function(){const e=(0,a.Z)(r,"createRenderRoot",this,3)([]);return this.addValueChangedListener(e),e}},{kind:"method",key:"addValueChangedListener",value:function(e){e.addEventListener("value-changed",(e=>{e.stopPropagation();const t=e.target.schema;if(e.target===this)return;const r=!t.name||"flatten"in t&&t.flatten?e.detail.value:{[t.name]:e.detail.value};this.data=Object.assign(Object.assign({},this.data),r),(0,u.B)(this,"value-changed",{value:this.data})}))}},{kind:"method",key:"_computeLabel",value:function(e,t){return this.computeLabel?this.computeLabel(e,t):e?e.name:""}},{kind:"method",key:"_computeHelper",value:function(e){return this.computeHelper?this.computeHelper(e):""}},{kind:"method",key:"_computeError",value:function(e,t){return Array.isArray(e)?(0,i.dy)(b||(b=v`<ul>
        ${0}
      </ul>`),e.map((e=>(0,i.dy)(f||(f=v`<li>
              ${0}
            </li>`),this.computeError?this.computeError(e,t):e)))):this.computeError?this.computeError(e,t):e}},{kind:"method",key:"_computeWarning",value:function(e,t){return this.computeWarning?this.computeWarning(e,t):e}},{kind:"get",static:!0,key:"styles",value:function(){return(0,i.iv)(k||(k=v`
      .root > * {
        display: block;
      }
      .root > *:not([own-margin]):not(:last-child) {
        margin-bottom: 24px;
      }
      ha-alert[own-margin] {
        margin-bottom: 4px;
      }
    `))}}]}}),i.oi)},41946:function(e,t,r){r.d(t,{iI:function(){return a},oT:function(){return n}});r(19083),r(77439),r(19423),r(40251),r(97499),r(61006),r(13334);const n=e=>e.map((e=>{if("string"!==e.type)return e;switch(e.name){case"username":return Object.assign(Object.assign({},e),{},{autocomplete:"username",autofocus:!0});case"password":return Object.assign(Object.assign({},e),{},{autocomplete:"current-password"});case"code":return Object.assign(Object.assign({},e),{},{autocomplete:"one-time-code",autofocus:!0});default:return e}})),a=(e,t)=>e.callWS({type:"auth/sign_path",path:t})},36719:function(e,t,r){r.d(t,{ON:function(){return o},PX:function(){return s},V_:function(){return u},lz:function(){return i},nZ:function(){return a},rk:function(){return c}});var n=r(95907);const a="unavailable",i="unknown",o="on",s="off",u=[a,i],l=[a,i,s],c=(0,n.z)(u);(0,n.z)(l)}}]);
//# sourceMappingURL=6997.2627a1b51b792c09.js.map