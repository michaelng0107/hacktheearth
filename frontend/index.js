//BUTTONS
const buttonvisual = document.querySelector("#vbutton");
const buttonplan = document.querySelector("#pbutton");
const buttonstats = document.querySelector("#sbutton");

//PAGES
const visualize = document.querySelector("#one");
const plan = document.querySelector("#two");
const stats = document.querySelector("#three");

const setup = () => {
    console.log("Staring Up!")
    visualize.classList.remove("hide");
    plan.classList.add("hide");
    stats.classList.add("hide")
}

//API CALLS
const chart = window.chart;

const request = fetch("http://127.0.0.1:8000/test/").then((response) => {console.log(response); return response.json()}).then((data) => {console.log(data);});

buttonvisual.addEventListener("click", (e) => {
    console.log("HIII");
    visualize.classList.remove("hide");
    plan.classList.add("hide");
    stats.classList.add("hide")
});

buttonplan.addEventListener("click", (e) => {
    console.log("HIII")
    plan.classList.remove("hide");
    visualize.classList.add("hide");
    stats.classList.add("hide")
});

buttonstats.addEventListener("click", (e) => {
    console.log("HIII")
    stats.classList.remove("hide");
    visualize.classList.add("hide");
    plan.classList.add("hide")
})

