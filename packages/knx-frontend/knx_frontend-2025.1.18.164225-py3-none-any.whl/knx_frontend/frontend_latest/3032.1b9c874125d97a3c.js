/*! For license information please see 3032.1b9c874125d97a3c.js.LICENSE.txt */
export const ids=["3032"];export const modules={37629:function(e,t,i){i.r(t),i.d(t,{HaBooleanSelector:function(){return s}});var c=i(44249),r=i(57243),o=i(50778),d=i(11297);i(52158),i(29939),i(20663);let s=(0,c.Z)([(0,o.Mo)("ha-selector-boolean")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,o.Cb)({type:Boolean})],key:"value",value(){return!1}},{kind:"field",decorators:[(0,o.Cb)()],key:"placeholder",value:void 0},{kind:"field",decorators:[(0,o.Cb)()],key:"label",value:void 0},{kind:"field",decorators:[(0,o.Cb)()],key:"helper",value:void 0},{kind:"field",decorators:[(0,o.Cb)({type:Boolean})],key:"disabled",value(){return!1}},{kind:"method",key:"render",value:function(){return r.dy`
      <ha-formfield alignEnd spaceBetween .label=${this.label}>
        <ha-switch
          .checked=${this.value??!0===this.placeholder}
          @change=${this._handleChange}
          .disabled=${this.disabled}
        ></ha-switch>
        <span slot="label">
          <p class="primary">${this.label}</p>
          ${this.helper?r.dy`<p class="secondary">${this.helper}</p>`:r.Ld}
        </span>
      </ha-formfield>
    `}},{kind:"method",key:"_handleChange",value:function(e){const t=e.target.checked;this.value!==t&&(0,d.B)(this,"value-changed",{value:t})}},{kind:"get",static:!0,key:"styles",value:function(){return r.iv`
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
    `}}]}}),r.oi)},29939:function(e,t,i){var c=i(44249),r=i(72621),o=i(62523),d=i(83835),s=i(57243),a=i(50778),n=i(26610);(0,c.Z)([(0,a.Mo)("ha-switch")],(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"field",decorators:[(0,a.Cb)({type:Boolean})],key:"haptic",value(){return!1}},{kind:"method",key:"firstUpdated",value:function(){(0,r.Z)(i,"firstUpdated",this,3)([]),this.addEventListener("change",(()=>{this.haptic&&(0,n.j)("light")}))}},{kind:"field",static:!0,key:"styles",value(){return[d.W,s.iv`
      :host {
        --mdc-theme-secondary: var(--switch-checked-color);
      }
      .mdc-switch.mdc-switch--checked .mdc-switch__thumb {
        background-color: var(--switch-checked-button-color);
        border-color: var(--switch-checked-button-color);
      }
      .mdc-switch.mdc-switch--checked .mdc-switch__track {
        background-color: var(--switch-checked-track-color);
        border-color: var(--switch-checked-track-color);
      }
      .mdc-switch:not(.mdc-switch--checked) .mdc-switch__thumb {
        background-color: var(--switch-unchecked-button-color);
        border-color: var(--switch-unchecked-button-color);
      }
      .mdc-switch:not(.mdc-switch--checked) .mdc-switch__track {
        background-color: var(--switch-unchecked-track-color);
        border-color: var(--switch-unchecked-track-color);
      }
    `]}}]}}),o.H)},26610:function(e,t,i){i.d(t,{j:function(){return r}});var c=i(11297);const r=e=>{(0,c.B)(window,"haptic",e)}},62523:function(e,t,i){i.d(t,{H:()=>b});var c=i("9065"),r=(i("16060"),i("4428")),o=i("11911"),d=i("78611"),s=i("91532"),a=i("80573"),n={CHECKED:"mdc-switch--checked",DISABLED:"mdc-switch--disabled"},l={ARIA_CHECKED_ATTR:"aria-checked",NATIVE_CONTROL_SELECTOR:".mdc-switch__native-control",RIPPLE_SURFACE_SELECTOR:".mdc-switch__thumb-underlay"};const h=function(e){function t(i){return e.call(this,(0,c.__assign)((0,c.__assign)({},t.defaultAdapter),i))||this}return(0,c.__extends)(t,e),Object.defineProperty(t,"strings",{get:function(){return l},enumerable:!1,configurable:!0}),Object.defineProperty(t,"cssClasses",{get:function(){return n},enumerable:!1,configurable:!0}),Object.defineProperty(t,"defaultAdapter",{get:function(){return{addClass:function(){},removeClass:function(){},setNativeControlChecked:function(){},setNativeControlDisabled:function(){},setNativeControlAttr:function(){}}},enumerable:!1,configurable:!0}),t.prototype.setChecked=function(e){this.adapter.setNativeControlChecked(e),this.updateAriaChecked(e),this.updateCheckedStyling(e)},t.prototype.setDisabled=function(e){this.adapter.setNativeControlDisabled(e),e?this.adapter.addClass(n.DISABLED):this.adapter.removeClass(n.DISABLED)},t.prototype.handleChange=function(e){var t=e.target;this.updateAriaChecked(t.checked),this.updateCheckedStyling(t.checked)},t.prototype.updateCheckedStyling=function(e){e?this.adapter.addClass(n.CHECKED):this.adapter.removeClass(n.CHECKED)},t.prototype.updateAriaChecked=function(e){this.adapter.setNativeControlAttr(l.ARIA_CHECKED_ATTR,""+!!e)},t}(a.K);var p=i("57243"),u=i("50778"),m=i("20552");class b extends o.H{constructor(){super(...arguments),this.checked=!1,this.disabled=!1,this.shouldRenderRipple=!1,this.mdcFoundationClass=h,this.rippleHandlers=new s.A((()=>(this.shouldRenderRipple=!0,this.ripple)))}changeHandler(e){this.mdcFoundation.handleChange(e),this.checked=this.formElement.checked}createAdapter(){return Object.assign(Object.assign({},(0,o.q)(this.mdcRoot)),{setNativeControlChecked:e=>{this.formElement.checked=e},setNativeControlDisabled:e=>{this.formElement.disabled=e},setNativeControlAttr:(e,t)=>{this.formElement.setAttribute(e,t)}})}renderRipple(){return this.shouldRenderRipple?p.dy`
        <mwc-ripple
          .accent="${this.checked}"
          .disabled="${this.disabled}"
          unbounded>
        </mwc-ripple>`:""}focus(){const e=this.formElement;e&&(this.rippleHandlers.startFocus(),e.focus())}blur(){const e=this.formElement;e&&(this.rippleHandlers.endFocus(),e.blur())}click(){this.formElement&&!this.disabled&&(this.formElement.focus(),this.formElement.click())}firstUpdated(){super.firstUpdated(),this.shadowRoot&&this.mdcRoot.addEventListener("change",(e=>{this.dispatchEvent(new Event("change",e))}))}render(){return p.dy`
      <div class="mdc-switch">
        <div class="mdc-switch__track"></div>
        <div class="mdc-switch__thumb-underlay">
          ${this.renderRipple()}
          <div class="mdc-switch__thumb">
            <input
              type="checkbox"
              id="basic-switch"
              class="mdc-switch__native-control"
              role="switch"
              aria-label="${(0,m.o)(this.ariaLabel)}"
              aria-labelledby="${(0,m.o)(this.ariaLabelledBy)}"
              @change="${this.changeHandler}"
              @focus="${this.handleRippleFocus}"
              @blur="${this.handleRippleBlur}"
              @mousedown="${this.handleRippleMouseDown}"
              @mouseenter="${this.handleRippleMouseEnter}"
              @mouseleave="${this.handleRippleMouseLeave}"
              @touchstart="${this.handleRippleTouchStart}"
              @touchend="${this.handleRippleDeactivate}"
              @touchcancel="${this.handleRippleDeactivate}">
          </div>
        </div>
      </div>`}handleRippleMouseDown(e){const t=()=>{window.removeEventListener("mouseup",t),this.handleRippleDeactivate()};window.addEventListener("mouseup",t),this.rippleHandlers.startPress(e)}handleRippleTouchStart(e){this.rippleHandlers.startPress(e)}handleRippleDeactivate(){this.rippleHandlers.endPress()}handleRippleMouseEnter(){this.rippleHandlers.startHover()}handleRippleMouseLeave(){this.rippleHandlers.endHover()}handleRippleFocus(){this.rippleHandlers.startFocus()}handleRippleBlur(){this.rippleHandlers.endFocus()}}(0,c.__decorate)([(0,u.Cb)({type:Boolean}),(0,d.P)((function(e){this.mdcFoundation.setChecked(e)}))],b.prototype,"checked",void 0),(0,c.__decorate)([(0,u.Cb)({type:Boolean}),(0,d.P)((function(e){this.mdcFoundation.setDisabled(e)}))],b.prototype,"disabled",void 0),(0,c.__decorate)([r.L,(0,u.Cb)({attribute:"aria-label"})],b.prototype,"ariaLabel",void 0),(0,c.__decorate)([r.L,(0,u.Cb)({attribute:"aria-labelledby"})],b.prototype,"ariaLabelledBy",void 0),(0,c.__decorate)([(0,u.IO)(".mdc-switch")],b.prototype,"mdcRoot",void 0),(0,c.__decorate)([(0,u.IO)("input")],b.prototype,"formElement",void 0),(0,c.__decorate)([(0,u.GC)("mwc-ripple")],b.prototype,"ripple",void 0),(0,c.__decorate)([(0,u.SB)()],b.prototype,"shouldRenderRipple",void 0),(0,c.__decorate)([(0,u.hO)({passive:!0})],b.prototype,"handleRippleMouseDown",null),(0,c.__decorate)([(0,u.hO)({passive:!0})],b.prototype,"handleRippleTouchStart",null)},83835:function(e,t,i){i.d(t,{W:function(){return c}});const c=i(57243).iv`.mdc-switch__thumb-underlay{left:-14px;right:initial;top:-17px;width:48px;height:48px}[dir=rtl] .mdc-switch__thumb-underlay,.mdc-switch__thumb-underlay[dir=rtl]{left:initial;right:-14px}.mdc-switch__native-control{width:64px;height:48px}.mdc-switch{display:inline-block;position:relative;outline:none;user-select:none}.mdc-switch.mdc-switch--checked .mdc-switch__track{background-color:#018786;background-color:var(--mdc-theme-secondary, #018786)}.mdc-switch.mdc-switch--checked .mdc-switch__thumb{background-color:#018786;background-color:var(--mdc-theme-secondary, #018786);border-color:#018786;border-color:var(--mdc-theme-secondary, #018786)}.mdc-switch:not(.mdc-switch--checked) .mdc-switch__track{background-color:#000;background-color:var(--mdc-theme-on-surface, #000)}.mdc-switch:not(.mdc-switch--checked) .mdc-switch__thumb{background-color:#fff;background-color:var(--mdc-theme-surface, #fff);border-color:#fff;border-color:var(--mdc-theme-surface, #fff)}.mdc-switch__native-control{left:0;right:initial;position:absolute;top:0;margin:0;opacity:0;cursor:pointer;pointer-events:auto;transition:transform 90ms cubic-bezier(0.4, 0, 0.2, 1)}[dir=rtl] .mdc-switch__native-control,.mdc-switch__native-control[dir=rtl]{left:initial;right:0}.mdc-switch__track{box-sizing:border-box;width:36px;height:14px;border:1px solid transparent;border-radius:7px;opacity:.38;transition:opacity 90ms cubic-bezier(0.4, 0, 0.2, 1),background-color 90ms cubic-bezier(0.4, 0, 0.2, 1),border-color 90ms cubic-bezier(0.4, 0, 0.2, 1)}.mdc-switch__thumb-underlay{display:flex;position:absolute;align-items:center;justify-content:center;transform:translateX(0);transition:transform 90ms cubic-bezier(0.4, 0, 0.2, 1),background-color 90ms cubic-bezier(0.4, 0, 0.2, 1),border-color 90ms cubic-bezier(0.4, 0, 0.2, 1)}.mdc-switch__thumb{box-shadow:0px 3px 1px -2px rgba(0, 0, 0, 0.2),0px 2px 2px 0px rgba(0, 0, 0, 0.14),0px 1px 5px 0px rgba(0,0,0,.12);box-sizing:border-box;width:20px;height:20px;border:10px solid;border-radius:50%;pointer-events:none;z-index:1}.mdc-switch--checked .mdc-switch__track{opacity:.54}.mdc-switch--checked .mdc-switch__thumb-underlay{transform:translateX(16px)}[dir=rtl] .mdc-switch--checked .mdc-switch__thumb-underlay,.mdc-switch--checked .mdc-switch__thumb-underlay[dir=rtl]{transform:translateX(-16px)}.mdc-switch--checked .mdc-switch__native-control{transform:translateX(-16px)}[dir=rtl] .mdc-switch--checked .mdc-switch__native-control,.mdc-switch--checked .mdc-switch__native-control[dir=rtl]{transform:translateX(16px)}.mdc-switch--disabled{opacity:.38;pointer-events:none}.mdc-switch--disabled .mdc-switch__thumb{border-width:1px}.mdc-switch--disabled .mdc-switch__native-control{cursor:default;pointer-events:none}:host{display:inline-flex;outline:none;-webkit-tap-highlight-color:transparent}`}};
//# sourceMappingURL=3032.1b9c874125d97a3c.js.map