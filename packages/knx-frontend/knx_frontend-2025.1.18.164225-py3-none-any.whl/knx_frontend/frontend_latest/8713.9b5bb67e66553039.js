export const ids=["8713"];export const modules={78393:function(e,t,i){i.r(t),i.d(t,{HaTTSVoiceSelector:function(){return n}});var s=i(44249),a=i(57243),d=i(50778);i(27556);let n=(0,s.Z)([(0,d.Mo)("ha-selector-tts_voice")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,d.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,d.Cb)({attribute:!1})],key:"selector",value:void 0},{kind:"field",decorators:[(0,d.Cb)()],key:"value",value:void 0},{kind:"field",decorators:[(0,d.Cb)()],key:"label",value:void 0},{kind:"field",decorators:[(0,d.Cb)()],key:"helper",value:void 0},{kind:"field",decorators:[(0,d.Cb)({type:Boolean})],key:"disabled",value(){return!1}},{kind:"field",decorators:[(0,d.Cb)({type:Boolean})],key:"required",value(){return!0}},{kind:"field",decorators:[(0,d.Cb)({attribute:!1})],key:"context",value:void 0},{kind:"method",key:"render",value:function(){return a.dy`<ha-tts-voice-picker
      .hass=${this.hass}
      .value=${this.value}
      .label=${this.label}
      .helper=${this.helper}
      .language=${this.selector.tts_voice?.language||this.context?.language}
      .engineId=${this.selector.tts_voice?.engineId||this.context?.engineId}
      .disabled=${this.disabled}
      .required=${this.required}
    ></ha-tts-voice-picker>`}},{kind:"field",static:!0,key:"styles",value(){return a.iv`
    ha-tts-picker {
      width: 100%;
    }
  `}}]}}),a.oi)},27556:function(e,t,i){var s=i(44249),a=i(72621),d=i(57243),n=i(50778),l=i(11297),o=i(81036),u=i(56587),r=i(421);i(74064),i(58130);const c="__NONE_OPTION__";(0,s.Z)([(0,n.Mo)("ha-tts-voice-picker")],(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"field",decorators:[(0,n.Cb)()],key:"value",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"label",value:void 0},{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"engineId",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"language",value:void 0},{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Boolean,reflect:!0})],key:"disabled",value(){return!1}},{kind:"field",decorators:[(0,n.Cb)({type:Boolean})],key:"required",value(){return!1}},{kind:"field",decorators:[(0,n.SB)()],key:"_voices",value:void 0},{kind:"field",decorators:[(0,n.IO)("ha-select")],key:"_select",value:void 0},{kind:"method",key:"render",value:function(){if(!this._voices)return d.Ld;const e=this.value??(this.required?this._voices[0]?.voice_id:c);return d.dy`
      <ha-select
        .label=${this.label||this.hass.localize("ui.components.tts-voice-picker.voice")}
        .value=${e}
        .required=${this.required}
        .disabled=${this.disabled}
        @selected=${this._changed}
        @closed=${o.U}
        fixedMenuPosition
        naturalMenuWidth
      >
        ${this.required?d.Ld:d.dy`<ha-list-item .value=${c}>
              ${this.hass.localize("ui.components.tts-voice-picker.none")}
            </ha-list-item>`}
        ${this._voices.map((e=>d.dy`<ha-list-item .value=${e.voice_id}>
              ${e.name}
            </ha-list-item>`))}
      </ha-select>
    `}},{kind:"method",key:"willUpdate",value:function(e){(0,a.Z)(i,"willUpdate",this,3)([e]),this.hasUpdated?(e.has("language")||e.has("engineId"))&&this._debouncedUpdateVoices():this._updateVoices()}},{kind:"field",key:"_debouncedUpdateVoices",value(){return(0,u.D)((()=>this._updateVoices()),500)}},{kind:"method",key:"_updateVoices",value:async function(){this.engineId&&this.language?(this._voices=(await(0,r.MV)(this.hass,this.engineId,this.language)).voices,this.value&&(this._voices&&this._voices.find((e=>e.voice_id===this.value))||(this.value=void 0,(0,l.B)(this,"value-changed",{value:this.value})))):this._voices=void 0}},{kind:"method",key:"updated",value:function(e){(0,a.Z)(i,"updated",this,3)([e]),e.has("_voices")&&this._select?.value!==this.value&&(this._select?.layoutOptions(),(0,l.B)(this,"value-changed",{value:this._select?.value}))}},{kind:"get",static:!0,key:"styles",value:function(){return d.iv`
      ha-select {
        width: 100%;
      }
    `}},{kind:"method",key:"_changed",value:function(e){const t=e.target;!this.hass||""===t.value||t.value===this.value||void 0===this.value&&t.value===c||(this.value=t.value===c?void 0:t.value,(0,l.B)(this,"value-changed",{value:this.value}))}}]}}),d.oi)},421:function(e,t,i){i.d(t,{MV:function(){return u},Wg:function(){return l},Xk:function(){return n},aT:function(){return s},b_:function(){return d},yP:function(){return o}});const s=(e,t)=>e.callApi("POST","tts_get_url",t),a="media-source://tts/",d=e=>e.startsWith(a),n=e=>e.substring(19),l=(e,t,i)=>e.callWS({type:"tts/engine/list",language:t,country:i}),o=(e,t)=>e.callWS({type:"tts/engine/get",engine_id:t}),u=(e,t,i)=>e.callWS({type:"tts/engine/voices",engine_id:t,language:i})}};
//# sourceMappingURL=8713.9b5bb67e66553039.js.map