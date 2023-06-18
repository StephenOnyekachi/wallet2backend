// for copying text
const copyBtns = [...document.getElementsByClassName('copy-btn')]
console.log(copyBtns)

let previous = null

copyBtns.forEach(btn=> btn.addEventListener('click', ()=>{
    console.log('click')
    const color = btn.getAttribute('data-hex')
    console.log(color)
    navigator.clipboard.writeText(color)
    btn.textContent = 'Copied'
    btn.style.color = "gold";

    // navigator.clipboard.readText().then(clipText=>{
    //     console.log(clipText)
    //     btn.textContent = `copied ${clipText}`
    // })

    if (previous){
        previous.textContent = 'click'
    }
    previous = btn
}))