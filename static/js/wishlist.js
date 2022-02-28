let updatebtns = document.getElementsByClassName('wishlist')

for(let i = 0; i < updatebtns.length; i++ ){
    updatebtns[i].addEventListener('click', function(e){
        e.preventDefault; 
        let productID = this.dataset.product
        let action = this.dataset.action
        console.log('productID:', productID, 'action:', action) 

        console.log('USER', user)

        if (user === 'AnonymousUser'){
            console.log('Not logged in')

        }else{
            updateUserOrder(productID, action)
        }
    })
}

function updateUserOrder(productID, action){
    console.log('User logged in, sending data...')

    var url = 'wishlist/'; 
    fetch(url, {
        method: 'POST',
        headers:{
            'Content-Type': 'application/json',
            'X-CSRFToken' : csrftoken,
        },
        body: JSON.stringify({'productID': productID, 'action': action})
    })

    .then((response) =>{
        return response.json()
    })
    .then((data) =>{
        console.log('data:', data)
        location.reload()
    })
}
