const tg = window.Telegram.WebApp;
tg.expand();

let cart = [];

function addToCart(name, price) {
    cart.push({ name, price });
    alert(name + " savatga qo‘shildi");
}

function sendOrder() {
    tg.sendData(JSON.stringify({
        action: "order",
        items: cart
    }));
}
