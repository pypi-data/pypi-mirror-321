export const ids=["9456"];export const modules={93285:function(e,i,t){t.r(i),t.d(i,{HaFormInteger:function(){return l}});var a=t(44249),s=t(57243),d=t(50778),h=t(11297);t(97522),t(76418),t(20663),t(70596);let l=(0,a.Z)([(0,d.Mo)("ha-form-integer")],(function(e,i){return{F:class extends i{constructor(...i){super(...i),e(this)}},d:[{kind:"field",decorators:[(0,d.Cb)({attribute:!1})],key:"localize",value:void 0},{kind:"field",decorators:[(0,d.Cb)({attribute:!1})],key:"schema",value:void 0},{kind:"field",decorators:[(0,d.Cb)({attribute:!1})],key:"data",value:void 0},{kind:"field",decorators:[(0,d.Cb)()],key:"label",value:void 0},{kind:"field",decorators:[(0,d.Cb)()],key:"helper",value:void 0},{kind:"field",decorators:[(0,d.Cb)({type:Boolean})],key:"disabled",value(){return!1}},{kind:"field",decorators:[(0,d.IO)("ha-textfield ha-slider")],key:"_input",value:void 0},{kind:"field",key:"_lastValue",value:void 0},{kind:"method",key:"focus",value:function(){this._input&&this._input.focus()}},{kind:"method",key:"render",value:function(){return void 0!==this.schema.valueMin&&void 0!==this.schema.valueMax&&this.schema.valueMax-this.schema.valueMin<256?s.dy`
        <div>
          ${this.label}
          <div class="flex">
            ${this.schema.required?"":s.dy`
                  <ha-checkbox
                    @change=${this._handleCheckboxChange}
                    .checked=${void 0!==this.data}
                    .disabled=${this.disabled}
                  ></ha-checkbox>
                `}
            <ha-slider
              labeled
              .value=${this._value}
              .min=${this.schema.valueMin}
              .max=${this.schema.valueMax}
              .disabled=${this.disabled||void 0===this.data&&!this.schema.required}
              @change=${this._valueChanged}
            ></ha-slider>
          </div>
          ${this.helper?s.dy`<ha-input-helper-text>${this.helper}</ha-input-helper-text>`:""}
        </div>
      `:s.dy`
      <ha-textfield
        type="number"
        inputMode="numeric"
        .label=${this.label}
        .helper=${this.helper}
        helperPersistent
        .value=${void 0!==this.data?this.data:""}
        .disabled=${this.disabled}
        .required=${this.schema.required}
        .autoValidate=${this.schema.required}
        .suffix=${this.schema.description?.suffix}
        .validationMessage=${this.schema.required?this.localize?.("ui.common.error_required"):void 0}
        @input=${this._valueChanged}
      ></ha-textfield>
    `}},{kind:"method",key:"updated",value:function(e){e.has("schema")&&this.toggleAttribute("own-margin",!("valueMin"in this.schema&&"valueMax"in this.schema||!this.schema.required))}},{kind:"get",key:"_value",value:function(){return void 0!==this.data?this.data:this.schema.required?void 0!==this.schema.description?.suggested_value&&null!==this.schema.description?.suggested_value||this.schema.default||this.schema.valueMin||0:this.schema.valueMin||0}},{kind:"method",key:"_handleCheckboxChange",value:function(e){let i;if(e.target.checked){for(const t of[this._lastValue,this.schema.description?.suggested_value,this.schema.default,0])if(void 0!==t){i=t;break}}else this._lastValue=this.data;(0,h.B)(this,"value-changed",{value:i})}},{kind:"method",key:"_valueChanged",value:function(e){const i=e.target,t=i.value;let a;if(""!==t&&(a=parseInt(String(t))),this.data!==a)(0,h.B)(this,"value-changed",{value:a});else{const e=void 0===a?"":String(a);i.value!==e&&(i.value=e)}}},{kind:"get",static:!0,key:"styles",value:function(){return s.iv`
      :host([own-margin]) {
        margin-bottom: 5px;
      }
      .flex {
        display: flex;
      }
      ha-slider {
        flex: 1;
      }
      ha-textfield {
        display: block;
      }
    `}}]}}),s.oi)}};
//# sourceMappingURL=9456.5e7975787d84004f.js.map