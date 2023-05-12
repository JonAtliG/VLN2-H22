let menuData = null;
let activeMap = {"pizzas": true, "sides": true, "drinks": true, "user_pizzas": true};
let offer_3_for_2 = [null, null, null];

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

function getProductElement (productObject, carturl) {
    let product = document.createElement("li");
    product.classList.add("menuitem");
    let product_name = document.createElement("p");
    product_name.id = "menuName";
    product_name.textContent = productObject.name;
    let product_img = document.createElement("img");
    if (productObject.img.length<1) {
        product_img.src = 'static/img/pizza logo.png';
    } else {
        product_img.src = productObject.img;
    }
    let productDescription = document.createElement("p")
    productDescription.id = "itemDescription"

    let productPrice = document.createElement("p")
    productPrice.id = "price"
    //Pizzas have undefined description
    if (productObject.desc === undefined) {
        let descriptionAndPrice = getPizzaDescriptionPrice(productObject.toppings)
        productDescription.textContent = descriptionAndPrice.desc;
        productPrice.textContent = "$"+descriptionAndPrice.price
    } else {
        productDescription.textContent = productObject.desc;
        productPrice.textContent = "$" + productObject.price.toString()
    }

    product.appendChild(product_name);
    product.appendChild(product_img);
    product.appendChild(productDescription);

    let cartImg = document.createElement("img")
    cartImg.src = "/static/img/CartPhoto.png"
    if (menuData.active_offer === 1) {
        let cartButton = document.createElement("button")
        console.log("lol")
        cartButton.setAttribute("onclick", "set3For2Pizza("+productObject.id+",'"+productObject.name+"')");
        cartButton.id = "addToCart";
        cartButton.appendChild(cartImg);
        product.appendChild(cartButton);
    } else {
        let cartButton = document.createElement("a")
        cartButton.href = carturl+productObject.id.toString();
        cartButton.id = "addToCart";
        cartButton.appendChild(cartImg);
        product.appendChild(cartButton);
    }

    product.appendChild(productPrice);
    return product;
}

const updateMenu = async () => {
    const menuInfo = [
        {
            key: "pizzas",
            title: "Sewer Pizzas",
            containerClass: "pizza_list_container",
            cartURL: "/cart/0/",
        },
        {
            key: "sides",
            title: "Sewer Sides",
            containerClass: "side_list_container",
            cartURL: "/cart/1/",
        },
        {
            key: "drinks",
            title: "Drinks",
            containerClass: "drink_list_container",
            cartURL: "/cart/2/",
        },
        {
            key: "user_pizzas",
            title: "Saved Pizzas",
            containerClass: "user_pizza_list_container",
            cartURL: "/cart/0/",
        },
    ]
    let menuContainer = document.getElementById("menu_container");
    menuContainer.innerHTML = '';
    let search_filter = document.getElementById("search_menu_input").value;

    // Using the list to set the order of action
    menuInfo.forEach(menuType => {
        if (menuData[menuType.key].length > 0 && activeMap[menuType.key]) {
            let menuTypeContainer = document.createElement("div");
            let titleContainer = document.createElement("div");
            let title = document.createElement("h1");
            let menuList = document.createElement("ul");
            menuTypeContainer.classList.add(menuType.containerClass)
            titleContainer.classList.add("title");
            title.textContent = menuType.title;
            menuList.classList.add("menu_list");
            menuData[menuType.key].forEach(product => {
                if (search_filter.length > 0) {
                    if (product.name.toLowerCase().startsWith(search_filter.toLowerCase())) {
                        menuList.appendChild(getProductElement(product))
                    }
                } else {
                    menuList.appendChild(getProductElement(product, menuType.cartURL));
                }
            })
            titleContainer.appendChild(title);
            menuTypeContainer.appendChild(titleContainer);
            menuTypeContainer.appendChild(menuList);
            menuContainer.appendChild(menuTypeContainer);
            }
    })
};

const setFilter = async (key) => {
    activeMap.pizzas = false
    activeMap.sides = false
    activeMap.drinks = false
    activeMap.user_pizzas = false
    activeMap[key] = true
    await updateMenu();
}

const set3For2Pizza = async (id, name) => {
    let pizzaElementIds = ["pizza_1", "pizza_2", "pizza_3"]
    console.log(document.getElementById("pizza_1").textContent)
    for (let i = 0; i < offer_3_for_2.length; i++) {
        if (offer_3_for_2[i] == null) {
            offer_3_for_2[i] = id;
            let pizzaElement = document.getElementById(pizzaElementIds[i]);
            pizzaElement.innerHTML = "";
            let pizzaName = document.createElement("p");
            pizzaName.textContent = name;
            pizzaName.classList.add("selected_pizza");
            pizzaElement.appendChild(pizzaName);
            break;
        }
    }
    if (!(offer_3_for_2[2] === null)) {
        let button = document.getElementById("save_offer_button_inactive");
        button.id = "save_offer_button_active"
        button.href = "/cart/"+offer_3_for_2[0].toString()+"/"+offer_3_for_2[1].toString()+"/"+offer_3_for_2[2].toString();
    }
}