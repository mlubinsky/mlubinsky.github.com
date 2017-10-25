class MyFooter extends HTMLElement {
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
        ::slotted(*) {
          display: inline-block;
        }
        span {
          color: #f00;
          font-size: 0.8em;
        }
      </style>
      <slot></slot>
      <span> © 2018, Vasya Pupkin</span>
    `;
  }
}
window.customElements.define('my-footer', MyFooter);