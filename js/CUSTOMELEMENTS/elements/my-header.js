class MyHeader extends HTMLElement {
  constructor() {
    super();
    this.attachShadow({
      mode: 'open',
    });
    this.shadowRoot.innerHTML = `
      <style>
        :host {
          display: block;
        }
        span {
          font-size: 0.8em;
          opacity: 0.6;
        }
      </style>
      <span>Text inside ShadowDOM.  </span>
      <slot></slot>
    `;
  }
}
window.customElements.define('my-header', MyHeader);