let updateBtns = document.getElementsByClassName('update-cart')

for(let i = 0; i < updateBtns.length; i++ ){
    updateBtns[i].addEventListener('click', function(){
        let productID = this.dataset.product
        let action = this.dataset.action
        console.log('productID:', productID, 'action:', action) 

        console.log('USER', user)

        if (user === 'AnonymousUser'){
            console.log('Not logged in')

        }else{
            console.log('User logged in, sending data...')
        }
    })
}