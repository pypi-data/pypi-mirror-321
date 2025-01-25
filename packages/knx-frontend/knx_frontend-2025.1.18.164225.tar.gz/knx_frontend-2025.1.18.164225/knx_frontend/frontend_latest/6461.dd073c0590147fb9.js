/*! For license information please see 6461.dd073c0590147fb9.js.LICENSE.txt */
export const ids=["6461"];export const modules={90918:function(e,t,o){o.r(t),o.d(t,{HaFormBoolean:()=>h});var a=o("44249"),i=o("9065"),d=o("50778"),r=o("4918"),n=o("6394");let l=class extends r.a{};l.styles=[n.W],l=(0,i.__decorate)([(0,d.Mo)("mwc-formfield")],l);var s=o("57243"),c=o("11297");o("76418");let h=(0,a.Z)([(0,d.Mo)("ha-form-boolean")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,d.Cb)({attribute:!1})],key:"schema",value:void 0},{kind:"field",decorators:[(0,d.Cb)({attribute:!1})],key:"data",value:void 0},{kind:"field",decorators:[(0,d.Cb)()],key:"label",value:void 0},{kind:"field",decorators:[(0,d.Cb)()],key:"helper",value:void 0},{kind:"field",decorators:[(0,d.Cb)({type:Boolean})],key:"disabled",value(){return!1}},{kind:"field",decorators:[(0,d.IO)("ha-checkbox",!0)],key:"_input",value:void 0},{kind:"method",key:"focus",value:function(){this._input&&this._input.focus()}},{kind:"method",key:"render",value:function(){return s.dy`
      <mwc-formfield .label=${this.label}>
        <ha-checkbox
          .checked=${this.data}
          .disabled=${this.disabled}
          @change=${this._valueChanged}
        ></ha-checkbox>
        <span slot="label">
          <p class="primary">${this.label}</p>
          ${this.helper?s.dy`<p class="secondary">${this.helper}</p>`:s.Ld}
        </span>
      </mwc-formfield>
    `}},{kind:"method",key:"_valueChanged",value:function(e){(0,c.B)(this,"value-changed",{value:e.target.checked})}},{kind:"get",static:!0,key:"styles",value:function(){return s.iv`
      ha-formfield {
        display: flex;
        min-height: 56px;
        align-items: center;
        --mdc-typography-body2-font-size: 1em;
      }
      p {
        margin: 0;
      }
      .secondary {
        direction: var(--direction);
        padding-top: 4px;
        box-sizing: border-box;
        color: var(--secondary-text-color);
        font-size: 0.875rem;
        font-weight: var(--mdc-typography-body2-font-weight, 400);
      }
    `}}]}}),s.oi)}};
//# sourceMappingURL=6461.dd073c0590147fb9.js.map