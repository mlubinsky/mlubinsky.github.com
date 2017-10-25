class MyMenu extends HTMLElement {
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
        a {
          display: flex;
          align-items: center;
          justify-content: center;
          background-color: #fff;
          cursor: pointer;
          height: 40px;
          text-decoration: none;
          color: currentColor;
          font-size: 1.2em;
          margin-bottom: 4px;
          border: 1px solid #fff;
        }
        a:hover {
          border: 1px solid currentColor;
        }
      </style>
      <a href="pages/page1.html">Page 1</a>
      <a href="pages/page2.html">Page 2</a>
      <a href="pages/page3.html">Page 3</a>
    `;
  }
}
window.customElements.define('my-menu', MyMenu);