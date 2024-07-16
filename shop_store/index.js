window.addEventListener("load", async function(event){
    let responsepraduct= await this.fetch("http://localhost:8000/api/products")
    let resdata = await responsepraduct.json()
    let product_list = document.querySelector("#product_list")
    for (product of resdata){
        product_list.innerHTML += `
        <div class="card" style="width: 18rem;">
            <img src="${product.image}" class="card-img-top" alt="...">
            <div class="card-body">
                <h5 class="card-title">${product.title}</h5>
                <h5 class="card-price">${product.price} $</h5>
                <p class="card-text">${product.Description}</p>
                <a href="#" class="btn btn-primary">Go somewhere</a>
            </div>
        </div>
        `
    }
})