let image = document.getElementById('image')

let height = image.offsetHeight
let width = image.offsetWidth

let n_h = height / 100 * 5
let n_w = width / 100 * 5

let all_tiles = 0
let count_tiles = [0, 0, 0, 0, 0, 0, 0]
let clicked_tiles = [0, 0, 0, 0, 0, 0, 0]

let default_color = 1
let rgb_t = document.getElementsByClassName('color')[0].style.color
let rgb_b = document.getElementsByClassName('color')[0].style.background

for (let i = 0; i < height / n_h; i++){
    for(let j = 0; j < width / n_w; j++)
    {
        let rnd = getRandomInt(1, 8)
        count_tiles[rnd - 1] += 1
        image.insertAdjacentHTML("beforeend", `<div class='tile' style='top: ${i*n_h}px; left: ${j*n_w}px; height: ${n_h}px; width: ${n_w}px;' onclick="check_tile(this)">${rnd}</div>`)
    }
}

function check_tile(el){
    if (default_color == el.textContent && el.style.background != rgb_b){
        el.style.background = rgb_b
        el.style.color = rgb_t
        all_tiles += 1
        clicked_tiles[parseInt(el.textContent, 10) - 1] += 1
    }
    let tiles = document.getElementsByClassName('tile')
    let color_palletee = document.getElementsByClassName('color')
    for (let i = 0; i < 7; i++){
        if (clicked_tiles[i] == count_tiles[i] && el.textContent == i+1 && el.style.background == rgb_b){
            for(let j = 0; j < 400; j++){
                if (tiles[j].textContent == el.textContent)
                {
                    tiles[j].style.transform = 'scale(5)'
                    tiles[j].style.opacity = 0
                } 
            }
            if (color_palletee[i].textContent == el.textContent){
                color_palletee[i].style.display = 'none'
            }
        }
    }
    if (all_tiles == 400){
        document.getElementsByClassName('download-btn')[0].style.display = 'block'
    }
}

function change_color(el){
    let elements = document.getElementsByClassName('color')
    for (let i = 0; i < elements.length; i++){
        elements[i].style.boxShadow = "0 0 0 0px #fff"
    }
    el.style.boxShadow = "0 0 0 5px #fff"
    default_color = el.textContent
    rgb_t = el.style.color
    rgb_b = el.style.background
    let tiles = document.getElementsByClassName('tile')
    for(let j = 0; j < 400; j++){
        tiles[j].style.transform = 'scale(1)'
    }
}

function getRandomInt(min, max) {
    const minCeiled = Math.ceil(min);
    const maxFloored = Math.floor(max);
    return Math.floor(Math.random() * (maxFloored - minCeiled) + minCeiled);
}