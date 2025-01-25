export const ids=["8714"];export const modules={46784:function(e,t,i){i.a(e,(async function(e,n){try{i.d(t,{u:function(){return l}});var a=i(69440),s=i(27486),r=e([a]);a=(r.then?(await r)():r)[0];const l=(e,t)=>{try{return d(t)?.of(e)??e}catch{return e}},d=(0,s.Z)((e=>new Intl.DisplayNames(e.language,{type:"language",fallback:"code"})));n()}catch(l){n(l)}}))},24022:function(e,t,i){i.a(e,(async function(e,t){try{var n=i(44249),a=i(72621),s=i(57243),r=i(50778),l=i(11297),d=i(81036),o=i(46784),u=i(4855),p=(i(74064),i(58130),e([o]));o=(p.then?(await p)():p)[0];const c="preferred",h="last_used";(0,n.Z)([(0,r.Mo)("ha-assist-pipeline-picker")],(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"field",decorators:[(0,r.Cb)()],key:"value",value:void 0},{kind:"field",decorators:[(0,r.Cb)()],key:"label",value:void 0},{kind:"field",decorators:[(0,r.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,r.Cb)({type:Boolean,reflect:!0})],key:"disabled",value(){return!1}},{kind:"field",decorators:[(0,r.Cb)({type:Boolean})],key:"required",value(){return!1}},{kind:"field",decorators:[(0,r.Cb)({attribute:!1})],key:"includeLastUsed",value(){return!1}},{kind:"field",decorators:[(0,r.SB)()],key:"_pipelines",value:void 0},{kind:"field",decorators:[(0,r.SB)()],key:"_preferredPipeline",value(){return null}},{kind:"get",key:"_default",value:function(){return this.includeLastUsed?h:c}},{kind:"method",key:"render",value:function(){if(!this._pipelines)return s.Ld;const e=this.value??this._default;return s.dy`
      <ha-select
        .label=${this.label||this.hass.localize("ui.components.pipeline-picker.pipeline")}
        .value=${e}
        .required=${this.required}
        .disabled=${this.disabled}
        @selected=${this._changed}
        @closed=${d.U}
        fixedMenuPosition
        naturalMenuWidth
      >
        ${this.includeLastUsed?s.dy`
              <ha-list-item .value=${h}>
                ${this.hass.localize("ui.components.pipeline-picker.last_used")}
              </ha-list-item>
            `:null}
        <ha-list-item .value=${c}>
          ${this.hass.localize("ui.components.pipeline-picker.preferred",{preferred:this._pipelines.find((e=>e.id===this._preferredPipeline))?.name})}
        </ha-list-item>
        ${this._pipelines.map((e=>s.dy`<ha-list-item .value=${e.id}>
              ${e.name}
              (${(0,o.u)(e.language,this.hass.locale)})
            </ha-list-item>`))}
      </ha-select>
    `}},{kind:"method",key:"firstUpdated",value:function(e){(0,a.Z)(i,"firstUpdated",this,3)([e]),(0,u.SC)(this.hass).then((e=>{this._pipelines=e.pipelines,this._preferredPipeline=e.preferred_pipeline}))}},{kind:"get",static:!0,key:"styles",value:function(){return s.iv`
      ha-select {
        width: 100%;
      }
    `}},{kind:"method",key:"_changed",value:function(e){const t=e.target;!this.hass||""===t.value||t.value===this.value||void 0===this.value&&t.value===this._default||(this.value=t.value===this._default?void 0:t.value,(0,l.B)(this,"value-changed",{value:this.value}))}}]}}),s.oi);t()}catch(c){t(c)}}))},93697:function(e,t,i){i.a(e,(async function(e,n){try{i.r(t),i.d(t,{HaAssistPipelineSelector:function(){return o}});var a=i(44249),s=i(57243),r=i(50778),l=i(24022),d=e([l]);l=(d.then?(await d)():d)[0];let o=(0,a.Z)([(0,r.Mo)("ha-selector-assist_pipeline")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,r.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,r.Cb)({attribute:!1})],key:"selector",value:void 0},{kind:"field",decorators:[(0,r.Cb)()],key:"value",value:void 0},{kind:"field",decorators:[(0,r.Cb)()],key:"label",value:void 0},{kind:"field",decorators:[(0,r.Cb)()],key:"helper",value:void 0},{kind:"field",decorators:[(0,r.Cb)({type:Boolean})],key:"disabled",value(){return!1}},{kind:"field",decorators:[(0,r.Cb)({type:Boolean})],key:"required",value(){return!0}},{kind:"method",key:"render",value:function(){return s.dy`
      <ha-assist-pipeline-picker
        .hass=${this.hass}
        .value=${this.value}
        .label=${this.label}
        .helper=${this.helper}
        .disabled=${this.disabled}
        .required=${this.required}
        .includeLastUsed=${Boolean(this.selector.assist_pipeline?.include_last_used)}
      ></ha-assist-pipeline-picker>
    `}},{kind:"field",static:!0,key:"styles",value(){return s.iv`
    ha-conversation-agent-picker {
      width: 100%;
    }
  `}}]}}),s.oi);n()}catch(o){n(o)}}))},4855:function(e,t,i){i.d(t,{Dy:function(){return o},PA:function(){return r},SC:function(){return s},Xp:function(){return a},af:function(){return d},eP:function(){return n},jZ:function(){return l}});const n=(e,t,i)=>"run-start"===t.type?e={init_options:i,stage:"ready",run:t.data,events:[t]}:e?((e="wake_word-start"===t.type?{...e,stage:"wake_word",wake_word:{...t.data,done:!1}}:"wake_word-end"===t.type?{...e,wake_word:{...e.wake_word,...t.data,done:!0}}:"stt-start"===t.type?{...e,stage:"stt",stt:{...t.data,done:!1}}:"stt-end"===t.type?{...e,stt:{...e.stt,...t.data,done:!0}}:"intent-start"===t.type?{...e,stage:"intent",intent:{...t.data,done:!1}}:"intent-end"===t.type?{...e,intent:{...e.intent,...t.data,done:!0}}:"tts-start"===t.type?{...e,stage:"tts",tts:{...t.data,done:!1}}:"tts-end"===t.type?{...e,tts:{...e.tts,...t.data,done:!0}}:"run-end"===t.type?{...e,stage:"done"}:"error"===t.type?{...e,stage:"error",error:t.data}:{...e}).events=[...e.events,t],e):void console.warn("Received unexpected event before receiving session",t),a=(e,t,i)=>e.connection.subscribeMessage(t,{...i,type:"assist_pipeline/run"}),s=e=>e.callWS({type:"assist_pipeline/pipeline/list"}),r=(e,t)=>e.callWS({type:"assist_pipeline/pipeline/get",pipeline_id:t}),l=(e,t)=>e.callWS({type:"assist_pipeline/pipeline/create",...t}),d=(e,t,i)=>e.callWS({type:"assist_pipeline/pipeline/update",pipeline_id:t,...i}),o=e=>e.callWS({type:"assist_pipeline/language/list"})}};
//# sourceMappingURL=8714.aa25ccfb7a910fe4.js.map