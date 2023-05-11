let menuData = null;

window.onload = function () {
    let jsonElement = document.getElementById("jsonData");
    menuData = JSON.parse(jsonElement.getAttribute('data-json'))[0];
    updateMenu().catch()
}

function getPizzaDescriptionPrice (toppings) {
    const toppingList = [];
    for (let topping in toppings) {
        if (toppings[topping]) {
            toppingList.push(topping);
        }
    }
    let description = '';
    if (toppingList.length > 1) {
        description += toppingList[0];
        for (let i=1; i<toppingList.length-1; i++) {
            description += ', ' + toppingList[i].replace('_', ' ');
        }
        description += ' and '+ toppingList[toppingList.length-1].replace('_', ' ');
    }
    return {"desc": description, "price": (6.99+toppingList.length).toString()}
}

function getProductElement (productObject) {
    let product = document.createElement("li");
    product.classList.add("menuitem");
    let product_name = document.createElement("p");
    product_name.id = "menuName";
    product_name.textContent = productObject.name;
    let product_img = document.createElement("img");
    if (productObject.img === undefined) {
        product_img.src = '/static/img/pizza%20log.png';
    } else {
        product_img.src = productObject.img;
    }
    let productDescription = document.createElement("p")
    productDescription.id = "itemDescription"
    let cartButton = document.createElement("button")
    cartButton.id = "addToCart"
    let cartImg = document.createElement("img")
    cartImg.src = "/static/img/CartPhoto.png"
    //cartButton.onclick =
    let productPrice = document.createElement("p")
    productPrice.id = "price"
    //Pizzas have undefined description
    if (productObject.desc === undefined) {
        let descriptionAndPrice = getPizzaDescriptionPrice(productObject.toppings)
        productDescription.textContent = descriptionAndPrice.desc;
        productPrice.textContent = "$"+descriptionAndPrice.price
    } else {
        productDescription.textContent = productObject.desc;
        productPrice.textContent = "$"+productObject.price.toString()
    }
    cartButton.appendChild(cartImg);
    product.appendChild(product_name);
    product.appendChild(product_img);
    product.appendChild(productDescription);
    product.appendChild(cartButton);
    product.appendChild(productPrice);
    return product;
}

const updateMenu = async () => {
    const menuInfo = [
        {
            key: "pizzas",
            title: "Sewer Pizzas",
            containerClass: "pizza_list_container"
        },
        {
            key: "sides",
            title: "Sewer Sides",
            containerClass: "side_list_container",
        },
        {
            key: "drinks",
            title: "Drinks",
            containerClass: "drink_list_container",
        },
        {
            key: "user_pizzas",
            title: "Saved Pizzas",
            containerClass: "user_pizza_list_container",
        },
    ]
    let menuContainer = document.getElementById("menu_container");
    // Using the list to set the order of action
    menuInfo.forEach(menuType => {
        if (menuData[menuType.key].length > 0) {
            let menuTypeContainer = document.createElement("div");
            let titleContainer = document.createElement("div");
            let title = document.createElement("h1");
            let menuList = document.createElement("ul");
            menuTypeContainer.classList.add(menuType.containerClass)
            titleContainer.classList.add("title");
            title.textContent = menuType.title;
            menuList.classList.add("menu_list");
            menuData[menuType.key].forEach(product => {
                menuList.appendChild(getProductElement(product));
            })
            titleContainer.appendChild(title);
            menuTypeContainer.appendChild(titleContainer);
            menuTypeContainer.appendChild(menuList);
            menuContainer.appendChild(menuTypeContainer);
            }
    })
};

