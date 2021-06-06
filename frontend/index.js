//BUTTONS
const buttonvisual = document.querySelector("#vbutton");
const buttonplan = document.querySelector("#pbutton");
const buttonstats = document.querySelector("#sbutton");

let onpage = buttonvisual

//PAGES
const visualize = document.querySelector("#one");
const plan = document.querySelector("#two");
const stats = document.querySelector("#three");

const setup = () => {
    console.log("Staring Up!")
    visualize.classList.remove("hide");
    plan.classList.add("hide");
    stats.classList.add("hide");
    buttonvisual.classList.add("selected")
}

//API CALLS
const apitest = (data) => {
    console.log(data);
    console.log(data[0]);
    console.log(data[0].height);


}

const getGraph = (graphnumber, specie) =>{
    let url = "http://127.0.0.1:8000/graph" + graphnumber + "/" + specie;
    fetch(url).then((response) => {console.log(response); return response.json()}).then((data) => {apitest(data);});
}

// getGraph(2,1);

let species = []

const getspecies = fetch("http://127.0.0.1:8000/species").then((response) => {console.log(response); return response.json()}).then((data) => {
    for(let i = 0; i < data.length; i++){

        species[i] = data[i][i+1];
    }
});

const changeLabels = (button) => {
    onpage.classList.remove("selected");
    button.classList.add("selected");
    onpage = button;
}

buttonvisual.addEventListener("click", (e) => {

    visualize.classList.remove("hide");
    plan.classList.add("hide");
    stats.classList.add("hide");
    changeLabels(buttonvisual);
});

buttonplan.addEventListener("click", (e) => {

 
    plan.classList.remove("hide");
    visualize.classList.add("hide");
    stats.classList.add("hide");
    changeLabels(buttonplan);
});

buttonstats.addEventListener("click", (e) => {


    stats.classList.remove("hide");
    visualize.classList.add("hide");
    plan.classList.add("hide");
    changeLabels(buttonstats);
})

