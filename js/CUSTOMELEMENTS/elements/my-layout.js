class MyLayout extends HTMLElement {
  constructor() {
    // Сперва вызываем конструктор суперкласса HTMLElement:
    super();
    // Cоздаем ShadowDOM элемента - его локальную,
    // закрытую от внешнего мира область разметки, но доступную для JS:
    this.attachShadow({
      mode: 'open',
    });
    // присваеваем нашему элементу свой шаблон:
    this.shadowRoot.innerHTML = `
      <style>
        :host {
          display: block;
        }
        .header {
          position: fixed;
          top: 0;
          left: 0;
          right: 0;
          height: 40px;
          line-height: 40px;
          padding-left: 20px;
          padding-right: 20px;
          background-color: #000;
          color: #fff;
        }
        .menu {
          position: fixed;
          top: 0;
          bottom: 0;
          right: 0;
          width: 240px;
          padding: 20px;
          background-color: #eee;
          box-shadow: 0 0 8px rgba(0, 0, 0, 0.4);
          z-index: 1000;
        }
        .content {
          padding-top: 60px;
          padding-bottom: 60px;
        }
        .footer {
          position: fixed;
          left: 0;
          right: 0;
          bottom: 0;
          height: 40px;
          line-height: 40px;
          padding-left: 20px;
          padding-right: 20px;
          background-color: #eee;
          border-top: 2px solid #000;
        }
      </style>
      <div class="header"><slot name="header"></slot></div>
      <div class="content"><slot></slot></div>
      <div class="menu"><slot name="menu"></slot></div>
      <div class="footer"><slot name="footer"></slot></div>
    `;
  }
}
// Регистируем созданный элемент:
window.customElements.define('my-layout', MyLayout);
// Теперь браузер знает о существовании нового тега <my-layout>.