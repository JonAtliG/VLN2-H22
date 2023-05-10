console.log("hello world")

const Cart = []

const addToCart = async (item) => {
    Cart.push(item);
    console.log()
    await updateAmount()
};

const updateAmount = async () => {
    if (!(document.getElementById("cart_amount"))) {
        const nav_cart = document.getElementById('nav_cart');
        let cartAmount = document.createElement("p");
        cartAmount.id = "cart_amount"
        cartAmount.textContent = Cart.length.toString()
        nav_cart.appendChild(cartAmount)
    } else {
        document.getElementById("cart_amount").textContent = Cart.length.toString();
    }
};
