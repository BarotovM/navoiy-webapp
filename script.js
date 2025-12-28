const tg = window.Telegram.WebApp;
tg.expand();

function sendData() {
    tg.sendData(JSON.stringify({
        status: "ok",
        message: "Test buyurtma yuborildi"
    }));
}
